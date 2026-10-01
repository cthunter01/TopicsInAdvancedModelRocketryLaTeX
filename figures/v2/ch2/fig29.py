#!/usr/bin/env python3
"""Chapter 2, Figure 29: roll-coupled response to an impulse H in yaw (scan figures/ch2/fig29.png).

The rocket of Figs 26-28 (fig26.py: I_L = C_1 = 1, I_R omega_Z = 4/(3 sqrt 5), C_2 = 0.47); initial conditions
alpha_X0 = alpha_Y0 = Omega_Y0 = 0, Omega_X0 = H/I_L = 3.1 (in the angle unit of Figs 26 and 27 per time unit;
matched to the scan).
Equations: omega_1, omega_2 by eqs. (55), (56); D_1, D_2 by (57); A_1 sin(phi_1) by the display before (65a);
phi by (65a) (= phi_2, (65b)); A by (66a) (A_2 = -A, (66b)); the motion by eq. (67). Checked against a direct
integration of the coupled equations.
Writes fig29.csv: t, aX (alpha_X), aY (alpha_Y); fig29-marks.csv: H (H/I_L, the initial slope), the curves' extent.
"""
import pathlib, sys
import numpy as np
sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from fig26 import modes, denominator, integrate, write, IL, C2_DAMPED

H_IL = 3.1          # H / I_L
T_END = 12.6        # the 1973 window: 12.51 upper, 12.70 lower

w1, w2, D1, D2 = modes(C2_DAMPED)
s1 = H_IL * (D1 - D2) / denominator(w1, w2, D1, D2)                     # A_1 sin phi_1
p = np.arctan((D1 - D2) / (w2 - w1))                                    # (65a)
A = s1 / np.sin(p)                                                      # (66a)
t = np.linspace(0, T_END, 513)
aX = A * (np.exp(-D1 * t) * np.sin(w1 * t + p) - np.exp(-D2 * t) * np.sin(w2 * t + p))   # (67)
aY = A * (np.exp(-D1 * t) * np.cos(w1 * t + p) - np.exp(-D2 * t) * np.cos(w2 * t + p))
print(f"D_1 {D1:.5f}, D_2 {D2:.5f}; A {A:.4f}, phi {p:.4f}")
write(pathlib.Path(__file__).with_suffix(".csv"), t, aX, aY, integrate(t, C2_DAMPED, [0, 0, H_IL * IL, 0]),
      H=H_IL)
