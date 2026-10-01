#!/usr/bin/env python3
"""Chapter 3, Figure 25: the development of boundary-layer separation in a positive (adverse) pressure
gradient (scan figures/ch3/fig25.png; after Hoerner).

Geometry from the scan: the wall is flat to x = 110, then a circular arc (radius 589 px) turning to 24 deg, then
straight (fit within about 2 px); the five stations a-e stand where the scan's profiles do (x = 128, 206, 282,
358, 432 on the wall), each profile normal to the wall; the dashed boundary-layer edge is the scan's (a smooth
fit, y = 61 + 18.5 / (1 + exp((x - 300)/60)) scan px), delta at each station measured along the normal.

The profiles are Falkner-Skan similarity solutions of the boundary-layer equations (38)-(39),
f''' + f f'' + beta (1 - f'^2) = 0, u/U = f'(eta), delta at f' = 0.99:
  a  beta = +0.05 (fitted to the scan: a full, stable profile)
  b  beta = -0.12 (fitted: adverse gradient, a point of inflection)
  c  beta = -0.19884, the separation profile: f''(0) = 0, eq. (110), with its inflection point
  d  beta = -0.13 and e beta = -0.07 on the lower (reversed-flow) branch of the solutions (Stewartson), matched
     to the height of the scan's line of stationary fluid (u = 0) at d and e: 0.33 and 0.44 delta.
Between and beyond the stations the profile is followed continuously along this family of solutions
(monotone cubic in the arc length along the wall; beyond e to beta = -0.01 at the right edge, where the scan's
u = 0 line meets it). The streamlines are contours of the stream function of that field, psi = U delta F(n/delta),
F = integral of f' (eqs. (43)-(44)): the U-shaped streamlines of the reversed flow (psi < 0) turn on the u = 0
line (dash-dot, the line of stationary fluid of the text), as in the scan; psi = 0 is the dividing streamline
leaving the wall at c. Their levels put the turns where the scan's are (x = 320, 357, 396, 445).

Drawing units are the scan's pixels (150 per inch), x as in the scan, y up from the flat wall (scan row 132.5);
the figure draws them 1.2 times the printed size. Writes (x, y in drawing units)
  fig25-wall.csv, fig25-band.csv   the wall line; the hatched band under it (closed)
  fig25-edge.csv                   the boundary-layer edge (dashed)
  fig25-a.csv ... fig25-e.csv      the profile curves u(n)
  fig25-arrows.csv                 the profile arrows (x0, y0, x1, y1, head)
  fig25-stream.csv                 the streamlines (rows of nan between lines)
  fig25-heads.csv                  the streamlines' arrowheads, as short segments (x0, y0, x1, y1)
  fig25-zero.csv                   the line u = 0
  fig25-points.csv                 named points (name, x, y); "vortex" is the end of the label's leader, on the
                                   lower branch of the innermost U-shaped streamline
"""
import csv, pathlib
import numpy as np
from scipy.integrate import solve_bvp
from scipy.interpolate import PchipInterpolator
import contourpy

HERE = pathlib.Path(__file__).resolve().parent
R, X0, TH = 589.0, 110.0, np.radians(24.0)
SARC, XE = R * TH, X0 + R * np.sin(TH)
XL, XR = 12.0, 590.0                       # ends of the wall
U = 38.0                                    # length of U (the scan's 36-40)
ABOVE = 22.0                                # the profiles stand this far above delta
STEP, HEADMIN = 10.0, 9.0
BAND = 10.0                                 # depth of the hatched band
STATIONS = [("a", 128.0, 0.05, "u"), ("b", 206.0, -0.12, "u"), ("c", 282.0, None, "sep"),
            ("d", 358.0, -0.13, "l"), ("e", 432.0, -0.07, "l"), ("far", XR, -0.01, "l")]
NOSES = [320.0, 357.0, 396.0, 445.0]        # x of the turns of the psi < 0 streamlines (scan)
SHORT = 372.0                               # the first one's upper branch ends here (scan)
PSI_OUT = 6.0                               # one streamline above the dividing one (psi > 0)
VORTEX_X = 518.0                            # the "vortex" leader ends on the innermost U-shaped streamline's
                                            # lower branch here (clear of its arrowhead at x = 502-509)


