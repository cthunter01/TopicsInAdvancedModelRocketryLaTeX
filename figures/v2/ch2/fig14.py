#!/usr/bin/env python3
"""Chapter 2, Figure 14: the divergent homogeneous response in yaw of a statically unstable rocket (C_1 < 0).

Equations (chapters/ch2-sec3a.tex): eq. (24) alpha_X = A_1 e^{-t/tau_1} + A_2 e^{-t/tau_2} with eq. (25)
1/tau_1 = C_2/2I_L - sqrt(C_2^2/4I_L^2 - C_1/I_L), 1/tau_2 = C_2/2I_L + sqrt(C_2^2/4I_L^2 - C_1/I_L) and eq. (26)
A_1 = (tau_1 alpha_X0 + tau_1 tau_2 Omega_X0)/(tau_1 - tau_2), A_2 = (tau_2 alpha_X0 + tau_1 tau_2 Omega_X0)/(tau_2 - tau_1).
With C_1 < 0, tau_1 is negative and the first mode grows (the text after eq. (26)). The straight line is the
tangent at t = 0, slope Omega_X0.

A qualitative sketch (no numeric scale). Units shared by the family Figs 10-14: time in 1/omega_n of Figs 10-13,
the yaw angle in the family's unit. The parameters are matched to the scan (figures/ch2/fig14.png) with its
tangent kept as drawn: alpha_X0 = 0.37 (the drawn tick, a third of Figs 11-13's), Omega_X0 = 0.13,
C_1/I_L = -0.42 and C_2/2I_L = 0.13 (a little damping); the curve leaves the top of the frame about a third of
the way across, as drawn.

Writes fig14.csv (t, alpha), up to alpha = 3.0 (above the frame).
"""
import math
import pathlib

import numpy as np

C1_IL = -0.42        # C_1/I_L < 0: statically unstable
D = 0.13             # C_2/2I_L
ALPHA0 = 0.37        # alpha_X0
OMEGA0 = 0.13        # Omega_X0
ALPHA_END = 3.0      # stop above the frame (ymax 2.8)

root = math.sqrt(D * D - C1_IL)
tau1, tau2 = 1 / (D - root), 1 / (D + root)       # eq. (25): tau1 < 0
A1 = (tau1 * ALPHA0 + tau1 * tau2 * OMEGA0) / (tau1 - tau2)     # eq. (26)
A2 = (tau2 * ALPHA0 + tau1 * tau2 * OMEGA0) / (tau2 - tau1)


def response(t):
    return A1 * np.exp(-t / tau1) + A2 * np.exp(-t / tau2)     # eq. (24)


fine = np.linspace(0.0, 10.0, 100001)
t_end = fine[int(np.argmax(response(fine) >= ALPHA_END))]
t = np.linspace(0.0, t_end, 301)
alpha = response(t)

out = pathlib.Path(__file__).with_suffix(".csv")
out.write_text("t,alpha\n" + "\n".join(f"{a:.5f},{b:.5f}" for a, b in zip(t, alpha)) + "\n")
print(f"{out.name}: {len(t)} points; tau1 = {tau1:.4f}, tau2 = {tau2:.4f}, A1 = {A1:.4f}, A2 = {A2:.4f}; "
      f"alpha reaches {alpha[-1]:.3f} at t = {t[-1]:.3f}")
