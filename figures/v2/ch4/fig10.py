#!/usr/bin/env python3
"""Chapter 4, Figure 10: non-vertical trajectories for a 30 deg launch angle, B14 engine (scan:
figures/ch4/fig10.png). The three printed curves (a)-(c), DIGITIZED from the 1973 art.

Why digitized: the book's 2-D method (eqs. (106)-(115) with the launch-rod phase (125)-(131), dt = .001 s,
ch4-sec3.tex) would determine the curves, but the B14 engine model is incomplete: the book gives F_m = 28.6 N,
F_s = 0, t_s = t_b (ch4-sec2b.tex) and t_b = 0.35 s (caption), not t_m or the propellant mass
(corrections/v2-figures.md: Ch4 Figs 5, 7-10, 12-14 are digitized). The caption's burnout points (x_b, y_b =
23/40, 9/15, 3/5 m) are not drawn in the 1973 art and are not used.

Method (shared by fig12.py, fig13.py and fig14.py, which import this file):
  - the frame convention (one for Figs 10, 12, 13 and 14): x is read between the drawn x ticks, piecewise
    linearly, along lines parallel to the drawn y axis; y is the affine fit of the tick marks. Each 1973 frame is
    distorted as a whole, lettering included: the y axis leans against the x axis by 1.3, 0.8, 0.8 and 0.2 deg
    (Figs 10, 12, 13, 14), and the zeros of the lettering lean with it (shear dcol/drow of the zeros against the
    y axis: +0.015/+0.016, -0.018/-0.018, +0.010/+0.013, +0.008/+0.006; Fig 11, whose frame is square: -0.005/
    +0.002); the x ticks close up to the right in Figs 10, 13 and 14 (73.0 to 69.7, 76.8 to 70.1 and 96.5 to
    88.0 px per tick step) and the lettering narrows with them (Figs 13, 14). So neither the affine fit (which follows
    the lean but averages the ticks) nor a column-only x grid (which follows the ticks but not the lean) reads
    the curves as drawn. calibration <name>.calib.json: "points" (the tick marks set on the axis lines fitted
    through the ink: the y mapping), "xgrid" (the tick columns on the x axis line, extended by one step at both
    ends) and "lean" (the two fitted axis lines). tools/v2/digitize.py reads xgrid by column alone, so its overlay
    of these curves is off by the lean (up to 5 px at the top of a frame); the round trip is the check this script
    prints (the same measure as digitize.py overlay, with this mapping);
  - the axis lines (a band of 2.6 px round each fitted line) and the time leaders (each refitted as a straight
    line through its ink and erased from a point just off the curve), and any curve tag that crowds a curve,
    are erased from a darkness image of the scan;
  - each curve is followed from a seed on its descending branch, down to 6 px (3 px for a curve only a few
    pixels high) above the x axis, and up over the apex and back down the ascending branch to 3 px from the
    axes: a step of 1 px, the ink run nearest the prediction along the normal (runs wider than 7 px, i.e.
    crossings, are skipped), the direction and its turning rate smoothed. Tracing over the apex from the
    descending side leaves each apex leader behind the direction of travel;
  - the trace is smoothed (7-point moving average), extended at the foot along the straight line fitted to its
    last 10 points to the x axis line (the impact) and joined to the origin; a smoothing cubic spline (arc-length
    parameter, about 0.45 px rms from the trace, the two ends held) fairs it, so that the pixel steps of the scan
    do not show as kinks at the final size; resampled every 1.5 px of arc and mapped to data;
  - each curve tag is set 2.75 mm (at the final size, SPEC "scale" in per m) out along the normal of the
    descending branch at the height SPEC "tags" gives (where the 1973 tag stands); a curve with no height there
    has its tag placed in the .tex (nan in the marks).
Writes <name>-a.csv, <name>-b.csv, <name>-c.csv (x, y in m, launch to impact) and <name>-marks.csv (curve,
apex x and y, impact x: the points the printed time leaders touch, the apex being the curve's highest point; tag
x and y: the centre of the curve tag).
"""
import csv
import json
import pathlib
import sys

import numpy as np
from PIL import Image
from scipy import ndimage
from scipy.interpolate import splev, splprep

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent.parent
sys.path.insert(0, str(ROOT / "tools" / "v2"))
from digitize import Axes  # noqa: E402  (the calibration mapping of the overlay tool)

