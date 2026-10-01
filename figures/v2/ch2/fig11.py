#!/usr/bin/env python3
"""Chapter 2, Figure 11: the underdamped homogeneous response in yaw and its envelope A e^{-Dt}.

Equations (chapters/ch2-sec3a.tex): eq. (15) alpha_X = A e^{-Dt} sin(omega t + phi); eq. (16) D = C_2/2I_L;
eq. (17) omega = sqrt(C_1/I_L - C_2^2/4I_L^2); eqs. (18), (19) tan phi = alpha_X0 omega / (D alpha_X0 + Omega_X0),
A = alpha_X0 / sin phi; the damping ratio of eq. (20) zeta = C_2 / 2 sqrt(C_1 I_L) = D/omega_n.
The envelope (the caption's dotted line) is A e^{-Dt}; the zeros are at omega t + phi = pi, 2pi.

A qualitative sketch (no numeric scale). Units shared by the family Figs 10-14: time in 1/omega_n (C_1/I_L = 1),
the yaw angle in one arbitrary unit (alpha_X0 = 1). zeta = 0.227 and Omega_X0 = 2.27 are fitted to the drawn curve
of the scan (figures/ch2/fig11.png: 95% of its points within 1 px of the fit): phi = 0.372 rad, A = 2.75 alpha_X0.

Writes fig11.csv (t, alpha, env: the response and the envelope) and fig11-marks.csv (one row: the constants,
the zeros t1, t2 and the envelope's first point of contact tc, where sin(omega t + phi) = 1).
"""
import math
import pathlib

import numpy as np

C1_IL = 1.0          # C_1/I_L: the time unit is 1/omega_n
ZETA = 0.227         # damping ratio, eq. (20)
ALPHA0 = 1.0         # alpha_X0
OMEGA0 = 2.27        # Omega_X0 (per 1/omega_n)
T_END = 9.2          # the family's last instant

wn = math.sqrt(C1_IL)
D = ZETA * wn                                          # eqs. (16), (20)
w = math.sqrt(C1_IL - D * D)                           # eq. (17)
phi = math.atan2(ALPHA0 * w, D * ALPHA0 + OMEGA0)      # eq. (18)
A = ALPHA0 / math.sin(phi)                             # eq. (19)
t1, t2 = (math.pi - phi) / w, (2 * math.pi - phi) / w
tc = (math.pi / 2 - phi) / w

t = np.linspace(0.0, T_END, 461)
alpha = A * np.exp(-D * t) * np.sin(w * t + phi)
env = A * np.exp(-D * t)

here = pathlib.Path(__file__)
out = here.with_suffix(".csv")
out.write_text("t,alpha,env\n" + "\n".join(f"{a:.5f},{b:.5f},{c:.5f}" for a, b, c in zip(t, alpha, env)) + "\n")
marks = {"alpha0": ALPHA0, "Omega0": OMEGA0, "A": A, "D": D, "omega": w, "phi": phi, "t1": t1, "t2": t2, "tc": tc}
mk = here.with_name(here.stem + "-marks.csv")
mk.write_text(",".join(marks) + "\n" + ",".join(f"{v:.5f}" for v in marks.values()) + "\n")
print(f"{out.name}: {len(t)} points; D = {D:.4f}, omega = {w:.4f}, phi = {phi:.4f} rad, A = {A:.4f}; "
      f"zeros {t1:.4f}, {t2:.4f}; peak {alpha.max():.4f}")
