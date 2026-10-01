#!/usr/bin/env python3
"""Chapter 3, Figure 14: the Blasius profile f'(eta) = u/U_inf against eta (eta vertical).

Data: Table 1 (chapters/ch3-sec3a.tex, label ch3:tab:1: Howarth's solution of eq. (51), f f'' + 2 f''' = 0 with
the boundary conditions (52), (53)), read from the chapter source. Between the tabulated points (every 0.2 in
eta) f and f' are interpolated by piecewise cubic Hermite polynomials that use the table's own derivative
columns (f' for f, f'' for f'), so the curve passes through every tabulated value with the tabulated slope.
Beyond eta = 8.8 (the table's end) f' = 1 and f = 7.07923 + (eta - 8.8). Checked against a numerical solution
of eq. (51) (shooting on f''(0)): the interpolant differs from it by less than 2e-5 in f' (printed by the
script).

The dashed line is the displacement thickness: delta* sqrt(U_inf/(nu x)) = lim (eta - f) = 8.8 - 7.07923
= 1.72077 (Table 1). The figure letters it 1.73 (Schlichting 1.72; corrections/v2-figures.md, minor): the line
is placed by the table, the printed lettering is kept.

The curve is drawn until it meets the u/U_inf = 1.0 border, i.e. until the gap 1 - f' is less than half the
curve's line width (0.5pt) on the 4.2 in axes, as the 1973 curve ends there (about eta = 6).

This module is also imported by fig15.py, fig19.py, fig20.py and fig21.py (blasius(), f, fp).

Writes fig14.csv (fp, eta) and fig14-marks.csv (dstar: the displacement thickness line).
"""
import pathlib
import re

import numpy as np
from scipy.interpolate import CubicHermiteSpline

ROOT = pathlib.Path(__file__).resolve().parents[3]
LINE_PT = 0.5                    # half the house curve width (1pt), in pt
AXIS_W_PT = 4.2 * 72.27          # Figs 14 and 15: 4.2 in axes


def table1():
    """Table 1 of chapters/ch3-sec3a.tex as an array of rows (eta, f, f', f'')."""
    src = (ROOT / "chapters" / "ch3-sec3a.tex").read_text()
    body = src[src.index(r"\label{ch3:tab:1}"):]
    body = body[body.index(r"\midrule"):body.index(r"\bottomrule")]
    rows = []
    for m in re.finditer(r"^\s*([0-9.]+)\s*&\s*([0-9.]+)\s*&\s*([0-9.]+)\s*&\s*([0-9.]+)\s*\\\\", body, re.M):
        rows.append([float(g) for g in m.groups()])
    t = np.array(rows)
    assert t.shape == (45, 4) and t[0, 0] == 0.0 and t[-1, 0] == 8.8, t.shape
    return t


class blasius:
    """f(eta), f'(eta), f''(eta) from Table 1 (cubic Hermite through the table, constant flow beyond 8.8)."""

    def __init__(self):
        t = table1()
        self.tab = t
        self._f = CubicHermiteSpline(t[:, 0], t[:, 1], t[:, 2])
        self._fp = CubicHermiteSpline(t[:, 0], t[:, 2], t[:, 3])
        self.eta_max = t[-1, 0]
        self.f_end = t[-1, 1]

    def f(self, eta):
        eta = np.asarray(eta, dtype=float)
        return np.where(eta <= self.eta_max, self._f(np.minimum(eta, self.eta_max)),
                        self.f_end + (eta - self.eta_max))

    def fp(self, eta):
        eta = np.asarray(eta, dtype=float)
        return np.where(eta <= self.eta_max, self._fp(np.minimum(eta, self.eta_max)), 1.0)

    def delta_star(self):
        """lim (eta - f): the displacement thickness in units of sqrt(nu x/U_inf)."""
        return self.eta_max - self.f_end

    def meets(self, gap):
        """The eta where 1 - f' first falls to gap (bisection on the interpolant)."""
        lo, hi = 0.0, self.eta_max
        for _ in range(60):
            mid = 0.5 * (lo + hi)
            if 1.0 - float(self.fp(mid)) > gap:
                lo = mid
            else:
                hi = mid
        return 0.5 * (lo + hi)


def ode_check(b):
    """Largest difference in f' between the interpolant and a numerical solution of eq. (51)."""
    from scipy.integrate import solve_ivp
    sol = solve_ivp(lambda e, y: [y[1], y[2], -0.5 * y[0] * y[2]], (0, 8.8), [0, 0, 0.332057],
                    dense_output=True, rtol=1e-11, atol=1e-13)
    e = np.linspace(0, 8.8, 2001)
    return float(np.max(np.abs(sol.sol(e)[1] - b.fp(e))))


def write_csv(path, header, cols, fmt="{:.5f}"):
    lines = [",".join(header)]
    for row in zip(*cols):
        lines.append(",".join(fmt.format(v) for v in row))
    path.write_text("\n".join(lines) + "\n")


if __name__ == "__main__":
    b = blasius()
    end = b.meets(LINE_PT / AXIS_W_PT)
    eta = np.linspace(0.0, end, 241)
    here = pathlib.Path(__file__)
    out = here.with_suffix(".csv")
    write_csv(out, ["fp", "eta"], [b.fp(eta), eta])
    write_csv(here.with_name(here.stem + "-marks.csv"), ["dstar"], [[b.delta_star()]])
    print(f"{out.name}: {len(eta)} points, eta 0 to {end:.3f} (f' = {float(b.fp(end)):.5f}); "
          f"delta* = {b.delta_star():.5f} (printed 1.73); ODE check: max |df'| = {ode_check(b):.2e}")