# ---- wall and edge ------------------------------------------------------------------------------------------
def W(s):
    s = np.asarray(s, float)
    th = np.clip(s / R, 0, TH)
    x = np.where(s < 0, X0 + s, np.where(s <= SARC, X0 + R * np.sin(th), XE + (s - SARC) * np.cos(TH)))
    y = np.where(s < 0, 0.0, np.where(s <= SARC, -R * (1 - np.cos(th)), -R * (1 - np.cos(TH)) - (s - SARC) * np.sin(TH)))
    t = np.stack([np.cos(th), -np.sin(th)], -1)
    n = np.stack([np.sin(th), np.cos(th)], -1)
    return np.stack([x, y], -1), t, n


def s_of_x(x):
    if x <= X0:
        return x - X0
    if x <= XE:
        return R * np.arcsin((x - X0) / R)
    return SARC + (x - XE) / np.cos(TH)


def edge(x):
    return 132.5 - (61 + 18.5 / (1 + np.exp((np.asarray(x) - 300) / 60)))


def delta(s):
    p, t, n = W(s)
    h = np.linspace(0, 400, 16001)
    q = p + h[:, None] * n
    return h[np.argmin(np.abs(q[:, 1] - edge(q[:, 0])))]


# ---- Falkner-Skan family -------------------------------------------------------------------------------------
def fs(beta, guess=None, eta_max=12.0, tau=None):
    x = np.linspace(0, eta_max, 300)
    if guess is None:
        y = np.vstack([np.log(np.cosh(0.8 * x)) / 0.8, np.tanh(0.8 * x), 0.8 / np.cosh(0.8 * x) ** 2])
    else:
        y = guess.sol(np.minimum(x, guess.x[-1]))
    if tau is None:
        f = lambda e, y: np.vstack([y[1], y[2], -y[0] * y[2] - beta * (1 - y[1] ** 2)])
        bc = lambda a, b: np.array([a[0], a[1], b[1] - 1])
        r = solve_bvp(f, bc, x, y, tol=1e-7, max_nodes=200000)
        r.beta = beta
    else:
        f = lambda e, y, p: np.vstack([y[1], y[2], -y[0] * y[2] - p[0] * (1 - y[1] ** 2)])
        bc = lambda a, b, p: np.array([a[0], a[1], b[1] - 1, a[2] - tau])
        r = solve_bvp(f, bc, x, y, p=[beta], tol=1e-7, max_nodes=200000)
        r.beta = r.p[0]
    assert r.status == 0, (beta, tau, r.message)
    return r


YG = np.linspace(0, 3.0, 601)               # n / delta


def family():
    """FS solutions in order along the branch: upper branch from beta = 0.05 to separation, lower branch on
    to beta = -0.01; each as u(Y), Y = eta / eta_99, with the arc-length parameter q along the (beta, f''(0))
    curve (scaled by 0.2 and 0.47)."""
    sols, g = [], None
    def add(r, branch):
        eta = np.linspace(0, r.x[-1], 12001)
        v = r.sol(eta)
        e99 = eta[np.argmax(v[1] >= 0.99)]
        sols.append(dict(beta=r.beta, tau=v[2][0], branch=branch, u=np.interp(YG * e99, eta, v[1], right=1.0)))
    for b in [0.05, 0.0, -0.05, -0.1, -0.12, -0.14, -0.16, -0.17, -0.18, -0.185, -0.19, -0.193, -0.195,
              -0.197, -0.198]:
        g = fs(b, g); add(g, "u")
    for t in [0.015, 0.01, 0.005, 0.0]:
        g = fs(g.beta, g, tau=t, eta_max=16); add(g, "u" if t > 0 else "sep")
    for t in [-0.01, -0.02, -0.035, -0.05, -0.07, -0.09, -0.11, -0.13]:
        g = fs(g.beta, g, tau=t, eta_max=16); add(g, "l")
    for b in list(np.arange(-0.15, -0.035, 0.01)) + [-0.03, -0.025, -0.02, -0.015, -0.01]:
        g = fs(b, g, eta_max=24 if b < -0.03 else 40); add(g, "l")
    B = np.array([d["beta"] for d in sols]); T = np.array([d["tau"] for d in sols])
    q = np.r_[0, np.cumsum(np.hypot(np.diff(B) / 0.2, np.diff(T) / 0.47))]
    Uf = np.array([d["u"] for d in sols])
    F = np.concatenate([np.zeros((len(sols), 1)), np.cumsum((Uf[:, 1:] + Uf[:, :-1]) / 2 * np.diff(YG), 1)], 1)
    return sols, q, Uf, F


