# v2 audit: ch3/fig24 (consistency fix, verification)

Sources checked:
- The 1973 scan `figures/ch3/fig24.png`.
- The redraw `figures/v2/ch3/fig24.pdf`, built 23:15:16, after the tex (23:15:15), so it is current.
  - Renders: 300 dpi whole; 800 dpi crops of the two right-hand labels and of the formula label.
  - `pdftotext -bbox`: the label extents in pt.
  - `pdfinfo`: 354.9 x 246.2 pt (4.93 x 3.42 in), the same as round 2.
  - `pdffonts`: all fonts embedded.
- `build/v2/png/ch3-fig24-compare.png`.
- Sources: `figures/v2/ch3/fig24.tex`, `fig24.py` (21:56), `fig24*.csv` (22:21) and `fig24.calib.json`.
- The round-1 and round-2 audits, the consistency issue and the fixer's report.
- Inventory row `ch3-fig24`.
- Caption and citing text: `chapters/ch3-sec3c-sec4a.tex`:184-186, 203-216, 289-298, 327-331.
- `STYLE.md` s.16 (labels `\small`, tick labels `\footnotesize`); `tamrfig.sty` (`every picture`: `font=\small`).
- The Ch2 curve-family figures 24, 25, 30, 31, checked for the label-size claim.

## Consistency issue: label size

The issue: the three direct labels were `\footnotesize`; the house label size is `\small`. **Resolved.**

- **Size.** The label scope at fig24.tex:25 now sets only `inner sep=1.5pt`, so the labels take the picture default, `\small`, as STYLE s.16 says. The bbox extents confirm it: the $R_d$ labels are 52.6 pt wide (formerly about 47 pt).
- **Clearances at the new size.** The fixer moved one label. The others stay.

### The moved label: $R_d = 3 \times 10^5$

It is now anchor south east at (140 deg, -0.40), so the box spans about 107-140 deg and C_p = -0.40 to -0.13. Measured from the bbox (1.68 pt per degree, 52.1 pt per unit):
- **Theory curve.** It crosses -0.40 at 143.7 deg, 6.2 pt right of the box corner. That is about 5 pt perpendicular, allowing for the curve's slope and half its width. Under the box (107-140 deg) the theory lies at -1.6 to -0.65, well below it. Nothing passes behind.
- **Its own dashed curve.** It rises from -1.25 to -0.443 under the box. The closest approach is about 2 pt at the right corner. That is the same kind of gap as before: round 2 measured 1.5 pt.
- **Gridlines.** The box knocks out the 120 deg gridline. It sits 6.6 pt below the 0 gridline.

### The other two labels

- **$R_d = 6 \times 10^4$.** It stays at the right, in its gap of the -1 gridline, as printed and as the inventory notes. The theory crosses its height band at 134-137 deg, about 14 pt left of the box. The dash-dot plateau (-1.13) is about 2.6 pt below the box.
- **$C_p = 1 - 4\sin^2\varphi$.** It is unchanged at (118, -2.42), clear of the theory by about 5 pt (800 dpi crop).

### Why the move was needed

At `\small` the 3e5 label is about 33 deg wide. Ending at 179 deg, as printed, it would start at about 146 deg. The computed theory crosses that band (-0.40 to -0.15) between 143.7 and 147.6 deg. Keeping the computed curve (standing rule) and the house size means moving the label. Its new place is above its own plateau and knee, and still reads as that curve's label. The inventory fixes no position for it, only for the 6e4 label. The fixer's doubt records the departure from the 1973 position. This was the right call.

## Regression check against the scan, the inventory and the earlier audits

- **Curves.** I re-ran the overlay (`digitize.py overlay`, residual 0.31 px):
  - theory: 95% 1.41 px, max 2.24 px;
  - 3e5: 95% 2.00 px, max 3.00 px;
  - 6e4: 95% 2.00 px, max 3.00 px.
  - These are identical to rounds 1 and 2. All ok.
- **Round-1 should-fix.** The knock-out on the 3e5 label is still there (`fill=white`, fig24.tex:26).
- **Lettering.** Everything on the inventory list is present: the y ticks 1 to -3, the x ticks 0-180 deg with the grid every 20 deg, $\varphi$, both $R_d$ labels and the formula. The $C_p$ ordinate title is still the logged addition.
- **Encoding.** Solid s1, dashed s2, dash-dot s3, each with a direct label. Text stays ink.
- **Text.** All four claims still hold: the minimum near the shoulder; the stagnation points at 0 and 180 deg; incomplete recovery; supercritical recovery more complete than subcritical.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | The issue is resolved. The three direct labels are `\small`, all clear the curves, and nothing regressed. | fig24.tex:21-29 | None. |
| 2 | note | The $R_d = 3 \times 10^5$ label moved from the right end (as printed) to above its curve's knee (107-140 deg). At the house size, the computed theory curve runs through the printed spot. The move is justified, and it is recorded as the fixer's gate doubt. | fig24.tex:26 | List it at the Chapter 3 gate with the $C_p$ ordinate addition. |
| 3 | note | The issue's premise is not exact. The approved Ch2 curve families, Figs 24, 25, 30 and 31, set their curve labels in `\footnotesize` (e.g. ch2/fig25.tex:26), and Fig 24's round-1 audit cited Ch2 Fig 25 as its precedent. The fix follows STYLE s.16 (labels `\small`), so it stands. | ch2/fig24, 25, 30, 31.tex | For the orchestrator: either confirm `\footnotesize` as an allowed exception for crowded curve families, or list those four Ch2 figures for the same change. |

## Verdict: pass

No must-fix and no should-fix.
