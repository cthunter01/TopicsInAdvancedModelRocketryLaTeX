#!/usr/bin/env python3
"""Chapter 3, Figure 23: flow about a circular cylinder with a separated wake (after Schlichting): geometry.

Lengths in units of the cylinder radius a, origin at the cylinder's centre, x downstream, y up.

Outer flow. The streamlines are drawn round the cylinder together with its boundary layer and dead-water
region, which displace the outer flow as a larger, open body would. They are the potential flow of a uniform
stream U past a doublet and a source at one point (xd, 0) (the plane potential flow the book's argument rests on:
the stream function of the cylinder, psi = U (r - a^2/r) sin(theta), with a source for the wake's displacement):
    psi / U = y (1 - mu / r^2) + (q / pi) theta,      r, theta about (xd, 0), theta in (-pi, pi]
mu (the doublet: an effective radius sqrt(mu)), q (half the wake's displacement far downstream) and xd are fitted
to the eight drawn streamlines (fit(): mu = 1.886, q = 0.190, xd = 0.098; their upstream spacing kept uniform,
psi = +-(0.417 + 0.215 k), k = 0..3): rms 3.3 px, 95% within 6.5 px of the scan (the 1973 streamlines are drawn by
hand; at the left edge they still spread a little wider than the potential flow allows).

Effective body. The dividing streamline psi = q (closed form below) is the edge of the hatched region (boundary
layer and dead water): 0.31 a thick at A, 0.42 a at B, then round the dead water to two lobes that curl back
into a pocket closing on the wake's centre line at x = 1.74 (the lobes and pocket drawn to the scan's shape,
fitted to the dividing streamline).

Velocity profile at B: u/U from Table 1 (the Blasius solution: dp/dx = 0 at B in the potential flow), f'(eta) for
eta = 0 to 5 (f' = 0.99) over the thickness of the layer at B, in a box 0.44 a wide (the drawn width).

Writes fig23-stream.csv (x, s1..s4: the upper streamlines; the lower are their mirror images), fig23-wake.csv (the
closed outline of the hatched region), fig23-profile.csv (the profile curve, x, y), fig23-box.csv (the profile box's
closed outline), fig23-ticks.csv (the profile's velocity lines: x, y, length), fig23-marks.csv (named values).
"""
import json
import pathlib
import sys
import numpy as np
from scipy.optimize import brentq

HERE = pathlib.Path(__file__).resolve().parent
MU, Q, XD = 1.886, 0.190, 0.098
PSI = [0.417 + 0.215 * k for k in range(4)]
X0, X1 = -4.95, 4.75                       # the drawn extent of the streamlines
X_TIP, X_CUSP = 1.80, 1.74                 # the lobes' tips; the pocket's cusp on the axis
BOX_W, BOX_TOP = 0.44, 2.05                # the velocity-profile box at B


def psi(x, y):
    return y * (1 - MU / ((x - XD) ** 2 + y ** 2)) + (Q / np.pi) * np.arctan2(y, x - XD)


def dividing(theta):
    """The dividing streamline psi = q at the polar angle theta (0 < theta <= pi) about (xd, 0):
    r^2 sin(theta) - q (1 - theta/pi) r - mu sin(theta) = 0."""
    s = np.sin(theta); b = Q * (1 - theta / np.pi)
    r = (b + np.sqrt(b * b + 4 * MU * s * s)) / (2 * s)
    return XD + r * np.cos(theta), r * np.sin(theta)


def fit():
    """Refit mu, q, xd and the streamline spacing to the scan (prints them)."""
    from PIL import Image
    from scipy.optimize import least_squares
    root = HERE.parent.parent.parent
    ink = np.asarray(Image.open(root / "figures/ch3/fig23.png").convert("L")) < 140
    xc, yc, a = 336.5, 138.5, 65.5
    pts = []
    for c in range(14, 646, 4):
        if 325 <= c <= 372 or 120 <= c <= 170:          # the profile box, the U label
            continue
        ys = np.flatnonzero(ink[:, c]); g = []
        for y in ys:
            if g and y - g[-1][-1] <= 2: g[-1].append(y)
            else: g.append([y])
        g = [float(np.mean(v)) for v in g if len(v) <= 4]
        up = [y for y in g if y < yc - 3][:4]; dn = [y for y in g if y > yc + 3][-4:]
        if len(up) == 4 and len(dn) == 4:
            x = (c - xc) / a
            for k in range(4):
                pts.append((x, 3 - k, (yc - up[k]) / a)); pts.append((x, k, (dn[k] - yc) / a))

    def res(p):
        mu, q, xd, p0, dp = p
        out = []
        for x, k, y in pts:
            f = lambda yy: yy * (1 - mu / ((x - xd) ** 2 + yy ** 2)) + (q / np.pi) * np.arctan2(yy, x - xd) \
                - (p0 + dp * k)
            out.append(brentq(f, 0.02, 6) - y)
        return np.array(out)
    s = least_squares(res, [1.7, 0.2, 0.0, 0.4, 0.27])
    r = res(s.x) * a
    print("mu q xd psi0 dpsi:", np.round(s.x, 3), f"rms {np.sqrt(np.mean(r ** 2)):.2f} px, "
          f"95% {np.percentile(np.abs(r), 95):.2f} px")


