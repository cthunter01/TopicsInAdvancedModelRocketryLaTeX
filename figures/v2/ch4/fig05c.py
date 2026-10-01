#!/usr/bin/env python3
"""Chapter 4, Figure 5(c): percent error in y_max of the approximate methods, B14 engine (digitized).

Digitized from the 1973 art, figures/ch4/fig05c.png, by the method of fig05a.py (whose helpers this script
imports; the book gives neither the B14 thrust curve nor its propellant mass, so the interval solution
(83)-(87) with the coast of eq. (67) against eqs. (20), (21) and (27), (28) cannot be rerun). Calibration
fig05c.calib.json: piecewise linear between the drawn ticks (the x ticks close up from 39 px per 0.01 kg at
the left to 34 px at the right, so a single scale would misplace the curves by up to 8 px); the hand-drawn y
axis leans about 4 px the other way (column 70.5 at the top, 74.5 at the bottom), so the two k_max curves
meet it 2-4 px left of the .02 tick (column 75): that ink maps to m_o of about .0195 by the x scale
continued past the tick, and the value at .02 is the ink's at the tick. The k_max curves bend sharply there
(the Caporaso-Bengen dashes drop 5.5 px over the 2 px between the first dash, at the axis, and the next), so
the first two samples of each curve are weighted 30 in the smoothing spline (curve(w0=...)); unweighted, its
natural end cuts the bend and the Caporaso-Bengen k_max curve starts at 5.73, 0.3 point low.

As printed: the Fehskens-Malewicki k_min curve falls from +1% at the axis into the thin zero line near
m_o = .045 and ends just below it (about -0.4%), where the Caporaso-Bengen k_min curve (-1.2% at the axis,
-0.5% at the right) runs into it; the Caporaso-Bengen k_max curve (6.1% at the .02 tick, 6.0 in the CSV;
6.2% where it meets the leaning axis) crosses that curve near .048 (-1%) and levels out at about -2%. The
Fehskens-Malewicki k_max curve is at 10.8% at the .02 tick (10.7 in the CSV; 10.9% at the leaning axis).
The printed curves end about 3 px short of the .14 tick; they are run on to it.

Writes fig05c.csv: m0, fm_kmin, cb_kmin, fm_kmax, cb_kmax (percent).
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from fig05a import COLS, Scan, curve, write  # noqa: E402

GUIDE = {
    "fm_kmax": [(73, 51.5), (80, 57), (90, 65.5), (100, 73), (120, 86), (140, 97), (150, 101.5), (160, 105),
                (180, 111), (200, 116), (220, 121), (250, 126.5), (300, 131), (350, 135.5), (400, 139),
                (450, 141.5), (507, 143.5)],
    "cb_kmax": [(74, 97), (80, 106), (90, 113), (100, 120.5), (110, 127), (120, 133), (130, 138.5),
                (140, 144), (150, 148.5), (160, 153), (170, 157), (180, 160), (190, 162), (200, 163.5),
                (220, 165.5), (250, 168.5), (300, 170.5), (330, 171.5), (350, 170.5), (400, 169.5),
                (450, 169.5), (507, 169.5)],
    # into the zero line (row 151.5) near col 170, then along its lower edge
    "fm_kmin": [(74, 144), (80, 145.5), (92, 147.5), (104, 148.5), (116, 150), (140, 150.5), (170, 152),
                (200, 152.5), (250, 153), (300, 153), (350, 153.5), (400, 154.5), (450, 154.5),
                (507, 154.5)],
    "cb_kmin": [(74, 162.5), (100, 162.5), (120, 162), (140, 161), (160, 160.5), (180, 159.5), (200, 158.5),
                (250, 158), (300, 156.5), (350, 156.5), (400, 155.5), (450, 155.5), (507, 155.5)],
}

if __name__ == "__main__":
    s = Scan("fig05c")
    for r in range(s.ink.shape[0]):                    # the leaning y axis (col 70.5 at row 20, 74.5 at 280)
        s.ink[r, :int(round(72.5 + 4 * (r - 20) / 260))] = False
    s.ink[285:, :] = False                             # the x axis
    s.mask_box(138, 117, 180, 134)                     # "k_max"
    s.mask_box(76, 182, 115, 199)                      # "k_min"
    s.mask_box(290, 218, 530, 262)                     # legend
    for a, b in (((149, 120), (155, 105)), ((138, 130), (129, 140)),     # k_max leaders
                 ((89, 148), (85, 181)), ((100, 163), (91, 181))):      # k_min leaders
        s.mask_line(a, b)
    out = {}
    for c in COLS:
        pts = s.follow(GUIDE[c], tol=2.5, wmax=3.5)
        grid, out[c] = curve(s, pts, w0=(2, 30), label=c)
    write("fig05c", grid, out)
