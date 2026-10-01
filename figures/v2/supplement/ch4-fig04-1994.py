#!/usr/bin/env python3
"""Chapter 4, Figure 4 as replaced in 1994 (used as Figure 4 in Chapter 4 and in the Errata and Supplement Part):
the same drawing as the 1973 Figure 4, so the same data. "Approximation": eqs. (73a)-(73c) with the lettered
F_m = 13.0 N, F_s = 3.5 N, t_1 = t_m = 0.14 sec, t_2 = t_s = 0.22 sec, t_b = 1.20 sec, computed by
figures/v2/ch4/fig04.py (see its docstring; eq. (75) checks the lettered I_t = 5.0 N-sec). "Actual curve": the
shared figures/v2/common/b4.csv, traced from this figure's scan.

Writes ch4-fig04-1994.csv (t in sec, F in N).
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "ch4"))
import fig04  # noqa: E402

if __name__ == "__main__":
    fig04.write(HERE / "ch4-fig04-1994.csv")
