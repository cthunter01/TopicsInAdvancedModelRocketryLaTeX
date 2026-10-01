#!/usr/bin/env python3
"""Chapter 2, Figure 28: roll-coupled response to a step M_s in yaw (scan figures/ch2/fig28.png).

The rocket of Figs 26 and 27 (fig26.py: I_L = C_1 = 1, I_R omega_Z = 4/(3 sqrt 5), C_2 = 0.47), quiescent before
the step; M_s/C_1 = 1.33 (in the angle unit of Figs 26 and 27; matched to the scan).
Equations: omega_1, omega_2 by eqs. (55), (56); D_1, D_2 by (57); the particular solution (61); A_1 sin(phi_1),
A_2 sin(phi_2) by the displays before (63a) and (63b); phi_1, phi_2 by (63a), (63b); A_1, A_2 by (64a), (64b);
the motion by (62a), (62b). Checked against a direct integration of the coupled equations with the step.
Writes fig28.csv: t, aX (alpha_X), aY (alpha_Y); fig28-marks.csv: Ms (M_s/C_1), the curves' extent.
"""
import pathlib, sys
import numpy as np
sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from fig26 import modes, denominator, motion, integrate, write, C1, C2_DAMPED

MS_C1 = 1.33        # M_s / C_1
T_END = 12.8        # the 1973 window: 12.89 upper, 12.75 lower

w1, w2, D1, D2 = modes(C2_DAMPED)
den = denominator(w1, w2, D1, D2)
s1 = MS_C1 * (w2**2 + D2**2 - w1 * w2 - D1 * D2) / den                  # A_1 sin phi_1
s2 = MS_C1 * (w1**2 + D1**2 - w1 * w2 - D1 * D2) / den                  # A_2 sin phi_2
p1 = np.arctan((w2**2 + D2**2 - w1 * w2 - D1 * D2) / (w1 * D2 - w2 * D1))  # (63a)
p2 = np.arctan((w1**2 + D1**2 - w1 * w2 - D1 * D2) / (w2 * D1 - w1 * D2))  # (63b)
A1, A2 = s1 / np.sin(p1), s2 / np.sin(p2)                               # (64a), (64b)
t = np.linspace(0, T_END, 513)
aX, aY = motion(t, w1, w2, D1, D2, A1, A2, p1, p2)
aX = aX + MS_C1                                                         # (62a): + M_s/C_1, eq. (61)
print(f"D_1 {D1:.5f}, D_2 {D2:.5f}; A_1 {A1:.4f}, A_2 {A2:.4f}; phi_1 {p1:.4f}, phi_2 {p2:.4f}")
write(pathlib.Path(__file__).with_suffix(".csv"), t, aX, aY, integrate(t, C2_DAMPED, [0, 0, 0, 0], Ms=MS_C1 * C1),
      Ms=MS_C1)
