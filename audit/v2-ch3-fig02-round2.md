# v2 audit: ch3/fig02 (round 2)

Sources checked: scan `figures/ch3/fig02.png`; redraw `figures/v2/ch3/fig02.pdf` (rendered 300 dpi); source
`figures/v2/ch3/fig02.tex` lines 1-18 and its data `fig02.py`, `fig02.csv`, `fig02.calib.json` (all unchanged since
before round 1: 15:31, against the round-1 report at 16:47; the PDF was rebuilt only for the `tamrfig.sty` change);
`digitize.py overlay` of `fig02.csv` (rerun); round-1 report; inventory row `ch3-fig02`
(`figures/v2/inventory.csv`:68); `corrections/v2-figures.md`:38 (gate item "Formulas from outside the book");
`STYLE.md` section 16; `figures/v2/tamrfig.sty`.

| round-1 # | severity | status | evidence |
|-----------|----------|--------|----------|
| 1 | note | accepted: gate item | The curve is still USSA-1962 (fig02.py, unchanged), logged at corrections/v2-figures.md:38 with ch3-fig02 as the pilot sample. The overlay still passes: mean 0.41 px, 95% 1.21 px (0.20 mm), max 2.00 px. |
| 2 | note | accepted: deferred | The axis is still defined inline (fig02.tex:7-13). Factoring it into a shared style is only due when Ch3 Figs 3, 4, 7 and 8 are drawn. |

## New findings

None. The only change since round 1 is the house style (ink2 axes at 0.7pt, gridc grid). The 300 dpi render keeps
everything round 1 checked: the 0.05 horizontal and 500 m vertical ruling, y labels 0.70-1.00, x labels 0-2500
without a separator, the y title $\rho/\rho_o$, and the $\rho_o = 1.225014$ kg/m$^3$ note knocked out on the 0.80
line.

## Verdict

pass (0 must-fix, 0 should-fix)
