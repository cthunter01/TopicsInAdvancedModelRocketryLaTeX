#!/usr/bin/env python3
"""Chapter 2, Figure 31: coupled amplitude ratio against coupled frequency ratio, roll-coupled response to
sinusoidal forcing in pitch and yaw at the roll rate.

Eq. (73b), AR_c = 1 / (C_1 sqrt((beta_c^2 - 1)^2 + (2 zeta_c beta_c)^2)), plotted in units of 1/C_1 (the same
function as eq. (48b) of Figure 25: ch2-sec3d.tex:419-422), for the figure's coupled damping ratios
zeta_c = .2, .5, sqrt(2)/2, 1, 2 over beta_c = 0 ... 2.00 and AR_c = 0 ... 3/C_1 (the axes). The peaks check
against eqs. (74a), (75): beta_cres = sqrt(1 - 2 zeta_c^2), AR_cres = 1/(2 C_1 zeta_c sqrt(1 - zeta_c^2)).
zeta_c = 0 is 1/|beta_c^2 - 1|, which leaves the frame (3/C_1) at beta_c = sqrt(2/3) and returns at sqrt(4/3).

Writes fig31.csv (beta, z02, z05, z07, z1, z2: AR_c C_1) and fig31-z0.csv (beta, ar: the zeta_c = 0 curve,
its two branches ending exactly on the frame and separated by a nan row).
"""
import math, pathlib

ZETAS = [("z02", 0.2), ("z05", 0.5), ("z07", math.sqrt(2) / 2), ("z1", 1.0), ("z2", 2.0)]
here = pathlib.Path(__file__).parent
name = pathlib.Path(__file__).stem


def ar(beta, zeta):
    return 1 / math.sqrt((beta * beta - 1) ** 2 + (2 * zeta * beta) ** 2)


betas = sorted({round(0.0025 * i, 4) for i in range(801)} | {round(0.9 + 0.0005 * i, 4) for i in range(401)})
rows = ["beta," + ",".join(k for k, _ in ZETAS)]
for b in betas:
    rows.append(f"{b:.4f}," + ",".join(f"{ar(b, z):.5f}" for _, z in ZETAS))
(here / f"{name}.csv").write_text("\n".join(rows) + "\n")

lo, hi = math.sqrt(2 / 3), math.sqrt(4 / 3)          # 1/|beta^2 - 1| = 3
left = [lo * i / 200 for i in range(201)]
right = [hi + (2 - hi) * i / 200 for i in range(201)]
z0 = ["beta,ar"] + [f"{b:.5f},{1 / abs(b * b - 1):.5f}" for b in left] + ["nan,nan"] \
     + [f"{b:.5f},{1 / abs(b * b - 1):.5f}" for b in right]
(here / f"{name}-z0.csv").write_text("\n".join(z0) + "\n")
for k, z in ZETAS:
    if z < math.sqrt(2) / 2:
        print(f"zeta_c = {z:.3f}: peak {1 / (2 * z * math.sqrt(1 - z * z)):.4f}/C_1 at beta_c = {math.sqrt(1 - 2 * z * z):.4f}")
print(f"{name}.csv: {len(betas)} points; {name}-z0.csv: two branches")
