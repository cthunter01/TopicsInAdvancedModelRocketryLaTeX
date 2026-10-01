#!/usr/bin/env python3
"""Chapter 2, Figure 23: overdamped response to an impulse of strength H in yaw.

Curve: eq. (40), alpha_X = H tau_1 tau_2 / (I_L (tau_1 - tau_2)) [e^(-t/tau_1) - e^(-t/tau_2)], with the time
constants tau_1, tau_2 from eq. (25); the initial conditions are eqs. (37a), (37b). Marks: t_m and alpha_Xm by
eqs. (43a), (43b), checked here against the curve's numerical maximum.

The figure has no numeric scale. Figures 21, 22 and 23 are drawn in one frame, the same rocket (the same
H/I_L and C_1/I_L) with three dampings: t in units of 1/omega_n, alpha_X in units of H/(I_L omega_n), where
omega_n = sqrt(C_1/I_L) and zeta = C_2 / (2 sqrt(C_1 I_L)). The caption compares this response with the
critically damped one of Figure 22 (the maximum sooner and smaller, the return more gradual): that is the
same rocket with a larger C_2. Here zeta = 1.7 (tau_1/tau_2 = 9.46), a least-squares fit of eq. (40)'s shape
to the 1973 curve (zeta = 1.701). In these units eq. (25) reads 1/tau = zeta -+ sqrt(zeta^2 - 1), and the
initial slope H/I_L is 1. Writes fig23.csv (t, alpha).
"""
import math
import pathlib

import numpy as np

ZETA = 1.7
T_END = 8.3                      # the curve's end; the axis runs to 8.6

S = math.sqrt(ZETA**2 - 1)
TAU1 = 1 / (ZETA - S)            # eq. (25), the large time constant
TAU2 = 1 / (ZETA + S)            # eq. (25), the small time constant
K = TAU1 * TAU2 / (TAU1 - TAU2)  # H tau_1 tau_2 / (I_L (tau_1 - tau_2)) in units of H/(I_L omega_n)

t = np.linspace(0, T_END, 416)
alpha = K * (np.exp(-t / TAU1) - np.exp(-t / TAU2))  # eq. (40)

r = TAU1 / TAU2
tm = TAU1 * TAU2 * math.log(r) / (TAU1 - TAU2)                                   # eq. (43a)
am = K * (r ** (-TAU2 / (TAU1 - TAU2)) - r ** (-TAU1 / (TAU1 - TAU2)))           # eq. (43b)
tf = np.linspace(0, 3, 300001)
af = K * (np.exp(-tf / TAU1) - np.exp(-tf / TAU2))
assert abs(tf[af.argmax()] - tm) < 1e-4 and abs(af.max() - am) < 1e-9

out = pathlib.Path(__file__).with_suffix(".csv")
out.write_text("t,alpha\n" + "\n".join(f"{a:.4f},{b:.5f}" for a, b in zip(t, alpha)) + "\n")
print(f"{out.name}: {len(t)} points; tau_1 = {TAU1:.4f}, tau_2 = {TAU2:.4f}, t_m = {tm:.4f}, "
      f"alpha_Xm = {am:.4f}")
