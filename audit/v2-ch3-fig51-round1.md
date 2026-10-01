# v2 audit: ch3/fig51 (round 1)

Sources checked: scan `figures/ch3/fig51.png` (zoomed: region markers, inset); redraw `figures/v2/ch3/fig51.tex`,
`fig51.py`, `fig51.csv`, `fig51.calib.json`, `figures/v2/ch3/fig51.pdf` rendered at 400 and 1200 dpi;
`build/v2/png/ch3-fig51.png`; inventory row ch3-fig51; caption and citing text `chapters/ch3-sec6c.tex` lines
196-411 (eqs. (199)-(205), the GCR-x values, the printed GCR-x equations, Table 6, the three phases, base drag about
7%); STYLE.md sections 14 and 16; `corrections/v2-figures.md` rule 3; approved Ch3 Fig 22 (frame), Ch2 Fig 25 and
Ch3 Fig 2 (label knock-outs); `pdffonts` (fonts embedded); page 443 x 293 pt = 6.15 in wide.

Independent checks:
- Equations: I recomputed with my own script (scratch `chk51.py`) from the printed GCR-x equations: (C_Df)_b = 82.8
  (C_f)_B, C_Db = .0149/sqrt, (C_Do)_F = 46.4 (C_f)_F, the body switch at 5e5 (B = 1735) and the fin switch at 5.14e6.
  fig51.csv agrees to 1e-5, apart from the deliberate pair of rows at R = 5e5 (laminar and turbulent sides, 0.0011
  apart). Against Table 6: 1e4 gives 0.014 / 1.114 / 1.972 / 3.086 (table 3.080, off the plot); 5e5 gives 0.473
  (table 0.473); 2e6 gives 0.433 (table 0.432); 5e6 gives 0.369 (0.370); 1e7 gives 0.396 (0.396).
- Text claims hold on the redraw: the C_Db maximum is 0.0378 at 5e5, and C_Db/(C_Do)_FB is 6.4-8.1% above 5e5
  ("about 7%"). (C_Do)_B rises from 5e5 to about 2e6 and then falls. (C_Do)_FB is nearly flat in region (2) and has
  its minimum at the fin switch.
- Overlay (`digitize.py overlay`, the drafter's calibration of the drawn gridlines; residual 0.49 px; I spot-checked
  the gridline columns with `lines`), 95th percentile: C_Db 2.0 px, (C_Do)_B 2.24 px, (C_Do)_F 3.0 px, (C_Do)_FB
  2.0 px. All are within the 3 px target.
- Axes: a true log x axis over 1e4-1e7, with the printed tick lettering (10^4, 2, 3, 4, 6, 8 ...) and the printed
  rulings (1.5, 2.5, 3.5, 5, 7, 9) as minor grid. y runs 0-1.6, labelled every 0.2, grid every 0.1. The axis titles
  are $\CD$ and $R_\ell$. The frame and size (5.4 x 3.5 in) match the approved Fig 22.
- Lettering: $(\CDo)_F$, $(\CDo)_{FB}$, $(\CDo)_B$ and $C_{Db}$ are all in ink and set in the section 14 forms. The
  inset has $U_\infty$ with a flow arrow and "GCR-x". The circled 2 and 3 use `curve tag`.
- Inset GCR-x drawn to the text's proportions (l_N 3.5, l_s 11.5, l_T 3, d_b 0.8, c 1.75, b 5; fin root on the cone
  at r = 0.458). It sits on a blanked patch, as in the scan, and is consistent with Fig 50.

## Findings
| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | should-fix | The four curve labels have no white knock-out, so gridlines run through the lettering. The 1.5 gridline crosses the middle of $(\CDo)_F$ and $(\CDo)_{FB}$, and the vertical rulings cross $(\CDo)_B$ and $C_{Db}$. The approved gridded charts (Ch2 Fig 25, Ch3 Fig 2) set such labels with `fill=white` wherever no curve passes behind, and the 1973 art blanks the grid behind its lettering. No curve passes behind any of the four boxes, except near $(\CDo)_{FB}$ (see 2). | fig51.tex line 23 `curve label/.style={font=\small, inner sep=1.5pt}` | add `fill=white` to `curve label` |
| 2 | should-fix | The $(\CDo)_{FB}$ label is anchored on its own curve: (C_Do)_FB = 1.5 at R = 4.31e4, and the label's west anchor is at (4.3e4, 1.5). The "(" comes within about 0.5 mm of the curve at its lower left (measured at 1200 dpi). With a white fill from finding 1, the box would paint over part of the curve. | fig51.tex line 45 | move it right, e.g. `(axis cs:4.9e4,1.5)` (the box then clears the curve by about 4 pt and still ends left of the inset patch) |
| 3 | note | The inset's white patch runs to x = 1e7, so it covers half the width of the right-hand 1e7 gridline between 1.0 and 1.5, which shows as a lighter segment of the chart's edge. | fig51.tex line 37 | optional: stop the patch at about 9.6e6, or redraw the 1e7 line over it |
| 4 | note | Four series in three colours: the body pair, (C_Do)_B and C_Db, share s2 and differ by dash pattern (long dash, dash-dot), and the fins' curve is s3. All are labelled directly and the printed dash patterns are kept, so they read unambiguously. This is a reasonable use of the house palette. | | none |
| 5 | note | The region (3) marker starts at 5e6 (the caption's bound), while the fin switch and the kink in the curves are at 5.14e6, about 1 mm to the right (D35, no note). The markers carry arrowheads where the 1973 bars are plain lines; this is the house dimension idiom and does not change the meaning. | lines 49-55 | none |

## Verdict: pass (no must-fix)
