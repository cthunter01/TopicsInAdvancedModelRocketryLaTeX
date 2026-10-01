# v2 audit: ch2/fig23 (round 1)

Sources checked: figures/ch2/fig23.png (scan); figures/v2/ch2/fig23.pdf (current build: 4.76 x 2.86 in, all
fonts embedded; rendered at 400 dpi) and build/v2/png/ch2-fig23-compare.png; figures/v2/ch2/fig23.tex, fig23.py,
fig23.csv, fig23.calib.json; figures/v2/inventory.csv row ch2-fig23; caption chapters/ch2-sec3b.tex:187-191;
citing text ch2-sec3b.tex:167-182 (eq. (40)) and 240-265 (eqs. (43a), (43b)); eqs. (24)-(26) at
ch2-sec3a.tex:362-427; STYLE.md sections 13 and 16; corrections/v2-figures.md; approved examples ch1/fig03.tex,
ch2/fig25.tex; siblings Figs 21, 22.

Checked and correct:
- Lettering: $\alpha_X$ (rad) and $t$ (sec) titles; y ticks $0$ and $\alpha_{Xm}$; t tick $t_m$; "Slope $=
  \dfrac{H}{I_L}$". Below the plot, in the printed order:
  $\alpha_{Xm} = \frac{H\tau_1\tau_2}{I_L(\tau_1-\tau_2)}\bigl[(\tau_1/\tau_2)^{-\frac{\tau_2}{\tau_1-\tau_2}}
  - (\tau_1/\tau_2)^{-\frac{\tau_1}{\tau_1-\tau_2}}\bigr]$, which is eq. (43b) exactly (exponent signs and
  fractions as the inventory reads them). Then $t_m = \frac{\tau_1\tau_2\ln(\tau_1/\tau_2)}{\tau_1-\tau_2}$,
  which is eq. (43a) with the slashed fraction as lettered (the inventory's reading). I checked independently that
  (43b) follows from (40) at (43a): $e^{-t_m/\tau_1} = (\tau_1/\tau_2)^{-\tau_2/(\tau_1-\tau_2)}$. Nothing
  added.
- Curve: eq. (40) with $\tau_1 = 3.0748$, $\tau_2 = 0.3252$ by eq. (25) at $\zeta = 1.7$, in units of
  $1/\omega_n$ and $H/(I_L\omega_n)$. fig23.csv agrees with the formula to $5\times10^{-6}$, and fig23.py reruns
  to a byte-identical CSV. The initial slope is $K(1/\tau_2 - 1/\tau_1) = 1 = H/I_L$, so the drawn line
  $\alpha = t$ is the true tangent.
- Marks: $t_m = 0.8170$, $\alpha_{Xm} = 0.2493$ by eqs. (43a), (43b), at the numerical maximum. The dashed
  guides meet at the drawn peak.
- Caption comparison with Fig 22 (same rocket, larger $C_2$, same axis scale), all true: the maximum is sooner
  ($t_m$ 0.817 against 1) and smaller ($\alpha_{Xm}$ 0.249 against 0.368), and the return is more gradual
  ($\alpha_X(8.3) = 0.0245$, still clearly above the axis, against Fig 22's 0.0021). The curve is still above 0
  at the right edge, as printed.
- Overlay on the scan. `main` calibration: mean 2.18 px, 95% 5.00 px (0.85 mm). `fit` calibration: mean
  0.77 px, 95% 3.61 px (0.61 mm). The computed shape follows the 1973 curve closely.
- Style and legibility: the conventions are identical to Figs 21 and 22. The width is 4.76 in. Nothing overlaps or
  is clipped. The exponent fractions are tiny (see finding 2) but legible.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | The shared axis scale and $\zeta = 1.7$ (a fit of eq. (40)'s shape to this scan) give $t_m$ and $\alpha_{Xm}$ 0.82 and 0.68 of Fig 22's. On the scans the ratios are about 0.90 and 0.88. Matching those ratios would need $\zeta \approx 1.2$, but then the tail would be on the axis by the right edge ($\alpha/\alpha_{Xm} = 0.03$), while the scan shows about 0.14 (12 px above the axis at column 500, against 84 px for $\alpha_{Xm}$; the computed curve gives 0.10-0.15 over the last part of the axis). The 1973 pair is not self-consistent. The drafter's choice keeps the printed shape and makes the caption's "more gradual" plain. A side effect: the curve uses only the lower third of the axis height (peak 0.45 in of 1.44 in). | fig23.py:113-114; fig23.tex:83 | None needed. Optional: lower `ymax` and the tangent top together in Figs 22 and 23 (e.g. ymax 0.7, `\ts` 0.58) to tighten the empty upper area without changing the shared scale. |
| 2 | note | The exponent fractions $\frac{\tau_2}{\tau_1-\tau_2}$, $\frac{\tau_1}{\tau_1-\tau_2}$ are at scriptscript size of `\small` (about 5 pt). The chapter's eq. (43b) is 6 pt and the 1973 lettering is tinier still. | fig23.tex:93-99 | Optional: `\normalsize` for the formula nodes of Figs 21-23 alike. |
| 3 | note | Per STYLE.md section 16 the overlay mismatch (95% above 3 px) belongs in corrections/v2-figures.md, which the drafter cannot write. | corrections/v2-figures.md | For the orchestrator: one minor line for Figs 21-23. |

## Verdict

pass (0 must-fix, 0 should-fix)
