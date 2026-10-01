# v2 audit: ch3/fig52 (round 2)

Sources checked: scan `figures/ch3/fig52.png`; redraw `figures/v2/ch3/fig52.tex` (21:52), `fig52.py`, `fig52.csv`
(21:59), `fig52.calib.json`, `figures/v2/ch3/fig52.pdf` (21:59). All of these predate the round-1 audit (22:12), so
the figure is unchanged. I rendered the PDF at 400 dpi (whole figure) and at 1200 dpi (the legend, and the curves
leaving the top). Also checked: `build/v2/png/ch3-fig52.png`; inventory row ch3-fig52; caption and citing text
`chapters/ch3-sec6c.tex` lines 449-566 (eqs. (210), (211), Table 7, "no distinction ... below 1e5", "within 10%
from 4e5 to 2.2e6"); the round-1 audit and the fix report; `tamrfig.sty` legend style (line 177); `pdffonts` (all
fonts embedded); page 452.4 x 292.6 pt = 6.28 in wide.

Round-1 follow-up: round 1 had no must-fix or should-fix findings. The fixer passed notes 2 and 3 on as style
suggestions (the kit's legend `fill opacity=0.9`; the `\small` legend font). Note 1 (the curves differ from the
1973 art above 0.5 N; Table 7 D_e at 2e6 is 0.9% off) needs no figure change. No regression.

Independent checks (repeated):
- I recomputed with my own code D_e = 3.33e-13 (C_Do)_FB R^2, with (C_Do)_FB from the printed GCR-x equations, and
  D_a = 3.33e-13 x 0.473 R^2. They match fig52.csv to 1.0e-5 relative. At 1e6, 2e6 and 2.2e6 they give 0.157,
  0.577 and 0.688 for D_e and 0.158, 0.630 and 0.762 for D_a (Table 7: 0.156/0.157, 0.582/0.631,
  0.689/0.763). The curves leave 0.8 N at 2.39e6 (D_e) and 2.25e6 (D_a), clipped cleanly at the frame (1200 dpi).
- The text's claims hold. The two curves cannot be told apart below 1e5. The ratio (C_Do)_FB/0.473 is 1.10 at 4e5
  and 0.90 at 2.2e6 ("within 10%"). D_a lies above D_e beyond about 1.2e6.
- Overlay (`digitize.py overlay`; I wrote the overlay CSVs from fig52.csv in scratch and did not rerun fig52.py),
  95th percentile: D_e 2.24 px, D_a 2.00 px.
- Axes, frame and size are identical to Fig 51 (5.4 x 3.5 in). The legend sits at the lower right with $D_e$
  (series1, solid) and $D_a$ (series2, dashed), as printed.

## Findings
| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | Still open at kit level, from round-1 note 2. The kit's `legend style` uses `fill opacity=0.9`, so the PDF carries transparency. At 1200 dpi the gridlines show through the legend box as RGB (250,250,249) ghosts. That is invisible in print, but it is against the flat-art rule. The fixer correctly passed it to the kit owner. If the kit is not changed before this figure is switched, a local `fill opacity=1` in this figure's `legend style` options would remove it without redefining the kit style. | tamrfig.sty line 177; fig52.tex `legend style={...}` | kit owner: `fill opacity=1` |
| 2 | note | Round-1 note 3: the legend is `\small` against the kit's `\footnotesize`. It matches this family's curve labels (Fig 51). This is a gate choice, not a defect. | | none |

## Verdict: pass (no must-fix)
