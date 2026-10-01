#!/usr/bin/env python3
"""Chapter 4, Figure 8(a): percent error in v_b of the approximate methods, F100 engine (digitized).

Fehskens-Malewicki, eqs. (20), (21), and Caporaso-Bengen, eqs. (27), (28), against the interval method
(83)-(87), k_min = .00012 and k_max = .0045 kg/m (key table, ch4-sec2b.tex:356-372). The book does not give
the F100 thrust curve or propellant mass, and the k_min curves include the transonic drag divergence of the
caption (m_o below 0.17 kg), which the chapter does not model (its k is constant), so the four printed curves
are digitized from the 1973 art, figures/ch4/fig08a.png, by the method of fig07a.py (whose helpers this script
imports). Calibration fig08a.calib.json: x piecewise linear between the drawn ticks, y the affine fit to the
y ticks, the x axis and the zero line (within 0.8 px).

As printed: the two k_max curves come in through the top of the frame (cut at 15%); the k_min curves drop
steeply near .16-.17 (the kink of the caption); the k_min dashed touches the zero line at its minimum (about
+0.3 near .175: read by hand there) and the k_max dashed crosses it near .26; the last dashes of the k_min
dashed touch the k_min solid (read by hand there).

Overlay of the written curves on the crop (tools/v2/digitize.py overlay): 95% of the points lie within
0 px of the ink for the solids and 2 px for the dashed curves (the gaps between dashes): all pass (3 px).

Writes fig08a.csv: m0, fm_kmin, cb_kmin, fm_kmax, cb_kmax (percent).
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from fig07a import digitize_panel  # noqa: E402

CURVES = {
    # solid, from the top of the frame near .205 to 4.2
    "fm_kmax": dict(guide=[(190, 16.5), (200, 25), (210, 34), (220, 42), (230, 50), (240, 57), (250, 63.5),
                           (260, 69), (270, 74), (280, 78.5), (300, 86), (350, 99.3), (400, 107.3), (450, 112.5),
                           (470, 114.3)],
                    top=15),
    # dashed, from the top of the frame near .17 through the zero line near .26 to -2.0
    "cb_kmax": dict(guide=[(150.5, 17.5), (160, 38), (170, 58), (180, 79), (190, 94), (200, 107), (210, 118),
                           (220, 127), (232, 137), (240, 141), (250, 145.5), (260, 151), (270, 155), (280, 158.5),
                           (300, 163.5), (350, 170.5), (400, 172), (450, 171), (470, 170)],
                    exclude=[(232, 250), (256, 278)], thr=0.35, top=15),
    # solid, from 8.3 down to 5.6 near .155, the steep drop to 2.2 by .18, then 2.2-2.4
    "fm_kmin": dict(guide=[(87, 78), (100, 86), (110, 92), (120, 98.5), (130, 104), (135, 109), (139, 117),
                           (143, 123.5), (147, 128.5), (152, 131), (160, 133), (170, 134.5), (200, 134.5),
                           (300, 134), (350, 133.5), (400, 132.8), (450, 132.5), (470, 133)],
                    exclude=[(0, 85)]),
    # dashed, from 3.4 down to the zero line near .175, then up to 2.0 under the k_min solid
    "cb_kmin": dict(guide=[(85, 124), (100, 124.5), (110, 125.5), (120, 126.5), (128, 130), (135, 137), (140, 143),
                           (147, 149), (153, 152), (158, 152.5), (165, 151.5), (175, 150), (185, 149), (200, 147.5),
                           (220, 145.5), (240, 143.3), (260, 142), (280, 140.5), (300, 140), (350, 138), (380, 137),
                           (400, 136.5), (420, 136), (440, 135.7), (460, 135.3), (470, 135)],
                    exclude=[(0, 82), (150, 160), (232, 250), (453, 475)],
                    extra=[(155, 152.0), (458, 135.2), (464, 135.0), (470, 134.6)], thr=0.35, win=(2.5, 1.5)),
}

if __name__ == "__main__":
    digitize_panel("fig08a", CURVES, step=0.001)
