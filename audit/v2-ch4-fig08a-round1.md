# v2 audit: ch4/fig08a (round 1)

Sources checked: scan `figures/ch4/fig08a.png` (5x zoom of the k_min drop and both label areas); redraw
`figures/v2/ch4/fig08a.pdf` (rendered at 300 and 600 dpi, with a crop of 0.10-0.26); source
`figures/v2/ch4/fig08a.tex` lines 1-33; `fig08a.py` lines 1-54 (with the helpers it imports from `fig07a.py`);
`fig08a.csv` (344 rows); `fig08a.calib.json`. Other sources: inventory row `ch4-fig08a`
(`figures/v2/inventory.csv`:135); float and caption `chapters/ch4-sec2b.tex`:449-457 (transonic drag divergence
below 0.17 kg, k_min cases); the collective text and key table :306-372 (F100: k_min = .00012, k_max = .0045);
`corrections/v2-figures.md`:82-84; the template `fig06a.tex`.

Reruns:
- I ran `fig08a.py` on a copy in the scratch directory. The CSV it writes is byte-identical to the repository's.
- I ran the overlay of the four curves. 95% of the points are within 0.00 px for FM k_min and FM k_max and 2.00 px
  for CB k_min and CB k_max. The maxima are 1.0, 0.0, 3.0 and 2.83 px. All pass.
- Calibration: the y residual is 0.76 px at most. The x mapping is piecewise between the ticks.
- I compared the k_min drop column by column (cols 125-182) against the scan's run centres. The print's drop is a
  rounded S on both curves: the FM slope eases 3.5, 2.5, 1.5, 1 px per 3 columns into the flat part. The CSV
  follows it to within about 1 px perpendicular to the line, so the kink is kept as printed.

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | The $k_{\min}$ leaders are short (about 2.5 mm each at final size), because the label sits in the narrow gap between FM k_min (7.8) and CB k_min (3.2) next to the y axis, as in the print. Both leaders are visible at 600 dpi and end on their curves. | fig08a.tex:28-30 | None needed. |
| 2 | note | The CB k_min minimum is +0.44 (CSV) where the print's dashes nearly touch the zero line. The script reads it by hand at about +0.3. The rerun overlay shows the trace about 1 px above the dash centres there (0.1 point). | fig08a.py:44-50 | None needed. |

Also checked, with no issue:
- **Frame and axes.** The frame is identical to fig06a (axis box 2403 x 1501 px at 600 dpi). x runs 0.10-0.50,
  labelled at each 0.10 with minor ticks at the 0.05s, as printed. y runs -15 to 15 in steps of 5. The titles are
  "Percent error in $v_b$" and "$m_o$ (kg)".
- **Legend and zero line.** The legend is at the lower right, as printed, and the zero line runs the full width.
- **Curves leaving the top.** The two k_max curves come in through the top of the frame, cut at 15. CB k_max enters
  at 0.172 (print: col 150.5, 0.171) and FM k_max at 0.207 (print: 0.206).
- **Leader ends.** The leader ends lie on the intended curves within 0.003 point: FM k_max 10.474, CB k_max 4.311,
  FM k_min 7.812, CB k_min 3.188.
- **Labels.** $k_{\max}$ is at (0.247, 6.9) and $k_{\min}$ at (0.125, 5.4), at the printed places.
- **Curve identities and shapes.** These match the print and the inventory:
  - FM k_min runs from 8.3 to 5.6 near 0.155, drops steeply to 2.2 by 0.18, then stays at 2.0-2.2.
  - CB k_min runs from 3.4, falls to its minimum near 0.175, then rises to 2.0 under the FM k_min solid.
  - FM k_max falls to 4.2.
  - CB k_max crosses zero near 0.27 and ends at -1.9.
- **Caption.** The caption's "additional error ... below 0.17 kg ... in the $k_{\min}$ cases" is visible as the
  abrupt drop of both k_min curves at 0.15-0.17.
- **Style.** The house style is followed. No panel letter is drawn in the art (`\figurepanel{a}`).

## Verdict

pass (0 must-fix, 0 should-fix, 2 notes)
