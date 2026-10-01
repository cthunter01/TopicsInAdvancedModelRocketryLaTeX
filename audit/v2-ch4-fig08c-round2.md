# v2 audit: ch4/fig08c (round 2)

Sources checked: scan `figures/ch4/fig08c.png` (8x zooms of cols 120-200, rows 100-160: both k_min corners);
redraw `figures/v2/ch4/fig08c.pdf` (rendered at 300 and 600 dpi, with a 600 dpi crop of 0.13-0.22); source
`figures/v2/ch4/fig08c.tex` lines 1-33; `fig08c.py` (all) and the new `trace_cornered` and `smooth(pin, knots)` in
`fig07a.py`; `fig08c.csv`; `fig08c.calib.json`. Other sources: inventory row `ch4-fig08c`
(`figures/v2/inventory.csv`:137); caption `chapters/ch4-sec2b.tex`:469-477; the template `fig06a.tex`; the
round-1 report.

Reruns:
- I ran `fig08c.py` on a scratch copy. The CSV it writes is byte-identical to the repository's.
- I ran the overlay of the four curves:

  | curve | 95% within | max |
  |-------|-----------|-----|
  | FM k_min | 0.00 px | 0.00 px |
  | CB k_min | 2.00 px | 2.83 px |
  | FM k_max | 0.00 px | 2.00 px |
  | CB k_max | 2.21 px | 2.83 px |

  All pass.
- All four leader ends lie on their CSV curves within 0.003 point: FM k_max 8.446, CB k_max 3.928, FM k_min 4.841,
  CB k_min 5.571.

Round-1 follow-up:
- **Should-fix 1 (k_min corners rounded off): resolved.** Both k_min curves are now traced in two pieces that meet
  at a hand-read corner. The CSV has a row at each corner: 0.16861 (FM, 2.461) and 0.16670 (CB, 0.913).
  - **FM k_min against the scan ink, column by column.** The ink centres lie within 0.0-0.5 px of the CSV at cols
    148-171, through the corner. For example, col 155 is ink 132.5 against CSV 132.4. In round 1 the CSV sat 2.1 px
    inside the corner.
  - **FM k_min slope.** The slope runs about -0.16 per 0.001 kg into the corner and -0.04 just after it. The curve
    then dips to 2.15 at 0.186 and rises, as printed.
  - **CB k_min against the dash centres.** The steep dashes (cols 144-151) are within about 0.5 px measured across
    the line. The flat dashes (cols 154-170) are within 0.1 px.
  - **CB corner position.** The drafter's corner (152.7, 146.8) is where the steep dashes, extrapolated, meet the
    first flat dash (it starts at col 154, row 146.5). This is consistent with the scan.
  - **Render.** The 600 dpi render shows V corners on both curves, as in the 8x scan zoom.
  - **Ripple check.** I checked the fixed-knot fits for ripple. On each side the slope changes sign only at the
    printed minima (FM at 0.186, CB at 0.174) and at the common end. Against a running mean, the ripple is 0.01
    point at most.
- **Leaders after the change.** The $k_{\min}$ leader ends moved onto the new curves: (0.1548, 4.841) on FM k_min
  and (0.1394, 5.571) on CB k_min. The leader to FM k_min still crosses the CB k_min dashed curve, as printed, and
  reads correctly.
- **Docstring and header.** The docstring (corner method, corner readings) and the tex header comment agree with
  the CSV.
- **Note 2 (the inventory swaps the CB starts): still stands, outside this figure's files.** The redraw follows the
  print: the higher start 9.52 is k_max, and the lower start 8.81 is k_min.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | Carried forward, not in this figure's files: the inventory row gives "CB k_min dashed ~9.8 at .11" and "CB k_max dashed ~8.8 at .11". This is swapped. Read dash by dash with the leaders, k_max starts higher (9.5) and k_min lower (8.8). The redraw is right. | inventory.csv:137 | Correct the inventory's curves text at its next update. |

Also checked, with no issue:
- **Frame and axes.** The frame is identical to fig06a (the x axis is 2402 px long at 600 dpi). x runs 0.10-0.50,
  labelled every 0.10 with minor ticks at the 0.05s. The titles are "Percent error in $y_{\max}$" and "$m_o$ (kg)".
  The legend is at the lower right, as printed, and the zero line runs the full width.
- **Curve shapes.**
  - FM k_max runs from 14.3 to 3.95.
  - FM k_min runs from 11.5 to the corner, then to 3.90; it meets FM k_max near 0.44 (0.05 point apart at the
    ends).
  - CB k_max runs from 9.5 through zero near 0.32 to -0.40.
  - CB k_min runs from 8.8 to the corner and then to 3.37.
- **Caption.** The caption's "additional error ... below 0.17 kg ... in the $k_{\min}$ cases" now shows as printed:
  steep k_min curves ending in sharp corners at 0.167-0.169 kg.
- **Style.** The house style is followed; there is no local style and no panel letter in the art.

## Verdict

pass (0 must-fix, 0 should-fix, 1 note). The round-1 should-fix is resolved, with no regression.
