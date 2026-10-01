#!/usr/bin/env python3
"""Chapter 4, Figure 13: non-vertical trajectories for a 30 deg launch angle, F100 engine (scan:
figures/ch4/fig13.png). The three printed curves (a)-(c), DIGITIZED from the 1973 art.

Why digitized: the book gives no F100 engine model (only t_b = 0.50 s, the engine-alone mass .110 kg and the
0.453 kg maximum, ch4-sec3.tex; no I_t, F_m, F_s, t_m, t_s or propellant mass, nor whether transonic drag was
modelled for (a)), so eqs. (106)-(115) with (125)-(131) cannot be run (corrections/v2-figures.md). The caption's
burnout points (61/103, 28/47, 13/21 m) are not drawn and not used.
Method: fig10.py (calibration fig13.calib.json with the family's frame convention: x between the unevenly spaced
x ticks along the drawn y axis, which leans 0.79 deg against the x axis). The (c) tag, close to the descending
branch of (c), is erased too. Writes fig13-a/b/c.csv and fig13-marks.csv.
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import fig10  # noqa: E402

SPEC = dict(
    name="fig13",
    seeds={"a": (420, 142, (0.4, 1), (-0.4, -1)),
           "b": (370, 211, (0.5, 1), (-0.5, -1)),
           "c": (148, 290, (0.3, 1), (-0.3, -1))},
    erase=[(335.8, 14.8, 330.5, 40),      # 9.40, below the apex of (a)
           (287.3, 108.4, 283, 128),      # 9.00, below the apex of (b)
           (142.5, 275, 174, 257),        # 3.80
           (159, 312, 180, 301.5),        # 9.40, at the impact of (c)
           (365, 301, 389, 313),          # 21.84, from the left
           (444, 312, 472, 286)],         # 26.47
    disks=[(162.5, 285.5, 10.5)],         # the (c) tag
    margin={},
    tags={"a": 680.5, "b": 440.0, "c": 61.1},
    scale=0.0035,
)

if __name__ == "__main__":
    fig10.main(SPEC)
