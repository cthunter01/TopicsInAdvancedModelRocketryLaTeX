#!/usr/bin/env python3
"""Chapter 3, Figure 30: C_Do against the rounding radius ratio r/h, 2-D and 3-D bodies (measured curves).

The caption calls both curves averages of experimental data (after Hoerner); the book gives no equation, so
they are digitized from the 1973 art, figures/ch3/fig30.png. Calibration fig30.calib.json: piecewise linear
between the drawn ticks (the hand-ruled x ticks are spaced 73-76.5 px). Each curve's ink is followed column by
column where it is shallow and row by row where it is steep (the 3-D curve falls almost vertically near
r/h = 0.065), with the two inset leaders masked out where they touch the curves; the centre-line samples are
ordered along the curve, smoothed with a parametric smoothing spline in chord length (lam = 3000 px^3: the
pixel steps go, the knees stay), resampled, run into the axis level as drawn (a parabola over the first
r/h = 0.012, matched in value and slope) and written in data coordinates:
    fig30-2d.csv  the solid curve, 2-D half-streamlined section, R = 10^5
    fig30-3d.csv  the dashed curve, 3-D streamlined body, R = 10^6
Checked with tools/v2/digitize.py overlay (fig30.calib.json): 95% of the points within 0 px (2-D) and
2 px (3-D: the gaps between the dashes) of the scan's ink; the traced ink centre line lies within 0.40 px
(2-D) and 0.54 px (3-D) of the curves for 95% of its samples (max 0.81 and 1.12 px).
"""
import json
import pathlib
import numpy as np
from PIL import Image
from scipy.interpolate import make_smoothing_spline

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent.parent

spec = json.loads((HERE / "fig30.calib.json").read_text())
ax = spec["axes"]["main"]
XG, YG = np.array(ax["xgrid"], float), np.array(ax["ygrid"], float)
img = np.asarray(Image.open(ROOT / spec["crop"]).convert("L"))
ink = img < 128

# the axes and the inset leaders are not curve ink
ink[:, :89] = False
ink[285:, :] = False
rr, cc = np.mgrid[0:ink.shape[0], 0:ink.shape[1]]
for (x0, y0), (x1, y1) in (((246, 137), (214, 190.5)), ((444, 220), (414, 273.5))):
    t = np.clip(((cc - x0) * (x1 - x0) + (rr - y0) * (y1 - y0)) / ((x1 - x0) ** 2 + (y1 - y0) ** 2), 0, 1)
    ink &= np.hypot(cc - (x0 + t * (x1 - x0)), rr - (y0 + t * (y1 - y0))) > 2.3


def runs(v):
    idx = np.flatnonzero(v)
    if idx.size == 0:
        return []
    cut = np.flatnonzero(np.diff(idx) > 1)
    return [(s + e) / 2 for s, e in zip(np.r_[idx[0], idx[cut + 1]], np.r_[idx[cut], idx[-1]])]


def follow(u0, u1, v0, by="cols", max_jump=3.5, lo=0, hi=None):
    """Follow the curve from u = u0 to u1 (columns, or rows with by="rows"), starting at v0 in the other
    coordinate: in each line the ink run nearest the prediction. Returns (px, py) samples."""
    m = ink if by == "cols" else ink.T
    pts, last, slope, lu = [], float(v0), 0.0, None
    step = 1 if u1 >= u0 else -1
    for u in range(u0, u1 + step, step):
        cand = [r + lo for r in runs(m[lo:hi, u])]
        if not cand:
            continue
        pred = last + (slope * (u - lu) if lu is not None else 0)
        best = min(cand, key=lambda r: abs(r - pred))
        if abs(best - pred) <= max_jump * (1 if lu is None else max(1, abs(u - lu))):
            if lu is not None:
                slope = 0.6 * slope + 0.4 * (best - last) / (u - lu)
            last, lu = best, u
            pts.append((u, best) if by == "cols" else (best, u))
    return np.array(pts, float)


def smooth(px, py, lam, n=400):
    """Parametric smoothing spline in chord length; n samples."""
    s = np.r_[0, np.cumsum(np.hypot(np.diff(px), np.diff(py)))]
    keep = np.r_[True, np.diff(s) > 1e-6]
    px, py, s = px[keep], py[keep], s[keep]
    fx, fy = make_smoothing_spline(s, px, lam=lam), make_smoothing_spline(s, py, lam=lam)
    t = np.linspace(0, s[-1], n)
    return fx(t), fy(t)


def to_data(px, py):
    oy = np.argsort(YG[:, 0])
    return np.interp(px, XG[:, 0], XG[:, 1]), np.interp(py, YG[oy, 0], YG[oy, 1])


def level_start(x, y, xa):
    """Run the curve into the axis level, as drawn: below x = xa (the first ink columns, beside the axis
    line) a parabola with zero slope at x = 0 and the curve's value and slope at xa."""
    k = np.searchsorted(x, xa)
    ya, sa = y[k], (y[k + 1] - y[k - 1]) / (x[k + 1] - x[k - 1])
    xa = x[k]
    xs = np.linspace(0, xa, 7)[:-1]
    return np.r_[xs, x[k:]], np.r_[ya + sa * (xs ** 2 - xa ** 2) / (2 * xa), y[k:]]


def write(name, px, py):
    x, y = to_data(px, py)
    x, y = level_start(x, y, 0.012)
    rows = ["x,y"] + [f"{a:.5f},{b:.5f}" for a, b in zip(x, y)]
    (HERE / name).write_text("\n".join(rows) + "\n")
    print(f"{name}: {len(x)} points, C_Do {y[0]:.3f} at 0, {np.interp(0.1, x, y):.3f} at 0.1, "
          f"{y[-1]:.3f} at {x[-1]:.3f}")


# 2-D (solid): one pass by columns; the steepest part (slope about 3) is still a run per column
p2 = follow(89, 460, 28.5, max_jump=4)
p2 = p2[np.argsort(p2[:, 0] + p2[:, 1])]
write("fig30-2d.csv", *smooth(p2[:, 0], p2[:, 1], lam=3000))

# 3-D (dashed): columns to the knee, rows down the steep fall, columns along the tail
a = follow(89, 126, 55.5, max_jump=4)
b = follow(92, 248, 128.5, by="rows", max_jump=3, lo=110, hi=170)
c = follow(150, 460, 241.5, max_jump=3, lo=200, hi=284)
p3 = np.r_[a, b, c]
p3 = p3[np.argsort(p3[:, 0] + p3[:, 1])]
write("fig30-3d.csv", *smooth(p3[:, 0], p3[:, 1], lam=3000))
