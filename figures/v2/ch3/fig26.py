#!/usr/bin/env python3
"""Chapter 3, Figure 26: drag coefficient of (a) circular cylinders and (b) spheres against R_D = U D / nu.

Average experimental curves (the caption; after Schlichting, ref. 15): the book has no equation for them, so
they are digitized from figures/ch3/fig26.png. The 1973 "log" paper is not logarithmic between decades (its
rulings 1, 1.5, 2, 2.5, 3, 3.5, 4, 5 ... 9 per decade sit at 0, 0.25, 0.43 ... of the decade: standing rule 3 of
corrections/v2-figures.md), so each traced pixel is read against the drawn gridlines, not a log fit: R_D by
interpolating log10 R_D between the two neighbouring vertical rulings at their printed values, C_D linearly
between the two neighbouring 0.2 rulings. The horizontal rulings run about 4 px lower at the right than at the
left (the scan is sheared), so each is fitted as a straight line and read at the traced column. Gridline
positions: fig26.calib.json (xgrid, ygrid at the panel's left edge; the slope below).

The curve is followed column by column (row by row down the steep drops), with the gridlines masked and the
crossings bridged; where it runs along a ruling (panel (b) at C_D = 0.4) the ruling itself is taken. Read
against the rulings, the path is smoothed on the true log axes (smooth_path: about 0.6 px of the scan), the
sharp corners kept as drawn (the cylinder's at the foot of its drop, the sphere's at the top of its drop). Writes
fig26-a.csv and fig26-b.csv (R, CD), replotted on true log axes in fig26.tex.
"""
import json
import pathlib
import numpy as np
from PIL import Image
from scipy.interpolate import UnivariateSpline

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent.parent
spec = json.loads((HERE / "fig26.calib.json").read_text())
gray = np.asarray(Image.open(ROOT / spec["crop"]).convert("L"))
ink = gray < 128
H, W = ink.shape


class Panel:
    def __init__(self, key, slope):
        ax = spec["axes"][key]
        self.xg = np.array(ax["xgrid"], float)             # [column, R] of each vertical ruling
        self.yg = np.array(ax["ygrid"], float)             # [row at the panel's left edge, C_D]
        self.slope = slope                                 # rows per column of the horizontal rulings
        self.c0 = self.xg[0, 0]
        # the horizontal rulings' rows at the left edge, refitted on the scan with the common slope
        rows = []
        for r, _ in self.yg:
            cs, rs = [], []
            for c in range(int(self.xg[0, 0]) + 3, int(self.xg[-1, 0]) - 3):
                if np.min(np.abs(self.xg[:, 0] - c)) < 3:
                    continue
                rr = r + slope * (c - self.c0)
                lo = int(round(rr)) - 4
                idx = np.flatnonzero(ink[lo:lo + 9, c])
                if 1 <= idx.size <= 6 and np.ptp(idx) <= 5:
                    cs.append(c); rs.append(lo + idx.mean() - slope * (c - self.c0))
            rows.append(np.median(rs))
        self.yg[:, 0] = rows
        self.top = self.yg[:, 0].min() - 3
        self.bottom = self.yg[:, 0].max() + 3

    def hrow(self, i, c):
        return self.yg[i, 0] + self.slope * (c - self.c0)

    def to_data(self, px, py):
        lx = np.interp(px, self.xg[:, 0], np.log10(self.xg[:, 1]))
        y = np.empty_like(py)
        for k, (c, r) in enumerate(zip(px, py)):
            rows = self.yg[:, 0] + self.slope * (c - self.c0)
            o = np.argsort(rows)
            y[k] = np.interp(r, rows[o], self.yg[o, 1])
        return 10 ** lx, y

    def mask(self):
        """The ink with the rulings removed (2 px either side of each)."""
        m = ink.copy()
        cols = np.arange(W)
        for i in range(len(self.yg)):
            rr = self.hrow(i, cols)
            for c in cols:
                lo = int(round(rr[c])) - 2
                if 0 <= lo < H:
                    m[lo:lo + 5, c] = False
        for c, _ in self.xg:
            m[:, int(round(c)) - 2:int(round(c)) + 3] = False
        return m


def runs(v, off=0, maxlen=7):
    idx = np.flatnonzero(v)
    if idx.size == 0:
        return []
    cut = np.flatnonzero(np.diff(idx) > 1)
    s, e = np.r_[idx[0], idx[cut + 1]], np.r_[idx[cut], idx[-1]]
    return [off + (a + b) / 2 for a, b in zip(s, e) if b - a + 1 <= maxlen]


