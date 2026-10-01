# v2 audit: ch2/fig18 (round 1)

Sources checked: scan `figures/ch2/fig18.png`; inventory row `ch2-fig18`; caption `chapters/ch2-sec3a.tex:732-733`;
citing text `chapters/ch2-sec3a.tex:709-727`; eqs. (16), (33), (34a), (34b); credit
`backmatter/figure-credits.tex:35`; errata/supplement/`corrections/ch2.md` (nothing on this figure); redraw
`figures/v2/ch2/fig18.{tex,py,csv,calib.json,pdf}`; `build/v2/png/ch2-fig18{,-compare}.png`; own 400 dpi render
(including a crop of the curve's right end against the dashed line); `digitize.py overlay`; STYLE.md sections
13 and 16.

Checks made:
- Lettering: $\frac{M_s}{C_1}$ (y tick), 0, $\alpha_X$ (rad), $t$ (sec): all present; no t tick, as printed;
  the speck left of the scan's axis is not drawn. Nothing added.
- Curve: independently evaluated $(M_s/C_1)[1 - (1 + Dt)e^{-Dt}]$, $D = \omega_n$ (eqs. (33), (34a), (34b)):
  the CSV agrees to 7e-6; zero value and slope at 0; monotone; maximum 0.99829 $M_s/C_1$ at the end, so it
  approaches the line from below and never reaches it (caption). 0.979 at two thirds of the way across and
  0.989 at three quarters: meets the dashed line about two thirds across, as in the scan.
- Time axis shared with Figs 16, 17, 19 ($2.75\pi/\omega_n$). The calibration pins the scan's curve end to
  that time (the scan has no time tick), so the overlay measures shape at the family scale.
- Overlay (calibration exact, 3 points): mean 2.01 px, 95% 5.39 px (0.91 mm), max 6.08 px (computed curve;
  the scan rises a little faster: the .py notes that the scan alone fits $DT \approx 7.8$ rather than 8.64).
- Size 329.2 x 196.3 pt (4.57 in wide); fonts Type 1, embedded.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | From about $t = 5.5/\omega_n$ the curve lies within 0.5 mm of the dashed asymptote and covers it to the end (the curve is 0.2% below at the end), so the dashed line shows only over the left 60%. The scan does the same ("meets the dashed line ... and runs along it"), and the approach from below still reads. | `fig18.tex:16-17` | none |
| 2 | note | Docstring nit: "within 2 percent of $M_s/C_1$ from two thirds of the way across" is 2.13% at exactly two thirds (2% from 0.68 of the way), and "1 percent from three quarters" is 1.15% (1% from 0.78). No effect on the figure. | `fig18.py:11-12` | optional: say "about 2 percent ... about 1 percent" |
| 3 | note | Same local `every axis y label` override as the family (style suggestion in the Fig 15 report). | `fig18.tex:14-15` | style suggestion only |

## Verdict: pass (no must-fix)
