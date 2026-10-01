# v2 audit: ch2/fig34 (round 2)

Sources checked: figures/ch2/fig34.png (scan); figures/v2/ch2/fig34.pdf (rendered at 400 and 1200 dpi;
258.36 x 185.785 pt = 3.59 in wide, fonts embedded; PDF 17:45:29 is newer than fig34.tex 17:45:14, and neither has
changed since round 1); figures/v2/ch2/fig34.tex:1-34; the round-1 report audit/v2-ch2-fig34-round1.md and the
round-1 fix record; figures/v2/inventory.csv row ch2-fig34; caption chapters/ch2-sec4.tex:259-265; eqs. (81),
(82) and the v1 editor's note, ch2-sec4.tex:229-257; corrections/v2-figures.md:64-65 (gate item "Ch2 Figs 34,
35"); STYLE.md sections 13 and 16; tamrfig.sty (`cp mark`: 5pt, 0.5pt stroke); approved fig39.tex; the companion
fig35.tex.

Round-1 finding checked:
- Round 1, item 1 (note for the lead: record the placement in the gate entry): **still open, outside this
  figure**. corrections/v2-figures.md:64-65 still reads "Keep as drawn (illustrative) or place by the equations.
  **gate**". The figure files correctly leave this to the lead. The value to record is unchanged:
  Z_CS = Z_1 + 0.326 L at r_1/r_2 = 93/148.

Checks (all pass, no regressions):
- C.P. by eq. (82): with r_1/r_2 = 0.62838, 2/3 - (1/3)(0.62838)(1.62838) = 0.32559, so the mark sits 71.6
  units behind Z_1. On the 1200 dpi render (Z_1 row 521, aft end row 2575, mark row 1191) it measures
  0.3262 L. The 1973 mark sits at about 0.58 L.
- Geometry: the conical shoulder points up, with the small forward end r_1 = 93 at Z_1 and the large aft end
  r_2 = 148 a length L = 220 behind it. It is symmetric about the centre line, and the centre line is drawn first
  (fig34.tex:17).
- Lettering: Z_1, $\bar{Z}_{CS}$, C.P.$_{CS}$, r_1, r_2 and L are all present, in the notation of the caption
  and Fig 39. Nothing is added. The labels are clear of the outline and the arrowheads are visible. The width is
  3.59 in.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | The corrections gate entry for Figs 34 and 35 still does not record that the marks are placed by eqs. (82)/(84) (0.326 L here, 0.674 L in Fig 35). This is a lead action outside the figure files, carried over from round 1. | corrections/v2-figures.md:64-65 | For the lead: close the gate entry with the positions used. |
| 2 | note | The $\bar{Z}_{CS}$ station line stops 5.7 units (3.2 pt) from the mark's centre. That leaves a hairline gap (about 0.1 mm, 4-5 px at 1200 dpi) before the mark's 2.75 pt outer edge. In Fig 33 and in the approved Fig 39 (`shorten <=2.9pt`) the line touches the mark. The gap is barely visible at print size. Fig 35 has the same gap. | fig34.tex:21 (`-- (-5.7,-\zcp)`) | Optional: end the line at `(-5.2,-\zcp)` (2.9 pt), the same change as in Fig 35. |

## Verdict: pass (0 must-fix, 0 should-fix)
