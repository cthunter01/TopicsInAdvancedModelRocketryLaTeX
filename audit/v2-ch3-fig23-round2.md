# v2 audit: ch3/fig23 (round 2)

Sources checked:
- Scan: `figures/ch3/fig23.png`, with a 4x crop of the cylinder, S and the wake arrows.
- Redraw: `figures/v2/ch3/fig23.pdf` (rebuilt 22:39, after the tex). I rendered it whole at 300 dpi and the wake at 800 dpi, and checked `pdfinfo` and `pdffonts`.
- Sources: `figures/v2/ch3/fig23.tex`, `fig23.py`, `fig23-*.csv`, `fig23.calib.json`.
- Earlier rounds: the round-1 audit and the round-1 fix report.
- Inventory row `ch3-fig23`.
- Caption and citing text: `chapters/ch3-sec3c-sec4a.tex`:174-201, and the Fig 24 caption (:203-216).
- Kit: `tamrfig.sty` (curve tag, point, hatch, centerline, thin vec), unchanged since 21:33.

## Round-1 finding

Round 1 had one optional note (finding 1): the straight arrows in the separated layer sat too far out, and their comment was wrong. It is **resolved**.
- Placement:
  - fig23.tex:43 now draws them from (0.86, +-0.84) a to (1.16, +-0.71) a.
  - On the scan, using the drafter's calibration (centre (336.5, 138.5), a = 65.5 px), I measured:
    - upper arrow: (0.84, 0.84) a to (1.20, 0.70) a;
    - lower arrow: (0.87, -0.81) a to (1.22, -0.67) a.
  - Both now start beside S, as printed, and point downstream. The lower one is mirrored.
- Comment: fig23.tex:40-41 now says "the separated layer's outer flow, downstream from beside S (as printed)". "Reversed flow" is kept for the curved eddy arrows only.

## Regression check

- **Arrows over the hatch.** At 800 dpi the moved arrows keep their 2pt white casing. They clear:
  - the S dot and its tag (the tail is about 0.2 a from the dot);
  - the outer edge of the hatched band;
  - the curved eddy arrows.
- **Rest of the drawing.** Nothing else changed:
  - The CSVs are dated 22:21, before round 1.
  - My overlay matches round 1 (computed sketch, scan px, 95%): upper 8.0 / 5.0 / 3.0 / 3.0, lower 5.71 / 4.0 / 3.61 / 4.0, wake outline 8.6. These are reported, not judged.
- **Lettering.**
  - $U_\infty$ sits in a gap of the first streamline above the axis.
  - A, B, C and S are kit `curve tag`s inside the cylinder, with `point` dots on the surface, as in the scan (letters inside).
  - A, B and C are at 180, 90 and 0 deg, so the Fig 24 caption holds. S is at 43 deg.
- **Caption.** It holds: A to B accelerates, B to C has the adverse gradient, and separation is at S.
- **Size and fonts.** Page 4.78 x 1.97 in; fonts embedded.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | The round-1 note (arrow position and comment) is resolved. The arrows match the scan to within about 0.05 a, and nothing regressed. | fig23.tex:40-44 | None. |
| 2 | note | The computed streamlines and the hatched edge still sit up to 0.07 a outside the hand drawing over the cylinder. This is the approved computed-sketch method, and it is unchanged since round 1. | fig23.py | None. |

## Verdict: pass

No must-fix and no should-fix.
