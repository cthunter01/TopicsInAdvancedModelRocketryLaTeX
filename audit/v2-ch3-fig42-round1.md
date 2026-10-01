# v2 audit: ch3/fig42 (round 1)

Sources checked: scan `figures/ch3/fig42.png` (zoomed x3); redraw `figures/v2/ch3/fig42.tex`, `fig42.py`,
`fig42.csv`, `fig42.calib.json`; rebuilt with `make fig F=ch3/fig42` (4.87 x 3.28 in) and rendered at 350 dpi;
inventory row `ch3-fig42`; caption and citing text `chapters/ch3-sec5b.tex:184-223` (eq. (151), u/U = 0.0172);
STYLE.md sections 14, 16.

Checks run:
- `fig42.py` rerun into the scratch dir reproduces `fig42.csv` byte for byte: 361 traced points (u/U 0.086 to
  2.983), cubic C_D = 0.19828 + 0.03980 x + 0.04994 x^2 - 0.00375 x^3; residual rms 0.32 px, 95% 0.64 px,
  max 1.24 px. Values 0.198 (0), 0.284 (1), 0.448 (2), 0.666 (3) against the inventory's 0.20, about 0.29, 0.45,
  0.665.
- `digitize.py overlay` (affine, residual 4.15 px): 95% 0.00 px, max 2.00 px, "ok". Gridline-masked mesh check:
  |offset| 95% 0.74 px, max 1.19 px: the curve sits on the art from 0.1 to 2.95.
- Text: at u/U = 0.0172 the effect is "too small to be read from the curve": redraw 0.199 against 0.198 at 0,
  true.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | Below u/U of about 0.09 the drawn curve runs along the 0.2 ruling and is masked, so the start is the cubic's extrapolation: 0.198 with slope 0.040, 0.002 below the 0.20 the print starts on (0.6 px on the scan, 0.17 mm at final size). Invisible at final size. | fig42.py (free cubic); fig42.csv first rows | Optional, only if the figure is revisited: constrain c0 = 0.20. |
| 2 | note | Lettering as printed: y title $\CD$ (upright), y ticks 0-0.8 labelled every 0.1, x title $\dfrac{u}{U}$ (lowercase u over capital U, as the scan and caption: u tangential surface velocity, U free stream), x ticks 0, 1, 2, 3 with rulings every 0.5 (minor grid). The family brief's "U/U*" is a slip; the redraw is right. | fig42.tex:9-15 | none |
| 3 | note | One solid s1 curve, no labels (as printed); width 4.87 in; family frame 4.2 x 2.6 in, `tamr grid` with `grid=both`, as Figs 40 and 41. | fig42.tex:8-17 | none |

## Verdict: pass (no must-fix)
