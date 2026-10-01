#!/usr/bin/env python3
"""Chapter 3, Figure 46: wetted area over maximum frontal area S_s/S_m against fineness ratio ell/d_m.

Each curve is written with two columns, so the figure can plot either (fig46.tex, \\ifexact):
  exact    the book's exact formula where it gives one:
             cylinder  eq. (170)   S_s/S_m = 4 ell/d_m
             ellipsoid eq. (171a)  1 + (2 f / e) sin^-1 e,  e = sqrt(1 - 1/(4 f^2)),  f = ell/d_m
                                   (the half prolate spheroid's lateral area over pi d_m^2/4)
             ogive     eq. (171c)  2.67 f (the book gives no exact ogive formula)
             cone      eq. (171d)  2 sqrt(1/4 + f^2)
  printed  the straight lines the 1973 figure draws (the caption's "approximate" functions):
             cylinder  eq. (170)   4 f
             ellipsoid pi f        the asymptote of (171a) (sin^-1 e = pi/2 - 1/(2f) + ..., so (171a) = pi f
                                   + O(1/f)); eq. (171b) prints 1 + pi f, one unit above the drawn line
             ogive     eq. (171c)  2.67 f
             cone      eq. (171e)  2 f
The noses start at ell/d_m = 1.5 (eq. (171c)'s limit; the caption: "terminated at the lower limit"); every
curve runs to ell/d_m = 6 or to S_s/S_m = 16, the chart's top, whichever comes first (one point beyond is
written so the axes clip the line exactly at the frame).

The three printed nose lines are eq. (168), S_s = integral of P(x) dx, taken literally (the slope of the
surface neglected): for the half spheroid it gives exactly pi f, for the cone exactly 2 f, for the slender
(parabolic-arc) ogive 8/3 f = 2.67 f. For the record (not plotted) the exact lateral area of the tangent ogive,
S_s/S_m = 8 rho [f + (1/2 - rho) sin^-1(f/rho)] with rho = f^2 + 1/4 (radius of the arc in units of d_m), is
printed by this script.

Overlay on the scan: python3 tools/v2/digitize.py overlay figures/v2/ch3/fig46.calib.json --axes main ...
"""
import math
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
TOP, F_MAX = 16.0, 6.0


def ellipsoid_exact(f):            # eq. (171a)
    e = math.sqrt(1.0 - 1.0 / (4.0 * f * f))
    return 1.0 + 2.0 * f / e * math.asin(e)


def cone_exact(f):                 # eq. (171d)
    return 2.0 * math.sqrt(0.25 + f * f)


def ogive_true(f):                 # tangent ogive, exact lateral area (not plotted)
    rho = f * f + 0.25
    return 8.0 * rho * (f + (0.5 - rho) * math.asin(f / rho))


CURVES = {
    "cylinder": (0.0, lambda f: 4.0 * f, lambda f: 4.0 * f),
    "ellipsoid": (1.5, ellipsoid_exact, lambda f: math.pi * f),
    "ogive": (1.5, lambda f: 2.67 * f, lambda f: 2.67 * f),
    "cone": (1.5, cone_exact, lambda f: 2.0 * f),
}


def column(f0, fn, step=0.02):
    """(f, y) from f0 while y <= TOP and f <= F_MAX, plus one point beyond the top (clipped by the axes)."""
    pts, f = [], f0
    while f <= F_MAX + 1e-9:
        y = fn(f)
        pts.append((f, y))
        if y > TOP:
            break
        f = round(f + step, 10)
    return pts


for name, (f0, exact, printed) in CURVES.items():
    a, b = column(f0, exact), column(f0, printed)
    n = max(len(a), len(b))
    rows = ["f,exact,printed"]
    for i in range(n):
        f = (a if len(a) >= len(b) else b)[i][0]
        rows.append(f"{f:.3f},{exact(f):.5f},{printed(f):.5f}")
    out = HERE / f"fig46-{name}.csv"
    out.write_text("\n".join(rows) + "\n")
    print(f"{out.name}: {n} points")

if __name__ == "__main__":
    print("f      (171a)   pi f    true ogive  2.67 f   (171d)   2 f")
    for f in (1.5, 2.0, 3.0, 4.0, 5.0, 6.0):
        print(f"{f:4.1f}  {ellipsoid_exact(f):7.3f}  {math.pi * f:7.3f}  {ogive_true(f):7.3f}    "
              f"{2.67 * f:7.3f}  {cone_exact(f):7.3f}  {2 * f:6.3f}")
