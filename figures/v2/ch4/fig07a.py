#!/usr/bin/env python3
"""Chapter 4, Figure 7(a): percent error in v_b of the approximate methods, D4 engine (digitized).

The curves are the errors of the Fehskens-Malewicki solution, eqs. (20), (21), and of the Caporaso-Bengen
solution, eqs. (27), (28), against the interval method (83)-(87), for k_min = .00007 and k_max = .0027 kg/m
(the key table after Figure 5, ch4-sec2b.tex:356-372). The book gives neither the D4 thrust curve nor its
propellant mass (only t_b = 2.90 s, ch4-sec3.tex:201), nor the twenty liftoff masses (ch4-sec2b.tex:314-317),
so the interval solution cannot be rerun as for Figure 6 (fig06.py): the four printed curves are digitized
from the 1973 art, figures/ch4/fig07a.png (rule: compute else digitize, corrections/v2-figures.md "Ch4 Figs
5, 7-10, 12-14"). Each curve keeps its printed extent (m_o about .031 to .124 kg here).

Method. Calibration fig07a.calib.json (read on the crop at 150 dpi): x piecewise linear between the drawn
ticks (xgrid; their spacing shrinks from 48.5 to 43.5 px across the axis), y the affine fit to the y ticks,
the x axis (-15) and the zero line (0) at every tick column (the hand-drawn axes are not quite square; the fit
is within 1.2 px of every point). Each curve is followed from a hand-read guide (GUIDE: pixel points read
from 3-8x zooms of the crop): along the normal of the guide, the darkness-weighted centre of the ink run
nearest the guide is taken if it is within a few pixels and no longer than 5 px (longer runs are leaders,
crossings or lines merged with it); runs in the `exclude` column ranges (crossings, merges with the zero
line or another curve) are dropped and bridged; `extra` adds points read by hand where the ink of two lines
is one run (a curve lying on the zero line or on another curve). The centres are smoothed with a parametric
smoothing spline in chord length (s = n * sigma^2 px^2, sigma = 0.5 px unless a curve's `sigma` says less),
snapped again to that spline with a tighter window, smoothed again, mapped to data coordinates and written on a
common m_o grid (every 0.00025 kg here, plus each curve's ends; nan outside a curve). A curve that leaves the top of the frame is cut at 15%. A curve with a sharp
corner (the k_min curves of Fig 8(c)) takes a `corner` pixel: its two sides are traced and smoothed apart and
joined there (trace_cornered), and the grid gets a row at the corner.

Overlay of the written curves on the crop (tools/v2/digitize.py overlay): 95% of the points lie within
0 px of the ink for the solids and 2 px for the dashed curves (the gaps between dashes): all pass (3 px).

Writes fig07a.csv: m0, fm_kmin, cb_kmin, fm_kmax, cb_kmax (percent).
This module also holds the helpers that fig07b.py, fig07c.py and fig08a-c.py import (`digitize_panel`).
"""
import json
import pathlib
import sys

import numpy as np
from PIL import Image
from scipy import ndimage
from scipy.interpolate import PchipInterpolator, splev, splprep

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent.parent
sys.path.insert(0, str(ROOT / "tools" / "v2"))
import digitize  # noqa: E402  (the calibration maths, Axes, shared with the overlay check)

COLS = ("fm_kmin", "cb_kmin", "fm_kmax", "cb_kmax")


def load(name):
    """Darkness (0 white .. 1 black) of the crop, and its calibration."""
    spec = json.loads((HERE / f"{name}.calib.json").read_text())
    ax = digitize.Axes(spec["axes"]["main"])
    g = np.asarray(Image.open(ROOT / spec["crop"]).convert("L"), float)
    return (255.0 - g) / 255.0, ax


def guide(anchors, step=0.5):
    """A polyline through the hand-read pixel points (PCHIP in the column: no overshoot), by arc length."""
    a = np.array(sorted(anchors), float)
    f = PchipInterpolator(a[:, 0], a[:, 1])
    xs = np.arange(a[0, 0], a[-1, 0] + 1e-9, 0.25)
    p = np.c_[xs, f(xs)]
    s = np.r_[0, np.cumsum(np.hypot(*np.diff(p, axis=0).T))]
    t = np.arange(0, s[-1], step)
    return np.c_[np.interp(t, s, p[:, 0]), np.interp(t, s, p[:, 1])]


