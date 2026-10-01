# v2 consistency check: ch2/fig21

Issue resolved here: (1) the alpha_Xm and t_m lines become solid `peak line` (they were dashed `guide`). Fig 21
is also the reference frame for issue (2), Figs 22 and 23. Verifier only (no edits).

Sources checked: `figures/v2/ch2/fig21.tex` against the fixer's pre-fix copy (`scratchpad/ch2fix/g1-peaks/before/`);
`figures/v2/tamrfig.sty`; STYLE.md section 16; scan `figures/ch2/fig21.png`; inventory row `ch2-fig21`;
`audit/v2-ch2-fig21-round1.md`; `build/v2/png/ch2-fig21-compare.png`; my own scratch build; renders at 300 dpi
(pre-fix against current) and 400 dpi.

Checks made:
- Source diff: `\draw[guide]` becomes `\draw[peak line]` on the path (0, alpha_Xm) -- (t_m, alpha_Xm) -- (t_m, 0),
  and the header comment is updated. Nothing else changed: the frame (x=0.46in, y=1.8in, ymin=-0.42, ymax=1.0),
  the tangent, the curve and the formula anchor are all as before.
- Render: 425 pixels differ at 300 dpi. All of them fall in columns 118-294 and rows 208-580, which is exactly the
  horizontal line from the axis to the peak and the vertical line from the peak to the t axis. At 400 dpi both
  lines are solid ink2 hairlines. They meet at the curve's maximum and end on the two axes, as on the scan.
  Size 342.88 x 262.773 pt (4.76 x 3.65 in), unchanged.
- Lettering: the same 46 words at the same positions before and after: titles, ticks $0$, $\alpha_{Xm}$, $t_m$,
  "Slope $= \frac{H}{I_L}$", and both formulas (eqs. (41b), (41a)) intact.
- Inventory: "solid guide at alpha_Xm and solid vertical from the peak to t_m" is now met. Round 1 had them
  dashed.
- Frame (reference for Figs 22 and 23), measured at 300 dpi: the vertical axis runs 229 px (0.76 in) below the t
  axis; the formula block's top is 40 px below the axis end and its left edge is 123 px right of the axis line.
  The trough (-0.316) lies within the axis range; nothing overlaps or is clipped.
- Build: compiles cleanly; no warnings; all fonts embedded.

## Findings

None.

## Verdict: pass
