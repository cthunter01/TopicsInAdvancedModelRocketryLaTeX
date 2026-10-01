# v2 consistency verification: ch3/fig16

Issue verified: labelled free-stream velocity arrows were drawn at two weights across Chapter 3. They were `vec` in
Figs 06, 11, 27, 28, 29, 39 and 51, and `thin vec` in Figs 16, 25, 30 and 34. The fix for this figure was the
U_inf arrow at fig16.tex:44.

Sources checked:
- the scan `figures/ch3/fig16.png`, with the U_inf and x arrows zoomed 4x
- the redraw `figures/v2/ch3/fig16.pdf`, current by `make -q` (built 23:12:29, after the 23:12:28 .tex): 325.23 x 148.31 pt = 4.52 x 2.06 in, all fonts embedded. I rendered it at 400 dpi and the U_inf end at 1200 dpi.
- `build/v2/png/ch3-fig16-compare.png`
- `figures/v2/ch3/fig16.tex`, `fig16.py`, `fig16-*.csv` and `fig16.calib.json`
- the inventory row `ch3-fig16`
- STYLE.md section 16 ("force and velocity vectors `vec` ... lighter arrows `thin vec`") and the kit styles `vec` and `thin vec` in `tamrfig.sty`:62-63
- the round-1 and round-2 reports
- every labelled `vec` and `thin vec` arrow in `figures/v2/ch3/*.tex`

Checks made:
- **The issue is resolved.** fig16.tex:44 is now `\draw[vec] (8,0) -- (62,0) node[midway, above=1pt] {$U_\infty$};`, the kit style, not a local one. Elsewhere in the chapter, labelled free-stream arrows are now `vec`: Fig 06 (U), Fig 25 (U_inf, u), Fig 34 (U), Fig 51 (U_inf), and also Fig 30:37 and :56 and Figs 11, 27, 28 and 29. The remaining `thin vec` arrows with symbol labels are coordinate axes (x, y in Figs 13, 16, 17 and 37, y in Fig 06) and tau_o (Figs 16 and 17).
- **Only the intended change.** I compiled a scratch copy of the file with line 44 set back to `thin vec`. It is 324.88 x 148.31 pt, which is the size the round-2 report records, so the rest of the file matches the audited state. I then compiled both versions with one fixed bounding box and compared them pixel by pixel at 400 dpi. The only differences are the arrow (drawing x = 6 to 60) and the U_inf label, which sits 0.35 pt higher because the node's default outer sep grows with the line width. This keeps the label's gap above the thicker shaft. The figure is 0.35 pt wider than before, because the heavier round cap at x = 8 sets the left edge. The cap is drawn whole and is not clipped (checked at 1200 dpi).
- **No regression against the scan or the data.** The data CSVs (22:17) and fig16.py predate both round-2 audits. I re-ran the overlay myself: 95% within 2.00 px for the body (max 3.16) and 1.00 px for the profile (max 1.41), the same as rounds 1 and 2.
- **Lettering matches the inventory.** U(x), u(y), $\tau_o$, ds, $\phi$, $U_\infty$ "with arrow, upstream on the axis" and x "axis arrow downstream" are all present, and nothing is added. The U_inf label is centred over its shaft and clear of it. The arrowhead stops 16 units (3.3 mm) before the dash-dot axis starts.
- **The figure reads correctly.** The heavy U_inf arrow and the light x arrow lie on the same axis line and are clearly different: one is the free stream, the other the coordinate. Fig 06 uses the same pairing (U `vec`, y `thin vec`). The 1973 art draws both arrows at about one weight, so this follows the house convention, not the scan, which is acceptable for the modernized style.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | Resolved: the U_inf free-stream arrow is now kit `vec`, which matches the chapter's other labelled velocity arrows (STYLE s.16). Nothing else changed apart from a 0.35 pt lift of the label (outer sep) and 0.35 pt more page width (the heavier cap). | fig16.tex:44 | none |
| 2 | note | The fixer's style suggestion: $\tau_o$ is `thin vec` here and in Fig 17. These are the only Ch3 figures that draw tau_o, so the chapter is consistent. tau_o is a wall stress, not a free-stream velocity. Here its arrow also continues the tangent for about 4 cm, and a heavy arrow would outweigh the profile. The 1973 line is thin, and Fig 17's is a short stroke. Keeping both thin is reasonable, and the issue did not raise it. | fig16.tex:48; fig17.tex:69 | none (if the owner wants stresses treated as forces, change Figs 16 and 17 together) |
| 3 | note (gate) | Carried from rounds 1 and 2: phi is 22.5 deg on the true tangent, against about 21 deg in 1973. There is still no entry in `corrections/v2-figures.md`. | fig16.tex:4 | orchestrator: log under "Minor (logged only)" |

## Verdict: pass (no must-fix)
