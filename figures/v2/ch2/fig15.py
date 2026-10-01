#!/usr/bin/env python3
"""Chapter 2, Figure 15: a step disturbance of intensity M_s (scan: figures/ch2/fig15.png).

The step input as the text defines it (unnumbered display before eq. (27)): f_x(t) = 0 for t < 0 and
f_x(t) = M_s for t >= 0; the riser at t = 0 is drawn on the vertical axis, as in the scan. Units: M_X in
units of M_s; t in units of the half-width of the plot (the scan's t axis runs equally far either side of
the origin, and its M_s line to the t axis's right end). Sampled densely so that the overlay on the scan
checks the whole path. Writes fig15.csv (t, M).
"""
import pathlib

MS = 1.0
n = 200
pts = [(-1 + i / n, 0.0) for i in range(n + 1)]            # f_x = 0, t < 0 (along the t axis)
pts += [(0.0, MS * i / 50) for i in range(1, 51)]           # the step at t = 0
pts += [(i / n, MS) for i in range(1, n + 1)]               # f_x = M_s, t >= 0
out = pathlib.Path(__file__).with_suffix(".csv")
out.write_text("t,M\n" + "\n".join(f"{t:.4f},{m:.4f}" for t, m in pts) + "\n")
print(f"{out.name}: {len(pts)} points")
