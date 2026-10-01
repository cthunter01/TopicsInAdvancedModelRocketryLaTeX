#!/usr/bin/env python3
"""Chapter 3, Figure 52: drag force on the GCR-x rocket against R_l, 10^4 to 10^7.

    D_e = 3.33 x 10^-13 (C_Do)_FB R^2      eq. (210), (C_Do)_FB from the GCR-x equations (fig51.gcrx: the
                                           printed 82.8 coefficient, as Tables 6 and 7 use)
    D_a = 3.33 x 10^-13 x .473 R^2         eq. (211) with the constant (C_Do)_FB = 0.473 of the caption; eq. (211)
                                           rounds the product to 1.58 x 10^-13 (0.3% more, under a line width),
                                           Table 7's D_a column uses 1.575 x 10^-13

Sampled every 1/400 decade from 10^4 to 10^7 (the plot clips at 0.8 N). Checks itself against Table 7 and
writes fig52.csv. Run with --overlay <dir> to write the curves for tools/v2/digitize.py overlay
(fig52.calib.json: the 1973 paper's drawn gridlines).
"""
import importlib.util
import pathlib
import sys

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("fig51", HERE / "fig51.py")
fig51 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fig51)

K = 3.33e-13


def d_exact(R):
    return K * fig51.gcrx(R)[3] * R * R


def d_approx(R):
    return K * 0.473 * R * R


def samples():
    rs = {round(10 ** (4 + k / 400), 6) for k in range(0, 1201)}
    rs |= {fig51.R_CRIT_B, fig51.R_CRIT_F}
    return sorted(rs)


# Table 7 (ch3-sec6c.tex): R, D_e, D_a (newtons)
TABLE7 = [
    (1e4, 1.03e-4, 1.57e-5), (5e4, 1.16e-3, 3.94e-4), (7e4, 1.94e-3, 7.70e-4), (1e5, 3.33e-3, 1.57e-3),
    (1.5e5, 6.18e-3, 3.53e-3), (2e5, 9.55e-3, 6.31e-3), (3e5, 1.77e-2, 1.42e-2), (4e5, 2.77e-2, 2.51e-2),
    (5e5, 3.94e-2, 3.94e-2), (6e5, 5.74e-2, 5.65e-2), (7e5, 7.80e-2, 7.70e-2), (8e5, 1.02e-1, 1.01e-1),
    (9e5, 1.28e-1, 1.27e-1), (1e6, 1.56e-1, 1.57e-1), (1.25e6, 2.39e-1, 2.46e-1), (1.5e6, 3.39e-1, 3.53e-1),
    (1.75e6, 4.50e-1, 4.82e-1), (2e6, 5.82e-1, 6.31e-1), (2.2e6, 6.89e-1, 7.63e-1), (2.4e6, 8.05e-1, 9.09e-1),
    (3e6, 1.21, 1.42), (4e6, 2.05, 2.51), (5e6, 3.07, 3.94), (6e6, 4.45, 5.65), (8e6, 8.31, 10.1),
    (1e7, 13.2, 15.7),
]


def check_table():
    """largest relative difference from Table 7, for each column"""
    we = max(abs(d_exact(R) - e) / e for R, e, a in TABLE7)
    wa = max(abs(d_approx(R) - a) / a for R, e, a in TABLE7)
    return we, wa


def main():
    out = HERE / "fig52.csv"
    rows = ["R,De,Da"]
    for R in samples():
        rows.append(f"{R:.6g},{d_exact(R):.6g},{d_approx(R):.6g}")
    out.write_text("\n".join(rows) + "\n")
    we, wa = check_table()
    print(f"{out.name}: {len(rows) - 1} points; Table 7 max relative difference D_e {we:.1%}, D_a {wa:.1%}")
    if "--overlay" in sys.argv:
        dest = pathlib.Path(sys.argv[sys.argv.index("--overlay") + 1])
        dest.mkdir(parents=True, exist_ok=True)
        for name, fn in (("De", d_exact), ("Da", d_approx)):
            lines = ["x,y"] + [f"{R:.6g},{fn(R):.6g}" for R in samples() if fn(R) <= 0.8]
            (dest / f"fig52-{name}.csv").write_text("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
