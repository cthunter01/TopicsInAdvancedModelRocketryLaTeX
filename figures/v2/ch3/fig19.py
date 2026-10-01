#!/usr/bin/env python3
"""Chapter 3, Figure 19: eta_k against R_k/sqrt(R_x), flat plate (two-dimensional, incompressible).

Eqs. (91), (92), (94)-(96) (chapters/ch3-sec3b.tex): eta_k = (k/2x) sqrt(R_x), R_k = k u_k/nu, R_x = U_inf x/nu,
and the Blasius variable eta_B = 2 eta (eq. (96)), so the velocity at the top of the particle is
u_k = U_inf f'(2 eta_k) (eq. (45), Table 1). Then k = 2 x eta_k/sqrt(R_x) and
    R_k/sqrt(R_x) = k u_k/(nu sqrt(R_x)) = 2 eta_k u_k/U_inf = 2 eta_k f'(2 eta_k).
The book does not print this relation (it takes the chart from its Ref. 3, NACA TN 4363) but it follows from
these equations; f' is interpolated from Table 1 as in fig14.py (imported). The text's example,
(R_k)_t/sqrt(R_x) = 1.73, gives eta_k = 1.19 (the text reads 1.20 off the chart).

Writes fig19.csv (r: R_k/sqrt(R_x), eta), from the origin to r = 6 (the right of the axes).
"""
import pathlib
import sys

import numpy as np
from scipy.optimize import brentq

sys.dont_write_bytecode = True     # (no __pycache__ beside the figures)
from fig14 import blasius, write_csv

SCALE = 2.0                      # eta_B = SCALE * eta (eq. (96))
b = blasius()


def r(eta):
    return 2.0 * eta * b.fp(SCALE * eta)


end = brentq(lambda e: r(e) - 6.0, 1e-6, 4.0)
eta = np.linspace(0.0, end, 301)
out = pathlib.Path(__file__).with_suffix(".csv")
write_csv(out, ["r", "eta"], [r(eta), eta])
ex = brentq(lambda e: r(e) - 1.73, 1e-6, 4.0)
print(f"{out.name}: {len(eta)} points; eta = {end:.4f} at r = 6; example r = 1.73 -> eta_k = {ex:.3f} (text 1.20)")
