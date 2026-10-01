# v2 audit: ch3/fig14 (round 1)

Sources checked: scan `figures/ch3/fig14.png` (2x upscale, 4x crop of the δ* dimension); redraw
`figures/v2/ch3/fig14.pdf` (300 and 600 dpi renders, `pdftotext -bbox` label sizes, `pdffonts`) and
`build/v2/png/ch3-fig14-compare.png`; sources `figures/v2/ch3/fig14.tex`, `fig14.py`, `fig14.csv`,
`fig14-marks.csv`, `fig14.calib.json`; inventory row `ch3-fig14` (`figures/v2/inventory.csv`:80);
`chapters/ch3-sec3a.tex`:330-336 (eqs. (45), (46)), :351-363 (eqs. (51)-(53)), :393-450 (Table 1), :455-489
(citing text, caption, eq. (54)); `chapters/ch3-sec3b.tex`:664-677 (Fig 21a = Fig 14 with η halved);
`corrections/v2-figures.md` (Minor: Ch3 Figs 14, 15); `STYLE.md` sections 14 and 16.

Checks made:
- **Curve.** `fig14.csv` against Table 1 at η = 0.6, 1.0, 1.4, 2.0, 3.0, 4.0, 5.0: 0.19894, 0.32979, 0.45627,
  0.62977, 0.84604, 0.95552, 0.99155, the table values to 1e-5. Against my own shooting solution of eq. (51)
  (f''(0) = 0.332057) the whole CSV agrees to 1.7e-5 in f'. The curve runs from the origin to f' = 0.99835 at
  η = 5.79, where it meets the u/U∞ = 1.0 line (the 1973 curve ends near η = 6).
- **Overlay** (`digitize.py overlay`, the drafter's calibration, residual 0.00 px): 241 points, mean 0.14 px,
  95% 1.00 px (0.17 mm), max 1.00 px: ok.
- **Dashed line.** It is drawn at lim(η − f) = 8.8 − 7.07923 = 1.72077 (my ODE: 1.72079) and lettered 1.73 as
  printed. This is the logged minor item, approved.
- **Lettering.**
  - All of the inventory's lettering is present. The y title is $\eta = y\sqrt{U_\infty/\nu x}$ (rotated) and
    the x title $f'(\eta) = u/U_\infty$.
  - y ticks 0-8 step 1; x ticks 0, 0.2, ..., 1.0 with a gridline every 0.1, as printed.
  - "1.73" sits in a gap of the dashed line at x = 0.15, as printed.
  - $\delta^{*}\sqrt{U_\infty/\nu x}$ is a two-headed `\dimline` along the 0.8 gridline from η = 0 to the dashed
    line. Its label knocks out the η = 1 gridline, as printed (the scan shows small heads at both ends).
  - The asterisk is set as $\delta^{*}$, the caption's form; the scan's raised dot is a print artifact.
  - Label sizes: "1.73" and the dimension label are both \small (bbox height 9.01 pt).
- **Caption and text.**
  - η is the vertical axis.
  - The curve is near-linear at the wall and steepens towards U∞ (ch3-sec3a.tex:457-461).
  - δ* ≈ δ/3 (1.72 against δ at η = 5).
  - Fig 21a is this curve with η halved (checked in the Fig 21 audit).
- **Style and size.**
  - The house `tamr grid` with major and minor grids; the curve in s1, 1 pt; the reference level in `guide`
    (dashed); the dimension uses `\dimline`.
  - Axes 4.2 x 2.7 in, the same frame as Fig 15 (and the height of Figs 19-21).
  - Page 4.98 x 3.40 in (≤ 6.5 in); all fonts embedded. Nothing overlaps or is clipped. The dimension's 4 pt
    heads are visible at final size.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | The dashed line is placed at Table 1's 1.7208 and lettered 1.73. This is the logged minor item (corrections/v2-figures.md, Minor, "Ch3 Figs 14, 15") under the approved rule (computed placement, printed lettering kept). | fig14.tex:20-22; fig14-marks.csv | None. |
| 2 | note | `\pgfplotstableread{...}\marks` defines `\marks`, which is the name of an e-TeX primitive (mark classes). The figure compiles and renders correctly, and the LaTeX kernel uses its own `\tex_marks:D` copy, so nothing breaks here. A figure-specific name would be more robust. | fig14.tex:9-10 | Optional: rename it, e.g. `\figmarks`. |

## Verdict: pass

No must-fix. The curve is Table 1 exactly, the overlay on the scan is within 1 px, and every printed label,
the 1.73 reference level and the δ* dimension are present in the house style.
