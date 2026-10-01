#!/usr/bin/env python3
"""Chapter 2, Figure 8: damping moment M_d against angular velocity Omega_X (a measured curve).

The book gives no equation for this "typical" curve (ch2-sec2.tex: its form is "roughly as shown"), so it is
digitized from the 1973 art, figures/ch2/fig08.png (the cleanest tracing: Fig 9 draws the same curve under
its linear approximation), with the method of fig07.py. Calibration: fig08.calib.json, piecewise between the
drawn ticks (they are unevenly spaced; read against them the drawn initial slope is C_2). Fig 9 (fig09.py)
reuses this curve.

Fit: M_d = C_2 Omega up to the join at 60 rad/sec (where the drawn curve leaves its tangent: the concave fit
with the least residual), then C_2 Omega + r(Omega) with r a cubic B-spline joined with r = r' = r'' = 0;
C_2 = 1.25x10^4 dyn-cm-sec (the Fig 9 lettering; eq. (9): the linear approximation is the tangent at zero).
The drawn maximum (about 1.37x10^6 near 139 rad/sec) and the slight fall to 150 come from the trace.
Writes fig08.csv (Omega in rad/sec, M_d in dyn-cm).
"""
import pathlib
import sys
import numpy as np

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from fig07 import load_calib, to_data, trace, fit, report  # noqa: E402

C2, XJ = 1.25e4, 60.0
crop, xgrid, ygrid = load_calib("fig08.calib.json")
# the x axis runs from row ~312.5 at the origin to ~310 at 150 rad/sec: stop 3 px above it
P = trace(crop, 100, 523, 10, lambda c: 309.5 - (c - 130) * 2.3 / 370, 309)
x, y = to_data(P[:, 0], P[:, 1], xgrid, ygrid)
keep = x > 4.0                    # the first few columns merge with the axes
x, y = x[keep], y[keep]
f = fit(x, y, C2, XJ, 150.0, n_inner=4)
report("fig08", f, x, y, ygrid, C2, 150.0, [25, 50, 75, 87, 100, 125, 137, 150])
w = np.linspace(0, 150, 151)
(HERE / "fig08.csv").write_text("Omega,Md\n" + "".join(f"{wi:.1f},{mi:.0f}\n" for wi, mi in zip(w, f(w))))
print(f"fig08.csv: {len(w)} points")
