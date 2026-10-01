# v2 audit: ch3/fig52 (round 1)

Sources checked: scan `figures/ch3/fig52.png`; redraw `figures/v2/ch3/fig52.tex`, `fig52.py`, `fig52.csv`,
`fig52.calib.json`, `figures/v2/ch3/fig52.pdf` rendered at 400 dpi; `build/v2/png/ch3-fig52.png`; inventory row
ch3-fig52; caption and citing text `chapters/ch3-sec6c.tex` lines 425-566 (eqs. (208)-(211), Table 7, "no
distinction ... below 1e5", "within 10% from 4e5 to 2.2e6"); STYLE.md section 16; `corrections/v2-figures.md`
rule 3; approved Ch4 Fig 6(a) (legend precedent); `tamrfig.sty` legend style; `pdffonts` (fonts embedded); page
452 x 293 pt = 6.28 in wide.

Independent checks:
- Equations: I recomputed with my own script (scratch `chk52.py`). D_e = 3.33e-13 (C_Do)_FB R^2 uses (C_Do)_FB from
  the printed GCR-x equations, and D_a = 3.33e-13 x 0.473 R^2. fig52.csv agrees to 1e-5 relative. Against Table 7:
  1e5 gives 3.3e-3 / 1.6e-3 (table 3.33e-3 / 1.57e-3); 5e5 gives 0.0394 / 0.0394; 1e6 gives 0.157 / 0.158; 2.2e6 gives
  0.688 / 0.762 (table 0.689 / 0.763); 2.4e6 gives 0.807 (0.805). Eq. (211)'s rounded 1.58e-13 would move D_a by
  0.3%, less than a line width.
- The curves leave the 0.8 N top at R = 2.39e6 (D_e) and 2.25e6 (D_a) and are clipped cleanly at the frame. The two
  curves cannot be told apart below 1e5, as the text says. D_a lies visibly above D_e beyond about 1.2e6.
- Overlay (`digitize.py overlay`, the drafter's gridline calibration; residual 1.87 px, x piecewise on the drawn
  rulings), 95th percentile: D_e 2.24 px, D_a 2.0 px. Above about 0.5 N the 1973 curves run visibly right of the
  computed ones.
- Axes: a true log x axis, identical to Fig 51 (ticks, lettering, printed rulings as minor grid); y runs 0-0.8,
  labelled every 0.1; titles "$D$ (N)" (upright) and $R_\ell$; same 5.4 x 3.5 in frame as Figs 22 and 51.
- Encoding: D_e is `series1` solid and D_a is `series2` dashed, as the house rule for two compared methods
  requires. The legend sits at the lower right as printed, with the grid blanked behind it, entries $D_e$ and $D_a$.

## Findings
| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | Above 0.5 N the 1973 curves lie right of the computed curves (the drafter's doubt). The computed curves are kept per the gate decision. Table 7's own D_e at 2e6 (0.582) also disagrees with Table 6 x eq. (210) (0.575, computed 0.577); this is a 0.9% table slip, minor, logged only. | | log under the Ch3 gate items only if not already recorded |
| 2 | note | The kit's `legend style` has `fill opacity=0.9`, which is transparency in a kit style; "flat line art only" forbids it. It is harmless here because no curve passes behind the legend. This is kit-level, not the drafter's. | tamrfig.sty line 177 | kit owner: `fill opacity=1` |
| 3 | note | The legend font is overridden to `\small`, against the kit's `\footnotesize`. This matches the house label size and Fig 51's curve labels; approved Ch4 Fig 6(a) uses the kit default. | fig52.tex `legend style={..., font=\small}` | none (or settle one legend size at the gate) |

## Verdict: pass (no must-fix)
