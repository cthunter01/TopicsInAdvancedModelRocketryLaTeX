#!/usr/bin/env python3
"""Chapter 3, Figure 16: notation for the friction drag of a body of finite thickness, eq. (58)
(scan figures/ch3/fig16.png).

The body (no equation given: "an object of finite thickness") is the scan's teardrop as a least-squares fit
to its outline: a half ellipse for the nose (leading edge x = 195.4, greatest half-thickness 62.3 at x = 295.9)
and a circular arc on each side from there to the pointed tail (x = 452.3), tangent at the shoulder; fit residual
1.6 px rms.

The element ds is placed at x = 240 on the upper surface; the line tangent to the surface there (true tangent:
standing rule 4) meets the axis at phi = 22.5 deg (the scan draws its line about 21 deg, slightly off tangent).
The local profile u(y), normal to the surface at the element, is the laminar flat-plate (Blasius) profile of
Table 1, u/U = f'(eta), linearly interpolated; the drawn height is eta = 7.0 (least-squares fit to the scan's
profile; delta, eta = 5 by eq. (54), lies at 5/7 of it), the outer velocity U(x) 68 px long.

Drawing units are the scan's pixels (150 per inch), x as in the scan, y up from the axis (scan row 198.5); the
figure draws them 1.2 times the printed size. Writes
  fig16-body.csv     the outline, closed (x, y)
  fig16-profile.csv  the profile curve u(y) (x, y)
  fig16-arrows.csv   the profile arrows (x0, y0, x1, y1, head: 1 = long enough for a head)
  fig16-points.csv   named points (name, x, y); the row phi carries the angle in degrees as x
"""
import csv, pathlib
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent.parent
XN, XM, T, XT = 195.4, 295.9, 62.3, 452.3     # nose, shoulder, half-thickness, tail
A = XM - XN                                    # semi-axis of the nose ellipse
L = XT - XM
RHO = (T * T + L * L) / (2 * T)                # radius of the tail arcs
XP = 240.0                                     # the element's upstream edge
W = 24.0                                       # width of the element ds (arc length)
DEPTH = 40.0                                   # depth of the cleared strip under it
H = 109.0                                      # height of the profile along the normal (scan 108.8)
UU = 68.0                                      # length of U(x) (scan 68)
ETA_TOP = 7.0                                  # eta at the profile's top (fitted)
STEP = 10.0                                    # arrow spacing (house, this family)
HEADMIN = 9.0
TAU = 135.0                                    # length of the tau_o arrow along the tangent


def blasius():
    """Table 1 of the chapter: eta, f' (chapters/ch3-sec3a.tex)."""
    eta = np.arange(0, 8.81, 0.2)
    fp = [0.00000, 0.06641, 0.13277, 0.19894, 0.26471, 0.32979, 0.39378, 0.45627, 0.51676, 0.57477,
          0.62977, 0.68132, 0.72899, 0.77246, 0.81152, 0.84605, 0.87609, 0.90177, 0.92333, 0.94112,
          0.95552, 0.96696, 0.97587, 0.98269, 0.98779, 0.99155, 0.99425, 0.99616, 0.99748, 0.99838,
          0.99898, 0.99937, 0.99961, 0.99977, 0.99987, 0.99992, 0.99996, 0.99998, 0.99999, 1.00000,
          1.00000, 1.00000, 1.00000, 1.00000, 1.00000]
    return eta, np.array(fp)


def half(x):
    x = np.asarray(x, float)
    nose = T * np.sqrt(np.clip(1 - ((XM - x) / A) ** 2, 0, 1))
    tail = np.sqrt(np.clip(RHO ** 2 - (x - XM) ** 2, 0, None)) - (RHO - T)
    return np.where(x <= XM, nose, tail)


def upper_point(s0, ds):
    """the point at arc length ds downstream of x = s0 on the upper (nose) surface, by small steps"""
    x, y, s = s0, float(half(s0)), 0.0
    while s < ds:
        x2 = x + 0.01
        y2 = float(half(x2))
        s += np.hypot(x2 - x, y2 - y)
        x, y = x2, y2
    return np.array([x, y])


