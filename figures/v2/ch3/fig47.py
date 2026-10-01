#!/usr/bin/env python3
"""Chapter 3, Figure 47: geometrical definitions of the nose shapes (scan: figures/ch3/fig47.png).

Writes fig47.csv: every line of the figure as page coordinates in centimetres (x, y) with a style code s
(fig47.tex draws each code in its house style; rows of NaN separate the polylines):
  1 outline   2 hidden   3 phantom (ink: a position after half a turn, the circle the base sweeps)
  4 centerline   5 hatched region (closed polygon, filled, not stroked)   6 thin line (the right-angle mark)
  7 phantom in ink2 (the piece of the cone cut away, shown for context)
  11-15 rotation arrows (thin vec), one code each, cells (a)-(e)

Geometry (exact):
  * The 3D drawings use the house view of tamrfig.sty (`tamr view`: x = (1.15, 0.61), y = (-1.15, 0.61),
    z = (0, 1.38) cm per unit, times VIEW): a true orthographic view, elevation 32 deg, azimuth 45 deg; the
    direction towards the viewer is the cross product of the projection's rows, (-0.5996, -0.5996, 0.5301),
    as \\getview gives. The 2D drawings (the middle ellipse of (a), the circle of (d), the triangle of (e))
    are face-on at 1.626 VIEW cm per unit, the length of a horizontal page-parallel unit in the view. The
    cutting planes rise towards the back left: (a) towards azimuth 95 deg (from page left, gamma = 40 deg
    towards the back), (b) 129 deg (gamma = 6), (c) 121 deg (gamma = 14). The (b) and (c) planes are turned
    nearer edge-on, as in the 1973 art (a narrow sliver of section in front of the axis), and they and their
    heights z0 are placed so that the section keeps clear of the cone's right silhouette generator (which the
    cut-away piece shows) except near the apex: at least 0.8 mm apart on the page below 0.9 H, and no
    cut-away line runs within 0.6 mm of a solid line except where they meet. With the 1973-like azimuth of
    (a) (gamma = 40) the (b) and (c) sections ran along that generator for 1-2 cm, a double edge.
  * (a)-(c): one right circular cone, base radius R = 1 at z = 0, apex at z = H = 2.5 (half-angle
    alpha = atan(R/H) = 21.80 deg, the 1973 cones' proportions). Each cutting plane rises at beta from the
    horizontal; it contains the horizontal t and the slope s = cos(beta) h + sin(beta) z (h horizontal) and
    crosses the cone axis at z0. On the plane, at (a along t, b along s), the cone is
        a^2 = k^2 (H - z0 - b sin(beta))^2 - b^2 cos^2(beta),   k = R/H,
    a conic with eccentricity sin(beta)/cos(alpha): (a) ellipse, beta = 48 deg < 90 - alpha;
    (b) parabola, beta = 90 - alpha (the plane parallel to a generator); (c) hyperbola, beta = 76 deg > 90 - alpha.
    The section is hatched on the plane. The plane is opaque; the piece of the cone on the viewer's side of
    it (the one containing the apex) is cut away and drawn phantom in ink2 (a part shown for context, the
    kit's convention, as Ch2 Fig 41); edges of the kept piece hidden by the
    plane or by the cone itself are hidden lines. Visibility is found by casting a ray from each point
    towards the viewer.
  * The noses are the sections' halves revolved, at the same scale as the cone: (a) the ellipse divided along
    its minor axis (the middle drawing) and spun about its semimajor axis (a half prolate spheroid, semi-axes
    of the section; the middle drawing and this nose at A_SCALE = 1.5 times the cone's scale, as the 1973
    art enlarges them); (b), (c) the parabolic and hyperbolic segments cut off by the base chord, revolved about
    their axes (the nose profile is the section curve itself); (d) the circle's smaller segment (chord at
    0.78 of the radius from the centre), bisected by the radial line, the hatched half revolved about the
    chord: a tangent ogive with length = the half chord, base radius = the segment's height (the top circle
    is drawn at a smaller scale, D_SCALE); (e) the right triangle revolved about its altitude (a cone). Each
    nose stands on the meridian plane facing the viewer (foreshortened by cos 32 deg as the view requires);
    the generating region is solid, its position after half a turn phantom ((d), (e)), the circle swept by
    the base phantom, the axis a centre line, and the rotation arrow a circle round the axis, counterclockwise
    seen from above (left, front, right, as printed).
"""
import math
import pathlib
import sys

