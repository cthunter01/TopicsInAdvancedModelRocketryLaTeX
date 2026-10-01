# v2 audit: ch4/fig09b (round 1)

Sources checked: scan `figures/ch4/fig09b.png` (2x view, 6x crops at both k labels, a pixel dump of columns 86-130
by rows 144-180); redraw `figures/v2/ch4/fig09b.pdf` (built with `make fig F=ch4/fig09b`, log clean; 300 and 600
dpi renders, `pdffonts`), `build/v2/png/ch4-fig09b-compare.png`; sources `fig09b.tex`, `fig09.py`, `fig09b.csv`,
`fig09b.calib.json`; template `figures/v2/ch4/fig06a.tex` (and fig06b, whose y title and legend position this
panel shares); inventory row `ch4-fig09b` (`figures/v2/inventory.csv`:139); caption and citing text
`chapters/ch4-sec2b.tex`:306-372 and :487-493; `corrections/v2-figures.md`; STYLE.md section 16.

Checks made:
- **Data reproduced.** A copy of `fig09.py` run in my scratch directory writes a `fig09b.csv` byte-identical to the
  committed one.
- **Calibration.** `digitize.py lines/ticks`: x axis at row 292-292.5, ticks at columns 237, 292.5, 348, 404.5, 461,
  516.5 (and 124.5, 180.5, as calibrated); y ticks at rows 20.5, 66.5, 111, 156.5, 202.5, 248, 293.5. The
  calibration points agree within 0.5 px; affine residual 0.79 px.
- **Overlay** (`digitize.py overlay`, each curve as its own CSV):

  | curve | mean | 95% | max |
  |---|---|---|---|
  | FM k_min | 0.06 px | 0.00 px | 2.83 px |
  | CB k_min | 0.53 px | 2.00 px (0.34 mm) | 2.00 px |
  | FM k_max | 0.03 px | 0.00 px | 1.00 px |
  | CB k_max | 0.74 px | 2.05 px (0.35 mm) | 10.05 px |

  The 10 px is the extrapolated start (finding 1).
- **Independent traces** (`digitize.py trace`, `--max-jump 2`, in pieces between the leader crossings; one point
  is 9.1 px on this scan). Each piece agrees with the CSV, with mean differences within ±0.003 points:
  - CB k_min, 0.111-0.300: 95% 0.03 points.
  - FM k_min, 0.158-0.245 and 0.270-0.300: 95% 0.02-0.03 points.
  - FM k_max, 0.203-0.243 and 0.270-0.299: 95% 0.03 points.
  - CB k_max, 0.203-0.300: 95% 0.04 points.
- **The crossing near 0.13.** The 8x overlay shows each fitted solid on its own ink through the crossing, and FM
  k_max on the zero line at the start.
- **Curve identity.** At 6x the 1973 leaders end as follows:
  - k_max on the flatter solid (column 400, row 173) and, crossing the steeper solid, on the upper dashed
    (column 422, row 216).
  - k_min on the steeper solid (column 197.5, row 168) and on the lower dashed.

  The redraw's leader ends all lie on the intended curves:
  - (0.2467, -1.976) is FM k_max.
  - (0.2565, -6.604) is CB k_max.
  - (0.1566, -1.159) is FM k_min.
  - (0.1397, -7.052) is CB k_min.
- **Values against the inventory.**
  - FM k_max: +0.13 at 0.11 and -2.87 at 0.30 (inventory about 0.2 and -2.9).
  - FM k_min: +0.95 to -6.26 (about 1 and -6.3).
  - CB k_max: -1.64 to -8.03 (about -1.8 and -8).
  - CB k_min: -5.72 to -9.01 (about -5.8 and -9).
- **Lettering.**
  - y title "Percent error in $y_b$"; x title "$m_o$ (kg)".
  - y ticks -15 to 15 by 5; x ticks 0.10-0.30 by 0.05 with minor ticks at the midpoints.
  - $k_{\max}$ near 0.25 and $k_{\min}$ near 0.15, each with two straight leaders.
  - Legend at the upper right as printed; `muted` zero line.
  - The inventory's comma-like stray mark left of the y title is scan dirt and is rightly not drawn.
- **Template and family.**
  - Same options as fig06a/fig06b (4.0 x 2.5 in, `tamr`, series1 = FM, series2 = CB).
  - Page 341.05 x 219.91 pt, identical to fig06b's (the $y_b$ title).
  - Fonts embedded. Nothing clipped; the legend clears the curves (highest +0.95).
- **Caption and text.**
  - The caption ("Burnout altitude error ... Type F7 engine") is true of the redraw.
  - The largest error in the panel is -9.01% (CB k_min at 0.30), under the 10% the text cites
    (ch4-sec2b.tex:325-330).

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | **CB k_max is drawn from 0.110 kg, but its printed ink starts at about 0.114 kg.** The first dash is at columns 101-108, row 173. The other three curves start at columns 91-92, which is 0.110 kg. The redraw extends this curve back to 0.110 with the others by extrapolating the spline over about 9 px: -1.64 at 0.110, 1.9 mm at final size, a 0.08-point change in value. This is reasonable, since all four curves are evaluated at the same twenty masses starting from the engine-alone 0.110 kg. However, it is recorded only in the `fig09.py` docstring. | fig09b.csv rows 0.1100-0.1125 (cb_kmax); fig09.py docstring | Keep the extension and log it as a minor item in `corrections/v2-figures.md` at the gate (orchestrator). The alternative is to start cb_kmax at the printed 0.114, with its own first mass in fig09.py. |
| 2 | note | As in the scan, several leaders cross lines on the way to their curves. The right $k_{\max}$ leader crosses the zero line and both solids before it reaches CB $k_{\max}$. The upper $k_{\min}$ leader crosses the CB $k_{\max}$ dashed line. All of them end clearly on their curves at 600 dpi. | fig09b.tex:24-28 | None. |

## Verdict: pass

No must-fix and no should-fix. The curves sit on the scan (95% within 2.05 px) and agree with independent traces to
0.04 point. The k assignment matches the printed leaders, and the panel is identical in frame and style to
fig06a/fig06b. Finding 1 is a gate-log item only.
