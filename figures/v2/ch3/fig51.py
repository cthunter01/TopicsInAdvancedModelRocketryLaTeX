#!/usr/bin/env python3
"""Chapter 3, Figure 51: drag coefficients of the GCR-x rocket against R_l, 10^4 to 10^7.

Computed from the chapter's GCR-x equations as printed (chapters/ch3-sec6c.tex, after eqs. (199)-(205)):

    (C_Df)_b = 82.8 (C_f)_B                 (82.8 as printed: ednote, corrections D21; Table 6 uses it)
    C_Db     = .0149 / sqrt((C_Df)_b)       (eq. (200) with d_b/d_m = .8)
    (C_Do)_B = (C_Df)_b + C_Db
    (C_Do)_F = 46.4 (C_f)_F                 (eq. (201))
    (C_Do)_FB = (C_Df)_b + C_Db + (C_Do)_F  (eq. (205))
    (C_f)_B = 1.328/sqrt(R)                       R < 5 x 10^5      (eq. (203a))
            = 0.074/R^(1/5) - 1735/R              R >= 5 x 10^5     (eq. (203b), B = 1735)
    (C_f)_F = 4.25/sqrt(R)                        R < 5.14 x 10^6   (eq. (204a), l_b/c = 18/1.75)
            = 0.118/R^(1/5) - 17,900/R            R >= 5.14 x 10^6  (eq. (204b))

R is sampled every 1/200 decade with the two switch points (5 x 10^5 and 5.14 x 10^6) added, so the kinks are
sharp. The script checks itself against Table 6 (23 Reynolds numbers) and writes fig51.csv; fig52.py imports
gcrx() from here. Run with --overlay to write the curves in the scan's printed-paper coordinates for
tools/v2/digitize.py overlay (fig51.calib.json: the drawn gridlines, as the 1973 curves were plotted on them).
"""
import math
import pathlib
import sys

R_CRIT_B = 5e5
R_CRIT_F = 5.14e6


def cf_body(R):
    return 1.328 / math.sqrt(R) if R < R_CRIT_B else 0.074 / R ** 0.2 - 1735 / R


def cf_fins(R):
    return 4.25 / math.sqrt(R) if R < R_CRIT_F else 0.118 / R ** 0.2 - 17900 / R


def gcrx(R):
    """(C_Db, (C_Do)_B, (C_Do)_F, (C_Do)_FB) of the GCR-x at R_l = R."""
    cdfb = 82.8 * cf_body(R)
    cdb = 0.0149 / math.sqrt(cdfb)
    cdo_b = cdfb + cdb
    cdo_f = 46.4 * cf_fins(R)
    return cdb, cdo_b, cdo_f, cdo_b + cdo_f


def samples():
    rs = {round(10 ** (4 + k / 200), 6) for k in range(0, 601)}
    rs |= {R_CRIT_B, R_CRIT_F, R_CRIT_B * (1 - 1e-9), R_CRIT_F * (1 - 1e-9)}
    return sorted(rs)


# Table 6 (ch3-sec6c.tex): R, C_Db, (C_Do)_B, (C_Do)_F, (C_Do)_FB
TABLE6 = [
    (1e4, .014, 1.114, 1.970, 3.080), (5e4, .021, .513, .883, 1.396), (7e4, .023, .438, .748, 1.186),
    (1e5, .025, .373, .627, 1.000), (1.5e5, .028, .312, .510, .822), (2e5, .030, .276, .441, .717),
    (3e5, .033, .233, .359, .592), (4e5, .036, .210, .312, .522), (5e5, .038, .194, .279, .473),
    (6e5, .034, .223, .255, .478), (7e5, .033, .242, .236, .478), (8e5, .031, .257, .221, .478),
    (9e5, .031, .266, .208, .474), (1e6, .030, .272, .197, .469), (1.25e6, .030, .284, .176, .460),
    (1.5e6, .029, .289, .161, .450), (2e6, .029, .293, .139, .432), (3e6, .029, .292, .112, .404),
    (4e6, .029, .287, .098, .385), (5e6, .030, .281, .089, .370), (6e6, .030, .276, .102, .378),
    (8e6, .031, .268, .122, .390), (1e7, .031, .261, .135, .396),
]


def check_table():
    worst = 0.0
    for R, *tab in TABLE6:
        calc = gcrx(R)
        for t, c in zip(tab, calc):
            worst = max(worst, abs(t - c))
    return worst


def main():
    here = pathlib.Path(__file__)
    out = here.with_suffix(".csv")
    rows = ["R,CDb,CDoB,CDoF,CDoFB"]
    for R in samples():
        cdb, b, f, fb = gcrx(R)
        rows.append(f"{R:.6g},{cdb:.5f},{b:.5f},{f:.5f},{fb:.5f}")
    out.write_text("\n".join(rows) + "\n")
    print(f"{out.name}: {len(rows) - 1} points; Table 6 max |difference| {check_table():.4f}")
    if "--overlay" in sys.argv:
        # one CSV per curve for digitize.py overlay (scratch use only; not read by the figure)
        dest = pathlib.Path(sys.argv[sys.argv.index("--overlay") + 1])
        dest.mkdir(parents=True, exist_ok=True)
        for k, name in enumerate(["CDb", "CDoB", "CDoF", "CDoFB"]):
            lines = ["x,y"]
            for R in samples():
                v = gcrx(R)[k]
                if v <= 1.6:
                    lines.append(f"{R:.6g},{v:.5f}")
            (dest / f"fig51-{name}.csv").write_text("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