import numpy as np

HERE = pathlib.Path(__file__).resolve().parent

# ---- view (tamrfig.sty: tamr view) -------------------------------------------------------------------------
VIEW = 0.52                                      # tamr view=0.52: 1 unit = 0.846 cm along the page
VX, VY, VZ = np.array([1.15, 0.61]), np.array([-1.15, 0.61]), np.array([0.0, 1.38])
_c = np.array([VY[0] * VZ[1] - VZ[0] * VY[1], VZ[0] * VX[1] - VX[0] * VZ[1], VX[0] * VY[1] - VY[0] * VX[1]])
C = _c / np.linalg.norm(_c)                       # towards the viewer: (-0.5996, -0.5996, 0.5301)
U2D = VIEW * np.hypot(*(VX - VY)) / math.sqrt(2)  # cm per unit of a 2D drawing (1.626 VIEW)
U = np.array([1.0, -1.0, 0.0]) / math.sqrt(2)     # page right
W = np.array([1.0, 1.0, 0.0]) / math.sqrt(2)      # away from the viewer (page up)
Z = np.array([0.0, 0.0, 1.0])


def proj(p, origin):
    """3D point(s) -> page cm, the drawing's origin (page cm) added."""
    p = np.atleast_2d(p)
    return VIEW * (np.outer(p[:, 0], VX) + np.outer(p[:, 1], VY) + np.outer(p[:, 2], VZ)) + origin


# ---- the cone and the planes --------------------------------------------------------------------------------
R, H = 1.0, 2.5
K = R / H
ALPHA = math.degrees(math.atan(K))
PLANES = {   # beta (deg), z0, rising azimuth offset gamma (deg, from page left towards the back), rectangle
    #          margins: [a half-width, below the section, above it]
    "a": dict(beta=48.0, z0=1.5, gamma=40.0, rect=(0.95, 0.75, 0.5)),
    # (b), (c): turned and placed to keep the section off the right silhouette generator (see the docstring)
    "b": dict(beta=90.0 - ALPHA, z0=1.7, gamma=6.0, rect=(1.50, 0.25, 0.55)),
    "c": dict(beta=76.0, z0=2.0, gamma=14.0, rect=(1.75, 0.25, 0.20)),
}

rows = []           # (x, y, s)


def emit(pts, s):
    """One polyline (page cm) with style s."""
    pts = np.asarray(pts)
    if len(pts) < 2:
        return
    for x, y in pts:
        rows.append((x, y, s))
    rows.append((math.nan, math.nan, s))


def emit_runs(pts3, codes, origin):
    """A sampled 3D curve whose points carry style codes: one polyline per run of equal codes (each run
    extended to the next point so that the pieces meet)."""
    P = proj(pts3, origin)
    i = 0
    n = len(codes)
    while i < n - 1:
        j = i
        while j + 1 < n and codes[j + 1] == codes[i]:
            j += 1
        emit(P[i:min(j + 2, n)], codes[i])
        i = j + 1


