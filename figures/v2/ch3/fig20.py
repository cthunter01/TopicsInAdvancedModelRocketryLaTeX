#!/usr/bin/env python3
"""Chapter 3, Figure 20: eta_k against R_k/sqrt(R_x), cone at zero angle of attack (three-dimensional).

The construction of Fig 19 (eqs. (91), (92), (94)-(96), chapters/ch3-sec3b.tex: R_k/sqrt(R_x) = 2 eta_k u_k/U_inf)
with the laminar velocity profile of the cone, which the book does not give. Mangler's transformation (outside
the book; owner's decision, corrections/v2-figures.md) maps the cone's boundary layer at station x onto the flat
plate's at x/3, so the cone's profile is the Blasius one with y scaled by sqrt(3):
    u/U_inf = f'(sqrt(3) eta_B) = f'(2 sqrt(3) eta),     R_k/sqrt(R_x) = 2 eta_k f'(2 sqrt(3) eta_k),
f' interpolated from Table 1 as in fig14.py (imported; f' = 1 beyond the table's eta_B = 8.8). The text's
example, (R_k)_t/sqrt(R_x) = 1.73, gives eta_k = 0.966 (the text reads 0.96 off the chart).

Writes fig20.csv (r: R_k/sqrt(R_x), eta), from the origin to r = 6 (the right of the axes).
"""
import math
import pathlib
import sys

import numpy as np
from scipy.optimize import brentq

sys.dont_write_bytecode = True     # (no __pycache__ beside the figures)
from fig14 import blasius, write_csv

SCALE = 2.0 * math.sqrt(3.0)     # eta_B of the equivalent flat plate = SCALE * eta (Mangler)
b = blasius()


def r(eta):
    return 2.0 * eta * b.fp(SCALE * eta)


end = brentq(lambda e: r(e) - 6.0, 1e-6, 4.0)
eta = np.linspace(0.0, end, 301)
out = pathlib.Path(__file__).with_suffix(".csv")
write_csv(out, ["r", "eta"], [r(eta), eta])
ex = brentq(lambda e: r(e) - 1.73, 1e-6, 4.0)
print(f"{out.name}: {len(eta)} points; eta = {end:.4f} at r = 6; example r = 1.73 -> eta_k = {ex:.3f} (text 0.96)")
