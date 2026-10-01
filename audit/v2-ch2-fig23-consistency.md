# v2 consistency check: ch2/fig23

Issues resolved here: (1) the alpha_Xm and t_m lines become solid `peak line` (they were dashed `guide`); (2) the
frame is set like Fig 21 (ymin -0.42, the vertical axis running below 0 as printed), the formula block is checked
and the size is checked. Verifier only (no edits).

Sources checked: `figures/v2/ch2/fig23.tex` against the fixer's pre-fix copy (`scratchpad/ch2fix/g1-peaks/before/`);
`figures/v2/tamrfig.sty`; STYLE.md section 16; scan `figures/ch2/fig23.png`; inventory row `ch2-fig23`;
`audit/v2-ch2-fig23-round1.md`; `build/v2/png/ch2-fig23-compare.png`; my own scratch build; renders at 300 and
400 dpi, side by side with Figs 21 and 22; the fixer's unadopted alternative (`scratchpad/ch2fix/g1-peaks/optB/`).

Checks made:
- Source diff: the same three changes as Fig 22: `peak line` for the marks, `ymin=-0.42` in Fig 21's scale, and
  Fig 21's formula anchor. The header comment is reflowed. The tau/zeta computation, curve, tangent, ticks and
  ymax are unchanged.
- Peak lines: solid ink2 hairlines at 400 dpi, meeting at the computed peak ($t_m = 0.817$,
  $\alpha_{Xm} = 0.249$) and ending on both axes, as on the scan (inventory: "solid guides at alpha_Xm and t_m").
- Frame: the vertical axis runs 229 px (0.76 in, 300 dpi) below the t axis, the same as Figs 21 and 22. It now
  runs below 0 as printed. The curve is still clearly above 0 at the right edge.
- Formula block: its top is 40 px below the axis end and its left edge is 123 px right of the axis, identical to
  Figs 21 and 22. Its right edge is at 1010 of 1429 px, well inside the figure. All formula words moved rigidly
  39.22 pt down. All plot words are unmoved, and the word count is unchanged (77). Eq. (43b) keeps both exponent
  fractions $-\frac{\tau_2}{\tau_1-\tau_2}$ and $-\frac{\tau_1}{\tau_1-\tau_2}$ and the brackets. Eq. (43a) keeps
  the slashed $\ln(\tau_1/\tau_2)$. Nothing overlaps or is clipped.
- Size: 342.88 x 245.201 pt = 4.76 x 3.41 in (was 2.86 in). That is below Fig 21's 3.65 in, and the width is
  unchanged. Sensible.
- Build: compiles cleanly; no warnings; all fonts embedded.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | As in Fig 22, the band beside the axis stub below 0 is empty and the formulas sit beneath the axis end (Fig 21's placement), where the 1973 art sets them beside the lower axis. The fixer's alternative (`scratchpad/ch2fix/g1-peaks/optB/fig23b.tex`) tucks them into the band, but its $t_m$ line still extends below the axis end. The adopted layout keeps the three impulse responses identical. | `fig23.tex:32` | None needed. Owner's choice at the gate (Figs 22 and 23 together). |

## Verdict: pass
