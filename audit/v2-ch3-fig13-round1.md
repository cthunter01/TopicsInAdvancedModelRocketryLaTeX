# v2 audit: ch3/fig13 (round 1)

Sources checked: figures/v2/ch3/fig13.tex, fig13.py, fig13-edge.csv, fig13-p1/p2/p3.csv, fig13-arrows.csv,
fig13.calib.json and the PDF (rendered at 300 and 600 dpi; `make fig F=ch3/fig13`: 5.45 x 2.06 in, fonts embedded);
the scan figures/ch3/fig13.png (zoomed 2x); inventory row ch3-fig13; caption and citing text
chapters/ch3-sec3a.tex:206-224; Table 1 (chapters/ch3-sec3a.tex:397-454) and eq. (54); STYLE.md sections 14 and
16; tamrfig.sty (`\dimline`, `guide`, `hatch`, `open point`, `thin vec`). I ran the overlays myself, including a
test of the fix proposed below (scratch only).

Checks that passed:
- Lettering complete and as printed: $U_\infty$ over the upstream profile and over the second boundary-layer
  profile; $y$ (axis up from the leading edge); $x$ (the L-shaped arrow under the plate); $u(x,y)$ beside the first
  profile; $\delta(x)$ upright in the gap of a `\dimline` from the plate to the edge at the scan's station
  (x = 305.5; the dimension ends at 102.2 and $\delta(305.5) = 102.25$).
- The upstream uniform profile and three developing profiles, 16 rows each (y = 10 to 150), at the scan's stations
  and arrow length; the open circle at the leading edge; the plate hatched below at 45 deg (`hatch`).
- Computation: Blasius $u/U_\infty = f'(5y/\delta)$ from Table 1 (all 45 rows parsed; Hermite with $f''$). Spot
  check at station 2: $\delta = 80.95$, row y = 19.33, $\eta = 1.194$, $f' = 0.3919$, so u = 29.79 (CSV 29.785).
  The edge is eq. (54)'s $\sqrt{x}$ law with c = 5.85.
- Legibility: nothing clipped; arrowheads are visible at the 2.2 mm row spacing; width within 6.5 in. Local helpers
  have new names. Their style matches Fig 10 (`profile arrow`, `profile line`, dashed boundary-layer edge).

## Findings
| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | must-fix | Each profile is scaled with $\delta$ taken at its base line ($\delta(x_s)$ = 36.3, 81.0, 108.4 px). Its knee, where it reaches $U_\infty$, is drawn on the tip line at $x_s + 76$, where the dashed edge stands at $\delta(x_s+76)$ = 62.6, 95.7, 119.8 px. The edge therefore passes 26.3, 14.7 and 11.4 px above the knees (6.2, 3.5 and 2.7 mm at final size). Full-length arrows of profile 1 lie well below the drawn edge, as if inside the boundary layer, and the similarity in $y/\delta$ the text relies on (ch3-sec3a.tex:208-216) is not visible. The 1973 art draws the edge through the knees. Overlay of the computed profiles on the 1973 profiles: 95% 9.6, 7.7, 5.4 px (MISMATCH). | fig13.py:78-88 | In fig13.py use `d = delta(xs + U)` for each station, for both the profile line and its arrows. The profiles stay similar (one function of $y/\delta$), eq. (54) and the edge are unchanged, and the edge then meets each knee on its tip line. Tested: the overlay becomes 95% 2.2, 2.8, 2.2 px (max 3.2 px), all ok. The $u(x,y)$ label at x = 118 stays clear (profile 1 at y = 27 is then at x of about 89.5). Update the comments in fig13.py and fig13.tex to match. |
| 2 | should-fix | The edge computed from eq. (54) (c = 5.85) departs from the 1973 dash-dot edge: overlay 95% 8.95 px (1.5 mm), max 20.8 px. The sqrt law sits above the 1973 edge near the leading edge and beyond the third profile, because the 1973 edge flattens (through its knees, c = 6.07, 5.66, 5.37 at x = 114.5, 267.5, 419.5). Computing it is approved, but STYLE s.16 requires a mismatch over 3 px to be logged. | fig13.py:7-9, 31 | Report the overlay numbers in the drafter's doubts for the Minor list of corrections/v2-figures.md (and correct the docstring's implication that the sqrt fit matches the 1973 edge). |
| 3 | note | The edge is a dashed `guide`, where the 1973 art and the family notes have dash-dot. No text names the style, the house dash-dot means a centre line, and the choice matches Fig 10's dashed boundary-layer edge. | fig13.tex:48 | None; mention it in doubts for the gate. |
| 4 | note | `\csvline`, `\csvarrows`, `profile arrow` and `profile line` duplicate Fig 10's word for word. | fig13.tex:11-35 | Kit candidate (style_suggestions). |

## Verdict: fix
