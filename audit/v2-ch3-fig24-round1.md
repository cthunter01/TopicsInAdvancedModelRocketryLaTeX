# v2 audit: ch3/fig24 (round 1)

Sources checked: scan `figures/ch3/fig24.png` (2x); redraw `figures/v2/ch3/fig24.pdf` (300 dpi whole, 600 and
1200 dpi crops of the right-hand labels; `pdffonts`); sources `figures/v2/ch3/fig24.tex`, `fig24.py`, `fig24.csv`,
`fig24-r3e5.csv`, `fig24-r6e4.csv`, `fig24.calib.json`; inventory row `ch3-fig24` (`figures/v2/inventory.csv`:90);
caption `chapters/ch3-sec3c-sec4a.tex`:203-216; citing text :184-186, :289-298, :327-331 and `ch3-sec3b.tex`:422-426;
`STYLE.md` sections 14 and 16; `tamrfig.sty` (series1-3, tamr grid); approved Ch2 Fig 25 (curve-label size).

Checks made:
- **Theory curve.** fig24.csv is exactly 1 - 4 sin^2(phi). I checked 30, 60, 90, 120 and 150 deg: 0, -2, -3, -2
  and 0. It is solid s1.
- **Experimental curves.** They are digitized against the six gridline crossings (residual 0.31 px).
  - Overlay (`digitize.py overlay`), whole curves: theory 95% 1.41 px; R_d = 3e5 95% 2.00 px, max 3.00 px;
    R_d = 6e4 95% 2.00 px, max 3.00 px.
  - The traced parts alone (phi >= 22 and 20 deg): the same, all ok.
  - The 3e5 curve has its minimum -2.11 at 80 deg and a plateau of -0.43. The 6e4 curve has its minimum -1.37
    at 71 deg and a plateau of -1.13. Both match the inventory and the scan.
  - Below 20-22 deg the three printed curves run within a pixel or two of each other. There each experimental
    curve is the theory plus a smooth correction that joins the trace in value and slope. In the 4x crop of
    0-40 deg it sits on the printed ink.
- **Text.**
  - The minimum pressure is near the shoulder.
  - phi = 0 and 180 deg are the stagnation points.
  - The experimental pressure over the rear never regains its phi = 0 value.
  - Supercritical recovery (plateau -0.43) is more complete than subcritical (-1.13).
  - All four hold on the redraw.
- **Lettering.**
  - y ticks 1, 0, -1, -2, -3 with true minus signs.
  - x ticks 0, 60, 120, 180 deg, with the grid every 20 deg.
  - x title $\varphi$ (varphi, STYLE s.14).
  - Labels $R_d = 3 \times 10^{5}$ and $R_d = 6 \times 10^{4}$; the 6e4 label is in a white gap of the -1
    gridline, as printed.
  - $C_p = 1 - 4\sin^2\varphi$ right of the rising branch, its white box clear of the curve by about 4 mm.
  - An upright $C_p$ ordinate title was added; the 1973 axis has none. The inventory suggests it, and it names
    the quantity the theory label already states.
- **Encoding.** Theory is solid s1, 3e5 dashed s2, 6e4 dash-dot s3. Each experimental curve has a direct label,
  so aqua is allowed.
- **Size.** Axes 4.2 x 2.9 in, page 4.93 x 3.42 in; fonts embedded. The curve labels are `\footnotesize`, as in
  the approved Ch2 Fig 25.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | should-fix | The $R_d = 3 \times 10^{5}$ label has no knock-out, so the 160-degree gridline runs through its "=" (1200 dpi crop). The 6e4 label beside it has a white knock-out, so the two direct labels differ. No curve passes behind the 3e5 label, so the house rule allows the knock-out. | fig24.tex:24 | Add `fill=white` to that node, as on the 6e4 label at line 25. |
| 2 | note | Below 22 deg (3e5) and 20 deg (6e4) the experimental curves are not traced but blended from the theory (`smooth_resample`). The printed curves cannot be separated there; the blend lies on the printed ink. | fig24.py:100-122, 140, 148 | None. |
| 3 | note | The $C_p$ ordinate title is an addition to the 1973 lettering. It adds no new meaning (the quantity is the theory label's) and the inventory recommends it. | fig24.tex:17 | Mention at the Chapter 3 gate with the other additions, if the gate lists them. |

## Verdict: pass

No must-fix. One should-fix (the 3e5 label's knock-out).
