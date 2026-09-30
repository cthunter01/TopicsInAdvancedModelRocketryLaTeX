#!/usr/bin/env python3
"""The B4 thrust-time curve as traced in Chapter 1 Figure 4 (panel (a) of figures/ch1/fig04a.png), for the four
panels of that figure only: its lettered results (the rectangle areas of (b), the 49.7 squares of (c), the
weights of (d)) were read off this tracing, which falls from the spike more slowly than the 1994 one shared by
the other B4 figures (b4.py; corrections/v2-figures.md, rule 5 and its exception).

Axes calibrated at the labelled ticks (0, .4, .8, 1.2 sec; 0-16 N). The spike is read row by row (the rise is
the run left of the peak, the fall the run right of it), the plateau column by column; one parametric
smoothing spline through the ordered points. Writes b4-1973.csv (t in sec, F in N) and prints the area.
"""
import pathlib
import numpy as np
from PIL import Image
from scipy.interpolate import splprep, splev

HERE = pathlib.Path(__file__).parent
ROOT = HERE.parent.parent.parent
CROP = ROOT / "figures/ch1/fig04a.png"
XT = [(94.5, 0), (145.5, 0.4), (199.0, 0.8), (252.5, 1.2)]
YT = [(299.5, 0), (255.5, 4), (210.5, 8), (165.5, 12), (120.5, 16)]


def t_of(px):
    return float(np.interp(px, [p for p, _ in XT], [v for _, v in XT]))


def f_of(py):
    return float(np.interp(-py, [-p for p, _ in YT], [v for _, v in YT]))


def runs(v, off):
    idx = np.flatnonzero(v) + off
    if idx.size == 0:
        return []
    cut = np.flatnonzero(np.diff(idx) > 1)
    return [((s + e) / 2) for s, e in zip(np.r_[idx[0], idx[cut + 1]], np.r_[idx[cut], idx[-1]])]


ink = np.asarray(Image.open(CROP).convert("L")) < 128
top = min(r for r in range(140, 170) if runs(ink[r, 100:135], 100))           # the highest row of the spike
peak_x = float(np.mean(runs(ink[top, 100:135], 100)))
rise = [(runs(ink[r, 97:int(peak_x)], 97)[0], r) for r in range(294, top, -1) if runs(ink[r, 97:int(peak_x)], 97)]
fall = [(runs(ink[r, int(peak_x) + 1:140], int(peak_x) + 1)[-1], r) for r in range(top + 1, 256)
        if runs(ink[r, int(peak_x) + 1:140], int(peak_x) + 1)]
fall_c = max(x for x, r in fall)
plat, last = [], 259.0
for c in range(int(fall_c) + 2, 250):
    rr = runs(ink[240:285, c], 240)
    if rr:
        best = min(rr, key=lambda y: abs(y - last))
        if abs(best - last) < 5:
            last = best
            plat.append((float(c), best))
P = np.array([(94.5, 297.0, 5)] + [(x, r, 1) for x, r in rise] + [(peak_x, top - 0.5, 20)]
             + [(x, r, 1) for x, r in fall] + [(x, y, 1) for x, y in plat], float)
for _ in range(2):
    tck, u = splprep([P[:, 0], P[:, 1]], w=P[:, 2], s=len(P) * 1.0 ** 2)
    fx, fy = splev(u, tck)
    P = P[(np.hypot(fx - P[:, 0], fy - P[:, 1]) < 2.0) | (P[:, 2] > 1)]
sx, sy = splev(np.linspace(0, 1, 600), tck)
pts = [(0.0, 0.0)] + [(t_of(x), max(0.0, f_of(y))) for x, y in zip(sx, sy) if t_of(x) > 0]
pts += [(1.2, pts[-1][1]), (1.2, 0.0)]
keep = [pts[0]]
for p in pts[1:]:
    if abs(p[0] - keep[-1][0]) >= 0.002 or abs(p[1] - keep[-1][1]) >= 0.05:
        keep.append(p)
arr = np.array(keep)
(HERE / "b4-1973.csv").write_text("t,F\n" + "\n".join(f"{t:.4f},{F:.3f}" for t, F in arr) + "\n")
area = float(np.trapezoid(arr[:, 1], arr[:, 0]))
print(f"b4-1973.csv: {len(arr)} points; peak {arr[:, 1].max():.2f} N at {arr[arr[:, 1].argmax(), 0]:.3f} sec; "
      f"plateau {np.median(arr[(arr[:, 0] > 0.4) & (arr[:, 0] < 1.1), 1]):.2f} N; area {area:.3f} N-sec "
      f"(Fig 4(b) 5.20, (c) 4.97, actual 5.0)")
