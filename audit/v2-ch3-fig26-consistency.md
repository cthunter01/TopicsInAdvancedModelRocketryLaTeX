# v2 audit: ch3/fig26 (consistency fix, verification)

Sources checked:
- The 1973 scan `figures/ch3/fig26.png`.
- The redraw `figures/v2/ch3/fig26.pdf`, built 23:15:46, after the tex (23:15:45), so it is current.
  - Renders: 300 dpi whole; 800 dpi crops of the upper-right corner of each panel.
  - `pdfinfo`: 427.1 x 398.3 pt (5.93 x 5.53 in), the same as rounds 1 and 2.
  - `pdffonts`: all fonts embedded.
- `build/v2/png/ch3-fig26-compare.png`.
- Sources: `figures/v2/ch3/fig26.tex`, `fig26.py` (22:08), `fig26-a.csv` and `fig26-b.csv` (22:21), and `fig26.calib.json`.
- The round-1 and round-2 audits, the consistency issue and the fixer's report.
- Inventory row `ch3-fig26`.
- The approved placements: ch3/fig53.tex:30, 51; ch1/fig03.tex:14; ch1/fig05.tex; ch2/fig20.tex; ch2/fig46.tex. Also ch3/fig21.tex:21, 26, the other figure in this issue.
- `tamrfig.sty` (`panel`: `\small\itshape`, inner sep 1pt; unchanged since 21:33).

## Consistency issue: panel-letter placement

The issue: (a) and (b) sat at `rel axis cs:0.985,0.975` with inner sep 1.5pt, lower and further left than the approved `anchor=north east` at `(rel axis cs:1,1)`. **Resolved.**

- **Code.**
  - fig26.tex:56 and :62 now read `\node[panel, anchor=north east, fill=white] at (rel axis cs:1,1)`.
  - The local inner sep is gone, so the kit's 1pt applies.
  - This is the form in Fig 53 and the Ch1 and Ch2 references. It is identical to the fixed Fig 21 (fig21.tex:21, 26), so Figs 21, 26 and 53 now place their letters the same way.
- **The kept `fill=white`.** It is justified: the issue says to keep it where a gridline would cross the letter.
  - At 800 dpi the 8 x 10^5 and 9 x 10^5 minor rulings (grid=both) run up to the letter and stop at its box.
  - The top frame line and the 10^6 gridline at the corner stay whole across the letter.
- **Clearances.** Both letters are well clear of the curves:
  - (a): the curve is below 1.19 near the corner, so the letter has about 0.2 units (about 0.35 in) clear above it.
  - (b): the curve is at 0.13 at 10^6, far below the letter.

## Regression check against the scan, the inventory and the earlier audits

- **Curves.** I re-ran the overlay (`digitize.py overlay`, piecewise xgrid/ygrid):
  - (a): 1629 points, 95% 2.00 px, max 3.00 px;
  - (b): 1421 points, 95% 2.00 px, max 2.83 px.
  - These are identical to rounds 1 and 2. All ok.
- **Axes and lettering.** All unchanged:
  - the true log abscissa from 10^3 to 10^6, with tick labels 10^3, 2, 3, 4, 6, 8, ...;
  - the rulings 1, 1.5, ..., 4, 5-9 in each decade;
  - C_D from 0 to 1.4 and from 0 to 0.8;
  - the upright $C_D$ title, and $R_D = U_\infty D/\nu$ under each panel;
  - the shared x scale and C_D scale.
- **Panel letters.** The 1973 letters are circled and stand outside the plot on the right. The house places them at the upper right inside the axes (STYLE s.16), which is now the exact approved placement.
- **Earlier notes.** Round 1/2 note 1 (a local `fill=white`, and a kit "panel on grid" variant suggested) still applies. The overlay's slope note is unchanged.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | The issue is resolved. (a) and (b) now sit at `(rel axis cs:1,1)`, anchor north east, with the kit inner sep, the same as Figs 21 and 53. Nothing regressed. | fig26.tex:56, 62 | None. |
| 2 | note | `fill=white` is kept because the 8 and 9 x 10^5 rulings would cross the letters, as the issue allows. Figs 21 and 26 now carry the same gridded-panel form. | fig26.tex:56, 62 | Kit suggestion (standing): a `panel on grid` style. |

## Verdict: pass

No must-fix and no should-fix.
