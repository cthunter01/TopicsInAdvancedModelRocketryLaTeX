# v2 audit: ch3/fig43 (round 1)

Sources checked: scan `figures/ch3/fig43.png` (zoomed x3, the t and d_m constructions x6); redraw
`figures/v2/ch3/fig43.tex` and its current PDF (5.20 x 2.38 in, fonts embedded, clean log
`build/v2/ch3/fig43.log`), rendered at 400 dpi; `build/v2/png/ch3-fig43-compare.png`; inventory row `ch3-fig43`;
caption and citing text `chapters/ch3-sec6a.tex:55-82` (eqs. (159)-(162)); `corrections/ch3.md` D36 (l_n, l_t
kept as printed); STYLE.md sections 14 and 16; kit `figures/v2/tamrfig.sty` (dimline, dimout, edge fin, leader);
sibling drawings `figures/v2/ch3/fig45.tex`, `fig50.tex` (same notation).

Checks run:
- Overlay: the PDF rendered at 115.45 dpi (1 drawing unit = 1 scan pixel) and registered on the scan by
  cross-correlation (offset 10, 22 px): body, nose, boattail, both fins and the edge-on fin lie on the scan's
  ink (median 0 px); the remaining distance is the dimension rows, drawn about 15 px closer to the body by
  design. The drafter's numbers (95th percentiles 0.5-1.4 px for the outlines) are consistent with this.
- Geometry: nose 92 (tangent ogive), cylinder to 441.5, conical boattail to the base at 484.5, d_b/d_m = 0.77;
  fin root LE 402, tip LE 458.5, span 54, TE square at the base; edge-on pair a white strip from the root LE to
  the base. Matches the scan's stations (nose tip at scan x 44: 136, 485.5, 528.5, LE 446).
- Lettering: ell_n, ell_s, ell_t, ell_b, c_r, c_t, b, d_m, d_b, t all present, italic, upright (none rotated);
  l_n and l_t as printed (D36, as Figure 50). b runs from the root to the tip of one fin, as the caption says.
- Dimensions: chain ell_n / ell_s / ell_t with heads meeting at the shared extension lines, ell_b below; c_r a
  \dimline, c_t and d_m, d_b by arrows from outside (\dimout); b a \dimline with its label in a gap. Legible at
  final size: ell_t (0.95 cm) holds its label and both heads; the b and d_b extension lines (0.9 mm apart, as
  printed) stay distinct.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | should-fix | t is drawn as a plain leader from the strip's lower-left corner to the letter, which reads as "this part is t" rather than "this thickness is t". The 1973 art dimensions the thickness exactly as it dimensions d_m and d_b: a vertical line at scan x 463 from just under the upper body line (y 140) to the lens top, continuing from the lens bottom down to y 216 and a shoulder to the letter t (traced column by column on the scan). The redraw renders d_m and d_b with \dimout; Figure 50 (same notation) renders its t with \dimout too (fig50.tex:48). | fig43.tex:50-51 | Dimension t across the edge-fin strip with \dimout (two dim stubs from outside pointing at y = +2.2 and -2.2) at a station inside the strip, e.g. x about 419 (the printed one), and set t at the lower stub's tail. If the label crowds the lower fin's LE there (LE at y about -34 at x 419), keep the present leader from the lower stub's tail down-left to t. |
| 2 | note | The header comment says the d_m and d_b labels sit "beside the lower arrow's tail, as Figure 45", but Figure 45 puts its d labels beside the upper arrows' tails. Each figure follows its own 1973 art (Fig 43 prints the labels at the lower leaders, Fig 45 at the upper ones), and in Fig 43 the lower side is the right choice for d_b (b crowds the upper side). | fig43.tex:7-8 | Correct the comment ("as printed"), or align the family if the owner wants one placement. |
| 3 | note | The extension line at the boattail joint (x 441.5) runs through the lower fin's interior from y -21.75 to -55.5, as in the 1973 art; it is thin ink2 and does not read as a fin edge. | fig43.tex:32 | none |
| 4 | note | The fin roots run straight at the body radius over the boattail to the base, leaving a thin wedge between root and boattail, as printed (inventory and comment say so). | fig43.tex:25-26 | none |

## Verdict: pass (no must-fix)
