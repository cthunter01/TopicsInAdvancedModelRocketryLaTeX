# v2 audit: ch3/fig13 (round 2)

Sources checked: figures/v2/ch3/fig13.tex, fig13.py, fig13-edge.csv, fig13-p1/p2/p3.csv, fig13-arrows.csv,
fig13.calib.json and the PDF (rebuilt with `make fig F=ch3/fig13`: 5.45 x 2.06 in, fonts embedded; rendered at
300 dpi); build/v2/png/ch3-fig13-compare.png beside the scan figures/ch3/fig13.png; inventory row ch3-fig13;
caption and citing text chapters/ch3-sec3a.tex:206-224; Table 1 and eq. (54); STYLE.md sections 14 and 16; the
round-1 audit and the drafter's fix record. I ran the overlays myself and looked at the overlay image.

Round-1 findings:
- Must-fix 1 (knees off the edge): fixed. fig13.py:146-156 scales each station's profile and its arrows with
  $\delta(x_s + U_\infty)$: 62.6, 95.7 and 119.8 px. Check: at $y = \delta$ the profile reaches
  $u = 0.9915\,U_\infty$ = 75.36 px, where the edge stands at 62.42, 95.56 and 119.73 px, so each knee lies on the
  dashed edge within 0.2 px. This is visible on the 300 dpi render. Overlay of the profiles on the 1973 profiles:
  p1 95% 2.24 px (max 3.00), p2 2.83 px (max 2.83), p3 2.24 px (max 2.83). All ok, against 9.0, 7.6 and 5.4 px
  before the fix. The profiles are still one function of $y/\delta$, as the text (ch3-sec3a.tex:208-216) says. The
  $u(x,y)$ label at x = 118 stays clear of profile 1.
- Should-fix 2 (edge mismatch to be logged): done. The overlay numbers (95% 8.95 px, max 20.8 px) and the 1973
  edge's flattening (c = 6.07, 5.66, 5.37) are in the drafter's doubts for the Minor list. My overlay of the edge
  gives the same numbers (mean 3.58 px, 95% 8.95 px, max 20.81 px). The fig13.py docstring (lines 68-73) and the
  fig13.tex header (lines 4-10) now say that c only sets the scale and that the 1973 edge departs from the sqrt
  law. Resolved.
- Note 3 (dashed `guide` edge against the 1973 dash-dot): in doubts for the gate. Resolved.
- Note 4 (helpers duplicated in Fig 10): in style_suggestions. Resolved.

Checks:
- Lettering complete and as printed: $U_\infty$ over the upstream profile and over the second boundary-layer
  profile; $y$; $x$ on the L-shaped arrow; $u(x,y)$; $\delta(x)$ upright in the gap of a `\dimline` ending at
  102.2. The edge at x = 305.5 is $\delta$ = 102.25.
- Blasius values, checked independently by linear interpolation of Table 1. Station 1, y = 10: 20.087 (CSV
  20.087). Station 2, y = 56.67: 63.79 (CSV 63.82). Station 3, y = 38.0: 38.946 (CSV 38.952). The differences are
  Hermite against linear interpolation only.
- 16 rows at each of the four stations, the open circle at the leading edge, and 45-deg `hatch` under the plate.
  Arrowheads are visible at the 2.2 mm spacing. Nothing is clipped, and the width is within 6.5 in.

## Findings
| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | Must-fix 1 is fixed and verified: the knees are on the edge within 0.2 px, and the profile overlays are 95% 2.2-2.8 px. Should-fix 2 and the notes are carried into doubts and the comments. | fig13.py:146-156; fig13.tex:4-10 | None. |
| 2 | note | The edge stays a recorded mismatch against the 1973 dash-dot (95% 8.95 px). This is the approved computed curve, logged in doubts for the Minor list of corrections/v2-figures.md. | fig13-edge.csv | None (gate item). |

## Verdict: pass (no must-fix)
