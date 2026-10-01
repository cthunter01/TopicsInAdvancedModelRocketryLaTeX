#!/usr/bin/env python3
"""Chapter 2, Figure 19: overdamped response to a step disturbance in yaw (scan: figures/ch2/fig19.png).

Eq. (35), alpha_X = A_1 e^{-t/tau_1} + A_2 e^{-t/tau_2} + M_s/C_1, with tau_1, tau_2 from eq. (25) and
A_1 = -M_s tau_1/(C_1(tau_1 - tau_2)), A_2 = M_s tau_2/(C_1(tau_1 - tau_2)) (eqs. (36a), (36b)).

Normalised units shared by Figs 16-19 (one rocket, C_1/I_L the same, C_2 varied): I_L = C_1 = M_s = 1, so
omega_n = 1, t is in units of 1/omega_n and alpha_X in units of M_s/C_1; the time axis runs to
T = 2.75 pi/omega_n, as in Figs 16-18, so that the caption's "more slowly than ... the critically damped
response" is seen at the same scale as Fig 18. The one free parameter, the damping ratio
zeta = C_2/(2 sqrt(C_1 I_L)) = 2.1, is matched to the scan on that time axis (least squares over the traced
curve: 2.12; zeta = 2.1 ends at 0.880 M_s/C_1, the scan at 0.88).
Writes fig19.csv (t, alpha).
"""
import math, pathlib

ZETA = 2.1
I_L, C1, MS = 1.0, 1.0, 1.0
C2 = 2 * ZETA * math.sqrt(C1 * I_L)
T = 2.75 * math.pi

root = math.sqrt(C2 ** 2 / (4 * I_L ** 2) - C1 / I_L)
tau1 = 1 / (C2 / (2 * I_L) - root)                  # eq. (25)
tau2 = 1 / (C2 / (2 * I_L) + root)
A1 = -MS * tau1 / (C1 * (tau1 - tau2))              # eq. (36a)
A2 = MS * tau2 / (C1 * (tau1 - tau2))               # eq. (36b)


def alpha(t):                                       # eq. (35)
    return A1 * math.exp(-t / tau1) + A2 * math.exp(-t / tau2) + MS / C1


n = 400
rows = [(T * i / n, alpha(T * i / n)) for i in range(n + 1)]
out = pathlib.Path(__file__).with_suffix(".csv")
out.write_text("t,alpha\n" + "\n".join(f"{t:.5f},{a:.5f}" for t, a in rows) + "\n")
print(f"{out.name}: {len(rows)} points; tau1 = {tau1:.4f}, tau2 = {tau2:.4f}, end {rows[-1][1]:.4f}")
