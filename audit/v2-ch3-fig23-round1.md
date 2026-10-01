# v2 audit: ch3/fig23 (round 1)

Sources checked: scan `figures/ch3/fig23.png` (2x whole, 4x crops of the cylinder and of the wake arrows); redraw
`figures/v2/ch3/fig23.pdf` (300 dpi whole, 600 dpi crop of the profile box, B, S and the upper lobe; `pdffonts`);
sources `figures/v2/ch3/fig23.tex`, `fig23.py`, `fig23-*.csv`, `fig23.calib.json`; inventory row `ch3-fig23`
(`figures/v2/inventory.csv`:89); caption and citing text `chapters/ch3-sec3c-sec4a.tex`:174-201, and the Fig 24
caption (:211-214: phi from A, B = 90 deg, C = 180 deg); `STYLE.md` sections 14 and 16; `tamrfig.sty` (curve tag,
point, hatch, centerline, thin vec); `corrections/v2-figures.md`.

Checks made:
- **Lettering.** $U_\infty$ is set in a white gap of the first streamline above the axis at x = -3.0 a, as printed.
  A, B, C and S are kit `curve tag`s inside the cylinder, each with a `point` dot on the surface. The text cites
  "point A", "point B", so the curve tag is the house form; the 1973 art has plain letters. A, B, C sit at 180,
  90 and 0 deg from the downstream axis, so the Fig 24 caption (B = 90 deg, C = 180 deg from A) holds. S is at
  43.2 deg from the downstream axis, where the scan puts it (measured: 44 deg). Nothing is missing against the
  inventory lettering list.
- **Streamlines.** There are 4 above, 4 below, and the stagnation line ahead and the wake centre line behind.
  Each has a small head at x = -4.0 a (scan: -3.9 a). They are the potential flow of a stream past a doublet
  plus a source at (0.098, 0) (mu 1.886, q 0.190), fitted to the scan. That is the "governing equation, parameters
  matched" route for an unlabelled sketch.
  - Overlay (`digitize.py overlay`, the drafter's calibration, residual 0.00 px; distances in scan px):

    | | s1 | s2 | s3 | s4 |
    |---|---|---|---|---|
    | upper, 95% | 8.0 | 5.0 | 3.0 | 3.0 |
    | lower, 95% | 5.7 | 4.0 | 3.6 | 4.0 |

    Wake outline: 8.6 px. The drafter reports rms 3.3 px and 95% 6.5 px.
  - Column reads: over the cylinder (x = -0.3 to 1.0 a) the computed streamlines lie 0.02-0.07 a above the
    drawn ones. Far upstream they are within 0.05 a.
- **Hatched region.** The edge is the dividing streamline. Its thickness is 0.31 a at A (scan 0.28 a) and 0.42 a
  at B (scan 0.34 a); it is about 0.06 a outside the drawn edge over the top. The two lobes have their tips at
  x = 1.80 a (scan 1.81 a). The pocket's cusp on the axis is at 1.74 a (scan 1.73 a). The hatch is the kit's
  45-degree `hatch`, the same direction as the scan's.
- **Velocity profile at B.** It is the Blasius f'(eta) of Table 1 across the layer's thickness at B, in a white
  box 0.44 a wide (scan 0.42 a) standing on the wall normal at B. The box top is at 2.05 a (scan 1.95 a). The
  horizontal velocity lines run from the wall normal to the profile, and the box hides the streamlines behind it,
  as printed.
- **Arrows.** The upper straight arrow points downstream along the separated layer. The curved arrows turn
  clockwise above and anticlockwise below, ending in the lobe tips: the same senses as the scan. All are
  `thin vec` with a 2pt white casing over the hatch (a knock-out, not transparency).
- **Cross-hair.** It is a kit `centerline`, shortened (horizontal +-0.56 a, vertical -0.86 to +0.56 a) to clear
  the tags. Nothing touches.
- **Size.** 4.78 x 1.97 in; fonts embedded. The local styles (`streamline`, `flow arrow`, `eddy`) have new names,
  not kit redefinitions. The `streamline` style matches Fig 28's (0.5pt ink).

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | The straight arrows in the separated layer sit about 0.15 a further from the cylinder and a little upstream of where the scan has them. Redraw: (0.80, +-1.00) to (1.06, +-0.90), tail at 51 deg, above S. Scan: about (0.85, +-0.82) to (1.18, +-0.69), starting beside S. The direction is the same. The source comment "reversed flow: along the separated layer behind S" mislabels them: they point downstream, as printed. | fig23.tex:41-42 | Optional: move them to about (0.86, +-0.84) to (1.16, +-0.71) so they start beside S, as printed, and say "the separated layer's outer flow" in the comment. |
| 2 | note | The innermost streamlines and the hatched region come out up to 0.07 a (about 1 mm at final size) fuller over the top of the cylinder than the 1973 hand drawing. The cause is the one-source potential-flow fit; the drawn wake is narrower over B (0.34 a against 0.42 a). This is the approved computed-sketch method, and the qualitative picture is unchanged. | fig23.py (MU, Q, XD) | None required. |
| 3 | note | Points A, B, C, S are circled `curve tag`s; the 1973 letters are plain. This is the house form for point letters the text cites. | fig23.tex:50-53 | None. |

## Verdict: pass

No must-fix and no should-fix.
