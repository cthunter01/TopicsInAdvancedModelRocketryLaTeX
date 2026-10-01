# v2 audit: ch3/fig15 (round 2)

Sources checked: scan `figures/ch3/fig15.png` (the overlay image, and `digitize.py lines` for the gridline
calibration); redraw `figures/v2/ch3/fig15.pdf` (300 dpi render, crops of both dimension ends,
`pdftotext -bbox`, `pdffonts`, `pdfinfo`); sources `figures/v2/ch3/fig15.tex`, `fig15.py`, `fig15.csv`,
`fig15-marks.csv`, `fig15.calib.json` (and `fig14.py`, which it imports); inventory row `ch3-fig15`
(`figures/v2/inventory.csv`:81); `chapters/ch3-sec3a.tex`:335 (eq. (46)), Table 1, :519-552 (citing text,
eq. (56), caption); `corrections/v2-figures.md`:142 (Minor); `STYLE.md` section 16; the round-1 audit and fix
records.

Checks made:
- **Round-1 items.**
  - Finding 3 (optional rename of `\marks` and `\join`) is resolved: `fig15.tex`:9-11 use `\figmarks` and
    `\vjoin`. Before the figure defines them, `\figmarks`, `\vinf` and `\vjoin` are all undefined after
    `\usepackage{tamrfig}`, so nothing is overwritten.
  - Finding 1 (should-fix, assigned to the orchestrator) is still open. It asked for the 1973 curve's offset
    from eq. (46) to be logged. `corrections/v2-figures.md`:142-143 still record only the 0.865/0.8604 lettering.
    The fixer declined it correctly (corrections/ is outside the figure's files) and passed it on in its doubts.
    It is carried forward below.
- **Regression.**
  - The current source compiles cleanly in my scratch directory.
  - Its 300 dpi render is pixel-identical to the PDF in the tree and to the round-1 auditor's render.
- **Data.**
  - I re-ran `fig15.py` in a scratch copy. `fig15.csv` and `fig15-marks.csv` are byte-identical.
  - Against my own ODE solution of eq. (51), (η f' − f)/2 agrees with the whole CSV to 2.3e-5.
  - Spot values (ODE): η = 1.0: 0.0821; 1.4: 0.1579; 1.8: 0.2525; 2.2: 0.3588; 3.2: 0.6172; 5.0: 0.8372.
  - The asymptote is at 0.86039 (ODE 0.86039) and the curve joins it at η = 6.325. Lettered 0.865, the logged
    minor item.
- **Overlay** (`digitize.py overlay`, the drafter's calibration, residual 0.00 px): 321 points, mean 1.74 px,
  95% 4.12 px (0.70 mm), max 5.00 px: **MISMATCH**.
  - These are the round-1 numbers. The calibration is sound: `digitize.py lines` finds the scan's η gridlines
    within 0.5 px of `fig15.calib.json`.
  - The overlay image shows the 1973 curve left of eq. (46) for η about 1.2-3.2, as the inventory note predicts.
  - The computed curve is correct by the approved rule.
- **Lettering and caption.**
  - Everything printed is present: the rotated η title, $\frac{v}{U_\infty}\sqrt{\frac{U_\infty x}{\nu}}$,
    ticks 0-8 and 0-1.0.
  - "0.865" is the label of a two-headed `\dimline` along η = 7, from the axis to the asymptote. Both heads
    are visible at 300 dpi; the right head touches the curve where it lies on the asymptote.
  - The text's "v does not vanish but attains an asymptotic value" is visible: the curve runs onto the dashed
    line and up to η = 8.
- **Size.** Page 4.98 x 3.47 in; fonts embedded; nothing clipped or overlapping.
- **Family.** Same frame as Fig 14.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | should-fix | Still open from round 1 (orchestrator, not a figure change). The computed curve misses the STYLE §16 overlay target: 95% 4.12 px (0.70 mm), max 5 px. STYLE §16 requires such a mismatch to go to `corrections/v2-figures.md`, and the Minor entry at line 142 still records only the 1.73/0.865 lettering. | corrections/v2-figures.md:142-143 | Orchestrator: extend the Minor entry "Ch3 Figs 14, 15". Record that Fig 15's 1973 curve lies up to 0.04 left of eq. (46) for η 1.2-3.2 (η = 1.4: 0.13 vs 0.158; 1.8: 0.215 vs 0.253; 2.2: 0.34 vs 0.359; 3.2: 0.607 vs 0.617), that the overlay is 95% 4.1 px, and that the computed curve is kept. No change to the figure files. |
| 2 | note | Round-1 optional item resolved: `\figmarks` and `\vjoin` replace `\marks` and `\join`. The render is unchanged. | fig15.tex:9-11 | None. |
| 3 | note | The asymptote is at the computed 0.8604 and lettered 0.865 (eq. (56)), the logged minor item, approved. | fig15-marks.csv; fig15.tex:21-24 | None. |

## Verdict: pass

No must-fix. The figure is correct and unchanged since round 1. The one open item is the orchestrator's log
entry for the known offset of the 1973 art (finding 1), which needs no change to the figure.
