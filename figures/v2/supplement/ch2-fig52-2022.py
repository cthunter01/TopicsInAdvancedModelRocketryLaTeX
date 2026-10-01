#!/usr/bin/env python3
"""Chapter 2, Figure 52 (Mandell's 2022 figure, used in the chapter and in the supplement Part): the roll rates
to avoid to keep AR_c from exceeding 1.25/C_1.

The boundary is eq. (73b), AR_c = 1 / (C_1 sqrt((beta_c^2 - 1)^2 + (2 zeta_c beta_c)^2)) (ch2-sec3d.tex), set
equal to 1.25/C_1 (the caption): (beta_c^2 - 1)^2 + (2 zeta_c beta_c)^2 = 0.64, i.e.
    zeta_c = sqrt(0.64 - (beta_c^2 - 1)^2) / (2 beta_c),   0.2 <= beta_c^2 <= 1.8.
(Not eqs. (115)-(117), which give the roll rate.) Its feet are beta_c = sqrt(0.2) = 0.4472 and sqrt(1.8) =
1.3416; its peak, from eqs. (74a) and (75) with AR_cres = 1.25/C_1, is zeta_c = sqrt(0.2) = 0.4472 (the
supplement's 0.4472) at beta_c = sqrt(0.6) = 0.7746. Sampled on beta_c^2 - 1 = -0.8 cos(theta),
theta = 0 ... pi, so that the vertical feet are sampled finely.

Writes ch2-fig52-2022.csv (beta, zeta).
"""
import math, pathlib

here = pathlib.Path(__file__).parent
name = pathlib.Path(__file__).stem

n = 240
rows = ["beta,zeta"]
for i in range(n + 1):
    th = math.pi * i / n
    u = -0.8 * math.cos(th)                       # beta_c^2 - 1
    beta = math.sqrt(1 + u)
    zeta = 0.8 * math.sin(th) / (2 * beta) + 0.0
    rows.append(f"{beta:.5f},{zeta:.5f}")
(here / f"{name}.csv").write_text("\n".join(rows) + "\n")
print(f"{name}.csv: {n + 1} points; feet {math.sqrt(0.2):.4f}, {math.sqrt(1.8):.4f}; "
      f"peak {math.sqrt(0.2):.4f} at {math.sqrt(0.6):.4f}")
