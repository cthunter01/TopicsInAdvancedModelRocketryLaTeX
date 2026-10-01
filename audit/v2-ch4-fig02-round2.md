# v2 audit: ch4/fig02 (round 2)

Sources checked:
- Scan `figures/ch4/fig02.png`.
- Redraw `figures/v2/ch4/fig02.pdf` (rebuilt with `make fig F=ch4/fig02`; clean log, 3.57 x 4.75 in). I looked at
  300 and 600 dpi renders, 600 dpi crops of the velocity triangle and the launch point, and
  `build/v2/png/ch4-fig02-compare.png`. All fonts are embedded, with no opacity operators or soft masks.
- Sources `fig02.tex`, `fig02.py`, `fig02.csv`, `fig02-end.csv` and `fig02.calib.json`. None has changed since
  round 1.
- Inventory row `ch4-fig02`, and the caption and citing text in `chapters/ch4-intro-sec1.tex`:345-376.
- Round-1 audit `audit/v2-ch4-fig02-round1.md` and the fixer's report.

## Independent checks

- **Data.** I reran `nonvertical()` from `fig02.py` in scratch, writing nothing to the repository. It reproduces
  `fig02.csv` and `fig02-end.csv` byte for byte. The end point is t = 5.14 s, x = 160.8 m, y = 276.0 m and
  theta = 50.01 deg.
- **Method.** Eqs. (125)-(131) on the rod, then (106)-(115), dt = 0.001 s, with Table 2's B4 model at theta_o =
  22 deg (matched to the scan).
- **Overlay (my run).** Residual 0.00 px. 259 points: mean 0.15 px, 95% within 1.00 px (0.17 mm), max 1.00 px.
  That is within tolerance.
- **Lettering.** Everything is present:
  - $y$, $x$ and "Trajectory";
  - "Launch point" over "$x = y = 0$" (digit 0), with the launch dot;
  - $\theta$, $v$, $\dot y = v_y$ and $\dot x = v_x$, with no vector arrows, as printed;
  - the rocket icon.
- **Geometry (rule 4).**
  - The axes are at right angles. $\dot x$ is horizontal and $\dot y$ vertical, head to tail, closing on $v$ along
    the computed tangent.
  - θ runs from the vertical reference line (`guide`, a construction line) to $v$, with one head on $v$. This is
    the form of eqs. (14)-(15) and the text's definition (:351-352).
- **Caption.** x is the horizontal range and y the vertical altitude from the launch point. True.
- **House and family consistency.**
  - The path is s1 at 1pt, as in Figs 3 and 15.
  - θ uses `angle arc single`. Fig 15 now uses the same style, so the family is consistent.
  - Text is in ink, and no kit name is redefined.

## Round-1 findings

- **1 (note, inventory row out of date): still open, for the orchestrator.** The row still says method "sketch"
  and data "trajectory is a freehand arc; no numbers".
- **2 (note, θ arc style): resolved in Fig 15**, which now matches this figure.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | The inventory row still describes the curve as a freehand sketch. The redraw computes it: `fig02.py`, eqs. (125)-(131) then (106)-(115), Table 2's B4 model, theta_o = 22 deg matched to the scan, overlay 95% 1.0 px. | `figures/v2/inventory.csv` row `ch4-fig02` | Orchestrator: update the method and data cells. Optionally log the matched 22 deg in a Chapter 4 Minor line. |

## Verdict: pass

The figure is unchanged since round 1 and still builds clean against the current kit. Its curve reproduces from
the book's equations and lies within 1 px of the 1973 arc. Every printed label is kept, the velocity triangle is
consistent on right-angled axes, and θ now matches Fig 15. The only open item is the inventory update, which is
outside the figure's files.
