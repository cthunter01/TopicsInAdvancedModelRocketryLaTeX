# v2 audit: ch3/fig54 (round 1)

Sources checked: scan `figures/ch3/fig54.png` (zoomed x4: both noses, both bases); redraw
`figures/v2/ch3/fig54.tex`; `figures/v2/ch3/fig54.pdf` (3.90 x 2.73 in, fonts embedded) rendered at 400 and
200 dpi; `build/v2/png/ch3-fig54-compare.png`; inventory row `ch3-fig54`; caption and citing text
`chapters/ch3-sec7.tex:170-183, 199-207`; standing rule 1 in `corrections/v2-figures.md` (Fig 54 named:
expansions "dotted", wakes "wavy"); STYLE.md section 16.

Checks run:
- Attached shock of (a) measured on the scan (left branch, 18 rows): 46.0 deg from the axis; redraw 46.3 deg
  from the cone tip. Cone half-angle atan(9.25/43) = 12.1 deg, nose 43 px, body radius 9.25 px, as the scan.
- (b) nose: an ellipsoid of length 37; the three expansion starts (y = 167, 158, 144) lie on its surface
  (r = 7.25, 8.56, 9.25 computed from the ellipse). Bow shock apex 185.7, nose tip 181: a 4.7 px stand-off
  ahead of the nose (detached), as the scan.
- Inventory elements, each present: (a) straight oblique shock from the tip, three expansions curving from the
  shoulder each side; (b) curved bow shock ahead of the round nose, three curved expansions each side; both
  bases: flat base, three-line expansion fans from each base corner, shear layers converging to a short neck
  (with the short cross line at the neck, as printed), two recompression shocks diverging from the neck, two
  parallel wake lines on the axis; dash-dot axes (extended above each nose, as the scan's axis line).
- Caption line styles: shocks and compression waves solid (`outline`); expansions dotted (`dotted guide`,
  printed dashed); wakes wavy (snake decoration on the shear layers and the wake beyond the neck, printed
  straight): standing rule 1 applied. At final size (200 dpi check) the dotted fans, the wavy lines (amplitude
  0.65 pt, the two wake lines 1.65 mm apart) and the solid shocks are distinct.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | The shoulder expansions start 1.4 mm from the corner in (a) but 1.5 pt (0.5 mm) in (b), where the lowest expansion leaves the same shoulder; the gap in (a) is visibly larger than in the scan (there the dashes start at the corner) and than in (b). | fig54.tex:45-47 vs 61-63 | Optional: one start offset for both panels (e.g. `shorten <=0.8mm` in (a), or the base fans' 10-unit radius). |
| 2 | note | Where each fan starts, its three dotted lines are closer than a dot (0.27 mm apart at the base fans' 10-unit radius) and the first dots fuse into short bars; the 1973 dashes merge there too and at final size it reads as the fan's origin. | fig54.tex:31 (base fans), 45-47 | Optional: start the three lines of a fan at staggered radii (e.g. 10, 12, 14). |
| 3 | note | The neck cross line is drawn `[thin line]` only, so it takes TikZ's default black rather than `ink` (no visible difference). | fig54.tex:36 | Optional: `[outline, thin line]`. |
| 4 | note | Local styles `shock`, `expansion`, `wake` are new names over kit styles (`outline`, `dotted guide`, a snake decoration); no kit name redefined. A house "wavy" (wake) style may be wanted if another figure needs one (style suggestion). | fig54.tex:18-23 | none |
| 5 | note | Panel letters (a), (b) in the `panel` style at the lower right of each panel, one baseline (the 1973 circled letters below centre); the 1973 shading strokes in the tubes and cone are dropped (flat line art). | fig54.tex:52, 67 | none |

## Verdict: pass (no must-fix)