def main():
    sols, q, Uf, F = family()
    def q_of(beta, branch):
        if branch == "sep":
            return float(q[[i for i, d in enumerate(sols) if d["branch"] == "sep"][0]])
        idx = [i for i, d in enumerate(sols) if d["branch"] == branch]
        bb, qq = np.array([sols[i]["beta"] for i in idx]), q[idx]
        o = np.argsort(bb)
        return float(np.interp(beta, bb[o], qq[o]))
    def at(qv, arr):
        i = int(np.clip(np.searchsorted(q, qv) - 1, 0, len(q) - 2))
        w = (qv - q[i]) / (q[i + 1] - q[i])
        return arr[i] * (1 - w) + arr[i + 1] * w
    S = [s_of_x(x) for _, x, _, _ in STATIONS]
    Q = [q_of(b, br) for _, _, b, br in STATIONS]
    qs = PchipInterpolator(S, Q)

    rows, pts = [], {}
    # wall, band, edge
    sw = np.linspace(s_of_x(XL), s_of_x(XR), 400)
    pw, tw, nw = W(sw)
    write("fig25-wall.csv", pw)
    write("fig25-band.csv", np.r_[pw, (pw - BAND * nw)[::-1], pw[:1]])
    xe = np.linspace(XL, XR, 200)
    write("fig25-edge.csv", np.c_[xe, edge(xe)])

    # profiles
    arrows = []
    for (name, x, beta, br), s, qv in zip(STATIONS, S, Q):
        if name == "far":
            continue
        p, t, n = W(s)
        d = delta(s)
        u = at(qv, Uf)
        H = d + ABOVE
        h = np.linspace(0, H, 240)
        uu = U * np.interp(h / d, YG, u)
        write(f"fig25-{name}.csv", p + h[:, None] * n + uu[:, None] * t)
        for hk in np.arange(H, 0, -STEP):
            uk = U * float(np.interp(hk / d, YG, u))
            a0 = p + hk * n
            arrows.append([*a0, *(a0 + uk * t), int(abs(uk) >= HEADMIN)])
        pts[name] = p
        pts[name + "top"] = p + H * n
        print(f"{name}: x = {x:.0f}, s = {s:.1f}, delta = {d:.1f}, beta = {sols[int(np.argmin(abs(q - qv)))]['beta']:.4f}"
              f", f''(0) = {sols[int(np.argmin(abs(q - qv)))]['tau']:.4f}")
    with open(HERE / "fig25-arrows.csv", "w", newline="") as fh:
        w = csv.writer(fh); w.writerow(["x0", "y0", "x1", "y1", "head"])
        w.writerows([[f"{v:.3f}" for v in r[:4]] + [r[4]] for r in arrows])

    # the field downstream of c: psi(s, n) = delta F(n / delta), u(s, n)
    sc = s_of_x(282.0)
    sg = np.linspace(sc, S[-1], 500)
    ng = np.linspace(0, 1.0, 400)                                   # n / (1.6 delta)
    PSI = np.zeros((len(ng), len(sg))); UU = np.zeros_like(PSI); X = np.zeros_like(PSI); Y = np.zeros_like(PSI)
    for j, s in enumerate(sg):
        d = delta(s); qv = float(qs(s))
        nn = ng * 1.6 * d
        PSI[:, j] = d * np.interp(nn / d, YG, at(qv, F))
        UU[:, j] = np.interp(nn / d, YG, at(qv, Uf))
        p, t, n = W(s)
        X[:, j] = p[0] + nn * n[0]; Y[:, j] = p[1] + nn * n[1]
    # the line u = 0 from c, and psi on it (the least psi of its normal): a psi < 0 streamline turns there
    z, zpsi = [], []
    for j in range(len(sg)):
        col = UU[:, j]
        k = np.flatnonzero((col[:-1] < 0) & (col[1:] >= 0))
        if k.size:
            k = k[0]; f = -col[k] / (col[k + 1] - col[k])
            z.append([X[k, j] + f * (X[k + 1, j] - X[k, j]), Y[k, j] + f * (Y[k + 1, j] - Y[k, j])])
            zpsi.append(PSI[:, j].min())
    z, zpsi = np.array(z), np.array(zpsi)
    levels = [float(np.interp(x, z[:, 0], zpsi)) for x in NOSES] + [PSI_OUT]
    gen = contourpy.contour_generator(X, Y, PSI)
    lines, heads = [], []
    for lv in levels:
        for ln in gen.lines(lv):
            ln = ln[ln[:, 0] <= XR - 8]
            if lv > 0:
                ln = ln[ln[:, 0] >= 330]
            if len(ln) < 5:
                continue
            ln = ln[np.argsort(ln[:, 0])] if lv >= 0 else order_u(ln)
            if lv < 0:                                              # upper branches end at staggered x (the
                i = levels.index(lv)                                # first one short, as in the scan), so
                k = int(np.argmin(ln[:, 0]))                        # that their heads stand apart
                xend = SHORT if i == 0 else XR - 8 - 16 * (i - 1)
                ln = ln[: k + 1 + int(np.searchsorted(ln[k:, 0], xend))]
            lines.append(ln)
            if lv == levels[len(NOSES) - 1]:                        # the innermost one: the "vortex" leader
                k = int(np.argmin(ln[:, 0]))                        # ends on its lower branch (lower end ->
                lo = ln[: k + 1][::-1]                              # turn, reversed to increasing x)
                pts["vortex"] = np.array([VORTEX_X, np.interp(VORTEX_X, lo[:, 0], lo[:, 1])])
            heads.append(head(ln, len(ln) - 1))                     # downstream at the right end
            if lv < 0:                                              # reversed flow: a head on the lower branch,
                k = lower_mid(ln)                                   # pointing upstream (the line runs with
                if k is not None:                                   # the flow)
                    heads.append(head(ln, k))
    with open(HERE / "fig25-stream.csv", "w", newline="") as fh:
        w = csv.writer(fh); w.writerow(["x", "y"])
        for ln in lines:
            w.writerows([[f"{a:.3f}", f"{b:.3f}"] for a, b in ln]); w.writerow(["nan", "nan"])
    with open(HERE / "fig25-heads.csv", "w", newline="") as fh:
        w = csv.writer(fh); w.writerow(["x0", "y0", "x1", "y1"])
        w.writerows([[f"{v:.3f}" for v in h] for h in heads])
    z = np.r_[[pts["c"]], z]
    z = z[z[:, 0] <= XR - 8]
    write("fig25-zero.csv", z)
    for name, x in (("noseA", NOSES[0]), ("noseD", NOSES[3])):
        pts[name] = z[np.argmin(abs(z[:, 0] - x))]
    # the pressure-gradient arrow, parallel to the wall below it
    for name, x in (("pg0", 226.0), ("pg1", 312.0)):
        p, t, n = W(s_of_x(x)); pts[name] = p - 36 * n
    for name, x in (("rev1", 383.0), ("rev2", 470.0), ("rev3", 548.0)):
        p, t, n = W(s_of_x(x)); pts[name] = p + 5 * n; pts[name + "t"] = p + 5 * n - 22 * t
    with open(HERE / "fig25-points.csv", "w", newline="") as fh:
        w = csv.writer(fh); w.writerow(["name", "x", "y"])
        for k, v in pts.items():
            w.writerow([k, f"{v[0]:.3f}", f"{v[1]:.3f}"])
    print("streamline levels (psi / U, px):", [round(v, 3) for v in levels])


