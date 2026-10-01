#!/usr/bin/env python3
"""Chapter 3, Figure 42: drag coefficient of a finless projectile against the spin ratio u/U (0 to 3).

A measured curve (after Hoerner, Fluid-Dynamic Drag; the book gives no equation): digitized from the 1973 art,
figures/ch3/fig42.png. Calibration fig42.calib.json: its "mesh" (every gridline crossing, each gridline fitted
through its ink; the verticals lean by up to 6 px over the chart height and are spaced 71.5-77.5 px) maps pixels
to data piecewise linearly. The curve is followed column by column with the gridlines masked (below u/U = 0.08 it
runs along the 0.2 gridline and is hidden by the mask) and fitted as the cubic
C_D = c0 + c1 x + c2 x^2 + c3 x^3 (x = u/U): the drawn curve leaves 0.20 with a small slope, so no evenness is
imposed (an even fit misses the art by up to 4 px). Writes fig42.csv (x = u/U, cd).
"""
import json
import pathlib
import numpy as np
from PIL import Image
from scipy import ndimage
from scipy.interpolate import LinearNDInterpolator

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent.parent


def load_mesh(name):
    spec = json.loads((HERE / name).read_text())
    m = spec["axes"]["main"]["mesh"]
    X, Y = np.meshgrid(np.array(m["x"]), np.array(m["y"]), indexing="ij")
    to_data = LinearNDInterpolator(np.c_[np.ravel(m["px"]), np.ravel(m["py"])], np.c_[X.ravel(), Y.ravel()])
    return ROOT / spec["crop"], to_data


def line_mask(dark, min_len=40):
    """Every horizontal or vertical run of ink at least min_len long (gridlines, frame), widened by a pixel."""
    mask = np.zeros_like(dark)
    for m, mm in ((dark, mask), (dark.T, mask.T)):
        for i, row in enumerate(m):
            idx = np.flatnonzero(row)
            if idx.size < min_len:
                continue
            cut = np.flatnonzero(np.diff(idx) > 1)
            for s, e in zip(np.r_[idx[0], idx[cut + 1]], np.r_[idx[cut], idx[-1]]):
                if e - s + 1 >= min_len:
                    mm[i, s:e + 1] = True
    return ndimage.binary_dilation(mask, iterations=1)


def runs(v, off):
    idx = np.flatnonzero(v)
    if idx.size == 0:
        return []
    cut = np.flatnonzero(np.diff(idx) > 1)
    return [((s + e) / 2 + off, e - s + 1) for s, e in zip(np.r_[idx[0], idx[cut + 1]], np.r_[idx[cut], idx[-1]])]


def trace(ink, c0, c1, row0, step, max_jump=2.0, max_turn=0.6):
    """Follow the curve from (c0, row0) to column c1: in each column the ink run nearest the prediction, within
    max_jump px of it and with a slope change of at most max_turn."""
    pts, last, lastc, slope = [], float(row0), c0, 0.0
    for c in range(c0, c1, step):
        rr = [r for r in runs(ink[5:330, c], 5) if r[1] <= 6]
        if not rr:
            continue
        pred = last + slope * (c - lastc)
        best = min(rr, key=lambda r: abs(r[0] - pred))[0]
        snew = (best - last) / (c - lastc) if pts else slope
        if abs(best - pred) <= max_jump * max(1, abs(c - lastc) / 3) and (len(pts) < 5 or abs(snew - slope) <= max_turn):
            if pts:
                slope = 0.8 * slope + 0.2 * snew
            pts.append((c, best))
            last, lastc = best, c
    return np.array(pts, float)


if __name__ == "__main__":
    crop, to_data = load_mesh("fig42.calib.json")
    dark = np.asarray(Image.open(crop).convert("L")) < 128
    ink = dark & ~line_mask(dark)
    # seed at u/U = 1.35 (column 300), then left to 0 and right to 3
    P = np.r_[trace(ink, 300, 98, 185.5, -1)[::-1], trace(ink, 301, 547, 185.0, 1)]
    d = to_data(P[:, 0], P[:, 1])
    ok = ~np.isnan(d[:, 0])
    x, cd = d[ok, 0], d[ok, 1]
    A = np.c_[np.ones_like(x), x, x ** 2, x ** 3]
    coef, *_ = np.linalg.lstsq(A, cd, rcond=None)
    f = lambda u: coef[0] + coef[1] * u + coef[2] * u ** 2 + coef[3] * u ** 3
    px_per = 361.0                                    # pixels per unit C_D (0.1 = 36.1 px)
    res = (f(x) - cd) * px_per
    print(f"fig42: {ok.sum()} traced points (u/U {x.min():.3f} .. {x.max():.3f}); C_D = {coef[0]:.5f} "
          f"{coef[1]:+.5f} x {coef[2]:+.5f} x^2 {coef[3]:+.5f} x^3; residual rms {np.sqrt((res ** 2).mean()):.2f} px, "
          f"95% {np.percentile(abs(res), 95):.2f} px, max {abs(res).max():.2f} px")
    print("   " + "  ".join(f"{u:g}: {f(u):.3f}" for u in (0, 0.0172, 1, 2, 3)))
    u = np.round(np.linspace(0, 3, 121), 3)
    (HERE / "fig42.csv").write_text("x,cd\n" + "".join(f"{ui:.3f},{f(ui):.5f}\n" for ui in u))
    print(f"fig42.csv: {len(u)} points")
