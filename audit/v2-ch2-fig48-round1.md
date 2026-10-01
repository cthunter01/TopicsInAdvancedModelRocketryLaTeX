# v2 audit: ch2/fig48 (round 1)

Sources checked: scan `figures/ch2/fig48.png` (zoomed 2-6x; pixel profiles of the tube walls, the end view and
the scale bar); redraw `figures/v2/ch2/fig48.tex` / `.pdf` (4.64 x 7.10 in, fonts embedded), rendered at 400 dpi,
and `build/v2/png/ch2-fig48{,-compare}.png`; inventory row `ch2-fig48`; caption and citing text
`chapters/ch2-sec6.tex:46-67, 105`; `corrections/v2-figures.md` standing rule 4; STYLE.md section 16.

Geometry checked against the lettered dimensions (coordinates are centimetres at 1:3):
- Overall 37.25 = nose 8.27 + tube 28.98. The shoulder line is 1.27 below the nose base. The casing is
  2.10 x 7.00, flush with the tail. The tube radius is 1.24 (OD 2.48). Fin root chord 5.08, tip chord 2.54
  (trailing edge square at the tail), span 5.08 (fin tip at x = 6.32), thickness 0.16 in the end view and
  edge-on. All are correct in the .tex (lines 40-73).
- Scale bar: 8 units = 8 cm at the drawing's 1:3, so it is true (rule 4). The scan's bar measures about
  15.0 px/cm against the drawing's 14.17 px/cm, which confirms the 6% error. The two-row checker matches the
  scan: top row black at 0-2 and 4-6, bottom row black at 2-4 and 6-8.
- C.G. 24.83 and C.P. 32.42 from the tip. On the scan they measure 24.8 and 32.4 (tip at row 30, tail at row
  558). They are 7.59 apart, or 3.06 calibers, which agrees with the text's "static stability margin of three
  calibers" (ch2-sec6.tex:105).
- End view: on the scan only the LEFT fin is too long (its thick ink runs to x = 75, about 7.3 cm from the
  body). The right, top and bottom fins measure 5.0-5.1 cm, so the drafter's note is correct. The scan's
  dashed inner circle is the casing (ratio about 0.83 of the body's), as drawn. The end view sits 8.68 below
  the tail on the scan, 8.75 in the redraw.
- Leader attachment points (nose at 6.8 from the tip, tube at 21.35 above the tail, casing top corner, C.G.,
  C.P.) match the scan.
- All lettering in the inventory is present and correct: Estes BNC-50X, Estes BT-50, C.G., C.P.,
  Flight Systems 21 x 70-mm casing, the 13 dimension values, Scale (cm), 0 2 4 6 8, DTV-1 underlined.
  Vertical dimensions read bottom to top as printed.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | Drawn to scale, the tube wall (0.035 cm, 0.12 mm at 1:3) is thinner than a line, so the 2.48 and 2.41 arrows in the end view point at the same visible line, and the ID's hidden line along the tube merges with the outline. The scan has the same near-merge: three arrows on one thick line on each side, and a wobbly double line for the walls. This is consistent with rule 4. | fig48.tex:105-109; header lines 5, 15-17 | None needed. If the owner wants 2.41 to be readable, exaggerate the wall in the end view only (a conventional drafting liberty) and say so in the header. |
| 2 | note | The callout is split as "Flight Systems / 21 x 70-mm casing". The 1973 art splits it as "Flight Systems 21 x 70- / mm casing". The wording is unchanged and the new break avoids splitting "70-mm". | fig48.tex:116-117 | None. |
| 3 | note | The edge-on fin in the side view is drawn at 0.4pt. Fig 51 draws its edge-on fins at the outline weight (0.6pt). This is a minor difference within the family; both are legible. | fig48.tex:61 vs fig51.tex:23 | Optional: use one weight for edge-on fins across Figs 48 and 51. |
| 4 | note | The figure is 7.10 in tall (the v1 inclusion was about 7.2 in). With the three-line caption it fits the 9 in text block, but it will float to a page of its own. | fig48.pdf | None. |
| 5 | note | The local `hidden` style (0.45pt, 2.6/1.6 dash) is identical to the ones in Figs 41 and 42. Fig 45 uses 0.5pt with a 3/2 dash. The local `dim arrow` and `\dimout` (outside arrows for a short dimension) are also used here. | fig48.tex:29-36 | Style suggestion: add `hidden` and an outside-arrow dimension helper to tamrfig.sty so all figures share one. |

## Verdict: pass (no must-fix)
