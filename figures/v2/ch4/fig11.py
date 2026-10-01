#!/usr/bin/env python3
"""Chapter 4, Figure 11: non-vertical trajectories for a 30 deg launch angle, B4 engine (scan:
figures/ch4/fig11.png). COMPUTED by the book's own 2-D method (owner decision 2026-10-01: the computed apex and
impact times are the ones marked on the curves; corrections/v2-figures.md).

  launch rod   eqs. (125)-(131), the method of drag from prior velocity with the trajectory angle held at
               theta_o = 30 deg, for the first metre of travel ("the first meter or so", ch4-sec3.tex); while the
               thrust is below m g cos(theta_o) the model stays on the pad
  free flight  eqs. (106)-(115), thrust along the velocity, drag k v^2 against it, from the prior velocity
  coast        the same equations with F = 0 and the burnout mass, continued to ground impact (no recovery)
  dt           .001 s, as the book recommends for this method
  engine       B4 from trajectory.py (the Figure 4 lettering: I_t 5.0 N-sec, F_m 13.0 N at t_m 0.14 sec, F_s 3.5 N
               from t_s 0.22 sec, t_b 1.20 sec; thrust eqs. (73a)-(73c)); propellant 8.33 g (Table 1); the mass by
               eq. (74) with c = I_t/m_f, so the model loses the propellant in proportion to the impulse delivered;
               g = 9.8 m/sec^2
  cases        the caption's: (a) m_o = .021 kg, k = .00005 kg/m; (b) .050, .00012; (c) .100, .002
Thrust and mass are taken at the start of each interval. The apex is where the vertical velocity changes sign and
the impact where y returns to 0, each interpolated within its interval.

The computed burnout points agree with the caption's x_b, y_b (82/131, 35/51, 15/19 m), and curve (c) with the
1973 art; after burnout curves (a) and (b) do not (computed apex times 7.07 and 6.02 s, impact 19.16 and 13.06 s,
against the printed 5.60/16.70 and 6.20/14.30): see corrections/v2-figures.md.
Writes fig11-a.csv, fig11-b.csv, fig11-c.csv (x, y, t every .01 s, with the burnout, apex and impact points; x and
y first, so that tools/v2/digitize.py overlay reads them as they are) and fig11-marks.csv (curve, burnout x and y,
apex x, y and t, impact x and t).
"""
import csv
import math
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from trajectory import B4, G  # noqa: E402

THETA_O = 30.0       # deg from the vertical
ROD = 1.0            # m of travel along the launch rod
DT = 0.001
CASES = {"a": (0.021, 0.00005), "b": (0.050, 0.00012), "c": (0.100, 0.002)}
CAPTION_BURNOUT = {"a": (82, 131), "b": (35, 51), "c": (15, 19)}
PRINTED_TIMES = {"a": (5.60, 16.70), "b": (6.20, 14.30), "c": (2.80, 5.70)}


def mass(t, m0, e=B4):
    """Eq. (74), with c = I_t/m_f; after burnout the burnout mass."""
    c = e.It / e.mp
    fm, fs, tm, ts, tb = e.Fm, e.Fs, e.t1, e.t2, e.tb
    if t <= tm:
        return m0 - fm * t * t / (2 * c * tm)                                           # (74a)
    if t <= ts:
        return m0 - fm / c * (t - tm / 2) + (fm - fs) * (t - tm) ** 2 / (2 * c * (ts - tm))   # (74b)
    if t <= tb:
        return m0 - fm * ts / (2 * c) - fs * (ts - tm) / (2 * c) - fs / c * (t - ts)    # (74c)
    return m0 - fm * ts / (2 * c) - fs * (ts - tm) / (2 * c) - fs / c * (tb - ts)


def thrust(t, e=B4):
    return e.thrust(t) if t < e.tb - 1e-9 else 0.0


def fly(m0, k, e=B4):
    th = math.radians(THETA_O)
    n, x, y, v = 0, 0.0, 0.0, 0.0
    rows = [(0.0, 0.0, 0.0)]
    # launch rod: eqs. (125)-(131)
    while math.hypot(x, y) < ROD:
        t = n * DT
        f, m = thrust(t), mass(t, m0, e)
        dv = DT * (f - m * G * math.cos(th) - k * v * v) / m                            # (125)
        if v + dv <= 0:                                                                 # still on the pad
            dv, v = 0.0, 0.0
        y += DT * (v + dv / 2) * math.cos(th)                                           # (126), (129)
        x += DT * (v + dv / 2) * math.sin(th)                                           # (127), (130)
        v += dv                                                                         # (128)
        n += 1                                                                          # (131)
        rows.append((n * DT, x, y))
    xd, yd = v * math.sin(th), v * math.cos(th)
    burn = apex = None
    while True:
        t = n * DT
        f, m = thrust(t), mass(t, m0, e)
        ddy = DT * (f * yd / v - m * G - k * v * yd) / m                                 # (106)
        ddx = DT * (f * xd / v - k * v * xd) / m                                         # (107)
        dy = DT * (yd + ddy / 2)                                                        # (108)
        dx = DT * (xd + ddx / 2)                                                        # (109)
        yd0, x0, y0 = yd, x, y
        yd += ddy                                                                       # (110)
        xd += ddx                                                                       # (111)
        v = math.hypot(xd, yd)                                                          # (112)
        y += dy                                                                         # (113)
        x += dx                                                                         # (114)
        n += 1                                                                          # (115)
        t = n * DT
        if burn is None and n == round(e.tb / DT):
            burn = (t, x, y)
        if apex is None and yd0 > 0 >= yd:
            s = yd0 / (yd0 - yd)
            apex = (t - DT + s * DT, x0 + s * dx, y0 + s * dy)
        if y < 0:
            s = y0 / (y0 - y)
            impact = (t - DT + s * DT, x0 + s * dx, 0.0)
            break
        rows.append((t, x, y))
    return rows, burn, apex, impact


def main():
    with open(HERE / "fig11-marks.csv", "w", newline="") as fm:
        mw = csv.writer(fm)
        mw.writerow(["curve", "burnx", "burny", "apexx", "apexy", "apext", "impactx", "impactt"])
        for key, (m0, k) in CASES.items():
            rows, burn, apex, impact = fly(m0, k)
            keep = [r for i, r in enumerate(rows) if i % 10 == 0]
            keep += [burn, apex, impact]
            keep = sorted(set(keep))
            with open(HERE / f"fig11-{key}.csv", "w", newline="") as f:
                wr = csv.writer(f)
                wr.writerow(["x", "y", "t"])
                for t, x, y in keep:
                    wr.writerow([f"{x:.3f}", f"{y:.3f}", f"{t:.4f}"])
            mw.writerow([key, f"{burn[1]:.2f}", f"{burn[2]:.2f}", f"{apex[1]:.2f}", f"{apex[2]:.2f}",
                         f"{apex[0]:.2f}", f"{impact[1]:.2f}", f"{impact[0]:.2f}"])
            cb, pt = CAPTION_BURNOUT[key], PRINTED_TIMES[key]
            print(f"fig11 ({key}): burnout ({burn[1]:.1f}, {burn[2]:.1f}) m [caption {cb[0]}/{cb[1]}]; "
                  f"apex ({apex[1]:.1f}, {apex[2]:.1f}) m at {apex[0]:.2f} s [printed {pt[0]:.2f}]; "
                  f"impact {impact[1]:.1f} m at {impact[0]:.2f} s [printed {pt[1]:.2f}]")


if __name__ == "__main__":
    main()