class Cut:
    def __init__(self, beta, z0, gamma, rect):
        self.beta, self.z0 = math.radians(beta), z0
        th = math.radians(135.0 - gamma)          # azimuth of h, the direction in which the plane rises
        self.h = np.array([math.cos(th), math.sin(th), 0.0])
        self.t = np.array([-math.sin(th), math.cos(th), 0.0])
        sb, cb = math.sin(self.beta), math.cos(self.beta)
        self.s = cb * self.h + sb * Z
        self.m = -sb * self.h + cb * Z           # upward normal; the viewer is on its side
        self.P0 = np.array([0.0, 0.0, z0])
        assert self.m @ C > 0
        # the section: Q(b) = a^2
        self.Q = lambda b: K * K * (H - z0 - b * sb) ** 2 - b * b * cb * cb
        bs = np.linspace(-8, 8, 160001)
        zs = z0 + bs * sb
        ok = (self.Q(bs) >= 0) & (zs <= H) & (zs >= 0)
        self.bv = bs[ok].max()                   # the vertex nearest the apex
        self.bc = -z0 / sb                       # the base chord (z = 0)
        lo = bs[ok].min()
        self.closed = lo > self.bc + 1e-3        # an ellipse: the lower vertex above the base
        self.blo = lo if self.closed else self.bc
        if self.closed:                          # refine the two vertices (roots of Q)
            a2, a1 = (K * K * sb * sb - cb * cb), -2 * K * K * (H - z0) * sb
            a0 = K * K * (H - z0) ** 2
            r = np.sort(np.roots([a2, a1, a0]).real)
            self.blo, self.bv = r[0], r[1]
            self.A = (self.bv - self.blo) / 2
            self.B = math.sqrt(self.Q((self.bv + self.blo) / 2))
        else:
            self.ac = math.sqrt(self.Q(self.bc))
        aw, mlo, mhi = rect
        self.rect = (-aw, aw, self.blo - mlo, self.bv + mhi)

    def X(self, a, b):
        return self.P0 + np.outer(a, self.t) + np.outer(b, self.s)

    def side(self, p):                           # > 0: the viewer's side (the cut-away piece)
        return (np.atleast_2d(p) - self.P0) @ self.m

    def behind_plane(self, p):
        """Points on the far side whose ray towards the viewer passes through the rectangle."""
        p = np.atleast_2d(p)
        d = self.side(p)
        tau = -d / (C @ self.m)
        Y = p + np.outer(tau, C) - self.P0
        a, b = Y @ self.t, Y @ self.s
        a0, a1, b0, b1 = self.rect
        return (d < 0) & (a >= a0) & (a <= a1) & (b >= b0) & (b <= b1)

    def section(self, n=241):
        """The section's boundary (closed polygon, plane coordinates) from the base chord round the vertex."""
        if self.closed:
            th = np.linspace(0, 2 * np.pi, 2 * n)
            bm = (self.bv + self.blo) / 2
            return self.B * np.sin(th), bm + self.A * np.cos(th)
        tau = np.linspace(-1, 1, 2 * n)
        b = self.bv - (self.bv - self.bc) * tau ** 2
        a = np.sign(tau) * np.sqrt(np.maximum(self.Q(b), 0))
        return np.r_[a, a[0]], np.r_[b, b[0]]


def cone_cut(key, origin):
    cut = Cut(**PLANES[key])
    apex = np.array([0.0, 0.0, H])
    # the base circle: the seen arc runs between the silhouettes through the front (azimuth 225 deg)
    phis = np.radians(np.linspace(0, 360, 721))
    base = np.c_[R * np.cos(phis), R * np.sin(phis), np.zeros_like(phis)]
    nrm = np.c_[np.cos(phis), np.sin(phis), np.full_like(phis, K)]
    front = nrm @ C > 0
    codes = np.where(cut.side(base) > 0, 7, np.where(~front | cut.behind_plane(base), 2, 1))
    emit_runs(base, codes, origin)
    # the silhouette generators: n . c = 0
    s45 = -K * C[2] / (C[0] * math.sqrt(2))      # cos(phi) + sin(phi) = sqrt2 sin(phi + 45) = -k c_z / c_x
    p1 = math.asin(s45 / math.sqrt(2))
    sil = [math.degrees(p1) - 45, 180 - math.degrees(p1) - 45]
    for ph in sil:
        b0 = np.array([R * math.cos(math.radians(ph)), R * math.sin(math.radians(ph)), 0.0])
        lam = np.linspace(0, 1, 401)[:, None]
        g = b0 * (1 - lam) + apex * lam
        codes = np.where(cut.side(g) > 0, 7, np.where(cut.behind_plane(g), 2, 1))
        emit_runs(g, codes, origin)
    # the plane (opaque, all of it seen) and the section on it
    a0, a1, b0_, b1 = cut.rect
    corners = cut.X(np.array([a0, a1, a1, a0, a0]), np.array([b0_, b0_, b1, b1, b0_]))
    emit(proj(corners, origin), 1)
    a, b = cut.section()
    sec = proj(cut.X(a, b), origin)
    emit(sec, 5)
    emit(sec, 1)
    return cut, sil


# ---- noses ------------------------------------------------------------------------------------------------
def meridian(r, zz):
    """A point of the meridian plane facing the viewer: radius r towards page right, height zz."""
    return np.outer(r, U) + np.outer(zz, Z)


