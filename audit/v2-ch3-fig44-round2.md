# v2 audit: ch3/fig44 (round 2)

Sources checked: scan `figures/ch3/fig44.png`; redraw `figures/v2/ch3/fig44.tex` and its current PDF (337.7 x 242.9 pt
= 4.69 x 3.37 in, TeXGyreTermesX embedded, clean log), rendered at 400 dpi and at 115.45 dpi without
anti-aliasing for the overlay; inventory row `ch3-fig44`; caption and citing text `chapters/ch3-sec6a.tex:116-132`;
every "Aerobee" in `figures/v2/ch3/*.tex` (fig41.tex:28 and fig44.tex:69); round-1 audit
`audit/v2-ch3-fig44-round1.md` and the round-1 fix report; the Figure 49 redraw (family conventions).

Checks run:
- Round-1 should-fix 1 (Aerobee-HI): resolved. The cell is lettered "Aerobee-Hi" (fig44.tex:69), centred on the
  row-2 baseline with Trapezoidal and Python-2. The scope comment (line 64) and the header (lines 4-6) give the
  reason. The two Chapter 3 redraws now spell the rocket the same way (fig41.tex:28 "Stine\\ Aerobee-Hi\\
  experiment"), as do the text and the caption.
- Round-1 note 2 (\breakpath hard-codes 0.36): left in place and reported as a style suggestion, which is
  appropriate since the fix belongs in the kit. The local helpers keep their new names (\tube, \cellname,
  \breakpath). Nothing in the kit is redefined.
- Regression check, per-cell overlay. Ink-colour pixels of each cell's drawing (names and rules excluded) were
  registered on the scan separately. Median / 95th percentile / max, px: Delta 0.0 / 2.0 / 4.1, Rectangular
  0.0 / 2.0 / 5.0, Swept 0.0 / 1.4 / 5.0, Trapezoidal 0.0 / 2.2 / 6.0, Aerobee-Hi 0.0 / 2.0 / 5.0, Python-2
  0.0 / 2.8 / 6.0. Between 97% and 99% of the ink in each cell is within 3 px. The maxima are the house zigzag
  breaks, which replace the 1973 cut-cylinder ends by design. The geometry is unchanged from round 1.
- The gross-area constructions are unchanged and still match the text's rule (LE and TE extended to the axis;
  Python-2 lines parallel to the base). The booktabs rules, hatch, guide and break match Figures 45 and 49.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | The inventory row `ch3-fig44` still lists the lettering as "Aerobee-HI (as lettered ...)". The fixer reported this as a doubt and did not edit the inventory, as the constraints require. Update it at the gate so that the inventory matches the redraw and Figure 41. | figures/v2/inventory.csv:110 | gate: inventory lettering to "Aerobee-Hi" |
| 2 | note | The local \breakpath still repeats the kit's zigzag constants with amplitude 0.36, which is pending the kit suggestion from round 1. It matches \breakline exactly today: the hatch is bounded by the drawn zigzag in the Python-2 cell. | fig44.tex:26-31 | none here |

## Verdict: pass (no must-fix)
