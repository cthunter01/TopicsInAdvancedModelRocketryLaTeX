# v2 audit: ch2/fig42 (round 1)

Sources checked: scan `figures/ch2/fig42.png` (3x upscale; 7x crops with pixel rulers of the nose and shoulder,
of the $r_o$/$r_i$/$r_t$/$s$ region and of the "Planform ... $A_f$" lettering; a 12x glyph comparison of the
$A$ subscript against the $t$ of $c_t$ and the $f$ of "fin"); redraw `figures/v2/ch2/fig42.pdf` (400 dpi
render, crops of the left end and of the right-hand dimensions) and `build/v2/png/ch2-fig42-compare.png`; build
log `build/v2/ch2/fig42.log` (no warnings); `pdfinfo`/`pdffonts` (350.7 x 169.1 pt = 4.87 in wide, all fonts
embedded); source `figures/v2/ch2/fig42.tex`; inventory row `ch2-fig42`; `chapters/ch2-sec4.tex`:812-890
(eqs. (105a), (105b), (106), (107), (108a), (108b), the fin symbol list, the citing sentence and the caption);
STYLE.md sections 13 and 16; `corrections/v2-figures.md` (standing rule 2); the approved `figures/v2/ch2/fig39.tex`.

Checks made:
- **Stations** (scan pixels from the nose tip at scan x = 28, against the redraw):
  - nose 0-57 / 0-54, drawn as an exact half-ellipse (the caption's ellipsoidal nosecone, blunt tip);
  - shoulder 57-75 / 54-73;
  - tube 130-480 / 128-478;
  - fin root leading edge 405 / 404, tip leading edge 452 / 449.5, trailing edge 480 / 478;
  - span 57.7 / 58.5;
  - the $R$ dimension lines at 83 and 101 / 83 and 101.
- **Geometry.**
  - The shoulder's radius equals the tube's inner radius (11), so the "R of solid cylinder" also matches the
    bore.
  - The fin root is on the tube's outer surface, so $r_t$ = $r_o$ = 13.5. This matches the text's "radius of
    fin root from rocket centerline".
  - The tip trailing edge is flush with the aft end.
  - There is an exploded gap between the shoulder and the tube, as the family note asks.
- **Dimensions.**
  - "R of ellipsoidal nose" and "R of solid cylinder" have their arrows outside. The upper dimension line is
    carried up to its name, as printed.
  - $r_o$ and $r_i$ run from the centre line to the outer wall and the bore, arrows outside, labels rotated, in
    the printed order.
  - $r_t$ runs from the centre line to the fin root, arrows outside, with the label below.
  - $s$ runs from the root to the tip, label rotated in the gap.
  - $c_t$ has its arrows outside and the label between them. $c_r$ has its label in the gap.
  - The extension lines are at the tip leading edge, the trailing edge and the root leading edge.
- **Lettering.**
  - All ten inventory items are present.
  - $r_o$, $r_i$ stay lowercase as printed (rule 2; eq. (105b) has $R_o$, $R_i$).
  - $A_f$: the inventory flags the subscript as faint (f or t). At 12x its hook is at the top, like the f of
    "fin". The t of $c_t$ and $r_t$ hooks at the bottom. So the printed letter is f, which agrees with eq. (108a);
    $A_f$ is correct and needs no rule-2 entry.
- **Caption.** The ellipsoidal nosecone, the solid cylinder (shoulder) and the hollow cylinder (body tube) are
  shown. Two of the "set of four fins" appear in profile, as in 1973's side view.
- **Legibility.**
  - Nothing is clipped. Width is within 6.5 in.
  - The "Planform" leader ends inside the upper fin at (466, 32), crossing the trailing edge as in 1973. It
    clears the third line of the label and the $r_o$/$r_i$ labels.
  - The 2.5-unit (0.5 mm) spacing of the nose-radius and shoulder-radius extension lines, and of the $r_o$/$r_i$
    extension lines, separates cleanly in the 400 dpi render.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | The lower $r_o$ and $r_i$ arrows start at y = -12. That is only 1.5 units (0.3 mm) above the $r_t$/$s$ extension line at y = -13.5, which passes beneath them, so they look as if they spring from the tube's lower surface. The upper arrows define the dimensions unambiguously, and 1973 has the same arrangement. | fig42.tex:50-51 | Optional: start the two lower arrows at y = -10 to leave a visible gap above the extension line. |
| 2 | note | `hidden` and `dim arrow` repeat the Fig 41 local definitions. | fig42.tex:11-14 | Style suggestion (with Fig 41): move `hidden` and an outside-arrow dimension helper into `tamrfig.sty`. |

## Verdict: pass

No must-fix or should-fix items. Geometry, dimensions and lettering match the scan, the inventory, eqs.
(105)-(108) and the caption. The $A_f$ reading is confirmed against the scan's glyphs.
