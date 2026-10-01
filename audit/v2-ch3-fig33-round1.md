# v2 audit: ch3/fig33 (round 1)

Sources checked: scan `figures/ch3/fig33.png` (zoomed 4x: joint, boattail, base region, velocity profile, break);
inventory row `ch3-fig33`; caption and citing text `chapters/ch3-sec4b.tex:399-417, 474-476, 516-523`; STYLE.md
sections 14 and 16; `figures/v2/tamrfig.sty`; redraw `figures/v2/ch3/fig33.tex` / `.pdf`, rebuilt with
`make fig F=ch3/fig33` (4.76 x 2.96 in) and rendered at 400 dpi; an independent overlay of the redraw on the scan
(the PDF rendered at 119.8 dpi, i.e. one drawing unit per scan pixel, best shift searched).

Checked and correct:
- Lettering: $\epsilon$ (upper side, arrows from outside onto the extension line and the boattail surface),
  $\delta$ (lower side, dimension from the boattail surface to the outer boundary-layer line, label upright in the
  gap), $p_b$ in each loop (lowercase per STYLE s14), R (curve tag: the caption cites "point R"). Nothing missing,
  nothing added.
- Geometry measured on the scan and reproduced: tube radius 53, boattail joint x = 125, flat base x = 277 with radius
  40 (scan: joint 124.5, base 276, radii 53/40), so $\epsilon$ = atan(13/152) = 4.9 deg, inside the text's
  "about 5 or 10 degrees". The $\delta$ dimension ends on both lines (body at y = 42.14 exact; outer line about
  73.9 at x = 252). The boundary layer is 28.8 thick at the joint and 31.8 at $\delta$: it thickens over the
  boattail as the caption says. The dividing streamlines run from the base corners to R on the axis; the loops are
  closed, without arrowheads (as printed; the caption claims no sense of rotation).
- Velocity profile at x = 325: the station line spans the shear layer from the dividing streamline (y = 33.6) to the
  outer edge (64.4); the curve ends on the outer edge at x = 361 (outer line 58.2 there); three velocity lines, as
  printed.
- Fins: leading edge from the tube at x = 52, tip chord 277-417 at r = 177, trailing edge to the base corner, crossing
  the flow lines as printed; the trailing edge passes left of the velocity profile, as in the scan.
- Overlay: 95.2% of the redraw's ink within 3 px of the scan's ink at the best shift (the drafter's 95.3%); the misses
  are the lettering, the circled R and the break line.
- Kit only: `outline`, `thin line`, `hair`, `centerline`, `extension`, `angle arc single`, `\dimline`,
  `\breakline`, `curve tag`; no local styles. No overlaps, nothing clipped; arrowheads of $\epsilon$ and $\delta$
  visible at final size.

## Findings

| # | severity | finding | where | suggested fix |
|---|---|---|---|---|
| 1 | note | The 1973 hatched S-break of a solid bar is drawn as the house zigzag `\breakline` (allowed by the family notes and the house rule for a broken-off tube). | fig33.tex:34-35 | none |
| 2 | note | The three velocity lines of the profile are drawn axial (horizontal); in the scan they lean slightly, about parallel to the outer flow line. The inventory calls them horizontal; the meaning (a velocity profile across the shear layer) is unchanged. | fig33.tex:51-52 | none |
| 3 | note | The circled R sits with its centre 22 units (4.7 mm) from the convergence point (462, 0); the 1973 plain R is about 12 units away. The larger circle accounts for it, and the tag reads clearly as belonging to the point. | fig33.tex:54 | optional: (474, 12) |
| 4 | note | The flow lines start at x = 14 and the centre line at x = 0, left of the break line at x = 32 (the scan's flow lines also start at the cut). | fig33.tex:27, 38 | none |

## Verdict: pass (no must-fix)