def nose(key, origin, prof_r, prof_z, half, ring_r, top):
    """prof_r, prof_z: the generating profile from the tip (r = 0, z = L) to the base (r = Rn, z = 0).
    half: True = one half (the generating region is the half-section: (d), (e)), False = symmetric ((a)-(c))."""
    Rn, L = prof_r[-1], prof_z[0]
    emit(proj(meridian(prof_r, prof_z), origin), 1)
    if half:
        emit(proj(meridian(-prof_r, prof_z), origin), 3)               # after half a turn
        emit(proj(meridian(np.array([0.0, 0.0, Rn]), np.array([L, 0.0, 0.0])), origin), 1)  # axis, radius
    else:
        emit(proj(meridian(-prof_r, prof_z), origin), 1)
        emit(proj(meridian(np.array([-Rn, Rn]), np.zeros(2)), origin), 1)                  # base diameter
    ph = np.radians(np.linspace(0, 360, 241))
    emit(proj(np.c_[Rn * np.cos(ph), Rn * np.sin(ph), np.zeros_like(ph)], origin), 3)    # swept base
    # the axis: a centre line from 0.25 cm below the arrow's front to above the tip
    zr = -0.28
    front = proj(np.array([ring_r * math.cos(math.radians(225)), ring_r * math.sin(math.radians(225)), zr]),
                 np.zeros(2))[0, 1]
    zb = (front - 0.25) / (VIEW * VZ[1])
    emit(proj(np.array([[0, 0, zb], [0, 0, L + top]]), origin), 4)
    # the rotation arrow: below the base, round the axis, from the left past the front to the right
    ph = np.radians(np.linspace(150, 338, 121))
    emit(proj(np.c_[ring_r * np.cos(ph), ring_r * np.sin(ph), np.full_like(ph, zr)], origin),
         10 + "abcde".index(key) + 1)
    return L, Rn


def run():
    rows.clear()
    CW = 3.15                                    # cell width (cm)
    TOP_Y, NOSE_Y = -2.85, -7.75                 # page y of the cones' bases and of the noses' bases
    dims = {}
    for i, key in enumerate("abc"):
        x0 = CW * (i + 0.5)
        cut, sil = cone_cut(key, np.array([x0, TOP_Y]))
        if key == "a":
            # the middle drawing: the section face-on, major axis vertical, upper half hatched
            A_SCALE = 1.5
            A, B = cut.A * A_SCALE, cut.B * A_SCALE
            cy = -4.75
            th = np.linspace(0, 2 * np.pi, 361)
            ex, ey = x0 + U2D * B * np.sin(th), cy + U2D * A * np.cos(th)
            up = np.linspace(-np.pi / 2, np.pi / 2, 181)
            emit(np.c_[np.r_[x0 + U2D * B * np.sin(up), x0 + U2D * B * np.sin(up[0])],
                       np.r_[cy + U2D * A * np.cos(up), cy + U2D * A * np.cos(up[0])]], 5)
            emit(np.c_[ex, ey], 1)
            emit(np.array([[x0 - U2D * B, cy], [x0 + U2D * B, cy]]), 1)       # the minor axis
            emit(np.array([[x0, cy - U2D * A - 0.18], [x0, cy + U2D * A + 0.18]]), 4)
            zz = np.linspace(A, 0, 181)
            prof_r = B * np.sqrt(np.maximum(0, 1 - (zz / A) ** 2))
            prof_r[0] = 0
            L, Rn = nose(key, np.array([x0, NOSE_Y]), prof_r, zz, False, B + 0.3, 0.45)
            dims[key] = (A / B / 2, f"ellipse semi-axes A = {cut.A:.3f}, B = {cut.B:.3f} (drawn x{A_SCALE}); "
                                    f"nose ell/d = {A / (2 * B):.3f}")
        else:
            tau = np.linspace(0, 1, 181)
            b = cut.bv - (cut.bv - cut.bc) * tau ** 2
            prof_r = np.sqrt(np.maximum(cut.Q(b), 0))
            prof_z = b - cut.bc
            L, Rn = nose(key, np.array([x0, NOSE_Y]), prof_r, prof_z, False, prof_r[-1] + 0.3, 0.45)
            dims[key] = (L / (2 * Rn), f"segment length {L:.3f}, half chord {Rn:.3f}; nose ell/d = {L / (2 * Rn):.3f}")
    # (d): the circle, its chord, the hatched half-segment; the tangent ogive
    x0 = CW * 3.5
    rho_d, delta = 1.0, 0.78                     # circle radius (the drawing's units), chord from the centre
    D_SCALE = 1.12                               # the top circle's radius in 2D units
    cx, cy = x0, -1.75
    s_ = U2D * D_SCALE
    th = np.linspace(0, 2 * np.pi, 361)
    emit(np.c_[cx + s_ * np.cos(th), cy + s_ * np.sin(th)], 1)
    half = math.sqrt(rho_d ** 2 - delta ** 2)
    emit(np.array([[cx - s_ * half, cy + s_ * delta], [cx + s_ * half, cy + s_ * delta]]), 1)   # the chord
    emit(np.array([[cx, cy + s_ * delta], [cx, cy + s_ * rho_d]]), 1)                          # radial line
    arc = np.linspace(math.pi / 2, math.pi - math.asin(delta), 91)
    poly = np.r_[np.c_[cx + s_ * np.cos(arc), cy + s_ * np.sin(arc)],
                 [[cx, cy + s_ * delta], [cx, cy + s_ * rho_d]]]
    emit(poly, 5)
    ext = 0.22
    emit(np.array([[cx - s_ - ext, cy], [cx + s_ + ext, cy]]), 4)
    emit(np.array([[cx, cy - s_ - ext], [cx, cy + s_ + ext]]), 4)
    # the ogive: length L = half chord, base radius Rn = rho - delta (circle radius rho), in nose units
    Ln = 2.2
    rho_n = Ln / half                            # the circle's radius at the nose's scale
    Rn = rho_n * (rho_d - delta)
    zz = np.linspace(Ln, 0, 181)                 # height above the base; the arc centred at (Rn - rho_n, 0)
    prof_r = np.sqrt(np.maximum(0, rho_n ** 2 - zz ** 2)) + Rn - rho_n
    prof_r[0] = 0
    nose("d", np.array([x0, NOSE_Y]), prof_r, zz, True, Rn + 0.3, 0.45)
    dims["d"] = (Ln / (2 * Rn), f"chord at {delta} rho: half chord {half:.4f} rho, segment height {rho_d - delta:.2f} rho; "
                 f"nose ell/d = {Ln / (2 * Rn):.3f}; top circle at {D_SCALE / rho_n:.3f} of the nose's scale")
    # (e): the right triangle; the cone
    x0 = CW * 4.5
    He, Re = 2.2, 1.13
    tx, ty = x0 - U2D * Re / 2, -2.65            # the right angle
    emit(np.array([[tx, ty + U2D * He], [tx, ty], [tx + U2D * Re, ty], [tx, ty + U2D * He]]), 1)
    q = 0.17
    emit(np.array([[tx, ty + q], [tx + q, ty + q], [tx + q, ty]]), 6)
    zz = np.array([He, 0.0])
    nose("e", np.array([x0, NOSE_Y]), np.array([0.0, Re]), zz, True, Re + 0.3, 0.45)
    dims["e"] = (He / (2 * Re), f"altitude {He}, base {Re}; nose ell/d = {He / (2 * Re):.3f}")
    return dims