# Fig 10. Pixel coordinates of the crop (x = column, y = row); the axis lines are in fig10.calib.json ("lean").
# seeds: a pixel on the descending branch, the direction towards the impact and the direction towards the apex.
# erase: leaders (x1, y1, x2, y2), from just off the curve to the label. tags: the height (m) on the descending
# branch where each tag stands out; scale: the final size, in per m (fig10.tex).
SPEC = dict(
    name="fig10",
    seeds={"a": (400, 125, (0.3, 1), (-0.3, -1)),
           "b": (300, 214, (0.5, 1), (-0.5, -1)),
           "c": (130, 285, (0.4, 1), (-0.6, -1))},
    erase=[(319.7, 18.0, 318.5, 39),      # 6.80, below the apex of (a)
           (238.5, 153.5, 250, 139),      # 5.80
           (124.5, 275.5, 151, 257),      # 2.40
           (138, 295, 180, 283),          # 4.90
           (337, 293.5, 350, 283),        # 12.90
           (437, 294.5, 456, 279)],       # 18.25
    disks=[],
    margin={},
    tags={"a": 354.4, "b": 186.4, "c": 16.0},
    scale=0.007,
)


class FrameAxes:
    """The frame convention: x read between the drawn x ticks ("xgrid", piecewise linear) along lines parallel
    to the drawn y axis ("lean": the fitted axis lines, row = xaxis[0] col + xaxis[1], col = yaxis[0] row +
    yaxis[1]); y the affine fit of the tick marks ("points"), as in tools/v2/digitize.py."""

    def __init__(self, spec):
        self.ax = Axes(spec)
        self.grid = np.array(spec["xgrid"], float)
        self.xa = spec["lean"]["xaxis"]
        self.lean = spec["lean"]["yaxis"][0]

    def foot(self, px, py):
        """The column where the line through (px, py) parallel to the y axis meets the x axis line."""
        a, b = self.xa
        t = (a * px + b - py) / (1 - a * self.lean)
        return px + self.lean * t

    def to_data(self, px, py):
        px, py = np.asarray(px, float), np.asarray(py, float)
        _, y = self.ax.to_data(px, py)
        return np.interp(self.foot(px, py), self.grid[:, 0], self.grid[:, 1]), y

    def to_pixel(self, x, y):
        x, y = np.asarray(x, float), np.asarray(y, float)
        cf = np.interp(x, self.grid[:, 1], self.grid[:, 0])
        rf = self.xa[0] * cf + self.xa[1]
        A = self.ax.A                     # y = A[0, 1] col + A[1, 1] row + A[2, 1]
        y0 = A[0, 1] * cf + A[1, 1] * rf + A[2, 1]
        t = (y - y0) / (A[0, 1] * self.lean + A[1, 1])
        return cf + self.lean * t, rf + t


def darkness(gray):
    return np.clip((200.0 - gray) / 120.0, 0.0, 1.0)


def erase(dk, segs, disks, hw=1.8):
    """Erase each leader: refit it as the straight line through its ink (from 0.3 of its length on, away from the
    curve), then clear a band of half-width hw along it from the given start (just off the curve) to 3 px past its
    end; and clear each disk (cx, cy, r) (a curve tag)."""
    h, w = dk.shape
    rr, cc = np.mgrid[0:h, 0:w]
    for cx, cy, r in disks:
        dk[(cc - cx) ** 2 + (rr - cy) ** 2 <= r * r] = 0
    for x1, y1, x2, y2 in segs:
        u = np.array([x2 - x1, y2 - y1], float)
        length = np.hypot(*u)
        u /= length
        t = (cc - x1) * u[0] + (rr - y1) * u[1]
        nrm = np.abs(-(cc - x1) * u[1] + (rr - y1) * u[0])
        sel = (t >= 0.3 * length) & (t <= length) & (nrm <= 3.5) & (dk > 0.5)
        if sel.sum() > 5:
            pts = np.c_[cc[sel], rr[sel]].astype(float)
            wt = dk[sel]
            m = (pts * wt[:, None]).sum(0) / wt.sum()
            _, vec = np.linalg.eigh(np.cov((pts - m).T, aweights=wt))
            v = vec[:, 1] if vec[:, 1] @ u > 0 else -vec[:, 1]
            x1, y1 = m + ((np.array([x1, y1]) - m) @ v) * v
            u = v
            t = (cc - x1) * u[0] + (rr - y1) * u[1]
            nrm = np.abs(-(cc - x1) * u[1] + (rr - y1) * u[0])
        dk[(t >= 0) & (t <= length + 3) & (nrm <= hw)] = 0


