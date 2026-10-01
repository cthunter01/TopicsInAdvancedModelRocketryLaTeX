# v2 audit: ch3/fig44 (round 1)

Sources checked: scan `figures/ch3/fig44.png` (each cell zoomed x4, the cell names x7-8 and measured glyph by
glyph); redraw `figures/v2/ch3/fig44.tex` and its current PDF (4.69 x 3.37 in, fonts embedded, clean log),
rendered at 400 dpi; `build/v2/png/ch3-fig44-compare.png`; inventory row `ch3-fig44`; caption and citing text
`chapters/ch3-sec6a.tex:113-131` (the gross-area rule and the Python-2 rule); every "Aerobee-Hi" in
`chapters/` (ch3-sec5a.tex:202-208, ch3-sec5b.tex:77-93, 164, ch3-intro-sec2a.tex:22); the Figure 41 redraw and
its audit (`figures/v2/ch3/fig41.tex`, `audit/v2-ch3-fig41-round1.md`); STYLE.md sections 8, 14, 16; kit
`\breakline`, `hatch`, `guide`.

Checks run:
- Overlay per cell (PDF at 115.45 dpi, 1 unit = 1 scan pixel, registered by cross-correlation): outlines and
  hatching median 0 px, 95th percentile 2.0, 1.4, 2.0, 1.8, 1.0, 2.1 px for Delta, Rectangular, Swept,
  Trapezoidal, Aerobee-HI, Python-2. All six fins sit on the scan's ink.
- Gross-area construction against the text (extend the LE and TE to the body axis): Delta LE to (0, 84.55), TE
  along the base; Rectangular LE horizontal; Swept LE and TE parallel, both meeting the axis 8.04 higher; Trapezoidal
  LE to 79.04 and TE to -3.83 (below the base, hatched there as the scan shows); Aerobee-HI LE to 85.59 and the
  45-degree root chamfer to (0, 18.5) (as the scan, and as Figure 49(a)); Python-2: lines from the root chord's
  ends parallel to the base (the LE one dashed at 63, the TE one along the base), the fin running aft past the
  base and broken off (\breakline, hatch bounded by the same zigzag). All slopes recomputed: consistent.
- Lettering: six names present. The final glyph of "Aerobee-H?" was measured: a dotless stroke 14 px tall,
  the same height as H; this letterer's i in "Trapezoidal" in the same figure is likewise a dotless stroke at
  ascender height (13 px, the same as d and l, against x-height 10 px).
- Layout: booktabs-weight rules (top, mid, bottom; no vertical rules), as STYLE section 16 directs for tables in
  figures and as Figure 45; names centred under the drawings on one baseline per row; clearances between the
  rules and the drawings about 2.6 mm. Flat line art, ink and ink2 only.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | should-fix | "Aerobee-HI" does not follow from the print: the last glyph is a dotless cap-height stroke, which is exactly how this hand writes i (the i of "Trapezoidal" in the same figure), so the case is not shown. Where a hand glyph does not show its case, the house sets the listed/text form (STYLE s14); the text writes Aerobee-Hi everywhere, and the Figure 41 redraw, after the same check, letters "Aerobee-Hi" (audit round 1, finding 1). As drawn, the same rocket is spelled two ways in one chapter's redraws. | fig44.tex:4, 62, 67 | Letter "Aerobee-Hi" and change the comment; the inventory row's lettering note can be updated at the gate. |
| 2 | note | Local helpers under new names: \tube, \cellname and \breakpath (the \breakline zigzag as a path, to bound a fill). \breakpath repeats the kit's zigzag constants with the amplitude 0.36 hard-coded, so it would drift if the kit's \breakline changed. | fig44.tex:20-31 | Kit candidate: a path form of \breakline that reads `break amplitude` (style suggestion; no change needed here). |
| 3 | note | The 1973 art draws the tube's top as a cut cylinder (an S-shaped end); the redraw uses the house zigzag \breakline, as the family brief and STYLE section 16 direct. Names are centred rather than at the cells' lower left: table style. | fig44.tex:20-23, 31 | none |
| 4 | note | Trapezoidal: the dashed TE extension meets the axis 3.83 below the base and the sliver below the base line is hatched, as printed; geometrically right for the rule. | fig44.tex:55-59 | none |

## Verdict: pass (no must-fix)
