#!/usr/bin/env python3
"""Chapter 3, Figure 41: drag coefficient against angle of attack, 0-10 deg.

Two curves, both from the zero-lift value 0.75 (the caption: the same drag coefficient for both rockets at zero
angle of attack; ch3-sec5b.tex: the trial rocket is assumed to have the Aerobee-Hi's "about 0.75"):

  trial   "Rocket of Figure 37, semiempirical": computed, C_D = 0.75 + C_D(alpha) with eq. (149),
          C_D(alpha) = 16.83 alpha^2 + 8.9 alpha^3 (alpha in radians); the total column of Table 4
          (.005 at 1 deg ... .559 at 10 deg) is this function.
  stine   "Stine Aerobee-Hi experiment": Stine's wind-tunnel measurements (ref. 18), which the book does not
          tabulate: digitized from the 1973 art, figures/ch3/fig41.png. Calibration fig41.calib.json: its "mesh"
          (every gridline crossing, each gridline fitted through its ink; the scan is skewed by up to 5 px) maps
          pixels to data piecewise linearly. The curve is followed column by column (gridlines masked, the
          Stine leader that meets it at 4.8 deg rejected by a limit on the change of slope) and fitted as
          C_D = 0.75 + c2 a^2 + c3 a^3 (a in degrees): even in a at zero (drag is symmetric in the angle of
          attack) and through the common zero-lift value (a free constant gives 0.754, 0.6 px higher).

Writes fig41.csv (alpha in degrees, stine, trial).
"""
import json
import math
import pathlib
import numpy as np
from PIL import Image
from scipy import ndimage
from scipy.interpolate import LinearNDInterpolator

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent.parent
CD0 = 0.75


def trial(a_deg):
    a = np.radians(a_deg)
    return CD0 + 16.83 * a ** 2 + 8.9 * a ** 3                      # eq. (149) + the zero-lift 0.75


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
    """Follow a curve from (c0, row0) to column c1: in each column the ink run nearest the prediction, accepted
    only if within max_jump px of it and if the slope it implies differs from the running slope by at most
    max_turn (so a steep leader that meets the curve is not followed)."""
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
    crop, to_data = load_mesh("fig41.calib.json")
    dark = np.asarray(Image.open(crop).convert("L")) < 128
    ink = dark & ~line_mask(dark)
    # seed on the solid curve at 9.4 deg (column 550, clear of gridlines), then left to 0 deg and right to 10
    P = np.r_[trace(ink, 550, 99, 38.5, -1)[::-1], trace(ink, 551, 567, 38.0, 1)]
    d = to_data(P[:, 0], P[:, 1])
    ok = ~np.isnan(d[:, 0])
    a, cd = d[ok, 0], d[ok, 1]
    A = np.c_[a ** 2, a ** 3]
    (c2, c3), *_ = np.linalg.lstsq(A, cd - CD0, rcond=None)
    res = (CD0 + A @ [c2, c3] - cd) * (abs(P[ok, 1].max() - P[ok, 1].min()) / abs(cd.max() - cd.min()))
    stine = lambda x: CD0 + c2 * x ** 2 + c3 * x ** 3
    print(f"stine: {ok.sum()} traced points, fit C_D = 0.75 + {c2:.6f} a^2 {c3:+.7f} a^3 (a deg); residual rms "
          f"{np.sqrt((res ** 2).mean()):.2f} px, 95% {np.percentile(abs(res), 95):.2f} px, max {abs(res).max():.2f} px; "
          f"at 10 deg {stine(10.0):.3f} (doubled: {stine(10.0) / CD0:.2f} x)")
    print(f"trial: at 10 deg {trial(10.0):.3f} (Table 4: 0.75 + .559)")
    al = np.round(np.linspace(0, 10, 101), 2)
    rows = ["alpha,stine,trial"] + [f"{x:.2f},{stine(x):.5f},{trial(x):.5f}" for x in al]
    (HERE / "fig41.csv").write_text("\n".join(rows) + "\n")
    print(f"fig41.csv: {len(al)} points")
