# v2 audit: ch4/fig02 (round 1)

Sources checked:
- Scan `figures/ch4/fig02.png`, with a 4x crop of the velocity triangle.
- Redraw `figures/v2/ch4/fig02.pdf` (`make fig F=ch4/fig02`; clean log, 3.57 x 4.75 in): 300 dpi render, an 800 dpi
  crop of the triangle and rocket, and `build/v2/png/ch4-fig02-compare.png`. I also checked `pdffonts` (all
  embedded) and looked for opacity operators (none).
- Sources `fig02.tex`, `fig02.py`, `fig02.csv`, `fig02-end.csv` and `fig02.calib.json`.
- Inventory row `ch4-fig02`.
- Text:
  - `chapters/ch4-intro-sec1.tex`:330-374: the coordinate frame, eqs. (12)-(15), and θ as "the angle between the
    tangent to the trajectory and the y-axis".
  - `chapters/ch4-sec3.tex`:76-118: eqs. (106)-(115) and (125)-(131).
- STYLE.md sections 15 and 16; standing rule 4 in `corrections/v2-figures.md`.

Checks made:
- **Data reproduce.** I reran `fig02.py`'s `nonvertical()` in scratch, writing nothing to the repo. It reproduces
  `fig02.csv` byte for byte (259 rows). The end point is $t$ = 5.14 s, x = 160.8 m, y = 276.0 m, θ = 50.01 deg, as in
  `fig02-end.csv`.
- **Equations.**
  - The rod phase is (125)-(131) at θ_o = 22 deg for 1 m.
  - Free flight is (106)-(115) with v from (112).
  - The B4 thrust and mass come from `trajectory.py`, with $m_o$ = 0.040 kg and k = 0.92e-4 (Table 2's model).
  - dt = 0.001 s, as the text recommends for this method (ch4-sec3.tex:121-124).
- **Overlay (my run).** `digitize.py overlay fig02.calib.json`: residual 0.00 px; 259 points, mean 0.15 px, 95%
  1.00 px (0.17 mm), max 1.00 px. That is within tolerance.
- **Lettering.** Everything the scan and the inventory list is present:
  - the axis labels $y$ and $x$ (lowercase, italic) and "Trajectory";
  - "Launch point" with "$x = y = 0$" below it (digit 0, STYLE s15) and the launch dot;
  - $\theta$, $v$, $\dot y = v_y$ and $\dot x = v_x$ (lowercase v, as STYLE s15 says for the lettered V_y);
  - the rocket icon on the trajectory.
  - No vector arrows, as printed.
- **Geometry (rule 4).**
  - The axes are at right angles.
  - The rocket lies along the computed tangent at the end of the curve.
  - $v$ continues that tangent from P, just ahead of the nose, as in 1973.
  - $\dot x$ is horizontal and $\dot y$ vertical, head to tail, so cos θ = ẏ/v and sin θ = ẋ/v hold as drawn
    (eqs. (14), (15)).
  - θ runs from a vertical reference line (`guide`) through P to $v$, with a single head on $v$, as printed.
- **Caption.** The range x is horizontal from the launch point and the altitude y vertical. True.
- **House style.**
  - `tamr sketch` axes: the y label is upright above its arrow and the x label sits after its arrow.
  - The trajectory is s1 and the vectors `vec`. The reference line is `guide`, and the small icon is `thin line`.
  - Text is in ink. Nothing is filled or transparent, and no kit name is redefined.
  - Legible at final size.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | The inventory row is out of date. It still says method "sketch" and data "trajectory is a freehand arc; no numbers". The redraw computes the curve by the book's nonvertical method, with Table 2's B4 model at a launch angle matched to the scan (22 deg, not the 30 deg of Figs 10-14; the file says 30 deg cannot be matched). This follows the owner's rule that unlabelled sketches take their shape from the governing equation, and the overlay passes (95% 1.0 px). | `figures/v2/inventory.csv` row `ch4-fig02` | Orchestrator: update the method and data cells. Optionally add a Chapter 4 Minor line: "Ch4 Fig 2: trajectory by eqs. (125)-(131), (106)-(115), Table 2's B4 model at θ_o = 22 deg (matched); overlay 95% 1.0 px." |
| 2 | note | θ here is `angle arc single` with its label in the arc's gap. Fig 15 marks the same angle (from the vertical to the flight direction) with double-headed arcs. Fig 2 is the form to keep, because STYLE s16 gives the single head to an angle measured from a reference line, and 1973 prints one head. | `fig02.tex`:45 | None here. The change belongs to Fig 15 (its finding 1). |

## Verdict: pass

No must-fix and no should-fix. The curve is computed by the book's method and sits within 1 px of the 1973 arc.
Every printed label is kept, and the velocity triangle is now consistent with eqs. (14)-(15) on right-angled axes.
