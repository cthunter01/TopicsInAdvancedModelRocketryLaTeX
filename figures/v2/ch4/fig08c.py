#!/usr/bin/env python3
"""Chapter 4, Figure 8(c): percent error in y_max of the approximate methods, F100 engine (digitized).

Fehskens-Malewicki, eqs. (20), (21), and Caporaso-Bengen, eqs. (27), (28), with y_max = y_b + y_c by (67),
against the interval method (83)-(87), k_min = .00012 and k_max = .0045 kg/m (key table,
ch4-sec2b.tex:356-372). The book does not give the F100 thrust curve or propellant mass, nor the transonic drag
model behind the k_min curves below m_o = 0.17 kg (caption), so the four printed curves are digitized from the
1973 art, figures/ch4/fig08c.png, by the method of fig07a.py (whose helpers this script imports). Calibration
fig08c.calib.json: x piecewise linear between the drawn ticks (spacing 59 to 52 px), y the affine fit to the y
ticks, the x axis and the zero line (within 0.5 px).

As printed: the two dashed curves start side by side, 9.5 (upper) and 8.8 (lower); followed dash by dash, the
upper one descends gently through the zero line near .33 to -0.4 (the lower k_max leader reaches it: k_max)
and the lower one drops steeply to 0.9 near .17, then rises to 3.4 (the upper k_min leader reaches it: k_min);
they cross near .24 (bridged). From about .30 the k_max dashed lies on and then just under the zero line (read
by hand there). The k_min solid drops steeply to a corner at 2.5 near .17 and dips to 2.2 near .19; the two
solids meet near .44 and end together at 3.9.

The k_min corners. Both k_min curves end their steep drop in a sharp V corner (the transonic-drag feature the
caption names) and turn almost flat at once. A smoothing spline through a corner rounds it off, so each k_min
curve is traced in two pieces that share a hand-read corner pixel (`corner`, trace_cornered in fig07a.py), and
the CSV has a row at each corner's m_o. The corners are the intersections of straight-line fits to the ink
centres on either side, read at 12x: FM k_min (154.9, 132.4) px = (0.1686 kg, 2.46%), from the row centres of
the steep line at rows 117-128 and the column centres at cols 158-164; CB k_min (152.7, 146.8) px =
(0.1667 kg, 0.91%), from the dash centres of the steep dashes at rows 123-144 and of the flat dashes at cols
153-162 (the corner falls in a gap between dashes).

Overlay of the written curves on the crop (tools/v2/digitize.py overlay): 95% of the points lie within
0 px of the ink for the solids and 2 px for the dashed curves (the gaps between dashes): all pass (3 px).

Writes fig08c.csv: m0, fm_kmin, cb_kmin, fm_kmax, cb_kmax (percent).
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from fig07a import digitize_panel  # noqa: E402

CURVES = {
    "fm_kmax": dict(guide=[(82, 24.5), (90, 29), (100, 34.5), (110, 41), (120, 46.5), (130, 52), (140, 57.5),
                           (150, 63), (160, 67.3), (170, 71.7), (180, 75.5), (190, 79), (200, 82.5), (210, 85.5),
                           (220, 88.5), (230, 90.7), (240, 93.2), (250, 95.7), (260, 97.8), (270, 99.5), (280, 101.3),
                           (300, 104.3), (320, 107), (340, 109.5), (370, 112.5), (400, 114.5), (430, 116),
                           (450, 117.3), (460, 118)],
                    exclude=[(0, 81), (440, 465)], extra=[(443, 117.2), (449, 117.8), (455, 118.0), (461, 118.0)]),
    "fm_kmin": dict(guide=[(82, 49), (90, 53.3), (100, 61.8), (110, 71.7), (120, 84.5), (130, 98.2), (140, 112),
                           (145, 118.5), (150, 126.3), (158, 133.3), (165, 134.5), (180, 135.5),
                           (200, 133.3), (220, 131.5), (240, 130.5), (260, 129), (280, 127.5), (300, 126.2),
                           (320, 125), (340, 123.5), (370, 122.5), (400, 120.5), (430, 119.5), (450, 118.7),
                           (460, 118)],
                    exclude=[(0, 81), (440, 465)], extra=[(443, 118.6), (449, 118.2), (455, 118.0), (461, 118.0)],
                    corner=(154.9, 132.4)),
    "cb_kmin": dict(guide=[(85, 74.3), (94, 78.5), (101.5, 83.8), (108.5, 89.8), (115.5, 96.5), (121, 104.2),
                           (127, 111), (133, 117.5), (138.5, 124.5), (144, 133), (149.5, 142.5), (155, 146.8),
                           (160, 147.3), (170, 147), (180, 146.5), (190, 145.5), (200, 145), (220, 143.2),
                           (240, 141.3), (250, 138.8), (260, 138), (270, 137), (280, 136.5), (300, 134.3),
                           (320, 132.6), (350, 130), (370, 128.5), (400, 126), (430, 124.5), (450, 123.5),
                           (460, 122.7)],
                    exclude=[(0, 82), (119, 123), (225, 247)], thr=0.35, win=(2.5, 1.5), corner=(152.7, 146.8)),
    "cb_kmax": dict(guide=[(85, 66.8), (92, 72.3), (99.5, 77.3), (108.5, 85), (119.5, 92.3), (128.7, 96.5),
                           (139.5, 104), (149.5, 109.5), (157.5, 114), (170, 119.5), (180, 123.5), (190, 127.5),
                           (200, 132.3), (210, 135.5), (220, 138), (230, 140.3), (240, 141.7), (250, 144.8),
                           (260, 146), (270, 147.5), (280, 148.5), (290, 150.5), (300, 152), (320, 154), (340, 155.5),
                           (370, 156.2), (400, 157), (430, 157.7), (450, 157.7), (460, 157.7)],
                    exclude=[(0, 82), (165, 169), (225, 247), (303, 470)], thr=0.35, win=(2.5, 1.5),
                    extra=[(308, 152), (326, 154), (344, 155), (362, 156), (380, 157), (398, 157.8), (416, 158),
                           (434, 158), (452, 158), (460, 158)]),
}

if __name__ == "__main__":
    digitize_panel("fig08c", CURVES, step=0.001)
