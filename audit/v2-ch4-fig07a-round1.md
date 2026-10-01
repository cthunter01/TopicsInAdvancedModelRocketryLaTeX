# v2 audit: ch4/fig07a (round 1)

Sources checked: scan `figures/ch4/fig07a.png` (3x and 4x zooms of the left start and the right-hand merge with the
zero line); redraw `figures/v2/ch4/fig07a.pdf` (rendered at 300 and 600 dpi, with crops); source
`figures/v2/ch4/fig07a.tex` lines 1-32; `fig07a.py` lines 1-182 (also the shared helpers `digitize_panel`, `trace`,
`snap`, `smooth`, `to_data`); `fig07a.csv` (378 rows); `fig07a.calib.json`. Other sources: inventory row
`ch4-fig07a` (`figures/v2/inventory.csv`:132); float and caption `chapters/ch4-sec2b.tex`:425-431; the collective
text and key table :306-372 (D4: k_min = .00007, k_max = .0027); `corrections/v2-figures.md`:82-84 (Figs 5, 7-10,
12-14 digitized); the approved template `figures/v2/ch4/fig06a.tex` and its round-2 audit.

Reruns:
- I ran `fig07a.py` on a copy in the scratch directory (with symlinks to the crops and `tools/v2`). The CSV it writes is
  byte-identical to the repository's.
- I ran `tools/v2/digitize.py overlay` on the four curves, split from the CSV. 95% of the points are within 0.00 px
  for FM k_min and FM k_max and 2.00 px for CB k_min and CB k_max (the gaps between dashes). The maxima are 1.0, 0.0,
  3.0 and 2.24 px. All pass.
- Calibration: the y residual of the affine fit is 1.15 px at most. The x mapping is piecewise between the drawn
  ticks (`xgrid`).

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | Over its first printed dash, the CB k_min curve starts about 0.35 point below the print. The first dash (cols 84-89) runs from -4.35 at $m_o$ = 0.0316 to -4.63 at 0.0327. The CSV starts at -4.78 at 0.0319 and is -4.9 at 0.033. From the second dash onwards it is on the ink. This first dash is the 3.0 px maximum in the overlay. At final size the offset is about 0.6 mm over a 1 mm stretch. The print's small down-turn at the start is lost; the smoothing spline does not follow a single dash. | fig07a.csv rows 7-14; fig07a.py:176-178 | Optional: add the first dash's centre, e.g. `extra=[(84.5, 190.6), (88, 192)]`, to `cb_kmin`. Otherwise leave as is (the overlay passes). |
| 2 | note | From about 0.104 kg the FM k_min solid runs 0.03-0.15 point under the zero line (-0.15 at the end), where the print draws the two as one line. The offset is within the calibration's 1.15 px residual. At final size the blue line still overlaps the grey zero line along its whole length (0.25 mm offset, 1 pt line). | fig07a.csv rows from m0 0.104 | None needed. |

Also checked, with no issue:
- **Frame and axes.** The frame is identical to fig06a. The axis box is 2403 x 1501 px at 600 dpi (4.00 x 2.50 in),
  the same as the template, and the page is 340.5 x 219.9 pt.
- **Ticks and titles.** x runs 0.03-0.13, labelled at the odd hundredths with minor ticks at the even ones, as
  printed. y runs -15 to 15 in steps of 5, with true minus signs. The titles are "Percent error in $v_b$" and
  "$m_o$ (kg)".
- **Zero line.** The thin muted zero line runs the full width, as printed (the print's zero line runs on past the
  curves to 0.13).
- **Legend.** The legend is at the upper right as printed: solid "Fehskens-Malewicki", dashed "Caporaso-Bengen", in
  the template's style.
- **k labels.** The $k_{\max}$ and $k_{\min}$ labels are at the printed places: $k_{\max}$ at about (0.096, 3.3)
  between FM k_max and CB k_max, and $k_{\min}$ at about (0.036, -1.6). Their four leader ends lie on the intended
  CSV curves within 0.002 point: FM k_max 5.991, CB k_max 0.966, FM k_min 3.086, CB k_min -5.025.
- **Curve identities.** The curves are identified as in the print and the inventory: FM k_max 4.9 -> 6.0 -> 5.9;
  CB k_max 4.4 -> -1.5; FM k_min 3.6 -> 0; CB k_min min -5.5 near 0.045, then up to -1.9.
- **Extents.** The curves end at the printed ends (about 0.031-0.124).
- **Style.** The data curves are series1/series2 (s1 solid = FM, s2 dashed = CB). Leaders use the `leader` style and
  the labels are \footnotesize in ink. No panel letter is drawn in the art (`\figurepanel{a}` supplies it, as for
  fig06a). There is no grid and no local style.
- **Captions and text.** The caption ("Burnout velocity error ... Type D4 engine") and the text's "referred to as
  $k_{\min}$/$k_{\max}$ in the figures" hold for the redraw. The text's 10% claim is a logged v1 question, not a
  figure issue.

## Verdict

pass (0 must-fix, 0 should-fix, 2 notes)
