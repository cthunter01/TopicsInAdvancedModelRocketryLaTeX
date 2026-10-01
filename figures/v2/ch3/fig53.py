#!/usr/bin/env python3
"""Chapter 3, Figure 53: C_D/C_Ds against Mach number for a finned body with ogive and half-round noses.

(a) Experimental (Hoerner, the chapter's reference 9): measured curves, so digitized from the 1973 art,
    figures/ch3/fig53.png (calibration fig53.calib.json: the hand-ruled grid is uneven and turned slightly, so
    pixels are mapped by interpolating between the drawn gridlines). Below M = 0.9 both curves are the
    subsonic value, C_D/C_Ds = 1 (C_Ds is the subsonic C_D, ch3-sec7.tex), written as exactly 1. The two
    curves are one line up to their split just below the ogive's peak (as printed, and as Table 8's equal
    values at M = 0.95 and 1.00 say); the half-round curve is written from the split on. The traced centre
    line of each curve is smoothed (a smoothing spline along its arc length, held closer at the knee and the
    peaks; residual about 0.3 px rms, 1 px at most) and resampled: fig53-a-ogive.csv, fig53-a-half.csv
    (columns M, r = CD/CDs).
(b) The book's approximations, computed: eq. (214a) 1.0 + 35.5 (M - 0.9)^2 (0.9 <= M <= 1.05) and (214b)
    1.27 + 0.53 exp(-5.2 (M - 1.05)) (1.05 <= M <= 2.0) for the ogive (sharp) nose; eq. (215a)
    1.0 + 4.88 (M - 0.9)^1.1 (0.9 <= M <= 1.2) and (215b) 2.0 + 0.3 exp(-5.75 (M - 1.2)) (1.2 <= M <= 2.0)
    for the half-round nose; 1.0 below M = 0.9, where the formulas start from it (as printed). Each peak
    is the value of the second formula (1.800 and 2.300, Table 8's [C_D/C_Ds]_a). fig53-b-ogive.csv
    (M from 0), fig53-b-half.csv (from M = 0.9: below it the curves are one line, drawn with the ogive's).

Run from anywhere; prints the digitized curves at Table 8's Mach numbers beside the table's experimental
values, and writes the four CSVs beside this script.
"""
import json
import pathlib
import numpy as np
from PIL import Image
from scipy.interpolate import make_smoothing_spline

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent.parent
MS = np.round(np.arange(0, 2.01, 0.2), 1)        # the vertical gridlines
YS = np.round(np.arange(0, 2.41, 0.4), 1)        # the horizontal gridlines

# Table 8 (ch3-sec7.tex), experimental columns, for the comparison printed by this script
TAB_M = [0.90, 0.95, 1.00, 1.05, 1.10, 1.20, 1.40, 1.60, 1.80, 2.00]
TAB_OG = [1.00, 1.17, 1.43, 1.70, 1.67, 1.57, 1.40, 1.30, 1.27, 1.27]
TAB_HR = [1.00, 1.17, 1.43, 1.76, 2.00, 2.17, 2.10, 2.03, 2.00, 2.00]


class Grid:
    """Pixel <-> data through the drawn gridlines of one panel: each vertical line is straight between its
    columns at two rows, each horizontal line between its rows at two columns; a point's M (y) is
    interpolated between the vertical (horizontal) lines at its row (column)."""

    def __init__(self, spec):
        self.r0, self.r1 = spec["rows"]
        self.v0, self.v1 = (np.array(v, float) for v in spec["vcols"])
        self.c0, self.c1 = spec["cols"]
        self.h0, self.h1 = (np.array(h, float) for h in spec["hrows"])

    def vcols(self, row):
        return self.v0 + (self.v1 - self.v0) * (row - self.r0) / (self.r1 - self.r0)

    def hrows(self, col):
        return self.h0 + (self.h1 - self.h0) * (col - self.c0) / (self.c1 - self.c0)

    def to_data(self, px, py):
        m = np.array([np.interp(x, self.vcols(y), MS) for x, y in zip(px, py)])
        v = np.array([np.interp(-y, -self.hrows(x), YS) for x, y in zip(px, py)])
        return m, v

    def to_pixel(self, m, v):
        m, v = np.atleast_1d(m).astype(float), np.atleast_1d(v).astype(float)
        px, py = np.interp(m, MS, self.v1), np.interp(v, YS, self.h0)
        for _ in range(8):
            px = np.array([np.interp(a, MS, self.vcols(y)) for a, y in zip(m, py)])
            py = np.array([np.interp(b, YS, self.hrows(x)) for b, x in zip(v, px)])
        return px, py


