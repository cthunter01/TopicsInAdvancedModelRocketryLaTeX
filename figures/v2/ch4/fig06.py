#!/usr/bin/env python3
"""Chapter 4, Figure 6(a)-(c): percent error of the approximate methods for the B4 engine, against liftoff
mass, for k_min = 0.00005 and k_max = 0.002 (the key table after Figure 5). Error = 100 (approx - exact)/exact,
exact = the interval method; see trajectory.py. The book computed twenty liftoff masses per engine without
listing them; the curves here start at 21 g (the engine alone, where the printed curves start) and are sampled
every 2 g from 22 g to 100 g.
Writes fig06a.csv (v_b), fig06b.csv (y_b), fig06c.csv (y_max): m0, fm_kmin, cb_kmin, fm_kmax, cb_kmax.
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from trajectory import interval, fehskens_malewicki, caporaso_bengen

KMIN, KMAX = 0.00005, 0.002
here = pathlib.Path(__file__).parent
rows = {q: [] for q in "abc"}
for m0 in [0.021] + [0.022 + 0.002 * i for i in range(40)]:
    if m0 > 0.1000001:
        break
    cols = {q: [f"{m0:.3f}"] for q in "abc"}
    for k in (KMIN, KMAX):
        vb, yb, ymax, _ = interval(m0, k)
        exact = (vb, yb, ymax)
        for approx in (fehskens_malewicki(m0, k), caporaso_bengen(m0, k)):
            for q, a, e in zip("abc", approx, exact):
                cols[q].append(f"{100 * (a - e) / e:.3f}")
    for q in "abc":
        rows[q].append(",".join(cols[q]))
for q in "abc":
    (here / f"fig06{q}.csv").write_text("m0,fm_kmin,cb_kmin,fm_kmax,cb_kmax\n" + "\n".join(rows[q]) + "\n")
print(f"fig06a/b/c.csv: {len(rows['a'])} liftoff masses")
