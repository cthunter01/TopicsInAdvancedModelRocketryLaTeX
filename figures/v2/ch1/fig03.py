#!/usr/bin/env python3
"""Chapter 1, Figure 3(a): the mass curve m(t). It passes through the values of the table in panel (b)
(t = 0.2 ... 1.2 sec) and, before them, the steep start and rounded knee read off the scan at the line's centre
(21 g at t = 0; 19.2, 18.3, 17.3, 16.35, 15.85 g at 0.05, 0.075, 0.10, 0.125, 0.15 sec); monotone cubic (PCHIP)
interpolation between. Writes fig03.csv (t, m)."""
import pathlib
from scipy.interpolate import PchipInterpolator
import numpy as np

T = [0.0, 0.05, 0.075, 0.10, 0.125, 0.15, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2]
M = [21.0, 19.2, 18.3, 17.3, 16.35, 15.85, 15.1, 12.8, 11.3, 10.2, 9.4, 9.0]
f = PchipInterpolator(T, M)
t = np.linspace(0, 1.2, 121)
out = pathlib.Path(__file__).with_suffix(".csv")
out.write_text("t,m\n" + "\n".join(f"{a:.3f},{b:.3f}" for a, b in zip(t, f(t))) + "\n")
print(f"{out.name}: {len(t)} points")
