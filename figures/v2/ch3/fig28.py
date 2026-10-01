#!/usr/bin/env python3
"""Chapter 3, Figure 28: streamlines and surface pressure of a half-body (after Prandtl and Tietjens, ref. 12).

The half-body is the potential flow of a point source in a uniform stream (the axisymmetric Rankine half-body:
the book appeals to "the techniques of potential-flow theory, involving ... sources and sinks" and to "potential
theory" for the zero drag of the half-body). The 1973 streamlines are those of the axisymmetric body: a stream
tube of upstream radius w0 ends downstream at sqrt(w0^2 + R^2) (drawn 32.3, 38.3, 42.3 px for 31.8, 37.7, 44.6;
the plane half-body would give 44, 53, 62).

Units: R, the body's radius far downstream; U = 1. Source of strength Q = 4 pi m at the origin, m = R^2 / 4,
stagnation point (the nose) a distance R/2 ahead of it; X is measured aft from the nose.
  Stokes stream function   psi = w^2 / 2 - m cos(theta)     (theta from the downstream axis, w the radius)
  body (psi = m)           w = R cos(theta/2), at the distance r = R / (2 sin(theta/2)) from the source
  a streamline of upstream radius w0:  w^2 / 2 - m cos(theta) = w0^2 / 2 + m
  velocity                 u = 1 + m x / r^3,  v = m w / r^3;   C_p = p / ((rho/2) u_o^2) = 1 - (u^2 + v^2)
On the surface C_p falls from 1 at the nose through 0 at X = 0.296 R to its least value -1/3 at X = 0.789 R
(w = sqrt(2/3) R) and returns to 0 far downstream. The 1973 curve, read against its own ordinate, reaches about
-0.39 near X = 1.1 R: the computed curve is used, as the standing rules require; the difference (and the lower
(b) suction lobe, 1.33 R from the axis against about 1.6 R drawn) is a Chapter 3 gate item for
corrections/v2-figures.md.

Writes (X, w in units of R):
  fig28-body.csv     X, w        the body contour (upper half; the drawing mirrors it)
  fig28-stream.csv   X, s1..s4   the four streamlines of panel (a), upstream radii 0.35, 0.70, 1.05, 1.40 R
                                 (the drawn spacing)
  fig28-cp.csv       X, cp       C_p along the surface against X (panel (a))
  fig28-strokes.csv  X, w, dX, dw, cp   panel (b): at every 0.12 R of arc along the surface, a stroke along the
                                 outward normal of length 1.5 R per unit |C_p| (the drawn scale)
  fig28-envpos.csv, fig28-envneg.csv, fig28-envtail.csv   the envelope of the strokes: the positive lobe, the
                                 suction lobe while C_p <= -0.2 (solid in the print), its tail (dashed)
"""
import pathlib
import numpy as np
from scipy.optimize import brentq

HERE = pathlib.Path(__file__).resolve().parent
R = 1.0
m = R * R / 4
x_nose = -R / 2                     # the nose, relative to the source
X_END = 15.6                        # the drawn length behind the nose (R)
X_LEFT = -4.4                       # the left end of the streamlines
K = 1.5                             # panel (b): R per unit C_p
DS = 0.12                           # panel (b): stroke spacing along the surface (R)


def body_theta(theta):
    w = R * np.cos(theta / 2)
    r = R / (2 * np.sin(theta / 2))
    return r * np.cos(theta), w, r


def velocity(x, w):
    r = np.hypot(x, w)
    return 1 + m * x / r ** 3, m * w / r ** 3


def cp_at(x, w):
    u, v = velocity(x, w)
    return 1 - (u * u + v * v)


def write(name, header, cols, fmt="{:.5f}"):
    rows = [",".join(header)] + [",".join(fmt.format(c) for c in row) for row in zip(*cols)]
    (HERE / name).write_text("\n".join(rows) + "\n")
    print(f"{name}: {len(cols[0])} rows")


