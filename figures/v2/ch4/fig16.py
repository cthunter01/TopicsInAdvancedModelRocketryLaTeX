#!/usr/bin/env python3
"""Chapter 4, Figure 16: a Malewicki chart, the maximum altitude y_max of vertical flight against the liftoff mass
m_o for B4-powered models with k = .00005, .0001, .0002, .0004, .0008 and .0016 kg/m (lettered on the curves;
caption chapters/ch4-sec5.tex:162-169), the line of Bengen's maxima and the line of the engine's own mass.

COMPUTED with the closed-form method the chapter gives for such charts (Section 5.1, ch4-sec5.tex:70-77: "the
methods of Section 2 ... closed-form, algebraic solutions"; the charts carry Malewicki's name): the
Fehskens-Malewicki burnout velocity and altitude, eqs. (20) and (21) (ch4-sec2a.tex:55-64), with the mean of the
liftoff and burnout masses and the average thrust F = I_t/t_b (Section 2.1's assumptions), plus the coast to the
apex by eq. (67) at the burnout mass: trajectory.fehskens_malewicki. B4 data: the Figure 4 lettering (I_t = 5.0
N-sec, t_b = 1.20 sec) and Table 1's propellant mass 8.33 g; g = 9.8 m/sec^2. The book's numerical method,
eqs. (83)-(87) (trajectory.interval, its "exact" solution), can be selected with METHOD below; it gives the same
curves within 1-4 m, with the maxima of the high-k curves further right (k = .0016: m_o .0407 against .0378 kg).
METHOD switches the data only: the six k labels and the callout in fig16.tex are placed for the
Fehskens-Malewicki curves, and under the interval method the lower end of the Bengen line would run through the
".0016" label and along the ".0008" and ".0004" labels, so they would have to be moved (the positions for that
variant are in the fig16.tex header). Which method the edition uses is a Chapter 4 gate question.
Overlaid on the scan (digitize.py overlay with fig16.calib.json), the Fehskens-Malewicki curves lie on the
printed ones: 95% of the points within 1.0-1.4 px (0.24 mm) of the ink (a bilinear mesh through the ruled grid,
which is keystoned by up to 4 px, gives a median vertical offset of -0.4 px). The interval method's curves lie
1-1.5 px above the printed ones (95% within 2.0-3.2 px). The computed line of Bengen's maxima is within 3.6 px
(0.61 mm; interval method 5.4 px): its lower end bends to m_o = .0378 kg where the printed line runs on to
about .040 kg (the printed curves are flat there, so their maxima are ill-defined).

Curves start at the engine alone, m_o = .021 kg (the mass of curve (a) of Figure 11, "the mass of the engine
alone", ch4-sec3.tex:148, 189), and run to .10 kg. The line of Bengen's maxima is the locus of each curve's
maximum as k varies continuously: from the k whose maximum is the chart's 700 m (about .000032) to .0016, where
the printed line ends on the lowest curve.

Writes fig16.csv (m0; y_max in m for each k, columns k00005 ... k0016) and fig16-bengen.csv (k, m0, ymax).
"""
import math
import pathlib
import sys

import numpy as np
from scipy.optimize import brentq, minimize_scalar

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import trajectory as T  # noqa: E402

METHOD = "fm"                     # "fm": eqs. (20), (21), (67); "interval": eqs. (83)-(87) (then move the labels: fig16.tex header)
K = [("k00005", 0.00005), ("k0001", 0.0001), ("k0002", 0.0002), ("k0004", 0.0004), ("k0008", 0.0008),
     ("k0016", 0.0016)]
M_ENGINE, M_END, Y_TOP = 0.021, 0.10, 700.0


def ymax(m0, k):
    f = T.fehskens_malewicki if METHOD == "fm" else T.interval
    return f(m0, k)[2]


def bengen(k):
    """The liftoff mass of the maximum altitude for k, and that altitude."""
    r = minimize_scalar(lambda m: -ymax(m, k), bounds=(0.0095, 0.1), method="bounded",
                        options={"xatol": 1e-7})
    return r.x, -r.fun


def main():
    m = np.round(np.linspace(M_ENGINE, M_END, 159), 6)
    cols = [[ymax(x, k) for x in m] for _, k in K]
    with open(HERE / "fig16.csv", "w") as fh:
        fh.write("m0," + ",".join(n for n, _ in K) + "\n")
        for i, x in enumerate(m):
            fh.write(f"{x:.6f}," + ",".join(f"{c[i]:.2f}" for c in cols) + "\n")
    k_top = brentq(lambda k: bengen(k)[1] - Y_TOP, 1e-5, 1e-4, xtol=1e-12)
    ks = np.exp(np.linspace(math.log(k_top), math.log(K[-1][1]), 60))
    with open(HERE / "fig16-bengen.csv", "w") as fh:
        fh.write("k,m0,ymax\n")
        for k in ks:
            mo, yo = bengen(k)
            fh.write(f"{k:.8f},{mo:.6f},{yo:.2f}\n")
    print(f"fig16 ({METHOD}): k at the 700 m top of Bengen's line {k_top:.7f} (m_o {bengen(k_top)[0]:.4f})")
    for n, k in K:
        mo, yo = bengen(k)
        print(f"  k = {k:<7g} y_max {ymax(M_ENGINE, k):6.1f} m at the engine alone, maximum {yo:6.1f} m at "
              f"m_o = {mo:.4f} kg, {ymax(M_END, k):6.1f} m at {M_END}")


if __name__ == "__main__":
    main()
