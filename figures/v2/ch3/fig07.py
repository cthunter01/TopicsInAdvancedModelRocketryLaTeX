#!/usr/bin/env python3
"""Chapter 3, Figure 7: standard absolute viscosity ratio mu/mu_o against altitude, 0-2500 m.

The book plots the U.S. Standard Atmosphere, 1962 (its reference 19) without printing the law. That standard
gives the viscosity by Sutherland's formula mu = beta T^(3/2)/(T + S), beta = 1.458e-6 kg/(m sec K^(1/2)),
S = 110.4 K, with the temperature T = T_o - L h of Figure 3 (T_o = 288.15 K, L = 0.0065 K/m; see fig03.py).
At sea level the formula gives mu_o = 1.78938e-5 kg/(m-sec) (the standard's table: 1.7894e-5); the figure
letters 1.78943e-5, which is the formula at 288.16 K (or the English-unit table value 3.7373e-7 lb-sec/ft^2
converted); the ratio plotted does not depend on it. Checked with tools/v2/digitize.py overlay (fig07.calib.json).
"""
import pathlib
T0, L, BETA, S = 288.15, 0.0065, 1.458e-6, 110.4


def mu(t):
    return BETA * t ** 1.5 / (t + S)


out = pathlib.Path(__file__).with_suffix(".csv")
rows = ["h,mu"]
for h in range(0, 2501, 50):
    rows.append(f"{h},{mu(T0 - L * h) / mu(T0):.6f}")
out.write_text("\n".join(rows) + "\n")
print(f"{out.name}: {len(rows) - 1} points; mu_o = {mu(T0):.6g} kg/(m sec)")