# the body: theta from pi (the nose) down to the drawn end; dense near the nose
th = np.r_[np.linspace(np.pi, np.pi / 2, 400, endpoint=False), np.linspace(np.pi / 2, 0.001, 4000)]
xb, wb, _ = body_theta(th)
Xb = xb - x_nose
keep = Xb <= X_END
Xb, wb, xb = Xb[keep], wb[keep], xb[keep]
# thin the dense tail to about 0.02 R in X or in w
sel = [0]
for i in range(1, len(Xb)):
    if np.hypot(Xb[i] - Xb[sel[-1]], wb[i] - wb[sel[-1]]) >= 0.02:
        sel.append(i)
if sel[-1] != len(Xb) - 1:
    sel.append(len(Xb) - 1)
sel = np.array(sel)
Xs, ws, xs = Xb[sel], wb[sel], xb[sel]
write("fig28-body.csv", ["X", "w"], [Xs, ws])
write("fig28-cp.csv", ["X", "cp"], [Xs, cp_at(xs, ws)])

# streamlines of panel (a)
Xg = np.r_[np.arange(X_LEFT, 3.0, 0.05), np.arange(3.0, X_END + 1e-9, 0.2)]
cols = [Xg]
for w0 in (0.35, 0.70, 1.05, 1.40):
    psi = w0 * w0 / 2 + m
    ys = []
    for X in Xg:
        x = X + x_nose
        f = lambda w: w * w / 2 - m * x / np.hypot(x, w) - psi
        ys.append(brentq(f, 1e-9, 10.0))
    cols.append(np.array(ys))
write("fig28-stream.csv", ["X", "s1", "s2", "s3", "s4"], cols)

# panel (b): strokes along the outward normal at equal arc length
d = np.r_[0.0, np.cumsum(np.hypot(np.diff(Xb), np.diff(wb)))]
s_pts = np.arange(0.0, d[-1], DS)
Xp = np.interp(s_pts, d, Xb)
wp = np.interp(s_pts, d, wb)
tX = np.gradient(Xp); tw = np.gradient(wp)
tX[0], tw[0] = 0.0, 1.0                      # at the nose the surface is normal to the axis
n = np.hypot(tX, tw)
nX, nw = -tw / n, tX / n                     # outward normal (the body lies below the upper contour)
cpp = cp_at(Xp + x_nose, wp)
cpp[0] = 1.0
live = np.abs(cpp) >= 0.012                  # strokes while they are longer than about 0.02 R
write("fig28-strokes.csv", ["X", "w", "dX", "dw", "cp"],
      [Xp[live], wp[live], (K * np.abs(cpp) * nX)[live], (K * np.abs(cpp) * nw)[live], cpp[live]])

# envelopes: finely, from the surface
s_f = np.arange(0.0, min(d[-1], 9.0), 0.01)
Xf = np.interp(s_f, d, Xb); wf = np.interp(s_f, d, wb)
tX = np.gradient(Xf); tw = np.gradient(wf); tX[0], tw[0] = 0.0, 1.0
n = np.hypot(tX, tw); nX, nw = -tw / n, tX / n
cf = cp_at(Xf + x_nose, wf); cf[0] = 1.0
eX = Xf + K * np.abs(cf) * nX
ew = wf + K * np.abs(cf) * nw
zero = np.flatnonzero(cf <= 0)[0]            # C_p = 0 on the shoulder: both lobes start at the surface there
pos = slice(0, zero + 1)
neg_solid = (np.arange(len(cf)) >= zero) & ((cf <= -0.2) | (Xf < Xf[np.argmin(cf)]))
i_end_solid = np.flatnonzero(neg_solid)[-1]
tail = (np.arange(len(cf)) >= i_end_solid) & (Xf <= 7.0)
write("fig28-envpos.csv", ["X", "w"], [eX[pos], ew[pos]])
write("fig28-envneg.csv", ["X", "w"], [eX[neg_solid], ew[neg_solid]])
write("fig28-envtail.csv", ["X", "w"], [eX[tail], ew[tail]])
print(f"C_p min {cf.min():.4f} at X = {Xf[np.argmin(cf)]:.3f} R; C_p = 0 at X = {Xf[zero]:.3f} R; "
      f"solid suction envelope to X = {Xf[i_end_solid]:.2f} R")