def trace(panel, clean, seed, stop, mode="cols", max_jump=2.5, max_gap=24, on_rulings=False):
    """Follow the curve from seed (col, row) to the column (cols) or row (rows) `stop`. With on_rulings, where
    the masked ink has no continuation and a horizontal ruling lies within 3.5 px of the prediction, the curve
    is taken to run along that ruling (or, where the merged ink spreads past the ruling on one side, a half
line-width inside that edge)."""
    pts, slope = [], 0.0
    u, v = (seed[0], seed[1]) if mode == "cols" else (seed[1], seed[0])
    u = int(round(u)); step = 1 if stop > u else -1
    last = u; pts.append((u, v)); onrule = False
    u += step
    while (u - stop) * step <= 0:
        gap = abs(u - last)
        pred = pts[-1][1] + slope * (u - last)
        # leaving a ruling, the curve first shows 2-4 px from it (the mask hides the nearer ink)
        jump = 4.5 if onrule else max_jump * max(1.0, gap / 2)
        if mode == "cols":
            c = runs(clean[int(panel.top):int(panel.bottom), u], int(panel.top))
        else:
            c = runs(clean[u, :], 0)
        best = min(c, key=lambda r: abs(r - pred)) if c else None
        if best is not None and abs(best - pred) <= jump:
            new = (best - pts[-1][1]) / (u - last)
            slope = 0.0 if onrule else (new if len(pts) < 2 else 0.6 * slope + 0.4 * new)
            pts.append((u, best)); last = u; onrule = False
        elif on_rulings and mode == "cols":
            rows = [panel.hrow(i, u) for i in range(len(panel.yg))]
            near = min(rows, key=lambda r: abs(r - pred))
            if abs(near - pred) <= 3.5:
                # the curve merges with the ruling: where the merged ink reaches past the ruling's own
                # half-width on one side, the curve's centre is a half line-width inside that edge
                lo = int(round(near)) - 6
                col = ink[lo:lo + 13, u]
                idx = np.flatnonzero(col)
                hit = near
                if np.any(np.abs(panel.xg[:, 0] - u) < 3.5):
                    hit = None                      # a vertical ruling crosses here too: leave a gap
                elif idx.size and np.min(np.abs(np.arange(lo, lo + 13)[idx] - near)) <= 1.5:
                    # the run that holds the ruling
                    rr = np.arange(lo, lo + 13)[idx]
                    k = np.argmin(np.abs(rr - near))
                    a = b = k
                    while a > 0 and rr[a - 1] == rr[a] - 1: a -= 1
                    while b < len(rr) - 1 and rr[b + 1] == rr[b] + 1: b += 1
                    top, bot = rr[a], rr[b]
                    if bot - near > 1.2: hit = bot - 0.8
                    elif near - top > 1.2: hit = top + 0.8
                if hit is not None:
                    pts.append((u, hit)); slope = 0.0; last = u; onrule = True
        if abs(u - last) > max_gap:
            break
        u += step
    a = np.array(pts, float)
    if mode == "rows" and len(a) > 9:
        # the drops cross a ruling every few rows, and the mask makes the column jump where it does: a
        # moving average of 9 rows (the row step is 1, so the curve's run of columns is smoothed in place)
        k = np.ones(9) / 9
        a[4:-4, 1] = np.convolve(a[:, 1], k, mode="valid")
    return a if mode == "cols" else a[:, ::-1]


# the redraw's scales (fig26.tex): inches per decade of R_D and per unit of C_D
XS, YS = 5.2 / 3, 1.75


def smooth_path(panel, pts, sigma=0.008, pin_end=False, pin_start=False):
    """Read a traced path (pixels, in drawing order) against the rulings, then smooth it as x and y splines of
    its arc length on the redraw's true log axes (sigma in inches; 0.008 in is about 0.6 px of the scan). The
    smoothing comes after the reading: on the 1973 paper the scale jumps at each ruling (the "2" ruling sits at
    0.43 of the decade), so a curve smooth on the paper is kinked on true log axes until smoothed there. With
    pin_end (pin_start) the last (first) point, a sharp corner, is held by weight. Returns log10 R_D, C_D."""
    R, CD = panel.to_data(pts[:, 0].copy(), pts[:, 1].copy())
    P = np.c_[np.log10(R) * XS, CD * YS]
    d = np.r_[0.0, np.cumsum(np.hypot(*np.diff(P, axis=0).T))]
    keep = np.r_[True, np.diff(d) > 1e-9]
    P, d = P[keep], d[keep]
    w = np.ones(len(d))
    if pin_end:
        w[-1] = 30.0
    if pin_start:
        w[0] = 30.0
    sx = UnivariateSpline(d, P[:, 0], w=w, k=3, s=len(d) * sigma ** 2)
    sy = UnivariateSpline(d, P[:, 1], w=w, k=3, s=len(d) * sigma ** 2)
    t = np.linspace(0, d[-1], int(d[-1] / 0.004) + 2)
    return sx(t) / XS, sy(t) / YS


