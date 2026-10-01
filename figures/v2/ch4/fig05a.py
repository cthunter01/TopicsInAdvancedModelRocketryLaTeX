#!/usr/bin/env python3
"""Chapter 4, Figure 5(a): percent error in v_b of the approximate methods, B14 engine (digitized).

The book does not give the B14 thrust curve or the propellant mass its "exact" interval solution used
(ch4-sec2b.tex:308-320: "variable mass-time and thrust-time functions" on an IBM 360/65), and a triangle fitted
to Figure 10 does not reproduce the printed errors (inventory row ch4-fig05a), so the four printed curves of
each Figure 5 panel are digitized from the 1973 art, figures/ch4/fig05a.png (rule: compute else digitize,
corrections/v2-figures.md "Ch4 Figs 5, 7-10, 12-14"). The legend, the k_max/k_min labels and their leaders
are the template's (fig06a.tex); the methods are eqs. (20), (21) (Fehskens-Malewicki) and (27), (28)
(Caporaso-Bengen) against the interval method (83)-(87), k_min = .00005 and k_max = .002 kg/m (key table).

Method. Calibration fig05a.calib.json: piecewise linear between the drawn ticks (x: the 13 ticks .02-.14 on
the bottom axis; y: the 7 ticks -15..15), continued linearly beyond the end ticks. The labels, the legend
and the four leaders are masked out of the ink. Each curve is followed column by column: a hand-read guide
(GUIDE below, pixel points every 10-50 px, read from 5x zooms) predicts its row, and the ink run nearest the
prediction within 2.5 px is taken. Where
the curve shares a run with a neighbour (the zero line, a curve it merges into), the run's edge on the
curve's side is used, less half a line width; inside a bundle (both edges taken by other lines) the guide is
kept. The samples are smoothed with a parametric smoothing spline in chord length (lam = 3e4 px^3: the
pixel steps and the merges go, the bends stay), run into the axis at m_o = 0.02 kg (the engine-alone mass,
where the printed curves start; the hand-drawn y axis leans a few pixels) and to 0.14 kg, and written in
data coordinates every 0.0005 kg. A curve that leaves the top of the frame is written up to just above 15%
and as nan beyond (the plot clips it at 15).

Writes fig05a.csv: m0, fm_kmin, cb_kmin, fm_kmax, cb_kmax (percent).
This module also holds the helpers that fig05b.py and fig05c.py import (`Scan`, `curve`, `write`).
"""
import json
import pathlib
import numpy as np
from PIL import Image
from scipy.interpolate import make_smoothing_spline

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent.parent
COLS = ("fm_kmin", "cb_kmin", "fm_kmax", "cb_kmax")


def extrap(v, grid):
    """np.interp through the (pixel, value) pairs of `grid`, continued linearly beyond its ends."""
    g = grid[np.argsort(grid[:, 0])]
    v = np.asarray(v, float)
    out = np.interp(v, g[:, 0], g[:, 1])
    for sel, (a, b) in ((v < g[0, 0], (g[0], g[1])), (v > g[-1, 0], (g[-2], g[-1]))):
        out[sel] = a[1] + (v[sel] - a[0]) * (b[1] - a[1]) / (b[0] - a[0])
    return out


