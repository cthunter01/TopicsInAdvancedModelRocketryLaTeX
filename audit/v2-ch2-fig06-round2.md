# v2 audit: ch2/fig06 (round 2)

Sources checked: figures/ch2/fig06.png (scan; pixel zooms 4-16x with a grid at the origin and the tail);
figures/v2/ch2/fig06.pdf (current: written 0.9 s after the .tex; 358.4 x 246.9 pt = 4.98 x 3.43 in;
TeXGyreTermesX, NewTXMI, NewTXMI7 all Type 1 embedded); renders at 113.6 and 400 dpi;
build/v2/png/ch2-fig06-compare.png; figures/v2/ch2/fig06.tex, diffed against figures/v2/ch2/fig01.tex;
figures/v2/inventory.csv row ch2-fig06; caption chapters/ch2-intro-sec1.tex:415-419; citing text
ch2-intro-sec1.tex:377-386; STYLE.md sections 13 and 16; corrections/v2-figures.md (standing rule 2: lowercase
f, no O); round 1 audit (audit/v2-ch2-fig06-round1.md) and the round-1 fix notes; this round's Fig 1 audit
(audit/v2-ch2-fig01-round2.md), whose geometry checks carry over because the code is shared.

Round-1 findings:
- 1 (F, Z not visible from O to the nose): **resolved.** The centre line runs from the nose tip through O to
  beyond the tail (line 118, after the body). The axis lettered "F, Z" now reads continuously from O to its
  arrow, which supports the text's "Z always coincides with F".
- 2 (\rad 0.062): **resolved.** `\rad` = 0.088 (line 53), the same as Fig 1.
- 3 (occlusion not recorded): **resolved.** Header lines 8-10 say this scan also draws the f-F face over the
  lower half of the forward body, and that the redraw follows Fig 1 (standing rule 4).
- Note 4 (a possible tiny arrowhead on the scan's OY): unchanged. Both OX and OY are drawn without heads, as
  accepted.

Checks of the round-1 changes:
- The diff against fig01.tex shows only the header, the lettering block (the labels; `de line` solid, 0.6 pt),
  two comments, and Fig 1's O label (absent here, as standing rule 2 requires). The stubs, the rad, the centre
  line and the arc trim are Fig 1's.
- The stubs over the body are OA, OX (= Od) and OD: the near-half lines, recomputed in Fig 1's audit (radial .
  c = +0.684, +0.684, +0.549; all the others are negative). OX is solid here, so the dash phase has no effect;
  at 400 dpi the three solid stubs run on into their lines past the upper silhouette.
- Lettering against the scan and the inventory: A, B, C, D, E, "F, Z", X, Y, lowercase f; A-X $\alpha_Y$, X-D
  $\alpha_F$, B-Y $\alpha_X$, Y-E $\alpha_F$, C-f $\alpha_X$, f-F $\alpha_Y$; no O. All correct. The caption
  (X, Y, Z follow yaw and pitch, zero roll) and the text ($\alpha_X = \alpha_D$, $\alpha_Y = \alpha_E$, Z along
  F) still hold.
- Legibility at 400 dpi: "F, Z" is clear of the arrow and the nose; X sits clear of the A-X-D chord; Y, B and E
  are clear of each other; the $\alpha_Y$ arc ends on the nose silhouette. The width is 4.98 in (at most
  6.5 in).

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | should-fix | As in Fig 1 (round 2, finding 1), the tail (tail ring and fins) sits about 15 scan px further aft than the scan's. In this scan the tail-ring centre at (339.4, 323.8) is 92-94 px from the origin circle at (278.5, 254); the redraw has 1.3 x 0.8325 x 100 = 108 px. The aft body is about 16% long, and the header's "the rocket is Figure 1's" carries the claim of the scan's proportions. | fig06.tex:53 (`\def\stail{-1.3}`) | Same value as Fig 1 after its fix (`\stail` about -1.12), keeping the two files identical apart from lettering. Or, if Fig 1 keeps -1.3, the same correction to the record. |
| 2 | note | As in Fig 1, OA, OX and OD now stop at the body's surface, about 0.7 mm short of the C.G. mark, where the scan runs them into the origin. This is consistent hidden-line treatment, and the fix notes record it. | fig06.tex:119-126 | None (owner's call at the gate). |
| 3 | note | As in Fig 1, the scan's OY end may carry a tiny arrowhead (round 1, note 4). It is still unresolved, and leaving both OX and OY without heads is consistent. | fig06.tex:93-94 | None. |

## Verdict: pass

No must-fix. One should-fix (the tail station, shared with Fig 1) and two notes.