def runs(v, off):
    """(centre, first, last) of each run of ink in a 1-D mask (index + off)."""
    idx = np.flatnonzero(v)
    if idx.size == 0:
        return []
    cut = np.flatnonzero(np.diff(idx) > 1)
    return [((s + e) / 2 + off, s + off, e + off) for s, e in zip(np.r_[idx[0], idx[cut + 1]], np.r_[idx[cut], idx[-1]])]


def trace_cols(ink, g, c0, c1, row, top, bot, max_jump=3.0, mask=1.6):
    """Follow a curve column by column from c0 to c1 (either direction), from `row`: in each column the
    centre of the ink run nearest the prediction, with the horizontal gridlines masked and the columns on a
    vertical gridline skipped (the curve is bridged across both)."""
    step = 1 if c1 >= c0 else -1
    pts, last, slope, lastc = [], float(row), 0.0, c0
    for c in range(c0, c1 + step, step):
        if np.min(np.abs(g.vcols(last) - c)) < 2.6:
            continue
        col = ink[top:bot, c].copy()
        for r in g.hrows(c) - top:
            col[max(int(np.floor(r - mask)), 0):max(int(np.ceil(r + mask)) + 1, 0)] = False
        rr = runs(col, top)
        if not rr:
            continue
        pred = last + slope * (c - lastc)
        best = min(rr, key=lambda r: abs(r[0] - pred))[0]
        if abs(best - pred) <= max_jump + 0.5 * abs(slope) * abs(c - lastc):
            if pts:
                slope = 0.6 * slope + 0.4 * (best - last) / (c - lastc)
            last, lastc = best, c
            pts.append((c, best))
    return pts


def trace_rows(ink, g, r0, r1, col, left, right, max_jump=3.0, half_width=1.2):
    """The same row by row (for the steep parts), from row r0 to r1 (upwards when r1 < r0). A run that
    merges with a vertical gridline is read from its edge away from the gridline."""
    step = 1 if r1 >= r0 else -1
    pts, last, slope, lastr = [], float(col), 0.0, r0
    for r in range(r0, r1 + step, step):
        vc = g.vcols(r)
        cand = []
        for cen, a, b in runs(ink[r, left:right], left):
            near = vc[np.argmin(np.abs(vc - cen))]
            if b - a + 1 <= 3 and abs(cen - near) < 1.6:
                continue                                   # the gridline alone
            if a <= near <= b:                             # merged with the gridline
                cen = (b - half_width) if (b - near) > (near - a) else (a + half_width)
            cand.append(cen)
        if not cand:
            continue
        pred = last + slope * (r - lastr)
        best = min(cand, key=lambda x: abs(x - pred))
        if abs(best - pred) <= max_jump + 0.5 * abs(slope) * abs(r - lastr):
            if pts:
                slope = 0.6 * slope + 0.4 * (best - last) / (r - lastr)
            last, lastr = best, r
            pts.append((best, r))
    return pts


