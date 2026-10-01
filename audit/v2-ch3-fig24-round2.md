# v2 audit: ch3/fig24 (round 2)

Sources checked:
- Scan: `figures/ch3/fig24.png`.
- Redraw: `figures/v2/ch3/fig24.pdf`, rebuilt at 22:39 after the tex.
  - Renders: 300 dpi whole; 1200 dpi crop of the two right-hand labels; 2400 dpi crop of the left edge of the 3e5 label box.
  - Also checked: `pdfinfo`, `pdffonts`.
- Sources: `figures/v2/ch3/fig24.tex`, `fig24.py`, `fig24.csv`, `fig24-r3e5.csv`, `fig24-r6e4.csv`, `fig24.calib.json`.
- Earlier rounds: the round-1 audit and the round-1 fix report.
- Inventory row `ch3-fig24`.
- Caption and citing text: `chapters/ch3-sec3c-sec4a.tex`:184-186 and :203-216.

## Round-1 finding

**Should-fix 1 is resolved.** The $R_d = 3 \times 10^5$ label had no knock-out.

- fig24.tex:25 now gives it `fill=white`, as on the 6e4 label at :26.
- At 1200 dpi, the 160-degree gridline is broken behind both labels, and the -1 gridline is broken behind the 6e4 label, as printed.
- The knock-out clips no curve:
  - The theory's rising branch passes left of the 3e5 box. At 2400 dpi it is about 2.7 pt clear of the box's top-left corner. Check: $1 - 4\sin^2\varphi = -0.21$ at $\varphi = 146.6\dg$, while the box starts at about 147 deg.
  - The 3e5 plateau (-0.43) runs about 1.5 pt below the box's lower edge. Its dashes are intact.

## Regression check

- **Curves.** The three curves are unchanged (CSVs dated 22:21).
  - My overlay, 95% (all ok): theory 1.41 px; 3e5 2.00 px; 6e4 2.00 px. Calibration residual 0.31 px.
  - The theory is exactly $1 - 4\sin^2\varphi$ at 0, 30, 45, 60, 90, 120, 150 and 180 deg.
  - The 3e5 curve has its minimum of -2.11 at 80 deg and ends at -0.43.
  - The 6e4 curve has its minimum of -1.37 at 71 deg and ends at -1.13.
- **Lettering.**
  - The y ticks (1 to -3) and the x ticks (0 to 180 deg, grid every 20 deg) are as printed.
  - The axis title is $\varphi$.
  - All three curve labels are present.
  - The $C_p$ ordinate title is the logged addition.
- **Encoding.** Solid s1, dashed s2 and dash-dot s3, each with a direct label.
- **Size and fonts.** Page 4.93 x 3.42 in; fonts embedded.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | Round-1 should-fix 1 (the 3e5 label's knock-out) is resolved. Both direct labels now knock out the gridlines, and neither clips a curve (2400 dpi check). | fig24.tex:25-26 | None. |
| 2 | note | The upright $C_p$ ordinate title is still an addition to the 1973 lettering. It is carried as a gate doubt in the round-1 fix report. | fig24.tex:17 | List it at the Chapter 3 gate with the other additions. |

## Verdict: pass

No must-fix and no should-fix.