def to_frame(panel, path, start=False, end=False):
    """Continue a traced path (pixels, left to right) to the frame (the 10^3 and 10^6 rulings, where the trace
    stops a few pixels short behind them) along a straight line fitted to its first or last 16 columns."""
    if start:
        seg = path[path[:, 0] <= path[0, 0] + 16]
        k, b = np.polyfit(seg[:, 0], seg[:, 1], 1)
        xs = np.arange(panel.xg[0, 0], path[0, 0] - 0.5, 1.0)
        path = np.vstack([np.c_[xs, k * xs + b], path])
    if end:
        seg = path[path[:, 0] >= path[-1, 0] - 16]
        k, b = np.polyfit(seg[:, 0], seg[:, 1], 1)
        xs = np.arange(path[-1, 0] + 1.0, panel.xg[-1, 0] + 0.5, 1.0)
        path = np.vstack([path, np.c_[xs, k * xs + b]])
    return path


def finish(panel, gentle, drop, tail, name, corners):
    """Join the parts of a curve in drawing order, smooth them (smooth_path) and write R, C_D.

    The path runs from 10^3 through the pieces traced column by column (gentle), the drop traced row by row and
    the recovery (tail), continued to the frame at both ends (to_frame). A sharp corner of the drawing is kept:
    corners = "foot" (the cylinder: the drop ends in a point) or "top" (the sphere: the curve meets the 0.4 ruling
    and turns down at once; its foot is rounded); the path is smoothed in two parts that meet at the corner."""
    g = np.vstack(gentle)
    g = g[np.argsort(g[:, 0], kind="stable")]
    g = g[g[:, 0] < drop[:, 0].min() - 0.5]
    t = np.vstack(tail)
    t = t[np.argsort(t[:, 0], kind="stable")]
    t = t[t[:, 0] > drop[:, 0].max() + 0.5]
    g = to_frame(panel, g, start=True)
    t = to_frame(panel, t, end=True)
    if corners == "foot":
        first, second = np.vstack([g, drop]), np.vstack([drop[-1:], t])
    else:
        first, second = np.vstack([g, drop[:1]]), np.vstack([drop, t])
    x1, y1 = smooth_path(panel, first, pin_end=True)
    x2, y2 = smooth_path(panel, second, pin_start=True)
    # meet exactly at the corner
    w = np.exp(-np.hypot((x2 - x2[0]) * XS, (y2 - y2[0]) * YS) / 0.01)
    x2, y2 = x2 + (x1[-1] - x2[0]) * w, y2 + (y1[-1] - y2[0]) * w
    gx, gy = np.r_[x1, x2[1:]], np.r_[y1, y2[1:]]
    gx[0], gx[-1] = 3.0, 6.0
    rows = ["R,CD"] + [f"{10 ** x:.5g},{y:.4f}" for x, y in zip(gx, gy)]
    (HERE / name).write_text("\n".join(rows) + "\n")
    print(f"{name}: {len(gx)} points; C_D {gy.min():.3f} .. {gy.max():.3f}; R {10 ** gx[0]:.4g} .. {10 ** gx[-1]:.4g}")


# (a) circular cylinder: the plateau and peak column by column, the drop row by row, the recovery
pa = Panel("a", slope=0.0090)
ca = pa.mask()
a1 = trace(pa, ca, (136, 117.5), 92, on_rulings=True)          # back to R_D = 10^3 (ends on the 1.0 ruling)
a2 = trace(pa, ca, (136, 117.5), 468, on_rulings=True)         # plateau, peak (on the 1.2 ruling), the shoulder
a3 = trace(pa, ca, (470, 88.0), 272, mode="rows", max_gap=40)   # the drop
a4 = trace(pa, ca, (514, 272.0), 545)                          # recovery to 10^6
a5 = trace(pa, ca, (514, 272.0), 503)                          # back into the corner at the foot
finish(pa, [a1, a2], a3, [a4, a5], "fig26-a.csv", corners="foot")

# (b) sphere
pb = Panel("b", slope=0.0084)
cb = pb.mask()
b1 = trace(pb, cb, (110, 569.5), 91, on_rulings=True)
b2 = trace(pb, cb, (110, 569.5), 474, on_rulings=True)         # along the 0.4 ruling, the hump, to the drop
b3 = trace(pb, cb, (476, 582.5), 648, mode="rows", max_gap=40)  # the drop (behind the 3 x 10^5 ruling)
b4 = trace(pb, cb, (503, 650.5), 546)                          # recovery to 10^6
b5 = trace(pb, cb, (503, 650.5), 486)                          # back into the corner at the foot
finish(pb, [b1, b2], b3, [b4, b5], "fig26-b.csv", corners="top")
