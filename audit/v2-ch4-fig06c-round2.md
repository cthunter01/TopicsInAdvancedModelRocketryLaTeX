# v2 audit: ch4/fig06c (round 2)

Sources checked:
- Scan `figures/ch4/fig06c.png`, with a 5x zoom of the callouts.
- Redraw `figures/v2/ch4/fig06c.pdf`, rendered at 300 and 600 dpi, with crops of the $k_{\min}$ callout. I
  measured the leader pixels in the 600 dpi render.
- Source files `fig06c.tex`, `fig06c.csv` (committed with the pilot, unmodified) and `fig06c.calib.json`.
- `fig06.py` and `trajectory.py`, which I read and ran but did not edit.
- Template `fig06a.tex`, compared by diff.
- Inventory row `ch4-fig06c`.
- The book's equations: `chapters/ch4-sec2a.tex`:55-64 and :118-130, and `ch4-sec2b.tex`:56-66 and :281-300.
- Caption: `ch4-sec2b.tex`:416-422.
- `corrections/v2-figures.md`:41, :74-81 and :157.
- Round-1 audit and fix reports.
- A scratch copy of fig06c.tex with the leader change suggested below, compiled and rendered in my scratch
  directory. The repository file was not touched.

Checks made:
- **Data, recomputed independently.**
  - My own implementation (not importing `trajectory.py`): the interval method (83)-(87), dt = 0.001 s, with the
    mass by (74), coasting at the burnout mass to apex. For each approximation, eq. (67) at $m_b$ with its own
    $v_b$, added to (21) or (27).
  - All 164 values agree with fig06c.csv within 0.0005 point.
  - The Table 2 regression in `trajectory.py` passes.
- **Overlay** (computed curves, numbers for the record; `digitize.py overlay`):

  | curve | 95% | max |
  |---|---|---|
  | FM $k_{\max}$ | 4.00 px (0.68 mm) | 4.00 px |
  | CB $k_{\max}$ | 6.08 px (1.03 mm) | 6.08 px |
  | FM $k_{\min}$ | 6.08 px (1.03 mm) | 7.00 px |
  | CB $k_{\min}$ | 9.00 px (1.52 mm) | 9.22 px |

  These are the same as round 1. The computed curves are the pilot-gate decision.
- **Round-1 note 2 (the $k_{\min}$ label): applied, but the new leaders are weak.**
  - The label moved from (0.068, -5.3) to (0.0375, -2.25), into the gap between FM $k_{\min}$ (-0.57) and CB
    $k_{\min}$ (-3.80), as printed. No leader now crosses a curve, and both endpoints lie on the CSV curves
    (difference 0.000).
  - The label's box, with the default inner sep, spans -1.0 to -3.44. That leaves 0.4 point (0.8 mm) above it
    and below it. So the `north east` and `south` leaders run almost horizontally:
    - the upper one rises 6.0 deg over 4.2 mm to FM $k_{\min}$, which falls about 3 deg there;
    - the lower one falls 6.7 deg over 3.2 mm to CB $k_{\min}$, which rises about 4 deg.
  - Each meets its curve at only about 9-10 deg.
  - At 300 dpi the lower leader sits 1.4-1.8 mm under "min" and reads as an underline of the label. The upper
    leader reads as a short stub under the solid line.
  - The scan's leaders for this label meet their curves at about 19 and 50 deg. The family's other forks meet
    theirs at 25 deg or more: fig06a, 6(b) and 5(a)-(c), and this figure's own $k_{\max}$.
- **$k_{\max}$ callout.** Unchanged:
  - `south east` runs to (0.036, 0.908) on FM $k_{\max}$;
  - `south west` runs to (0.026, -2.380) on CB $k_{\max}$, crossing both FM curves and the zero line, as
    printed.
- **Content.** All present: the y title "Percent error in $y_{\max}$" (upright max), y ticks -15 to 15, x ticks
  0.02-0.10 with the minors, $m_o$ (kg), both k labels with two leaders each, the legend at upper right (as
  printed) and the zero line.
- **Template.**
  - The diff against fig06a.tex changes only the header, the y title, the legend position, the CSV name and the
    label positions.
  - Page 4.74 x 3.05 in, fonts embedded.
- **Caption.** "Maximum altitude error ... Type B4 engine" holds.
- **The relayed request "Keep 1-3 as they are, use exact curves for 46".** It is the owner's Chapter 3 gate
  answer: Ch3 Figs 9, 12 and 28, and Ch3 Fig 46's exact curves (corrections:120-157). It does not concern Ch4
  Fig 6, so round 1's note 3 is closed.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | should-fix | The $k_{\min}$ leaders, new this round, meet their curves at about 9-10 deg. The label box nearly fills the 3.2-point gap, so `kmin.north east` and `kmin.south` can only run sideways. At final size the lower leader looks like an underline beneath "min" rather than a pointer to the CB $k_{\min}$ dashes, and the upper one looks like a stub under FM $k_{\min}$. The printed leaders meet the curves at about 19 and 50 deg, and every other fork in the family at 25 deg or more. | fig06c.tex:27-29 | Keep the label at (0.0375, -2.25) and fork both leaders from its east side to CSV points at 0.046: `\draw[leader] (kmin.east) -- (axis cs:0.046,-0.855);` and `\draw[leader] (kmin.east) -- (axis cs:0.046,-3.460);`. I compiled this on a scratch copy. The leaders open at about +/-22 deg, each about 7 mm long, meet their curves at about 25 deg and cross nothing. Any other arrangement that meets each curve at 20 deg or more without crossings is equally acceptable. |
| 2 | should-fix (orchestrator; no change to the figure) | Still open from round 1. The Ch4 Fig 6 entry quotes only 6(a)'s overlay ("4-6 px (0.7-1.0 mm)"), which understates 6(c). STYLE s16 asks for each failed overlay to be logged. The fixer declined properly, since corrections/ is not among its files, and passed the numbers on. | corrections/v2-figures.md:74-81 | Orchestrator: add "6(c): 95% at 4.0-9.0 px (0.7-1.5 mm); computed 0.3 point low at 0.022, rising to about 1 point low at 0.10 (CB $k_{\min}$ -3.79 against about -2.8 printed; FM $k_{\min}$ -3.16 against about -2.2)". |

## Verdict

fix (0 must-fix; 2 should-fix). Finding 1 is a two-line leader change in fig06c.tex. Finding 2 is
record-keeping for the orchestrator. The data are re-verified and unchanged.
