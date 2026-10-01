#!/usr/bin/env python3
"""Chapter 3, Figure 10: the concept of free-stream velocity (velocity profiles above and below a rocket).

Drawing coordinates are the house model rocket's units (tamrfig.sty `model': length 6.4, diameter 0.4; nose
tip at the origin, axis along +x, y up). The scan (figures/ch3/fig10.png) draws the rocket 409 px long, so one
unit is 63.9 scan pixels (fig10.calib.json: nose tip at pixel 48, axis at row 177.25).

The profiles stand at x = 2.33 (the scan's station, behind the nose joint) on both sides of the body. The
boundary layer is laminar there, so its profile is Blasius's: u = V f'(eta), eta = 5 y'/delta (eqs. (45),
(54); y' the distance from the surface), with f' from Table 1 (Howarth's solution of eq. (51), read from
chapters/ch3-sec3a.tex, label ch3:tab:1) interpolated by cubic Hermite polynomials with the table's f''
column as the derivative (as fig14.py; f' = 1 beyond eta = 8.8). The thickness is greatly exaggerated, as the
caption says: delta = 0.65 (1.6 diameters), the scan's (its dashed edge below the body lies 41.5 px from the
surface). V (the arrows' full length, 74 px = 1.16) and the arrow rows (every 18.4 px = 0.288 from 14 px =
0.219 off the surface) are the scan's.

Writes fig10-profile.csv (x, y: the upper profile line through the arrow tips, from the surface to the top;
the lower one is its mirror image) and fig10-arrows.csv (x0, y, u: an arrow from (x0, y) to (x0 + u, y); the
upper side has seven, the eighth row being the V dimension, the lower side eight).
"""
import pathlib
import re

import numpy as np
from scipy.interpolate import CubicHermiteSpline

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]

R = 0.2                 # body radius (model)
XS = 2.33               # station of the profiles
V = 1.16                # free-stream velocity: an arrow's full length
DELTA = 0.65            # boundary-layer thickness (eta = 5)
Y0, DY = 0.219, 0.288   # arrow rows: distance of the first from the surface, spacing
TOP = 2.40              # the profiles' extent from the surface


def table1():
    """Table 1 of chapters/ch3-sec3a.tex as an array of rows (eta, f, f', f'')."""
    src = (ROOT / "chapters" / "ch3-sec3a.tex").read_text()
    body = src[src.index(r"\label{ch3:tab:1}"):]
    body = body[body.index(r"\midrule"):body.index(r"\bottomrule")]
    rows = [[float(g) for g in m.groups()] for m in
            re.finditer(r"^\s*([0-9.]+)\s*&\s*([0-9.]+)\s*&\s*([0-9.]+)\s*&\s*([0-9.]+)\s*\\\\", body, re.M)]
    t = np.array(rows)
    assert t.shape == (45, 4) and t[0, 0] == 0.0 and t[-1, 0] == 8.8, t.shape
    return t


T = table1()
_FP = CubicHermiteSpline(T[:, 0], T[:, 2], T[:, 3])


def fp(eta):
    eta = np.asarray(eta, dtype=float)
    return np.where(eta < T[-1, 0], _FP(np.clip(eta, 0, T[-1, 0])), 1.0)


def write(name, header, rows, fmt="%.4f"):
    path = HERE / name
    path.write_text(header + "\n" + "\n".join(",".join(fmt % v for v in r) for r in rows) + "\n")
    print(f"{name}: {len(rows)} rows")


yy = np.unique(np.r_[np.linspace(0, 1.8 * DELTA, 90), TOP])
write("fig10-profile.csv", "x,y", list(zip(XS + V * fp(5 * yy / DELTA), R + yy)))

rows = [Y0 + k * DY for k in range(8)]
arrows = [(XS, R + y, float(V * fp(5 * y / DELTA))) for y in rows[:7]]
arrows += [(XS, -(R + y), float(V * fp(5 * y / DELTA))) for y in rows]
write("fig10-arrows.csv", "x0,y,u", arrows)
print("V dimension at y =", R + rows[7])
