#!/usr/bin/env python3
"""Chapter 3, Figure 34: base drag coefficient C_Db against forebody friction drag coefficient C_fb.

The curve is the book's empirical fit, eq. (125): C_Db = 0.029 / sqrt(C_fb) (lettered on the figure as
.029/sqrt(C_fb)), drawn from where it enters the frame at C_Db = 0.30, C_fb = (0.029/0.30)^2 = 0.00934, to
C_fb = 0.8 (C_Db = 0.0324). The caption's experimental data are not drawn (as printed). Checked against the
scan with tools/v2/digitize.py overlay (fig34.calib.json, axes steep and tail). Writes fig34.csv.
"""
import math
import pathlib

x0 = (0.029 / 0.30) ** 2
# geometric spacing through the bend, then even steps
xs = [x0 * (0.1 / x0) ** (i / 40) for i in range(40)] + [0.1 + 0.0125 * i for i in range(57)]
out = pathlib.Path(__file__).with_suffix(".csv")
out.write_text("cfb,cdb\n" + "".join(f"{x:.6f},{0.029 / math.sqrt(x):.6f}\n" for x in xs))
print(f"{out.name}: {len(xs)} points, C_fb {xs[0]:.5f} .. {xs[-1]:.4f}")
