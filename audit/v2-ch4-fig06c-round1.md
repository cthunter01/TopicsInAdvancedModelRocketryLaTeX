# v2 audit: ch4/fig06c (round 1)

Sources checked:
- Scan `figures/ch4/fig06c.png` (2x upscale).
- Redraw `figures/v2/ch4/fig06c.pdf`: 300 and 400 dpi renders, with a crop of the callouts; `pdffonts`.
- Source files `fig06c.tex`, `fig06c.csv` (41 rows) and `fig06c.calib.json`.
- `fig06.py` and `trajectory.py`, which I read but did not edit.
- Template `fig06a.tex`, compared by diff, and its audits (rounds 1 and 2).
- Inventory row `ch4-fig06c`.
- Chapter text:
  - `chapters/ch4-sec2a.tex`:55-64 and :122-128;
  - `chapters/ch4-sec2b.tex`:56-58 (eq. (67)), :300-303 (coasting "entirely analogous"), :308-330, :343-372 and
    :416-422 (caption).
- `corrections/v2-figures.md`:41 and :74-81.
- `STYLE.md` section 16.

Checks made:
- **Data.**
  - The Table 2 regression in `trajectory.py` passes.
  - I recomputed the $y_{\max}$ errors (index 2) at all 41 masses. The largest difference from fig06c.csv is
    0.0005 point.
  - Exact $y_{\max}$ is the interval method run through the coast at the burnout mass.
  - Each approximation adds eq. (67) at $m_b$ with its own $v_b$, as the .tex header says and as the text describes
    (inventory: $y_{\max} = y_b + y_c$ by (67)).
- **Overlay** (`digitize.py overlay`, the drafter's calibration):

  | curve | mean | 95% | max |
  |---|---|---|---|
  | FM $k_{\max}$ | 2.43 px | 4.00 px (0.68 mm) | 4.00 px |
  | CB $k_{\max}$ | 3.95 px | 6.08 px (1.03 mm) | 6.08 px |
  | FM $k_{\min}$ | 2.96 px | 6.08 px (1.03 mm) | 7.00 px |
  | CB $k_{\min}$ | 5.73 px | 9.00 px (1.52 mm) | 9.22 px |

  Computed against printed (the inventory's readings):

  | curve | 0.022 | 0.06 | 0.10 |
  |---|---|---|---|
  | FM $k_{\max}$ | 2.21 vs ~2.5 | -0.18 vs ~0 | -1.66 vs ~-0.9 |
  | FM $k_{\min}$ | 0.22 vs ~0.6 | | -3.16 vs ~-2.2 |
  | CB $k_{\max}$ | -1.41 vs ~-0.8 | -6.84 vs ~-6.5 | -8.39 vs ~-7.7 |
  | CB $k_{\min}$ | -4.38 vs ~-4.1 | -3.16 vs ~-2.5 | -3.79 vs ~-2.8 |

  So the computed curves lie 0.3 point low at the left and up to about 1.0 point low at the right. This is the
  offset the inventory already notes ("y_max errors run ~0.5-1 point more negative than print"). The shapes are
  as printed: CB $k_{\min}$ is shallow and U-shaped, the CB pair crosses near 0.034, and FM $k_{\max}$ crosses 0
  near 0.055. Using the computed curves is the owner's pilot-gate decision.
- **Lettering.**
  - y title "Percent error in $y_{\max}$" (upright max); y ticks -15 to 15 in steps of 5.
  - x title $m_o$ (kg); x ticks 0.02-0.10 with minor ticks at 0.01.
  - $k_{\max}$ and $k_{\min}$, each with two leaders.
  - Legend at upper right, as printed, clear of the curves.
  - The thin zero line.
  - No panel letter in the art (`\figurepanel{c}`).
- **Leaders.**
  - All four end exactly on the CSV curves: (0.036, 0.908) FM $k_{\max}$, (0.026, -2.380) CB $k_{\max}$, (0.062,
    -3.148) CB $k_{\min}$, (0.076, -2.037) FM $k_{\min}$.
  - The $k_{\max}$ callout matches the scan. Its leader to CB $k_{\max}$ crosses both FM curves and the zero line,
    as the printed one does.
- **Template.** The diff against fig06a.tex changes only the header comment, the y title, the legend position, the
  CSV name and the label positions. Size 4.74 x 3.06 in. Fonts embedded.
- **Caption.** The caption (maximum-altitude error, B4) holds.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | should-fix | The overlay misses the tolerance on all four curves. For CB $k_{\min}$ it reaches 95% at 9.0 px (1.52 mm), about 1 point below the print at 0.10, and the CB $k_{\max}$ and FM $k_{\min}$ curves reach 6.1 px (1.03 mm). The Ch4 Fig 6 entry in corrections/v2-figures.md quotes only 6(a): "4-6 px (0.7-1.0 mm) ... the k_min pair about 0.6 point low". That understates 6(c). STYLE s16 requires the mismatch to be logged. | corrections/v2-figures.md:74-81 | Orchestrator: extend the entry with "6(c): 95% at 4.0-9.0 px (0.7-1.5 mm); computed 0.3 point low at 0.022 rising to about 1 point low at 0.10 (CB $k_{\min}$ -3.79 against about -2.8 printed; FM $k_{\min}$ -3.16 against about -2.2)", so that the owner sees 6(c)'s size of offset. No change to the figure or data. |
| 2 | note | The $k_{\min}$ label has moved. In the print it sits at about (0.040, -1.5), between FM $k_{\min}$ and CB $k_{\min}$, so neither leader crosses a curve. In the redraw it is at (0.068, -5.3), below CB $k_{\min}$, and its leader to FM $k_{\min}$ at 0.076 crosses the CB $k_{\min}$ dashes. The crossing is steep and the leader runs on to the solid line, so it is legible; 6(a) has the same kind of crossing (accepted in its round 2). Label position is not a content invariant. | fig06c.tex:27-29 | Optional: put the label at about (0.046, -2.2), in the 2.7-point gap at 0.045 between FM $k_{\min}$ (-0.82) and CB $k_{\min}$ (-3.50). Run short north and south leaders to (0.046, -0.86) and (0.046, -3.47). That is the printed arrangement, with no crossing. |
| 3 | note | As for 6(b), the relayed request "use exact curves for 46" agrees with the computed curves if "exact" means the book's interval method. | - | Orchestrator: confirm the reading. |

## Verdict

pass (0 must-fix, 1 should-fix, a record-keeping item outside the figure)
