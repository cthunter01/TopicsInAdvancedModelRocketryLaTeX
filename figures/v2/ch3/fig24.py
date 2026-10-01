#!/usr/bin/env python3
"""Chapter 3, Figure 24: pressure coefficient on a circular cylinder against the angle phi from point A.

Theory (computed): C_p = 1 - 4 sin^2(phi), the potential-flow distribution the figure letters and the text
quotes (ch3-sec3c-sec4a.tex, "the curve C_p = 1 - 4 sin^2 phi"); 1 at 0 and 180 degrees, -3 at 90.
Experiment (digitized; average curves after Hoerner, ref. 9, no equation in the book): the supercritical
R_d = 3 x 10^5 (short dashes in the print) and the subcritical R_d = 6 x 10^4 (long dashes, solid through its
dip, dash-dot on its plateau). Traced from figures/ch3/fig24.png against fig24.calib.json (gridline crossings;
the scan is turned about 0.4 degrees, which the affine fit takes out), column by column on the gentle parts
and row by row on the steep rise of the 3 x 10^5 curve, with the gridlines masked and the dashes bridged;
then a smoothing spline (0.008 in C_p, about half a pixel). Below about 20 degrees the three curves run within
a pixel or two of one another into C_p = 1, too close to trace: there each experimental curve is the theory
plus a small correction that joins the trace at 22 (3 x 10^5) or 20 (6 x 10^4) degrees with its value and
slope and vanishes at C_p(0) = 1 with zero slope (smooth_resample).
Writes fig24.csv (phi in degrees, theory), fig24-r3e5.csv and fig24-r6e4.csv (phi, C_p).
"""
import json
import pathlib
import numpy as np
from PIL import Image
from scipy.interpolate import UnivariateSpline

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent.parent
spec = json.loads((HERE / "fig24.calib.json").read_text())
CROP = ROOT / spec["crop"]
P = np.array(spec["axes"]["main"]["points"], float)

# pixel <-> data: least-squares affine map (as tools/v2/digitize.py)
A, *_ = np.linalg.lstsq(np.c_[P[:, :2], np.ones(len(P))], P[:, 2:], rcond=None)
B, *_ = np.linalg.lstsq(np.c_[P[:, 2:], np.ones(len(P))], P[:, :2], rcond=None)


def to_data(px, py):
    d = np.c_[px, py, np.ones(len(px))] @ A
    return d[:, 0], d[:, 1]


def to_pixel(x, y):
    p = np.c_[x, y, np.ones(len(x))] @ B
    return p[:, 0], p[:, 1]


gray = np.asarray(Image.open(CROP).convert("L"))
ink = gray < 128
# mask the gridlines (every 20 degrees, every unit of C_p), 2 px either side of their drawn centre lines
H, W = ink.shape
yy, xx = np.mgrid[0:H, 0:W]
dx, dy = to_data(xx.ravel().astype(float), yy.ravel().astype(float))
dx, dy = dx.reshape(H, W), dy.reshape(H, W)
sx = 416 / 180.0          # px per degree
sy = 287 / 4.0            # px per unit of C_p
grid = (np.abs(dx - 20 * np.round(dx / 20)) * sx < 2.2) | (np.abs(dy - np.round(dy)) * sy < 2.2)
clean = ink & ~grid


def runs(v, maxlen=7):
    idx = np.flatnonzero(v)
    if idx.size == 0:
        return []
    cut = np.flatnonzero(np.diff(idx) > 1)
    s, e = np.r_[idx[0], idx[cut + 1]], np.r_[idx[cut], idx[-1]]
    return [(a + b) / 2 for a, b in zip(s, e) if b - a + 1 <= maxlen]