def snap(dark, path, win, maxlen=5.0, thr=0.5, reach=4.0):
    """Along the normal at each point of the path, the centre of the ink run (darkness > thr) nearest the
    path, if within `win` px and no longer than `maxlen` px."""
    d = np.gradient(path, axis=0)
    d /= np.hypot(d[:, 0], d[:, 1])[:, None]
    n = np.c_[-d[:, 1], d[:, 0]]
    ks = np.arange(-win - reach, win + reach + 1e-9, 0.25)
    out = []
    for p, nn in zip(path, n):
        prof = ndimage.map_coordinates(dark, [p[1] + ks * nn[1], p[0] + ks * nn[0]], order=1, mode="constant")
        idx = np.flatnonzero(prof > thr)
        if idx.size == 0:
            continue
        cut = np.flatnonzero(np.diff(idx) > 1)
        best = None
        for s0, e0 in zip(np.r_[idx[0], idx[cut + 1]], np.r_[idx[cut], idx[-1]]):
            if s0 == 0 or e0 == len(ks) - 1:
                continue                                  # cut by the window: length unknown
            w = prof[s0:e0 + 1]
            c = float(np.sum(ks[s0:e0 + 1] * w) / np.sum(w))
            if abs(c) <= win and (e0 - s0 + 1) * 0.25 <= maxlen and (best is None or abs(c) < abs(best)):
                best = c
        if best is not None:
            out.append(p + best * nn)
    return np.array(out).reshape(-1, 2)


def keep(pts, exclude, extra):
    m = np.ones(len(pts), bool)
    for c0, c1 in exclude:
        m &= ~((pts[:, 0] >= c0) & (pts[:, 0] <= c1))
    pts = np.r_[pts[m], np.array(extra, float).reshape(-1, 2)]
    return pts[np.argsort(pts[:, 0], kind="stable")]


def smooth(pts, sigma=0.5, step=0.5, pin=None, knots=None):
    """Parametric smoothing spline in chord length through the centres, evaluated every `step` px. With `pin`
    and `knots` (for one side of a corner, see trace_cornered): instead the weighted least-squares cubic
    spline with interior knots every `knots` px of chord length, the point `pin` (among the centres) weighted
    20 so that the spline ends on it."""
    pts = pts[np.r_[True, np.hypot(*np.diff(pts, axis=0).T) > 0.05]]
    u = np.r_[0, np.cumsum(np.hypot(*np.diff(pts, axis=0).T))]
    if pin is None:
        tck, _ = splprep([pts[:, 0], pts[:, 1]], u=u, s=len(pts) * sigma ** 2, k=3)
    else:
        w = np.where(np.hypot(pts[:, 0] - pin[0], pts[:, 1] - pin[1]) < 1e-6, 20.0, 1.0)
        n = max(1, int(round(u[-1] / knots)))
        t = np.r_[[0.0] * 4, np.linspace(0, u[-1], n + 1)[1:-1], [u[-1]] * 4]
        tck, _ = splprep([pts[:, 0], pts[:, 1]], u=u, w=w, task=-1, t=t, k=3)
    x, y = splev(np.arange(0, u[-1] + 1e-9, step), tck)
    return np.c_[x, y]


def trace(dark, spec):
    if "corner" in spec:
        return trace_cornered(dark, spec)
    win = spec.get("win", (4.0, 2.0))
    kw = dict(maxlen=spec.get("maxlen", 5.0), thr=spec.get("thr", 0.5))
    ex, extra = spec.get("exclude", ()), spec.get("extra", ())
    sigma = spec.get("sigma", 0.5)
    pts = keep(snap(dark, guide(spec["guide"]), win[0], **kw), ex, extra)
    pts = keep(snap(dark, smooth(pts, sigma), win[1], **kw), ex, extra)
    return pts, smooth(pts, sigma)


def trace_cornered(dark, spec):
    """A curve with a sharp corner at the hand-read pixel spec["corner"] = (col, row) (Fig 8(c)'s k_min curves).
    Each side is traced on its own, its guide and centres ending at the corner, and smoothed on its own by the
    least-squares spline of `smooth` held to the corner (knots every spec.get("knots", 24) px: the smoothing
    spline of one side, which picks its own few knots, cannot both end on the corner and follow the bend
    beyond it). The two sides are joined at the corner, so no spline runs through it. The centres within
    spec.get("corner_gap", 1.5) columns of the corner are dropped (the ink of the two sides is one there).
    The other keys apply to both sides."""
    cx, cy = spec["corner"]
    gap, knots = spec.get("corner_gap", 1.5), spec.get("knots", 24)
    win = spec.get("win", (4.0, 2.0))
    kw = dict(maxlen=spec.get("maxlen", 5.0), thr=spec.get("thr", 0.5))
    ex, extra = list(spec.get("exclude", ())), list(spec.get("extra", ()))
    sides = [([p for p in spec["guide"] if p[0] < cx] + [(cx, cy)], ex + [(cx - gap, np.inf)],
              [p for p in extra if p[0] < cx] + [(cx, cy)]),
             ([(cx, cy)] + [p for p in spec["guide"] if p[0] > cx], ex + [(-np.inf, cx + gap)],
              [(cx, cy)] + [p for p in extra if p[0] > cx])]
    allpts, paths = [], []
    for gd, exs, exa in sides:
        pts = keep(snap(dark, guide(gd), win[0], **kw), exs, exa)
        pts = keep(snap(dark, smooth(pts, pin=(cx, cy), knots=knots), win[1], **kw), exs, exa)
        allpts.append(pts)
        paths.append(smooth(pts, pin=(cx, cy), knots=knots))
    left, right = paths
    path = np.r_[left[left[:, 0] < cx - 1e-6], [(cx, cy)], right[right[:, 0] > cx + 1e-6]]
    return np.r_[allpts[0], allpts[1][1:]], path


