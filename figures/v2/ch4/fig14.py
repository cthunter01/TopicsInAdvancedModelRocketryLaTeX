#!/usr/bin/env python3
"""Chapter 4, Figure 14: non-vertical trajectories for a 30 deg launch angle, F7 engine (scan:
figures/ch4/fig14.png). The three printed curves (a)-(c), DIGITIZED from the 1973 art.

Why digitized: the book gives no F7 engine model (only t_b = 9.00 s, "low thrust" and the engine-alone mass .110 kg,
ch4-sec3.tex; no I_t, F_m, F_s, t_m, t_s or propellant mass), so eqs. (106)-(115) with (125)-(131) cannot be run
(corrections/v2-figures.md). The caption's burnout points (1050/1079, 696/311 m) are not drawn and not used; curve
(c) strikes the ground under power (caption: 6.84 s).
Method: fig10.py (calibration fig14.calib.json with the family's frame convention: x between the unevenly spaced
x ticks along the drawn y axis, which leans 0.17 deg against the x axis). Curve (c) is only about 9 px high, so
its descent is followed to 3 px above the axis; its tag is placed in fig14.tex, beside the 3.80 label, as printed.
Writes fig14-a/b/c.csv and fig14-marks.csv.
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import fig10  # noqa: E402

SPEC = dict(
    name="fig14",
    seeds={"a": (560, 115, (0.2, 1), (-0.2, -1)),
           "b": (400, 283, (0.6, 1), (-0.6, -1)),
           "c": (140, 324.5, (1, 0.6), (-1, -0.4))},
    erase=[(469, 15, 464.5, 43),          # 15.20, below the apex of (a)
           (308, 251, 318, 236),          # 10.40
           (127, 318, 155, 303),          # 3.80
           (153, 327, 190, 319),          # 6.84
           (439, 325, 453, 293),          # 20.01
           (543, 304, 575, 326.5)],       # 41.03, from the left
    disks=[],
    margin={"c": 3.0},
    tags={"a": 1047.7, "b": 230.0},
    scale=4.2 / 2200,
)

if __name__ == "__main__":
    fig10.main(SPEC)
