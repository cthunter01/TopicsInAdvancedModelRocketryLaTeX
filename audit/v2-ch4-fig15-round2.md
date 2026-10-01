# v2 audit: ch4/fig15 (round 2)

Sources checked:
- Scan `figures/ch4/fig15.png`.
- Redraw `figures/v2/ch4/fig15.pdf` (rebuilt with `make fig F=ch4/fig15`; clean log, 5.05 x 2.66 in). I looked at
  300 and 600 dpi renders, 600 dpi crops of panels (a) and (b), and `build/v2/png/ch4-fig15-compare.png`. All
  fonts are embedded, with no opacity operators or soft masks.
- Sources `fig15.tex` (as changed by the round-1 fix), `fig15.py`, `fig15.csv`, `fig15-pos.csv` and
  `fig15.calib.json`.
- Inventory row `ch4-fig15`, and the caption and citing text in `chapters/ch4-sec3.tex`:225-252.
- Round-1 audit `audit/v2-ch4-fig15-round1.md` and the fixer's report.

## Independent checks

- **Data.** I copied `fig15.py` to scratch and ran it there. It reproduces `fig15.csv` and `fig15-pos.csv` byte for
  byte: 16.57 px/m; (b) at (379.19, 269.82) px, theta = 74.003 deg, s = 340.3 px.
- **Overlay (my run).** I split the curve into the drawn pieces and ran `digitize.py overlay`:
  - s 80-222: mean 4.75 px, 95% 11.29 px (1.91 mm);
  - s 472-545: mean 10.42 px, 95% 15.67 px (2.65 mm).
  - These are the round-1 numbers. The cause is the same: the 1973 freehand arc passes through neither C.G.
- **Forces (rule 4).** Nothing changed here since round 1.
  - $g\sin\theta_o$ and $g\sin\theta$ are the true normal components. The dashed closures (`guide`, the kit's
    construction line) run parallel to the axis.
  - $F\cos\theta$ is vertical from F's tail.
  - The caption's comparisons hold: $g\sin\theta$ 96 > 50, and $F\cos\theta$ 14 < 45.
- **Lettering.** Everything is present:
  - (a): $\theta_o$, $g$, $g\sin\theta_o$, $v$, $F$, $F\cos\theta_o$, (a);
  - (b): $F$, $F\cos\theta$, $g$, $g\sin\theta$, $\theta$, $v$, (b).
  - The o subscripts are the letter o, with no vector arrows, as printed.

## Round-1 findings

- **1 (should-fix, θ_o and θ arcs had two heads): resolved.**
  - Both `\anglemark` calls (:67, :83) now pass `arc={angle arc single}`.
  - At 600 dpi, each arc starts on the vertical: g's own line in (a), the `guide` reference in (b). The single head
    lands on the body outline, on the flight direction, through the existing trim.
  - This is the form Fig 2 uses for the same angle, so the family is consistent.
  - The labels θ_o and θ sit between the two rays, just outside the arcs.
  - No other part of the drawing moved.
- **2 (should-fix, overlay mismatch not logged; inventory method/data out of date): still open.** It was
  correctly declined by the fixer, because both files lie outside the figure's writable set. `git diff` shows no
  Chapter 4 Fig 15 entry in `corrections/v2-figures.md` yet. STYLE s16 requires an entry for any curve over the
  3 px tolerance, so the orchestrator must add it before the chapter gate (finding 1).
- **3 (note, F cos θ in (b) mostly arrowhead): no change, which is acceptable.** It is still recognisable at final
  size, and its smallness is the caption's point.
- **4 and 5 (notes): no change needed.**

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | Open orchestrator action, carried from round-1 finding 2. STYLE s16 requires the overlay mismatch to be logged, and it still is not: 95% at 11.3 px (1.9 mm) and 15.7 px (2.7 mm) against 3 px. The inventory row still lists the method as "draw" and the data as "n/a". Neither is a change to the figure's files. | `corrections/v2-figures.md` (Chapter 4 Minor); `figures/v2/inventory.csv` row `ch4-fig15` | Orchestrator: add the Minor line the fixer drafted. The path is computed by eqs. (125)-(131), (106)-(115) for Fig 14 (c)'s model with a constant 7 N and constant mass, scaled so both C.G.s lie on it with tangent axes; it lies 11.3 px and 15.7 px from the 1973 freehand arc, which passes through neither C.G.; the forces are resolved per rule 4. Then mark the inventory row as computed (`fig15.py`). |

## Verdict: pass

The round-1 should-fix on the angle arcs is resolved, and θ now reads the same way as in Fig 2. There are no
regressions: the data reproduce, the forces are consistent, every label is kept and the build is clean. The one
open item is the log and inventory entry, which belongs to the orchestrator.