if __name__ == "__main__":
    dims = run()
    out = HERE / "fig47.csv"
    with out.open("w") as fh:
        fh.write("x,y,s\n")
        for x, y, s in rows:
            fh.write("nan,nan,%d\n" % s if math.isnan(x) else f"{x:.4f},{y:.4f},{s}\n")
    print(f"{out.name}: {len(rows)} rows; view towards the viewer {np.round(C, 4)}; alpha = {ALPHA:.2f} deg")
    for k_, (fr, txt) in dims.items():
        print(f"  ({k_}) {txt}")
    if "--preview" in sys.argv:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(figsize=(16 / 2.54 * 1.5, 10 / 2.54 * 1.5))
        sty = {1: dict(c="k", lw=1), 2: dict(c="k", lw=0.8, ls=(0, (2, 1.5))), 3: dict(c="b", lw=0.8, ls=(0, (8, 2, 2, 2))),
               7: dict(c="c", lw=0.8, ls=(0, (8, 2, 2, 2))),
               4: dict(c="gray", lw=0.6, ls="-."), 5: dict(c="r", lw=0.4), 6: dict(c="k", lw=0.5)}
        seg = []
        for x, y, s in rows:
            if math.isnan(x):
                if seg:
                    xs, ys = zip(*seg)
                    ax.plot(xs, ys, **sty.get(s, dict(c="g", lw=0.8)))
                seg = []
            else:
                seg.append((x, y))
        ax.set_aspect("equal")
        ax.set_xlim(0, 15.75)
        ax.set_ylim(-9.4, 0)
        fig.savefig(sys.argv[sys.argv.index("--preview") + 1], dpi=110)
