#!/usr/bin/env python3
"""Chapter 3, Figure 11: the nose body of the surface-integral notation, matched to the 1973 art.

The book draws a nose body truncated at its base without naming its shape or size. The 1973 drawing,
figures/ch3/fig11.png, turns out to be an orthographic view in the house 3D view itself (elevation 32 deg,
azimuth 45 deg: the body along the view's x axis, the transverse lines through the base centre along y and
z). This script fits the exact nose shapes of the kit (tangent ogive, paraboloid r = R sqrt(x/L), ellipsoid,
cone, and the tangent parabola r = R (2 t - t^2), t = x/L) and the fineness L/R to the drawn outline (the
silhouettes and the seen half of the base rim), with a scale and a shift free. The paraboloid is the shape
that follows the drawn nose, whose upper silhouette curls into the blunt tip (the ogive and the tangent
parabola run to a point well ahead of the drawn tip; the ellipsoid misses the base). Its fineness is weakly
determined: the mean distance of the outline from the ink is within 0.1 px of its least for L/R = 4.3 to 5.2,
and the rim's drawn semi-axis (67 px) with the tip's distance from the base centre (283 px) give 5.3; the
round fineness 2.5 (L/R = 5.0) is drawn. The far half of the rim is drawn in 1973 inside the true ellipse
(a narrower dashed arc); the redraw draws the true one, so it is left out of the overlay.

The outline is that of fig11.tex: in the view c (the unit vector towards the viewer), the surface normal of
the body of revolution r(x), (-r', cos phi, sin phi), is normal to c on the silhouettes,
    c_y cos phi + c_z sin phi = c_x r'(x),  i.e.  cos(phi - phi_c) = (c_x / |c_yz|) r'(x),
and the base rim (x = L) is seen where its normal (-r'(L), cos phi, sin phi) faces the viewer.

Writes fig11.calib.json's transform ("page": house-view page coordinates at tamr view = 1, cm, to crop pixels)
and fig11.csv (the outline: the two silhouettes and the seen rim, as page coordinates, for
    tools/v2/digitize.py overlay figures/v2/ch3/fig11.calib.json --axes page figures/v2/ch3/fig11.csv
fig11.tex computes the same outline itself), and prints the fit, the overlay statistics and where the 1973
art puts the element dS (x and phi on the surface, and the page directions of n and t there).
"""
import json
import pathlib
import numpy as np
from PIL import Image
from scipy import ndimage, optimize

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent.parent
CROP = "figures/ch3/fig11.png"

# the house view (tamrfig.sty, tamr view): page = x (1.15, 0.61) + y (-1.15, 0.61) + z (0, 1.38), cm
EX, EY, EZ = np.array([1.15, 0.61]), np.array([-1.15, 0.61]), np.array([0.0, 1.38])
C = np.cross([1.15, -1.15, 0.0], [0.61, 0.61, 1.38])
C /= np.linalg.norm(C)                     # towards the viewer: (-0.5996, -0.5996, 0.5301)
R = 1.0


def radius(shape, L, x):
    t = np.clip(x / L, 0, 1)
    if shape == "ogive":
        rho = (R * R + L * L) / (2 * R)
        return np.sqrt(np.maximum(rho**2 - (L - x) ** 2, 0)) + R - rho
    if shape == "paraboloid":
        return R * np.sqrt(t)
    if shape == "ellipsoid":
        return R * np.sqrt(1 - (1 - t) ** 2)
    if shape == "cone":
        return R * t
    if shape == "tangent parabola":
        return R * (2 * t - t * t)
    raise ValueError(shape)


def outline(shape, L, n=400):
    """The silhouettes (upper, lower) and the seen and hidden arcs of the base rim, as 3D points."""
    x = L * np.linspace(0, 1, n + 1)[1:] ** 2
    r = radius(shape, L, x)
    dr = np.gradient(r, x)
    amp, phc = np.hypot(C[1], C[2]), np.arctan2(C[2], C[1])
    q = C[0] * dr / amp
    ok = np.abs(q) <= 1
    psi = np.arccos(q[ok])
    up = np.stack([x[ok], r[ok] * np.cos(phc + psi), r[ok] * np.sin(phc + psi)], 1)
    dn = np.stack([x[ok], r[ok] * np.cos(phc - psi), r[ok] * np.sin(phc - psi)], 1)
    phi = np.linspace(0, 2 * np.pi, 721)
    rim = np.stack([np.full_like(phi, L), R * np.cos(phi), R * np.sin(phi)], 1)
    seen = -dr[-1] * C[0] + np.cos(phi) * C[1] + np.sin(phi) * C[2] > 0
    return up, dn, rim[seen], rim[~seen]


def page(p):
    return p[:, :1] * EX + p[:, 1:2] * EY + p[:, 2:3] * EZ