def smooth(px, py, g, sharp=(), lam=2000.0, ds=1.5):
    """Smooth an ordered pixel polyline along its arc length (a smoothing spline in each coordinate) and
    resample it every ds pixels; returns data. Points near the pixels in `sharp` (the knee and the peaks)
    are weighted up (a Gaussian of 6 px along the curve), so the smoothing irons out the tracing noise
    of the long, gently curved parts without rounding those off."""
    px, py = np.asarray(px, float), np.asarray(py, float)
    s = np.r_[0, np.cumsum(np.hypot(np.diff(px), np.diff(py)))]
    keep = np.r_[True, np.diff(s) > 1e-6]
    px, py, s = px[keep], py[keep], s[keep]
    w = np.ones_like(s)
    for cx, cy in sharp:
        k = np.argmin(np.hypot(px - cx, py - cy))
        w += 30.0 * np.exp(-(s - s[k]) ** 2 / (2 * 6.0 ** 2))
    sx = make_smoothing_spline(s, px, w=w, lam=lam)
    sy = make_smoothing_spline(s, py, w=w, lam=lam)
    ss = np.linspace(0, s[-1], max(int(s[-1] / ds), 2))
    return g.to_data(sx(ss), sy(ss)), (px, py, sx(s), sy(s))


def at(m, y, x):
    return float(np.interp(x, m, y))


