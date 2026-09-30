# v2 audit: ch4/fig06a (round 2)

Sources checked: scan `figures/ch4/fig06a.png`; redraw `figures/v2/ch4/fig06a.pdf` (rendered 300 and 600 dpi, with
crops of the $k_{\min}$ and $k_{\max}$ callouts and the origin); source `figures/v2/ch4/fig06a.tex` lines 1-30,
`fig06.py` lines 1-30, `fig06a.csv` (41 rows), `fig06a.calib.json` (all changed since round 1 except the
calibration). I reran `fig06.py` with `trajectory.py` on a copy in the scratch directory: the fig06a/b/c.csv it
writes are byte-identical to the repository's. I also reran `digitize.py overlay` of the four curves. Other
sources: round-1 report; inventory row `ch4-fig06a` (`figures/v2/inventory.csv`:129); the float and caption
`chapters/ch4-sec2b.tex`:401-406 (panel letter by `\figurepanel{a}`); `corrections/v2-figures.md`:61 (the Ch4
Fig 6 gate item); `STYLE.md` section 16.

| round-1 # | severity | status | evidence |
|-----------|----------|--------|----------|
| 1 | should-fix | resolved | The $k_{\min}$ label now sits below both curves at (0.036, -6.2) (fig06a.tex:25), and all three problems are gone. (a) The label is about 6.8 mm below the dashed CB $k_{\min}$ curve (600 dpi crop). (b) The CB leader is a short vertical from the label's north anchor to (0.036, -2.52) (fig06a.tex:26). It meets the curve at a clear angle. The CSV value there is -2.496, a 0.14 pt difference that cannot be seen. (c) The FM leader runs from the label's north-west corner (about y = -5, well clear of the zero line) to (0.026, 1.946), which is FM $k_{\min}$ at 0.026 exactly (fig06a.csv row 5), and meets that curve at a clear angle. The $k_{\max}$ leaders still end on their curves: (0.060, 7.975) and (0.046, 2.440) match CSV rows 22 and 15. |
| 2 | should-fix | resolved | fig06.py:16 samples 0.021, then 0.022 + 0.002 i up to 0.100 (docstring :4-6: 21 g is the engine alone, where the printed curves start). The first row is 0.021: 2.962 / -4.445 / 8.949 / 7.634 (FM $k_{\min}$ / CB $k_{\min}$ / FM $k_{\max}$ / CB $k_{\max}$), which agrees with round 1's independent values at 0.021. Each curve continues monotonically into 0.022, with no hook. In the render the curves begin 0.001 kg (about 1.1 mm) right of the y axis, as printed. |
| 3 | should-fix | resolved | Logged at corrections/v2-figures.md:61 (gate, pilot). The entry says the overlay puts 95% of the points 4-6 px (0.7-1.0 mm) from the ink for all four curves, with the $k_{\min}$ pair about 0.6 point low. The rerun overlay with the current CSV agrees: 95% at FM $k_{\max}$ 4.00 px, CB $k_{\max}$ 5.00 px, FM $k_{\min}$ 4.00 px and CB $k_{\min}$ 5.83 px. Under the listed decisions this is a gate item, not a finding. |
| 4 | note | accepted: no action | The calibration still handles the scan's non-linear x axis piecewise (`xgrid`); the redraw's axis is linear, which is correct. |
| 5 | note | accepted: gate item | The offset is covered by the same log entry (corrections/v2-figures.md:61). |

## New findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | With the $k_{\min}$ label below both curves, its leader to FM $k_{\min}$ crosses the dashed CB $k_{\min}$ curve (near $m_o$ = 0.031, y = -3.1) and the zero line before reaching the solid curve. The 1973 label sits between the two curves, so neither of its leaders crosses a curve. The crossing is at a steep angle, and the leader runs on about 5 points past the dashed curve, so it still reads as pointing to the solid curve. | fig06a.tex:25, 27 | None needed. Optional: a label between the curves at the left (about (0.026, -1.2)) would avoid the crossing, but that space is tight at this size. |

Also checked, with no issue: the legend (solid "Fehskens-Malewicki", dashed "Caporaso-Bengen", lower right, spelled
as in ch4-sec2b.tex:319-320, 345); the thin solid zero line (inventory: "a thin solid horizontal zero line"); the y
title "Percent error in $v_b$"; y ticks -15 to 15 in steps of 5 with true minus signs; x ticks 0.02-0.10 with
leading zeros and minor ticks at 0.01; the x title $m_o$ (kg). No panel letter is drawn in the art: `\figurepanel{a}`
supplies it in the float, as for the other panels of Figs 5-9. The figure is 4.73 in wide.

## Verdict

pass (0 must-fix, 0 should-fix)
