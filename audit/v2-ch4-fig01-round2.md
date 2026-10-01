# v2 audit: ch4/fig01 (round 2)

Sources checked:
- Scan `figures/ch4/fig01.png`.
- Redraw `figures/v2/ch4/fig01.pdf` (rebuilt with `make fig F=ch4/fig01`; clean log, 3.40 x 5.91 in). I looked at
  300 and 800 dpi renders, an 800 dpi crop of the lower half of (b) and of the exhaust triangle, a 4x zoom of the
  150 dpi render of the dm_e slice, and `build/v2/png/ch4-fig01-compare.png`. All fonts are embedded. There are no
  opacity operators or soft masks; the only patterns are the hatch.
- Source `fig01.tex`, as changed by the round-1 fix.
- Inventory row `ch4-fig01`, and the caption and citing text in `chapters/ch4-intro-sec1.tex`:98-125.
- Round-1 audit `audit/v2-ch4-fig01-round1.md` and the fixer's report.
- `figures/v2/tamrfig.sty`: unchanged since before round 1 apart from the legend opacity, which does not affect
  this figure.

## Round-1 findings

- **1 (must-fix, dm_e slice not reading as hatched): resolved.**
  - `fig01.tex`:55 now fills the slice with `hatch back` (135 deg), so the lines cross the 60 deg axis at 75 deg.
  - `\slab` is now 0.8 (:52). S, the aft-face line, the c / v / c + v triangle and the dm_e leader all follow it.
  - At 800 dpi, four ink2 lines cross the slice between the tail and the aft face.
  - In the 150 dpi render the slice reads clearly as a hatched band, and the dm_e leader ends on its lower edge.
- **2 (note, four ends at one corner): improved.** With the deeper slice, the head of c ends 0.4 units past the
  plume tip, so the plume outlines meet just inside the arrowhead. The centre line ends inside the head. The
  corner reads cleanly at 800 dpi.
- **3 (note, C.G. at 0.72 L): no change needed.** Each figure follows its own 1973 drawing.
- **4 (note, departures recorded only in the header): still open, optional, for the orchestrator.** These are the
  longer vectors, the v + dv label at its head, E into the C.G. and c + v at 19 deg. The header now also mentions
  the 0.8-unit slice.

## Regression check

- Panel (a) matches the compare from round 1.
- In (b), nothing outside the lower triangle moved: E, v, dv, v + dv, both state lists and the panel letter are
  unchanged.
- The exhaust triangle still closes head to tail, so c + v is c plus v, as eq. (4) and the text (:150-152) need.
- All lettering is present and unchanged: both state lists, every `\vec` label, dm_e with an italic e, and (a),
  (b) at the lower right.
- The caption and the text claims still hold.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | The fixer read the relayed user request ("Keep 1-3 as they are, use exact curves for 46") as the Chapter 3 gate answer, and I agree. `corrections/v2-figures.md`:157-160 records that answer with the same date: three items kept as redrawn (Ch3 Figs 9, 12, 28) and Ch3 Fig 46 with the exact curves. Chapter 4 has no Figure 46. So the request does not freeze Ch4 Figs 1-3, and the round-1 must-fix was rightly applied. | `fig01.tex`:52, :55 | None. If the orchestrator reads the request otherwise, the revert is two lines: `hatch back` -> `hatch` and `\slab` 0.8 -> 0.6. That would bring back the round-1 legibility problem. |
| 2 | note | Round-1 note 4 is still open: the departures from the 1973 drawing are recorded only in the file header. | `corrections/v2-figures.md` (Chapter 4 Minor) | Orchestrator, optional: one Minor line (longer vectors; v + dv labelled at its head; E into the C.G.; c + v at 19 deg; 0.8-unit dm_e slice, hatched at 135 deg). |

## Verdict: pass

The round-1 must-fix is resolved: the expelled mass dm_e now reads as a hatched slice at 150 dpi and at final
size. There are no regressions. Lettering, vector geometry, caption and text claims, and house style are all
correct.
