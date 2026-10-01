#!/usr/bin/env python3
"""Chapter 2, Figure 21: underdamped response to an impulse of strength H in yaw.

Curve: eq. (38), alpha_X = (H / (I_L omega)) e^(-D t) sin(omega t), with D and omega from eqs. (16), (17)
(D = C_2 / 2 I_L, omega = sqrt(C_1/I_L - C_2^2 / 4 I_L^2)); the initial conditions are eqs. (37a), (37b).
Marks: t_m and alpha_Xm by eqs. (41a), (41b), checked here against the curve's numerical maximum.

The figure has no numeric scale. Figures 21, 22 and 23 are drawn in one frame, the same rocket (the same
H/I_L and C_1/I_L) with three dampings: t in units of 1/omega_n, alpha_X in units of H/(I_L omega_n), where
omega_n = sqrt(C_1/I_L) and zeta = D/omega_n. Here zeta = 0.25 (a least-squares fit of eq. (38)'s shape to the
1973 curve gives zeta = 0.244, D/omega = 0.252). In these units D = zeta, omega = sqrt(1 - zeta^2), and the
initial slope H/I_L is 1. Writes fig21.csv (t, alpha).
"""
import math
import pathlib

import numpy as np

ZETA = 0.25
T_END = 8.3                      # the curve's end; the axis runs to 8.6

D = ZETA                         # eq. (16) in units of omega_n
W = math.sqrt(1 - ZETA**2)       # eq. (17) in units of omega_n
A = 1 / W                        # H/(I_L omega) in units of H/(I_L omega_n)

t = np.linspace(0, T_END, 416)
alpha = A * np.exp(-D * t) * np.sin(W * t)            # eq. (38)

tm = math.atan(W / D) / W                             # eq. (41a)
am = A * math.exp(-(D / W) * math.atan(W / D)) * math.sin(math.atan(W / D))   # eq. (41b)
tf = np.linspace(0, 3, 300001)
af = A * np.exp(-D * tf) * np.sin(W * tf)
assert abs(tf[af.argmax()] - tm) < 1e-4 and abs(af.max() - am) < 1e-9

out = pathlib.Path(__file__).with_suffix(".csv")
out.write_text("t,alpha\n" + "\n".join(f"{a:.4f},{b:.5f}" for a, b in zip(t, alpha)) + "\n")
print(f"{out.name}: {len(t)} points; t_m = {tm:.4f}, alpha_Xm = {am:.4f}")
