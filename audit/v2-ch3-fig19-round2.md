# v2 audit: ch3/fig19 (round 2)

Sources checked: scan `figures/ch3/fig19.png`; redraw `figures/v2/ch3/fig19.pdf` (300 dpi render, `pdffonts`,
`pdfinfo`); sources `figures/v2/ch3/fig19.tex`, `fig19.py`, `fig19.csv`, `fig19.calib.json` (and `fig14.py`);
inventory row `ch3-fig19` (`figures/v2/inventory.csv`:85); `chapters/ch3-sec3b.tex`:553-598 (eqs. (91)-(93),
citing text, caption), :612-624 (worked example), :660-677 (eqs. (94)-(96)); `chapters/ch3-sec3a.tex` (eq. (45),
Table 1); `STYLE.md` sections 14 and 16; the approved `figures/v2/ch3/fig02.tex` (upright short y label); the
round-1 audit and fix records.

Checks made:
- **Round-1 items.** There were none (one note, no action).
- **Regression.**
  - `fig19.tex` and `fig19.py` are unchanged since round 1 (21:47 and 21:49, before the round-1 report).
  - The current source compiles cleanly in my scratch directory. Its 300 dpi render is pixel-identical to the
    PDF in the tree and to the round-1 auditor's render.
- **Derivation.** By (91), k = 2xη_k/√R_x; by (92), R_k = k u_k/ν; and by (96) and (45), u_k = U∞ f'(2η_k). So
  R_k/√R_x = 2η_k f'(2η_k).
- **Data.**
  - I re-ran `fig19.py` in a scratch copy. `fig19.csv` is byte-identical.
  - Against my own ODE solution of eq. (51), the whole CSV agrees to 4.3e-5 (r = 0.2118, 0.8268, 1.7496,
    3.8221, 5.5859 at η 0.4, 0.8, 1.2, 2.0, 2.8).
  - The curve ends at η = 3.003 at r = 6.
- **Worked example** (ch3-sec3b.tex:618-620). 1.73 gives η_k = 1.192 (text 1.20, reading accuracy). With the
  text's x = 0.03 m and R_x = 1.206e5, eq. (93) gives k_t = 2.07e-4 m from 1.20 (text 2.08e-4).
- **Overlay** (`digitize.py overlay`, the drafter's calibration, residual 0.00 px): 301 points, mean 0.54 px,
  95% 1.41 px (0.24 mm), max 2.24 px: ok.
- **Lettering.**
  - y title $\eta_{\mathrm{2\text{-}D}}$, upright at mid-height, set as in the approved Ch3 Fig 2.
  - x title $(R_k/\sqrt{R_x})_{\mathrm{2\text{-}D}}$, with the indistinct numerator subscript set k per the
    caption.
  - Ticks 0-3.2 step 0.4 (with "2.0") and 0-6 step 1, and the grid at the printed spacing. The scanner speck
    is not drawn.
- **Size.** Page 4.92 x 3.28 in; fonts embedded; nothing clipped or overlapping.
- **Family.** Identical frame, ticks and label treatment to Fig 20.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | No round-1 items to resolve. The figure, data and render are unchanged and re-verified independently (CSV to 4.3e-5, overlay 95% 1.41 px). | fig19.* | None. |

## Verdict: pass

No must-fix and no should-fix.
