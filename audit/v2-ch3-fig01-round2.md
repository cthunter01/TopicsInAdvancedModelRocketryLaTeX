# v2 audit: ch3/fig01 (round 2)

Sources checked: figures/v2/ch3/fig01.tex and the PDF (rebuilt with `make fig F=ch3/fig01`: 3.79 x 3.52 in, fonts
embedded; rendered at 300 dpi); build/v2/png/ch3-fig01-compare.png beside the scan figures/ch3/fig01.png; inventory
row ch3-fig01; caption and citing text chapters/ch3-intro-sec2a.tex:140-168; STYLE.md sections 14 and 16;
tamrfig.sty (`model` rocket, `\anglemark`, `cg mark`, `cp mark`, `every picture` font); the round-1 audit
(audit/v2-ch3-fig01-round1.md) and the drafter's round-1 fix record; Figs 10 and 12 of this family for
consistency.

Round-1 findings:
- Note 1 (C.P. placed for three fins, two-fin profile drawn, Fig 12 four fins): carried into the drafter's doubts
  for the gate, as asked. Resolved.
- Note 2 (`\anglemark` against Ch1 Fig 6's `angle arc`): carried into doubts for the consistency pass. Fig 12 of
  this family uses `\anglemark` too, so the family is uniform. Resolved.
- Note 3 (headless 1973 lines drawn as house `vec`, overbars kept): carried into doubts. Resolved.

Checks (the figure is unchanged since round 1, and no regression was found):
- Lettering complete and as printed: $\bar V$, $\alpha$, C.G. (`\CG`, quartered circle), C.P. (`\CP`, circle and
  dot), $\bar D$. The heading "Drag is determined by:" sits over a rule, and the eight bullet items are in the
  printed order and wording, "angle of attack ($\alpha$)" included. All are set `\small` by the kit default.
- Geometry: the axis is at 52 deg and alpha at 23 deg. $\bar V$ starts at the C.G. and $\bar D$ at the C.P., at
  180 deg from $\bar V$. The C.P. (0.813 L) is aft of the C.G. (0.72 L). The arc's ends land on the centre line and
  on $\bar V$.
- Axis: a thin solid extension beyond the nose and the tail, and dash-dot inside the body. This now matches Fig 10
  (changed in round 1) and Fig 12 (ahead of the nose).
- Legibility: nothing clipped or overlapping. The C.G. and C.P. labels are clear of the outline and of $\bar D$.
  Width is within 6.5 in.

## Findings
| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | All round-1 notes are carried into doubts for the gate and the consistency pass. Nothing is open. | fig01.tex | None. |

## Verdict: pass (no must-fix)
