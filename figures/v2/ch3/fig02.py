#!/usr/bin/env python3
"""Chapter 3, Figure 2: rho/rho_o against altitude, 0-2500 m.

The book plots the U.S. Standard Atmosphere, 1962 (its reference 19) without printing the law. In the
troposphere that standard gives T = T_o - L h and rho/rho_o = (T/T_o)^(g_o M/(R* L) - 1), with T_o = 288.15 K,
L = 0.0065 K/m and g_o M/(R* L) = 5.25588 (h geopotential; below 2500 m it differs from the geometric altitude
by under 1 m, less than the line width). Checked against the scan with tools/v2/digitize.py overlay.
"""
import pathlib
T0, L, EXP = 288.15, 0.0065, 5.25588 - 1
out = pathlib.Path(__file__).with_suffix(".csv")
rows = ["h,rho"]
for h in range(0, 2501, 50):
    rows.append(f"{h},{((T0 - L * h) / T0) ** EXP:.5f}")
out.write_text("\n".join(rows) + "\n")
print(f"{out.name}: {len(rows) - 1} points")
