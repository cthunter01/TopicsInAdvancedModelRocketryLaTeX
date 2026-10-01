#!/usr/bin/env python3
"""Chapter 2, Figure 24: phase angle against frequency ratio, steady-state response to sinusoidal forcing.

Eq. (48a), phi = arctan[2 zeta beta / (beta^2 - 1)], with the arctangent extended to run continuously from
0 to -pi (chapters/ch2-sec3b.tex:456-462), i.e. phi = -atan2(2 zeta beta, 1 - beta^2), for the figure's
damping ratios zeta = .2, .5, sqrt(2)/2, 1, 2 over beta = 0 ... 2.00 (the axis).
zeta = 0 is the step: phi = 0 for beta < 1, a vertical drop at beta = 1, phi = -pi for beta > 1.

Writes fig24.csv (beta, z02, z05, z07, z1, z2: phi in radians) and fig24-z0.csv (beta, phi: the step).
"""
import math, pathlib

ZETAS = [("z02", 0.2), ("z05", 0.5), ("z07", math.sqrt(2) / 2), ("z1", 1.0), ("z2", 2.0)]
here = pathlib.Path(__file__).parent
name = pathlib.Path(__file__).stem


def phi(beta, zeta):
    return -math.atan2(2 * zeta * beta, 1 - beta * beta) + 0.0  # + 0.0: no "-0"


# 0.0025 steps, and 0.0005 steps for 0.9 < beta < 1.1 where zeta = .2 turns fast (slope -1/zeta at beta = 1)
betas = sorted({round(0.0025 * i, 4) for i in range(801)} | {round(0.9 + 0.0005 * i, 4) for i in range(401)})
rows = ["beta," + ",".join(k for k, _ in ZETAS)]
for b in betas:
    rows.append(f"{b:.4f}," + ",".join(f"{phi(b, z):.5f}" for _, z in ZETAS))
(here / f"{name}.csv").write_text("\n".join(rows) + "\n")
(here / f"{name}-z0.csv").write_text(
    "beta,phi\n0,0\n1,0\n1,{p:.5f}\n2,{p:.5f}\n".format(p=-math.pi))
print(f"{name}.csv: {len(betas)} points; {name}-z0.csv: the zeta = 0 step")
