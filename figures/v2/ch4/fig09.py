#!/usr/bin/env python3
"""Chapter 4, Figure 9(a)-(c): percent error of the approximate methods for the F7 engine, against liftoff mass,
for k_min = 0.00012 and k_max = 0.0045 (the key table after Figure 5, ch4-sec2b.tex:369).

DIGITIZED, not computed. The curves are the book's interval method (83)-(87) against the Fehskens-Malewicki
(20), (21) and Caporaso-Bengen (27), (28), (67) approximations, as for Figure 6 (fig06.py), but the book does
not give the F7 engine's thrust curve (I_t, F_m, F_s, t_m, t_s) or its propellant mass, nor the twenty liftoff
masses: only t_b = 9.00 s, the engine-alone mass 0.110 kg and the largest m_o 0.300 kg (ch4-sec3.tex:219-222).
So the four printed curves of each panel are digitized from the 1973 art, figures/ch4/fig09a/b/c.png.

Calibration fig09a/b/c.calib.json (the same map tools/v2/digitize.py uses): an affine fit to every labelled and
minor tick of (a) and (b) (max residual 0.74 and 0.79 px: the scans lean by about 1 px); for (c) piecewise
linear between the drawn x ticks, which close up from 56 to 51 px across the panel (the page bends), and
between the y ticks ((c) also leans: its y axis runs 4 px to the right over its height, which moves the curves
by under 2 px, 0.001 kg, in m_o). The curves run from m_o = 0.110 kg (the engine alone, where the printed
curves start) to 0.300 kg; the (b) k_max dashed curve's first dash is printed at 0.113 and is run back to 0.110
with the others.

Method, per panel: in each scan column the ink runs (gray < 128) are matched to the four curves and the zero line
by hand-read guide polylines (pixel coordinates: a line takes the run nearest its guide within 2.5 px, and keeps
the sample only within 2 px of the guide), with the leaders and the k labels masked. A run that holds one line
gives its centre; a run where lines touch or cross (the two Fehskens-Malewicki curves of (a) and (c), the k_min
solid on the k_max dashed in (a), the solids on the zero line in (b) and (c)) gives the upper line its top edge
plus half a line width and the lower line its bottom edge minus half a line width (each line the run's centre
when the run is no thicker than one line and a pixel), at a lower weight. The samples are mapped to data and
fitted with a smoothing spline in m_o (make_smoothing_spline; the dashes' gaps and the masked leaders are
bridged by it), evaluated every 0.0025 kg.

Checks. The traced centre line lies within 0.4-0.7 px of the fitted curves for 95% of its samples (max 1.0-1.5 px)
in every curve of the three panels. tools/v2/digitize.py overlay (fig09{a,b,c}.calib.json): 95% of the points
within 0-2 px (0.34 mm; the dashed curves' gaps give the 2 px) of the scan's ink for all twelve curves; the
largest single distances are 10 px for the (b) k_max dashed curve (run back from 0.113 to 0.110, where no ink is
printed) and 3-3.6 px elsewhere.

Writes fig09a.csv (v_b), fig09b.csv (y_b), fig09c.csv (y_max): m0, fm_kmin, cb_kmin, fm_kmax, cb_kmax
(the columns of fig06a-c.csv), and prints each curve's end values and fit residuals.
"""
import json
import pathlib
import numpy as np
from PIL import Image
from scipy.interpolate import make_smoothing_spline

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent.parent
CURVES = ("fm_kmin", "cb_kmin", "fm_kmax", "cb_kmax")
W1 = 2.0          # one line's thickness in the scan at gray < 128 (px)
TOL = 2.5         # a run is a line's when its guide passes within this distance of it (px) ...
NEAR = 2.0        # ... and a sample is kept when it lies within this distance of the guide (px)
LAM = 1e4         # smoothing (y in percent, m_o in scan pixels)
X0, X1, DX = 0.110, 0.300, 0.0025

