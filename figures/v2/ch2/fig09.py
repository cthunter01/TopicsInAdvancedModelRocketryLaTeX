#!/usr/bin/env python3
"""Chapter 2, Figure 9: the linearization approximations for the rocket of Figures 7 and 8.

True curves: the same data as Figures 7 and 8 (fig07.csv and fig08.csv, digitized by fig07.py and fig08.py;
run those first, as make figdata does). Linear approximations: eq. (8) M_c = C_1 alpha_X and eq. (9)
M_d = C_2 Omega_X, the tangents at zero, with the lettered C_1 = 1x10^6 dyn-cm and C_2 = 1.25x10^4
dyn-cm-sec. Writes fig09-mc.csv (alpha, true M_c, C_1 alpha) and fig09-md.csv (Omega, true M_d, C_2 Omega).
"""
import csv
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
C1, C2 = 1.0e6, 1.25e4
for src, dst, head, C in (("fig07.csv", "fig09-mc.csv", "alpha,true,linear", C1),
                          ("fig08.csv", "fig09-md.csv", "Omega,true,linear", C2)):
    with open(HERE / src) as fh:
        rows = [(float(a), float(b)) for a, b in list(csv.reader(fh))[1:]]
    (HERE / dst).write_text(head + "\n" + "".join(f"{x:g},{y:.1f},{C * x:.1f}\n" for x, y in rows))
    print(f"{dst}: {len(rows)} points (true from {src}; linear slope {C:g})")
