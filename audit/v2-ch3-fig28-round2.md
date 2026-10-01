# v2 audit: ch3/fig28 (round 2)

Sources checked:
- Scan `figures/ch3/fig28.png`: 4x crop of (a) at the nose and ordinate, 5x crop of the (b) lobes. Column reads of the (b) suction lobe and the (a) minimum used the drafter's calibration.
- Redraw `figures/v2/ch3/fig28.pdf` (22:22:32, after the tex; the CSVs are from 22:21). Renders: whole at 300 dpi, (a) at the nose and (b) at the nose at 700 dpi. Also `pdfinfo` and `pdffonts`.
- Sources `figures/v2/ch3/fig28.tex`, `fig28.py` (the round-1 fix edited only its docstring; checked that it parses with `ast`), `fig28-*.csv` and `fig28.calib.json`.
- The round-1 audit and fix reports.
- Inventory row `ch3-fig28`.
- Caption and citing text `chapters/ch3-sec4b.tex`:95-119.
- `corrections/v2-figures.md`.

## Round-1 finding

**Should-fix 1** asked the orchestrator to log the computed-versus-drawn difference for the gate. The fixer could not write that entry, so the item is still open with the orchestrator.

- **Fixer's part (done).** The fixer declined the corrections entry, because `corrections/` is outside the figure's files, and passed it on as a doubt. Within its own scope it corrected the false claim in fig28.py:17-20. The docstring now says the difference is "a Chapter 3 gate item for corrections/v2-figures.md".
- **Docstring figures.** I re-measured both numbers on the scan and both are right.
  - (a): the drawn minimum is at row 170 against the 110 px per unit ordinate, so -0.39 at X = 1.04 R ("about -0.39 near X = 1.1 R").
  - (b): the drawn suction lobe reaches 1.61 R from the axis at X = 0.65-0.84 R. The computed lobe reaches 1.33 R (fig28-envneg.csv, w max 1.327).
- **Orchestrator's part (still open).** `corrections/v2-figures.md` still has no Fig 28 entry: a grep for Fig 28, Rankine and half-body found none. This is not something the figure's files can fix.

## Re-check of the computation

I rederived the computation independently from the Stokes stream function. The setup is m = R^2/4, nose at X = 0, u = 1 + m x/r^3, v = m w/r^3.

| Check | Result |
|---|---|
| Body stream function | psi = m to 1.1e-16 |
| C_p minimum | -1/3 at X = 0.789 R, w = 0.8165 R |
| C_p = 0 | X = 0.296 R |
| C_p at X = 1, 2, 3, 9 R | -0.3125, -0.139, -0.066, -0.0068 |
| fig28-cp.csv against exact C_p at every body point | within 1.5e-5 |
| Streamlines | start at 0.35, 0.70, 1.05, 1.41 R; end at 1.059, 1.220, 1.449, 1.720 R |
| Exact sqrt(w0^2 + R^2) | 1.059, 1.221, 1.450, 1.720 R |

## Regression check

- **Drawing unchanged.** The tex is unchanged since round 1, so the PDF and drawing are identical. On the rendered PDF:
  - The ordinate title $p/((\rho/2)u_o^2)$ uses the letter o.
  - Ticks 0.2-1.0 are in ink2.
  - $u_o$ sits over a `vec` on the axis, and the dash-dot axis starts after the arrowhead.
  - (b): dashed positive envelope, solid suction lobe, dashed tail. The strokes are normal to the surface.
  - Panel letters are at the lower right of each drawing.
- **Overlaps.** None found at 700 dpi.
  - Downstream, the innermost streamline runs 0.06 R (about 0.4 mm) outside the body contour. The 1973 art merges the two lines there too.
- **Text holds.**
  - (a): the streamlines are convex toward the body at the stagnation point and concave aft.
  - (b): positive pressure ahead, suction on the shoulder, in balance.
- **Size and fonts.** 5.14 x 2.94 in; fonts embedded.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | **Orchestrator action outstanding (not the figure's files).** The round-1 should-fix was correctly declined in the figure's files and passed on as a doubt. Still needed: a Chapter 3 gate item in `corrections/v2-figures.md`, which has none yet. The item should cover four facts. (1) Fig 28 is computed from the axisymmetric Rankine half-body, an outside formula the pilot gate did not name. (2) In (a), C_p min is -1/3 at 0.79 R against a drawn -0.39 near 1.0-1.1 R, with faster recovery (overlay 95% 9 px). (3) The (b) suction lobe reaches 1.33 R against 1.61 R drawn. (4) Fig 27 uses the same body. If the gate keeps the formula, About This Edition should name it. | corrections/v2-figures.md (gate section) | Orchestrator adds the entry; no change to the figure. |
| 2 | note | The docstring now matches the repository. It no longer says the difference is already recorded, and its numbers (-0.39 near 1.1 R; 1.33 R against about 1.6 R) agree with my scan reads. | fig28.py:16-20 | None. |
| 3 | note | The computed data are exact (C_p within 1.5e-5; streamline asymptotes to 1e-3 R), and nothing regressed. | fig28-*.csv, fig28.tex | None. |

## Verdict: pass

There is no must-fix item. The round-1 should-fix is closed for the figure; only the orchestrator's corrections entry (finding 1) remains open.
