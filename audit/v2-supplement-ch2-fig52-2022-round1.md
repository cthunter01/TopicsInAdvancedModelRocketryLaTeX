# v2 audit: supplement/ch2-fig52-2022 (round 1)

Sources checked: 2022 chart scan `figures/supplement/ch2-fig52-2022.png` (axis titles upscaled 3x); redraw
`figures/v2/supplement/ch2-fig52-2022.pdf` (300 dpi render) and `build/v2/png/supplement-ch2-fig52-2022-compare.png`;
`figures/v2/supplement/ch2-fig52-2022.tex` lines 1-24, `.py`, `.csv`, `.calib.json`; inventory row
`sup-ch2-fig52-2022` (`figures/v2/inventory.csv`:66); `chapters/ch2-sec3d.tex`:406, 410-418 (eqs. (73b), (74a),
(75)); `chapters/ch2-sec6.tex`:452-460 (caption), :476-488 (the range to avoid, 25%, rule of thumb 0.44 / 1.35 /
2.0); `backmatter/supplement/s-ch2-2022.tex`:45-64 (the figure in the supplement Part, note: bounded region,
$\zeta_c \ge 0.4472$), :111-124; `corrections/v2-figures.md` (minor: eq. (73b) with $1.25/C_1$); `STYLE.md` sections 13, 16.

Checks made:
- **Formula.** The script sets eq. (73b) equal to $1.25/C_1$, giving $(\beta_c^2-1)^2 + (2\zeta_c\beta_c)^2 = 0.64$,
  and parametrises it by $\beta_c^2 - 1 = -0.8\cos\theta$. I substituted all 241 rows back into eq. (73b): the
  largest departure of $C_1\mathit{AR}_c$ from 1.25 is $3\times10^{-5}$.
  - The feet are $\beta_c = \sqrt{0.2} = 0.4472$ and $\sqrt{1.8} = 1.3416$.
  - The peak is $\zeta_c = 0.44721$ at $\beta_c = 0.77460$. This agrees with eqs. (74a) and (75)
    ($\mathit{AR}_{\mathrm{cres}} = 1/(2\cdot0.4472\cdot0.8944) = 1.25$) and with the supplement's 0.4472.
- **Points evaluated** (the branch crossings; the render agrees with each):

  | $\zeta_c$ | 0.1 | 0.2 | 0.3 | 0.4 |
  |---|---|---|---|---|
  | $\beta_c$ | 0.453 and 1.325 | 0.472 and 1.272 | 0.511 and 1.174 | 0.600 and 1.000 |

  At $\zeta_c = 0.4$, $\beta_c = 1.000$ falls exactly on a gridline crossing in both the chart and the redraw.
- **Text.** The rule of thumb (below $0.44\,\omega_{nc}$, or above $1.35\,\omega_{nc}$ but not over $2.0\,\omega_{nc}$)
  reads off the feet, which sit just inside those limits, and off the $\beta_c = 2.0$ gridline. "Bounded by the
  curve" and "no amplification over 25% for $\zeta_c \ge 0.4472$" both hold of the drawn arch.
- **Lettering** (compared with the chart, upscaled):
  - x title: Coupled Frequency Ratio $\beta_c = (\omega_z/\omega_{nc})$.
  - y title: Coupled Damping Ratio $\zeta_c$.
  - Both are kept as printed, including the lowercase $\omega_z$. The 2022 chart is typed, so its case is not in
    doubt (STYLE section 13, typewritten subscripts keep their case). The chapter prose writes $\omega_Z$.
  - The tick ranges are the chart's: 0 to 2.5 in steps of 0.5, and 0 to 0.50 in steps of 0.05. The gridlines
    are at the chart's spacing (`tamr grid`: a design chart read for values).
  - The chart title is the caption and is correctly left out.
- **Restyle.** The redraw drops the spreadsheet look, as the family brief asks: the Excel point markers, the
  sans-serif lettering and the three-decimal tick labels (0.000 becomes 0, 0.050 becomes 0.05). The tick values
  are unchanged.
- **Overlay** (computed curve against the 2022 chart).
  - With the tool's default ink threshold the report is a false MISMATCH (95th percentile 37.6 px). The chart's
    curve is a light grey line (grey level about 200-228) that the default `--dark 140` does not count as ink.
  - With `--dark 230` (the gridlines, at 239 and above, are still excluded) the mean is 1.06 px, the 95th
    percentile 3.61 px and the maximum 5.39 px, on this crop's larger scale. The visual overlay coincides along
    the whole arch; the chart's peak sits at about 0.445.
- **Size and fonts.** 5.72 in wide (at most 6.5 in); all fonts embedded. No overlaps or clipping.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | The overlay against this crop needs `--dark 230`: the 2022 curve is light grey, and the default threshold misses it and reports 37.6 px. With the right threshold the computed boundary matches (mean 1.06 px). Record the threshold with the overlay numbers wherever they are logged. | ch2-fig52-2022.calib.json | none (bookkeeping) |
| 2 | note | The axis title keeps the chart's lowercase $\omega_z$ while Chapter 2's prose (ch2-sec6.tex:470, 476, 487) writes $\omega_Z$. This follows standing rule 2 and the typed-case rule; the inventory already flags it. | ch2-fig52-2022.tex:18 | none (owner may confirm at the gate, since the figure sits in the chapter) |
| 3 | note | There is no shading of the avoided region, which is faithful to the 2022 chart. The text ("bounded by the curve") does not need shading. | - | none |

## Verdict

pass (0 must-fix, 0 should-fix)
