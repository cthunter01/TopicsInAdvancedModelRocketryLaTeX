# v2 audit: ch3/fig20 (round 1)

Sources checked: scan `figures/ch3/fig20.png` (6x crops of the y and x titles, 2x of the plot); redraw
`figures/v2/ch3/fig20.pdf` (300 dpi render, `pdffonts`) and `build/v2/png/ch3-fig20-compare.png`; sources
`figures/v2/ch3/fig20.tex`, `fig20.py`, `fig20.csv`, `fig20.calib.json` (and `fig14.py`, which it imports);
inventory row `ch3-fig20` (`figures/v2/inventory.csv`:86); `chapters/ch3-sec3b.tex`:550-610 (eqs. (91)-(93),
citing text, caption), :612-631 (worked example, "three-dimensional results ... nosecones"), :664-677 (eqs.
(94)-(96)); `corrections/v2-figures.md` (pilot gate: Mangler's scaling for Ch3 Figs 20, 21(b)); `STYLE.md`
sections 14 and 16.

Checks made:
- **Mangler's scaling.** For a cone r_0 = x sin θ, so x̄ = ∫r_0² dx/L² = x³sin²θ/(3L²) and ȳ = r_0 y/L. Then the
  flat-plate variable ȳ√(U/νx̄) = y√(3U/νx) = √3 η_B, so u/U∞ = f'(√3 η_B) = f'(2√3 η_3). That is `fig20.py`'s
  relation r = 2η f'(2√3 η), the construction of Fig 19 with the cone profile, as the owner decided.
- **Values.**
  - My own ODE solution of eq. (51) gives r = 0.3615, 1.2899, 2.3153, 3.9996 and 5.600 at η = 0.4, 0.8, 1.2,
    2.0 and 2.8.
  - The whole `fig20.csv` agrees with the ODE to 3.6e-5.
  - The curve ends at η = 3.00 at r = 6 (inventory: about 3.0).
- **Worked example** (ch3-sec3b.tex:618-620): 1.73 gives η_k = 0.966 on the redraw against the text's 0.96. The
  text's k_t = 1.66e-4 m follows from 0.96.
- **Overlay** (`digitize.py overlay`, the drafter's calibration, residual 0.00 px): 301 points, mean 0.26 px,
  95% 1.00 px (0.17 mm), max 1.41 px: ok.
- **Lettering.**
  - y title $\eta_{\mathrm{3\text{-}D}}$, upright (printed at about 1.65, here at mid-height).
  - x title $(R_k/\sqrt{R_x})_{\mathrm{3\text{-}D}}$, with the numerator subscript set k per the caption.
  - Ticks 0-3.2 step 0.4 and 0-6 step 1, with the printed grid.
- **Caption.** A cone at zero angle of attack: yes, by Mangler's cone result.
- **Style and size.**
  - Identical frame, ticks, label style and series to Fig 19 (one frame for 19 and 20, as asked).
  - Page 4.92 x 3.28 in; fonts embedded; nothing clipped or overlapping.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | The cone profile comes from outside the book (Mangler's √3 scaling, owner's pilot-gate decision). The overlay passes at 1.0 px, so the "About This Edition" mention promised in corrections/v2-figures.md applies. | fig20.py docstring | None in the figure (About This Edition is a later step). |
| 2 | note | The worked example reads 0.966 on the computed curve against the text's 0.96. That is within chart-reading accuracy, so no note is needed. | ch3-sec3b.tex:618-620 | None. |

## Verdict: pass

No must-fix and no should-fix.
