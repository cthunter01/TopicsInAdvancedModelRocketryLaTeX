# v2 audit: ch3/fig05 (round 2)

Sources checked: figures/ch3/fig05.png (the scan); figures/v2/ch3/fig05.pdf (rebuilt with `make fig F=ch3/fig05`:
4.45 x 2.33 in, fonts embedded, clean log; rendered at 300 dpi) and build/v2/png/ch3-fig05-compare.png;
figures/v2/ch3/fig05.tex; figures/v2/inventory.csv row ch3-fig05; the caption (chapters/ch3-intro-sec2a.tex:448-452)
and the citing text (ch3-intro-sec2a.tex:414-434); STYLE.md sections 14 and 16; corrections/v2-figures.md; the
round 1 audit (audit/v2-ch3-fig05-round1.md) and the round 1 fix record.

Changes since round 1: none. fig05.tex is unchanged (21:51, before the round 1 audit). tamrfig.sty is also
unchanged (21:33), so a regression is not possible. The rebuild has the same size as before.

Round 1 findings:
- R1 #1 (note: pi/2 and theta sit beside their arcs, where the scan puts them in a gap in the arc). The fixer kept
  this as a house choice. The labels read clearly, and `\anglemark` / `angle label` are available if the gate wants
  the scan's form. No action needed.
- R1 #2 (note: the 1973 (b) is slightly rotated as well as sheared). The redraw keeps symmetric pure shear, which
  the text describes ("will neither move away nor turn"). No action needed.

Re-checked and still correct:
- Lettering: $\tau = \dfrac{F}{A_c}$; four $F$ in each panel; "Face area $= A_c$"; $\dfrac{\pi}{2}$; $\gamma =
  \dfrac{\pi}{2} - \theta$; $\theta$; panel letters (a) and (b). Nothing is missing or added.
- Force senses form a balanced couple pair: top to the right, right side up, bottom to the left, left side down.
  In (b) the forces lie along the turned sides with the same senses (inventory: "same senses as in (a)").
- (b) geometry: the sides turn 6.5 deg (bottom and top counterclockwise, verticals clockwise). The angle at the
  lower left is therefore theta = 77 deg, which is less than 90 deg as the text says. The arc runs from g/2 to
  90 - g/2, so it measures theta exactly. Both arcs have a head at each end, as printed.
- House rules: panel letters use the `panel` style, at the lower right of each drawing, on one baseline. Vectors
  use `vec` and the arcs use `angle arc`. No local styles are defined.
- Legibility at final size: nothing overlaps or is clipped (no ink touches the page edge), and the width is
  within 6.5 in.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | Both round 1 notes stand as house choices. The angle labels sit beside the arcs, not in a gap, and (b) is drawn as symmetric pure shear. No new issues. | fig05.tex:46-47, 52-61 | None. |

## Verdict: pass (0 must-fix, 0 should-fix)
