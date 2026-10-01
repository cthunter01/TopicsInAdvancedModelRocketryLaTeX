#!/usr/bin/env python3
"""Digitize curves from a version 1 scan crop, and check any curve (digitized or computed) against it.

All pixel coordinates are those of the crop figures/<dir>/<name>.png (150 dpi, origin top-left, y down).

  digitize.py lines <crop> [--min-len PX] [--dark T]
      Print the long horizontal and vertical lines (axes, gridlines, frames) with their centre, thickness
      and extent: read the tick values off them to write the calibration.

  digitize.py ticks <crop> [--xaxis ROW] [--yaxis COL] [--gap PX] [--depth PX] [--span LO,HI]
      List the tick marks along an axis line found by "lines": ink groups in a thin band just outside and
      just inside it (wide groups, marked (wN), are usually lettering or a curve, not ticks).

  digitize.py trace <calib.json> --axes KEY --seed PX,PY [--to PX] [--dir right|left] [--mode cols|rows]
                    [--max-jump PX] [--gap PX] [--step PX] [--smooth N] [--dark T] --out FILE.csv
      Follow one curve from a seed pixel on it, column by column (--mode rows: row by row, for steep
      parts), skipping gridlines (masked) and bridging dashes and crossings up to --gap pixels; write
      x,y in data coordinates. It stops at --to (a column, or a row with --mode rows) or else at the
      edge of the calibrated area. Trace a curve in pieces when it turns steep, and join the CSVs.

  digitize.py overlay <calib.json> --axes KEY FILE.csv[:LABEL] ... [--out PNG] [--dark T] [--tol PX]
      Draw each CSV (data coordinates; first two columns x,y; a header row is skipped) over the faded crop
      and report, per curve, the distance of its points from the nearest ink of the scan: mean, 95th
      percentile and maximum in pixels and millimetres. A curve whose 95th percentile exceeds --tol
      (default 3 px = 0.5 mm) is reported as MISMATCH and the command exits 1.

Calibration file (JSON), one entry per set of axes in the crop (panels have their own):
  {"crop": "figures/ch3/fig02.png",
   "axes": {"main": {"xlog": false, "ylog": false,
                     "points": [[px, py, x, y], ...]}}}      # >= 3 points not on one line
Each point is a pixel whose data coordinates are known: tick marks, gridline crossings, axis origin.
The map pixel -> (x or log10 x, y or log10 y) is the least-squares affine fit, so a slightly rotated
scan is handled; the fit residual is printed and should be under a pixel.
Optional "xgrid": [[px, x], ...] and "ygrid": [[py, y], ...] (the pixel column/row of each drawn gridline
and its value) replace the fit on that axis by piecewise-linear interpolation between the drawn lines:
for the 1973 "log" paper whose intermediate lines are not at log positions (Ch3 Figs 22, 26, 51, 52, 55).
"""
import argparse, csv, json, math, pathlib, sys
import numpy as np
from PIL import Image, ImageDraw
from scipy import ndimage

ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
PX_MM = 25.4 / 150


def load_gray(path):
    return np.asarray(Image.open(ROOT / path if not pathlib.Path(path).is_absolute() else path).convert("L"), dtype=np.uint8)


# ---- lines ----------------------------------------------------------------------------------------------

def long_runs(dark, axis, min_len, max_gap=2):
    """For each row (axis=0) or column (axis=1), the longest run of ink allowing gaps up to max_gap px:
    returns list of (index, start, end) with end-start+1 >= min_len."""
    m = dark if axis == 0 else dark.T
    out = []
    for i, row in enumerate(m):
        idx = np.flatnonzero(row)
        if idx.size < min_len:
            continue
        splits = np.flatnonzero(np.diff(idx) > max_gap + 1)
        starts = np.r_[idx[0], idx[splits + 1]]
        ends = np.r_[idx[splits], idx[-1]]
        k = np.argmax(ends - starts)
        if ends[k] - starts[k] + 1 >= min_len:
            out.append((i, int(starts[k]), int(ends[k])))
    return out


def group_lines(runs):
    """Merge adjacent rows/columns into lines: (centre, thickness, start, end)."""
    lines, cur = [], []
    for r in runs:
        if cur and r[0] - cur[-1][0] > 1:
            lines.append(cur); cur = []
        cur.append(r)
    if cur:
        lines.append(cur)
    res = []
    for g in lines:
        idx = [r[0] for r in g]
        res.append((sum(idx) / len(idx), len(idx), min(r[1] for r in g), max(r[2] for r in g)))
    return res


def line_mask(dark, min_len):
    """Pixels on long horizontal or vertical runs (gridlines, axes)."""
    mask = np.zeros_like(dark, dtype=bool)
    for i, s, e in long_runs(dark, 0, min_len):
        mask[i, s:e + 1] = True
    for i, s, e in long_runs(dark, 1, min_len):
        mask[s:e + 1, i] = True
    return mask


