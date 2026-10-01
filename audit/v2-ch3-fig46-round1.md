# v2 audit: ch3/fig46 (round 1)

Sources checked: scan `figures/ch3/fig46.png` (zoomed); redraw `figures/v2/ch3/fig46.tex`, `fig46.py`,
`fig46-{cylinder,ellipsoid,ogive,cone}.csv`, `fig46.calib.json`; rebuilt with `make fig F=ch3/fig46` (4.86 x 3.53 in)
and rendered at 400 and 600 dpi; inventory row `ch3-fig46`; equations (168)-(171e), caption and citing text
`chapters/ch3-sec6a.tex:239-286`, `chapters/ch3-sec6b.tex:60-77` ("Figure 46 or equation (171c) gives 2.7 l/d_m");
`corrections/v2-figures.md` (standing rules, gate decisions, line 153 on eq. (171b)); STYLE.md sections 14, 16.

Checks run:
- The CSVs match the formulas to 5e-6: cylinder 4f (eq. 170); ellipsoid exact column eq. (171a), printed column
  pi f; ogive 2.67 f (171c) in both; cone exact eq. (171d), printed 2 f (171e). Noses start at f = 1.5; each
  curve stops one sample past S_s/S_m = 16 or at f = 6 and is clipped at the frame.
- Spot values (f = 1.5 / 3 / 5): (171a) 4.917 / 9.540 / 15.780; pi f 4.712 / 9.425 / 15.708; printed (171b)
  1 + pi f 5.712 / 10.425 / 16.708; (171d) 3.162 / 6.083 / 10.050; 2 f 3.0 / 6.0 / 10.0; 2.67 f 4.005 / 8.01 /
  13.35.
- Scan line centres, read at sample columns with the piecewise calibration: ellipsoid 5.37, 5.68, 8.46, 10.39,
  14.87 at f = 1.7, 1.8, 2.7, 3.3, 4.7 (pi f: 5.34, 5.65, 8.48, 10.37, 14.77; (171a): 5.53, 5.83, 8.61, 10.47,
  14.84). The printed ellipsoid line is pi f, not (171a) and not (171b). Cone 3.28 ... 9.63 at f = 1.6 ... 4.7,
  about 2.05 f (the drafter measured 2.03). Ogive 2.67-2.68 f. Cylinder 4.00 f.
- `digitize.py overlay`, both columns: exact cylinder / ellipsoid / ogive / cone 95% 1.00 / 2.24 / 1.00 / 2.24 px;
  printed 1.00 / 1.00 / 1.00 / 3.00 px. All are "ok". The dense rulings, every 19 px, make these distances
  forgiving, so the sampled line centres above are the better comparison.
- Text: the ogive is 2.67 l/d_m, as eq. (171c) states and the text's "2.7" reading needs (at f = 4.74, 12.65).

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | **Gate choice.** By default (`\exacttrue`) the redraw plots the exact eq. (171a) for the ellipsoid and the exact eq. (171d) for the cone, as the family brief asked. The 1973 lines are pi l/d_m and about 2 l/d_m. The exact ellipsoid lies 0.21 above the printed line at 1.5 and 0.07 above it at 5. The exact cone lies 0.16 above at 1.5 and 0.04 above at 6. That is 0.5 mm or less at final size, but it shows where the noses start on the grid (4.92 against 4.7, 3.16 against 3.0). With exact curves, the caption's "approximate ... terminated at the lower limit of fineness ratio for which they give acceptable accuracy" fits only the ogive line, so the gate has to choose. `\exactfalse` gives the printed lines (4f, pi f, 2.67f, 2f), which match the art. `corrections/v2-figures.md` records only the eq. (171b) question (line 153). It does not record this choice. | fig46.tex:13, fig46.py CURVES | Orchestrator: add a gate item to corrections/v2-figures.md (exact (171a)/(171d) vs the printed lines, with the numbers above). No change to the figure until the gate decides. |
| 2 | note | The drafter's eq. (171b) finding is confirmed. Eq. (171a) is exact: it is the lateral area of a half prolate spheroid over pi d_m^2/4, and the "1 +" is part of that curved area. Its large-f limit is pi f + O(1/f), because sin^-1 e = pi/2 - 1/(2f) + ..., so 2f sin^-1(e)/e = pi f - 1 + .... The printed 1 + pi f is 0.80 above (171a) at f = 1.5 and 0.93-0.94 above it at f = 5-6. The art follows pi f, which is also what eq. (168) gives when the surface slope is neglected. | ch3-sec6a.tex:266-267 | For the v1 corrections step (already in v2-figures.md line 153). Nothing to change in the figure. |
| 3 | note | Lettering and frame are as printed. Y title $\dfrac{S_s}{S_m}$ (lowercase s subscript, STYLE section 14), upright to the left. X title $\dfrac{\ell}{d_m}$. X ticks 0-6 with rulings every 0.5; y ticks 0-16 every 2 with rulings every 1. Labels "Cylinder", "Ellipsoid", "Ogive", "Cone" sit beside their lines on white knock-outs over the grid only, sloped with the lines, clear of them, with no other curve passing. All four curves are s1 solid. `tamr grid`, 4.2 x 2.8 in axes. | fig46.tex:17-34 | none |

## Verdict: pass (no must-fix)
