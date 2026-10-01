# v2 audit: ch3/fig26 (round 2)

Sources checked:
- The 1973 scan, `figures/ch3/fig26.png`.
- The redraw, `figures/v2/ch3/fig26.pdf`, rendered at 300 dpi; also `pdfinfo` and `pdffonts`. The PDF dates from 22:21, after the tex (22:00) and the CSVs, so it is current.
- The drafter's sources: `figures/v2/ch3/fig26.tex`, `fig26.py`, `fig26-a.csv`, `fig26-b.csv` and `fig26.calib.json`.
- The round-1 audit and the round-1 fix report.
- Inventory row `ch3-fig26`.
- The caption and citing text: `chapters/ch3-sec3c-sec4a.tex`:303-331 and `ch3-sec4b.tex`:169-171.
- Standing rule 3.

## Round-1 findings

Round 1 had no must-fix or should-fix items. The fix round changed nothing, and the timestamps confirm it. The two round-1 notes still stand:
- The local `fill=white` on the panel letters. The suggestion for a kit "panel on grid" style has been passed on.
- The overlay tool takes no account of the slope of the rulings.

## Re-check

- **Overlay.** I ran `digitize.py overlay` with piecewise xgrid and ygrid calibration.
  - (a): 1629 points, 95% 2.00 px, maximum 3.00 px. ok.
  - (b): 1421 points, 95% 2.00 px, maximum 2.83 px. ok.
  - In the overlay image, both curves sit on the scan, including the sharp foot of (a) and the corner at the top of (b)'s drop.
- **Values read from the CSVs.**
  - (a): 0.99 at 10^3; 0.95 at 2.2e3; 1.10 at 10^4; 1.15 over 3e4 to 5e4; peak 1.186 at 1.67e5; 0.29 at 4.9e5; 0.35 at 10^6.
  - (b): 0.45 at 10^3; 0.39 at 3e3; peak 0.444 at 4.9e4; 0.38 at 2.7e5; 0.19 at 3e5; 0.09 at 4.4e5; 0.13 at 10^6.
  - Both agree with the inventory.
  - Both agree with the text: "a sudden and considerable decrease" at about 3e5 for spheres and 5e5 for cylinders.
- **Axes and lettering.**
  - True log abscissa from 10^3 to 10^6, labelled 10^3, 2, 3, 4, 6, 8, 10^4 and so on, as printed.
  - Rulings at 1, 1.5, 2, 2.5, 3, 3.5, 4 and 5 to 9 in each decade.
  - C_D runs 0 to 1.4 in (a) and 0 to 0.8 in (b), in steps of 0.2.
  - Axis titles: $C_D$ (upright) and $R_D = U_\infty D/\nu$ under each panel.
  - The panel letters (a) and (b) are at the upper right inside the axes.
- **Size and fonts.** Both panels share the x scale and the C_D scale. The page is 5.93 x 5.53 in. Fonts are embedded.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | Unchanged since round 1, and nothing regressed. The overlay passes for both panels (95% 2.00 px), and every reading the text relies on holds. | fig26.tex, fig26-*.csv | None. |
| 2 | note | The panel letters still carry a local `fill=white` knock-out over the grid, as in Fig 21. The kit "panel on grid" suggestion is with the orchestrator. | fig26.tex:22, 28 | None in this figure. |

## Verdict: pass

No must-fix and no should-fix.
