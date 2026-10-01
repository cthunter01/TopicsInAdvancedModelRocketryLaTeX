#!/usr/bin/env python3
"""Chapter 4, Figure 2: the trajectory of the schematic, computed from the book's equations of motion.

The 1973 trajectory is an unlabelled freehand arc, so its shape is taken from the governing equations (12)-(13)
(with (14)-(15); for a model that does not oscillate, (90)-(91)), integrated by the book's nonvertical
"drag from prior velocity" method: eqs. (125)-(131) along the launch rod for the first metre, then eqs.
(106)-(115), dt = 0.001 sec. The model is Table 2's (B4 engine as in trajectory.py: thrust by eqs. (73a)-(73c),
mass lost in proportion to the impulse delivered; m_o = 0.040 kg, k = 0.92e-4 kg/m; g = 9.8 m/sec^2), launched
at theta_o = 22 deg: the launch angle (and the drawing scale, 1.69 scan px per metre) is the parameter matched
to the scan. The curve is drawn from the launch point to the rocket's position, where its tangent makes
theta = 50 deg with the vertical (the 1973 rocket and velocity vector lean about 47-48 deg, and its curve
reaches the rocket where the computed tangent is at about 51 deg).

Overlay against the scan (the 1973 x axis is oblique, so the curve is compared in the page's own frame: origin
at the launch point, y axis vertical after a 0.7 deg deskew): figures/v2/ch4/fig02.calib.json; 95% of the points
within 1.0 px (0.17 mm) of the 1973 curve, mean 0.15 px. (At the 30 deg launch angle of Figures 10-14 the 1973
curve cannot be matched: 95% beyond 35 px at any scale.)

Writes fig02.csv (x, y in metres, every 0.02 sec) and fig02-end.csv (the rocket's position x, y and theta in
degrees).
"""
import math, pathlib, sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from trajectory import B4, G

M0, K, THETA0, THETA_END = 0.040, 0.92e-4, 22.0, 50.0
ROD, DT = 1.0, 0.001


def nonvertical(m0, k, theta0, theta_end, eng=B4, dt=DT, rod=ROD):
    """(t, x, y, theta) from liftoff until the trajectory angle reaches theta_end (degrees)."""
    c = eng.It / eng.mp
    th0 = math.radians(theta0)
    t = x = y = v = s = 0.0
    m = m0
    out = [(0.0, 0.0, 0.0, theta0)]
    while s < rod:                                    # launch rod: eqs. (125)-(131)
        f = eng.thrust(t)
        dv = dt * (f - m * G * math.cos(th0) - k * v * v) / m          # (125)
        if v + dv < 0:                                # on the pad until the thrust exceeds the weight
            dv = -v
        ds = dt * (v + dv / 2)
        y += ds * math.cos(th0)                       # (126), (129)
        x += ds * math.sin(th0)                       # (127), (130)
        s += ds
        v += dv                                       # (128)
        if t < eng.tb:
            m -= f / c * dt
        t += dt                                       # (131)
        out.append((t, x, y, theta0))
    xd, yd = v * math.sin(th0), v * math.cos(th0)
    while True:                                       # free flight: eqs. (106)-(115)
        f = eng.thrust(t)
        v = math.hypot(xd, yd)
        dyd = dt * (f * yd / v - m * G - k * v * yd) / m               # (106)
        dxd = dt * (f * xd / v - k * v * xd) / m                       # (107)
        y += dt * (yd + dyd / 2)                      # (108), (113)
        x += dt * (xd + dxd / 2)                      # (109), (114)
        yd += dyd                                     # (110)
        xd += dxd                                     # (111)
        if t < eng.tb:
            m -= f / c * dt
        t += dt                                       # (115)
        th = math.degrees(math.atan2(xd, yd))
        out.append((t, x, y, th))
        if th >= theta_end:
            return out


if __name__ == "__main__":
    here = pathlib.Path(__file__).parent
    pts = nonvertical(M0, K, THETA0, THETA_END)
    step = round(0.02 / DT)
    rows = [p for i, p in enumerate(pts) if i % step == 0 or i == len(pts) - 1]
    (here / "fig02.csv").write_text("x,y\n" + "".join(f"{x:.3f},{y:.3f}\n" for _, x, y, _ in rows))
    t, x, y, th = pts[-1]
    (here / "fig02-end.csv").write_text(f"x,y,theta\n{x:.3f},{y:.3f},{th:.3f}\n")
    print(f"fig02.csv: {len(rows)} points; rocket at t = {t:.2f} sec, x = {x:.1f} m, y = {y:.1f} m, "
          f"theta = {th:.2f} deg")
