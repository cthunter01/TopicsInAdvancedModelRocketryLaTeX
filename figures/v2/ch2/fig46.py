#!/usr/bin/env python3
"""Chapter 2, Figure 46: the faired curve through the wind-tunnel data (the table of panel (a)).

The curve is hand-faired through measured points, so no equation determines it: it is digitized from panel
(b) of the crop figures/ch2/fig46.png (axes calibrated at the labelled ticks, fig46.calib.json [b]). The ink
is followed column by column from the origin to the curve's end (the run nearest the prediction from the
previous columns), skipping the columns under the x marks of the data points (their strokes cross the
curve; the last mark sits clear above the curve's end), and a smoothing spline through the origin is fitted
to the rest. Overlay on the crop: panel (b) 95% of the points within 0 px (max 1 px); the part panel (c)
shows beyond the straightedge (x > 0.16) 95% within 1 px (max 1 px). Panel (c) draws the same curve.

Writes fig46.csv (x = deflection angle in rad, y = moment in 10^5 dyn-cm) and fig46-points.csv (the table
of panel (a), as printed, with a leading zero on the angles).
"""
import csv
import json
import pathlib
import sys

import numpy as np
from PIL import Image
from scipy.interpolate import UnivariateSpline

HERE = pathlib.Path(__file__).parent
ROOT = HERE.parent.parent.parent
sys.path.insert(0, str(ROOT / "tools/v2"))
from digitize import Axes  # noqa: E402  (the calibration map of tools/v2/digitize.py)

CAL = json.loads((HERE / "fig46.calib.json").read_text())
AX = Axes(CAL["axes"]["b"])
CROP = ROOT / CAL["crop"]

# panel (a), as printed: moment (10^5 dyn-cm), deflection angle (rad)
TABLE = [("0.0", ".0000"), ("1.250", ".0240"), ("2.500", ".0490"), ("3.750", ".0770"), ("4.375", ".0875"),
         ("5.000", ".1000"), ("5.625", ".1135"), ("6.250", ".1340"), ("6.875", ".1610"), ("7.500", ".1852"),
         ("8.125", ".2315")]
PTS = np.array([(float(a), float(m)) for m, a in TABLE])   # (angle, moment)


def runs(v, off):
    idx = np.flatnonzero(v)
    if idx.size == 0:
        return []
    cut = np.flatnonzero(np.diff(idx) > 1)
    return [((s + e) / 2 + off, e - s + 1) for s, e in zip(np.r_[idx[0], idx[cut + 1]], np.r_[idx[cut], idx[-1]])]


ink = np.asarray(Image.open(CROP).convert("L")) < 128
# the marks' pixel columns (the curve is skipped within 7 px of each but the last)
mpx, mpy = AX.to_pixel(PTS[1:, 0], PTS[1:, 1])
# follow the curve from just right of the y axis (col 128, above the x axis) to its end (col 468)
pts, lastc, last, slope = [], 127, 455.0, -0.62
for c in range(128, 469):
    if np.min(np.abs(mpx[:-1] - c)) <= 7:     # under a mark: skip (the prediction bridges it); the last
        # mark sits clear above the curve's end, where the thickness test below separates them
        continue
    # rows above the x axis line (row 457-458); runs thicker than 4 px are a mark's stroke on the curve
    rr = [y for y, n in runs(ink[270:455, c], 270) if n <= 4]
    pred = last + slope * (c - lastc)
    if not rr:
        continue
    best = min(rr, key=lambda y: abs(y - pred))
    if abs(best - pred) > 2 + 0.2 * (c - lastc):
        continue
    if pts:
        slope = 0.7 * slope + 0.3 * (best - last) / (c - lastc)
    last, lastc = best, c
    pts.append((c, best))
P = np.array(pts, float)
x, y = AX.to_data(P[:, 0], P[:, 1])
# the origin, weighted, then a smoothing spline with an RMS residual of about 0.35 px (the traced centres
# are quantized to half a pixel); a stiffer fit droops at the flat end
xs = np.r_[0.0, x]
ys = np.r_[0.0, y]
w = np.r_[20.0, np.ones(len(x))]
sig = 0.35 / 18.2                                         # in moment units (18.2 px per 10^5 dyn-cm)
sp = UnivariateSpline(xs, ys, w=w, s=len(xs) * sig ** 2)
res = np.abs(sp(xs) - ys) * 18.2
xe = float(x.max())
xx = np.linspace(0, xe, 121)
yy = np.maximum.accumulate(sp(xx))                        # the faired curve never falls
yy[0] = 0.0
with open(HERE / "fig46.csv", "w", newline="") as f:
    wr = csv.writer(f)
    wr.writerow(["x", "y"])
    for a, b in zip(xx, yy):
        wr.writerow([f"{a:.5f}", f"{b:.4f}"])
with open(HERE / "fig46-points.csv", "w", newline="") as f:
    wr = csv.writer(f)
    wr.writerow(["x", "y"])
    for m, a in TABLE:
        wr.writerow([a if not a.startswith(".") else "0" + a, m])
print(f"fig46.csv: {len(xx)} points, x 0 .. {xe:.4f}, end y {yy[-1]:.3f}; initial slope {sp.derivative()(0.0):.1f}"
      f" (10^5 dyn-cm per rad); {len(x)} traced columns, max residual {res.max():.2f} px")