def snap(dk, col, row, win=6):
    """The ink pixel nearest (col, row)."""
    col, row = int(round(col)), int(round(row))
    yy, xx = np.nonzero(dk[row - win:row + win + 1, col - win:col + win + 1] > 0.6)
    if not yy.size:
        raise SystemExit(f"no ink near {col},{row}")
    k = np.argmin((yy - win) ** 2 + (xx - win) ** 2)
    return np.array([col - win + xx[k], row - win + yy[k]], float)


def follow(dk, p0, d0, stop, step=1.0, w=3.5, alpha=0.3, beta=0.15, max_miss=10, thr=0.45, maxrun=7.0):
    """Follow a curve from p0 in the direction d0 until stop(p): at each step the ink run along the normal
    nearest the predicted point (runs wider than maxrun px skipped); direction and turning rate smoothed."""
    p = np.array(p0, float)
    d = np.array(d0, float) / np.hypot(*d0)
    pts, miss, kap = [p.copy()], 0, 0.0
    offs = np.arange(-w, w + 0.01, 0.25)
    for _ in range(20000):
        c, s = np.cos(kap), np.sin(kap)
        d = np.array([c * d[0] - s * d[1], s * d[0] + c * d[1]])
        q = p + step * d
        nrm = np.array([-d[1], d[0]])
        vals = ndimage.map_coordinates(dk, [q[1] + offs * nrm[1], q[0] + offs * nrm[0]], order=1, mode="constant")
        idx = np.flatnonzero(vals > thr)
        best = None
        if idx.size:
            cut = np.flatnonzero(np.diff(idx) > 1)
            for a, b in zip(np.r_[idx[0], idx[cut + 1]], np.r_[idx[cut], idx[-1]]):
                if (b - a) * 0.25 > maxrun:
                    continue
                o = (offs[a:b + 1] * vals[a:b + 1]).sum() / vals[a:b + 1].sum()
                if best is None or abs(o) < abs(best):
                    best = o
        if best is None:
            miss += 1
            if miss > max_miss:
                break
            p = q
            continue
        miss = 0
        new = q + best * nrm
        dn = (new - p) / np.hypot(*(new - p))
        nd = (1 - alpha) * d + alpha * dn
        nd /= np.hypot(*nd)
        kap += beta * np.arctan2(d[0] * nd[1] - d[1] * nd[0], d @ nd)
        d, p = nd, new
        pts.append(p.copy())
        if stop(p):
            break
    return np.array(pts)


