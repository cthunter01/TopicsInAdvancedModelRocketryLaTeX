#!/usr/bin/env python3
"""Chapter 2, Figure 27: damped roll-coupled response to general initial conditions (scan figures/ch2/fig27.png).

The rocket and initial conditions of Fig 26 (fig26.py: I_L = C_1 = 1, I_R omega_Z = 4/(3 sqrt 5); alpha_X0 = 0.65,
alpha_Y0 = 1, Omega_X0 = Omega_Y0 = 1.55) with damping C_2 = 0.47: the coupled, positively-stable case.
Equations: omega_1, omega_2 by eqs. (55), (56); D_1, D_2 by (57); phi_1, phi_2 by (58a), (58b); A_1, A_2 by (59a),
(59b); the motion by eq. (51). Checked against a direct integration of the coupled equations.
Writes fig27.csv: t, aX (alpha_X), aY (alpha_Y); fig27-marks.csv: the initial conditions, the curves' extent.
"""
import pathlib, sys
import numpy as np
sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from fig26 import modes, general, motion, integrate, write, C2_DAMPED, AX0, AY0, OX0, OY0

T_END = 12.85       # the 1973 window: 12.80 upper, 12.92 lower

w1, w2, D1, D2 = modes(C2_DAMPED)
A1, A2, p1, p2 = general(w1, w2, D1, D2, AX0, AY0, OX0, OY0)
t = np.linspace(0, T_END, 513)
aX, aY = motion(t, w1, w2, D1, D2, A1, A2, p1, p2)
print(f"omega_1 {w1:.5f} (slow), omega_2 {w2:.5f} (fast); D_1 {D1:.5f}, D_2 {D2:.5f}; A_1 {A1:.4f}, A_2 {A2:.4f}")
write(pathlib.Path(__file__).with_suffix(".csv"), t, aX, aY, integrate(t, C2_DAMPED, [AX0, AY0, OX0, OY0]),
      aX0=AX0, aY0=AY0, OX0=OX0, OY0=OY0)
