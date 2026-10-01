# v2 audit: ch3/fig49 (round 2)

Sources checked: scan `figures/ch3/fig49.png`; redraw `figures/v2/ch3/fig49.tex` and its current PDF (271.8 x 148.5 pt
= 3.78 x 2.06 in, TeXGyreTermesX embedded, clean log), rendered at 400 dpi; inventory row `ch3-fig49`; caption and
citing text `chapters/ch3-sec6b.tex:119-149`; round-1 audit `audit/v2-ch3-fig49-round1.md` and the round-1 fix
report (no change); the Figure 44 redraw (family conventions).

Checks run:
- No changes since round 1: the file and PDF are dated 22:03, before the round-1 fixes to Figures 43-45, and the
  fixer reported the file untouched. There were no round-1 must-fix or should-fix items to verify.
- Areas recomputed from fig49.tex:21-25 with the shoelace formula. (a): the polygon (0, 3.648), (0.965, 3.21),
  (5.155, 1.31), (5.155, -0.76), (1.725, -0.76), (0.965, 0), (0, 0.965) has area 15.21 cm^2. (b): I + II + III =
  3.98 + 8.68 + 3.10 = 15.75 (the text has 15.76 from rounded parts). (b) is larger, as the caption says. The
  region dimensions are I 1.90 x 4.19, II 2.07 x 4.19 (tle 1.31 to te -0.76) and III 3.21 x 0.965, as in the text.
- Rendering: hatch directions as printed (I at 135 degrees, II and III at 45). The dashed guides are, in (a), the LE
  and chamfer extensions and, in (b), the top of III, the I/II line and the filled-in corner. I, II and III are
  curve tags (the text cites them as regions). The panel letters (a) and (b) use the panel style at lower right on
  one baseline (y -1.45). No overlaps; the III tag fits its region.
- Family: the same tube, \breakline amplitude 0.36, hatch, guide and centre-line conventions as Figure 44, and the
  same chamfer-extension construction as Figure 44's Aerobee-Hi cell. The longer centre-line overhang below the
  base (1.5 units) is there because this fin projects 0.76 below the base.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | The inventory lettering reads "circled (a) ; circled (b)". The redraw sets them in the house panel style "(a)", per the house rule for identifying panel letters. This is consistent and not a defect. | figures/v2/inventory.csv:115; fig49.tex:51 | none |

## Verdict: pass (no must-fix)
