# v2 audit: ch2/fig25 (round 1)

Sources checked: scan `figures/ch2/fig25.png` (2x upscale); redraw `figures/v2/ch2/fig25.pdf` (350 dpi render) and
`build/v2/png/ch2-fig25-compare.png`; source `figures/v2/ch2/fig25.tex` lines 1-36; inventory row `ch2-fig25`
(`figures/v2/inventory.csv`:38); `chapters/ch2-sec3b.tex`:430-442 (eqs. (46)-(48b)), :449-479 (citing text,
caption), :481-521 (resonance text, d(AR)/d(beta), eqs. (49a), (50)); `chapters/ch2-sec3d.tex`:419-422 (Fig 31
identical); `corrections/v2-figures.md` (Ch2 Fig 25 gate item); `STYLE.md` section 16.

Checks made:
- **Formula.** Line 23 plots $1/\sqrt{(\beta^2-1)^2+(2\zeta\beta)^2}$. That is eq. (48b) in units of $1/C_1$. The
  $\zeta = 0$ branches (lines 20-21) plot $1/|1-\beta^2|$ and leave the frame at $3/C_1$ exactly:
  $\beta = \sqrt{2/3} = 0.8165$ and $\sqrt{4/3} = 1.1547$.
- **Points evaluated** (in units of $1/C_1$, for $\zeta$ = .2, .5, $\sqrt2/2$, 1, 2); the render agrees with each:
  - $\beta = 0.5$: 1.288, 1.109, 0.970, 0.800, 0.468 ($\zeta = 0$: 1.333)
  - $\beta = 1.5$: 0.721, 0.512, 0.406, 0.308, 0.163 ($\zeta = 0$: 0.800)
  - $\beta = 2$: 0.322, 0.277, 0.243, 0.200, 0.117 ($\zeta = 0$: 0.333)
- **Resonance peaks.** Eq. (49a) with eq. (50) gives 2.552 at $\beta = 0.959$ for $\zeta = .2$ and 1.155 at 0.707
  for $\zeta = .5$. The drawn peaks match, and so does the inventory.
- **Caption and text.**
  - The $\zeta = \sqrt2/2$ curve, $1/\sqrt{1+\beta^4}$, is flat at $\beta = 0$ and falls monotonically, so there is
    no peak. Curves above $\sqrt2/2$ do not rise either. The caption holds.
  - "A range of $\beta$ about 1 where $\mathit{AR} > 1/C_1$": $\zeta = .5$ recrosses the dashed $1/C_1$ line exactly at
    $\beta = 1.00$, at the crossing of the two guides; $\zeta = .2$ recrosses at 1.356 and $\zeta = 0$ at 1.414.
    The dashed $1/C_1$ line is the value at $\beta = 0$.
- **Lettering.**
  - y title $\mathit{AR}$ [rad/(dyn-cm)] (the text's notation for amplitude ratio). y ticks 0, $\frac1{C_1}$,
    $\frac2{C_1}$, $\frac3{C_1}$, with minor ticks at 0.5, 1.5 and 2.5.
  - x title $\beta$; x ticks 0 to 2.00 in steps of 0.25.
  - Six curve labels. The ones set on their curves are placed exactly on them (1.06, 0.667 / 0.62, 0.722 /
    0.30, 0.664 all satisfy eq. (48b)).
  - Dashed guides at $1/C_1$ and $\beta = 1$.
- **Legibility.** No label touches another curve. The knock-outs of $\zeta = .2$ and $\zeta = \sqrt2/2$ interrupt
  only the $\beta = 1$ guide, not a curve. Six curves in one colour with a label on each follows STYLE section 16
  (the ordinal ramp is limited to five curves).

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | Known gate item: beyond $\beta \approx 1.6$ the computed tails lie below the 1973 art, and $\zeta = 2$ differs near $\beta = 0.5$. As a result the $\zeta = 0$ and $\zeta = .2$ tails nearly merge past $\beta \approx 1.75$ (0.333 against 0.322 at 2.00). This is correct by eq. (48b), and the labels at the peaks keep the two identifiable. | fig25.tex:20-24 | none (gate) |
| 2 | note | The tick labels use leading zeros (0.25, 0.50 ...) per STYLE section 16, while the printed curve labels keep ".2" and ".5". This follows the rules as written, but the figure mixes the two forms. | fig25.tex:10, 28-29 | Owner's call: $\zeta = 0.2$, $0.5$ would make the figure consistent. |
| 3 | note | Fig 31 ($\mathit{AR}_c$ against $\beta_c$) can reuse this definition, as the inventory says. | - | - |

## Verdict

pass (0 must-fix, 0 should-fix)
