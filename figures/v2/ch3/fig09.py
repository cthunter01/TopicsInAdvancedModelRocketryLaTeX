#!/usr/bin/env python3
"""Chapter 3, Figure 9: the velocity profile u(y) beside the fluid element (a qualitative sketch).

The book gives no equation for this profile: it is a generic u(y) (the text, ch3-sec2b.tex: "u is a function
of both the x and y coordinate values"), drawn after Schlichting. Its shape is matched to the 1973 art,
figures/ch3/fig09.png: the curve is traced row by row (the ink run nearest the prediction, right of the
velocity arrows' shafts) and fitted, in units of the profile's height H (its base line: x = 13 px, from
y = 338 px to y = 12 px; fig09.calib.json, axes "profile"), with the cubic

    u(y)/H = c0 + c1 (y/H) + c2 (y/H)^2 + c3 (y/H)^3

the lowest degree that follows the trace within 3 px (residual rms about 0.6 px). The profile bulges to a
maximum near y = 0.8 H and turns back a little at the top, as printed. Writes fig09.csv (y, u, both / H;
the tex scales them) and fig09-arrows.csv (the 18 velocity arrows of the art, at y/H = (k + 1/2)/18,
k = 0 .. 17, each of length u(y)).
"""
import json
import pathlib
import numpy as np
from PIL import Image

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent.parent

X0, YBOT, YTOP = 13.0, 338.0, 12.0     # the profile's base line in the crop (px)
H = YBOT - YTOP


def trace(crop):
    """Follow the profile from the middle (row 175) up and down: in each row, the centre of the ink run
    nearest the previous one, among runs right of x = 40 (the arrows' shafts end at the curve)."""
    ink = np.asarray(Image.open(crop).convert("L")) < 128
    pts = []
    for rows in (range(175, int(YTOP) + 1, -1), range(176, int(YBOT))):
        last = 112.0
        for r in rows:
            idx = np.flatnonzero(ink[r, 40:200]) + 40
            if idx.size == 0:
                continue
            cut = np.flatnonzero(np.diff(idx) > 1)
            starts, ends = np.r_[idx[0], idx[cut + 1]], np.r_[idx[cut], idx[-1]]
            # an arrow's shaft merges with the curve: take the right end of each run as the curve's
            # right edge, less half the stroke (1 px)
            cand = [e - 1.0 if e - s > 4 else (s + e) / 2 for s, e in zip(starts, ends)]
            best = min(cand, key=lambda c: abs(c - last))
            if abs(best - last) <= 3:
                pts.append((r, best))
                last = best
    pts.sort()
    rows, xs = np.array(pts).T
    return (YBOT - rows) / H, (xs - X0) / H


def main():
    spec = json.loads((HERE / "fig09.calib.json").read_text())
    y, u = trace(ROOT / spec["crop"])
    p = np.polyfit(y, u, 3)
    res = (np.polyval(p, y) - u) * H
    print(f"fig09: {y.size} traced points; cubic {np.round(p[::-1], 4)} (c0..c3); "
          f"residual rms {np.sqrt(np.mean(res**2)):.2f} px, max {np.abs(res).max():.2f} px")
    yy = np.linspace(0.0, 1.0, 101)
    with open(HERE / "fig09.csv", "w") as f:
        f.write("y,u\n")
        for a, b in zip(yy, np.polyval(p, yy)):
            f.write(f"{a:.4f},{b:.5f}\n")
    yk = (np.arange(18) + 0.5) / 18
    with open(HERE / "fig09-arrows.csv", "w") as f:
        f.write("y,u\n")
        for a, b in zip(yk, np.polyval(p, yk)):
            f.write(f"{a:.5f},{b:.5f}\n")


if __name__ == "__main__":
    main()
