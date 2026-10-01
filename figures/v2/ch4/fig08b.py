#!/usr/bin/env python3
"""Chapter 4, Figure 8(b): percent error in y_b of the approximate methods, F100 engine (digitized).

Fehskens-Malewicki, eqs. (20), (21), and Caporaso-Bengen, eqs. (27), (28), against the interval method
(83)-(87), k_min = .00012 and k_max = .0045 kg/m (key table, ch4-sec2b.tex:356-372). The book does not give
the F100 thrust curve or propellant mass, nor the transonic drag model behind the k_min curves below
m_o = 0.17 kg (caption), so the four printed curves are digitized from the 1973 art, figures/ch4/fig08b.png,
by the method of fig07a.py (whose helpers this script imports). Calibration fig08b.calib.json: x piecewise
linear between the drawn ticks (spacing 58 to 51.5 px), y the affine fit to the y ticks, the x axis and the
zero line (within 0.9 px).

As printed: the two Fehskens-Malewicki solids run nearly straight from 14.4 (k_min) and 12.2 (k_max) to one
point near .163, 10.3; the drawing breaks them there for the k_min leader and resumes them as one line at
.171, 10.0 (bridged straight). The line splits into two strands from about .21 to .32, up to 0.4% apart at
.26-.27 (the upper is taken as k_min, the order on the left), and is one line again from about .33 to the end,
7.6 at .443. The k_min dashed runs about 1% under them and joins the lower strand near .25; from about .33 the
three are one band, whose centre is written for all three. The k_max dashed dips to 2.0 near .22 and rises to
3.9.

Overlay of the written curves on the crop (tools/v2/digitize.py overlay): 95% of the points lie within
0 px of the ink for the solids and 2 px for the dashed curves (the gaps between dashes): all pass (3 px).

Writes fig08b.csv: m0, fm_kmin, cb_kmin, fm_kmax, cb_kmax (percent).
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from fig07a import digitize_panel  # noqa: E402

BAND = [(350, 78.3), (380, 79.9), (400, 80.6), (430, 81.7), (450, 82.6), (455, 82.6)]   # the merged band
CURVES = {
    "fm_kmin": dict(guide=[(83, 22), (90, 26.3), (100, 32.3), (115, 41.2), (130, 49), (140, 54.5), (146, 56.8),
                           (149, 58.6), (158, 60.8), (165, 62.3), (175, 63.8), (186, 65.2), (198, 65.8), (210, 67.2),
                           (222, 68.2), (240, 69.5), (260, 71), (280, 72.6), (300, 73.8), (320, 75), (330, 75.8)] + BAND,
                    exclude=[(0, 81), (108, 112), (149, 157)], win=(3, 1.2)),
    "fm_kmax": dict(guide=[(83, 41.8), (90, 44), (100, 47.5), (110, 50.5), (120, 53.7), (130, 56.2), (140, 58.5),
                           (146, 59.8), (149, 59.5), (158, 61), (165, 62.4), (175, 64), (186, 65.8), (198, 68),
                           (210, 69.7), (222, 70.7), (240, 73), (260, 75), (280, 75.7), (300, 76.7), (320, 77.8),
                           (330, 78.3)] + BAND,
                    exclude=[(0, 81), (124, 128), (147, 157)], win=(3, 1.2)),
    "cb_kmin": dict(guide=[(83, 48.5), (90, 49.6), (100, 52.5), (110, 55.7), (120, 58.5), (135, 64.3), (143, 67.3),
                           (148, 68.5), (165, 71), (175, 71.5), (190, 72.3), (200, 72.8), (210, 73.2), (222, 74),
                           (231, 74.5), (240, 74), (260, 75), (280, 75.8), (300, 76.8), (320, 77.8), (330, 78.3)] + BAND,
                    exclude=[(0, 81), (150, 158)], win=(2.5, 1.2), thr=0.35),
    "cb_kmax": dict(guide=[(82, 98), (100, 106.5), (120, 116.5), (140, 124.5), (150, 127), (165, 130), (180, 131.5),
                           (200, 132.8), (220, 133), (240, 132), (260, 131), (280, 130.2), (300, 128.5), (320, 127),
                           (340, 125), (360, 123), (380, 121.5), (400, 120), (420, 118), (440, 116.3), (455, 115.5)],
                    exclude=[(0, 80)], thr=0.35),
}

if __name__ == "__main__":
    digitize_panel("fig08b", CURVES, step=0.001)
