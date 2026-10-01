#!/usr/bin/env python3
"""Chapter 2, Figure 22: critically damped response to an impulse of strength H in yaw.

Curve: eq. (39), alpha_X = (H/I_L) t e^(-D t), with D from eq. (16) (D = C_2 / 2 I_L = omega_n at critical
damping); the initial conditions are eqs. (37a), (37b). Marks: t_m = 1/D and alpha_Xm = H/(I_L D e) by eqs.
(42a), (42b), checked here against the curve's numerical maximum.

The figure has no numeric scale. Figures 21, 22 and 23 are drawn in one frame, the same rocket (the same
H/I_L and C_1/I_L) with three dampings: t in units of 1/omega_n, alpha_X in units of H/(I_L omega_n), where
omega_n = sqrt(C_1/I_L). Here D = 1, and the initial slope H/I_L is 1: the curve is fully determined.
Writes fig22.csv (t, alpha).
"""
import math
import pathlib

import numpy as np

T_END = 8.3                      # the curve's end; the axis runs to 8.6
D = 1.0                          # eq. (16) at zeta = 1, in units of omega_n

t = np.linspace(0, T_END, 416)
alpha = t * np.exp(-D * t)                            # eq. (39)

tm = 1 / D                                            # eq. (42a)
am = 1 / (D * math.e)                                 # eq. (42b)
tf = np.linspace(0, 3, 300001)
af = tf * np.exp(-D * tf)
assert abs(tf[af.argmax()] - tm) < 1e-4 and abs(af.max() - am) < 1e-9

out = pathlib.Path(__file__).with_suffix(".csv")
out.write_text("t,alpha\n" + "\n".join(f"{a:.4f},{b:.5f}" for a, b in zip(t, alpha)) + "\n")
print(f"{out.name}: {len(t)} points; t_m = {tm:.4f}, alpha_Xm = {am:.4f}")
