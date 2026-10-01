# v2 audit: ch3/fig35 (round 1)

Sources checked: scan `figures/ch3/fig35.png` (start of the curve zoomed 4x); inventory row `ch3-fig35`; caption and
citing text `chapters/ch3-sec5a.tex:112-116, 136-142, 221-226`; `corrections/v2-figures.md` (pilot gate: Lamb's
prolate spheroid for Fig 35, computed); STYLE.md sections 14 and 16; redraw `figures/v2/ch3/fig35.tex`,
`fig35.py`, `fig35.csv`, `fig35.calib.json`, rebuilt with `make fig F=ch3/fig35` (4.85 x 3.31 in) and rendered at
400 dpi; `tools/v2/digitize.py overlay` run myself.

Checked and correct:
- Formula: Lamb's $\alpha_o = \frac{2(1-e^2)}{e^3}\left(\tfrac12\ln\frac{1+e}{1-e} - e\right)$,
  $\beta_o = \frac{1}{e^2} - \frac{1-e^2}{2e^3}\ln\frac{1+e}{1-e}$, $k_1 = \alpha_o/(2-\alpha_o)$,
  $k_2 = \beta_o/(2-\beta_o)$, $e = \sqrt{1 - (d/\ell_b)^2}$. Re-evaluated independently ($\alpha_o + 2\beta_o = 2$
  holds): 0.7782 at 4, 0.8719 at 6, 0.9155 at 8, 0.9543 at 12, 0.9710 at 16, 0.9798 at 20; the CSV agrees to
  5e-6. At $\ell_b/d$ = 16 it gives 0.971, the text's "(k_2 - k_1) = 0.97" (and 2(0.97) = 1.94).
- Overlay on the scan (piecewise against the drawn rulings): 97 points, mean 0.57 px, 95% within 1.41 px
  (0.24 mm), max 2.00 px. The scan's curve starts on the 4 ruling at about 0.780 (row 175); the computed 0.778.
- Axes: $(k_2 - k_1)$ rotated as printed; 0.6-1.0, labelled 0.6, 0.8, 1.0, grid every 0.1; $\dfrac{\ell_b}{d}$
  0-20, labelled every 4, grid every 2; curve from 4 only, as printed. Axes 4.2 x 2.6 in, the scan's aspect (1.6),
  and the same frame as Fig 36.
- No overlaps or clipping; curve s1, text ink.

## Findings

| # | severity | finding | where | suggested fix |
|---|---|---|---|---|
| 1 | note | The 1973 curve leaves the 4 ruling almost vertically. Lamb's curve starts there with a finite slope (0.07 per unit of $\ell_b/d$), so the redraw reaches 0.80 at 4.3, where the scan's curve also crosses it. This is within the overlay tolerance and follows the approved decision. | fig35.csv | none |
| 2 | note | Figs 35 and 36 share the frame size but not the x scale (0-20 against 0-24), as in 1973. | fig35.tex:11-12 | none |

## Verdict: pass (no must-fix)
