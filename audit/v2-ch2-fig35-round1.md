# v2 audit: ch2/fig35 (round 1)

Sources checked: figures/ch2/fig35.png (scan, upscaled 2x); figures/v2/ch2/fig35.pdf (rendered 400 dpi; 259.2 x
185.8 pt = 3.60 in wide, fonts embedded, PDF newer than its .tex); build/v2/png/ch2-fig35-compare.png;
figures/v2/ch2/fig35.tex:1-36; figures/v2/inventory.csv row ch2-fig35; caption chapters/ch2-sec4.tex:289-293,
citing text and eqs. (83), (84) ch2-sec4.tex:266-284 ("r_2 is smaller than r_1", 276-277) and the v1 editor's note
ch2-sec4.tex:238-252; corrections/v2-figures.md (gate item "Ch2 Figs 34, 35"); STYLE.md sections 13 and 16;
tamrfig.sty; approved fig39.tex (`\CP$_{CB}$`, `\bar{Z}_{CB}`); the companion figures/v2/ch2/fig34.tex.

Checked and correct:
- Geometry: conical boattail, nose direction up, large forward end r_1 = 148 at Z_1, small aft end r_2 = 93 a
  length L = 220 behind it (scan: L about 224 px, r_1 about 150, r_2 about 94; r_2/r_1 = 0.628), so r_2 < r_1 as
  the text requires; symmetric about the centre line; the Fig 34 frustum turned end for end; scale 1.16 x printed.
- C.P. placed by eq. (84), the owner's preference over the 1973 placement: Z_CB - Z_1 = (L/3)[1 + (0.6284)(1.6284)]
  = 0.6744 L = 148.4 units; measured on the 400 dpi render (Z_1 row 175, aft end 856, C.P. 635): 0.675 L. This is
  the volume-over-base-area rule measured aft from the forward (largest) end, and the mirror of Fig 34's 0.326 L
  (0.326 + 0.674 = 1), so the two figures agree with each other. (The 1973 mark sits at about 0.43 L.)
- Lettering complete and as printed: Z_1 and \bar{Z}_{CB} at the left ends of their station lines, C.P.$_{CB}$ to
  the right of the mark (clear of the outline: label ends at about x = 70, the side is at x = 111), r_1 above from
  the centre line to the forward corner, r_2 below to the aft corner, L at the right. Notation as Fig 39 and the
  caption. Nothing added.
- House style identical to Fig 34 (centre line first, outline over it, extension gaps, labels in dimension gaps);
  no overlaps, arrowheads visible, width well under 6.5 in.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | As for Fig 34: the C.P. moves from the drawn 0.43 L to 0.674 L behind Z_1 (eq. (84)); the "Ch2 Figs 34, 35" gate entry in corrections/v2-figures.md is still open and should record the placement used. | corrections/v2-figures.md (gate item); fig35.tex:5-7 | For the lead: update the gate entry (outside this figure's files). |

## Verdict

pass (0 must-fix, 0 should-fix)
