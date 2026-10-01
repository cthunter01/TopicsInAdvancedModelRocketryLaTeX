# v2 audit: ch3/fig25 (round 2)

Sources checked: the scan `figures/ch3/fig25.png`, both halves zoomed 3x; the redraw `figures/v2/ch3/fig25.pdf`
(current by `make -q`; 333.6 x 172.8 pt = 4.63 x 2.40 in; fonts all embedded), rendered at 400 dpi, with the
a-c and d-e/vortex regions at 900 dpi; `build/v2/png/ch3-fig25-compare.png`; `figures/v2/ch3/fig25.tex`,
`fig25.py`, `fig25-*.csv` and `fig25.calib.json`; the inventory row `ch3-fig25` (`figures/v2/inventory.csv`:91);
the caption and citing text in `chapters/ch3-sec3c-sec4a.tex`:232-275; the kit (`curve tag`, `leader`) in
`figures/v2/tamrfig.sty`; Ch3 Figs 23 and 33, which also use `curve tag` for cited points; the round-1 report
and the round-1 fix notes.

Checks made:
- **Round-1 must-fix 1 (station letters in curve tag): resolved.** fig25.tex:69 sets a-e with
  `\node[curve tag] at ($(\p)!13pt!180:(\p top)$) {\p};`. That is the kit style (no local circled style), with
  the letters upright as the text prints them ("point a", "the separation point c", "points d and e"). Each tag
  sits on its profile's normal, 13 pt below the foot. The 11 pt circle and the 10-unit (5.8 pt) band leave
  about 1.5 pt clear. At 900 dpi all five tags clear the hatch, and c clears the pressure-gradient arrow by
  about 1.3 mm.
- **Round-1 should-fix 2 (vortex leader): resolved.** fig25.tex:82 draws a straight kit `leader` (ink2) from the
  point `vortex` (518.000, -58.223) up and right to the label's west side. I split fig25-stream.csv into its five
  lines: the point lies 0.16 units from the innermost U-shaped streamline (nose at x = 444.6, psi = -5.282), on
  its lower (reversed-flow) branch. The leader ends about 3 mm downstream of that branch's arrowhead and crosses
  nothing. "vortex" sits inside the recirculating loop, between the dash-dot u = 0 line and the lower branch.
  It is not clipped (2.2 mm from the right edge). The 1973 label stands outside the bundle where the streamline
  ends, but the computed streamlines leave no room there, so this placement (stated in the fix notes) is
  reasonable.
- **No regressions.** I re-ran fig25.py into a temporary directory, deleted afterwards. All 13 CSVs are
  byte-identical to the repository's, including fig25-points.csv with the new `vortex` row. It printed
  f''(0) = 0.5311, 0.2818, 0.0000, -0.1417, -0.1259 for a-e: c is the separation profile of eq. (110), and d and
  e are reversed. I ran the overlay myself; 95% within: wall 2.83, edge 2.24, a 2.83, b 2.00, c 2.24, d 8.06,
  e 2.83, u = 0 line 11.00, all streamlines together 7.21 px. These equal the round-1 figures and the header.
  The size is unchanged.
- **Content.** All inventory lettering is present: "Undisturbed outer flow" with three flow arrows, $U_\infty$
  and u over their arrows, the delta `\dimline` (53 units = edge(30), checked), a-e, "Positive / pressure /
  gradient" with its arrow parallel to the wall, and "vortex" with its leader. The text's "line of stationary
  fluid ... as at points d and e" holds: d and e cross u = 0 on the dash-dot line, and the flow outside it moves
  forward.
- **Family.** The profile, profile arrow and profile stroke styles, the 10 px spacing, the 10-unit 45 deg wall
  band, thin vec for the free-stream arrows, and the 1.2x scale are the same as in Figs 16-18.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | Round-1 must-fix 1 (a-e in `curve tag`) is resolved, with the tags clear of the hatch band and the pressure-gradient arrow. | fig25.tex:67-70 | none |
| 2 | note | Round-1 should-fix 2 is resolved: a straight `leader` runs from "vortex" to a point on the innermost recirculating streamline's lower branch (checked against fig25-stream.csv, 0.16 units off). | fig25.tex:82; fig25-points.csv:12 | none |
| 3 | note (gate) | Carried from round 1: d's shallower reversed layer (8.1 px), the u = 0 line (11 px) and the streamlines (7.2 px overall, up to 18 px max) differ from the 1973 freehand art. They are listed in the .tex header but are still missing from `corrections/v2-figures.md`. | fig25.tex:7-9 | orchestrator: log them with the Ch3 items |

## Verdict: pass (no must-fix)
