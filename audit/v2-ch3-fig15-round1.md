# v2 audit: ch3/fig15 (round 1)

Sources checked: scan `figures/ch3/fig15.png` (4x crops of the 0.865 dimension's two ends and the x title, and
pixel-row reads of the printed curve at η = 1.0-4.0 with the drafter's gridline calibration); redraw
`figures/v2/ch3/fig15.pdf` (300 dpi render, `pdftotext -bbox`, `pdffonts`) and
`build/v2/png/ch3-fig15-compare.png`; sources `figures/v2/ch3/fig15.tex`, `fig15.py`, `fig15.csv`,
`fig15-marks.csv`, `fig15.calib.json` (and `fig14.py`, which it imports); inventory row `ch3-fig15`
(`figures/v2/inventory.csv`:81); `chapters/ch3-sec3a.tex`:330-336 (eq. (46)), :393-450 (Table 1), :519-552
(citing text, eq. (56), caption); `corrections/v2-figures.md` (Minor: Ch3 Figs 14, 15); `STYLE.md` section 16.

Checks made:
- **Curve.** Eq. (46) with Table 1 gives (η f' − f)/2:

  | η | 1.0 | 1.8 | 2.4 | 3.2 | 5.0 |
  |---|-----|-----|-----|-----|-----|
  | Table 1 by hand | 0.08211 | 0.25253 | 0.41364 | 0.61719 | 0.83723 |
  | `fig15.csv` | 0.08211 | 0.25253 | 0.41364 | 0.61719 | 0.83723 |

  Against my own shooting solution of eq. (51), the whole CSV agrees to 2.3e-5. The curve starts with a
  vertical tangent at the origin and runs to η = 8 at 0.86038.
- **Asymptote.** The dashed line is at (1/2) lim(η − f) = 0.86039 (my ODE: 0.86040). It runs from η = 0 up to
  6.325, where the curve comes within half a line width of it, and the curve continues on it to η = 8. The
  printed lettering 0.865 is kept, which is the logged minor item. On the scan the dashed asymptote sits at
  0.862-0.864, between the two values, so the calibration is sound.
- **Overlay** (`digitize.py overlay`, the drafter's calibration, residual 0.00 px): 321 points, mean 1.74 px,
  95% 4.12 px (0.70 mm), max 5.00 px: **MISMATCH**.
  - Pixel-row reads show that the 1973 curve lies left of eq. (46) between η ≈ 1.2 and 3.2:

    | η | 1.4 | 1.8 | 2.2 | 3.2 |
    |---|-----|-----|-----|-----|
    | printed | 0.13 | 0.215 | 0.34 | 0.607 |
    | eq. (46) | 0.158 | 0.253 | 0.359 | 0.617 |

  - Where the curve is steep the two agree (η = 2.6: 0.465 against 0.468).
  - The inventory note predicts exactly this ("Do not digitize: the printed curve lies up to about 0.04 left").
    The computed curve is right by the approved rule (computed curves are used where the 1973 art differs).
- **Lettering.**
  - All of the inventory's lettering is present. The y title $\eta = y\sqrt{U_\infty/\nu x}$ is rotated, as
    printed, and the x title is $\frac{v}{U_\infty}\sqrt{\frac{U_\infty x}{\nu}}$.
  - y ticks 0-8 step 1; x ticks 0, 0.2, ..., 1.0 with a gridline every 0.1.
  - "0.865" is the label of a `\dimline` along the η = 7 gridline, from the axis to the asymptote, in a gap at
    x ≈ 0.43 (printed at about 0.40).
  - The scan's η = 7 line shows a slight thickening at both ends at 150 dpi, so two heads (the house dimension)
    are a fair reading. The inventory's "arrowhead at the asymptote" is satisfied.
- **Caption and text.**
  - η is the vertical axis.
  - v does not vanish but tends to an asymptotic value (ch3-sec3a.tex:522-526): the curve visibly runs onto
    the dashed asymptote and up to η = 8.
- **Style and size.**
  - The same frame as Fig 14: axes 4.2 x 2.7 in, the same ticks and grids.
  - The curve in s1, the asymptote in `guide`, the value as a `\dimline`.
  - Page 4.98 x 3.47 in; fonts embedded. Nothing overlaps or is clipped: the left head of the dimension sits on
    the y axis, as printed.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | should-fix | The computed curve fails the STYLE §16 overlay target: 95% at 4.12 px (0.70 mm) against 3 px, max 5 px. The 1973 curve lies 0.01-0.04 left of eq. (46) for η ≈ 1.2-3.2 (η = 1.4: 0.13 against 0.158; 1.8: 0.215 against 0.253; 2.2: 0.34 against 0.359; 3.2: 0.607 against 0.617). STYLE §16 requires such a mismatch to go to corrections/v2-figures.md. The current Minor entry "Ch3 Figs 14, 15" records only the 0.865/0.8604 lettering, not the curve offset. The figure itself is right (computed by the approved rule). | corrections/v2-figures.md (Minor); fig15.csv | Orchestrator: add to the Minor entry that Fig 15's printed curve lies up to 0.04 left of eq. (46) between η 1.2 and 3.2 (overlay 95% 4.1 px), computed curve kept. No change to the figure. |
| 2 | note | The asymptote is placed at Table 1's 0.8604 and lettered 0.865 (eq. (56)), the logged minor item under the approved rule. | fig15.tex:22-26; fig15-marks.csv | None. |
| 3 | note | `\pgfplotstableread{...}\marks` redefines the e-TeX primitive `\marks`, and `\let\join` takes a math-symbol-like name. Both are harmless here (the figure compiles and renders correctly), but figure-specific names would be more robust. | fig15.tex:9-11 | Optional: rename to e.g. `\figmarks`, `\vjoin`. |

## Verdict: pass

No must-fix. The curve is eq. (46) with Table 1 exactly. The only open item is the log entry for the curve's
known offset from the 1973 art (finding 1), which is outside the figure's files.
