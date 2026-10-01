#!/usr/bin/env python3
"""Chapter 4, Figure 5(b): percent error in y_b of the approximate methods, B14 engine (digitized).

Digitized from the 1973 art, figures/ch4/fig05b.png, by the method of fig05a.py (whose helpers this script
imports; the book gives neither the B14 thrust curve nor its propellant mass, so the interval solution
(83)-(87) against eqs. (20), (21) and (27), (28) cannot be rerun). Calibration fig05b.calib.json: piecewise
linear between the drawn ticks; the hand-drawn y axis leans about 6 px (column 75.5 at the top, 69.5 at the
bottom), so the x scale is taken from the bottom ticks only.

As printed, the Fehskens-Malewicki curves for k_min and k_max are one line (one heavy solid, about 3-4 px,
no separation anywhere; both k labels lead to it near m_o = .022): it is traced once and written for both.
The Caporaso-Bengen k_min curve runs flat at about 6.1% and runs into that line between m_o = .045 and
.048; from .048 (col 175) on the three are one bundle, whose centre is written for all three. The Caporaso-Bengen k_max curve
dips just below the zero line (about -0.4% near .035) between .028 and .045.

Writes fig05b.csv: m0, fm_kmin, cb_kmin, fm_kmax, cb_kmax (percent).
"""
import pathlib
import sys
import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from fig05a import Scan, curve, write  # noqa: E402

GUIDE = {
    # the Fehskens-Malewicki line (both k), joined by the Caporaso-Bengen k_min dashes from about col 165
    "fm": [(77, 76), (80, 78.5), (88, 81), (100, 84), (120, 88.5), (140, 91.5), (156, 93.5), (160, 95),
           (170, 96.5), (180, 97), (200, 97.5), (240, 99), (300, 100.5), (350, 101.5), (400, 102),
           (450, 102.5), (521, 103)],
    # Caporaso-Bengen k_min, before it joins the line
    "cb_kmin": [(76, 96.5), (90, 96.5), (110, 96.5), (130, 96.5), (145, 97), (160, 97), (166, 97.5)],
    # Caporaso-Bengen k_max: 2.0 at the axis, into the zero line, the dip below it, then rising to 4.2
    "cb_kmax": [(74, 134), (78, 138.5), (82, 141), (86, 145.5), (90, 147), (96, 150), (104, 153.5),
                (112, 154.5), (120, 155.5), (126, 156), (134, 155.5), (140, 155), (150, 154),
                (160, 153), (170, 151.5), (180, 150), (188, 149), (200, 147.5), (220, 144),
                (240, 140.5), (260, 137.5), (300, 131.5), (350, 125.5), (400, 120.5), (450, 117.5),
                (500, 115), (521, 114.5)],
}

if __name__ == "__main__":
    s = Scan("fig05b")
    for r in range(s.ink.shape[0]):                    # the leaning y axis (col 75.5 at row 20, 69.5 at 280)
        s.ink[r, :int(round(76.5 - 6 * (r - 20) / 260))] = False
    s.ink[287:, :] = False                             # the x axis
    s.mask_box(147, 64, 186, 84)                       # "k_max"
    s.mask_box(78, 102, 112, 121)                      # "k_min"
    s.mask_box(290, 218, 530, 262)                     # legend
    s.ink[72:77, 86:147] = False                       # k_max leader along the top of the line
    for a, b in (((150, 81), (126, 156)),              # k_max leader to the dashed
                 ((86, 76), (84, 104)), ((90, 108), (111, 96))):        # k_min leaders
        s.mask_line(a, b)
    fm = s.follow(GUIDE["fm"], tol=2.5, wmax=7)        # the bundle (line + dashes) is one line here
    grid, y_fm = curve(s, fm, label="fm (both k)")
    pk = s.follow(GUIDE["cb_kmin"], tol=2.0, wmax=3.5)
    pk = np.r_[pk, fm[fm[:, 0] >= 175]]                # from col 175 the dashes run in the line
    _, y_cbmin = curve(s, pk, label="cb_kmin")
    pm = s.follow(GUIDE["cb_kmax"], tol=2.5, wmax=3.5)
    _, y_cbmax = curve(s, pm, label="cb_kmax")
    write("fig05b", grid, {"fm_kmin": y_fm, "cb_kmin": y_cbmin, "fm_kmax": y_fm, "cb_kmax": y_cbmax})
