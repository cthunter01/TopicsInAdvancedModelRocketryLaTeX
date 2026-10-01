#!/usr/bin/env python3
"""Chapter 2, Figure 10: the undamped (C_2 = 0) homogeneous response in yaw, simple harmonic motion.

Equations (chapters/ch2-sec3a.tex): eq. (15) alpha_X = A e^{-Dt} sin(omega t + phi) with eq. (16) D = C_2/2I_L = 0,
so that eq. (17) gives omega = omega_n = sqrt(C_1/I_L) and alpha_X = A sin(omega_n t + phi) (the text after
eq. (19)); the phase and amplitude from the initial conditions by eqs. (18), (19) with D = 0:
    tan phi = alpha_X0 omega_n / Omega_X0,   A = alpha_X0 / sin phi.

A qualitative sketch (no numeric scale). Units shared by the family Figs 10-14: time in 1/omega_n (C_1/I_L = 1),
the yaw angle in one arbitrary unit. The initial conditions are matched to the scan (figures/ch2/fig10.png):
alpha_X0 = 0.8 and Omega_X0 = 2.12 give phi = 0.361 rad and A = 2.83 alpha_X0, the drawn ratio of the A and
alpha_X0 ticks (the drawn sinusoid alone, fitted without the alpha_X0 tick, has A = 1.73 alpha_X0 and its first
zero 8 px earlier; a doubt of the 1973 art). The points a-f of the figure are the maxima, zeros and minimum:
omega_n t + phi = pi/2, pi, 3pi/2, 2pi, 5pi/2, 3pi.

Writes fig10.csv (t, alpha: the curve from t = 0 to f) and fig10-marks.csv (one row: the constants and the
instants a-f that the drawing places).
"""
import math
import pathlib

import numpy as np

C1_IL = 1.0          # C_1/I_L: the time unit is 1/omega_n
ALPHA0 = 0.8         # alpha_X0
OMEGA0 = 2.12        # Omega_X0 (per 1/omega_n)

wn = math.sqrt(C1_IL)
phi = math.atan2(ALPHA0 * wn, OMEGA0)          # eq. (18), D = 0
A = ALPHA0 / math.sin(phi)                     # eq. (19)
inst = {k: (m * math.pi / 2 - phi) / wn for k, m in zip("abcdef", range(1, 7))}

t = np.linspace(0.0, inst["f"], 401)
alpha = A * np.sin(wn * t + phi)

here = pathlib.Path(__file__)
out = here.with_suffix(".csv")
out.write_text("t,alpha\n" + "\n".join(f"{a:.5f},{b:.5f}" for a, b in zip(t, alpha)) + "\n")
marks = {"alpha0": ALPHA0, "Omega0": OMEGA0, "A": A, "phi": phi, **{f"t{k}": v for k, v in inst.items()}}
mk = here.with_name(here.stem + "-marks.csv")
mk.write_text(",".join(marks) + "\n" + ",".join(f"{v:.5f}" for v in marks.values()) + "\n")
print(f"{out.name}: {len(t)} points; phi = {phi:.4f} rad, A = {A:.4f} ({A / ALPHA0:.3f} alpha_X0), "
      f"first zero {inst['b']:.4f}, f {inst['f']:.4f}")
