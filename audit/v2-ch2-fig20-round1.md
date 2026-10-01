# v2 audit: ch2/fig20 (round 1)

Sources checked: figures/ch2/fig20.png (scan); figures/v2/ch2/fig20.pdf (current build: 5.91 x 2.48 in, all
fonts embedded; rendered at 400 dpi) and build/v2/png/ch2-fig20-compare.png; figures/v2/ch2/fig20.tex;
figures/v2/inventory.csv row ch2-fig20; caption chapters/ch2-sec3b.tex:43-51; citing text ch2-sec3b.tex:3-20
(the rectangle of area $M_s t_1$, the limit to an impulse of strength $H$); STYLE.md sections 13 and 16;
corrections/v2-figures.md (standing rule 2 names this figure's $T_1$, $M_{s1}$); approved examples ch1/fig05.tex
(three panels, panel letters), ch1/fig03.tex, ch2/fig25.tex.

Checked and correct:
- Lettering, all three panels: y title $M_X$ (dyn-cm) (the section 13 uppercase moment subscript), x title
  $t$ (sec), "0" under each origin; (a) $M_{s1}$ tick, $T_1$ tick, "Area $= H$"; (b) $M_{s2}$ tick, $T_2$ tick,
  "Area" / "$= H$" on two lines as printed; (c) $\infty$ at the arrow tip, "Strength $= H$". $T_1$, $T_2$,
  $M_{s1}$, $M_{s2}$ kept as printed (standing rule 2: the text's $t_1$, $M_s t_1$ are not imposed). Nothing
  added. The scan's specks are not reproduced.
- Geometry: all three panels share one scale (0.85 in per $T_1$, 0.5 in per $M_{s1}$). (b) is $2M_{s1}$ by
  $T_1/2$, so the two rectangles have exactly equal areas. That is what the caption relies on ($M_{s2} > M_{s1}$,
  $T_2 < T_1$, both products $H$). On the scan the ratios are about 2.0-2.06 and 0.51. The impulse in (c) is a
  heavy arrow at $t = 0$ that reaches the top of the axis ("infinity"), as printed.
- Style: `tamr sketch` axes with arrowheads. The pulses and the impulse are the plotted function, drawn in `s1`.
  Panel letters *(a)*, *(b)*, *(c)* use the `panel` style, at the upper right inside each set of axes on one
  baseline, as in approved ch1/fig05.tex. Tick labels are `\footnotesize` ink2. The labels are ink. The width is
  5.91 in, within 6.5 in. Nothing overlaps or is clipped. The $\infty$ is legible at 400 dpi and at the 150 dpi
  compare size.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | The $\infty$ is set like a tick label: `\footnotesize`, ink2, just left of the arrow tip. The scan letters it large, directly above the tip. The meaning is unchanged, and it matches how $M_{s1}$ and $M_{s2}$ (the intensities of (a) and (b)) are set. | fig20.tex:36 | None needed. Optional: put it above the tip (`anchor=south` at `axis cs:0,4.0`) if the owner prefers the printed position. |
| 2 | note | The impulse arrow uses an inline style (`s1`, 1.8 pt, Stealth 8 x 6 pt), not `vec` (1.3 pt, ink). That is right here: it is the plotted forcing function, not a force vector. It is heavier than the 1 pt pulses, as the scan's arrow is. | fig20.tex:34 | Style suggestion only: an `impulse` style in tamrfig.sty if other figures draw impulses (Ch2 Figs 21-23 do not). |

## Verdict

pass (0 must-fix, 0 should-fix)
