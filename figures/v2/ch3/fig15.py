#!/usr/bin/env python3
"""Chapter 3, Figure 15: the transverse velocity (v/U_inf) sqrt(U_inf x/nu) against eta (eta vertical).

Eq. (46) (chapters/ch3-sec3a.tex): v = (1/2) sqrt(nu U_inf/x) (eta f' - f), i.e.
(v/U_inf) sqrt(U_inf x/nu) = (eta f' - f)/2, with f and f' from Table 1 (interpolated as in fig14.py, which
this script imports). As eta grows it tends to (1/2) lim (eta - f) = (8.8 - 7.07923)/2 = 0.86039: the
asymptote of eq. (56), which the figure and eq. (56) letter 0.865 (Schlichting 0.8604; corrections/v2-figures.md,
minor). The asymptote is drawn at the computed limit (it is the line the curve approaches), the printed 0.865
kept as lettering.

The curve runs to the top of the axes (eta = 8); the dashed asymptote runs from eta = 0 up to where the curve
meets it (the gap less than half the curve's line width on the 4.2 in axes), as printed.

Writes fig15.csv (v, eta) and fig15-marks.csv (vinf: the asymptote; join: the eta where the curve meets it).
"""
import pathlib
import sys

import numpy as np

sys.dont_write_bytecode = True     # (no __pycache__ beside the figures)
from fig14 import AXIS_W_PT, LINE_PT, blasius, write_csv

b = blasius()
eta = np.linspace(0.0, 8.0, 321)
v = 0.5 * (eta * b.fp(eta) - b.f(eta))                    # eq. (46)
vinf = 0.5 * b.delta_star()
gap = LINE_PT / AXIS_W_PT
join = float(eta[np.argmax(vinf - v < gap)])

here = pathlib.Path(__file__)
write_csv(here.with_suffix(".csv"), ["v", "eta"], [v, eta])
write_csv(here.with_name(here.stem + "-marks.csv"), ["vinf", "join"], [[vinf], [join]])
print(f"fig15.csv: {len(eta)} points; v(8) = {v[-1]:.5f}; asymptote {vinf:.5f} (printed 0.865), "
      f"curve within half a line width of it from eta = {join:.3f}")
