#!/usr/bin/env python3
"""Chapter 3, Figure 35: the apparent mass factor (k_2 - k_1) against body fineness ratio l_b/d, 4 to 20.

The book takes the curve from Hopkins (its reference 6; Munk's apparent-mass factor) and prints no formula.
Munk's factor is Lamb's result for the prolate spheroid (owner's decision: compute from it). For a spheroid
of fineness ratio f = l_b/d (semi-axes a = f b), eccentricity e = sqrt(1 - 1/f^2):

    alpha_o = (2 (1 - e^2) / e^3) (ln((1 + e)/(1 - e))/2 - e)
    beta_o  = 1/e^2 - ((1 - e^2) / (2 e^3)) ln((1 + e)/(1 - e))
    k_1 = alpha_o / (2 - alpha_o)   (axial),   k_2 = beta_o / (2 - beta_o)   (transverse)

(H. Lamb, Hydrodynamics, 6th ed., art. 373.) It gives (k_2 - k_1) = 0.971 at l_b/d = 16, the text's 0.97
(ch3-sec5a), 0.778 at 4 where the printed curve starts. Checked against the scan with
tools/v2/digitize.py overlay (fig35.calib.json).
"""
import math
import pathlib


def k2_minus_k1(f):
    e = math.sqrt(1 - 1 / f**2)
    L = math.log((1 + e) / (1 - e))
    a0 = 2 * (1 - e * e) / e**3 * (0.5 * L - e)
    b0 = 1 / e**2 - (1 - e * e) / (2 * e**3) * L
    return b0 / (2 - b0) - a0 / (2 - a0)


out = pathlib.Path(__file__).with_suffix(".csv")
xs = [4 + 0.05 * i for i in range(40)] + [6 + 0.25 * i for i in range(57)]   # finer where it bends
rows = ["f,k"] + [f"{f:.2f},{k2_minus_k1(f):.5f}" for f in xs]
out.write_text("\n".join(rows) + "\n")
print(f"{out.name}: {len(rows) - 1} points, (k2-k1)(4) = {k2_minus_k1(4):.4f}, (16) = {k2_minus_k1(16):.4f}")
