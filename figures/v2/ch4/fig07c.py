#!/usr/bin/env python3
"""Chapter 4, Figure 7(c): percent error in y_max of the approximate methods, D4 engine (digitized).

Fehskens-Malewicki, eqs. (20), (21), and Caporaso-Bengen, eqs. (27), (28), with y_max = y_b + y_c by (67),
against the interval method (83)-(87), k_min = .00007 and k_max = .0027 kg/m (key table,
ch4-sec2b.tex:356-372). The book does not give the D4 thrust curve or propellant mass, so the four printed
curves are digitized from the 1973 art, figures/ch4/fig07c.png, by the method of fig07a.py (whose helpers this
script imports). Calibration fig07c.calib.json: x piecewise linear between the drawn ticks (even spacing), y the
affine fit to the y ticks, the x axis and the zero line (within 0.8 px). The crop is turned slightly (the x
axis and the zero line both rise about 4.5 px to the right): the fit takes the turn out, so the zero line is
level at 0.

As printed: the two solids start together at about +0.8 (one start point, read by hand, for both) and run as
one line to about .036; the k_min solid then crosses the zero line near .042, the k_max solid lies on it from
about .045 to .060 (bridged); they end at -2.3 (k_max) and -3.7 (k_min). The k_max leader stops between
the two solids; the k_min leader reaches the lower one, so the upper is k_max. The dashed curves cross near
.08 (bridged).

Overlay of the written curves on the crop (tools/v2/digitize.py overlay): 95% of the points lie within
0 px of the ink for the solids and 2 px for the dashed curves (the gaps between dashes): all pass (3 px).

Writes fig07c.csv: m0, fm_kmin, cb_kmin, fm_kmax, cb_kmax (percent).
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from fig07a import digitize_panel  # noqa: E402

CURVES = {
    # upper solid
    "fm_kmax": dict(guide=[(82, 145.5), (110, 148), (130, 149.5), (140, 150.5), (180, 153), (215, 155.5),
                           (240, 156.5), (300, 159.5), (400, 164.5), (500, 169.5), (518, 170.5)],
                    exclude=[(0, 83), (92, 128), (144, 212)], extra=[(82, 145.5)]),
    # dashed, from -1.4 to -9.3
    "cb_kmax": dict(guide=[(82, 165.5), (100, 170), (150, 181.5), (200, 190.5), (260, 201.5), (300, 207),
                           (350, 214), (450, 226), (518, 232)],
                    exclude=[(0, 80), (280, 320)], thr=0.35),
    # lower solid
    "fm_kmin": dict(guide=[(82, 145.5), (100, 147.5), (120, 151), (140, 153.5), (160, 155.5), (200, 158.5),
                           (215, 160), (240, 161.5), (300, 165.5), (400, 173), (500, 181), (518, 182.5)],
                    exclude=[(0, 83), (92, 155)], extra=[(82, 145.5)]),
    # dashed, from -5.3 down to -6.3 near .05 and back to -6.0
    "cb_kmin": dict(guide=[(82, 200), (100, 204), (150, 209.5), (200, 210), (260, 209), (300, 207), (350, 205.5),
                           (450, 202.5), (518, 202.5)],
                    exclude=[(0, 80), (280, 320)], thr=0.35),
}

if __name__ == "__main__":
    digitize_panel("fig07c", CURVES, step=0.00025)
