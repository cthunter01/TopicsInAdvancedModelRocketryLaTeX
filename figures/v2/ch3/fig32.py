#!/usr/bin/env python3
"""Chapter 3, Figure 32: drag coefficient of a paraboloidal nose against its fineness ratio L/d (measured).

After Stine's Handbook of Model Rocketry; the book gives no equation, so the curve is digitized from the 1973
art, figures/ch3/fig32.png. Calibration fig32.calib.json: piecewise linear between the drawn ticks (x every
0.5, y every 0.25). The ink is followed column by column where the curve is shallow and row by row down its
steep fall (L/d 0.3-0.5); the centre-line samples are ordered along the curve, smoothed with a parametric
smoothing spline in chord length (lam = 3000 px^3), resampled, run into the axis level as drawn and written
in data coordinates to fig32.csv (x = L/d, y = C_D).
Checked with tools/v2/digitize.py overlay (fig32.calib.json): 95% of the points within 0 px of the scan's
ink; the traced ink centre line lies within 0.39 px of the curve for 95% of its samples (max 1.02 px).
"""
import json
import pathlib
import numpy as np
from PIL import Image
from scipy.interpolate import make_smoothing_spline

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent.parent

spec = json.loads((HERE / "fig32.calib.json").read_text())
ax = spec["axes"]["main"]
XG, YG = np.array(ax["xgrid"], float), np.array(ax["ygrid"], float)
img = np.asarray(Image.open(ROOT / spec["crop"]).convert("L"))
ink = img < 128
ink[:, :90] = False          # the y axis
ink[302:, :] = False         # the x axis


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


a = follow(90, 122, 89.0, max_jump=4)                               # the flat start
b = follow(112, 250, 120.5, by="rows", max_jump=3, lo=100, hi=200)  # the fall
c = follow(135, 531, 248.5, max_jump=3, lo=200)                     # the tail
p = np.r_[a, b, c]
p = p[np.argsort(p[:, 0] + p[:, 1])]
x, y = to_data(*smooth(p[:, 0], p[:, 1], lam=3000))
# run the curve into the axis level, as drawn: below L/d = 0.05 (the first ink columns, beside the axis
# line) a parabola with zero slope at 0 and the curve's value and slope at 0.05
k = np.searchsorted(x, 0.05)
ya, sa, xa = y[k], (y[k + 1] - y[k - 1]) / (x[k + 1] - x[k - 1]), x[k]
xs = np.linspace(0, xa, 7)[:-1]
x, y = np.r_[xs, x[k:]], np.r_[ya + sa * (xs ** 2 - xa ** 2) / (2 * xa), y[k:]]
(HERE / "fig32.csv").write_text("x,y\n" + "".join(f"{a:.5f},{b:.5f}\n" for a, b in zip(x, y)))
print(f"fig32.csv: {len(x)} points, C_D {y[0]:.3f} at 0, {np.interp(0.75, x, y):.3f} at 0.75, "
      f"{np.interp(1, x, y):.3f} at 1, {np.interp(2, x, y):.3f} at 2, {y[-1]:.3f} at {x[-1]:.2f}")
