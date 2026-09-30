#!/usr/bin/env python3
"""The NAR B4 thrust-time curve, digitized once for every figure that draws it (corrections/v2-figures.md,
rule 5): Chapter 1 Figures 4 and 5(a), Chapter 4 Figure 4 and its 1994 replacement.

Source: the 1994 replacement of Chapter 4 Figure 4 (figures/supplement/ch4-fig04-1994.png, the largest and
cleanest tracing; axes calibrated at every labelled tick, see CAL). The spike is read row by row: on the rise
the solid "Actual curve" is the ink run right of the dashed approximation; on the fall it is the run left of
the dashed line above about 5 N and right of it below. The plateau is traced column by column. Writes b4.csv
(t in sec, F in N) and checks the area against the total impulse, 5.0 N-sec.
"""
import pathlib
import numpy as np
from PIL import Image

HERE = pathlib.Path(__file__).parent
ROOT = HERE.parent.parent.parent
CROP = ROOT / "figures/supplement/ch4-fig04-1994.png"
XT = [(117.5, 0), (249, 0.2), (381.5, 0.4), (514.5, 0.6), (649.5, 0.8), (782.5, 1.0), (915.5, 1.2)]
YT = [(571, 0), (503, 2), (434.5, 4), (366.5, 6), (297.5, 8), (229, 10), (160.5, 12), (92, 14), (23.5, 16)]


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


from scipy.interpolate import UnivariateSpline


def robust_spline(u, v, sigma=0.7):
    """Smoothing spline v(u) (u strictly increasing) fitted twice, dropping points more than 2.5 px off the first
    fit (stray pixels of the dashed approximation or lettering); sigma = expected pixel noise."""
    u, v = np.asarray(u, float), np.asarray(v, float)
    sp = UnivariateSpline(u, v, s=len(u) * sigma ** 2)
    ok = np.abs(sp(u) - v) < 2.5
    return UnivariateSpline(u[ok], v[ok], s=ok.sum() * sigma ** 2)


ink = np.asarray(Image.open(CROP).convert("L")) < 128
# rise: rows from just above the axis to the top of the spike, the rightmost run left of the peak
rise = [(r, runs(ink[r, 119:212], 119)[-1]) for r in range(130, 567) if runs(ink[r, 119:212], 119)]
# fall: the leftmost run right of the peak above ~5 N (row 390), the rightmost below
fall = []
for r in range(130, 440):
    rr = runs(ink[r, 213:285], 213)
    if rr:
        fall.append((r, rr[0] if r <= 390 else rr[-1]))
# plateau: column by column, the run nearest the previous row (the dashed line sits ~5 px lower)
plat, last = [], 441.0
for c in range(285, 912):
    rr = runs(ink[380:470, c], 380)
    if rr:
        best = min(rr, key=lambda y: abs(y - last))
        if abs(best - last) < 8:
            last = best
            plat.append((c, best))
from scipy.interpolate import splprep, splev
# the whole curve as one parametric smoothing spline through the ordered points: rise, the rounded top
# (weighted so the smoothing keeps the peak), the fall while it is steep (to about 4.4 N, row 420), then the
# plateau by columns; fitted twice with the stray points (> 2.5 px off the first fit) dropped
fall_c = max(x for r, x in fall if r <= 420)
seq = ([(117.5, 571.0, 5)] + [(x, r, 1) for r, x in rise[::-1]] + [(212.0, 127.5, 25)]
       + [(x, r, 1) for r, x in fall if r <= 420] + [(c, y, 1) for c, y in plat if c > fall_c + 2])
P = np.array(seq, float)
for _ in range(2):
    tck, u = splprep([P[:, 0], P[:, 1]], w=P[:, 2], s=len(P) * 0.8 ** 2)
    fx, fy = splev(u, tck)
    P = P[(np.hypot(fx - P[:, 0], fy - P[:, 1]) < 2.5) | (P[:, 2] > 1)]
sx, sy = splev(np.linspace(0, 1, 900), tck)
curve = list(zip(sx, sy))
pts = [(t_of(x), f_of(y)) for x, y in curve]
pts = [(0.0, 0.0)] + [p for p in pts[1:] if p[0] > 0] + [(1.2, pts[-1][1]), (1.2, 0.0)]
# thin: keep points at least 0.002 sec or 0.05 N apart
keep = [pts[0]]
for p in pts[1:]:
    if abs(p[0] - keep[-1][0]) >= 0.002 or abs(p[1] - keep[-1][1]) >= 0.05:
        keep.append(p)
arr = np.array(keep)
area = float(np.trapezoid(arr[:, 1], arr[:, 0]))
(HERE / "b4.csv").write_text("t,F\n" + "\n".join(f"{t:.4f},{F:.3f}" for t, F in arr) + "\n")
print(f"b4.csv: {len(arr)} points; peak {arr[:, 1].max():.2f} N at {arr[arr[:, 1].argmax(), 0]:.3f} sec; "
      f"plateau {np.median(arr[(arr[:, 0] > 0.4) & (arr[:, 0] < 1.1), 1]):.2f} N; area {area:.3f} N-sec (I_t = 5.0)")
