# v2 audit: ch3/fig01 (round 1)

Sources checked: figures/v2/ch3/fig01.tex and .pdf (rendered at 300 and 600 dpi; `make fig F=ch3/fig01`: 3.79 x 3.52 in,
fonts embedded); the scan figures/ch3/fig01.png (zoomed 2x); inventory row ch3-fig01; caption and citing text
chapters/ch3-intro-sec2a.tex:140-168; STYLE.md sections 14 and 16; tamrfig.sty (`model` rocket, `\anglemark`, cg/cp
marks); the approved Ch1 Fig 6 (figures/v2/ch1/fig06.tex) for the shared rocket conventions; Barrowman's C.P.
recomputed by hand for the drawn rocket.

Checks that passed:
- Lettering complete and as printed: $\bar V$, $\alpha$, C.G. (`\CG`, quartered-circle `cg mark`), C.P. (`\CP`,
  `cp mark`), $\bar D$; the list heading "Drag is determined by:" with its rule, and the eight bullet items in the
  printed order and wording, "angle of attack ($\alpha$)" included. Overbars kept (rule 2; STYLE s.14: no arrow is
  lettered).
- Geometry: axis 52 deg and alpha 23 deg match the scan (measured 51.7 deg and about 22 deg); $\bar V$ starts at the
  C.G., $\bar D$ at the C.P. and is exactly opposite $\bar V$, as the definition in the text requires (drag acts
  against the motion and is taken at the C.P., ch3-intro-sec2a.tex:140-157); C.P. aft of C.G.
- C.P. placement: Barrowman for the `model` rocket with three fins (ogive nose $C_{N\alpha}=2$ at 0.466 x 1.2 = 0.559;
  fins: $l_m = \sqrt{0.6^2+0.25^2} = 0.65$, $C_{N\alpha} = 1.25 \cdot 27/(1+\sqrt{1+(1.3/1.4)^2}) = 14.27$ at
  5.853) gives $\bar Z = 5.202 = 0.813L$, as the comment says (four fins: 0.836 L, also as stated).
- Axis drawn as Ch1 Figs 6-8 (thin solid extension beyond nose and tail, dash-dot centre line inside the body).
- Legibility: nothing clipped; C.G. and C.P. labels clear of the body outline by about 1.2 and 1.0 mm; arrowheads
  clear; width within 6.5 in.

## Findings
| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | The C.P. is computed for a three-fin rocket (0.813 L), but the pic is the kit's two-fin profile (`fins=2`: no edge-on fin), and Fig 12 of this family draws the rocket with four fins (two in profile, one edge-on on the axis), for which the C.P. would be at 0.836 L (1.8 mm further aft at final size). Nothing in the book fixes the fin count. | fig01.tex:9-11, 19, 23 | Say in the drafter's doubts that Fig 1 assumes three fins (matching the 1973 position) so the gate sees it; no change needed otherwise. |
| 2 | note | The angle of attack uses `\anglemark` (two heads, $\alpha$ in a white gap), where the approved Ch1 Fig 6 uses `angle arc` with $\alpha$ beside the arc. It is consistent with Fig 12 of this family, and the kit allows `\anglemark` in plane drawings. | fig01.tex:28 | None; check it in the chapter consistency pass. |
| 3 | note | The two 1973 lines have no heads and are drawn as house `vec` vectors, with the overbar lettering kept. The text names no line style, so this is fine. | fig01.tex:25-26 | None. |

## Verdict: pass (no must-fix)
