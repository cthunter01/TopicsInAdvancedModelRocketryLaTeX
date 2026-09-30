# v2 audit: ch2/fig25 (round 2)

Sources checked: scan `figures/ch2/fig25.png`; redraw `figures/v2/ch2/fig25.pdf` (rebuilt 16:55 for the style
change; rendered at 400 dpi); source `figures/v2/ch2/fig25.tex`:1-36 (unchanged since round 1, mtime 15:34);
round-1 report; inventory row `ch2-fig25` (`figures/v2/inventory.csv`:38); caption and text
`chapters/ch2-sec3b.tex`:473-490; `corrections/v2-figures.md` (Ch2 Fig 25 gate item); `figures/v2/tamrfig.sty`
(current `tamr`, `guide`, `series1`); STYLE.md section 16.

The source is unchanged. Under the current style, the axes are ink2 at 0.7pt with 0.55pt ticks. The two guides at
$1/C_1$ and $\beta = 1$ use the `guide` dash (3pt on, 2pt off, ink2). All six curves are s1 at 1pt, each with its own
label. Read off the render (400 px per $1/C_1$), the curve ends at $\beta = 2$ are 0.333, 0.322, 0.277, 0.243,
0.200 and 0.117; these are eq. (48b)'s values. The $\zeta = .2$ and $\zeta = .5$ peaks sit at 2.55 and 1.16
near $\beta$ 0.96 and 0.71. The $\zeta = 0$ branches leave the frame at its top. Each label stays on or just
beside its own curve and clear of the others. The white knock-outs (for $\zeta = .2$ and $\zeta = \sqrt2/2$) cut
only the $\beta = 1$ guide. Minor ticks sit at 0.5, 1.5 and 2.5. The caption (resonance only for
$\zeta < \sqrt2/2$) and the text (the range about $\beta = 1$ above the dashed $1/C_1$ line) hold. The figure has
no panels.

| round-1 # | severity | status | evidence |
|---|---|---|---|
| 1 | note | accepted: known gate item | The tails beyond $\beta \approx 1.6$ and $\zeta = 2$ near $\beta = 0.5$ follow eq. (48b), which the gate item in `corrections/v2-figures.md` covers. The $\zeta = 0$ and $.2$ tails still nearly merge past 1.75, and their labels at the peaks keep them apart. |
| 2 | note | accepted: note, owner's call | The ticks are still 0.25, 0.50 ... (fig25.tex:10), while the curve labels are still ".2" and ".5" (fig25.tex:28-29). Both follow the rules as written. |
| 3 | note | accepted: note, no action | Ch2 Fig 31 is not redrawn yet. This definition can be reused for it. |

## New findings

None.

## Verdict

pass (0 must-fix, 0 should-fix)
