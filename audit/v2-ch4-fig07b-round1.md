# v2 audit: ch4/fig07b (round 1)

Sources checked: scan `figures/ch4/fig07b.png` (3x and 5x zooms of the label and leader area); redraw
`figures/v2/ch4/fig07b.pdf` (rendered at 300 and 600 dpi, with a crop of the leaders); source
`figures/v2/ch4/fig07b.tex` lines 1-32; `fig07b.py` lines 1-42 (with the helpers it imports from `fig07a.py`);
`fig07b.csv` (377 rows); `fig07b.calib.json`. Other sources: inventory row `ch4-fig07b`
(`figures/v2/inventory.csv`:133); float and caption `chapters/ch4-sec2b.tex`:433-439; the collective text and key
table :306-372; `corrections/v2-figures.md`:82-84; the template `fig06a.tex` and its round-2 audit.

Reruns:
- I ran `fig07b.py` on a copy in the scratch directory. The CSV it writes is byte-identical to the repository's.
- I ran the overlay of the four curves. 95% of the points are within 0.00 px for FM k_min and FM k_max and 2.00 px
  for CB k_min and CB k_max. The maxima are 2.24, 0.0, 2.24 and 4.12 px. All pass.
- Calibration: the y residual is 0.71 px at most.

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | Two leaders cross a curve before reaching their own, as in the print. The $k_{\min}$ leader to FM k_min crosses the CB k_max dashed curve (at $m_o$ = 0.042, the dashed curve is at -3.56 and the solid at -2.69: about 1.4 mm apart at final size). The $k_{\max}$ leader to CB k_max crosses the FM k_min solid (at 0.065: -5.69 against -6.68, about 1.6 mm apart). In both cases the crossed line has the other method's line style. The leader runs on clearly past it, so the target reads correctly. This is the same pattern the fig06a round-2 audit accepted. | fig07b.tex:24-29 | None needed. |

Also checked, with no issue:
- **Frame and axes.** The frame is identical to fig06a (axis box 2403 x 1501 px at 600 dpi). x runs 0.03-0.13,
  labelled at the odd hundredths with minor ticks at the even ones. y runs -15 to 15 in steps of 5. The titles are
  "Percent error in $y_b$" and "$m_o$ (kg)".
- **Zero line.** The thin zero line runs the full width, as printed.
- **Legend.** The legend is at the upper right, as printed.
- **k labels.** $k_{\max}$ is at (0.0696, -4.27) and $k_{\min}$ at (0.0426, -5.89). The print has them at about
  (0.069, -4.5) and (0.043, -6.4).
- **Leader ends.** The leader ends lie on the intended curves within 0.005 point: FM k_max -1.920, CB k_max -6.683,
  FM k_min -2.690, CB k_min -7.870. The print's leaders reach the same four curves (zoom at 5x).
- **Curve identities.** The curves match the print and the inventory:
  - FM k_max crosses zero near 0.04 and ends at -5.8.
  - FM k_min runs from -0.5 to -9.8.
  - CB k_max runs from -1.8 to -12.0.
  - CB k_min runs from -7.3 to -10.6.
  - The two dashed curves cross near 0.088.
- **Faint dashes.** The faint dashes at 0.045-0.07 sit on the CB k_max trace (overlay at 2x).
- **Style.** The house style and the template's legend, leaders, zero line and type are followed. No panel letter is
  drawn in the art (`\figurepanel{b}`).
- **Captions and text.** The caption ("Burnout altitude error ... Type D4 engine") holds for the redraw. The errors to
  -12% exceed the text's 10% claim; that is the logged v1 question (corrections/v2-figures.md:387), not a figure
  issue.

## Verdict

pass (0 must-fix, 0 should-fix, 1 note)