def main():
    spec = json.loads((HERE / "fig53.calib.json").read_text())
    ga = Grid(spec["grid"]["a"])        # (b) is computed; its grid serves the overlay check
    ink = np.asarray(Image.open(ROOT / spec["crop"]).convert("L")) < 150

    # ---- (a) ogive: the common rise (rows 172 -> 98), the peak and decline (cols 341 -> 555) ----
    rise = trace_rows(ink, ga, 172, 98, 316.0, 300, 346)
    ogp = trace_cols(ink, ga, 341, 555, 96.5, 80, 165)
    # the flat part: the line leaves 1.0 at about col 312 (M 0.9); start the rise from the flat line there
    og = [(c, r) for c, r in [(306.0, 174.5), (309.0, 174.4)]] + rise + ogp
    (m_og, y_og), diag_og = smooth([p[0] for p in og], [p[1] for p in og], ga, sharp=[(312, 173.5), (345, 96.5)])
    # ---- (a) half-round: from the split (row 96) up to its peak (row mode), then on to M = 2.0 ----
    up = trace_rows(ink, ga, 95, 49, 341.5, 336, 372, max_jump=4.0)
    hrp = trace_cols(ink, ga, 366, 452, 48.5, 30, 63, max_jump=5.0, mask=0.9)
    # beyond M 1.55 the lettering "Half-round" stands just above the curve (rows 44-56): look below it
    hrq = trace_cols(ink, ga, 453, 555, hrp[-1][1], 57, 72, max_jump=4.0, mask=0.9)
    # from M 1.74 (col 495) the dashed line lies on the 2.0 gridline (its dashes show on both sides of it):
    # read there as the gridline
    hrq = [p for p in hrq if p[0] <= 483] + [(c, ga.hrows(c)[5]) for c in range(495, 557, 3)]
    hr = [rise[-1]] + up + hrp + hrq
    (m_hr, y_hr), diag_hr = smooth([p[0] for p in hr], [p[1] for p in hr], ga, sharp=[(340, 97), (380, 44.7)])

    # Below M = 0.9 the curves are the subsonic value 1.0, written exactly. The drawn flat line is ruled
    # straight while the grid falls to the right, so near M = 0.9 it reads 1.012 (1.3 px high): that offset
    # is taken out of the traced rise, tapering to nothing at M = 1.0, so that the curve leaves 1.0 at 0.9.
    off = 0.012 * np.clip((1.0 - m_og) / 0.1, 0, 1)
    k = (m_og >= 0.875) & (m_og <= 2.0)
    m_og, y_og = np.r_[0.0, m_og[k]], np.r_[1.0, np.maximum((y_og - off)[k], 1.0)]
    # both curves end at the grid's right edge, M = 2.0 (the traced lines stop a pixel or two short of it)
    k = m_hr <= 2.0
    m_hr, y_hr = m_hr[k], y_hr[k]
    m_og, y_og = np.r_[m_og, 2.0], np.r_[y_og, y_og[-1]]
    m_hr, y_hr = np.r_[m_hr, 2.0], np.r_[y_hr, y_hr[-1]]

    # residuals of the smoothing, in pixels
    for name, (px, py, fx, fy) in (("ogive", diag_og), ("half-round", diag_hr)):
        d = np.hypot(px - fx, py - fy)
        print(f"(a) {name}: {len(px)} traced points; smoothing residual rms {np.sqrt((d**2).mean()):.2f} px, "
              f"95% {np.percentile(d, 95):.2f} px, max {d.max():.2f} px")
    print("(a) against Table 8 [CD/CDs]_e:   M   ogive (table)   half-round (table)")
    for mm, to, th in zip(TAB_M, TAB_OG, TAB_HR):
        ho = at(m_hr, y_hr, mm) if mm >= m_hr[0] else at(m_og, y_og, mm)
        print(f"   {mm:.2f}   {at(m_og, y_og, mm):.3f} ({to:.2f})   {ho:.3f} ({th:.2f})")
    i = np.argmax(y_og); h = np.argmax(y_hr)
    print(f"(a) ogive peak {y_og[i]:.3f} at M {m_og[i]:.3f}; half-round peak {y_hr[h]:.3f} at M {m_hr[h]:.3f}; "
          f"split at M {m_hr[0]:.3f}, {y_hr[0]:.3f}; ends {y_og[-1]:.3f}, {y_hr[-1]:.3f} at M {m_og[-1]:.3f}")
    (HERE / "fig53-a-ogive.csv").write_text("M,r\n" + "".join(f"{a:.4f},{b:.4f}\n" for a, b in zip(m_og, y_og)))
    (HERE / "fig53-a-half.csv").write_text("M,r\n" + "".join(f"{a:.4f},{b:.4f}\n" for a, b in zip(m_hr, y_hr)))

    # ---- (b) computed ----
    def og_b(M):
        return np.where(M < 0.9, 1.0, np.where(M <= 1.05, 1.0 + 35.5 * (M - 0.9) ** 2,
                                               1.27 + 0.53 * np.exp(-5.2 * (M - 1.05))))

    def hr_b(M):
        return np.where(M < 0.9, 1.0, np.where(M <= 1.2, 1.0 + 4.88 * np.clip(M - 0.9, 0, None) ** 1.1,
                                               2.0 + 0.3 * np.exp(-5.75 * (M - 1.2))))
    mo = np.r_[0.0, np.linspace(0.9, 1.05, 61)[:-1], np.linspace(1.05, 2.0, 191)]
    yo = og_b(mo)
    yo[np.isclose(mo, 1.05)] = 1.27 + 0.53                 # the peak: (214b) at 1.05
    mh = np.r_[np.linspace(0.9, 1.2, 121)[:-1], np.linspace(1.2, 2.0, 161)]
    yh = hr_b(mh)
    yh[np.isclose(mh, 1.2)] = 2.0 + 0.3                    # the peak: (215b) at 1.2
    (HERE / "fig53-b-ogive.csv").write_text("M,r\n" + "".join(f"{a:.4f},{b:.5f}\n" for a, b in zip(mo, yo)))
    (HERE / "fig53-b-half.csv").write_text("M,r\n" + "".join(f"{a:.4f},{b:.5f}\n" for a, b in zip(mh, yh)))
    print("(b) at Table 8's M:  " + "  ".join(f"{mm:.2f}: {float(og_b(np.array(mm))):.3f}/{float(hr_b(np.array(mm))):.3f}"
                                             for mm in TAB_M))
    print("fig53-a-ogive.csv, fig53-a-half.csv, fig53-b-ogive.csv, fig53-b-half.csv written")


if __name__ == "__main__":
    main()
