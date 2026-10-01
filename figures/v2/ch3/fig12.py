#!/usr/bin/env python3
"""Chapter 3, Figure 12: causes and constituents of model rocket drag (the boundary layer and the wake).

Drawing coordinates are the house model rocket's units (tamrfig.sty `model': length 6.4, diameter 0.4, ogive
nose 1.2 long; nose tip at the origin, axis along +x, y up). The scan (figures/ch3/fig12.png) draws the rocket
415 px long, so one unit is 64.8 scan pixels (fig12.calib.json: nose tip at pixel 113, axis at row 148.5).

The boundary layer, greatly exaggerated as the caption says, keeps the shape of its governing laws with the
thickness read off the scan (its upper edge, 30 columns):
  - laminar from the nose tip to transition at x_t = 2.90 (the scan's): delta = a sqrt(x), the x^(1/2) growth
    of eq. (54); a = 0.0611 (least squares; rms 0.4 px against the scan);
  - turbulent from x_t: delta = b (x - x_v)^(4/5), the x^(4/5) growth of eq. (80) from a virtual origin x_v,
    continuous with the laminar layer at x_t; x_v = 1.519 and b = 0.0803 (least squares; rms 0.7 px);
  - the wake behind the base continues the turbulent edge.
Overlay on the scan (tools/v2/digitize.py overlay, fig12.calib.json): the edges from x = 1.2 to the base lie
95% within 1.0 px (upper) and 2.0 px (lower) of the scan's ink; with the wake, 1.0 and 2.2 px (max 9 px, at the
wake's end and where the 1973 lower wake bulges round the lug).
The edge lies at r(x) + delta(x), r the body radius (the tangent ogive nose, then 0.2).

Writes fig12-edge.csv (x, y: the upper edge from the nose tip to the end of the wake; the lower is its mirror
image) and fig12-eddies.csv (x1, x2, y: the short dashes that mark the turbulent boundary layer and the wake,
placed by a seeded random generator in loose rows, kept clear of the fins, the launch lug and its wake and the base bubble).
"""
import math
import pathlib

import numpy as np

HERE = pathlib.Path(__file__).resolve().parent

L, R, NL = 6.4, 0.2, 1.2                 # length, radius, nose length (model)
CR, CT, SPAN, SWEEP = 0.95, 0.45, 0.6, 0.5
XT = 2.90                               # transition
A_LAM = 0.0611                          # laminar: delta = A_LAM sqrt(x)
XV, B_TURB = 1.519, 0.0803              # turbulent: delta = B_TURB (x - XV)^0.8
X_END = 8.4                             # end of the wake drawn
LUG = (4.25, 4.85, 0.07)                # launch lug on the lower surface: x0, x1, height
LUG_WAKE = 5.2                          # its wake closes here
BUBBLE = 7.2                            # the base bubble closes here (on the axis)


def radius(x):
    x = np.asarray(x, dtype=float)
    rho = (R * R + NL * NL) / (2 * R)
    nose = np.sqrt(np.maximum(0, rho * rho - (NL - np.minimum(x, NL)) ** 2)) + R - rho
    return np.where(x < NL, nose, np.where(x <= L, R, R))


def delta(x):
    x = np.asarray(x, dtype=float)
    return np.where(x < XT, A_LAM * np.sqrt(np.maximum(x, 0)), B_TURB * np.maximum(x - XV, 0) ** 0.8)


def edge(x):
    return radius(x) + delta(x)


def in_fin(x, y):
    """inside the upper or lower fin (profile), with a margin"""
    ya = abs(y)
    le = (L - CR) + (ya - R) * SWEEP / SPAN
    return R <= ya <= R + SPAN + 0.03 and le - 0.04 <= x <= L + 0.02


def in_bubble(x, y):
    """inside the base recirculation bubble (a lens from the base to x = BUBBLE), with a margin"""
    if x < L or x > BUBBLE + 0.05:
        return False
    s = (x - L) / (BUBBLE - L)
    half = (R + 0.03) * math.sqrt(max(0.0, 1 - s ** 2)) if s > 0.35 else R + 0.03
    return abs(y) <= half


def in_lug(x, y):
    return y < 0 and LUG[0] - 0.05 <= x <= LUG_WAKE + 0.05 and -R - LUG[2] - 0.05 <= y


def write(name, header, rows, fmt="%.4f"):
    path = HERE / name
    path.write_text(header + "\n" + "\n".join(",".join(fmt % v for v in r) for r in rows) + "\n")
    print(f"{name}: {len(rows)} rows")


# the edge, dense near the nose tip
s = np.linspace(0, 1, 60)
xs = np.unique(np.r_[XT * s ** 2, np.linspace(XT, X_END, 120)])
write("fig12-edge.csv", "x,y", list(zip(xs, edge(xs))))

# the eddies: rows every 0.06 in y (+-10%); along each, dashes 0.05-0.14 long with gaps 0.04-0.12 and random
# phase, each set off the row by up to +-0.012
rng = np.random.default_rng(1973)
DY, MARGIN, JIT = 0.06, 0.022, 0.012
eddies = []
ymax = float(edge(X_END))


def dash_ok(x, x2, y):
    """the dash lies in the turbulent layer (between the body and the edge) or in the wake (inside the edge),
    clear of the fins, the bubble and the lug"""
    for xx in np.linspace(x, x2, 5):
        inner = R + MARGIN if xx <= L else 0.0
        if not inner <= abs(y) <= float(edge(xx)) - MARGIN:
            return False
        if in_fin(xx, y) or in_bubble(xx, y) or in_lug(xx, y):
            return False
    return True


rows = []
y = -ymax
while y < ymax:
    rows.append(y)
    y += DY * rng.uniform(0.9, 1.1)
for y0 in rows:
    x = XT + rng.uniform(0, 0.15)
    while x < X_END - 0.05:
        x2 = min(x + rng.uniform(0.05, 0.14), X_END - 0.02)
        y = y0 + rng.uniform(-JIT, JIT)
        if x2 - x > 0.04 and dash_ok(x, x2, y):
            eddies.append((x, x2, y))
        x = x2 + rng.uniform(0.04, 0.12)
write("fig12-eddies.csv", "x1,x2,y", eddies)
print(f"delta at transition {float(delta(XT)):.4f}, at the base {float(delta(L)):.4f}, at the wake's end "
      f"{float(delta(X_END)):.4f}")