# Hand-read guides (scan column, row) for each line, the leaders (segments) and the k labels (boxes) to mask.
PANELS = {
    "a": {
        "zero": [(72, 154.0), (300, 153.2), (521, 152.3)],
        "fm_kmax": [(92, 136.5), (170, 136.5), (196, 135.5), (250, 134), (300, 132.5), (352, 130.5), (400, 129),
                    (450, 127), (521, 124.5)],
        "fm_kmin": [(92, 136.5), (170, 136.8), (202, 139), (250, 140.5), (262, 141.5), (300, 143.5), (352, 145.5),
                    (400, 147.5), (450, 149.5), (521, 151.0)],
        "cb_kmax": [(92, 139.5), (200, 139.2), (286, 139.5), (352, 141.5), (400, 142.5), (450, 144), (521, 147)],
        "cb_kmin": [(92, 182.5), (100, 184), (118, 190), (136, 195), (154, 200), (172, 204.5), (190, 208),
                    (214, 211.5), (238, 213.5), (256, 215), (286, 215.5), (316, 214.5), (340, 213.5), (370, 211),
                    (400, 209.5), (436, 206.5), (466, 204), (490, 201.5), (521, 199.5)],
        "segs": [((386, 106), (388, 129)), ((391, 106), (417, 144)), ((365, 173), (383, 148)),
                 ((362, 185), (370, 212))],
        "boxes": [(372, 90, 425, 112), (355, 170, 410, 193)],
    },
    "b": {
        "zero": [(70, 157.0), (250, 156.3), (517, 155.3)],
        "fm_kmax": [(94, 156), (118, 157), (142, 158.3), (160, 160), (184, 161.5), (214, 163.5), (250, 165.5),
                    (300, 167.5), (352, 170.8), (400, 174), (450, 177.5), (517, 181.5)],
        "fm_kmin": [(94, 148.5), (100, 149.5), (112, 151.5), (124, 153.5), (142, 156.5), (160, 160.5),
                    (184, 165.5), (214, 170.5), (250, 176), (300, 182.5), (352, 190), (400, 196.5), (450, 203.5),
                    (517, 212.5)],
        "cb_kmax": [(94, 172.5), (106, 173.5), (124, 175.5), (148, 179.5), (160, 180.5), (190, 185.5),
                    (214, 188.5), (244, 192.5), (274, 196.5), (310, 201.5), (346, 206.5), (376, 210.5),
                    (412, 215.5), (448, 219.5), (478, 223.5), (517, 228.5)],
        "cb_kmin": [(94, 209), (112, 213), (130, 216.5), (160, 221), (190, 224.5), (226, 227.5), (262, 230),
                    (292, 230.5), (328, 231.5), (364, 233), (400, 234), (430, 235), (460, 236.5), (490, 237),
                    (517, 237.5)],
        "segs": [((406, 136), (399, 174)), ((410, 138), (421, 217)), ((172, 194), (197, 170)),
                 ((155, 202), (159, 221))],
        "boxes": [(395, 118, 450, 143), (148, 188, 202, 208)],
    },
    "c": {
        "zero": [(73, 153.0), (500, 153.2)],
        "fm_kmin": [(94, 143), (124, 146.5), (148, 149), (172, 152), (190, 153.5), (214, 155.5), (250, 158.8),
                    (286, 161.5), (328, 164.5), (364, 168.5), (400, 171.5), (448, 177), (501, 183)],
        "fm_kmax": [(94, 152), (124, 153.5), (160, 155), (172, 155.5), (208, 157), (250, 159), (286, 161.5),
                    (328, 163.5), (364, 165.5), (400, 167.5), (448, 170), (501, 172.8)],
        "cb_kmax": [(94, 166), (106, 167), (124, 169), (142, 171.5), (172, 175.5), (190, 177.5), (208, 179.5),
                    (226, 181.5), (244, 184.5), (262, 186), (280, 188.5), (298, 191), (316, 193.5), (340, 196.5),
                    (358, 198.5), (376, 201), (394, 203.5), (412, 205.5), (430, 207.5), (448, 210), (472, 213.5),
                    (501, 217)],
        "cb_kmin": [(94, 195.5), (100, 196.5), (118, 200.5), (136, 204), (154, 207.5), (172, 210.5), (190, 214),
                    (208, 216.5), (226, 218.5), (244, 220.5), (262, 222), (292, 224.5), (316, 226.5), (340, 227.5),
                    (370, 228.5), (400, 229.5), (430, 229.5), (466, 230), (501, 230.5)],
        "segs": [((147, 177), (165, 156)), ((150, 183), (172, 174)), ((461, 188), (467, 180)),
                 ((461, 205), (465, 229))],
        "boxes": [(138, 177, 188, 194), (452, 186, 498, 206)],
    },
}


class Axes:
    """Pixel -> data, as tools/v2/digitize.py maps it: the least-squares affine fit to the calibration points,
    replaced on an axis by piecewise-linear interpolation between the listed ticks where xgrid/ygrid are given."""

    def __init__(self, spec):
        pts = np.array(spec["points"], float)
        self.A, *_ = np.linalg.lstsq(np.c_[pts[:, :2], np.ones(len(pts))], pts[:, 2:], rcond=None)
        self.xgrid = np.array(spec["xgrid"], float) if spec.get("xgrid") else None
        self.ygrid = np.array(spec["ygrid"], float) if spec.get("ygrid") else None

    def to_data(self, px, py):
        px, py = np.asarray(px, float), np.asarray(py, float)
        d = np.c_[px, py, np.ones(len(px))] @ self.A
        x, y = d[:, 0], d[:, 1]
        if self.xgrid is not None:
            x = np.interp(px, self.xgrid[:, 0], self.xgrid[:, 1])
        if self.ygrid is not None:
            o = np.argsort(self.ygrid[:, 0])
            y = np.interp(py, self.ygrid[o, 0], self.ygrid[o, 1])
        return x, y


