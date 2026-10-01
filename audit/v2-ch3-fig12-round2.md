# v2 audit: ch3/fig12 (round 2)

Sources checked: figures/v2/ch3/fig12.tex, fig12.py, fig12-edge.csv, fig12-eddies.csv, fig12.calib.json and the
PDF (rebuilt with `make fig F=ch3/fig12`: 6.20 x 2.00 in, fonts embedded; rendered at 300 and 600 dpi, and at
1200 dpi around the base); build/v2/png/ch3-fig12-compare.png beside the scan figures/ch3/fig12.png; inventory row
ch3-fig12; caption chapters/ch3-sec3a.tex:36-45 and citing text chapters/ch3-sec2b.tex:429-430; eqs. (54) and
(80); STYLE.md sections 14 and 16; the round-1 audit and the drafter's fix record. I ran the overlay myself.

Round-1 findings:
- Should-fix 1 ($\alpha$ read into "angle of"): fixed. The label's east anchor moved from (-0.5,-0.55) to
  (-0.74,-0.55) (fig12.tex:95). At 600 dpi, "of" ends about 5 mm before $\alpha$, which sits in its white gap on
  the arc, so the label no longer reads "angle of $\alpha$". The label stays to the left of the angle, as in the
  1973 art, and has no leader there either. The width grew to 6.20 in (within 6.5 in). The V-bar line starts at
  x = -0.5, to the right of "attack", so they do not overlap. Resolved. (The comment at fig12.tex:94 says "about
  4 mm", but the measured gap is about 5 mm. This is immaterial.)
- Note 2 (reading of the 1973 lug and vortex; lug moved ahead of the fins): recorded in the drafter's doubts for
  the gate and for the inventory notes. Resolved.
- Note 3 (leaders with heads): recorded in doubts for the consistency pass. Resolved.
- Note 4 (four fins here, three-fin C.P. in Fig 1): recorded in doubts. Resolved.

Checks:
- All 10 callouts, $\alpha$ and $\bar V$ are present with the printed wording. Each leader is straight and ends on
  its subject: the nose outline, the laminar layer, the transition mark (2.90, 0.304), the turbulent layer, the
  upper fin's root leading edge (5.45, 0.2), the tip vortex, the lower surface (3.6, -0.2), the lug (4.6, -0.27)
  and the base bubble.
- Boundary layer: laminar $0.0611\sqrt{x}$ = 0.1040 and turbulent $0.0803(x-1.519)^{0.8}$ = 0.1040 at transition,
  so the edge is continuous. Overlay of the edges from x = 1.2 to the base: upper 95% 1.0 px, lower 95% 2.0 px
  (max 2.8 px), ok. With the wake, the upper edge is 95% 1.0 px, max 10 px at the freehand 1973 wake.
- $\alpha$: the arc is centred at (5.8, 0), on the extension of $\bar V$. Its ends land on the axis extension
  (-0.4, 0) and on $\bar V$ (-0.306, -1.077), where the line's y is -1.0767.
- Flat fills only: white fins and body over the `wash`. The tip vortex starts at the upper fin's tip trailing edge
  (6.4, 0.8) and stays clear of the wake edge (at most 0.58 there).

## Findings
| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | should-fix | The centre line is drawn to x = 6.45, past the base at x = 6.4. A dash about 0.4 mm long shows outside the base line, inside the base bubble (seen at 600 and 1200 dpi). Figs 1 and 10 end their centre lines at 6.3, 0.1 inside the base. | fig12.tex:67 | Use `\draw[centerline] (0.1,0) -- (6.3,0);`. The edge-on fin (white, from 5.45) already hides the centre line's aft part, so nothing else changes. |
| 2 | note | All round-1 findings are fixed or carried into doubts. The should-fix moved the label with no regression. | fig12.tex:94-95 | None. |

## Verdict: pass (no must-fix)
