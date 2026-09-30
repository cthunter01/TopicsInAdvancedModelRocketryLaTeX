#!/usr/bin/env python3
"""The B14 and E62 thrust-time curves of Chapter 1 Figure 5(b), (c), digitized from figures/ch1/fig05.png
(calibration engines.calib.json, every labelled tick). Each curve is traced both ways from a seed on it with
tools/v2/digitize.py, joined, cut where it returns to the axis after its peak, and started at (0, 0).
Writes b14.csv and e62.csv (t in sec, F in N).
"""
import csv, pathlib, subprocess, sys, tempfile

HERE = pathlib.Path(__file__).parent
ROOT = HERE.parent.parent.parent
TOOL = ROOT / "tools" / "v2" / "digitize.py"
CAL = HERE / "engines.calib.json"
# axes: seed pixel on the curve, max jump (px per column), mask lines at least this long (the axes only)
CURVES = {"b14": ("255,408", 5, 150), "e62": ("251,643", 7, 200)}


def trace(axes, seed, jump, minlen, direction, out):
    subprocess.run([sys.executable, str(TOOL), "trace", str(CAL), "--axes", axes, "--seed", seed, "--dir", direction,
                    "--max-jump", str(jump), "--min-len", str(minlen), "--smooth", "3", "--out", str(out)],
                   check=True, capture_output=True)
    with open(out) as f:
        return [(float(r["x"]), float(r["y"])) for r in csv.DictReader(f)]


with tempfile.TemporaryDirectory() as tmp:
    for name, (seed, jump, minlen) in CURVES.items():
        pts = sorted(set(trace(name, seed, jump, minlen, "left", pathlib.Path(tmp) / "l.csv")
                         + trace(name, seed, jump, minlen, "right", pathlib.Path(tmp) / "r.csv")))
        peak = max(range(len(pts)), key=lambda i: pts[i][1])
        end = next((i for i in range(peak, len(pts)) if pts[i][1] < 0.02 * pts[peak][1]), len(pts) - 1)
        pts = [(0.0, 0.0)] + [p for p in pts[:end] if p[0] > 0] + [(pts[end][0], 0.0)]
        (HERE / f"{name}.csv").write_text("t,F\n" + "\n".join(f"{t:.4f},{F:.3f}" for t, F in pts) + "\n")
        area = sum((t2 - t1) * (f1 + f2) / 2 for (t1, f1), (t2, f2) in zip(pts, pts[1:]))
        print(f"{name}.csv: {len(pts)} points; peak {pts[peak][1]:.1f} N at {pts[peak][0]:.3f} sec; "
              f"burnout {pts[-1][0]:.3f} sec; area {area:.2f} N-sec")
