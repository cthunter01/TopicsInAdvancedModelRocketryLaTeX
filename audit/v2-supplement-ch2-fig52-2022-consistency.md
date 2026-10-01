# v2 consistency check: supplement/ch2-fig52-2022 (Chapter 2's Figure 52)

Issue: the figure was drawn larger than the chapter's other single frequency-response plots (axes 5.0 x 3.2 in,
5.72 in overall). It should take axes 4.2 in wide and about 2.6-3.0 in high, to match Figs 25, 31 and 49, and keep
the 2022 chart's grid and lettering.

Sources checked:
- figures/v2/supplement/ch2-fig52-2022.tex:1-24 (modified 20:19), rebuilt with `make fig`. Rendered at 300 and
  600 dpi.
- build/v2/png/supplement-ch2-fig52-2022-compare.png, against the 2022 chart figures/supplement/ch2-fig52-2022.png.
- The CSV, the .py and the calib.json, all unchanged since 17:41.
- figures/v2/ch2/fig25.tex, fig31.tex and fig49.tex, with Fig 31 rendered at 300 dpi.
- The round-1 audit and inventory row sup-ch2-fig52-2022.
- The includes at chapters/ch2-sec6.tex:454 and backmatter/supplement/s-ch2-2022.tex:49.

## Checks

- **The issue: resolved.** The axes are now `width=4.2in, height=3.0in`, the values in fig25.tex:8 and
  fig31.tex:10. Fig 49 uses 4.2 x 2.6 in.
  - **Axes:** measured on the 300 dpi renders, the x-axis line runs 1274 px and the y-axis line 914 px in both
    Fig 52 and Fig 31, so the two plot areas are identical.
  - **Overall size:** 4.92 x 3.56 in (was 5.72 x 3.75 in). Figs 25 and 31 are 4.90 x 3.64 in; they are taller
    because of their fraction tick labels.
  - **Height chosen:** 3.0 in is at the top of the allowed range. The 2022 plot area's aspect is about 0.68, and
    0.71 is drawn.
- **Grid and lettering are kept.**
  - `tamr grid`, with vertical gridlines every 0.5 in $\beta_c$ and horizontal ones every 0.05 in $\zeta_c$. The
    top (0.50) and right (2.5) gridlines are drawn, as on the chart.
  - Ticks 0 to 2.5 and 0 to 0.50, as in round 1.
  - x title: Coupled Frequency Ratio $\beta_c = (\omega_z/\omega_{nc})$, with the lowercase $\omega_z$ as
    printed. y title: Coupled Damping Ratio $\zeta_c$.
  - Only one header comment line was added (the size).
- **The curve is unchanged.**
  - The CSV has 241 rows. The feet are at 0.44721 and 1.34164, and the peak is 0.44721 at 0.7746.
  - Substituted into eq. (73b), the largest departure of $C_1\mathit{AR}_c$ from 1.25 is $2.6\times10^{-5}$.
  - Overlay on the 2022 chart with `--dark 230`: mean 1.06 px, 95th percentile 3.61 px, max 5.39 px. These are
    identical to round 1, where the light-grey trace on this large crop was explained and accepted. The tool's
    MISMATCH flag is the same as in round 1.
  - At $\zeta_c = 0.4$ the curve still passes through the gridline crossing at $\beta_c = 1.0$.
- **Legibility and clipping.**
  - At 0.3 in per 0.05 step, the \footnotesize tick labels are well separated.
  - At 600 dpi, nothing overlaps or is clipped. The 0.50 and 2.5 labels, both axis titles and the feet at the
    axis are all complete.
  - All fonts are embedded.
  - The book still includes the PNG crop. Once switched, the PDF is included unscaled, so the new size carries
    through.

## Verdict: pass

The size matches Figs 25 and 31. Nothing else changed.