def trace(seed, stop, mode="cols", max_jump=3.0, max_gap=14, flat=False):
    """Follow a curve from seed (px, py) to the column (cols) or row (rows) `stop`; returns pixel points."""
    m = clean if mode == "cols" else clean.T
    u, v = (seed[0], seed[1]) if mode == "cols" else (seed[1], seed[0])
    u = int(round(u)); step = 1 if stop > u else -1
    c = runs(m[:, u]); v = min(c, key=lambda r: abs(r - v)) if c else v
    pts, last, slope = [(u, v)], u, 0.0
    u += step
    while (u - stop) * step <= 0:
        gap = abs(u - last)
        pred = pts[-1][1] + slope * (u - last)
        c = runs(m[:, u])
        best = min(c, key=lambda r: abs(r - pred)) if c else None
        if best is not None and abs(best - pred) <= max_jump * max(1.0, gap / 2):
            new = (best - pts[-1][1]) / (u - last)
            slope = 0.0 if flat else (new if len(pts) < 2 else 0.6 * slope + 0.4 * new)
            pts.append((u, best)); last = u
        elif gap > max_gap:
            break
        u += step
    a = np.array(pts, float)
    return a if mode == "cols" else a[:, ::-1]


def join(*pieces):
    a = np.vstack(pieces)
    x, y = to_data(a[:, 0], a[:, 1])
    return x, y


def theory(phi):
    return 1 - 4 * np.sin(np.radians(phi)) ** 2


def smooth_resample(x, y, cut, sigma=0.008):
    """A smoothing spline through the traced points beyond `cut` degrees, resampled every degree from 0 to 180.

    Below `cut` the experimental curves run within a pixel or two of the theory and of each other, too close
    to trace: there the curve is the theory plus a correction d (phi/cut)^n that joins the spline with its
    value d and slope at `cut` and vanishes at phi = 0 with zero slope (n >= 2: C_p(0) = 1, the curve flat at
    the stagnation point as the flow is symmetric). Beyond the last traced point the plateau is held flat."""
    keep = x >= cut
    x, y = x[keep], y[keep]
    o = np.argsort(x, kind="stable"); x, y = x[o], y[o]
    x, idx = np.unique(np.round(x, 3), return_index=True); y = y[idx]
    spl = UnivariateSpline(x, y, k=3, s=len(x) * sigma ** 2)
    h = 1e-3
    dc = float(spl(cut) - theory(cut))
    dd = float((spl(cut + h) - spl(cut - h)) / (2 * h) - (theory(cut + h) - theory(cut - h)) / (2 * h))
    n = max(2.0, cut * dd / dc) if dc > 0 else 2.0
    gx = np.arange(0.0, 180.0 + 1e-9, 1.0)
    gy = spl(np.minimum(gx, x[-1]))
    lo = gx < cut
    gy[lo] = theory(gx[lo]) + dc * (gx[lo] / cut) ** n
    return gx, gy


def write(name, x, y, header="phi,cp"):
    rows = [header] + [f"{a:.2f},{b:.4f}" for a, b in zip(x, y)]
    (HERE / name).write_text("\n".join(rows) + "\n")
    print(f"{name}: {len(x)} points")


# theory
phi = np.arange(0, 181, 1.0)
write("fig24.csv", phi, theory(phi))

# R_d = 3 x 10^5 (the middle curve on the falling branch)
p1 = trace((216, 239.5), 44)                    # minimum to the start
p2 = trace((216, 239.5), 265)                   # minimum to the foot of the rise
p3 = trace((272, 204.5), 122, mode="rows", max_jump=2.5)  # the steep rise, row by row (from right of
                                                          # the 100-degree gridline)
p4 = trace((p3[-1, 0], p3[-1, 1]), 452, max_jump=1.5, flat=True)  # plateau (the theory crosses it)
x, y = join(p1, p2, p3, p4)
xr, yr = smooth_resample(x, y, cut=22)
write("fig24-r3e5.csv", xr, yr)

# R_d = 6 x 10^4 (the upper curve on the falling branch, its dip and plateau)
q1 = trace((136, 112), 44)
q2 = trace((136, 112), 236)                     # through the dip to the step at about 80 degrees
q3 = trace((240, 168.5), 452, max_jump=1.5, flat=True)   # the plateau (the theory crosses it at 135 deg)
x, y = join(q1, q2, q3)
xr, yr = smooth_resample(x, y, cut=20)
write("fig24-r6e4.csv", xr, yr)
