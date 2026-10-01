#!/usr/bin/env python3
"""Chapter 4, Figure 7(b): percent error in y_b of the approximate methods, D4 engine (digitized).

Fehskens-Malewicki, eqs. (20), (21), and Caporaso-Bengen, eqs. (27), (28), against the interval method
(83)-(87), k_min = .00007 and k_max = .0027 kg/m (key table, ch4-sec2b.tex:356-372). The book does not give
the D4 thrust curve or propellant mass, so the four printed curves are digitized from the 1973 art,
figures/ch4/fig07b.png, by the method of fig07a.py (whose helpers this script imports). Calibration
fig07b.calib.json: x piecewise linear between the drawn ticks (spacing 49.5 to 44 px), y the affine fit to the
y ticks, the x axis and the zero line (within 0.7 px).

As printed: the k_max solid crosses the zero line near .04; the two dashed curves cross near .09 (excluded
there and bridged); several dashes between .045 and .07 are printed light (read at darkness 0.35).

Overlay of the written curves on the crop (tools/v2/digitize.py overlay): 95% of the points lie within
0 px of the ink for the solids and 2 px for the dashed curves (the gaps between dashes): all pass (3 px).

Writes fig07b.csv: m0, fm_kmin, cb_kmin, fm_kmax, cb_kmax (percent).
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from fig07a import digitize_panel  # noqa: E402

CURVES = {
    # solid, from 0.6 through the zero line near .04 to -5.8
    "fm_kmax": dict(guide=[(83, 148), (130, 156), (200, 165), (300, 177), (400, 193), (510, 209)],
                    exclude=[(0, 81), (100, 150)]),
    # dashed, from -1.8 to -12.0, crossing the k_min dashed near .09
    "cb_kmax": dict(guide=[(83, 172), (130, 186), (143, 190), (160, 195), (180, 200), (220, 211), (240, 216.5),
                           (300, 229), (400, 250), (510, 265)],
                    exclude=[(0, 81), (340, 378)], thr=0.35),
    # solid, from -0.5 to -9.8
    "fm_kmin": dict(guide=[(83, 160), (130, 177), (200, 199), (250, 209), (310, 218), (400, 232), (510, 247)],
                    exclude=[(0, 81)]),
    # dashed, from -7.3 to -10.6
    "cb_kmin": dict(guide=[(83, 222), (130, 228), (200, 233), (300, 238), (400, 244), (510, 252)],
                    exclude=[(0, 81), (340, 378)], thr=0.35),
}

if __name__ == "__main__":
    digitize_panel("fig07b", CURVES, step=0.00025)