class Scan:
    """The crop's ink (dark < `dark`) and the piecewise-linear calibration of <name>.calib.json."""

    def __init__(self, name, dark=150):
        spec = json.loads((HERE / f"{name}.calib.json").read_text())
        ax = spec["axes"]["main"]
        self.xg = np.array(ax["xgrid"], float)
        self.yg = np.array(sorted(ax["ygrid"]), float)
        img = np.asarray(Image.open(ROOT / spec["crop"]).convert("L"))
        self.ink = img < dark
        self.rr, self.cc = np.mgrid[0:img.shape[0], 0:img.shape[1]]

    def mask_box(self, c0, r0, c1, r1):
        self.ink[r0:r1 + 1, c0:c1 + 1] = False

    def mask_line(self, p0, p1, r=1.8):
        (x0, y0), (x1, y1) = p0, p1
        t = np.clip(((self.cc - x0) * (x1 - x0) + (self.rr - y0) * (y1 - y0))
                    / ((x1 - x0) ** 2 + (y1 - y0) ** 2), 0, 1)
        self.ink &= np.hypot(self.cc - (x0 + t * (x1 - x0)), self.rr - (y0 + t * (y1 - y0))) > r

    def to_data(self, px, py):
        """Pixels -> data, piecewise linear between the ticks and linear beyond the end ticks along the end
        intervals (no clamping: ink left of the .02 tick, where a hand-drawn y axis leans out, keeps its own
        x, so the smoothing spline does not sag over samples collapsed onto one abscissa)."""
        return extrap(px, self.xg), extrap(py, self.yg)

    def runs(self, c, lo, hi):
        v = self.ink[lo:hi + 1, c]
        idx = np.flatnonzero(v)
        if idx.size == 0:
            return []
        cut = np.flatnonzero(np.diff(idx) > 1)
        return [(s + lo, e + lo) for s, e in zip(np.r_[idx[0], idx[cut + 1]], np.r_[idx[cut], idx[-1]])]

    def follow(self, guide, tol=2.5, w=2.5, wmax=4.5):
        """Samples (px, py) of the curve along the guide polyline (pixel points, increasing columns).
        A run no longer than wmax (+ the guide's slope) is one line: its centre. A longer run is a bundle:
        the edge on the guide's side less w/2, or the guide itself when it lies inside."""
        g = np.array(guide, float)
        pts = []
        for c in range(int(np.ceil(g[0, 0])), int(np.floor(g[-1, 0])) + 1):
            k = min(max(np.searchsorted(g[:, 0], c), 1), len(g) - 1)
            slope = (g[k, 1] - g[k - 1, 1]) / (g[k, 0] - g[k - 1, 0])
            pred = np.interp(c, g[:, 0], g[:, 1])
            best = None
            for s, e in self.runs(c, int(pred - tol - 12), int(pred + tol + 12)):
                if e - s + 1 <= wmax + abs(slope):
                    y = (s + e) / 2
                elif pred < s + w / 2:
                    y = s + (w - 1) / 2
                elif pred > e - w / 2:
                    y = e - (w - 1) / 2
                else:
                    y = pred
                if abs(y - pred) <= tol and (best is None or abs(y - pred) < abs(best - pred)):
                    best = y
            if best is not None:
                pts.append((c, best))
        return np.array(pts, float)


def smooth(p, lam, w=None):
    """Parametric smoothing spline in chord length through the samples p (N x 2), with sample weights w
    (default all 1); returns 600 samples."""
    s = np.r_[0, np.cumsum(np.hypot(*np.diff(p, axis=0).T))]
    keep = np.r_[True, np.diff(s) > 1e-6]
    p, s = p[keep], s[keep]
    w = None if w is None else np.asarray(w, float)[keep]
    t = np.linspace(0, s[-1], 600)
    return np.c_[make_smoothing_spline(s, p[:, 0], w=w, lam=lam)(t),
                 make_smoothing_spline(s, p[:, 1], w=w, lam=lam)(t)]


def curve(scan, pts, lam=3e4, x0=0.02, x1=0.14, top=15.6, nfit=6, w0=None, label=""):
    """Smoothed samples -> (x, y) in data units on the grid x0..x1 step 0.0005, NaN above `top`. The ends
    are run into x0 and x1 along the slope of the last `nfit` smoothed pixels' worth of curve. w0 = (n, w)
    weights the first n samples by w (default none): the spline's natural end has no curvature, so where a
    curve bends sharply at the axis it would cut the bend and start low. Prints how far the traced samples
    lie from the smoothed curve (pixels)."""
    w = None
    if w0 is not None:
        w = np.ones(len(pts))
        w[:w0[0]] = w0[1]
    sp = smooth(pts, lam, w)
    dist = np.min(np.hypot(pts[:, None, 0] - sp[None, :, 0], pts[:, None, 1] - sp[None, :, 1]), axis=1)
    print(f"  {label}: {len(pts)} samples, {pts[0, 0]:.0f}-{pts[-1, 0]:.0f} px; to the smoothed curve "
          f"95% {np.percentile(dist, 95):.2f} px, max {dist.max():.2f} px")
    x, y = scan.to_data(sp[:, 0], sp[:, 1])
    o = np.argsort(x)
    x, y = x[o], y[o]
    grid = np.round(np.arange(x0, x1 + 1e-9, 0.0005), 4)
    out = np.interp(grid, x, y)
    for end in (0, 1):                       # linear run-out beyond the traced ends
        sel = x <= x[0] + nfit * 2.6e-4 if end == 0 else x >= x[-1] - nfit * 2.6e-4
        a, b = np.polyfit(x[sel], y[sel], 1)
        beyond = grid < x[0] if end == 0 else grid > x[-1]
        out[beyond] = a * grid[beyond] + b
    out[out > top] = np.nan
    return grid, out