def tangent_at(x):
    h = 1e-4
    d = (float(half(x + h)) - float(half(x - h))) / (2 * h)
    t = np.array([1.0, d]) / np.hypot(1.0, d)
    return t, np.array([-t[1], t[0]])          # tangent (downstream), outward normal


def main():
    rows = []
    # outline: nose ellipse by angle, tail arcs by x
    th = np.linspace(np.pi / 2, 3 * np.pi / 2, 181)
    upper_nose = [(XM + A * np.cos(a), T * np.sin(a)) for a in th[:91]]           # top -> nose
    lower_nose = [(XM + A * np.cos(a), T * np.sin(a)) for a in th[90:]]           # nose -> bottom
    xs = np.linspace(XM, XT, 121)
    lower_tail = [(x, -float(half(x))) for x in xs]
    upper_tail = [(x, float(half(x))) for x in xs[::-1]]
    outline = upper_nose + lower_nose[1:] + lower_tail[1:] + upper_tail[1:]
    with open(HERE / "fig16-body.csv", "w", newline="") as fh:
        w = csv.writer(fh); w.writerow(["x", "y"])
        w.writerows([[f"{x:.3f}", f"{y:.3f}"] for x, y in outline])

    P = np.array([XP, float(half(XP))])
    t, n = tangent_at(XP)
    phi = np.degrees(np.arctan2(t[1], t[0]))
    V = np.array([P[0] - P[1] / np.tan(np.radians(phi)), 0.0])
    P2 = upper_point(XP, W)
    t2, n2 = tangent_at(P2[0])
    pts = {"V": V, "P": P, "P2": P2, "Pd": P - DEPTH * n, "P2d": P2 - DEPTH * n2,
           "dl": P - 13 * n, "dr": P2 - 13 * n2, "dslab": (P + P2) / 2 - 27 * (n + n2) / 2,
           "T": P + H * n, "TU": P + H * n + UU * t, "tau": P + TAU * t}

    eta, fp = blasius()
    k = ETA_TOP / H
    hs = np.linspace(0, H, 110)
    curve = [P + h * n + UU * np.interp(h * k, eta, fp) * t for h in hs]
    with open(HERE / "fig16-profile.csv", "w", newline="") as fh:
        w = csv.writer(fh); w.writerow(["x", "y"])
        w.writerows([[f"{x:.3f}", f"{y:.3f}"] for x, y in curve])
    arrows = []
    for h in np.arange(H, 0, -STEP):
        u = UU * float(np.interp(h * k, eta, fp))
        a0 = P + h * n
        a1 = a0 + u * t
        arrows.append([f"{a0[0]:.3f}", f"{a0[1]:.3f}", f"{a1[0]:.3f}", f"{a1[1]:.3f}", int(u >= HEADMIN)])
    with open(HERE / "fig16-arrows.csv", "w", newline="") as fh:
        w = csv.writer(fh); w.writerow(["x0", "y0", "x1", "y1", "head"])
        w.writerows(arrows)
    # label anchors: u(y) beside the curve at 0.45 H; U(x) over the top arrow's middle
    h = 0.45 * H
    pts["uy"] = P + h * n + (UU * float(np.interp(h * k, eta, fp)) + 5) * t
    pts["Ux"] = P + (H + 9) * n + 0.42 * UU * t
    with open(HERE / "fig16-points.csv", "w", newline="") as fh:
        w = csv.writer(fh); w.writerow(["name", "x", "y"])
        for name, p in pts.items():
            w.writerow([name, f"{p[0]:.3f}", f"{p[1]:.3f}"])
        w.writerow(["phi", f"{phi:.3f}", "0"])
    print(f"P = ({P[0]:.1f}, {P[1]:.1f}), phi = {phi:.2f} deg, V = {V[0]:.1f}; eta_top = {ETA_TOP}")


if __name__ == "__main__":
    main()
