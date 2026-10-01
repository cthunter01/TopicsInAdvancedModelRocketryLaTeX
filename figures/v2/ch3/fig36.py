#!/usr/bin/env python3
"""Chapter 3, Figure 36: eta, the cross-flow drag of a finite cylinder over that of an infinite one, against
fineness ratio l_b/d, 2 to 24 (a measured curve).

The book takes the curve from Hopkins (its reference 6) and gives no formula for it, so it is digitized from
the 1973 art, figures/ch3/fig36.png. Calibration fig36.calib.json: the drawn rulings are not evenly spaced
(about 39 px per 2 at the left, 36 at the right), so x is read piecewise between the drawn verticals (each
taken at the row where the curve crosses it) and y between the drawn horizontals, as tools/v2/digitize.py
does with xgrid/ygrid.

The curve is followed column by column (the gridlines masked, as digitize.py trace does) from the x = 2
ruling, where it starts, to the x = 24 ruling, and the traced centre line is fitted with a cubic in l_b/d
(rms 0.3 px of the scan, max 1.2); the fit is written from 2 to 24. It gives eta = 0.737 at l_b/d = 16, the text's
0.74 (ch3-sec5a). Writes fig36.csv.
"""
import json
import pathlib
import sys

import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent.parent
sys.path.insert(0, str(ROOT / "tools" / "v2"))
import digitize  # noqa: E402  (load_gray, line_mask, runs_in, Axes)

spec = json.loads((HERE / "fig36.calib.json").read_text())
ax = digitize.Axes(spec["axes"]["main"])
img = digitize.load_gray(spec["crop"])
dark = img < 128
ink = dark & ~digitize.line_mask(dark, int(0.25 * min(dark.shape)))

# follow the curve from a seed on it (column 140, row 251) both ways, to the x = 2 and x = 24 rulings
# (columns within 2 px of a vertical ruling are skipped: what the mask leaves of the ruling is not the curve)
rulings = np.array(spec["axes"]["main"]["xgrid"])[:, 0]
pts = []
for step, stop in ((1, 531), (-1, 119)):
    row, slope, last = 251.0, 0.0, 140
    for col in range(140, stop + step, step):
        if np.min(np.abs(rulings - col)) <= 2:
            continue
        cand = digitize.runs_in(ink[:, col])
        pred = row + slope * (col - last)
        best = min(cand, key=lambda r: abs(r[0] - pred)) if cand else None
        if best is None or abs(best[0] - pred) > 2 * max(1, abs(col - last)):
            continue                                   # a gap (a ruling crossing): bridge it
        if col != last:
            slope = 0.6 * slope + 0.4 * (best[0] - row) / (col - last)
        row, last = best[0], col
        pts.append((col, row))
pts = np.array(sorted(set(pts)))
x, y = ax.to_data(pts[:, 0], pts[:, 1])

c = np.polyfit(x, y, 3)
res_px = (y - np.polyval(c, x)) / (0.05 / 27.9)         # 27.9 px per 0.05
xs = np.linspace(2, 24, 89)
out = HERE / "fig36.csv"
out.write_text("f,eta\n" + "".join(f"{f:.3f},{v:.5f}\n" for f, v in zip(xs, np.polyval(c, xs))))
print(f"{out.name}: traced {len(x)} points x {x.min():.2f}..{x.max():.2f}; cubic fit rms "
      f"{np.sqrt((res_px**2).mean()):.2f} px, max {np.abs(res_px).max():.2f} px; eta(2) = {np.polyval(c, 2):.3f}, "
      f"eta(16) = {np.polyval(c, 16):.3f}, eta(24) = {np.polyval(c, 24):.3f}")
