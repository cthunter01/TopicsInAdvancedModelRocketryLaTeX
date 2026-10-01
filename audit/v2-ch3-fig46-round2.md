# v2 audit: ch3/fig46 (round 2)

Sources checked: scan `figures/ch3/fig46.png`; redraw `figures/v2/ch3/fig46.tex`, `fig46.py`,
`fig46-{cylinder,ellipsoid,ogive,cone}.csv`, `fig46.calib.json`; `make fig F=ch3/fig46` (up to date, 4.86 x 3.53 in;
fonts TeXGyreTermesX-Regular, NewTXMI, NewTXMI7, all embedded), rendered at 400 dpi, compare image; inventory row
`ch3-fig46`; equations (168)-(171e), caption and citing text `chapters/ch3-sec6a.tex:239-286` and
`chapters/ch3-sec6b.tex:69` ("Figure 46 or equation (171c) gives 2.7 l/d_m"); `corrections/v2-figures.md` (standing rules,
pilot gate decisions, lines 153-155 on eq. (171b)); round-1 audit and fix report.

Checks run:
- Nothing changed since round 1. The fig46 files are dated 21:50 (data) and 22:07 (tex, pdf), and the round-1
  audit is dated 22:19. The fixer reported no changes because round 1 had no must-fix or should-fix items.
- I re-evaluated the CSVs against the formulas myself. Cylinder 4f (eq. 170), ellipsoid exact (171a) and printed
  pi f, ogive 2.67 f (171c), cone exact (171d) and printed 2f: maximum deviation 5.0e-6. Spot values at
  f = 1.5 / 3 / 5: (171a) 4.917 / 9.540 / 15.780; pi f 4.712 / 9.425 / 15.708; (171b) as printed, 1 + pi f, 5.712 /
  10.425 / 16.708; (171d) 3.162 / 6.083 / 10.050. The noses start at f = 1.5, and each curve is clipped at the frame
  (the ellipsoid at f = 5.1, the cylinder at 4.02).
- I ran `digitize.py overlay` myself (calibration residual 0.00 px). 95% distance, exact columns: cylinder 1.00,
  ellipsoid 2.24, ogive 1.00, cone 2.24 px. Printed columns: 1.00 / 1.00 / 1.00 / 3.00 px. These are the round-1
  numbers. The printed ellipsoid line is pi f (mean 0.11 px), not (171a) and not (171b).
- Lettering and frame, checked at 400 dpi: y title $S_s/S_m$ upright, x title $\ell/d_m$, x ticks 0-6 with rulings
  every 0.5, y ticks 0-16 every 2 with rulings every 1. Labels Cylinder, Ellipsoid, Ogive, Cone are sloped along
  their lines on white knock-outs, clear of the lines. All four curves are s1 solid. Axes are 4.2 x 2.8 in, `tamr grid`.
  The ogive reads 12.65 at f = 4.74, which gives the text's "2.7 l/d_m".

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | Round-1 note 1 (gate choice) is still open. The redraw defaults to exact (171a) for the ellipsoid and exact (171d) for the cone (`\exacttrue`). The 1973 lines and the caption ("approximate ... terminated at the lower limit of fineness ratio for which they give acceptable accuracy") describe pi l/d_m and 2 l/d_m, which `\exactfalse` reproduces. The exact curves lie 0.21 / 0.16 above the printed lines at f = 1.5 and 0.07 / 0.04 above at f = 5-6. `corrections/v2-figures.md` still records only the v1 question on (171b) (lines 153-155). It has no gate item for this choice. | fig46.tex:13; corrections/v2-figures.md:153 | Orchestrator: add the gate item (exact (171a)/(171d) against the printed approximate lines, with these numbers and the caption wording). No change to the figure before the gate decides. |
| 2 | note | Round-1 note 2 is confirmed again: eq. (171b) as printed (1 + pi l/d_m) is 0.80-0.94 above (171a) for f = 1.5-6. The art and the true asymptote of (171a) are both pi l/d_m. This is already listed as a v1 item. | ch3-sec6a.tex:266-267 | v1 corrections step; nothing in the figure. |
| 3 | note | No regressions. Data, overlay, lettering, ticks, rulings, frame size and fonts are as in round 1. Width 4.86 in, under the 6.5 in limit. | fig46.tex, fig46-*.csv | none |

## Verdict: pass (no must-fix)
