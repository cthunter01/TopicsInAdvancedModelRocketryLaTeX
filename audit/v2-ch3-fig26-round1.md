# v2 audit: ch3/fig26 (round 1)

Sources checked: scan `figures/ch3/fig26.png` (2x); redraw `figures/v2/ch3/fig26.pdf` (300 dpi whole, 600 dpi crop
of the x tick labels and title; `pdffonts`); sources `figures/v2/ch3/fig26.tex`, `fig26.py`, `fig26-a.csv`,
`fig26-b.csv`, `fig26.calib.json`; `digitize.py lines` on the crop (to check the xgrid/ygrid rulings); inventory row
`ch3-fig26` (`figures/v2/inventory.csv`:92); caption and citing text `chapters/ch3-sec3c-sec4a.tex`:303-331 and
`ch3-sec4b.tex`:169-171; `corrections/v2-figures.md` standing rule 3; `STYLE.md` sections 14 and 16; the approved
Ch3 Fig 22 (the same 1973 paper on true log axes).

Checks made:
- **Calibration.** The xgrid columns in fig26.calib.json match the rulings `digitize.py lines` finds. For
  example: 10^3 at 91.5 (found 91), 1.5e3 at 129.5 (130), "2" at 157.5 (157), "3" at 179.5 (179), 10^4 at 246
  (245.5), 2e4 at 310.5 (310.5), 10^5 at 397.5 (397). They confirm the non-logarithmic paper (the "2" at 0.43
  of a decade). The horizontal rulings run about 2-4 px lower at the right ("lines" finds the 1.0 ruling at row
  108 on the left and 110.5 on the right). The script reads them as straight sloped lines, which is the right
  treatment.
- **Overlay** (`digitize.py overlay`, piecewise xgrid/ygrid; it ignores the slope, so the right-hand ends read
  about 2 px high):
  - (a): 1629 points, mean 0.49 px, 95% 2.00 px, max 3.00 px.
  - (b): 1421 points, mean 0.73 px, 95% 2.00 px, max 2.83 px. Both ok.
  - Visually the curves sit on the scan throughout, including the cylinder's sharp foot and the sphere's corner
    at the top of its drop.
- **Values read from the CSVs.**
  - (a) 1.00 at 10^3; minimum 0.95 at 2-2.5e3; 1.15 over 2e4-5e4; peak 1.19 at 1.67e5; foot 0.29 at 4.9e5;
    0.35 at 10^6.
  - (b) 0.45 at 10^3; 0.395 over 2.5e3-5e3; 0.444 at 4-5e4; 0.38 at 2.7e5; 0.19 at 3e5; minimum 0.09 at
    4.4e5; 0.13 at 10^6.
  - These agree with the inventory's readings.
- **Text.** "A sudden and considerable decrease" at about 3e5 for a sphere and 5e5 for a cylinder holds: the
  sphere drops from 0.38 at 2.7e5 to 0.19 at 3e5, and the cylinder's drop ends at 4.9e5.
- **Axes.**
  - True log abscissa, 10^3-10^6, labelled 10^3, 2, 3, 4, 6, 8, 10^4 ... 10^6 as printed. Rulings at 1, 1.5,
    2, 2.5, 3, 3.5, 4, 5, 6, 7, 8, 9 per decade (major plus minor grid, one weight).
  - C_D 0-1.4 (a) and 0-0.8 (b), step 0.2, labelled 0, 0.2, ..., 1.0 with a leading zero.
  - Titles $C_D$ (upright) and $R_D = \dfrac{U_\infty D}{\nu}$ in each panel, with capital R_D and D as printed.
  - The tick-label treatment (powers of ten at the decades, bare digits between) is the same as the approved
    Fig 22. "8" and "10^4" are 1.5 mm apart and legible at 600 dpi.
- **Panels.** Both share the x scale (5.2 in, 1.733 in per decade) and the C_D scale (1.75 in per unit: 2.45 in
  and 1.4 in tall). The panel letters (a), (b) are in the kit `panel` style at the upper right inside the axes
  (the 1973 circled letters are outside on the right), with a white knock-out over the grid. They are well clear
  of the curves.
- **Size.** Page 5.93 x 5.53 in (<= 6.5 in); fonts embedded. Curves are s1, 1pt.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | The panel letters add `fill=white, inner sep=1.5pt` to `panel` so the grid does not cross them. This is the same local choice as Ch3 Fig 21; the kit has no gridded-panel variant yet. | fig26.tex:22, 28 | None now. Same style suggestion as Fig 21: a kit `panel on grid` variant. |
| 2 | note | The overlay tool's piecewise calibration has no slope term, so on the right of each panel it reads the curves 1-2 px high. The script's own reading (sloped rulings) is the better one, and the overlay passes either way. | fig26.py (Panel, slope 0.0090 / 0.0084) | None. |

## Verdict: pass

No must-fix and no should-fix.
