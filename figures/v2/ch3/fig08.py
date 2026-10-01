#!/usr/bin/env python3
"""Chapter 3, Figure 8: standard kinematic viscosity ratio nu/nu_o against altitude, 0-2500 m.

nu = mu/rho (chapters/ch3-intro-sec2a.tex), so nu/nu_o = (mu/mu_o)/(rho/rho_o), both from the U.S. Standard
Atmosphere, 1962 (the book's reference 19): mu/mu_o by Sutherland's formula as in fig07.py
(mu = beta T^(3/2)/(T + S), beta = 1.458e-6, S = 110.4 K) and rho/rho_o = (T/T_o)^(g_o M/(R* L) - 1) as in
fig02.py (g_o M/(R* L) = 5.25588), with T = T_o - L h (T_o = 288.15 K, L = 0.0065 K/m). The lettered
nu_o = 1.461e-5 m^2/sec agrees with mu_o/rho_o = 1.78938e-5/1.225 = 1.4607e-5 (1.4607e-5 also from the lettered
1.78943e-5/1.225014). Checked with tools/v2/digitize.py overlay (fig08.calib.json).
"""
import pathlib
T0, L, EXP, BETA, S = 288.15, 0.0065, 5.25588 - 1, 1.458e-6, 110.4


def mu(t):
    return BETA * t ** 1.5 / (t + S)


out = pathlib.Path(__file__).with_suffix(".csv")
rows = ["h,nu"]
for h in range(0, 2501, 50):
    t = T0 - L * h
    rows.append(f"{h},{(mu(t) / mu(T0)) / (t / T0) ** EXP:.6f}")
out.write_text("\n".join(rows) + "\n")
print(f"{out.name}: {len(rows) - 1} points; nu_o = {mu(T0) / 1.225:.5g} m^2/sec")
