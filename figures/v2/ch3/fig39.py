#!/usr/bin/env python3
"""Chapter 3, Figure 39(b): the six fin-tip planforms and their vortex-core paths, digitized from the 1973 art.

The tips and the core positions are Hoerner's measurements (the figure's source, figure-credits.tex), which the
book prints only as this drawing, so both are digitized from figures/ch3/fig39.png (150 dpi):

  tip outlines (tips 2-6; tip 1 is square and is drawn as such in fig39.tex): rays cast from a point inside
      each planform over the scan's ink without the dashes (components of 40 px or less; on tip 2, whose core
      runs just inside the outline, rows 556-576 where the dashes touch it are skipped), at 1 deg steps from
      straight up (the leading edge) round the tip to straight down (the trailing edge); on each ray the inner
      edge of the first ink plus half the line width (1.4 px) is a point of the line's centre. The points
      are scaled vertically (by less than 1 px) to put the straight leading and trailing edges they find on
      the edges' rows, and those within 1 px of the edges are set on them; the points are smoothed by a
      parametric smoothing spline, resampled every 1 px of arc length, kept between the two edges (the
      fillets overshoot them by up to 0.5 px) and joined to them with a continuous slope (join_edge).
  vortex cores (the dashed lines, tips 1-6): the centroids of the dashes (small, upright ink components in
      the tip's column, clear of the lettering) and the point where each core leaves the tip outline, fitted
      by a smoothing spline x(y) and resampled every 2 px down to the foot of the drawing (row 749).

The scan's y axis points down; the CSVs give x relative to the tip's own reference line (the solid vertical
line carried downstream from the tip's outermost point, at the column TIPX below) and y = -row, so that
fig39.tex can set each column at its own position (the redraw spaces the six columns evenly).

Writes fig39-tip2.csv ... fig39-tip6.csv (the tip outline from the leading edge, straight above the rays' centre,
round the tip to the trailing edge, straight below it) and fig39-core1.csv ... fig39-core6.csv (x, y). Prints the residuals of the fits.
"""
import csv, pathlib
import numpy as np
from PIL import Image
from scipy import ndimage
from scipy.interpolate import splprep, splev, UnivariateSpline

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent.parent
SCAN = ROOT / "figures/ch3/fig39.png"

# the solid reference line of each tip (column of the scan), measured with tools/v2/digitize.py lines
TIPX = [47.0, 146.0, 243.5, 333.0, 421.0, 519.5]
LE_ROW, TE_ROW = 487.0, 598.5          # leading and trailing edges (rows)
# the point inside each planform the rays start from (right of the raked tips' trailing-edge corners)
CENTRE = {2: (176.0, 543.0), 3: (288.0, 543.0), 4: (381.0, 543.0), 5: (466.0, 543.0), 6: (549.5, 543.0)}
# rows where a tip's core runs inside its outline and touches it (the rays would stop on the dashes): no points
SKIP_ROWS = {2: (556.0, 576.0)}
# where each core leaves the tip outline (row, column), read on 5x zooms of the scan
CORE_START = {1: (505.0, 45.5), 2: (556.0, 148.5), 3: (522.0, 240.5), 4: (533.0, 331.5),
              5: (515.0, 417.0), 6: (527.0, 516.5)}
# lettering in each column (the Delta AR labels start at this column, below row 695)
LABEL_X = [66.0, 167.0, 268.0, 356.0, 444.0, 543.0]
FOOT = 749.0


def write(name, xy):
    with open(HERE / name, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["x", "y"])
        for x, y in xy:
            w.writerow([f"{x:.2f}", f"{y:.2f}"])


def join_edge(s, y, edge, dev=1.0):
    """From the start of the curve up to the first point that lies `dev` px off the edge, replace the rows by
    a parabola that leaves the edge tangentially and meets the curve there with its slope."""
    off = np.abs(y - edge)
    i1 = int(np.argmax(off > dev))
    slope = abs((y[i1 + 2] - y[i1 - 2]) / (s[i1 + 2] - s[i1 - 2]))
    length = min(2 * off[i1] / max(slope, 1e-6), abs(s[i1] - s[0]))
    u = np.clip(1 - np.abs(s[i1] - s[: i1 + 1]) / length, 0, None)
    out = y.copy()
    out[: i1 + 1] = edge + np.sign(y[i1] - edge) * off[i1] * u ** 2
    return out