def bezier(p0, p1, p2, p3, n=40):
    t = np.linspace(0, 1, n)[:, None]
    return (1 - t) ** 3 * p0 + 3 * (1 - t) ** 2 * t * p1 + 3 * (1 - t) * t ** 2 * p2 + t ** 3 * p3


def write(name, header, rows, fmt="{:.4f}"):
    lines = [",".join(header)] + [",".join(fmt.format(v) for v in r) for r in rows]
    (HERE / name).write_text("\n".join(lines) + "\n")
    print(f"{name}: {len(rows)} rows")


if "--fit" in sys.argv:
    fit()
    sys.exit()

# streamlines (upper half)
xs = np.round(np.arange(X0, X1 + 1e-9, 0.05), 4)
rows = []
for x in xs:
    rows.append([x] + [brentq(lambda y: psi(x, y) - p, 1e-4, 6.0) for p in PSI])
write("fig23-stream.csv", ["x", "s1", "s2", "s3", "s4"], rows)

# the hatched region: the dividing streamline from the front stagnation point to the lobe's tip ...
th = np.linspace(np.pi, 0.05, 4000)
bx, by = dividing(th[1:])
bx = np.r_[dividing(np.pi - 1e-9)[0], bx]; by = np.r_[0.0, by]
x_front = bx[0]
top = bx <= X_TIP
tx, ty = bx[top], by[top]
y_tip = ty[-1]
# ... a round cap, the lobe's underside back to x = 1.45 (the lobe tapering to 0.13 a at the tip) ...
y_at = lambda x: np.interp(x, tx, ty)
xu = np.linspace(X_TIP, 1.45, 30)
thick = 0.13 + (0.32 - 0.13) * (X_TIP - xu) / (X_TIP - 1.45)
uy = y_at(xu) - thick
cap_c = np.array([X_TIP, y_tip - 0.065]); ang = np.linspace(90, -90, 20)
cap = np.c_[cap_c[0] + 0.065 * np.cos(np.radians(ang)), cap_c[1] + 0.065 * np.sin(np.radians(ang))]
# ... and the pocket, concave to the wake, down to the cusp on the axis (horizontal tangent there)
u0 = np.array([xu[-1], uy[-1]])
pocket = bezier(u0, u0 + np.array([-0.13, -0.17]), np.array([X_CUSP - 0.2, 0.02]), np.array([X_CUSP, 0.0]))
upper = np.vstack([np.c_[tx, ty], cap[1:], np.c_[xu[1:], uy[1:]], pocket[1:]])
# thin to about 0.01 a
sel = [0]
for i in range(1, len(upper)):
    if np.hypot(*(upper[i] - upper[sel[-1]])) >= 0.01:
        sel.append(i)
upper = upper[sel]
lower = upper[::-1] * np.array([1, -1])
outline = np.vstack([upper, lower[1:]])
write("fig23-wake.csv", ["x", "y"], outline.tolist())

# the velocity profile at B: Table 1, f'(eta), eta = 0 ... 5.0
fp = [0.00000, 0.06641, 0.13277, 0.19894, 0.26471, 0.32979, 0.39378, 0.45627, 0.51676, 0.57477, 0.62977,
      0.68132, 0.72899, 0.77246, 0.81152, 0.84605, 0.87609, 0.90177, 0.92333, 0.94112, 0.95552, 0.96696,
      0.97587, 0.98269, 0.98779, 0.99155]
eta = np.arange(len(fp)) * 0.2
delta = brentq(lambda y: psi(0.0, y) - Q, 1.0001, 3.0) - 1.0       # the layer's thickness at B
fy = 1.0 + delta * eta / eta[-1]
fx = BOX_W * np.array(fp) / fp[-1]
write("fig23-profile.csv", ["x", "y"], np.c_[fx, fy].tolist())
# the box's outline: up the wall normal at B, across the top, down to the layer's edge, along the profile
box = [[0.0, 1.0], [0.0, BOX_TOP], [BOX_W, BOX_TOP]] + np.c_[fx, fy][::-1].tolist()
write("fig23-box.csv", ["x", "y"], box)
ty_ = np.arange(1.0 + 0.065, BOX_TOP - 0.03, 0.065)
write("fig23-ticks.csv", ["x", "y", "len"],
      [[0.0, y, float(np.interp(y, fy, fx)) if y < fy[-1] else BOX_W] for y in ty_])

# named values
s_ang = 43.2                                    # S, measured on the scan (degrees from the downstream axis)
u_lab_x = -3.0
marks = {"xfront": x_front, "ytip": y_tip, "delta": delta, "boxw": BOX_W, "boxtop": BOX_TOP,
         "sx": np.cos(np.radians(s_ang)), "sy": np.sin(np.radians(s_ang)), "xcusp": X_CUSP,
         "ulabx": u_lab_x, "ulaby": brentq(lambda y: psi(u_lab_x, y) - PSI[0], 1e-4, 6.0),
         "x0": X0, "x1": X1}
write("fig23-marks.csv", list(marks), [list(marks.values())])
print(json.dumps({k: round(v, 4) for k, v in marks.items()}))
