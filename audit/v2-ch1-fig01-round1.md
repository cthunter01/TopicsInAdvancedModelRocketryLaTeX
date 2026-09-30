# v2 audit: ch1/fig01 (round 1)

Sources checked: figures/ch1/fig01.png (scan, upscaled 2x); figures/v2/ch1/fig01.pdf (rendered 350 and 1200 dpi);
figures/v2/ch1/fig01.tex:1-34; figures/v2/inventory.csv row ch1-fig01; caption chapters/ch1-sec1.tex:15-20 and
citation ch1-sec1.tex:13; corrections/v2-figures.md; figures/v2/tamrfig.sty (`cg mark`, `thin vec`, `panel`,
`centerline`, `pic rocket`, `model`).

Checked and correct: (a) two upright rockets of equal size, 1 lower left and 2 upper right, thin vector from C.G. 1
(0,0) to C.G. 2 (5.2,2.5), no rotation; (b) rocket 1 upright and rocket 2 turned 30 deg clockwise, both placed by
`\uprocket` so that their C.G. is the same point (9.3,0.4) (nose at C.G. + (90-tilt : 0.65L), axis at -90-tilt),
so the rotation is about the C.G. without translation; solid vertical reference line through rocket 1 above the
nose and below the tail; dash-dot line along rocket 2's axis beyond nose and tail; clockwise arc (radius 4.06,
90 to 60 deg) with its head on the rotated axis; labels 1, 2 in both panels on the correct rockets; panel letters
(a), (b) present (house `panel` style). Nothing added.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | should-fix | The translation vector ends at the centre of C.G. 2, and the `cg mark` drawn afterwards (white fill, radius 2.75pt) covers the front 2.75pt of the 5pt `thin vec` head: only a notched wedge of the head shows beside the mark. In the scan the arrow tip touches the C.G. circle and the whole head is visible. | fig01.tex:16-17 | End the arrow at the mark's rim, e.g. `\draw[thin vec, shorten >=2.9pt] (cg1) -- (cg2);`. |
| 2 | should-fix | In (b) the rotated rocket's own centre line (the pic's default `centerline=true`, from 0.08L ahead of the nose to 0.08L behind the tail) is drawn over the explicit extended axis line (line 25) with a different dash phase, so from about 1.9 cm aft of the C.G. to 3.2 cm ahead of it the rotated axis reads as a continuous grey line; the dash-dot pattern the scan shows along rocket 2 appears only beyond the nose. | fig01.tex:25-26 (`\uprocket{(cg)}{30}` inherits `centerline=true`) | Pass `centerline=false` to the two rockets of (b) (e.g. an optional key to `\uprocket`); lines 24-25 already draw both axes. |
| 3 | should-fix | Panel letters: with the panels now side by side, the printed double rule between them is gone and (a) at (6.6,-2.3) sits in the gutter, about 0.8 cm right of rocket 2's fins and 1.4 cm left of panel (b)'s lowest fin, rather than under its panel; (b) at (11.2,-1.9) is 0.4 cm higher than (a), so the two letters are not on one baseline. | fig01.tex:20, 31 | Put both letters on one baseline (e.g. y = -2.3) centred under their panels (about x = 2.6 for (a), x = 9.3 for (b)), or keep them at lower right but add a thin vertical rule between the panels. |
| 4 | note | The source comment calls this "the model rocket of Figures 6-8", but the rocket here is a slightly different body: L = 4.4, d = 0.3 (d/L 0.068 against 0.0625 in `model`), root chord 0.16L (0.148L), span 0.10L (0.094L), and the C.G. at 0.65L against 0.62L in Figs 6-8. Not noticeable at a glance; the fin shape (swept leading edge, square trailing edge) matches the scan. | fig01.tex:2, 7, 11-12 | Optional: use `model` scaled (d = L/16) and \cgf = 0.62, or reword the comment. |

## Verdict

pass (0 must-fix, 3 should-fix)
