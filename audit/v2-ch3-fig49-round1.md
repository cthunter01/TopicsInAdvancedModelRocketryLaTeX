# v2 audit: ch3/fig49 (round 1)

Sources checked: scan `figures/ch3/fig49.png` (both panels zoomed x4); redraw `figures/v2/ch3/fig49.tex` and its
current PDF (3.78 x 2.06 in, fonts embedded, clean log), rendered at 400 dpi; `build/v2/png/ch3-fig49-compare.png`;
inventory row `ch3-fig49`; caption and citing text `chapters/ch3-sec6b.tex:105-150` (region areas, sigma_F,
"Figure 49b ... standard method (Figure 49a)"); `corrections/ch3.md` D26 (Figure 48's labels against the text's
dimensions, no note); STYLE.md section 16; the Figure 44 redraw (shared tube, break, hatch and guide conventions).

Checks run:
- Region dimensions against the text: I is the right triangle (R, 3.21), (5.155, 1.31), (R, 1.31), legs 1.90 x
  4.19 (area 3.98); II the rectangle (R, 1.31)-(5.155, -0.76), 4.19 x 2.07 (8.68), the chamfered corner filled in
  with dashed edges; III the rectangle (0, 0)-(0.965, 3.21) (3.10). Root chord 3.21 + 0.76 = 3.97 and tip chord
  2.07, as the text's mean chord (3.97 + 2.07)/2 uses.
- Areas recomputed with the shoelace formula: (a) 15.21 cm^2 (LE extended to the axis at 3.648, chamfer extended
  to (0, 0.965)); (b) 15.75 (text 15.76 from rounded parts); exposed fin 12.37. (b) > (a), so the caption's
  "more conservative ... larger value of sigma_F" holds. (Extending the square trailing edge itself to the axis
  would give 16.70 and break the caption: the chamfer extension, as printed, is the consistent reading.)
- Overlay per panel (PDF at 115.45 dpi, registered by cross-correlation): fin outlines on the scan's ink (median
  0 px; 95th percentile 3-4 px including the shortened tube and the moved letters). The tube is drawn 5.8 cm
  long instead of the printed 7.4: a layout choice, nothing hangs on it.
- Hatching as printed: (b) III and II at 45 degrees, I at 135 (the herringbone along the dashed I/II line);
  (a) one 45-degree hatch. Dashed (guide) lines: (a) the LE and chamfer extensions inside the tube; (b) the top
  of III, the I/II line, the filled-in corner. Matches the scan.
- Letters: (a), (b) in the panel style at the lower right on one baseline (y -1.45); I, II, III, which the text
  cites as regions, in the house curve tag, at I's centroid and the middles of II and III. The III tag (about
  13 pt) fits its 17.8 pt wide region with about 0.8 mm to the centre line and to the tube wall.
- Family: same tube, \breakline amplitude 0.36, hatch, guide and centre-line conventions as Figure 44, and the
  same chamfer-extension construction as Figure 44's Aerobee cell.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | The fin is drawn to the text's dimensions (3.21, 1.90, 2.07, 4.19, 0.965) rather than Figure 48's labels (3.30, 1.91, 0.68 chamfer), as the 1973 Figure 49 itself is (D26, no note). Consistent with the region areas the text computes. | fig49.tex:5-10 | none |
| 2 | note | The III tag is tight in its region (about 0.8 mm each side) but clear of the centre line and the wall at final size. | fig49.tex:48 | none |

## Verdict: pass (no must-fix)
