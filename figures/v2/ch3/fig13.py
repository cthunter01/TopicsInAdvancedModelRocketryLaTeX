#!/usr/bin/env python3
"""Chapter 3, Figure 13: profiles of u in a laminar boundary layer over one side of a flat plate.

Drawing coordinates are the scan's pixels (figures/ch3/fig13.png, 150 dpi) measured from the plate's leading
edge (the open circle, pixel 128.5, 182): x along the plate, y up from its surface (fig13.calib.json).

  - The edge of the boundary layer is eq. (54), delta = 5 sqrt(nu x / U_inf), i.e. delta = c sqrt(x) in the
    drawing; c = 5.85 px^(1/2) sets its scale to the 1973 dash-dot edge (the least-squares value over 104
    points read off the scan between the profiles). The 1973 edge is not a sqrt curve: it flattens down the
    plate (through the 1973 knees c = 6.07, 5.66, 5.37 at x = 114.5, 267.5, 419.5), so the computed edge lies
    above it near the leading edge and beyond the third profile (overlay 95% 8.95 px, max 20.8 px; recorded
    as a mismatch). The computed edge is used (standing rule: curves from the book's equations).
  - The profiles are Blasius's, u/U_inf = f'(eta), eta = y sqrt(U_inf/(nu x)) = 5 y/delta (eqs. (45), (54)),
    with f' from Table 1 (Howarth's solution of eq. (51), read from chapters/ch3-sec3a.tex, label
    ch3:tab:1) interpolated by cubic Hermite polynomials that use the table's f'' column as the derivative
    (as fig14.py does; f' = 1 beyond eta = 8.8). So the profiles are similar, as the text
    (ch3-sec3a.tex:206-216) says: u/U_inf is one function of y/delta at every station.
  - Each profile is drawn as in the 1973 art (after Schlichting): its arrows start on the station's base line
    and its knee, where u reaches U_inf, lies on the edge at the tip line x_s + U_inf. So the profile at
    station x_s is scaled with delta(x_s + U_inf), the edge's height where the knee is drawn.
  - The stations (the profiles' base lines), U_inf (the arrows' full length, 76 px) and the arrow rows
    (16 rows, y = 10 to 150 every 9.33 px) are the scan's.

Writes fig13-edge.csv (x, y), fig13-p1.csv, fig13-p2.csv, fig13-p3.csv (the profile lines through the arrow
tips, x, y) and fig13-arrows.csv (x0, y, u: one arrow from (x0, y) to (x0 + u, y), for the upstream uniform
profile and the three stations).
"""
import pathlib
import re

import numpy as np
from scipy.interpolate import CubicHermiteSpline

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]

C_EDGE = 5.85                          # delta = C_EDGE sqrt(x), px (scale set by the scan's edge)
U = 76.0                               # U_inf, the length of a free-stream arrow (px)
X_UNIFORM = -116.5                     # base line of the upstream (uniform) profile
STATIONS = [38.5, 191.5, 343.5]        # base lines of the three boundary-layer profiles
X_END = 466.0                          # right end of the plate in the crop
TOP = 150.0                            # top of the profiles
ROWS = [10.0 + k * (TOP - 10.0) / 15 for k in range(16)]


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
    """f'(eta) = u/U_inf (Table 1; 1 beyond the table)."""
    eta = np.asarray(eta, dtype=float)
    return np.where(eta < T[-1, 0], _FP(np.clip(eta, 0, T[-1, 0])), 1.0)


def delta(x):
    return C_EDGE * np.sqrt(np.maximum(x, 0.0))


def write(name, header, rows, fmt):
    path = HERE / name
    path.write_text(header + "\n" + "\n".join(",".join(fmt % v for v in r) for r in rows) + "\n")
    print(f"{name}: {len(rows)} rows")


# the edge, dense near the leading edge (x = X_END s^2)
s = np.linspace(0, 1, 121)
xe = X_END * s ** 2
write("fig13-edge.csv", "x,y", list(zip(xe, delta(xe))), "%.3f")

# the profile lines: from the wall along u(y) to the edge, then straight up to the top; each profile is scaled
# with delta at its tip line (xs + U), where its knee meets the drawn edge
for i, xs in enumerate(STATIONS, 1):
    d = delta(xs + U)
    y = np.unique(np.r_[np.linspace(0, min(1.8 * d, TOP), 90), TOP])
    u = U * fp(5 * y / d)
    write(f"fig13-p{i}.csv", "x,y", list(zip(xs + u, y)), "%.3f")

# the arrows
arrows = [(X_UNIFORM, y, U) for y in ROWS]
for xs in STATIONS:
    d = delta(xs + U)
    arrows += [(xs, y, float(U * fp(5 * y / d))) for y in ROWS]
write("fig13-arrows.csv", "x0,y,u", arrows, "%.3f")

for xs in STATIONS:
    print(f"station x = {xs:5.1f}: delta at the tip line (x = {xs + U:5.1f}) = {float(delta(xs + U)):6.1f} px")
print(f"delta at the dimension (x = 305.5): {float(delta(305.5)):.1f} px")
