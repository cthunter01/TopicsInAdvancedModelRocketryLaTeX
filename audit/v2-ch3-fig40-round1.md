# v2 audit: ch3/fig40 (round 1)

Sources checked: scan `figures/ch3/fig40.png` (zoomed x3); redraw `figures/v2/ch3/fig40.tex`, `fig40.py`,
`fig40.csv`, `fig40.calib.json`; rebuilt with `make fig F=ch3/fig40` (5.09 x 3.31 in) and rendered at 350 dpi;
inventory row `ch3-fig40`; caption and citing text `chapters/ch3-sec5b.tex:15-40` (eqs. (146), (147));
`corrections/v2-figures.md` (pilot gate: Fig 40 computed by slender-body theory); STYLE.md sections 14, 16;
approved examples `figures/v2/ch3/fig02.tex`, `fig22.tex`, `figures/v2/ch2/fig25.tex`.

Checks run:
- Formula evaluated independently (NACA TR 1307 K_W(B), K_B(W) = (1 + tau)^2 - K_W(B), tau = d/b = r/s):
  0.1: 1.077/0.133; 0.2: 1.162/0.278; 0.289: 1.2425/0.4191; 0.5: 1.4503/0.7997; 0.7: 1.663/1.227;
  0.9: 1.886/1.724; 0.999: 1.999/1.997. `fig40.py` rerun into the scratch dir reproduces `fig40.csv` byte for
  byte. Ends: K_F(B) = 1, K_B(F) = 0 at d/b = 0; both 2.0 at d/b = 1 (they meet at (1.0, 2.0)).
- `digitize.py overlay` (affine calibration, residual 2.47 px): K_F(B) 95% 1.00 px, max 1.00; K_B(F) 95% 2.24 px
  (0.38 mm), max 3.16 px: both "ok".
- Independent check with the gridlines masked and the calibration's piecewise-bilinear mesh (column by column,
  the drawn curve's offset from the computed one): K_F(B) |offset| 95% 0.89 px (on the art everywhere);
  K_B(F) 95% 3.89 px, max 4.8 px. The computed K_B(F) lies 3.9-4.0 px (vertical; about 3.2 px normal to the
  curve, 0.55 mm) above the drawn curve from d/b = 0.65 to 0.95 (at 0.8: computed 1.454, drawn about 1.426),
  and 1-2 px below it at 0.3-0.4. The tool's unmasked number is flattered by the dense grid (rulings
  13.7 px apart vertically).

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | should-fix | The text reads values off this figure that the computed redraw no longer gives exactly: at d/b = .289 the text has K_B(F) = 0.44 and K_F(B) = 1.25 (ch3-sec5b.tex:38-40, used in eq. (147)); the redraw gives 0.419 and 1.242 (the 1973 art about 0.43 and 1.247). The K_B(F) read-off differs by 0.02 (0.7 mm at final size), so a reader gets (.42 + 1.24 - 1) = 0.66 for the factor the text writes as 0.69. Approved decision (compute), so no figure change, but it is not yet in `corrections/v2-figures.md`. | fig40.py docstring (states 1.242/0.419); corrections/v2-figures.md (no Fig 40 entry beyond the gate line) | Orchestrator: add a Fig 40 line to corrections/v2-figures.md (minor, no note in the book): computed 0.419/1.242 at d/b = .289 against the text's 0.44/1.25 and the 1973 art's about 0.43/1.25; with the masked-overlay numbers of note 2. |
| 2 | note | Overlay margin for the "compute when the overlay passes" proposal is thin for K_B(F): passes by the tool (95% 2.24 px), but with gridlines masked the computed curve sits about 3.9 px (vertical) / 3.2 px (normal) above the drawn one over d/b 0.65-0.95. Consistent with the 1973 draughtsman drawing K_B(F) about 0.03 low there; not a problem under the approved decision. | figures/v2/ch3/fig40.csv (KBF column) vs scan | Record the numbers with item 1; no change. |
| 3 | note | All lettering present and as printed: y title "$K_{F(B)}$ / or / $K_{B(F)}$" (three lines, upright), y ticks 0-2.0 labelled every 0.2 with rulings every 0.1, x title $\dfrac{d}{b}$, x ticks 0-1.0 labelled every 0.1 with rulings every 0.05, curve labels $K_{F(B)}$ (below its curve near d/b 0.3) and $K_{B(F)}$ (right of its curve near 0.65) on white knock-outs as printed. Notation per STYLE.md section 14 (italic F, B). | fig40.tex:10-23 | none |
| 4 | note | Legibility at final size good: the $K_{F(B)}$ knock-out clears its curve by about 0.3 mm at d/b of about 0.26; no other overlap or clipping; width 5.09 in. Two solid curves (s1, s2) as printed, both directly labelled, text in ink. | fig40.tex:20-21 | none |
| 5 | note | Family consistency: same 4.2 x 2.6 in axes, `tamr grid` with `grid=both`, upright y title (rotate=-90, anchor=east) as Figs 41 and 42 and the approved Fig 2. | fig40.tex:9-16 | none |

## Verdict: pass (no must-fix)
