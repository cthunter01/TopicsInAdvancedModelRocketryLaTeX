# v2 audit: ch4/fig08c (round 1)

Sources checked: scan `figures/ch4/fig08c.png` (5x zoom of the upper left; a 12x zoom of the two dashed curves at
0.11-0.17, read dash by dash); column profiles at cols 140-205 (the k_min corner) and 300-460 (CB k_max at the zero
line). Redraw `figures/v2/ch4/fig08c.pdf` (rendered at 300 and 600 dpi, with a crop of 0.10-0.26). Source
`figures/v2/ch4/fig08c.tex` lines 1-33; `fig08c.py` lines 1-61 (with the helpers it imports from `fig07a.py`);
`fig08c.csv` (349 rows); `fig08c.calib.json`. Other sources: inventory row `ch4-fig08c`
(`figures/v2/inventory.csv`:137); float and caption `chapters/ch4-sec2b.tex`:469-477; the collective text and key
table :306-372; `corrections/v2-figures.md`:82-84; the template `fig06a.tex`.

Reruns:
- I ran `fig08c.py` on a copy in the scratch directory. The CSV it writes is byte-identical to the repository's.
- I ran the overlay of the four curves. 95% of the points are within 0.00 px for FM k_min and FM k_max and 2.00 px
  for CB k_min and CB k_max. The maxima are 1.0, 2.0, 2.83 and 2.83 px. All pass.
- Calibration: the y residual is 0.48 px at most.

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | should-fix | **The k_min corners at 0.17 kg are rounded off.** The inventory asks to keep the kink, and the caption ("an additional error ... below 0.17 kg ... in the $k_{\min}$ cases") singles it out as the figure's feature. In the print, FM k_min falls steeply (about 4 px per 3 columns) to a sharp corner at col ~155 ($m_o$ ≈ 0.169, ≈ 2.4), then turns almost flat at once (0.5 px per 3 columns). The CSV eases the slope over cols 149-164 (0.163-0.177) at 2.5, 1.9, 1.4, 1.1 and 0.7 px per 3 columns. It runs about 0.15-0.2 point left of the steep line just before the corner (cols 143-149) and 0.26 point (2.1 px) inside the corner at col 155. The CB k_min dashed curve is rounded the same way: the print's corner is at col ~155 (≈ 0.169, 0.86), and the CSV is 0.15-0.2 above it at cols 155-158. Because the stroke is 2-3 px thick, the overlay still passes. At final size, though, the rounding spreads over about 0.012-0.015 kg (3-4 mm): the redraw shows a U-bend where the print has a V corner (compare render, and the 2x overlay). The cause is the smoothing spline (s = n·0.5² px²) running through a corner. The 8(a) drop is a rounded S in the print and is traced correctly; 8(b) has no such corner. | fig08c.py:37-49; fig08c.csv rows near m0 0.155-0.185 | Trace each k_min curve in two pieces split at a hand-read corner pixel: FM about (155.5, 132.5), CB about (155, 147), read at 8x. Give the corner to both pieces (as an `extra` point and the end of each guide), smooth each piece separately, and join them, so that no spline runs through the corner. A rough split trace in my scratch copy kept a sharp corner and still passed the overlay (95% within 0 px solid, 2 px dashed). A `break` key on the shared `trace` helper would do it without changing the other panels. |
| 2 | note | The inventory row swaps the two CB curves at the left: it gives "CB k_min dashed ~9.8 at .11" and "CB k_max dashed ~8.8 at .11". Read dash by dash at 12x, the chain that starts higher (9.5) is the gentle one that reaches zero near 0.32. The lower $k_{\max}$ leader ends on it, so it is k_max. The chain that starts lower (8.7) is the steep one with the corner. The first $k_{\min}$ leader ends on it (at about col 121, row 104), so it is k_min. The redraw (fig08c.py:12-15) is right. | inventory.csv:137 | None for the figure. The inventory's curves text could be corrected at its next update. |
| 3 | note | The $k_{\min}$ leader to FM k_min crosses the CB k_min dashed curve, as in the print. Its two leaders end 0.015 kg apart on lines of different styles, so they read correctly. The $k_{\max}$ leader to CB k_max is a short stub (about 1.9 mm at final size, from the label's south-west corner); the print's is about 1.7 mm. | fig08c.tex:25-30 | None needed. |

Also checked, with no issue:
- **Frame and axes.** The frame is identical to fig06a (axis box 2403 x 1501 px at 600 dpi). x runs 0.10-0.50,
  labelled at each 0.10 with minor ticks at the 0.05s. y runs -15 to 15 in steps of 5. The titles are
  "Percent error in $y_{\max}$" and "$m_o$ (kg)".
- **Legend and zero line.** The legend is at the lower right, as printed, and the zero line runs the full width.
- **Leader ends.** The leader ends lie on the intended curves within 0.004 point: FM k_max 8.447, CB k_max 3.928,
  FM k_min 4.789, CB k_min 5.550.
- **Labels.** $k_{\max}$ is at (0.199, 5.9) and $k_{\min}$ at (0.117, 2.5). The print has them at about
  (0.199, 5.8) and (0.118, 2.4).
- **Curve shapes.**
  - FM k_max runs from 14.3 to 3.95.
  - FM k_min runs from 11.45 to the corner, then rises to meet FM k_max near 0.44 (common end 3.9).
  - CB k_max runs from 9.5 through zero near 0.32 to -0.40. The scan profile at cols 440-460 puts its dashes 3-4 px
    under the zero line, at -0.35 to -0.45.
  - CB k_min runs from 8.7 to 1.0 at the corner and then to 3.4.
  - The dashed curves cross near 0.24.
- **Caption.** The caption's transonic-drag remark holds, apart from finding 1's rounding.
- **Text.** The errors of up to 14% are the logged v1 question about the text's 10% claim, not a figure issue.
- **Style.** The house style is followed. No panel letter is drawn in the art (`\figurepanel{c}`).

## Verdict

fix (0 must-fix, 1 should-fix: keep the sharp k_min corners at 0.17 kg)