def cmd_lines(a):
    img = load_gray(a.crop)
    dark = img < a.dark
    h, w = dark.shape
    min_len = a.min_len or int(0.25 * min(h, w))
    print(f"{a.crop}: {w} x {h} px; lines at least {min_len} px long (dark < {a.dark})")
    for name, axis in (("horizontal (y = row)", 0), ("vertical (x = column)", 1)):
        ls = group_lines(long_runs(dark, axis, min_len))
        print(f"{name}: {len(ls)}")
        for c, t, s, e in ls:
            print(f"  at {c:7.1f}  thick {t}  from {s} to {e}  (len {e - s + 1})")


def cmd_ticks(a):
    """Tick marks along an axis line: ink groups in thin bands just outside and just inside the line."""
    img = load_gray(a.crop)
    dark = img < a.dark

    def groups(mask1d, off):
        idx = np.flatnonzero(mask1d) + off
        out, cur = [], []
        for i in idx:
            if cur and i - cur[-1] > 1:
                out.append(cur); cur = []
            cur.append(i)
        if cur:
            out.append(cur)
        return [f"{sum(c) / len(c):.1f}" + ("" if len(c) <= 4 else f"(w{len(c)})") for c in out]

    lo, hi = (int(v) for v in a.span.split(",")) if a.span else (0, None)
    if a.xaxis is not None:
        r = a.xaxis
        for name, (r0, r1) in (("below", (r + a.gap, r + a.gap + a.depth)), ("above", (r - a.gap - a.depth, r - a.gap))):
            band = dark[max(r0, 0):r1, lo:hi].any(axis=0)
            print(f"x axis at row {r}, ticks {name} (rows {r0}-{r1}): columns " + " ".join(groups(band, lo)))
    if a.yaxis is not None:
        c = a.yaxis
        for name, (c0, c1) in (("left", (c - a.gap - a.depth, c - a.gap)), ("right", (c + a.gap, c + a.gap + a.depth))):
            band = dark[lo:hi, max(c0, 0):c1].any(axis=1)
            print(f"y axis at column {c}, ticks {name} (columns {c0}-{c1}): rows " + " ".join(groups(band, lo)))


# ---- calibration ----------------------------------------------------------------------------------------

class Axes:
    def __init__(self, spec):
        self.xlog, self.ylog = spec.get("xlog", False), spec.get("ylog", False)
        pts = np.array(spec["points"], dtype=float)
        if len(pts) < 3:
            raise SystemExit("calibration needs at least 3 points per axes")
        P = np.c_[pts[:, 0], pts[:, 1], np.ones(len(pts))]
        D = np.c_[self._fx(pts[:, 2]), self._fy(pts[:, 3])]
        self.A, *_ = np.linalg.lstsq(P, D, rcond=None)          # pixel -> data'
        B, *_ = np.linalg.lstsq(np.c_[D, np.ones(len(D))], pts[:, :2], rcond=None)
        self.B = B                                               # data' -> pixel
        back = np.c_[D, np.ones(len(D))] @ B
        self.residual = float(np.max(np.hypot(*(back - pts[:, :2]).T)))
        self.pix = pts[:, :2]
        # drawn-gridline calibration (paper whose "log" lines are not at log positions): pixel -> value
        # piecewise-linear between the listed gridlines, overriding the affine fit on that axis
        self.xgrid = np.array(spec["xgrid"], float) if spec.get("xgrid") else None
        self.ygrid = np.array(spec["ygrid"], float) if spec.get("ygrid") else None
        # a skewed frame (Ch4 Figs 10, 12-14): xgrid read along lines parallel to the drawn y axis
        # ("lean": {"xaxis": [a, b] (row = a col + b), "yaxis": [s, c] (col = s row + c)})
        self.lean = spec.get("lean")

    def _fx(self, x):
        return np.log10(x) if self.xlog else np.asarray(x, float)

    def _fy(self, y):
        return np.log10(y) if self.ylog else np.asarray(y, float)

    def to_data(self, px, py):
        d = np.c_[px, py, np.ones(len(px))] @ self.A
        x = 10 ** d[:, 0] if self.xlog else d[:, 0]
        y = 10 ** d[:, 1] if self.ylog else d[:, 1]
        if self.xgrid is not None:
            cx = px
            if self.lean:
                (a, b), s = self.lean["xaxis"], self.lean["yaxis"][0]
                cx = px + s * (a * np.asarray(px) + b - np.asarray(py)) / (1 - a * s)
            x = np.interp(cx, self.xgrid[:, 0], self.xgrid[:, 1])
        if self.ygrid is not None:
            o = np.argsort(self.ygrid[:, 0])
            y = np.interp(py, self.ygrid[o, 0], self.ygrid[o, 1])
        return x, y

    def to_pixel(self, x, y):
        p = np.c_[self._fx(x), self._fy(y), np.ones(len(x))] @ self.B
        px, py = p[:, 0], p[:, 1]
        if self.xgrid is not None:
            o = np.argsort(self.xgrid[:, 1])
            px = np.interp(x, self.xgrid[o, 1], self.xgrid[o, 0])
            if self.lean:   # from the foot (px, on the x axis line) up the drawn y axis to height y
                (a, b), s, A = self.lean["xaxis"], self.lean["yaxis"][0], self.A
                rf = a * px + b
                t = (self._fy(y) - (A[0, 1] * px + A[1, 1] * rf + A[2, 1])) / (A[0, 1] * s + A[1, 1])
                px, py = px + s * t, rf + t
        if self.ygrid is not None:
            o = np.argsort(self.ygrid[:, 1])
            py = np.interp(y, self.ygrid[o, 1], self.ygrid[o, 0])
        return px, py


