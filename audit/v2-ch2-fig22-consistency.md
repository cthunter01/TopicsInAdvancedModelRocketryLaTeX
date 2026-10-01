# v2 consistency check: ch2/fig22

Issues resolved here: (1) the alpha_Xm and t_m lines become solid `peak line` (they were dashed `guide`); (2) the
frame is set like Fig 21 (ymin -0.42, the vertical axis running below 0 as printed), the formula block is checked
and the size is checked. Verifier only (no edits).

Sources checked: `figures/v2/ch2/fig22.tex` against the fixer's pre-fix copy (`scratchpad/ch2fix/g1-peaks/before/`);
`figures/v2/tamrfig.sty`; STYLE.md section 16; scan `figures/ch2/fig22.png`; inventory row `ch2-fig22`;
`audit/v2-ch2-fig22-round1.md`; `build/v2/png/ch2-fig22-compare.png`; my own scratch build; renders at 200, 300
and 400 dpi, side by side with Figs 21 and 23; the fixer's unadopted alternative (`scratchpad/ch2fix/g1-peaks/optB/`).

Checks made:
- Source diff: (a) `\draw[guide]` becomes `\draw[peak line]`; (b) `ymin=0` becomes `ymin=-0.42` with the same
  x=0.46in, y=1.8in scale as Fig 21; (c) the formula anchor becomes Fig 21's
  `[xshift=0.35in, yshift=-6pt]ax.south west`. The header comment is updated. The curve, tangent, ticks, marks
  and ymax are unchanged.
- Peak lines: solid ink2 hairlines at 400 dpi, meeting at the computed peak ($t_m = 1$, $\alpha_{Xm} = 1/e$) and
  ending on both axes, as on the scan (inventory: "solid guide at alpha_Xm and vertical at t_m").
- Frame: measured at 300 dpi, the vertical axis runs 229 px (0.76 in) below the t axis, the same as Fig 21 (and
  Fig 23). It now runs below 0 as printed. The $0$ tick label and the $t_m$ tick label are unchanged.
- Formula block: its top is 40 px (0.13 in) below the axis end and its left edge is 123 px (0.41 in) right of the
  axis line, identical to Figs 21 and 23. All 12 formula words moved rigidly 39.22 pt down. All 15 plot words
  are unmoved, and the word count is unchanged (27). $\alpha_{Xm} = \frac{H}{I_L D e}$ and $t_m = \frac{1}{D}$
  (eqs. (42b), (42a)) are intact. Nothing overlaps: the $t_m$ tick label is about 0.8 in above the block.
- Size: 342.88 x 234.115 pt = 4.76 x 3.25 in (was 2.71 in). That is shorter than Fig 21 (3.65 in) and Fig 23
  (3.41 in), and the width is unchanged. Sensible.
- Build: compiles cleanly; no warnings; all fonts embedded.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | Unlike Fig 21, where the trough fills the band below 0, here the band beside the axis stub is empty. The formulas sit about 0.9 in below the t axis. The 1973 art sets them inside that band, beside the lower axis. The fixer's alternative in `scratchpad/ch2fix/g1-peaks/optB/fig22b.tex` (anchor `[xshift=0.35in, yshift=-0.24in]ax.origin`, about 2.7 in tall) does that, but at the cost of the placement shared with Fig 21. Keeping the family layout identical is a sound reading of "frame like Fig 21". | `fig22.tex:26` | None needed. Owner's choice at the gate if a tighter, 1973-like placement is preferred (apply to Figs 22 and 23 together). |

## Verdict: pass
