# v2 audit: ch3/fig36 (round 1)

Sources checked: scan `figures/ch3/fig36.png`; inventory row `ch3-fig36`; caption and citing text
`chapters/ch3-sec5a.tex:166-169, 175-182, 232-233`; STYLE.md sections 14 and 16; redraw `figures/v2/ch3/fig36.tex`,
`fig36.py`, `fig36.csv`, `fig36.calib.json`, rebuilt with `make fig F=ch3/fig36` (4.79 x 3.31 in) and rendered at
400 dpi; `tools/v2/digitize.py overlay` and an independent `digitize.py trace` of the scan (seed 140,251, both
directions, 388 points over 2.05-23.9) compared with the CSV.

Checked and correct:
- Curve: a cubic fit to the traced centre line (measured curve, no formula in the book: digitize is right). My
  independent trace differs from the CSV by mean 0.0000, rms 0.0006, max 0.0030 in $\eta$ (1.6 px). Spot values
  (trace / CSV): 4: 0.599 / 0.598; 8: 0.661 / 0.661; 12: 0.705 / 0.706; 16: 0.737 / 0.737; 20: 0.760 / 0.759;
  24: 0.773 / 0.774. $\eta(16)$ = 0.737, the text's "$\eta$ = 0.74". The curve runs 2-24, as printed (0.560 to 0.774).
- Overlay: 89 points, 95% within 0.00 px, max 0.00 px. Every point lands on the 2-3 px ink line.
- Axes: $\eta$ upright as printed; 0.5-1.0, labelled every 0.1, grid every 0.05; $\dfrac{\ell_b}{d}$ 0-24, labelled
  every 4, grid every 2. Axes 4.2 x 2.6 in (the scan's aspect, 1.62), the same frame as Fig 35.
- No overlaps or clipping; curve s1, text ink.

## Findings

| # | severity | finding | where | suggested fix |
|---|---|---|---|---|
| 1 | note | The header comment says "95% of points within 1.3 px", but `digitize.py overlay` with the default threshold now gives 0.00 px. The trace-to-fit numbers (rms 0.3 px, max 1.2 px; my trace: max 1.6 px) are the meaningful measure. | fig36.tex:4 | optional: quote the reproducible figure |

## Verdict: pass (no must-fix)