def tip_outline(mask, k):
    cx, cy = CENTRE[k]
    pts = []
    for th in np.arange(90.0, 270.01, 1.0):
        d = np.array([np.cos(np.radians(th)), -np.sin(np.radians(th))])
        rr = np.arange(3.0, 150.0, 0.2)
        v = ndimage.map_coordinates(mask, [cy + rr * d[1], cx + rr * d[0]], order=1)
        hit = np.flatnonzero(v > 0.5)
        if hit.size == 0:
            continue
        r = rr[hit[0]] + 1.4
        x, y = cx + r * d[0], cy + r * d[1]
        if k in SKIP_ROWS and SKIP_ROWS[k][0] <= y <= SKIP_ROWS[k][1]:
            continue
        pts.append((x, y))
    p = np.array(pts)
    # the straight leading and trailing edges: the rays find them about a pixel off the lines' centres (and the
    # scan's trailing edge is not quite level), so the points are scaled vertically to put the edges' median
    # ray points (the first and last 11 rays) on LE_ROW and TE_ROW; the points within 1 px of the edges are
    # then set on them
    lr, tr = np.median(p[:11, 1]), np.median(p[-11:, 1])
    p[:, 1] = LE_ROW + (p[:, 1] - lr) * (TE_ROW - LE_ROW) / (tr - lr)
    p[(np.abs(p[:, 1] - LE_ROW) < 1.0) & (p[:, 0] > cx - 25), 1] = LE_ROW
    p[(np.abs(p[:, 1] - TE_ROW) < 1.0) & (p[:, 0] > cx - 40), 1] = TE_ROW
    p[0], p[-1] = (cx, LE_ROW), (cx, TE_ROW)
    tck, u = splprep([p[:, 0], p[:, 1]], s=len(p) * 0.35 ** 2)
    fine = np.linspace(0, 1, 4000)
    x, y = splev(fine, tck)
    seg = np.hypot(np.diff(x), np.diff(y))
    s = np.r_[0, np.cumsum(seg)]
    n = int(s[-1]) + 1
    si = np.linspace(0, s[-1], n)
    xs, ys = np.interp(si, s, x), np.interp(si, s, y)
    # the ends run exactly along the edges, joining the curve with a continuous slope (the spline wavers by
    # up to 0.4 px along the straight parts)
    ys = np.clip(ys, LE_ROW, TE_ROW)              # no overshoot past the edges at the corners
    ys = join_edge(si, ys, LE_ROW)
    ys = join_edge(si[::-1], ys[::-1], TE_ROW)[::-1]
    xs[0], xs[-1] = cx, cx
    fx, fy = splev(u, tck)
    res = np.hypot(fx - p[:, 0], fy - p[:, 1])
    print(f"tip {k}: {len(p)} ray points, spline residual mean {res.mean():.2f} px, max {res.max():.2f} px")
    return xs, ys


def core(dark, lab, objs, k):
    xt = TIPX[k - 1]
    cen = []
    for i, sl in enumerate(objs):
        ys, xs = sl
        h, w = ys.stop - ys.start, xs.stop - xs.start
        m = lab[sl] == i + 1
        area = int(m.sum())
        yy, xx = np.nonzero(m)
        cxx, cyy = xx.mean() + xs.start, yy.mean() + ys.start
        if not (xt - 14 <= cxx <= xt + 32 and 495 <= cyy <= FOOT + 3):
            continue
        if not (4 <= h <= 10 and w <= 4 and 8 <= area <= 26):
            continue
        if cyy > 695 and cxx > LABEL_X[k - 1] - 2:
            continue
        cen.append((cyy, cxx))
    cen.sort()
    r0, c0 = CORE_START[k]
    cen = [(r0, c0)] + [c for c in cen if c[0] > r0 + 2]
    c = np.array(cen)
    w = np.ones(len(c)); w[0] = 5.0
    sp = UnivariateSpline(c[:, 0], c[:, 1], w=w, k=3, s=len(c) * 0.45 ** 2)
    res = np.abs(sp(c[:, 0]) - c[:, 1])
    rows = np.arange(r0, FOOT + 0.1, 2.0)
    print(f"core {k}: {len(c)} points (dashes and start), spline residual mean {res.mean():.2f} px, "
          f"max {res.max():.2f} px; x at the trailing edge {sp(TE_ROW) - xt:+.1f}, at the foot {sp(FOOT) - xt:+.1f} px")
    return sp(rows), rows


def main():
    img = np.asarray(Image.open(SCAN).convert("L")).astype(float)
    dark = img < 150
    lab, _ = ndimage.label(dark)
    objs = ndimage.find_objects(lab)
    # the outlines' ink without the dashes (small components): the cores of tips 2-6 run close to it
    sizes = ndimage.sum(dark, lab, index=np.arange(1, len(objs) + 1))
    big = np.r_[False, sizes > 40][lab].astype(float)
    for k in range(2, 7):
        x, y = tip_outline(big, k)
        write(f"fig39-tip{k}.csv", zip(x - TIPX[k - 1], -y))
    for k in range(1, 7):
        x, y = core(dark, lab, objs, k)
        write(f"fig39-core{k}.csv", zip(x - TIPX[k - 1], -y))


if __name__ == "__main__":
    main()
