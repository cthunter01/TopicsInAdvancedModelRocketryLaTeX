#!/usr/bin/env python3
"""Chapter 4, Figure 15: the flight path of the gravity-turn schematic, from the book's equations of motion.

The 1973 path is an unlabelled freehand arc beside the two rockets, so its shape is taken from the governing
equations (90)-(91) (the non-oscillating model of Section 3), integrated by the book's "drag from prior velocity"
method: eqs. (125)-(131) along a 1 m launch rod at theta_o = 30 deg, then eqs. (106)-(115), dt = 0.001 sec.
The case is the gravity turn the text describes for "a low-thrust, long-burning engine" (ch4-sec3.tex:231-240):
Figure 14's curve (c) model (m_o = 0.300 kg, k = 0.0045 kg/m, F7 engine, theta_o = 30 deg). The book gives
neither the F7's thrust curve nor its propellant mass, so the thrust is the engine's nominal average, 7 N
(the type designation), and the mass is held at m_o; g = 9.8 m/sec^2. These are parameters of a schematic:
the redraw keeps only the shape.

Position (a) is the rod exit (theta = theta_o = 30 deg), position (b) the point where theta = 74 deg (the
1973 (b) rocket's attitude). The track is scaled so that the chord between them is 334 scan px (the distance
between the 1973 C.G.s; 16.6 px per metre) and placed with (a)'s C.G. at (91, 101) px (scan pixels, y up).
The rockets' C.G.s lie on the track with their axes tangent to it (OFFSET = 0: the path is the C.G.s' own
track; a positive OFFSET would draw the parallel curve that far inside it). The redraw shows the path only
where it is clear of the rockets and their vectors, as 1973 does: from just past (a)'s nose (s = 80 px) to
(b)'s thrust vector (s = 222 px), and beyond (b)'s velocity vector (s = 472-545 px).
Overlay against the 1973 freehand path (fig15.calib.json; the pieces as drawn): 95% within 11.3 px (1.9 mm),
max 12.1 px, and 15.7 px (2.7 mm) for the piece beyond (b); the 1973 rockets sit up to 20 px from where the
track puts (b), and the 1973 arc is not drawn through either C.G.

Writes fig15.csv (s = arc length along the track from (a), x, y: the path from (a) to theta = 88 deg, in px)
and fig15-pos.csv (the C.G. and theta of (a) and (b)).
"""
import math, pathlib

G = 9.8
F, M, K, THETA0, ROD, DT = 7.0, 0.300, 0.0045, 30.0, 1.0, 0.001
THETA_B, THETA_END = 74.0, 88.0
CHORD_PX, CG_A, OFFSET = 334.0, (91.0, 101.0), 0.0


def track():
    """(s, x, y, theta) in metres and degrees from the rod exit to theta = THETA_END."""
    th0 = math.radians(THETA0)
    x = y = v = s = 0.0
    while s < ROD:                                    # eqs. (125)-(131)
        dv = DT * (F - M * G * math.cos(th0) - K * v * v) / M
        ds = DT * (v + dv / 2)
        y += ds * math.cos(th0)
        x += ds * math.sin(th0)
        s += ds
        v += dv
    out = [(0.0, x, y, THETA0)]
    xd, yd = v * math.sin(th0), v * math.cos(th0)
    arc = 0.0
    while True:                                       # eqs. (106)-(115)
        v = math.hypot(xd, yd)
        dyd = DT * (F * yd / v - M * G - K * v * yd) / M
        dxd = DT * (F * xd / v - K * v * xd) / M
        dy, dx = DT * (yd + dyd / 2), DT * (xd + dxd / 2)
        y += dy
        x += dx
        arc += math.hypot(dx, dy)
        yd += dyd
        xd += dxd
        th = math.degrees(math.atan2(xd, yd))
        out.append((arc, x, y, th))
        if th >= THETA_END:
            return out


if __name__ == "__main__":
    here = pathlib.Path(__file__).parent
    pts = track()
    a = pts[0]
    b = next(p for p in pts if p[3] >= THETA_B)
    scale = CHORD_PX / math.hypot(b[1] - a[1], b[2] - a[2])
    def px(p):
        return CG_A[0] + scale * (p[1] - a[1]), CG_A[1] + scale * (p[2] - a[2])
    rows = []
    for i, p in enumerate(pts):
        if i % 10 and p is not pts[-1]:
            continue
        x, y = px(p)
        t = math.radians(p[3])                        # inward normal of the heading (sin t, cos t)
        rows.append(f"{scale * p[0]:.2f},{x + OFFSET * math.cos(t):.2f},{y - OFFSET * math.sin(t):.2f}\n")
    (here / "fig15.csv").write_text("s,x,y\n" + "".join(rows))
    (xa, ya), (xb, yb) = px(a), px(b)
    (here / "fig15-pos.csv").write_text(
        f"pos,x,y,theta,s\na,{xa:.2f},{ya:.2f},{a[3]:.3f},0\nb,{xb:.2f},{yb:.2f},{b[3]:.3f},{scale * b[0]:.2f}\n")
    print(f"fig15.csv: {len(rows)} points, {scale:.2f} px/m; (b) at ({xb:.1f}, {yb:.1f}) px, s = {scale * b[0]:.1f} px")