def smooth(pts, n=7):
    k = np.ones(n) / n
    out = pts.copy()
    for j in range(2):
        out[:, j] = np.convolve(np.pad(pts[:, j], n // 2, mode="edge"), k, mode="valid")
    return out


def to_axis(pts, xa, n=10):
    """Extend the path along the line fitted to its last n points to the x axis line row = xa[0] col + xa[1]."""
    tail = pts[-n:]
    m = tail.mean(0)
    _, vec = np.linalg.eigh(np.cov((tail - m).T))
    v = vec[:, 1] if vec[:, 1] @ (tail[-1] - tail[0]) > 0 else -vec[:, 1]
    # m + s v on the line: m_y + s v_y = xa0 (m_x + s v_x) + xa1
    s = (xa[0] * m[0] + xa[1] - m[1]) / (v[1] - xa[0] * v[0])
    return m + s * v


def fair(pts, rms=0.45):
    """A smoothing parametric spline through the path (pixels), parametrized by arc length, within about rms px of
    the trace; its two ends (the origin and the foot) held."""
    seg = np.hypot(*np.diff(pts, axis=0).T)
    keep = np.r_[True, seg > 1e-6]
    pts = pts[keep]
    u = np.r_[0, np.cumsum(np.hypot(*np.diff(pts, axis=0).T))]
    wt = np.ones(len(pts))
    wt[[0, -1]] = 20.0
    tck, _ = splprep([pts[:, 0], pts[:, 1]], u=u, w=wt, s=len(pts) * rms ** 2, k=3)
    uu = np.linspace(0, u[-1], int(u[-1] * 4) + 2)
    return np.column_stack(splev(uu, tck))


def resample(pts, ds=1.5):
    seg = np.hypot(*np.diff(pts, axis=0).T)
    s = np.r_[0, np.cumsum(seg)]
    t = np.r_[np.arange(0, s[-1], ds), s[-1]]
    return np.c_[np.interp(t, s, pts[:, 0]), np.interp(t, s, pts[:, 1])]


def digitize(spec):
    calib = json.loads((HERE / f"{spec['name']}.calib.json").read_text())
    ax = FrameAxes(calib["axes"]["main"])
    gray = np.asarray(Image.open(ROOT / calib["crop"]).convert("L"), float)
    dk = darkness(gray)
    xa, ya = calib["axes"]["main"]["lean"]["xaxis"], calib["axes"]["main"]["lean"]["yaxis"]
    h, w = dk.shape
    rr, cc = np.mgrid[0:h, 0:w]
    dk[np.abs(rr - (xa[0] * cc + xa[1])) <= 2.6] = 0
    dk[np.abs(cc - (ya[0] * rr + ya[1])) <= 2.6] = 0
    erase(dk, spec["erase"], spec["disks"])
    near_origin = lambda p: p[1] > xa[0] * p[0] + xa[1] - 3.2 or p[0] < ya[0] * p[1] + ya[1] + 3.2
    curves, marks = {}, []
    for key, (col, row, d_down, d_up) in spec["seeds"].items():
        margin = spec["margin"].get(key, 6.0)
        s = snap(dk, col, row)
        down = follow(dk, s, d_down, lambda p: p[1] > xa[0] * p[0] + xa[1] - margin)
        up = follow(dk, s, d_up, near_origin)
        path = smooth(np.r_[up[::-1], down[1:]])
        foot = to_axis(path, xa)
        ox, oy = ax.to_pixel(np.array([0.0]), np.array([0.0]))
        path = np.r_[[[ox[0], oy[0]]], path, [foot]]
        rs = resample(fair(path))
        x, y = ax.to_data(rs[:, 0], rs[:, 1])
        x[0], y[0], y[-1] = 0.0, 0.0, 0.0
        curves[key] = np.c_[x, y]
        k = int(np.argmax(y))
        tg = tag(x, y, k, spec["tags"][key], spec["scale"]) if key in spec["tags"] else (np.nan, np.nan)
        marks.append((key, x[k], y[k], x[-1]) + tg)
    return curves, marks, ax, gray


def tag(x, y, k, height, scale, off=2.75):
    """The centre of a curve tag: off mm (at the final size, scale in per m) out along the normal of the
    descending branch (from the apex, index k, on) at the given height."""
    xd, yd = x[k:], y[k:]
    i = int(np.flatnonzero(yd <= height)[0])
    s = (yd[i - 1] - height) / (yd[i - 1] - yd[i])
    px, py = xd[i - 1] + s * (xd[i] - xd[i - 1]), height
    j = k + i
    tx, ty = x[j + 1] - x[j - 2], y[j + 1] - y[j - 2]
    n = np.array([-ty, tx]) / np.hypot(tx, ty)       # to the left of the direction of travel: outwards
    d = off / (scale * 25.4)
    return px + d * n[0], py + d * n[1]


def check(spec, curves, ax, gray):
    """The overlay check of tools/v2/digitize.py (distance from each point to the nearest ink of the scan, ink
    darker than 128) with the frame mapping: a round trip for a trace."""
    dist = ndimage.distance_transform_edt(~(gray < 128))
    h, w = gray.shape
    for key, xy in curves.items():
        px, py = ax.to_pixel(xy[:, 0], xy[:, 1])
        ok = (px >= 0) & (px < w - 1) & (py >= 0) & (py < h - 1)
        dv = dist[np.round(py[ok]).astype(int), np.round(px[ok]).astype(int)]
        print(f"{spec['name']} ({key}) overlay: distance to ink mean {dv.mean():.2f} px, 95% "
              f"{np.percentile(dv, 95):.2f} px, max {dv.max():.2f} px")


def write(spec, curves, marks):
    name = spec["name"]
    for key, xy in curves.items():
        with open(HERE / f"{name}-{key}.csv", "w", newline="") as f:
            wr = csv.writer(f)
            wr.writerow(["x", "y"])
            for x, y in xy:
                wr.writerow([f"{x:.2f}", f"{max(y, 0.0):.2f}"])
    with open(HERE / f"{name}-marks.csv", "w", newline="") as f:
        wr = csv.writer(f)
        wr.writerow(["curve", "apexx", "apexy", "impactx", "tagx", "tagy"])
        for key, ax_, ay_, ix, tx, ty in marks:
            wr.writerow([key, f"{ax_:.1f}", f"{ay_:.1f}", f"{ix:.1f}", f"{tx:.1f}", f"{ty:.1f}"])
    for key, ax_, ay_, ix, tx, ty in marks:
        print(f"{name} ({key}): {len(curves[key])} points; apex ({ax_:.0f}, {ay_:.0f}) m, impact {ix:.0f} m")


def main(spec):
    curves, marks, ax, gray = digitize(spec)
    write(spec, curves, marks)
    check(spec, curves, ax, gray)


if __name__ == "__main__":
    main(SPEC)
