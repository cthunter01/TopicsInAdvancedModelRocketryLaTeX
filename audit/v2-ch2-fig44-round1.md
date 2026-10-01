# v2 audit: ch2/fig44 (round 1)

Sources checked: the scan `figures/ch2/fig44.png` (zoomed 3x by quadrant, 6x at the pan, the wheel hub and the
dial); the redraw `figures/v2/ch2/fig44.tex` / `.pdf` (rendered at 400, 800 and 1600 dpi;
`build/v2/png/ch2-fig44-compare.png`; `pdftotext` of the lettering); inventory row `ch2-fig44`; caption and
citing text `chapters/ch2-sec5.tex:178-230` (pulley, steel shaft, ball bearings, aluminium plug, two-section
rocket, pointer-and-protractor, balance pan on a cord, counterweight, shaft centre line through the C.G.);
`chapters/ch2-sec6.tex:76-78` (Plate 1 balance as in Fig 44 without the pulley); `backmatter/figure-credits.tex:117`;
STYLE.md section 16; `figures/v2/tamrfig.sty`; the approved 3D example `figures/v2/ch2/fig03.tex`.

Size and fonts: 338.7 x 357.2 pt (4.70 x 4.96 in), within 6.5 in; one font (TeXGyreTermesX-Regular), embedded.

Checked and correct:
- Lettering: all eleven callouts of the inventory row, spelled and capitalised as printed: Test rocket forebody;
  Mounting plug; Angle indicator assembly; Panel; Pulley wheel; Test rocket afterbody; Ball bearing in bearing
  mount; Shaft; Counterweight; Bearing support plate; Balance pan. Leaders where the scan has them (none for
  Panel, Pulley wheel, Counterweight, Balance pan, as printed), each ending on its own part: the forebody tube,
  the plug's forward shoulder, the indicator collar, the afterbody's lower fin, the far bearing, the shaft inside
  the box, the near plate's lower edge. `\small` roman labels in `ink`, leaders `leader` (`ink2`); no label
  overlaps a line.
- Parts and the text: pulley wheel on the shaft's axis; shaft through a ball bearing at each plate and through
  both plates to the plug; plug a hub with two shoulders, the forebody (open aft end, tangent ogive nose) and
  afterbody (four fins, engine ring at the tail) slid off it along the rocket's axis; the rocket's axis meets the
  shaft's axis at the plug (the C.G. condition of the text); pointer on a collar, reading against the dial on the
  near plate (graduated every 10 deg, 36 ticks, about the scan's spacing); cord over the wheel with the
  counterweight on one side (left) and the balance pan on the other (right), as printed; pulley, counterweight
  and pan shown as a separable assembly (caption); one bolt hole seen in the bearing support plate nearest the
  rocket (caption), the second hidden by the top panel; the box open at its sides so the shaft is seen under the
  top panel, as in the 1973 art. Centre lines (dash-dot `centerline`): the rocket's axis beyond nose and tail,
  the shaft's axis through the exploded wheel and indicator and beyond the plug, as printed.
- Projection: x -> (a cos 45, a sin 45 sin 32), y -> (-a cos 45, a sin 45 sin 32), z -> (0, a cos 32) is a true
  orthographic view at elevation 32, azimuth 45 (right and up vectors orthonormal), viewer at (-x, -y, +z), so
  `\blk` correctly paints the -x, -y, +z faces; the silhouette angle 48.53 deg (tan = cos 32 / (sqrt 2 sin 32))
  is correct for cylinders along x and y, and 135/315 deg for `\cylz`. Visible/hidden fin split (fins 90, 180 in
  front) correct. Pan and counterweight cords leave the wheel at the y-extremes at z = 0, where a vertical cord is
  tangent to the rim's ellipse; the counterweight cord's start is correctly hidden behind the wheel's face.
- Hidden lines checked: shaft beyond the far plate hidden behind it (its end ring at x = 176 lies inside the
  plate's projection); far plate's inner face, bolt hole and the bottom panel's top seen through the open side;
  forebody passes behind the box without overlap; collar over the pointer's root.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | should-fix | The "Angle indicator assembly" leader crosses the near bearing support plate's left edge (y = +62) about 0.6 mm before it ends on the collar at (-63, 0, 8): the leader end is only about 2.9 units (0.6 mm) right of that edge, which runs down to the same point on the collar, so leader and plate edge converge on the target. In the scan the leader ends on the collar/pointer clear of the plate's edge. | `fig44.tex:159` | End the leader on the collar's near (left) half, e.g. at (-70, 3, 7) or on the pointer near its root (-63, 14, 0), so it stops short of the plate's edge. |
| 2 | note | The balance pan hangs on three strings; the 1973 cone of strings reads as three or four. Unlabelled detail, not cited. | `fig44.tex:148-149` | None needed. |
| 3 | note | The box is drawn with the top and bottom panels flush with the plates' top and bottom edges and set in 6 units from their sides; the 1973 art is ambiguous here (the far plate seems to stand slightly proud of the top panel). The redraw's box is consistent and keeps every labelled part. | `fig44.tex:111-116` | None needed. |
| 4 | note | The shaft from the far bearing ends at x = 285, 1 unit inside the hub's surface (x = 284); its end arc is drawn over the hub's outline. At final size this reads as the shaft entering the hub, which is what the text describes. | `fig44.tex:103` | None needed. |

## Verdict: pass (no must-fix)