def order_u(ln):
    """a U-shaped contour from the end of its upper branch, round the turn, to the end of its lower branch"""
    k = int(np.argmin(ln[:, 0]))                                    # the turn (leftmost point)
    a, b = ln[:k + 1], ln[k:]
    up, lo = (a, b) if a[:, 1].mean() > b[:, 1].mean() else (b, a)
    up = up[np.argsort(up[:, 0])][::-1]                             # from its right end to the turn
    lo = lo[np.argsort(lo[:, 0])]                                   # from the turn to its right end
    ln = np.r_[up, lo[1:]]
    return ln[::-1]                                                 # lower right end -> turn -> upper right end


def lower_mid(ln):
    """index of the middle of the lower branch (ln runs lower end -> turn -> upper end)"""
    k = int(np.argmin(ln[:, 0]))
    return k // 2 if k > 8 else None


def head(ln, k, length=5.0):
    """a short segment ending at ln[k], along the line's direction there"""
    p = ln[k]; j = max(0, k - 3)
    d = p - ln[j]; d = d / (np.hypot(*d) or 1)
    return [*(p - length * d), *p]


def write(name, arr):
    with open(HERE / name, "w", newline="") as fh:
        w = csv.writer(fh); w.writerow(["x", "y"])
        w.writerows([[f"{a:.3f}", f"{b:.3f}"] for a, b in arr])


if __name__ == "__main__":
    main()
