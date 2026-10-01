#!/usr/bin/env python3
"""Chapter 4, Figure 12: non-vertical trajectories for a 30 deg launch angle, D4 engine (scan:
figures/ch4/fig12.png). The three printed curves (a)-(c), DIGITIZED from the 1973 art.

Why digitized: the book gives no D4 engine model (only t_b = 2.90 s and the engine-alone mass .032 kg, ch4-sec3.tex;
no I_t, F_m, F_s, t_m, t_s or propellant mass), so eqs. (106)-(115) with (125)-(131) cannot be run
(corrections/v2-figures.md). The caption's burnout points (236/342, 133/160, 57/38 m) are not drawn and not used.
Method: fig10.py (calibration fig12.calib.json with the family's frame convention: x between the x ticks along the
drawn y axis, which leans 0.83 deg against the x axis; leaders erased, curves followed from their descending
branches). The (c) tag, which crowds the descending branch of (c), is erased too. Writes fig12-a/b/c.csv and
fig12-marks.csv.
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import fig10  # noqa: E402

SPEC = dict(
    name="fig12",
    seeds={"a": (362, 150, (0, 1), (0, -1)),
           "b": (330, 231, (0.6, 1), (-0.6, -1)),
           "c": (143, 308, (0.3, 1), (-0.3, -1))},
    erase=[(342.5, 35.5, 360, 19),        # 8.20
           (267.5, 178.5, 279, 158),      # 7.60
           (135.5, 300, 158, 283),        # 3.50
           (153, 317.5, 190, 300),        # 7.07
           (325, 306, 354, 318),          # 16.86, from the left to the impact of (b)
           (368, 317.5, 420, 291)],       # 24.48
    disks=[(156, 302.5, 11.5)],           # the (c) tag
    margin={},
    tags={"a": 489.7, "b": 280.0, "c": 25.8},
    scale=0.00525,
)

if __name__ == "__main__":
    fig10.main(SPEC)
