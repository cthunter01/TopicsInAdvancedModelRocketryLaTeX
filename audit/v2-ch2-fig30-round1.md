# v2 audit: ch2/fig30 (round 1)

Sources checked: scan `figures/ch2/fig30.png` (3x upscale of the left half); redraw `figures/v2/ch2/fig30.pdf`
(300 dpi render) and `build/v2/png/ch2-fig30-compare.png`; `figures/v2/ch2/fig30.tex` lines 1-45, `fig30.py`,
`fig30.csv`, `fig30-z0.csv`, `fig30.calib.json`; inventory row `ch2-fig30` (`figures/v2/inventory.csv`:43);
`chapters/ch2-sec3d.tex`:405-406 (eqs. (73a), (73b)), :419-422 (the curves are "identical to" Figs 24 and 25),
:424-430 (caption); `chapters/ch2-sec3b.tex`:455-462 (the extended-arctangent convention); `corrections/v2-figures.md`
(standing rule 2: $\varphi_c$); `figures/v2/ch2/fig24.tex` (the sibling); `STYLE.md` sections 13, 16.

Checks made:
- **Formula.** `fig30.py` computes eq. (73a) with the arctangent extended as for Fig 24:
  $\varphi_c = -\mathrm{atan2}(2\zeta_c\beta_c,\,1-\beta_c^2)$. I checked all 1121 rows of `fig30.csv`
  independently: the largest difference is $5\times10^{-6}$ rad. `fig30.csv` and `fig30-z0.csv` are identical
  to Fig 24's data, which is what the text's "identical to" requires.
- **Points evaluated.** They are the same as for Fig 24 (e.g. $\beta_c = 2$: $-2.881$, $-2.554$, $-2.386$,
  $-2.214$, $-1.930$ for $\zeta_c$ = .2 to 2). The render agrees.
- **Lettering.** The redraw keeps the figure's own symbols, as printed:
  - y title $\varphi_c$ (rad). Eq. (73a) and the text write $\varphi$, and standing rule 2 keeps the figure's
    form.
  - x title $\beta_c$.
  - Curve labels $\zeta_c = 0$ (beside the drop) and $\zeta_c = 2, 1, \sqrt2/2, .5, .2$ at the right ends, in
    the printed order.
  - y ticks 0 to $-\pi$ in $\pi/4$ steps, with minor ticks at the odd multiples of $\pi/8$; x ticks 0 to 2.00.
  - The subscripts are italic, as STYLE section 13 requires for letter subscripts.
- **Caption.** It asks for the "coupled phase angle" against the "coupled frequency ratio": the axes are
  $\varphi_c$ and $\beta_c$.
- **Overlay** (computed curves, the drafter's calibration). The 95th percentile is 2.00, 2.24, 1.41, 2.00 and
  2.00 px for $\zeta_c$ = .2 to 2, and 0.85 px for the step. Every curve is within 3 px.
- **Legibility.** No overlaps; nothing is clipped. The widest label, $\zeta_c = \sqrt2/2$, ends inside the
  bounding box. The figure is 5.43 in wide, and all fonts are embedded.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | The inventory says the printed $-\pi/2$ line runs past $\beta_c = 2$. The guide stops at 2.00, as in the approved Fig 25 and in Fig 24. | fig30.tex:23 | none |
| 2 | note | This is Fig 24 with c subscripts: the data files are byte-identical, and the label positions and layout are the same. Any change made to Fig 24 in review should be mirrored here. | fig30.tex, fig30.py | Keep the two in step |

## Verdict

pass (0 must-fix, 0 should-fix)
