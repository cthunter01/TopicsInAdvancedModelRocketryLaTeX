#!/usr/bin/env python3
"""Chapter 3, Figure 21: laminar velocity profiles u/U against eta, (a) flat plate, (b) cone.

(a) Eq. (96) (chapters/ch3-sec3b.tex): the eta of Ref. 3 is half the Blasius eta_B, so u/U = f'(2 eta_2-D):
Fig 14's curve with the vertical scale halved, as the text says (f' from Table 1, interpolated as in fig14.py,
imported).
(b) The cone's profile by Mangler's transformation (outside the book; owner's decision,
corrections/v2-figures.md): the flat plate's at x/3, u/U = f'(sqrt(3) eta_B) = f'(2 sqrt(3) eta_3-D) (as Fig 20).

Each curve is drawn until it meets the u/U = 1.0 border (the gap 1 - u/U less than half the curve's line width
on the 1.74 in panel), as the 1973 curves end there (about eta = 2.6 and 1.5).

Writes fig21-a.csv and fig21-b.csv (u, eta).
"""
import math
import pathlib
import sys

import numpy as np

sys.dont_write_bytecode = True     # (no __pycache__ beside the figures)
from fig14 import LINE_PT, blasius, write_csv

PANEL_W_PT = 1.74 * 72.27        # each panel's axes: 1.74 in
b = blasius()
end_B = b.meets(LINE_PT / PANEL_W_PT)    # the Blasius eta where 1 - f' = half a line width
here = pathlib.Path(__file__)
for key, scale in (("a", 2.0), ("b", 2.0 * math.sqrt(3.0))):
    eta = np.linspace(0.0, end_B / scale, 201)
    out = here.with_name(f"{here.stem}-{key}.csv")
    write_csv(out, ["u", "eta"], [b.fp(scale * eta), eta])
    print(f"{out.name}: {len(eta)} points, eta 0 to {eta[-1]:.3f} (u/U = {float(b.fp(end_B)):.5f})")
