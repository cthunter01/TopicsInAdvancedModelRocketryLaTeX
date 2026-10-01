#!/usr/bin/env python3
"""Chapter 3, Figure 55: the "drop chart", drop time t against k/m for drop distances x = 10, 25, 50, 100 m.

Computed from eq. (230), x = -(m/2k) ln[1 - tanh^2(t sqrt(gk/m))], which (1 - tanh^2 = sech^2) is
x = (m/k) ln cosh(t sqrt(gk/m)), so
    t = arccosh(exp(x k/m)) / sqrt(g k/m),
with g = 9.8 m/s^2 (ch3-sec8.tex, after eq. (220)). k/m from 10^-3 to 10^-1 m^-1, log-spaced; a curve that
leaves the chart at t = 10 s (the 100 m curve) ends there. Writes fig55-10.csv, fig55-25.csv, fig55-50.csv,
fig55-100.csv (columns km, t) beside this script.

The 1973 chart is drawn on paper whose intermediate rulings are not at log positions (corrections/
v2-figures.md, standing rule 3); the redraw is on true log axes. fig55.calib.json maps the scan by its drawn
gridlines for the overlay check. The overlay agrees below k/m of about 0.02 (to 0.03 s) but not above about
0.04, where the 1973 curves bend further right: at k/m = 0.094 drawn 1.75, 3.74, 6.31 s (10, 25, 50 m) against
1.66, 3.17, 5.62 s computed, and the 100 m curve meets t = 10 s at 0.068 drawn, 0.084 computed (25 m: 95% within
4.0 px, MISMATCH). The computed curves are kept (gate decision); the mismatch is reported for corrections/
v2-figures.md.
"""
import pathlib
import numpy as np
from scipy.optimize import brentq

HERE = pathlib.Path(__file__).resolve().parent
G = 9.8
X = (10, 25, 50, 100)
TMAX = 10.0


def drop_time(x, km):
    """Eq. (230) solved for t (s): x in m, km = k/m in 1/m."""
    km = np.asarray(km, float)
    return np.arccosh(np.exp(x * km)) / np.sqrt(G * km)


def main():
    km = np.logspace(-3, -1, 241)
    for x in X:
        t = drop_time(x, km)
        k = t <= TMAX
        kk, tt = km[k], t[k]
        if not k.all():                                   # end the curve where it leaves the chart
            kc = brentq(lambda q: drop_time(x, q) - TMAX, kk[-1], km[np.argmax(~k)])
            kk, tt = np.r_[kk, kc], np.r_[tt, TMAX]
        (HERE / f"fig55-{x}.csv").write_text("km,t\n" + "".join(f"{a:.6g},{b:.5f}\n" for a, b in zip(kk, tt)))
        msg = f"x = {x:3d} m: t = {tt[0]:.3f} s at k/m = 1e-3"
        msg += f", {drop_time(x, 0.1):.3f} s at 1e-1" if k.all() else f"; leaves t = 10 s at k/m = {kk[-1]:.4f}"
        print(msg + f"; free fall sqrt(2x/g) = {np.sqrt(2 * x / G):.3f} s")
    print("fig55-10.csv, fig55-25.csv, fig55-50.csv, fig55-100.csv written")


if __name__ == "__main__":
    main()
