#!/usr/bin/env python3
"""Chapter 2, Figure 49: resonant amplitude ratio against damping ratio.

Eq. (50), AR_res = 1 / (2 C_1 zeta sqrt(1 - zeta^2)) (ch2-sec3b.tex:517-519), plotted in units of 1/C_1 for
zeta up to 0.7 (the axis); the coupled form, eq. (75), is the same curve (the caption). The curve enters the
frame (8/C_1) at zeta_8 = sqrt((1 - sqrt(63/64))/2) = 0.06262. The owner's decision (corrections/v2-figures.md):
computed from eq. (50), which the text uses (1.746 at zeta = 0.3, ch2-sec6.tex:547-549; ten times at 0.05,
ch2-sec6.tex:551-553), although the 1973 curve reaches 8/C_1 already at zeta = 0.052.

Writes fig49.csv (zeta, ar: AR_res C_1), sampled evenly in log zeta.
"""
import math, pathlib

here = pathlib.Path(__file__).parent
name = pathlib.Path(__file__).stem


def ar_res(zeta):
    return 1 / (2 * zeta * math.sqrt(1 - zeta * zeta))


z8 = math.sqrt((1 - math.sqrt(63 / 64)) / 2)
n = 300
zetas = [z8 * (0.7 / z8) ** (i / n) for i in range(n + 1)]
rows = ["zeta,ar"] + [f"{z:.5f},{ar_res(z):.5f}" for z in zetas]
(here / f"{name}.csv").write_text("\n".join(rows) + "\n")
print(f"{name}.csv: {len(zetas)} points; zeta_8 = {z8:.5f}; AR_res(0.3) = {ar_res(0.3):.4f}; "
      f"AR_res(0.05) = {ar_res(0.05):.4f}; AR_res(0.7) = {ar_res(0.7):.4f}")
