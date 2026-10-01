#!/usr/bin/env python3
"""Chapter 3, Figure 18: stable and unstable boundary-layer velocity profiles (scan figures/ch3/fig18.png).

The two profiles are Falkner-Skan similarity solutions of the boundary-layer equations (38)-(39) with an
outer velocity U(x) ~ x^m (Schlichting, the book's ref. 15):

    f''' + f f'' + beta (1 - f'^2) = 0,   f(0) = f'(0) = 0,   f'(inf) = 1,   u/U_inf = f'(eta)

(beta = 0 is the Blasius profile of Table 1 in the variable eta / sqrt 2). An adverse pressure gradient
(beta < 0) gives a profile with a point of inflection (f''' = 0 inside the layer), a favourable one (beta > 0)
a full profile without one (the text, ch3-sec3b.tex: 396-403). beta is fitted to the scan's curves (least
squares, u at each height, delta at f' = 0.99): (a) beta = -0.1983 (wall shear f''(0) = 0.02, just short of
separation; the scan is closest to the separation profile itself, f''(0) = 0); (b) beta = +0.07.

Drawing units are the scan's pixels (150 per inch), y up from the wall; the figure draws them 1.2 times the
printed size. Writes
  fig18-a.csv, fig18-b.csv   the profile curves u(y) (x, y), from the wall to the top arrow
  fig18-arrows.csv           the profile arrows (panel, x0, y, x1, head: 1 = long enough for a head)
  fig18-marks.csv            the marked points: delta (both panels) and the point of inflection of (a)
"""
import csv, pathlib
import numpy as np
from scipy.integrate import solve_bvp

HERE = pathlib.Path(__file__).resolve().parent
U = 166.0          # length of the U_inf arrow (scan: 166 and 169 px)
DELTA = 142.5      # boundary-layer thickness drawn (scan: the delta dimension, 142.5 px)
TOP = 215.0        # height of the top arrow (scan: 214 px)
STEP = 10.0        # arrow spacing (house, this family)
HEADMIN = 9.0      # shorter arrows are drawn without a head
PANELS = {"a": dict(x0=32.0, tau=0.02), "b": dict(x0=344.0, beta=0.07)}


def falkner_skan(beta=None, tau=None, eta_max=10.0):
    """beta given: solve for f. tau given (wall shear f''(0)): beta is the unknown parameter."""
    x = np.linspace(0, eta_max, 300)
    y = np.vstack([np.log(np.cosh(0.8 * x)) / 0.8, np.tanh(0.8 * x), 0.8 / np.cosh(0.8 * x) ** 2])
    if tau is None:
        f = lambda e, y: np.vstack([y[1], y[2], -y[0] * y[2] - beta * (1 - y[1] ** 2)])
        bc = lambda a, b: np.array([a[0], a[1], b[1] - 1])
        r = solve_bvp(f, bc, x, y, tol=1e-8, max_nodes=200000)
        r.beta = beta
    else:
        # continuation from the separation side: start near beta = -0.19
        f = lambda e, y, p: np.vstack([y[1], y[2], -y[0] * y[2] - p[0] * (1 - y[1] ** 2)])
        bc = lambda a, b, p: np.array([a[0], a[1], b[1] - 1, a[2] - tau])
        g = falkner_skan(beta=-0.19, eta_max=eta_max)
        r = solve_bvp(f, bc, x, g.sol(x), p=[-0.19], tol=1e-8, max_nodes=200000)
        r.beta = r.p[0]
    assert r.status == 0, r.message
    return r


def main():
    arrows, marks = [], []
    for name, p in PANELS.items():
        r = falkner_skan(beta=p.get("beta"), tau=p.get("tau"))
        eta = np.linspace(0, 10, 20001)
        f, fp, fpp = r.sol(eta)
        e99 = eta[np.argmax(fp >= 0.99)]
        k = DELTA / e99                                   # pixels per unit eta
        x0 = p["x0"]
        h = np.linspace(0, TOP, 216)
        u = np.interp(h / k, eta, fp)
        with open(HERE / f"fig18-{name}.csv", "w", newline="") as fh:
            w = csv.writer(fh)
            w.writerow(["x", "y"])
            for hi, ui in zip(h, u):
                w.writerow([f"{x0 + U * ui:.2f}", f"{hi:.2f}"])
        for yi in np.arange(TOP, 0, -STEP):
            ui = float(np.interp(yi / k, eta, fp))
            arrows.append([name, x0, f"{yi:.1f}", f"{x0 + U * ui:.2f}", int(U * ui >= HEADMIN)])
        marks.append([f"delta-{name}", f"{x0 + U * 0.99:.2f}", f"{DELTA:.2f}"])
        fppp = -f * fpp - r.beta * (1 - fp ** 2)
        s = np.flatnonzero(np.diff(np.sign(fppp[20:])))
        if s.size and eta[20 + s[0]] < e99:
            ei = eta[20 + s[0]]
            marks.append([f"inflection-{name}", f"{x0 + U * float(np.interp(ei, eta, fp)):.2f}", f"{ei * k:.2f}"])
        print(f"({name}) beta = {r.beta:.5f}, f''(0) = {fpp[0]:.5f}, eta99 = {e99:.3f}"
              + (f", inflection at y/delta = {ei / e99:.3f}, u/U = {np.interp(ei, eta, fp):.3f}" if name == "a" else ""))
    with open(HERE / "fig18-arrows.csv", "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["panel", "x0", "y", "x1", "head"])
        w.writerows(arrows)
    with open(HERE / "fig18-marks.csv", "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["name", "x", "y"])
        w.writerows(marks)


if __name__ == "__main__":
    main()