def to_data(ax, path, top=None):
    """Pixel path -> data (x increasing). With `top`, the curve is cut where it leaves the frame at y = top,
    or run on along its end tangent to y = top if the ink stops just short of the frame."""
    x, y = ax.to_data(path[:, 0], path[:, 1])
    o = np.argsort(x)
    x, y = x[o], y[o]
    k = np.r_[True, np.diff(x) > 1e-7]
    x, y = x[k], y[k]
    if top is not None:
        if y[0] > top:
            i = np.flatnonzero(y <= top)[0]
            xc = np.interp(top, [y[i], y[i - 1]], [x[i], x[i - 1]])
            x, y = np.r_[xc, x[i:]], np.r_[top, y[i:]]
        elif top - y[0] < 0.6:
            slope = (y[5] - y[0]) / (x[5] - x[0])
            x, y = np.r_[x[0] + (top - y[0]) / slope, x], np.r_[top, y]
    return x, y


def digitize_panel(name, curves, step):
    """Trace the four curves of panel `name` (GUIDE-style specs keyed by COLS) and write <name>.csv."""
    dark, ax = load(name)
    data = {c: to_data(ax, trace(dark, curves[c])[1], curves[c].get("top")) for c in COLS}
    lo = min(v[0][0] for v in data.values())
    hi = max(v[0][-1] for v in data.values())
    grid = np.arange(np.ceil(lo / step) * step, hi, step)
    grid = np.unique(np.round(np.r_[grid, [v[0][0] for v in data.values()], [v[0][-1] for v in data.values()]], 6))
    corners = [float(ax.to_data(*np.array([curves[c]["corner"]], float).T)[0][0])
               for c in COLS if "corner" in curves[c]]
    if corners:                                   # a row at each corner, so the sampling does not cut it off
        grid = np.unique(np.round(np.r_[grid, corners], 6))
    rows = ["m0," + ",".join(COLS)]
    cols = {}
    for c in COLS:
        x, y = data[c]
        cols[c] = np.where((grid >= x[0] - 2e-6) & (grid <= x[-1] + 2e-6), np.interp(grid, x, y), np.nan)
    for i, m in enumerate(grid):
        rows.append(f"{m:.5f}," + ",".join("nan" if np.isnan(cols[c][i]) else f"{cols[c][i]:.3f}" for c in COLS))
    (HERE / f"{name}.csv").write_text("\n".join(rows) + "\n")
    for c in COLS:
        x, y = data[c]
        print(f"{name} {c}: m_o {x[0]:.4f}-{x[-1]:.4f} kg, error {y[0]:+.2f} .. {y[-1]:+.2f}%")
    return data


# ---- Figure 7(a) ---------------------------------------------------------------------------------------------
# pixel points on the crop; the curves start at about column 81 (the y axis leans: col 71.5 at the top, 76 at
# the foot) and end at column 503
CURVES = {
    # solid, from 4.9 rising slowly to 5.9
    "fm_kmax": dict(guide=[(81, 107), (150, 104), (220, 101.5), (300, 99), (400, 98), (503, 97.5)],
                    exclude=[(0, 80)]),
    # dashed, from 4.5 through the zero line (and the k_min solid lying on it) near .105 to -1.5
    "cb_kmax": dict(guide=[(82, 111), (150, 115), (230, 123), (300, 131), (370, 142), (430, 152), (503, 165)],
                    exclude=[(0, 80), (405, 455)]),
    # solid, from 3.6 down onto the zero line, which it follows from about .095 to the end
    "fm_kmin": dict(guide=[(81, 118), (110, 123), (150, 131), (200, 138), (250, 143), (300, 147), (350, 149.5),
                           (400, 151), (503, 152)],
                    exclude=[(0, 80)]),
    # dashed, from -4.4 down to -5.6 near .045, then up to -1.9; a tighter smoothing (sigma 0.3 px) so that the
    # spline follows the first dash (cols 84-89), which bends down more steeply than the rest
    "cb_kmin": dict(guide=[(84, 190), (100, 198), (130, 201), (200, 200), (250, 194), (300, 186), (350, 180),
                           (400, 174), (450, 170), (503, 167)],
                    exclude=[(0, 82)], sigma=0.3),
}

if __name__ == "__main__":
    digitize_panel("fig07a", CURVES, step=0.00025)
