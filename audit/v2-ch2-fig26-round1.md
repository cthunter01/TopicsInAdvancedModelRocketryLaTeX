# v2 audit: ch2/fig26 (round 1)

Sources checked: scan `figures/ch2/fig26.png` (zoomed: both plots' lettering, slope lines, origins);
inventory row `ch2-fig26`; caption and citing text `chapters/ch2-sec3c.tex:690-718` (eqs. (55)-(60), the
$C_2 = 0$ displays at 681-687); credit `backmatter/figure-credits.tex:59`; `corrections/ch2.md` (D9 only, on
the $b^2$ display, which the curves do not use) and `corrections/v2-figures.md` (standing rule 4 names Fig 26);
redraw `figures/v2/ch2/fig26.{tex,py,csv,calib.json,pdf}` and `fig26-marks.csv`; `build/v2/png/ch2-fig26{,-compare}.png`;
my own 400 dpi render; `digitize.py overlay`; STYLE.md sections 13 and 16; the sibling layouts Figs 27-29 and
Figs 10-14; the approved Ch1 Fig 3 (tangent drawn `series2, solid`).

Checks made:
- Lettering: upper Slope${}=\Omega_{X0}$, $\alpha_{X0}$ (tick label with tick), 0, $\alpha_X$ (rad), $t$ (sec);
  lower Slope${}=\Omega_{Y0}$, $\alpha_{Y0}$, 0, $\alpha_Y$ (rad), $t$ (sec). All present, in the section 13
  forms (the art's lowercase x/y/o subscripts). Nothing added; no panel letters, as printed.
- Curves: I integrated the book's coupled homogeneous equations (`ch2-sec3c.tex:11-16`) independently with
  $I_L = C_1 = 1$, $I_R\omega_Z = 4/(3\sqrt5)$, $C_2 = 0$ and $(\alpha_{X0}, \alpha_{Y0}, \Omega_{X0},
  \Omega_{Y0}) = (0.65, 1, 1.55, 1.55)$. The CSV agrees to $5\times10^{-6}$ (its rounding), and the script's
  closed form (eqs. (55), (56), (58a), (58b), (59), (60)) reproduces the CSV exactly. Both plots come from that
  one motion. $\omega_1 = \sqrt5/3 = 0.7454$, $\omega_2 = -3/\sqrt5 = -1.3416$, ratio $-5/9$: the motion
  repeats with period $42.2$ (the caption's "repeats itself periodically"); $D_1 = D_2 = 0$, so there is no decay
  (text, line 698-701).
- Shapes against the inventory: upper extrema 1.32 (t 0.85), 0.35, 0.90, $-2.35$, 2.08 (t 10.0), ending at
  $-0.32$ (just below 0); lower 2.12 (t 1.12), $-2.32$, 0.84, 0.33, 1.37, ending at $-2.34$ near the bottom
  of the axis ($y_{\min} = -2.7$). Both curves stay inside the axes (nothing clipped).
- Tangents: initial slopes of the CSV 1.53 and 1.55 (first difference) against the drawn 1.55: the lines are
  tangent (standing rule 4). Their labels sit at their upper ends, clear of the curves and of the axis titles.
- Overlay (fitted calibration, no printed scale): upper curve mean 0.94 px, 95% 3.16 px, max 4.24 px; lower
  curve mean 1.63 px, 95% 4.47 px, max 6.32 px. Tangents against the 1973 lines: upper 95% 7.63 px (the 1973
  line is steeper than the curve, rule 4), lower 5.84 px.
- Size 320.2 x 346.0 pt (4.45 x 4.81 in); fonts Type 1, all embedded. Layout identical to Figs 27-29
  (x = 0.27 in per unit, y = 0.36 in per unit, both plots $-2.7$ to 3.1, 0.42 in gap).

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | The computed curves' overlay is a little over the 3 px target (95% at 3.16 px upper, 4.47 px lower; drafter's figures confirmed). These are computed curves for an unscaled sketch with a fitted calibration, which the owner accepts. STYLE.md section 16 still asks for such mismatches to be recorded, and `corrections/v2-figures.md` has no entry for them. | `fig26.py` docstring; `corrections/v2-figures.md` (Minor) | orchestrator: log one Minor line (Fig 26 computed from eqs. (55)-(60), overlay 95% 3.2/4.5 px); no change to the figure |
| 2 | note | The printed vertical titles beside the axes become upright titles above the arrows (the `tamr sketch` placement, as in Figs 10-23). Wording and units are unchanged. | `fig26.tex:13-16` | none |
| 3 | note | The per-file override of `every axis y label` works around `tamr sketch`'s `rotate=-90`, which turns the label on its side under `axis lines=middle`. Figs 10-23 and 26-29 all carry the same override. | `tamrfig.sty` `tamr sketch` | style suggestion: drop `rotate=-90` from `tamr sketch`'s `ylabel style` (then the overrides can go) |
| 4 | note | In the lower plot the true tangent ($\alpha_{Y0} = 1$, slope 1.55) lies under the curve for its first ~0.3 time units, so only its upper part shows in orange. A tangent has to look like this, and the scan's lower line also hugs the curve. | `fig26.tex:38-39` | none |

## Verdict: pass (no must-fix)
