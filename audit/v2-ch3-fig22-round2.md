# v2 audit: ch3/fig22 (round 2)

Sources checked: scan `figures/ch3/fig22.png`; redraw `figures/v2/ch3/fig22.pdf` (rendered 300 and 600 dpi; at
600 dpi a glyph-by-glyph measurement of the x tick-label row, a scan of the gridline positions along one row and
one column of the plot, and the tag C clearance); source `figures/v2/ch3/fig22.tex` lines 1-29 (changed since
round 1); round-1 report; inventory row `ch3-fig22` (`figures/v2/inventory.csv`:88); caption
`chapters/ch3-sec3c-sec4a.tex`:23-32; `corrections/v2-figures.md`:20 (standing rule 3) and :54 (the Ch3 Fig 22
gate item); `STYLE.md` section 16.

| round-1 # | severity | status | evidence |
|-----------|----------|--------|----------|
| 1 | must-fix | resolved | fig22.tex:12-13 now ticks and labels 8e4, 8e5 and 8e6 "8", so each decade reads 2, 3, 4, 6, 8, as printed. At 600 dpi each "8" ends 47 px (2.0 mm) before its decade label ("8" at x 1322-1350, "$10^5$" from 1397; the same spacing before $10^6$ and $10^7$). The decade labels sit about 0.6 mm lower than the single digits because of their superscripts, close to the printed two-level arrangement. Legible. |
| 2 | should-fix | resolved | fig22.tex:15 and :18 add the minor rulings. Gridlines measured along a row of the 600 dpi render fall at 1, 1.5, 2, 2.5, 3, 3.5, 4, 5, 6, 7, 8, 9 in each x decade (36 lines, $1.5\times10^4$ to $10^7$). Along a column they fall at 0.25, 0.3, 0.35, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.5, 2, 2.5, 3, 3.5, 4, 5, 6, 7, 8, 9, 10, 15 and 20, all at true log positions. This is the printed ruling (inventory: 12 lines per decade; plus 15, 0.25 and 0.35). |
| 3 | note | accepted: gate item | The source is unchanged here: C is still computed with B = 1740 (fig22.tex:23) and starts on A at $5\times10^5$. The item is logged at corrections/v2-figures.md:54 ("Computed on true log axes with the formula", gate, pilot). |
| 4 | note | accepted: optional, unchanged | Tag C is still at $3\times10^6$ (fig22.tex:26). At 600 dpi its circle top is 26 px (1.1 mm) below curve B, which is legible. |

## New findings

None. The three curves, their domains (A $10^4$-$10^7$; B and C $5\times10^5$-$10^7$), the circled tags A, B and C,
the y labels (0.2 ... 1.0 ... 10.0, 20), the titles $1000\,C_f$ and $R_\ell = U_\infty\ell/\nu$, and the true
log-log ranges are as round 1 checked them. The figure is 6.14 in wide, within the text block.

## Verdict

pass (0 must-fix, 0 should-fix)