def load_calib(path, key):
    spec = json.loads((ROOT / path).read_text() if not pathlib.Path(path).is_absolute() else pathlib.Path(path).read_text())
    if key not in spec["axes"]:
        raise SystemExit(f"{path}: no axes '{key}' (have: {', '.join(spec['axes'])})")
    ax = Axes(spec["axes"][key])
    print(f"calibration {path} [{key}]: max residual {ax.residual:.2f} px")
    return spec["crop"], ax


# ---- trace ----------------------------------------------------------------------------------------------

def runs_in(col):
    """Centres and lengths of ink runs in a 1-D boolean array."""
    idx = np.flatnonzero(col)
    if idx.size == 0:
        return []
    splits = np.flatnonzero(np.diff(idx) > 1)
    starts = np.r_[idx[0], idx[splits + 1]]
    ends = np.r_[idx[splits], idx[-1]]
    return [((s + e) / 2, e - s + 1) for s, e in zip(starts, ends)]


def cmd_trace(a):
    crop, ax = load_calib(a.calib, a.axes)
    img = load_gray(crop)
    dark = img < a.dark
    h, w = dark.shape
    ink = dark & ~line_mask(dark, a.min_len or int(0.25 * min(h, w)))
    if a.mode == "rows":
        ink = ink.T
    sx, sy = (float(v) for v in a.seed.split(","))
    u, v = (sy, sx) if a.mode == "rows" else (sx, sy)      # u: stepping coordinate, v: followed one
    step = a.step if a.dir == "right" else -a.step
    if a.to is not None:
        stop = a.to
    else:  # default: the edge of the calibrated area (the extreme calibration pixels)
        edge = ax.pix[:, 1] if a.mode == "rows" else ax.pix[:, 0]
        stop = int(math.floor(edge.max())) if step > 0 else int(math.ceil(edge.min()))
    pts, last_u, slope = [], None, 0.0
    cu = int(round(u))
    # snap the seed
    cand = runs_in(ink[:, cu])
    if not cand:
        raise SystemExit(f"no ink at the seed column {cu}")
    v = min(cand, key=lambda r: abs(r[0] - v))[0]
    pts.append((cu, v)); last_u = cu
    cu += step
    while (cu <= stop if step > 0 else cu >= stop) and 0 <= cu < ink.shape[1]:
        pred = pts[-1][1] + slope * (cu - last_u)
        cand = runs_in(ink[:, cu])
        gap = abs(cu - last_u)
        best = min(cand, key=lambda r: abs(r[0] - pred)) if cand else None
        if best is not None and abs(best[0] - pred) <= a.max_jump * max(1, gap / a.step):
            if len(pts) >= 2:
                slope = 0.6 * slope + 0.4 * (best[0] - pts[-1][1]) / (cu - last_u)
            else:
                slope = (best[0] - pts[-1][1]) / (cu - last_u)
            pts.append((cu, best[0])); last_u = cu
        elif gap > a.gap:
            print(f"stopped at {'row' if a.mode == 'rows' else 'column'} {last_u}: no continuation within {a.gap} px")
            break
        cu += step
    arr = np.array(pts, float)
    if a.smooth > 1 and len(arr) > a.smooth:
        k = np.ones(a.smooth) / a.smooth
        arr[:, 1] = np.convolve(np.pad(arr[:, 1], a.smooth // 2, mode="edge"), k, mode="valid")[: len(arr)]
    px, py = (arr[:, 1], arr[:, 0]) if a.mode == "rows" else (arr[:, 0], arr[:, 1])
    x, y = ax.to_data(px, py)
    order = np.argsort(x) if a.mode == "cols" else np.arange(len(x))
    out = ROOT / a.out if not pathlib.Path(a.out).is_absolute() else pathlib.Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    with open(out, "w", newline="") as f:
        wr = csv.writer(f)
        wr.writerow(["x", "y"])
        for xi, yi in zip(x[order], y[order]):
            wr.writerow([f"{xi:.6g}", f"{yi:.6g}"])
    print(f"{len(x)} points, x {x.min():.4g} .. {x.max():.4g}, y {y.min():.4g} .. {y.max():.4g} -> {a.out}")


# ---- overlay --------------------------------------------------------------------------------------------

COLOURS = [(220, 30, 30), (30, 90, 220), (20, 150, 60), (200, 120, 0), (150, 40, 170), (0, 150, 160)]


def read_xy(path):
    xs, ys = [], []
    with open(ROOT / path if not pathlib.Path(path).is_absolute() else path) as f:
        for row in csv.reader(f):
            try:
                xs.append(float(row[0])); ys.append(float(row[1]))
            except (ValueError, IndexError):
                continue
    return np.array(xs), np.array(ys)


def cmd_overlay(a):
    crop, ax = load_calib(a.calib, a.axes)
    img = load_gray(crop)
    dark = img < a.dark
    dist = ndimage.distance_transform_edt(~dark)
    base = Image.fromarray((255 - (255 - img) * 0.45).astype(np.uint8)).convert("RGB")
    d = ImageDraw.Draw(base)
    bad = False
    for i, spec in enumerate(a.curves):
        path, _, label = spec.partition(":")
        x, y = read_xy(path)
        px, py = ax.to_pixel(x, y)
        inside = (px >= 0) & (px < img.shape[1] - 1) & (py >= 0) & (py < img.shape[0] - 1)
        c = COLOURS[i % len(COLOURS)]
        d.line(list(zip(px, py)), fill=c, width=1)
        dv = dist[np.round(py[inside]).astype(int), np.round(px[inside]).astype(int)]
        if dv.size == 0:
            print(f"{label or path}: no point inside the crop"); bad = True; continue
        p95 = float(np.percentile(dv, 95))
        flag = "MISMATCH" if p95 > a.tol else "ok"
        bad |= p95 > a.tol
        print(f"{label or path}: {dv.size} points; distance to ink mean {dv.mean():.2f} px, 95% {p95:.2f} px "
              f"({p95 * PX_MM:.2f} mm), max {dv.max():.2f} px  {flag}")
    cal = pathlib.Path(a.calib)
    out = ROOT / (a.out or f"build/v2/overlay/{cal.parent.name}-{cal.name.removesuffix('.calib.json').removesuffix('.json')}-{a.axes}.png")
    out.parent.mkdir(parents=True, exist_ok=True)
    base.save(out)
    print(f"overlay -> {out.relative_to(ROOT) if out.is_relative_to(ROOT) else out}")
    return 1 if bad else 0


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("lines"); s.add_argument("crop"); s.add_argument("--min-len", type=int, default=0)
    s.add_argument("--dark", type=int, default=128)
    s = sub.add_parser("ticks"); s.add_argument("crop"); s.add_argument("--xaxis", type=int); s.add_argument("--yaxis", type=int)
    s.add_argument("--gap", type=int, default=2); s.add_argument("--depth", type=int, default=4)
    s.add_argument("--span", help="lo,hi: only this range of columns (x axis) or rows (y axis)")
    s.add_argument("--dark", type=int, default=140)
    s = sub.add_parser("trace"); s.add_argument("calib"); s.add_argument("--axes", default="main")
    s.add_argument("--seed", required=True); s.add_argument("--to", type=int)
    s.add_argument("--dir", choices=["right", "left"], default="right")
    s.add_argument("--mode", choices=["cols", "rows"], default="cols")
    s.add_argument("--max-jump", type=float, default=3.0); s.add_argument("--gap", type=int, default=14)
    s.add_argument("--step", type=int, default=1); s.add_argument("--smooth", type=int, default=5)
    s.add_argument("--min-len", type=int, default=0); s.add_argument("--dark", type=int, default=128)
    s.add_argument("--out", required=True)
    s = sub.add_parser("overlay"); s.add_argument("calib"); s.add_argument("curves", nargs="+")
    s.add_argument("--axes", default="main"); s.add_argument("--out"); s.add_argument("--dark", type=int, default=128)
    s.add_argument("--tol", type=float, default=3.0)
    a = p.parse_args(argv)
    return {"lines": cmd_lines, "ticks": cmd_ticks, "trace": cmd_trace, "overlay": cmd_overlay}[a.cmd](a) or 0


if __name__ == "__main__":
    sys.exit(main())
