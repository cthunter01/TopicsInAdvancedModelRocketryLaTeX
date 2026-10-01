#!/usr/bin/env python3
"""Chapter 2, Figure 18: critically damped response to a step disturbance in yaw (scan: figures/ch2/fig18.png).

Eq. (33), alpha_X = (A_1 + A_2 t) e^{-Dt} + M_s/C_1, with D = C_2/(2 I_L) (eq. (16)), A_1 = -M_s/C_1
(eq. (34a)) and A_2 = -D M_s/C_1 (eq. (34b)): alpha_X = (M_s/C_1)[1 - (1 + Dt) e^{-Dt}]. Critical damping,
C_2^2/(4 I_L^2) = C_1/I_L, makes D = omega_n.

Normalised units shared by Figs 16-19 (one rocket, C_1/I_L the same, C_2 varied): I_L = C_1 = M_s = 1, so
omega_n = 1 (here D = 1, C_2 = 2), t is in units of 1/omega_n and alpha_X in units of M_s/C_1; the time axis
runs to T = 2.75 pi/omega_n, as in Figs 16 and 17 (the scan has no time tick; set alone, its curve would fit
D T = 7.8 rather than 8.64). The curve is within 2 percent of M_s/C_1 from two thirds of the way across
(1 percent from three quarters), where the scan's curve meets the dashed line and runs along it.
Writes fig18.csv (t, alpha).
"""
import math, pathlib

I_L, C1, MS = 1.0, 1.0, 1.0
C2 = 2 * math.sqrt(C1 * I_L)                        # critical damping
T = 2.75 * math.pi

D = C2 / (2 * I_L)                                  # eq. (16)
A1 = -MS / C1                                       # eq. (34a)
A2 = -D * MS / C1                                   # eq. (34b)


def alpha(t):                                       # eq. (33)
    return (A1 + A2 * t) * math.exp(-D * t) + MS / C1


n = 400
rows = [(T * i / n, alpha(T * i / n)) for i in range(n + 1)]
out = pathlib.Path(__file__).with_suffix(".csv")
out.write_text("t,alpha\n" + "\n".join(f"{t:.5f},{a:.5f}" for t, a in rows) + "\n")
print(f"{out.name}: {len(rows)} points; D = {D}, end {rows[-1][1]:.5f}")
