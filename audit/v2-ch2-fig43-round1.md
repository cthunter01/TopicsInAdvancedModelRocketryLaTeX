# v2 audit: ch2/fig43 (round 1)

Sources checked: the scan `figures/ch2/fig43.png` (zoomed 3x and 7x at the clamps, the tape bands and the tail T);
the redraw `figures/v2/ch2/fig43.tex` / `.pdf` (rendered at 400 and 800 dpi; `build/v2/png/ch2-fig43-compare.png`);
inventory row `ch2-fig43`; caption and citing text `chapters/ch2-sec5.tex:40-65, 83, 113, 135-150`
(Illustration A/B, eqs. (110)-(112)); `backmatter/figure-credits.tex:114`; STYLE.md section 16;
`corrections/v2-figures.md` standing rule 2; `figures/v2/tamrfig.sty`; `figures/v2/ch2/fig50.tex` (the other
circled-letter figure); the approved 3D example `figures/v2/ch2/fig03.tex`.

Size and fonts: 328.0 x 429.0 pt (4.56 x 5.96 in), within 6.5 in; one font (TeXGyreTermesX-Italic), embedded.

Checked and correct:
- Content: both panels, each with the overhanging two-by-four (cut by the panel edge), the C-clamp with its
  knurled, threaded screw and swivel pad, the upper "T" (heavy music-wire crossbar overhanging the beam's end),
  the torsion wire, and the rocket (ogive nose, tube, four fins, engine ring). No lettering other than the two
  circled letters, as printed; circled lowercase kept (standing rule 2; the text's "43A"/"43B" unchanged),
  at the lower right of each panel on one baseline (y = -644 in both), the same local `circled` style as
  Ch2 Fig 50.
- Projection: x -> (a, -a sin 32), y -> (a, a sin 32), z -> (0, a cos 32 / cos 45) is a true orthographic view
  at elevation 32, azimuth 45 (screen right and up vectors orthonormal), the house view of Ch2 Fig 3; viewer at
  (+x, -y, +z), so `\blk` correctly paints the +x, -y, +z faces; cylinder silhouettes at 48.5 deg (along x) and
  45/225 deg (along z) are the correct tangent angles; front/back fin split correct in both panels.
- Text: the wire hangs from the centre of the upper T's crossbar (crossbar x = -30..44, wire at x = 7, as
  "bent over the center of a two-inch length"); (a) the rocket is horizontal and parallel to the beam, hung
  between two tape bands at 0.68 of its length from the nose (scan: 0.69); (b) the rocket hangs vertically,
  nose down, from the lower T across the tail, the T's ends taped to two opposite fins (fins 0 and 180 deg,
  the crossbar along the same direction), as in the scan. The rod "as in Figure 43A" reads correctly.
- Hidden lines: beam end face over the clamp's lower part; clamp top re-painted over the beam; wire visible
  in front of the beam's end face (it hangs 7 units beyond it, as printed); tape on the back fin in (b) is not
  occluded by the front fins (checked: the front fin would need s > L).

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | should-fix | The separating rule is half covered by panel (b)'s beam: the (b) beam is clipped at screen x = -134 + 318 = 184, exactly the rule's centre line, and its white face fills are painted after the rule, so over the beam's height (about 0.6 in) the 0.5pt rule shows only 0.25pt (measured on the 800 dpi render: columns right of centre lose about 465 rows). | `fig43.tex:100` (rule drawn before panel (b)); `:103` (`\apparatus{-134}{152.4}`) | Draw the rule after the (b) scope (move line 100 below line 114), or clip (b) at -133.5 (the rule's half-width, 0.25pt, is 0.47 units) so the fill stops at the rule's right edge. |
| 2 | note | The printed heavy double rule between the panels is a single 0.5pt `ink2` rule. A reasonable part of the modern restyle; the panels stay clearly separated. | `fig43.tex:100` | None needed. |
| 3 | note | In (a) the lower T itself is not drawn (it lies under the tape bands); the wire meets the body between the bands, as in the scan, where only a slightly heavier top line shows between the bands. | `fig43.tex:92-97` | None needed. |
| 4 | note | The clamp's swivel pad sits directly under the upper arm (pad top z = 35.8, arm bottom z = 40) with no screw shank showing between them; the scan shows a short shank. Unlabelled detail. | `fig43.tex:77-80` | Optional. |
| 5 | note | Style suggestion: Figs 43 and 50 define the same local `circled` style (circle 0.5pt, 12.5pt, `\small\itshape`); worth promoting to `tamrfig.sty` as a "circled panel" style if more figures need it. | `fig43.tex:88-89`, `fig50.tex:21` | For the style owner. |

## Verdict: pass (no must-fix)
