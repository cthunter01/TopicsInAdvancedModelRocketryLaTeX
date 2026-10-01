#!/usr/bin/env python3
"""Chapter 3, Figure 4: standard speed of sound c (m/sec) against altitude, 0-2500 m.

The chapter's eq. (213), c = c_std sqrt(T/T_std) (chapters/ch3-sec7.tex), with the sea-level standard values the
text uses, c_std = 340 m/sec (chapters/ch3-intro-sec2a.tex, chapters/ch3-sec7.tex) and T_std = 288.15 K, and the
standard temperature T = T_o - L h of Figure 3 (U.S. Standard Atmosphere, 1962: T_o = 288.15 K, L = 0.0065 K/m;
see fig03.py). The 1973 curve starts at 340 exactly and follows this to within a pixel; the 1962 standard's own
c = sqrt(gamma R T) (gamma = 1.40, R = 287.053 J/(kg K)) starts at 340.29 m/sec and runs 0.29 m/sec (1.2 mm on
the scan) above the print, so the text's 340 is used. Checked with tools/v2/digitize.py overlay (fig04.calib.json).
"""
import math
import pathlib
T0, L, C_STD = 288.15, 0.0065, 340.0
out = pathlib.Path(__file__).with_suffix(".csv")
rows = ["h,c"]
for h in range(0, 2501, 50):
    rows.append(f"{h},{C_STD * math.sqrt((T0 - L * h) / T0):.4f}")
out.write_text("\n".join(rows) + "\n")
print(f"{out.name}: {len(rows) - 1} points")
