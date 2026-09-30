# v2 audit: ch3/fig22 (round 1)

Sources checked: scan `figures/ch3/fig22.png` (2x upscale, 3x crop of the x tick labels, and a
`digitize.py lines` listing of the printed ruling); redraw `figures/v2/ch3/fig22.pdf` (350 dpi render, and its
content stream expanded with qpdf to check the sampling of curve C) and `build/v2/png/ch3-fig22-compare.png`;
source `figures/v2/ch3/fig22.tex` lines 1-28; inventory row `ch3-fig22` (`figures/v2/inventory.csv`:88);
`chapters/ch3-sec3a.tex`:602-606 (eq. (63)); `chapters/ch3-sec3b.tex`:294-296 (eq. (86)), :758-799 (eqs.
(100)-(102b), B table, citing text); `chapters/ch3-sec3c-sec4a.tex`:22-32 (caption); `chapters/ch3-sec6a.tex`:
169-180 (reading $(C_f)_F$ from the figure); `corrections/v2-figures.md` (Ch3 Fig 22 gate item; standing rule 3);
`STYLE.md` section 16.

Checks made:
- **Formulas.**
  - A is $1000 \times 1.328/\sqrt{R_\ell}$, eq. (63), over $10^4$-$10^7$.
  - B is $1000 \times 0.074 R_\ell^{-1/5}$, eq. (86), over $5\times10^5$-$10^7$.
  - C is $1000(0.074 R_\ell^{-1/5} - 1740/R_\ell)$, eq. (101) with the caption's B = 1740, over
    $5\times10^5$-$10^7$.
  - Eqs. (100)/(102) at $R_{crit} = 5\times10^5$ give $B = 5\times10^5(0.0053634 - 0.0018781) = 1742.7$.
- **Values.**
  - A: 13.28 at $10^4$, 0.420 at $10^7$.
  - B: 5.36 at $5\times10^5$, 2.946 at $10^7$.
  - C: 1.883 at $5\times10^5$, where it starts on A (1.878) as printed. It peaks at 3.21 at $2.2\times10^6$ and
    ends at 2.772 at $10^7$.
  - The render agrees at each point.
- **Sampling.** In the PDF path the samples of C are equally spaced in log R (a 1.70 pt step), so the steep start
  of C is resolved.
- **Axes.**
  - True log-log. The ranges $10^4$-$10^7$ and 0.2-20 match the print, and the decades are nearly isometric, as
    printed.
  - y labels 0.2, 0.3, 0.4, 0.6, 0.8, 1.0, 2, 3, 4, 6, 8, 10.0, 20 are all present, with leading zeros per
    STYLE.
  - Titles $1000\,C_f$ and $R_\ell = U_\infty\ell/\nu$ as printed.
  - The circled tags A, B and C are present and sit on their curves.
- **Caption and text.** $R_{crit} = 5\times10^5$ and B = 1740 hold. Functions A, B and C are the curves the text
  names.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | must-fix | The x tick label "8" is missing in all three decades. The print labels 2, 3, 4, 6, 8 in each decade (inventory lettering; the scan's tick row reads "2 3 4 6 8" before $10^5$, $10^6$ and $10^7$). The redraw labels only 2, 3, 4, 6: 8e4, 8e5 and 8e6 are only unlabelled minor ticks. | fig22.tex:12-14 | Add 8e4, 8e5, 8e6 to `xtick` with the label "8". At the current size each "8" would sit about 0.7 mm from the following decade label: legible but tight. Setting $10^4$ ... $10^7$ on a lower line, as printed (e.g. with `extra x ticks` and a y shift), avoids that. |
| 2 | should-fix | The grid is coarser than printed. The 1973 ruling (and the inventory) has lines at 1, 1.5, 2, 2.5, 3, 3.5, 4, 5, 6, 7, 8, 9 in each decade on both axes; `lines` on the scan finds 12 per decade, plus 15 between 10 and 20 and 0.25 and 0.35 below 0.4. The redraw rules only 1, 2, 3, 4, 5, 6, 7, 8, 9. STYLE section 16 (`tamr grid`: "hairline grid at the printed spacing"), and this is a chart the text tells the reader to read values from (ch3-sec3b.tex:798-799, ch3-sec6a.tex:172-174). | fig22.tex:14, 17 | Add minor grid lines at 1.5, 2.5, 3.5 x each decade (x: 1.5e4 ... 3.5e6; y: 0.25, 0.35, 1.5, 2.5, 3.5, 15) at their true log positions. |
| 3 | note | Known gate item: B = 1740 (caption) is used where the text and table say 1700 and eqs. (100)/(102) give 1742.7. With 1740, C starts on A, as printed. Curve A lies about 0.1 decade below the 1973 art because the 1973 paper is not logarithmic (standing rule 3). | fig22.tex:22 | none (gate) |
| 4 | note | The tags sit on their curves (1973: beside them, in gaps of grid lines). Tag C at $3\times10^6$ clears curve B by about 1.4 mm at final size. That is legible but tight; $2.5\times10^6$ or a little to the right would give more room. | fig22.tex:23-25 | Optional. |

## Verdict

fix (1 must-fix, 1 should-fix)
