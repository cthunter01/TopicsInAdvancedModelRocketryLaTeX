# v2 audit: ch3/fig19 (round 1)

Sources checked: scan `figures/ch3/fig19.png` (6x crop of the x title, 2x of the plot); redraw
`figures/v2/ch3/fig19.pdf` (300 dpi render, `pdffonts`) and `build/v2/png/ch3-fig19-compare.png`; sources
`figures/v2/ch3/fig19.tex`, `fig19.py`, `fig19.csv`, `fig19.calib.json` (and `fig14.py`, which it imports);
inventory row `ch3-fig19` (`figures/v2/inventory.csv`:85); `chapters/ch3-sec3b.tex`:550-598 (eqs. (91)-(93),
citing text, caption), :612-624 (worked example), :660-677 (eqs. (94)-(96)); `chapters/ch3-sec3a.tex`
(eq. (45), Table 1); `corrections/v2-figures.md`; `STYLE.md` sections 14 and 16.

Checks made:
- **Derivation.** From (91) k = 2xη_k/√R_x, from (92) R_k = k u_k/ν, and with R_x = U∞x/ν:
  R_k/√R_x = 2η_k u_k/U∞. By (96) the Blasius variable at y = k is 2η_k, so u_k/U∞ = f'(2η_k) (eq. (45)). This is
  `fig19.py`'s relation r = 2η f'(2η).
- **Values.**
  - My own ODE solution of eq. (51) gives r = 0.2118, 0.8268, 1.7496, 3.8221 and 5.5859 at η = 0.4, 0.8, 1.2,
    2.0 and 2.8.
  - The whole `fig19.csv` agrees with the ODE to 4.7e-5.
  - The curve has a vertical tangent at the origin and ends at η = 3.003 at r = 6 (inventory: about 2.96 at 6).
- **Worked example** (ch3-sec3b.tex:618-620): (R_k)_t/√R_x = 1.73 gives η_k = 1.19 on the redraw. The text reads
  1.20 off the chart, which is within reading accuracy.
- **Overlay** (`digitize.py overlay`, the drafter's calibration, residual 0.00 px): 301 points, mean 0.54 px,
  95% 1.41 px (0.24 mm), max 2.24 px: ok.
- **Lettering.**
  - y title $\eta_{\mathrm{2\text{-}D}}$, upright at mid-height left of the ticks (printed at about 1.65).
  - x title $(R_k/\sqrt{R_x})_{\mathrm{2\text{-}D}}$. The numerator subscript is indistinct in the scan and is
    set k per the caption and text; R is the Reynolds number per STYLE §14.
  - y ticks 0, 0.4, ..., 2.0, ..., 3.2 (with "2.0" as printed) and x ticks 0-6, with major gridlines at the
    printed spacing (1 and 0.4).
  - The stray speck near (3.2, 2.5) is correctly not reproduced.
- **Caption.** η_k is plotted against R_k/√R_x for a flat plate: yes.
- **Style and size.**
  - `tamr grid`, curve in s1, upright short y label as in the approved Ch3 Fig 2.
  - Axes 4.2 x 2.7 in, the same frame as Fig 20.
  - Page 4.92 x 3.28 in; fonts embedded; nothing clipped or overlapping.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | The relation r = 2η f'(2η) is not printed in the book but follows from eqs. (91), (92), (94)-(96) and (45). The script names them, and the text's example (1.20) is reproduced to reading accuracy (1.19). | fig19.py docstring | None. |

## Verdict: pass

No must-fix and no should-fix.
