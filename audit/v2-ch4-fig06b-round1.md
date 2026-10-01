# v2 audit: ch4/fig06b (round 1)

Sources checked:
- Scan `figures/ch4/fig06b.png` (2x upscale).
- Redraw `figures/v2/ch4/fig06b.pdf`: 300 and 400 dpi renders, with a crop of the callouts; `pdffonts`.
- Source files `fig06b.tex`, `fig06b.csv` (41 rows) and `fig06b.calib.json`.
- `fig06.py` and `trajectory.py`, which I read but did not edit.
- Template `fig06a.tex`, compared by diff, and the template's audits `audit/v2-ch4-fig06a-round1.md` and
  `-round2.md`.
- Inventory row `ch4-fig06b`.
- Chapter text:
  - `chapters/ch4-sec2a.tex`:55-64 (eqs. (20), (21)) and :122-128 (eqs. (27), (28));
  - `chapters/ch4-sec2b.tex`:56-58 (eq. (67)), :169-192 (eqs. (73), (74)), :308-330, :343-372 (key table, B4
    $k_{\min} = .00005$, $k_{\max} = .002$) and :408-414 (caption).
- `corrections/v2-figures.md`:41 (pilot gate: use the computed curves, Ch4 Fig 6 named) and :74-81 (the Ch4 Fig 6
  entry).
- `STYLE.md` section 16.

Checks made:
- **Data.**
  - `trajectory.py`'s self-test passes against Table 2's "No disturbance" row: computed 111.407 / 78.058 / 6.461 /
    265.561 / 343.618.
  - I recomputed the $y_b$ errors (index 1 of `interval`, `fehskens_malewicki` and `caporaso_bengen`) at all 41
    liftoff masses in a scratch session. The largest difference from fig06b.csv is 0.0005 point, which is the
    CSV's rounding.
  - The formulas are eqs. (20), (21), (27) and (28) as printed, with $m = m_o - m_p/2$ and $F = I_t/t_b$. The
    error is 100(approx - exact)/exact.
  - The sampling is 0.021 (the engine alone, where the printed curves start), then every 2 g to 0.100.
- **Overlay** (`digitize.py overlay`, the drafter's calibration, residual 1.01 px):

  | curve | mean | 95% | max |
  |---|---|---|---|
  | FM $k_{\max}$ | 2.96 px | 5.00 px (0.85 mm) | 6.00 px |
  | CB $k_{\max}$ | 3.32 px | 5.10 px (0.86 mm) | 5.39 px |
  | FM $k_{\min}$ | 2.16 px | 4.00 px (0.68 mm) | 4.00 px |
  | CB $k_{\min}$ | 3.82 px | 5.39 px (0.91 mm) | 6.00 px |

  All four run 0.5-0.7 point below the print throughout. At 0.022 and at 0.10, computed against printed (the
  inventory's readings):

  | curve | 0.022 | 0.10 |
  |---|---|---|
  | FM $k_{\max}$ | 1.46 vs ~2 | -9.71 vs ~-9 |
  | CB $k_{\max}$ | -2.82 vs ~-2.2 | -13.80 vs ~-13.3 |
  | FM $k_{\min}$ | -3.94 vs ~-3.2 | -12.26 vs ~-11.7 |
  | CB $k_{\min}$ | -8.05 vs ~-7.5 | -12.44 vs ~-11.9 |

  The shapes and crossings are as printed: FM $k_{\max}$ crosses 0 near 0.029, and CB $k_{\max}$ crosses FM
  $k_{\min}$ near 0.036 and CB $k_{\min}$ near 0.047. Using the computed curves is the owner's pilot-gate decision,
  so the offset is not a finding in itself.
- **Lettering.**
  - y title "Percent error in $y_b$"; y ticks -15 to 15 in steps of 5.
  - x title $m_o$ (kg); x ticks 0.02-0.10 with minor ticks at 0.01.
  - $k_{\max}$ and $k_{\min}$, each with two leaders.
  - Legend at upper right, as printed (unlike 6(a)); it is clear of all curves.
  - The thin zero line.
  - No panel letter in the art (`\figurepanel{b}`).
- **Leaders.**
  - All four end exactly on the CSV curves: (0.038, -1.809) FM $k_{\max}$, (0.026, -4.364) CB $k_{\max}$, (0.026,
    -5.337) FM $k_{\min}$, (0.032, -8.943) CB $k_{\min}$.
  - The arrangement matches the scan.
  - Both forks diverge.
  - The $k_{\max}$ label has about 2 points of clearance to CB $k_{\max}$ below it and 2.5 points to FM $k_{\max}$
    above it.
  - The $k_{\min}$ leader to FM $k_{\min}$ crosses CB $k_{\min}$ steeply, as the printed one does.
- **Template.** The diff against fig06a.tex changes only the header comment, the y title, the legend position
  (north east), the CSV name and the label positions. Size 4.74 x 3.06 in. The 0.01 in difference from fig06a
  comes from the rotated $y_b$ title's descender. Fonts embedded.
- **Caption and text.**
  - The caption (burnout-altitude error, B4) holds.
  - Computed, CB $k_{\max}$ reaches -13.8%, which contradicts the text's 10% claim (ch4-sec2b.tex:326-330). This is
    already logged as a v1 item.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | should-fix | The overlay misses the 3 px tolerance on all four curves: 95% at 4.0-5.4 px (0.68-0.91 mm), with the computed curves 0.5-0.7 point below the print. The Ch4 Fig 6 entry in corrections/v2-figures.md is headed "(pilot sample 6(a))" and quotes only 6(a)'s overlay. STYLE s16 requires each failed overlay to be logged, and the 6(a) round-1 audit asked for 6(b)/(c) to be added once audited. | corrections/v2-figures.md:74-81 | Orchestrator: extend the entry with "6(b): 95% at 4.0-5.4 px (0.7-0.9 mm), all four curves 0.5-0.7 point below the print". No change to the figure or data. |
| 2 | note | The relayed owner request "Keep 1-3 as they are, use exact curves for 46" agrees with this redraw if "exact" means the book's exact interval-method computation, which the gate already chose for Ch4 Fig 6 (corrections:41). If it means the printed curves, 6(b) would have to be traced instead. | - | Orchestrator: confirm the reading. Nothing to do if computed is meant. |

## Verdict

pass (0 must-fix, 1 should-fix, a record-keeping item outside the figure)
