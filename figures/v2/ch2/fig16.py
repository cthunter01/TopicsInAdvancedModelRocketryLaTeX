#!/usr/bin/env python3
"""Chapter 2, Figure 16: undamped response to a step disturbance in yaw (scan: figures/ch2/fig16.png).

Eq. (30), alpha_X = A e^{-Dt} sin(omega t + phi) + M_s/C_1, with D = C_2/(2 I_L) (eq. (16)) and
omega = sqrt(C_1/I_L - C_2^2/(4 I_L^2)) (eq. (17)); phi = arctan(omega/D) (eq. (31a), taken as atan2, so
phi = pi/2 when D = 0) and A = -M_s/(C_1 sin phi) (eq. (31b)). Undamped: C_2 = 0, so D = 0, omega = omega_n
and alpha_X = (M_s/C_1)(1 - cos omega_n t); the first peak, 2 M_s/C_1 at pi/omega_n, is eqs. (32a), (32b).

Normalised units shared by Figs 16-19 (one rocket, C_1/I_L the same, C_2 varied): I_L = C_1 = M_s = 1, so
omega_n = 1, t is in units of 1/omega_n and alpha_X in units of M_s/C_1. The time axis runs to
T = 2.75 pi/omega_n, where the scan's curve ends (its pi/omega_n tick is at 0.364 of that span).
Writes fig16.csv (t, alpha).
"""
import math, pathlib

I_L, C1, C2, MS = 1.0, 1.0, 0.0, 1.0
T = 2.75 * math.pi

D = C2 / (2 * I_L)                                  # eq. (16)
w = math.sqrt(C1 / I_L - C2 ** 2 / (4 * I_L ** 2))  # eq. (17)
phi = math.atan2(w, D)                              # eq. (31a)
A = -MS / (C1 * math.sin(phi))                      # eq. (31b)


def alpha(t):                                       # eq. (30)
    return A * math.exp(-D * t) * math.sin(w * t + phi) + MS / C1


n = 400
rows = [(T * i / n, alpha(T * i / n)) for i in range(n + 1)]
out = pathlib.Path(__file__).with_suffix(".csv")
out.write_text("t,alpha\n" + "\n".join(f"{t:.5f},{a:.5f}" for t, a in rows) + "\n")
print(f"{out.name}: {len(rows)} points; peak {alpha(math.pi / w):.4f} at t = pi/omega = {math.pi / w:.4f}")
