# v2 audit: ch3/fig14 (round 2)

Sources checked: scan `figures/ch3/fig14.png` (4x crop of the δ* dimension); redraw `figures/v2/ch3/fig14.pdf`
(300 dpi render, 2x crop of the dimension, `pdftotext -bbox`, `pdffonts`, `pdfinfo`); sources
`figures/v2/ch3/fig14.tex`, `fig14.py`, `fig14.csv`, `fig14-marks.csv`, `fig14.calib.json`; inventory row
`ch3-fig14` (`figures/v2/inventory.csv`:80); `chapters/ch3-sec3a.tex`:330-336 (eqs. (45), (46)), Table 1,
:455-473 (citing text, caption); `chapters/ch3-sec3b.tex`:675-677; `corrections/v2-figures.md`:142 (Minor);
`STYLE.md` sections 14 and 16; the round-1 audit and fix records.

Checks made:
- **Round-1 items.** The only item was the optional rename of `\marks` (an e-TeX primitive). Resolved:
  `fig14.tex`:9-10 now read the table into `\figmarks`. In a test document after `\usepackage{tamrfig}`,
  `\figmarks` and `\dstar` are both undefined before the figure defines them, so nothing is overwritten.
- **Regression.**
  - The current source compiles cleanly in my scratch directory.
  - Its 300 dpi render is pixel-identical to the PDF in the tree and to the round-1 auditor's render (the
    difference bounding box is None).
  - The kit (`tamrfig.sty`, 21:33) predates the PDF (21:59).
- **Data.**
  - I re-ran `fig14.py` in a scratch copy of the tree. `fig14.csv` and `fig14-marks.csv` come out byte-identical
    to the files in the tree.
  - Against my own shooting solution of eq. (51) (f''(0) = 0.3320573), the whole CSV agrees to 1.6e-5 in f'.
    The curve ends at η = 5.793 with f' = 0.99835, on the 1.0 border.
  - lim(η − f) = 1.72079 by the ODE, and 1.72077 in `fig14-marks.csv`.
- **Overlay** (`digitize.py overlay`, the drafter's calibration, residual 0.00 px): 241 points, mean 0.14 px,
  95% 1.00 px (0.17 mm), max 1.00 px: ok.
- **Lettering and caption.**
  - Everything printed is present: the rotated η title, $f'(\eta) = u/U_\infty$, ticks 0-8 and 0-1.0, and "1.73"
    in a gap at x = 0.15.
  - The δ*√(U∞/νx) `\dimline` runs along the 0.8 gridline and knocks out the η = 1 line, as printed (compared at
    4x with the scan).
  - "1.73" and the dimension label are both \small (bbox 9.01 pt). The tick labels are \footnotesize.
  - The caption's δ* ≈ δ/3 holds (1.72 against δ at η = 5).
- **Size.** Page 4.98 x 3.40 in; all fonts embedded; nothing clipped or overlapping. The dimension's heads are
  visible at final size.
- **Family.** The frame (4.2 x 2.7 in, grid=both, ticks) is identical to Fig 15's, and the height matches
  Figs 19-21.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | Round-1 optional item resolved: `\marks` renamed `\figmarks`. The render is unchanged. | fig14.tex:9-10 | None. |
| 2 | note | The 1.73 label against Table 1's 1.7208 is the logged minor item (corrections/v2-figures.md:142), approved. | fig14-marks.csv; fig14.tex:20-22 | None. |

## Verdict: pass

No must-fix and no should-fix. The curve is Table 1 (and eq. (51)) to 2e-5, the overlay is within 1 px, every
printed label is present, and nothing has regressed since round 1.
