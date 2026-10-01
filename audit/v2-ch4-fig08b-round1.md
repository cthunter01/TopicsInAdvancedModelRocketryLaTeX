# v2 audit: ch4/fig08b (round 1)

Sources checked: scan `figures/ch4/fig08b.png` (6x zoom of the upper left, 4x zoom of the merged band). I also took
column profiles at cols 82-356 to separate the strands where the curves crowd. Redraw `figures/v2/ch4/fig08b.pdf`
(rendered at 300 and 600 dpi, with crops of 0.10-0.27 and of the band at 0.25-0.46). Source
`figures/v2/ch4/fig08b.tex` lines 1-33; `fig08b.py` lines 1-52 (with the helpers it imports from `fig07a.py`);
`fig08b.csv` (347 rows); `fig08b.calib.json`. Other sources: inventory row `ch4-fig08b`
(`figures/v2/inventory.csv`:136); float and caption `chapters/ch4-sec2b.tex`:459-467; the collective text and key
table :306-372; `corrections/v2-figures.md`:82-84; the template `fig06a.tex`.

Reruns:
- I ran `fig08b.py` on a copy in the scratch directory. The CSV it writes is byte-identical to the repository's.
- I ran the overlay of the four curves. 95% of the points are within 0.00 px for FM k_min and FM k_max and 2.00 px
  for CB k_min and CB k_max. The maxima are 2.24, 2.0, 3.0 and 2.24 px. All pass.
- Calibration: the y residual is 0.85 px at most.
- The overlay measures distance to the nearest ink, which proves little where the lines crowd. So I compared the CSV
  with the scan's ink runs column by column:
  - The two solids at 0.109-0.161 agree to within 0.5 px (for example, at col 106: rows 36.0 and 49.5 printed, 36.3
    and 49.7 written).
  - In the band at 0.21-0.31 the print shows two strands about 3 px apart, with the dashed curve running into the
    lower one. The CSV puts FM k_min on the upper strand and FM k_max on the lower strand, with CB k_min on it.
    For example, at col 260 the runs are at rows 70-72 and 74-76, and the CSV gives 70.9, 74.7 and 74.7.

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | Two leaders cross other lines, unlike the print. The $k_{\min}$ leader to CB k_min runs straight through the point where the two FM solids meet (about 0.169, 10.1); the 1973 art breaks both solids there to let the leader through. The $k_{\max}$ leader to FM k_max crosses the CB k_min dashed curve (at 0.1435: 9.85 against 10.62, about 1.3 mm). In both cases the leader runs on clearly past the crossed line (about 1.6 mm and 1.3 mm) to a line of the other style, so the target reads correctly. | fig08b.tex:25-30 | None needed. Optional: a white gap in the solids where the $k_{\min}$ leader passes, as printed (the white-casing pattern suggested for fig07c works). |
| 2 | note | Which FM curve is which after the solids merge (0.165-0.20) cannot be read from the art. The drafter keeps the left-hand order (upper strand = k_min). The two CSV columns differ by at most 0.05 point inside the merge, so nothing visible depends on the choice. On the page, the steeper k_min line seems to continue into the lower strand, but the 1973 art cannot settle this either. | fig08b.py:12-17 | None needed (doubt only). |
| 3 | note | The docstring says the line "splits into two about 0.3% apart from about .18 to .26" and closes "from about .27". The CSV, which follows the scan, has the strands apart from about 0.21 to 0.32, by up to 0.42 point at 0.26-0.28. The scan profile agrees with the CSV, not the docstring. | fig08b.py:14-16 | Optional: correct the docstring's ranges. |

Also checked, with no issue:
- **Frame and axes.** The frame is identical to fig06a (axis box 2403 x 1501 px at 600 dpi). x runs 0.10-0.50,
  labelled at each 0.10 with minor ticks at the 0.05s. y runs -15 to 15 in steps of 5. The titles are
  "Percent error in $y_b$" and "$m_o$ (kg)".
- **Legend and zero line.** The legend is at the lower right, as printed, and the zero line runs the full width.
- **Leader ends.** The leader ends lie on the intended curves within 0.003 point: FM k_max 10.617, CB k_max 2.819,
  FM k_min 12.642, CB k_min 9.106. The print's leaders reach the same curves: $k_{\min}$ to the top solid at about
  (0.128, 12.7) and to the upper dashed at (0.170, 8.9); $k_{\max}$ to the second solid at (0.144, 10.3) and to the
  lower dashed at (0.162, 2.7).
- **Labels.** $k_{\min}$ is at (0.168, 13.9) and $k_{\max}$ at (0.167, 5.5), at the printed places.
- **Curve identities.** These match the inventory:
  - FM k_min runs from 14.3 and FM k_max from 12.2; they meet near 0.17 at 10.0.
  - CB k_min runs from 11.4, joins the lower FM strand near 0.25 and is one band with both solids from about 0.33.
  - The common end is 7.6 at 0.443.
  - CB k_max dips to 2.0 near 0.22 and ends at 3.9.
- **Merged band.** In the band, the orange dashes lie on the blue solid and read as coincident curves at 600 dpi.
- **Caption.** The caption's transonic-drag remark holds: the k_min curves are steep below about 0.17 kg.
- **Text.** The errors of up to 14% are the logged v1 question about the text's 10% claim, not a figure issue.
- **Style.** The house style is followed. No panel letter is drawn in the art (`\figurepanel{b}`).

## Verdict

pass (0 must-fix, 0 should-fix, 3 notes)
