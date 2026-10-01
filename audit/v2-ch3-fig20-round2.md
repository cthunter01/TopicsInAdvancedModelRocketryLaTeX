# v2 audit: ch3/fig20 (round 2)

Sources checked: scan `figures/ch3/fig20.png` (and `digitize.py lines` for the gridline calibration); redraw
`figures/v2/ch3/fig20.pdf` (300 dpi render, `pdffonts`, `pdfinfo`); sources `figures/v2/ch3/fig20.tex`,
`fig20.py`, `fig20.csv`, `fig20.calib.json` (and `fig14.py`); inventory row `ch3-fig20`
(`figures/v2/inventory.csv`:86); `chapters/ch3-sec3b.tex`:553-610, :612-631, :660-677;
`corrections/v2-figures.md` (pilot gate: Mangler's scaling for Ch3 Figs 20, 21(b)); `STYLE.md` sections 14 and
16; the round-1 audit and fix records.

Checks made:
- **Round-1 items.** There were none (two notes, no action). Naming Mangler in About This Edition is a later step.
- **Regression.**
  - `fig20.tex` and `fig20.py` are unchanged since round 1.
  - The current source compiles cleanly in my scratch directory. Its 300 dpi render is pixel-identical to the
    PDF in the tree and to the round-1 auditor's render.
- **Mangler's scaling**, rederived. For a cone, r_0 = x sin θ, so x̄ = x³sin²θ/(3L²) and ȳ = r_0 y/L. Then
  ȳ√(U∞/νx̄) = √3 η_B, and u/U∞ = f'(2√3 η) in the η of eq. (94). This is `fig20.py`'s
  r = 2η f'(2√3 η).
- **Data.**
  - I re-ran `fig20.py` in a scratch copy. `fig20.csv` is byte-identical.
  - Against my own ODE solution, the whole CSV agrees to 3.3e-5 (r = 0.3615, 1.2899, 2.3153, 3.9996, 5.600 at
    η 0.4, 0.8, 1.2, 2.0, 2.8).
  - Above η ≈ 2.5 the curve is the straight line η = r/2 (f' = 1), ending at (6, 3.00), as printed.
- **Worked example.** 1.73 gives η_k = 0.966 (text 0.96). Eq. (93) with 0.96 gives k_t = 1.66e-4 m, as the
  text says.
- **Overlay** (`digitize.py overlay`, the drafter's calibration, residual 0.00 px): 301 points, mean 0.26 px,
  95% 1.00 px (0.17 mm), max 1.41 px: ok. `digitize.py lines` finds the scan's gridlines within 1 px of the
  calibration.
- **Lettering.**
  - $\eta_{\mathrm{3\text{-}D}}$ upright at mid-height.
  - $(R_k/\sqrt{R_x})_{\mathrm{3\text{-}D}}$ (k per the caption).
  - Ticks 0-3.2 step 0.4 and 0-6 step 1, with the printed grid.
- **Size.** Page 4.92 x 3.28 in; fonts embedded; nothing clipped.
- **Family.** Identical to Fig 19's frame.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | No round-1 items to resolve. The figure, data and render are unchanged and re-verified (Mangler's √3 rederived; CSV to 3.3e-5; overlay 95% 1.00 px). | fig20.* | None. |
| 2 | note | The cone profile is from outside the book (owner-approved). It is to be named in About This Edition at a later step. | fig20.py docstring | None in the figure. |

## Verdict: pass

No must-fix and no should-fix.
