#!/usr/bin/env python3
"""Chapter 3, Figure 17: the control surface A A_1 B_1 B round a flat plate in turbulent flow
(scan figures/ch3/fig17.png).

The caption and Table 2 treat the turbulent boundary layer, so the curves follow the chapter's turbulent law:
  - the boundary-layer edges grow as delta ~ x^(4/5), eq. (80), from the leading edge to delta_O at the
    trailing edge O (delta_O = 58 px, the scan's);
  - the profile at O is the 1/7th-power law, eq. (74): u/U_inf = (|y|/delta)^(1/7) inside the layer;
  - the wake profile u(x, y) at B B_1 carries the same momentum deficit, eq. (73) (D = b rho U^2 theta at
    any station downstream of the plate), theta = 7 delta / 72, eq. (76); its shape is the Gaussian wake
    defect u = U_inf (1 - a exp(-(y/b)^2)) (Schlichting, the book's ref. 15), its width set so that u reaches
    0.99 U_inf at y = delta_O (the wake lines, as in the scan), which with eq. (73) gives a = 0.233 and
    u(0) = 0.77 U_inf (the scan draws the dip to about 0.37 U_inf).
  - upstream (A A_1) the profile is uniform, U_inf.

Drawing units are the scan's pixels (150 per inch), x as in the scan, y up from the plate (scan row 170.5);
the figure draws them 1.2 times the printed size. Writes
  fig17-edge.csv     the upper boundary-layer edge from the leading edge to O (x, y); the lower is its mirror
  fig17-O.csv        the profile at O (x, y), the whole height
  fig17-B.csv        the wake profile at B (x, y)
  fig17-arrows.csv   the arrows of the three profiles (x0, y, x1, head: 1 = long enough for a head)
"""
import csv, pathlib
import numpy as np
from scipy.optimize import brentq

HERE = pathlib.Path(__file__).resolve().parent
XA, XLE, XO, XB = 32.5, 108.0, 340.0, 449.0   # control surface left side, leading edge, trailing edge, B
ELL = XO - XLE                                # plate length (232 px)
TOPY, BOTY = 127.0, -127.0                    # the top of the control surface; the profiles' lower ends
DELTA = 58.0                                  # boundary-layer thickness at O
U = 56.0                                      # length of U_inf
STEP = 10.0
ROWS = [s * (5 + STEP * k) for s in (1, -1) for k in range(12)]   # +-5 ... +-115
HEADMIN = 9.0


def wake():
    theta = 7.0 / 72.0 * DELTA                                     # eq. (76)
    def mom(a):
        b = DELTA / np.sqrt(np.log(100 * a))
        return a * b * np.sqrt(np.pi) / 2 - a * a * b * np.sqrt(np.pi / 2) / 2 - theta
    a = brentq(mom, 0.0101, 0.99)
    b = DELTA / np.sqrt(np.log(100 * a))
    return a, b


def main():
    a, b = wake()
    u_O = lambda y: U * min(1.0, (abs(y) / DELTA) ** (1 / 7))
    u_B = lambda y: U * (1 - a * np.exp(-(y / b) ** 2))
    u_A = lambda y: U
    # edge
    xs = XLE + ELL * np.linspace(0, 1, 121) ** 2                    # denser near the leading edge
    with open(HERE / "fig17-edge.csv", "w", newline="") as fh:
        w = csv.writer(fh); w.writerow(["x", "y"])
        for x in xs:
            w.writerow([f"{x:.3f}", f"{DELTA * ((x - XLE) / ELL) ** 0.8:.3f}"])
    # profiles: the 1/7 law sampled densely near the plate, where it turns
    yo = np.unique(np.r_[np.linspace(BOTY, -DELTA, 30), -DELTA * np.geomspace(1, 1e-6, 120),
                         0.0, DELTA * np.geomspace(1e-6, 1, 120), np.linspace(DELTA, TOPY, 30)])
    with open(HERE / "fig17-O.csv", "w", newline="") as fh:
        w = csv.writer(fh); w.writerow(["x", "y"])
        for y in yo:
            w.writerow([f"{XO + u_O(y):.3f}", f"{y:.4f}"])
    with open(HERE / "fig17-B.csv", "w", newline="") as fh:
        w = csv.writer(fh); w.writerow(["x", "y"])
        for y in np.linspace(BOTY, TOPY, 255):
            w.writerow([f"{XB + u_B(y):.3f}", f"{y:.3f}"])
    with open(HERE / "fig17-arrows.csv", "w", newline="") as fh:
        w = csv.writer(fh); w.writerow(["x0", "y", "x1", "head"])
        for x0, uf in ((XA, u_A), (XO, u_O), (XB, u_B)):
            for y in ROWS:
                u = uf(y)
                w.writerow([x0, f"{y:.1f}", f"{x0 + u:.3f}", int(u >= HEADMIN)])
    theta_B = np.trapezoid((u_B(np.linspace(0, 400, 40001)) / U) * (1 - u_B(np.linspace(0, 400, 40001)) / U),
                           np.linspace(0, 400, 40001))
    print(f"wake: a = {a:.4f}, b = {b:.2f} px, u(0)/U = {1 - a:.3f}; theta_B = {theta_B:.3f} = 7/72 delta "
          f"= {7 / 72 * DELTA:.3f} px")


if __name__ == "__main__":
    main()
