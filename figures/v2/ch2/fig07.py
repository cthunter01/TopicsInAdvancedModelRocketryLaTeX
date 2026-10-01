#!/usr/bin/env python3
"""Chapter 2, Figure 7: corrective moment M_c against angular deflection alpha_X (a measured curve).

The book gives no equation for this "typical" curve (ch2-sec2.tex: the dependence is analytically
complicated), so it is digitized from the 1973 art, figures/ch2/fig07.png (Fig 7 is the cleanest of the two
tracings: Fig 9 draws the same curve under its linear approximation). Calibration: fig07.calib.json,
piecewise between the drawn ticks. Fig 9 (fig09.py) reuses this curve, so the data are the same in both.

The traced centre line is fitted as
    M_c(alpha) = C_1 alpha                          for alpha <= a_j
    M_c(alpha) = C_1 alpha + r(alpha)               for alpha >  a_j
with C_1 = 1x10^6 dyn-cm (the Fig 9 lettering; eq. (8): the linear approximation is the tangent at zero),
r a cubic B-spline on [a_j, 0.3] joined with r = r' = r'' = 0 at a_j = 0.20 rad (where the drawn curve
leaves its tangent: the concave fit with the least residual), and the end condition dM_c/dalpha = 0 at
0.3 rad, the zero slope the text relies on (ch2-sec5.tex: the balance becomes unstable where the slope of
the corrective moment curve becomes zero, between 12 and 18 deg). Writes fig07.csv (alpha in rad, M_c in dyn-cm).
"""
import json
import pathlib
import numpy as np
from PIL import Image
from scipy.interpolate import BSpline

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent.parent


def load_calib(name, axes="main"):
    spec = json.loads((HERE / name).read_text())
    ax = spec["axes"][axes]
    return ROOT / spec["crop"], np.array(ax["xgrid"], float), np.array(ax["ygrid"], float)


def to_data(px, py, xgrid, ygrid):
    """Pixel -> data, piecewise linear between the drawn ticks (as tools/v2/digitize.py does with xgrid/ygrid)."""
    oy = np.argsort(ygrid[:, 0])
    return np.interp(px, xgrid[:, 0], xgrid[:, 1]), np.interp(py, ygrid[oy, 0], ygrid[oy, 1])


def runs(v, off):
    idx = np.flatnonzero(v)
    if idx.size == 0:
        return []
    cut = np.flatnonzero(np.diff(idx) > 1)
    return [(s + e) / 2 + off for s, e in zip(np.r_[idx[0], idx[cut + 1]], np.r_[idx[cut], idx[-1]])]


def trace(crop, c0, c1, top, bottom, start_row, max_jump=4.0):
    """Follow the one curve column by column from c0 to c1: in each column the centre of the ink run nearest
    the prediction (last row + smoothed slope), between row `top` and the row bottom(c) just above the x axis."""
    ink = np.asarray(Image.open(crop).convert("L")) < 128
    pts, last, slope = [], float(start_row), 0.0
    for c in range(c0, c1 + 1):
        rr = runs(ink[top:int(bottom(c)), c], top)
        if not rr:
            continue
        pred = last + slope
        best = min(rr, key=lambda r: abs(r - pred))
        if abs(best - pred) <= max_jump:
            if pts:
                slope = 0.7 * slope + 0.3 * (best - last) / (c - pts[-1][0])
            last = best
            pts.append((c, best))
    return np.array(pts, float)


def fit(x, y, C, xj, xmax, n_inner=4, end_slope_zero=False):
    """Least-squares fit of y = C x + r(x): r = 0 up to the join xj, a clamped cubic B-spline beyond it with
    its first three coefficients zero (r, r', r'' = 0 at xj); optionally with dy/dx = 0 at xmax.
    Returns the function y(x)."""
    k = 3
    t = np.r_[[xj] * 4, np.linspace(xj, xmax, n_inner + 2)[1:-1], [xmax] * 4]
    n = len(t) - k - 1
    basis = [BSpline(t, np.eye(n)[j], k) for j in range(n)]
    m = x > xj
    free = list(range(3, n))
    A = np.column_stack([basis[j](x[m]) for j in free])
    r = y[m] - C * x[m]
    if end_slope_zero:
        g = np.array([basis[j].derivative()(xmax) for j in free])
        K = np.block([[2 * A.T @ A, g[:, None]], [g[None, :], np.zeros((1, 1))]])
        sol = np.linalg.solve(K, np.r_[2 * A.T @ r, -C])[:-1]
    else:
        sol = np.linalg.lstsq(A, r, rcond=None)[0]
    coef = np.zeros(n)
    coef[free] = sol
    sp = BSpline(t, coef, k)
    return lambda xx: C * np.asarray(xx, float) + np.where(np.asarray(xx) > xj, sp(np.clip(xx, xj, xmax)), 0.0)


def report(name, f, x, y, ygrid, C, xmax, marks):
    px_per = abs(ygrid[-1, 0] - ygrid[0, 0]) / abs(ygrid[-1, 1] - ygrid[0, 1])
    res = (f(x) - y) * px_per
    xx = np.linspace(0, xmax, 3001)
    yy = f(xx)
    d = np.gradient(yy, xx)
    print(f"{name}: {len(x)} traced points; fit residual rms {np.sqrt((res ** 2).mean()):.2f} px, "
          f"95% {np.percentile(abs(res), 95):.2f} px, max {abs(res).max():.2f} px; "
          f"max {yy.max():.4g} at {xx[yy.argmax()]:.4g}; end slope {d[-1] / C:+.3f} C; concave: {bool((np.diff(d) <= 1e-9 * C).all())}")
    print("   " + "  ".join(f"{p:g}: {f(p):.4g}" for p in marks))


if __name__ == "__main__":
    C1, XJ = 1.0e6, 0.20
    crop, xgrid, ygrid = load_calib("fig07.calib.json")
    # the x axis runs from row ~317 at the origin to ~315 at 0.3 rad: stop 3 px above it
    P = trace(crop, 100, 521, 10, lambda c: 314.0 - (c - 163) * 1.9 / 357, 314)
    x, y = to_data(P[:, 0], P[:, 1], xgrid, ygrid)
    keep = x > 0.01               # the first few columns merge with the axes
    x, y = x[keep], y[keep]
    f = fit(x, y, C1, XJ, 0.3, n_inner=4, end_slope_zero=True)
    report("fig07", f, x, y, ygrid, C1, 0.3, [0.1, 0.2, 0.225, 0.25, 0.275, 0.3])
    a = np.round(np.linspace(0, 0.3, 151), 4)
    (HERE / "fig07.csv").write_text("alpha,Mc\n" + "".join(f"{ai:.4f},{mi:.1f}\n" for ai, mi in zip(a, f(a))))
    print(f"fig07.csv: {len(a)} points")
