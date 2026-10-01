#!/usr/bin/env python3
"""Chapter 4, Figure 4: the B4 thrust curve and its piecewise-linear approximation (the 1973 form, shown in the
Errata and Supplement Part; the 1994 replacement, figures/v2/supplement/ch4-fig04-1994.py, is the same drawing).

"Actual curve": the shared B4 tracing figures/v2/common/b4.csv (corrections/v2-figures.md, rule 5); nothing is
computed for it here.

"Approximation": COMPUTED from eqs. (73a)-(73c) (chapters/ch4-sec2b.tex:171-173) with the figure's lettered
parameters F_m = 13.0 N, F_s = 3.5 N, t_1 = t_m = 0.14 sec, t_2 = t_s = 0.22 sec, t_b = 1.20 sec (t_1 is t_m and
t_2 is t_s by the 1994 caption), F = 0 after burnout: the B4 engine of trajectory.py, whose thrust() is eq. (73).
The function is sampled every 2 ms with its corners exact (and the burnout drop as a vertical run), so the
overlay on the scan has points all along it; the plot is the same polyline as the five corners.
Checks: eq. (75) with the lettering gives the lettered I_t = 5.0 N-sec, and so does the area under the curve.

Writes fig04.csv (t in sec, F in N).
"""
import pathlib
import sys

import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from trajectory import B4  # noqa: E402  (eq. (73) with the Figure 4 lettering)


def approximation(eng=B4, dt=0.002):
    """(t, F) along eqs. (73a)-(73c): the corners exactly, samples between them, the drop at t_b."""
    t = np.union1d(np.arange(0.0, eng.tb, dt), [0.0, eng.t1, eng.t2, eng.tb])
    f = np.array([eng.thrust(x) for x in t])
    drop = np.linspace(eng.Fs, 0.0, 8)[1:]           # F = 0 after burnout: down the line t = t_b
    return np.r_[t, np.full(drop.size, eng.tb)], np.r_[f, drop]


def check(eng=B4):
    it75 = eng.Fm * eng.t2 / 2 + eng.Fs * (eng.tb - eng.t1 / 2 - eng.t2 / 2)        # eq. (75)
    t, f = approximation(eng)
    area = float(np.sum((t[1:] - t[:-1]) * (f[1:] + f[:-1]) / 2))
    assert abs(it75 - 5.0) < 1e-9 and abs(area - 5.0) < 1e-9, (it75, area)
    return it75, area


def write(path):
    t, f = approximation()
    with open(path, "w") as fh:
        fh.write("t,F\n")
        for a, b in zip(t, f):
            fh.write(f"{a:.4f},{b:.4f}\n")
    it75, area = check()
    print(f"{pathlib.Path(path).name}: {t.size} points; eq. (75) I_t = {it75:.3f} N-sec, area {area:.3f} N-sec "
          f"(lettered 5.0)")


if __name__ == "__main__":
    write(HERE / "fig04.csv")
