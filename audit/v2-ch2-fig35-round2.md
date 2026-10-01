# v2 audit: ch2/fig35 (round 2)

Sources checked: figures/ch2/fig35.png (scan); figures/v2/ch2/fig35.pdf (rendered at 400 and 1200 dpi;
259.243 x 185.785 pt = 3.60 in wide, fonts embedded; PDF 17:45:30 is newer than fig35.tex 17:45:29, and neither has
changed since round 1); figures/v2/ch2/fig35.tex:1-35; the round-1 report audit/v2-ch2-fig35-round1.md and the
round-1 fix record; figures/v2/inventory.csv row ch2-fig35; caption chapters/ch2-sec4.tex:288-294; eqs. (83),
(84) with "r_2 is smaller than r_1" (ch2-sec4.tex:266-284) and the v1 editor's note (238-252);
corrections/v2-figures.md:64-65; STYLE.md sections 13 and 16; tamrfig.sty; approved fig39.tex; the companion
fig34.tex.

Round-1 finding checked:
- Round 1, item 1 (note for the lead: record the placement in the gate entry): **still open, outside this
  figure**. corrections/v2-figures.md:64-65 is unchanged. The value to record is Z_CB = Z_1 + 0.674 L at
  r_2/r_1 = 93/148.

Checks (all pass, no regressions):
- C.P. by eq. (84): with r_2/r_1 = 0.62838, (1/3)[1 + (0.62838)(1.62838)] = 0.67441, so the mark sits 148.4 units
  behind Z_1. On the 1200 dpi render (Z_1 row 521, aft end row 2575, mark row 1905) it measures 0.6738 L. This
  mirrors Fig 34's 0.3262 L, and the two sum to 1. The 1973 mark sits at about 0.42 L.
- Geometry: the conical boattail points up, with the large forward end r_1 = 148 at Z_1 and the small aft end
  r_2 = 93. So r_2 < r_1, as the text requires. It is Fig 34's frustum turned end for end, at the same scale, and
  the centre line is drawn first (fig35.tex:18).
- Lettering: Z_1, $\bar{Z}_{CB}$, C.P.$_{CB}$, r_1, r_2 and L are all present, in the notation of the caption
  and Fig 39. Nothing is added. The labels are clear of the outline and the arrowheads are visible. The width is
  3.60 in.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | As for Fig 34: the corrections gate entry for Figs 34 and 35 still does not record the equation placement (0.674 L here). This is a lead action outside the figure files. | corrections/v2-figures.md:64-65 | For the lead: close the gate entry with the positions used. |
| 2 | note | The $\bar{Z}_{CB}$ station line stops 5.7 units (3.2 pt) from the mark's centre, leaving a hairline gap of about 0.1 mm before the mark's edge. In Fig 33 and the approved Fig 39 the line touches the mark. The gap is barely visible at print size. | fig35.tex:22 (`-- (-5.7,-\zcp)`) | Optional: end the line at `(-5.2,-\zcp)` (2.9 pt), the same change as in Fig 34. |

## Verdict: pass (0 must-fix, 0 should-fix)
