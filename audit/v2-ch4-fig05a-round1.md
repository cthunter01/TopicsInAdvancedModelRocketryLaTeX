# v2 audit: ch4/fig05a (round 1)

Sources checked:
- Scan `figures/ch4/fig05a.png`: 2x upscale, 4x crops of the k labels and the zero-line bundle, and pixel columns
  at rows 140-165.
- Redraw `figures/v2/ch4/fig05a.pdf`: 300 and 400 dpi renders, with crops of the callouts; `pdffonts`.
- Source files `fig05a.tex`, `fig05a.py`, `fig05a.csv` (241 rows) and `fig05a.calib.json`.
- Template `fig06a.tex`, compared by diff.
- Inventory row `ch4-fig05a`.
- Chapter text: `chapters/ch4-sec2b.tex`:201-205 (B14 $F_m$ = 28.6 N, $t_s = t_b$, $F_s = 0$), :308-330, :343-372
  (collective caption and key table: B14 $k_{\min} = .00005$, $k_{\max} = .002$), :374-380 (caption).
- `chapters/ch4-sec3.tex`:177-181 (Fig 10 caption: $m_o = .020$ kg, $t_b$ = 0.35 s).
- `corrections/v2-figures.md`, including the rule entry "Ch4 Figs 5, 7-10, 12-14 ... digitized".
- `STYLE.md` sections 15 and 16.

Checks made:
- **Method.** The curves are digitized, which is correct here. For the B14 the book gives only $F_m$ and $t_b$.
  It does not give $t_m$ or the propellant mass, which eqs. (74) and the average mass need. So the curve is not
  determined by the book, and the compute-else-digitize rule applies.
- **Reproducibility.** I reran `fig05a.py` on a scratch copy (scan, calibration, script). The CSV it writes is
  byte-identical to the repository's.
- **Calibration.**
  - `digitize.py ticks` finds the bottom-axis ticks at columns 72.0, 110.0, 148.0 ... 520.5, exactly the `xgrid`
    of `fig05a.calib.json`.
  - The y ticks are at the rows given in `ygrid`.
  - The y axis is vertical (column 72 at the top and at the bottom).
- **Overlay.** I ran `digitize.py overlay` on each column, using the drafter's piecewise calibration:

  | curve | points | mean | 95% | max |
  |---|---|---|---|---|
  | FM $k_{\max}$ | 221 | 0.02 px | 0.00 px | 3.00 px |
  | CB $k_{\max}$ | 232 | 0.41 px | 2.00 px (0.34 mm) | 2.24 px |
  | FM $k_{\min}$ | 241 | 0.00 px | 0.00 px | 1.00 px |
  | CB $k_{\min}$ | 241 | 0.27 px | 2.00 px | 2.24 px |

  All four pass. The overlay image shows that each trace follows its own printed line, not a neighbouring one.
- **Zero-line bundle.** Pixel columns show the thin zero line at row 152 and FM $k_{\min}$ as a separate solid at
  rows 154-155 from about 0.03 kg on. That is -0.2 point, as digitized (-0.21 at 0.04, -0.27 at 0.14). CB
  $k_{\min}$ dashes run in directly below it at the right.
- **Values against the inventory's readings.**
  - FM $k_{\max}$ leaves the frame at 0.030-0.031 and reads 0.91 at 0.10 and 0.40 at 0.14.
  - CB $k_{\max}$ leaves the frame at about 0.0248, crosses 0 at 0.0405 and has its minimum, -4.16, at 0.067.
  - FM $k_{\min}$ is +0.17 at 0.02.
  - CB $k_{\min}$ is -3.17 at 0.02 and -1.01 at 0.045.
  - All of these agree with the scan. The two off-scale curves are written up to just above 15 and then as nan,
    and `clip mode=individual` clips them at the top of the frame, as printed.
- **Lettering.**
  - y title "Percent error in $v_b$"; y ticks -15 to 15 in steps of 5, with true minus signs.
  - x title $m_o$ (kg); x ticks 0.02-0.14 with minor ticks at the odd 0.01s.
  - $k_{\max}$ and $k_{\min}$ (lowercase k, upright subscripts, STYLE s15), each with two leaders.
  - Legend at lower right, as printed: solid "Fehskens-Malewicki", dashed "Caporaso-Bengen".
  - The thin solid zero line.
  - No panel letter is drawn in the art; `\figurepanel{a}` supplies it in the float, as for fig06a.
- **Leaders.** Each of the four leaders ends exactly on its curve (CSV interpolation, difference 0.000):
  (0.045, 6.778) FM $k_{\max}$, (0.0385, 0.958) CB $k_{\max}$, (0.028, -0.106) FM $k_{\min}$, (0.032, -1.771) CB
  $k_{\min}$. The printed leaders reach the curves at about (0.043, 7.5), (0.037, 1.9), (0.028, -0.3) and (0.032,
  -1.7).
- **Template.**
  - The diff against fig06a.tex changes only the x range and ticks (0.02-0.14, as printed), the CSV name, the zero
    line's end and the label positions.
  - Frame 4.0 x 2.5 in; page 4.73 x 3.06 in, the same as fig06a. Fonts embedded.
  - series1/series2, `leader`, `\footnotesize` labels, legend style and the muted zero line are all the template's.
- **Caption and text.** The panel shows the burnout-velocity error for the B14 at the key table's two k values, as
  the caption and the collective caption say.
- **Text's 10% claim.** The k_max curves pass 15%, so the panel contradicts the text's 10% claim (ch4-sec2b.tex:326-330).
  This is already logged as a v1 item and is not raised here.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | The $k_{\max}$ leaders do not fan out from the label as they do in fig06a and in the scan. The upper leader starts at the label's north-east corner and runs up and to the left to FM $k_{\max}$ at 0.045. The lower one starts at the south-west corner and runs down and to the right to CB $k_{\max}$ at 0.0385. Both are about 3-4 mm long and slant the same way, so they read as two parallel strokes. They still end on their curves and are legible. | fig05a.tex:24-26 | Optional: `(kmax.north) -- (axis cs:0.047,6.13)` and `(kmax.west) -- (axis cs:0.037,1.97)`. Both points are on the CSV curves, and the leaders then diverge as in the template. |
| 2 | note | From about 0.10 kg the CB $k_{\min}$ curve is written on top of FM $k_{\min}$ (both -0.27 at 0.14). The print has the dashes about 1.5 px (0.15 point) below the solid. The orange dashes stay visible on the blue line, and the overlay passes. | fig05a.py GUIDE["cb_kmin"] | None needed. |
| 3 | note | The relayed owner request "Keep 1-3 as they are, use exact curves for 46" could be read as asking for Figs 4-6 to be computed. Fig 5 cannot be: the book does not give the B14's $t_m$ or propellant mass (inventory: a triangle fitted to Fig 10 gives FM $y_b$ errors of -3 to +1% against the printed +5.5 to +8.5%). Digitizing stays the only faithful option, as the existing rule entry says. | corrections/v2-figures.md "Ch4 Figs 5, 7-10, 12-14" | Orchestrator: confirm the reading with the owner if it is meant to cover Fig 5. Also update the inventory `method` from "compute-partial+digitize" to "digitize". |

## Verdict

pass (0 must-fix, 0 should-fix)
