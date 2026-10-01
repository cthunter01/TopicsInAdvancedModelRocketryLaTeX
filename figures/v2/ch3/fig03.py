#!/usr/bin/env python3
"""Chapter 3, Figure 3: standard temperature T (K) against altitude, 0-2500 m.

The book plots the U.S. Standard Atmosphere, 1962 (its reference 19), and describes the curve as a "linear
lapse rate" of about 1 deg C for each 154 meters (chapters/ch3-intro-sec2a.tex) from the sea-level 288 K. That
standard's troposphere is T = T_o - L h with T_o = 288.15 K and L = 0.0065 K/m (1/154 = 0.00649), h geopotential
(below 2500 m it differs from the geometric altitude by under 1 m, less than the line width), the same law as
fig02.py. Checked against the scan with tools/v2/digitize.py overlay (fig03.calib.json).
"""
import pathlib
T0, L = 288.15, 0.0065
out = pathlib.Path(__file__).with_suffix(".csv")
rows = ["h,T"]
for h in range(0, 2501, 50):
    rows.append(f"{h},{T0 - L * h:.4f}")
out.write_text("\n".join(rows) + "\n")
print(f"{out.name}: {len(rows) - 1} points")