def main():
    ink = np.asarray(Image.open(ROOT / CROP).convert("L")) < 140
    dist = ndimage.distance_transform_edt(~ink)

    def dists(par, shape, L):
        s, tx, ty = par
        up, dn, seen, _ = outline(shape, L)
        q = page(np.vstack([up, dn, seen]))
        px, py = tx + s * q[:, 0], ty - s * q[:, 1]
        xi = np.clip(np.round(px).astype(int), 0, ink.shape[1] - 1)
        yi = np.clip(np.round(py).astype(int), 0, ink.shape[0] - 1)
        return dist[yi, xi]

    def cost(par, shape, L):
        return np.mean(np.minimum(dists(par, shape, L), 8) ** 2)

    best = {}
    for shape in ("ogive", "paraboloid", "ellipsoid", "cone", "tangent parabola"):
        for L in np.arange(3.0, 8.01, 0.1):
            res = optimize.minimize(cost, [42.6, 127.0, 239.0], args=(shape, L), method="Nelder-Mead")
            if res.x[0] < 30:          # a collapsed fit (the scale shrunk onto one stroke)
                continue
            d = dists(res.x, shape, L)
            if shape not in best or d.mean() < best[shape][0]:
                best[shape] = (d.mean(), np.percentile(d, 95), L)
    for shape, (m, p95, L) in best.items():
        print(f"fig11: {shape:17s} best L/R {L:.1f}: mean {m:.2f} px, 95% {p95:.2f} px")
    L = 5.0                            # the fineness drawn (see above)
    res = optimize.minimize(cost, [42.6, 127.0, 239.0], args=("paraboloid", L), method="Nelder-Mead")
    s, tx, ty = res.x
    d = dists(res.x, "paraboloid", L)
    print(f"fig11: drawn: paraboloid L/R = {L:.1f}: mean {d.mean():.2f} px, 95% {np.percentile(d, 95):.2f} px, "
          f"max {d.max():.2f} px; scan scale {s:.2f} px per cm of the unit view (tamr view = "
          f"{s / 150 * 2.54:.3f}), tip at ({tx:.1f}, {ty:.1f}) px")

    # the transform, for digitize.py overlay
    calib = {"crop": CROP,
             "note": "written by fig11.py: house-view page coordinates (tamr view = 1, cm) of the fitted "
                     "body, the paraboloid with L/R = %.1f and its tip at the origin" % L,
             "axes": {"page": {"xlog": False, "ylog": False,
                               "points": [[round(tx, 3), round(ty, 3), 0.0, 0.0],
                                          [round(tx + s, 3), round(ty, 3), 1.0, 0.0],
                                          [round(tx, 3), round(ty - s, 3), 0.0, 1.0]]}}}
    (HERE / "fig11.calib.json").write_text(json.dumps(calib, indent=1) + "\n")
    up, dn, seen, hidden = outline("paraboloid", L)
    q = page(np.vstack([up[::-1], dn, seen]))
    with open(HERE / "fig11.csv", "w") as f:
        f.write("X,Y\n")
        for a, b in q:
            f.write(f"{a:.4f},{b:.4f}\n")

    # where the 1973 art puts dS: its centre at about (208, 168) px
    Lr = L
    target = np.array([208.0, 168.0])
    bestp = None
    for x in np.linspace(0.3, 4.5, 841):
        r, dr = R * np.sqrt(x / Lr), R / (2 * np.sqrt(x * Lr))
        for phd in np.arange(0, 360, 0.5):
            ph = np.radians(phd)
            if -dr * C[0] + np.cos(ph) * C[1] + np.sin(ph) * C[2] <= 0:
                continue
            q = page(np.array([[x, r * np.cos(ph), r * np.sin(ph)]]))[0]
            e = np.hypot(tx + s * q[0] - target[0], ty - s * q[1] - target[1])
            if bestp is None or e < bestp[0]:
                bestp = (e, x, phd)
    e, x, phd = bestp
    dr, ph = R / (2 * np.sqrt(x * Lr)), np.radians(phd)
    nv = np.array([-dr, np.cos(ph), np.sin(ph)]) / np.hypot(1, dr)
    tv = np.array([1, dr * np.cos(ph), dr * np.sin(ph)]) / np.hypot(1, dr)
    pn, pt = page(nv[None])[0], page(tv[None])[0]
    print(f"fig11: dS at x = {x:.2f} R, phi = {phd:.1f} deg (from +y towards +z); n drawn at "
          f"{np.degrees(np.arctan2(pn[1], pn[0])):.0f} deg on the page (the art: 99), t at "
          f"{np.degrees(np.arctan2(pt[1], pt[0])):.0f} deg (the art: 39); angle (n, V) "
          f"{np.degrees(np.arccos(nv[0])):.1f} deg, (t, V) {np.degrees(np.arccos(tv[0])):.1f} deg")


if __name__ == "__main__":
    main()