def write(name, grid, curves):
    rows = ["m0," + ",".join(COLS)]
    for i, m in enumerate(grid):
        rows.append(f"{m:.4f}," + ",".join("nan" if np.isnan(curves[c][i]) else f"{curves[c][i]:.3f}"
                                           for c in COLS))
    (HERE / f"{name}.csv").write_text("\n".join(rows) + "\n")
    for c in COLS:
        v = curves[c]
        sel = ~np.isnan(v)
        print(f"{name} {c}: {grid[sel][0]:.4f}-{grid[sel][-1]:.4f} kg, "
              + ", ".join(f"{np.interp(m, grid[sel], v[sel]):+.2f} at {m:.2f}" for m in (0.02, 0.04, 0.06, 0.10, 0.14)
                          if grid[sel][0] <= m))


# ---- Figure 5(a) -------------------------------------------------------------------------------------------
GUIDE = {
    # solid, from the top of the frame (y = 15 at row 16.5)
    "fm_kmax": [(114, 17), (120, 28.5), (130, 46.5), (140, 61.5), (150, 74.5), (160, 85.5), (170, 94),
                (180, 101), (200, 112), (220, 119), (250, 128), (300, 137), (350, 142.5), (400, 146),
                (450, 147.5), (500, 148.5), (520, 149)],
    # dashed, from the top of the frame, through the zero line at about .042, minimum -4.2 near .068
    "cb_kmax": [(90, 17), (92, 20), (96, 31), (100, 46), (104, 55.5), (110, 72.5), (116, 87.5), (120, 101.5),
                (124, 110), (128, 118), (132, 125.5), (136, 133), (140, 140.5), (144, 147.5), (148, 153),
                (152, 156.5), (156, 160.5), (160, 164), (164, 168), (168, 170.5), (172, 173.5), (176, 176),
                (182, 179), (190, 182.5), (200, 186), (220, 189), (250, 190.5), (280, 189.5), (300, 188.5),
                (330, 185), (350, 182.5), (380, 179), (400, 178), (450, 175), (500, 174.5), (520, 174.5)],
    # solid: +0.3 at the axis, across the zero line (row 152) to about -0.2 (row 154.5)
    "fm_kmin": [(74, 150), (80, 152), (90, 153.5), (100, 154.5), (150, 154.5), (250, 154.5), (350, 155),
                (450, 155), (520, 155)],
    # dashed: -3.3 at the axis rising to about -0.3, merging with fm_kmin at the right
    "cb_kmin": [(74, 182), (80, 179), (90, 175.5), (110, 170.5), (130, 166), (150, 163.5), (164, 161.5),
                (180, 160.5), (200, 159.5), (250, 157.5), (300, 156.5), (350, 155.5), (400, 155),
                (450, 155), (520, 155)],
}

if __name__ == "__main__":
    s = Scan("fig05a")
    s.ink[:, :74] = False                              # the y axis
    s.ink[286:, :] = False                             # the x axis
    s.mask_box(132, 97, 172, 117)                      # "k_max"
    s.mask_box(78, 184, 115, 203)                      # "k_min"
    s.mask_box(290, 218, 530, 262)                     # legend
    for a, b in (((151, 103), (159, 85)), ((145, 117), (137, 135)),     # k_max leaders
                 ((92, 189), (102, 155)), ((100, 188), (118, 168))):    # k_min leaders
        s.mask_line(a, b)
    out = {}
    for c in COLS:
        # fm_kmax runs into the zero line at the right: a 4-px run there is the pair, not the curve
        pts = s.follow(GUIDE[c], tol=2.5, wmax=4.5 if c in ("cb_kmin", "cb_kmax") else 3.5)
        grid, out[c] = curve(s, pts, label=c)
    write("fig05a", grid, out)
