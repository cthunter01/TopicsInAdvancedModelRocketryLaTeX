# v2 audit: supplement/ch4-fig04-1994 (round 1)

Sources checked:
- Scan `figures/supplement/ch4-fig04-1994.png`, with crops of the legend, the lettering block, the peak and the
  burnout corner.
- Redraw `figures/v2/supplement/ch4-fig04-1994.pdf`: 300 and 600 dpi renders, `build/v2/png/supplement-ch4-fig04-1994-compare.png`,
  `pdffonts`, and a scan for opacity operators.
- Sources `ch4-fig04-1994.tex`, `.py`, `.csv` and `.calib.json`, plus `figures/v2/ch4/fig04.py` (which it imports),
  `trajectory.py` (`B4.thrust`, eq. (73)) and the shared `figures/v2/common/b4.csv`.
- Inventory row `sup-ch4-fig04-1994`.
- Text: `chapters/ch4-sec2b.tex`:166-224 (eqs. (73)-(75), the citing sentence, the 1994 caption and its edcap),
  `backmatter/supplement/s-ch4-fig-table.tex`:1-27, and `frontmatter/about-this-edition.tex`:214, 249-252.
- `corrections/v2-figures.md`: rule 5 and the Minor entry "Ch4 Fig 4 (1973 and 1994)".
- STYLE.md sections 15 and 16, and the approved Ch1 Fig 5 and Ch1 Fig 3 frames.

Checks made:
- **Approximation, computed.**
  - `B4.thrust` is eqs. (73a)-(73c) with the lettered F_m 13.0, F_s 3.5, t_1 = t_m 0.14, t_2 = t_s 0.22 and t_b 1.20.
  - The CSV's corners are exact: (0.14, 13.0), (0.22, 3.5), then (1.2, 3.5) down to (1.2, 0).
  - Eq. (75) gives 13.0(0.22)/2 + 3.5(1.20 - 0.07 - 0.11) = 5.000 N-sec, and the trapezoid area of the polyline
    is also 5.000. Both equal the lettered I_t.
  - Eq. (75) as printed is the exact area of (73), which I checked algebraically.
  - Rerunning the script in a scratch copy reproduces `ch4-fig04-1994.csv` byte for byte.
- **Actual curve.** It is the shared `common/b4.csv` (rule 5): peak 12.96 N at 0.145 s, plateau mean 3.70 N,
  area 5.09 N-sec. The figure reads nothing else.
- **Overlay.** I reran `digitize.py overlay` with the drafter's calibration (residual 0.00 px):
  - Actual: 658 points, mean 0.06 px, 95% 0.00 px, max 5.1 px. The max is the burnout corner, where the scan
    rounds over about 0.01 s and the shared tracing turns square.
  - Approximation: 608 points, mean 0.88 px, 95% 3.16 px (0.54 mm), max 5.0 px. This is just over the 3 px
    tolerance. All of the excess is on the descending leg, which the 1973/1994 art draws bent near 5 N and
    meeting 3.5 N at about 0.225 s.
- **Lettering.** All present and as printed, in STYLE s15 form:
  - Legend "Actual curve" (solid) and "Approximation" (dashed), top left.
  - The block $I_t$ = 5.0 N-sec, $F_m$ = 13.0 N, $F_s$ = 3.5 N, $t_1$ = 0.14 sec, $t_2$ = 0.22 sec, $t_b$ = 1.20 sec,
    typeset as a table aligned on "=" and on the decimal points.
  - "B4" inside the curve.
  - Axis titles $F$ (N) (rotated) and $t$ (sec).
  - y ticks 0-16 step 2; x ticks 0, 0.2, ..., 1.0, 1.2, as printed and as the approved Ch1 Fig 3.
- **Caption and text.** Both curves are shown and the parameters are shown. "$t_1$ as shown here is $t_m$ ...
  $t_2$ ... is $t_s$" holds, because the block letters $t_1$ and $t_2$. The citing sentence (ch4-sec2b.tex:206-207)
  holds.
- **Style.**
  - Kit `tamr` frame at 4.2 in wide like Ch1 Fig 5(a), on a 4.82 x 3.15 in page.
  - Solid `series1` (s1) for the measured curve and dashed `series2` (s2) for the approximation: the
    solid/dashed encoding the caption relies on, and the colours and order of the fig06a template.
  - Text is in ink. The approximation is drawn first, so the measured curve lies over it at the peak and at
    t_b. The legend is opaque (the kit's opacity has been removed).
  - No transparency operators in the PDF, fonts embedded, the log is clean, and nothing is clipped or
    overlapping.
- **Family.** Apart from the CSV path in one `\addplot` line, this file is identical to `figures/v2/ch4/fig04.tex`,
  and the two CSVs are byte-identical. The 1973 and 1994 forms are one drawing at one size, as the brief asks.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | The approximation's overlay is 95% 3.16 px (0.54 mm), over the 3 px tolerance. The cause is the bend in the drawn descending leg; the computed leg is the straight line of eq. (73b). This is already logged in `corrections/v2-figures.md` (Minor, "Ch4 Fig 4 (1973 and 1994)"), and computed curves are approved. | descending leg, t 0.17-0.23 s | None. |
| 2 | note | After the switch, the supplement Part shows this figure and "The 1973 Figure 4, which this figure replaces" as two identical vector drawings at the same size. The current includes scale the scans to 0.75 and 0.6 \textwidth, but v2 includes are unscaled. "Reproduced larger" (ch4-sec2b.tex edcap; About This Edition :214) still describes the 1994 document truly. | `backmatter/supplement/s-ch4-fig-table.tex`:6, :20 | Gate: confirm that both forms stay as identical redraws, which is the brief's choice and the precedent of Ch1 Fig 2 and Ch2 Fig 36. The switcher drops the width options. |
| 3 | note | The legend is \footnotesize (the kit default) while the lettering block and "B4" are \small (`every picture`). The 1973 art letters them at one size. This is the kit-wide legend-size question already listed under "Style suggestions" in `corrections/v2-figures.md`. | legend | None here; settle it in the kit if wanted. |
| 4 | note | `ch4-fig04-1994.py` imports `figures/v2/ch4/fig04.py`, another figure's script, so a later edit there changes this figure's data silently. Both are in the same family, and both reproduce byte for byte today. | `ch4-fig04-1994.py`:13-15 | None needed. Optionally give the script its own copy of `approximation()`. |

## Verdict: pass
