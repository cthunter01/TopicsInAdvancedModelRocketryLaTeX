# v2 audit: ch3/fig34 (consistency fix verification)

Issue checked: labelled free-stream velocity arrows drawn at two weights (keys ch3/fig16, fig25, fig30, fig34).
The suggestion for Fig 34: draw the inset's labelled U as `vec` (STYLE s.16: force and velocity vectors are
`vec`). Alternatively, if `vec` is too heavy in the small insets, make the Fig 51 inset `thin vec`, so that the
three plot insets match.

Sources checked: redraw `figures/v2/ch3/fig34.tex`, rebuilt with `make fig F=ch3/fig34` (5.05 x 3.07 in) and
rendered at 400 dpi (inset zoomed); the compare render `build/v2/png/ch3-fig34-compare.png`; scan
`figures/ch3/fig34.png`; inventory row `ch3-fig34`; round-1 audit `audit/v2-ch3-fig34-round1.md`; `tamrfig.sty`
(vec 1.3pt with a 7 x 4.6pt Stealth head; thin vec 0.6pt); the other insets (fig51.tex:62, fig30.tex:36 and 55)
and the flow drawings (fig16.tex:44, fig25.tex:73-74). I reran `tools/v2/digitize.py overlay` on both calibrated
parts.

## Issue 2 (velocity-arrow weight): resolved

- fig34.tex:40 now draws the labelled U as `vec`, and the comment records the match with the Fig 51 inset.
- All three plot insets now agree. Fig 51's $U_\infty$ (fig51.tex:62), Fig 30's two insets' U (fig30.tex:36, 55)
  and Fig 34's U are all `vec`. The fallback (Fig 51 to `thin vec`) was not needed and was correctly not taken.
  Figs 16 and 25 are also `vec` now, so all the labelled free-stream arrows in the chapter agree.
- At 400 dpi the heavier arrow does not look too heavy. It is 0.52 in long against a 7pt head, sits at
  $C_{Db}$ = 0.225 between the 0.20 and 0.25 rulings, and its tip stops about 0.03 in short of the 0.3 vertical
  ruling. The U label is clear of the shaft and of every ruling. The heavier shaft also hides the 0.2 ruling's
  crossing near the tail (round-1 note 1).

## Regression check: none found

- The curve is untouched. My overlay gives: steep part, 97 points, mean 0.41 px, 95% within 1.00 px, max 2.00 px;
  tail, mean 0.15 px, 95% within 1.00 px, max 2.00 px (calibration residuals 0.96 and 1.26 px). This is as in
  round 1.
- Lettering, axes, scale, inset body, note and leader are unchanged, and they agree with the inventory row: the
  formula with the printed .029, U, "$C_{Db}$ calculated / using base area", and the axis titles $C_{Db}$ and
  $C_{fb}$.
- The figure size is unchanged (5.05 x 3.07 in, axes 4.2 x 2.5 in, as in Figs 35 and 36 apart from the printed
  aspect).

## Findings

| # | severity | finding | where | suggested fix |
|---|---|---|---|---|
| 1 | note | The fixer's report says the U label's white fill "still breaks the 0.2 grid line". At 400 dpi the label (about C_fb 0.235-0.255, C_Db 0.23-0.245) touches no ruling, so no ruling is broken. The report's wording is harmless, and nothing in the figure needs a change. | fig34.tex:40 | none |
| 2 | note | Figs 35 and 36 of this family have neither a velocity profile nor a velocity arrow, so neither issue applies to them. Their files are unchanged (mtimes predate the fix). | n/a | none |

## Verdict: pass
