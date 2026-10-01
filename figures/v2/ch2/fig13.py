#!/usr/bin/env python3
"""Chapter 2, Figure 13: the overdamped (zeta > 1) homogeneous response in yaw.

Equations (chapters/ch2-sec3a.tex): eq. (24) alpha_X = A_1 e^{-t/tau_1} + A_2 e^{-t/tau_2}; eq. (25)
1/tau_1 = C_2/2I_L - sqrt(C_2^2/4I_L^2 - C_1/I_L), 1/tau_2 = C_2/2I_L + sqrt(C_2^2/4I_L^2 - C_1/I_L);
eq. (26) A_1 = (tau_1 alpha_X0 + tau_1 tau_2 Omega_X0)/(tau_1 - tau_2),
A_2 = (tau_2 alpha_X0 + tau_1 tau_2 Omega_X0)/(tau_2 - tau_1); eq. (20) zeta = C_2 / 2 sqrt(C_1 I_L).
The tangent at t = 0 has the slope Omega_X0 (standing rule 4: the 1973 line is steeper than the curve).

A qualitative sketch (no numeric scale). Units shared by the family Figs 10-14: time in 1/omega_n (C_1/I_L = 1),
the yaw angle in one arbitrary unit. Fig 12's alpha_X0 = 1, Omega_X0 = 0.6 and C_1/I_L, with a larger C_2
(zeta = 1.5, fitted to the drawn curve of figures/ch2/fig13.png), so that the caption's comparison shows: the
response returns to zero more slowly than Fig 12's.

Writes fig13.csv (t, alpha).
"""
import math
import pathlib

import numpy as np

C1_IL = 1.0          # C_1/I_L: the time unit is 1/omega_n
ZETA = 1.5           # damping ratio, eq. (20)
ALPHA0 = 1.0         # alpha_X0 (as Fig 12)
OMEGA0 = 0.6         # Omega_X0 (as Fig 12)
T_END = 9.2          # the family's last instant

D = ZETA * math.sqrt(C1_IL)                        # C_2/2I_L
root = math.sqrt(D * D - C1_IL)
tau1, tau2 = 1 / (D - root), 1 / (D + root)       # eq. (25)
A1 = (tau1 * ALPHA0 + tau1 * tau2 * OMEGA0) / (tau1 - tau2)     # eq. (26)
A2 = (tau2 * ALPHA0 + tau1 * tau2 * OMEGA0) / (tau2 - tau1)

t = np.linspace(0.0, T_END, 461)
alpha = A1 * np.exp(-t / tau1) + A2 * np.exp(-t / tau2)         # eq. (24)

out = pathlib.Path(__file__).with_suffix(".csv")
out.write_text("t,alpha\n" + "\n".join(f"{a:.5f},{b:.5f}" for a, b in zip(t, alpha)) + "\n")
print(f"{out.name}: {len(t)} points; tau1 = {tau1:.4f}, tau2 = {tau2:.4f}, A1 = {A1:.4f}, A2 = {A2:.4f}; "
      f"peak {alpha.max():.4f}; alpha({T_END}) = {alpha[-1]:.4f}")
