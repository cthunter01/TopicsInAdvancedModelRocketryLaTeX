# v2 audit: ch3/fig34 (round 1)

Sources checked: scan `figures/ch3/fig34.png` (inset zoomed 4x); inventory row `ch3-fig34`; caption and citing text
`chapters/ch3-sec4b.tex:446-464` (eqs. (123)-(125)); `corrections/v2-figures.md` (minor: experimental data not
drawn); STYLE.md sections 14 and 16; redraw `figures/v2/ch3/fig34.tex`, `fig34.py`, `fig34.csv`,
`fig34.calib.json`, rebuilt with `make fig F=ch3/fig34` (5.05 x 3.07 in) and rendered at 400 dpi;
`tools/v2/digitize.py overlay` run myself on both calibrated parts.

Checked and correct:
- Curve: eq. (125) $C_{Db} = 0.029/\sqrt{C_{fb}}$; the CSV runs from (0.00934, 0.300) to (0.8, 0.0324); spot
  values 0.1 -> 0.0917, 0.8 -> 0.0324 agree. Overlay: steep part (C_fb <= 0.1) 41 points, 95% within 1.00 px, max
  1.00; tail (C_Db <= 0.15) 73 points, 95% within 1.00 px, max 1.00 (calibration residuals 0.96 and 1.26 px).
- Axes: $C_{Db}$ 0-0.30, ticks every 0.05 all labelled (0, 0.05, 0.10 ... 0.30); $C_{fb}$ 0-0.8, labelled every
  0.2, grid every 0.1; $C_{Db}$ upright at the left as printed. Axes 4.2 x 2.5 in (the scan's aspect, 1.69).
- Lettering: the formula $C_{Db} = \dfrac{.029}{\sqrt{C_{fb}}}$ with the printed leading-dot .029 (rule 2), set
  beside the curve in a white knock-out (no other curve); inset $U$ with its flow arrow; the note "$C_{Db}$
  calculated / using base area" with a leader arrow to the base. Nothing added; no data points (as printed, logged
  as minor).
- Inset: pointed nose, maximum radius at 0.45 of the length, truncated base (fineness 6.3), dash-dot axis, white
  fill so the grid stops at it; moved 0.04 left and 0.015 down so it fits inside the frame between the 0.20 and 0.25
  rulings (body 0.205-0.245; centre line ends at 0.792, inside 0.8). Straight leader with a head, as house.
- No overlaps or clipping; text in ink, curve s1.

## Findings

| # | severity | finding | where | suggested fix |
|---|---|---|---|---|
| 1 | note | The $U$ arrow starts at $C_{fb}$ = 0.195, so the 0.2 gridline crosses it 0.6 mm from its tail. | fig34.tex:27, 40 | optional: start the arrow at 0.205 |
| 2 | note | The formula's knock-out ends almost on the 0.3 gridline, which shows a short gap there. Harmless. | fig34.tex:24-25 | none (or nudge the label 0.01 left) |
| 3 | note | Fig 34's axes are 2.5 in high, Figs 35-36's 2.6 in: each keeps its printed aspect; all three are 4.2 in wide. | fig34.tex:16 | none |

## Verdict: pass (no must-fix)