def runs(v):
    """(top, bottom) rows of each ink run in a column."""
    idx = np.flatnonzero(v)
    if idx.size == 0:
        return []
    cut = np.flatnonzero(np.diff(idx) > 1)
    return list(zip(np.r_[idx[0], idx[cut + 1]], np.r_[idx[cut], idx[-1]]))


def guide(pts, c):
    p = np.array(pts, float)
    return np.interp(c, p[:, 0], p[:, 1])


def digitize(panel):
    spec = json.loads((HERE / f"fig09{panel}.calib.json").read_text())
    ax = Axes(spec["axes"]["main"])
    gray = np.asarray(Image.open(ROOT / spec["crop"]).convert("L")).astype(float)
    ink = gray < 128
    P = PANELS[panel]
    rr, cc = np.mgrid[0:ink.shape[0], 0:ink.shape[1]]
    for (x0, y0), (x1, y1) in P["segs"]:
        t = np.clip(((cc - x0) * (x1 - x0) + (rr - y0) * (y1 - y0)) / ((x1 - x0) ** 2 + (y1 - y0) ** 2), 0, 1)
        ink &= np.hypot(cc - (x0 + t * (x1 - x0)), rr - (y0 + t * (y1 - y0))) > 2.5
    for x0, y0, x1, y1 in P["boxes"]:
        ink[y0:y1, x0:x1] = False
    lines = ("zero",) + CURVES
    first = min(P[k][0][0] for k in CURVES)
    last = max(P[k][-1][0] for k in CURVES)
    samples = {k: [] for k in CURVES}
    for c in range(first, last + 1):
        pred = {k: guide(P[k], c) for k in lines}
        rs = [(t + 100, b + 100) for t, b in runs(ink[100:260, c])]
        if not rs:
            continue
        # each line takes the run nearest its guide (distance to the run's extent), if within TOL
        owner = {}
        for k in lines:
            d = [max(t - pred[k], pred[k] - b, 0) for t, b in rs]
            i = int(np.argmin(d))
            if d[i] <= TOL:
                owner.setdefault(i, []).append(k)
        for i, (top, bot) in enumerate(rs):
            mine = sorted(owner.get(i, []), key=lambda k: pred[k])
            if not mine:
                continue
            centre, width = (top + bot) / 2, bot - top + 1
            if len(mine) == 1:
                if width <= W1 + 1.5:
                    found = {mine[0]: (centre, 1.0)}
                else:
                    continue
            elif width <= W1 + 1:      # lines that coincide here: the run's centre for each
                found = {k: (centre, 0.3) for k in mine}
            else:                      # touching or crossing lines: the outer ones from the run's edges
                found = {mine[0]: (top - 0.5 + W1 / 2, 0.3), mine[-1]: (bot + 0.5 - W1 / 2, 0.3)}
            for k, (row, w) in found.items():
                if k != "zero" and abs(row - pred[k]) <= NEAR:
                    samples[k].append((c, row, w))
    out = {}
    for k in CURVES:
        s = np.array(samples[k], float)
        x, y = ax.to_data(s[:, 0], s[:, 1])
        o = np.argsort(x)
        x, y, w = x[o], y[o], s[o, 2]
        keep = np.r_[True, np.diff(x) > 1e-7]
        x, y, w = x[keep], y[keep], w[keep]
        u = (x - 0.1) / 0.025 * 56.0           # m_o in scan pixels, so lam is in px^3 as in the Ch3 scripts
        f = make_smoothing_spline(u, y, w=w, lam=LAM)
        res = y - f(u)
        out[k] = (f, x, y, res)
    return out


def main():
    grid = np.round(np.arange(X0, X1 + 1e-9, DX), 4)
    for panel, q in zip("abc", ("v_b", "y_b", "y_max")):
        fits = digitize(panel)
        u = (grid - 0.1) / 0.025 * 56.0
        cols = {k: fits[k][0](u) for k in CURVES}
        rows = ["m0," + ",".join(CURVES)]
        rows += [f"{m:.4f}," + ",".join(f"{cols[k][i]:.3f}" for k in CURVES) for i, m in enumerate(grid)]
        (HERE / f"fig09{panel}.csv").write_text("\n".join(rows) + "\n")
        print(f"fig09{panel}.csv (percent error in {q}): {len(grid)} masses")
        for k in CURVES:
            f, x, y, res = fits[k]
            print(f"  {k}: {len(x)} samples, x {x.min():.4f}-{x.max():.4f}; {cols[k][0]:+.2f} at {X0}, "
                  f"{cols[k][len(grid) // 2]:+.2f} at {grid[len(grid) // 2]:.3f}, {cols[k][-1]:+.2f} at {X1}; "
                  f"fit residual 95% {np.percentile(np.abs(res), 95):.3f} (percentage points)")


if __name__ == "__main__":
    main()
