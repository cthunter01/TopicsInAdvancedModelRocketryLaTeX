#!/usr/bin/env python3
"""Chapter 2, Figure 12: the critically damped (zeta = 1) homogeneous response in yaw.

Equations (chapters/ch2-sec3a.tex): eq. (22) alpha_X = (A_1 + A_2 t) e^{-Dt} with eq. (16) D = C_2/2I_L, which for
zeta = 1 equals omega_n = sqrt(C_1/I_L); eq. (23) A_1 = alpha_X0, A_2 = Omega_X0 + D alpha_X0.
The tangent at t = 0 has the slope Omega_X0 (standing rule 4 of corrections/v2-figures.md: the 1973 line is
steeper than the curve it leaves; the redraw draws the true tangent).

A qualitative sketch (no numeric scale). Units shared by the family Figs 10-14: time in 1/omega_n (C_1/I_L = 1),
the yaw angle in one arbitrary unit (alpha_X0 = 1). Omega_X0 = 0.6 is fitted to the drawn curve of the scan
(figures/ch2/fig12.png) at the family's time scale; it gives the single low peak the text describes
(1.10 alpha_X0 at t = 0.375). Fig 13 uses the same alpha_X0, Omega_X0 and C_1/I_L.

Writes fig12.csv (t, alpha).
"""
import math
import pathlib

import numpy as np

C1_IL = 1.0          # C_1/I_L: the time unit is 1/omega_n
ALPHA0 = 1.0         # alpha_X0
OMEGA0 = 0.6         # Omega_X0 (per 1/omega_n)
T_END = 9.2          # the family's last instant

D = math.sqrt(C1_IL)                 # zeta = 1: C_2/2I_L = sqrt(C_1/I_L)
A1 = ALPHA0                          # eq. (23)
A2 = OMEGA0 + D * ALPHA0

t = np.linspace(0.0, T_END, 461)
alpha = (A1 + A2 * t) * np.exp(-D * t)       # eq. (22)

out = pathlib.Path(__file__).with_suffix(".csv")
out.write_text("t,alpha\n" + "\n".join(f"{a:.5f},{b:.5f}" for a, b in zip(t, alpha)) + "\n")
tp = OMEGA0 / (D * A2)
print(f"{out.name}: {len(t)} points; peak {alpha.max():.4f} at t = {tp:.4f}; alpha({T_END}) = {alpha[-1]:.5f}")
