#!/usr/bin/env python3
"""Chapter 2, Figure 33: the four nose outlines, generated exactly from their definitions.

Units of the nose length L; r across (positive to the right), y = -z/L along the axis (tip at 0, base at
-1, i.e. up is towards the tip). One fineness for all four, L/d = 2.4 (R = L/4.8), measured on the scan
(tips at row 54, bases at row 237-238, base half-widths 37-39 px: L = 183 px, R = 38 px).

  conical         r = R z/L                                  (straight lines)
  tangent ogive   circular arc of radius rho = (R^2 + L^2)/(2R) tangent to the body at the base; centre
                  at (r, z) = (R - rho, L): r = R - rho + rho cos(phi), z = L - rho sin(phi),
                  0 <= phi <= asin(L/rho)
  paraboloidal    paraboloid of revolution with its vertex at the tip, r^2 = R^2 z/L:
                  r = R t, z = L t^2, -1 <= t <= 1
  ellipsoidal     half a prolate spheroid (semi-axes L and R): r = R sin(theta), z = L (1 - cos(theta)),
                  -90 <= theta <= 90 deg

The C.P. positions drawn are those printed and listed in eqs. (80a)-(80d) (chapters/ch2-sec4.tex): 2/3 L,
.466 L, 1/2 L, 1/3 L from the tip. The volume-over-base-area rule of the text (ch2-sec4.tex:194-201)
reproduces (80a), (80c) and (80d) exactly for any fineness; for the tangent ogive it depends on the
fineness, and the script prints its value at L/d = 2.4 for comparison with .466 L.

Writes figures/v2/ch2/fig33-cone.csv, -ogive.csv, -paraboloid.csv, -ellipsoid.csv (columns r,y), each the
open profile from the left base corner over the tip to the right base corner (the figure closes the base).
"""
import csv, math, pathlib

HERE = pathlib.Path(__file__).resolve().parent
FINENESS = 2.4                  # L/d
L = 1.0
R = L / (2 * FINENESS)
N = 181                         # samples per profile


def cone():
    # straight sides, sampled like the others so that the overlay checks the whole side (t = 0 is the tip)
    return [(R * t, -L * abs(t)) for t in (-1 + 2 * i / (N - 1) for i in range(N))]


def ogive():
    rho = (R * R + L * L) / (2 * R)
    phit = math.asin(L / rho)
    right = []                              # the right half, from the tip (phi = phit) to the base (phi = 0)
    for i in range(N // 2 + 1):
        phi = phit * (1 - i / (N // 2))
        r = R - rho + rho * math.cos(phi)
        z = L - rho * math.sin(phi)
        right.append((max(r, 0.0), -z))
    right[0] = (0.0, 0.0)                   # the tip exactly
    left = [(-r, y) for r, y in reversed(right[1:])]
    return left + right


def paraboloid():
    pts = []
    for i in range(N):
        t = -1 + 2 * i / (N - 1)
        pts.append((R * t, -L * t * t))
    return pts


def ellipsoid():
    pts = []
    for i in range(N):
        th = math.radians(-90 + 180 * i / (N - 1))
        pts.append((R * math.sin(th), -L * (1 - math.cos(th))))
    return pts


def volume_cp(profile_r, n=200000):
    """C.P. from the tip by the text's rule: L - volume / base area (midpoint rule in z)."""
    v = 0.0
    for i in range(n):
        z = (i + 0.5) / n * L
        v += math.pi * profile_r(z) ** 2 * (L / n)
    return L - v / (math.pi * R * R)


def main():
    for name, pts in (("cone", cone()), ("ogive", ogive()), ("paraboloid", paraboloid()),
                      ("ellipsoid", ellipsoid())):
        with open(HERE / f"fig33-{name}.csv", "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["r", "y"])
            for r, y in pts:
                w.writerow([f"{r + 0.0:.6f}", f"{y + 0.0:.6f}"])   # + 0.0: no "-0.000000"
    rho = (R * R + L * L) / (2 * R)
    shapes = {
        "cone (80a: 2/3)": lambda z: R * z / L,
        "tangent ogive (80b: .466)": lambda z: math.sqrt(max(0.0, rho * rho - (L - z) ** 2)) + R - rho,
        "paraboloid (80c: 1/2)": lambda z: R * math.sqrt(z / L),
        "ellipsoid (80d: 1/3)": lambda z: R * math.sqrt(max(0.0, 1 - (1 - z / L) ** 2)),
    }
    for k, f in shapes.items():
        print(f"{k:28s} volume rule at L/d = {FINENESS}: C.P. {volume_cp(f):.4f} L from the tip")


if __name__ == "__main__":
    main()
