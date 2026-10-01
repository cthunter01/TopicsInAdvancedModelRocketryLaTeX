# v2 audit: ch2/fig34 (round 1)

Sources checked: figures/ch2/fig34.png (scan, upscaled 2x); figures/v2/ch2/fig34.pdf (rendered 400 dpi; 258.4 x
185.8 pt = 3.59 in wide, fonts embedded, PDF newer than its .tex); build/v2/png/ch2-fig34-compare.png;
figures/v2/ch2/fig34.tex:1-35; figures/v2/inventory.csv row ch2-fig34; caption chapters/ch2-sec4.tex:260-264,
citing text and eqs. (81), (82) with the v1 editor's note ch2-sec4.tex:229-257; corrections/v2-figures.md (gate
item "Ch2 Figs 34, 35"); STYLE.md sections 13 and 16; tamrfig.sty; approved fig39.tex (`\CP$_{CS}$`,
`\bar{Z}_{CS}`); the companion figures/v2/ch2/fig35.tex.

Checked and correct:
- Geometry: conical shoulder, nose direction up, small forward end r_1 = 93 at Z_1, large aft end r_2 = 148 a
  length L = 220 behind it (scan: L 219 px, r_1 about 94, r_2 about 148; r_1/r_2 = 0.628 as printed), drawn
  symmetric about the centre line (the 1973 outline is a few pixels lopsided); the same frustum as Fig 35 turned
  end for end; scale 1.16 x printed, as Figs 33 and 35.
- C.P. placed by eq. (82), the owner's preference over the 1973 placement: Z_CS - Z_1 = L [2/3 - (1/3)(0.6284)
  (1.6284)] = 0.3256 L = 71.6 units; measured on the 400 dpi render (Z_1 row 175, aft end 856, C.P. 397): 0.326 L.
  The volume-over-base-area rule of ch2-sec4.tex:194-201 applied to the frustum gives the same expression, so the
  redraw agrees with the text's rule and eq. (82). (The 1973 mark sits at about 0.58 L.)
- Lettering complete and as printed: Z_1 and \bar{Z}_{CS} at the left ends of their station lines (the Z_1 line
  runs through the forward end and on to the right as the upper L extension, the \bar{Z}_{CS} line crosses the
  outline and stops at the C.P. mark), C.P.$_{CS}$ to the right of the mark (clear of the outline: label ends at
  about x = 70, the side is at x = 111), r_1 dimensioned above from the centre line to the forward corner, r_2
  below to the aft corner, L at the right between the two ends. Notation as Fig 39 and the caption (\bar{Z}_{CS},
  uppercase CS). Nothing added.
- House style: centre line drawn first and dash-dot past both ends (serving as the inner extension of r_1 and r_2),
  outline 0.6pt over it, extension lines with small gaps at the corners, labels in dimension gaps, arrowheads
  visible, no overlaps, width well under 6.5 in.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | The C.P. is now at 0.326 L behind Z_1 (eq. (82)) where the 1973 drawing has about 0.58 L. corrections/v2-figures.md still lists "Ch2 Figs 34, 35" as an open gate item ("Keep as drawn or place by the equations"); the entry should record that the redraw places the marks by eqs. (82)/(84) at 0.326 L and 0.674 L for a radius ratio 0.628. | corrections/v2-figures.md (gate item); fig34.tex:5-6 | For the lead: update the gate entry with the positions used (outside this figure's files). |

## Verdict

pass (0 must-fix, 0 should-fix)
