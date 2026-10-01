# v2 audit: ch2/fig43 (round 2)

Sources checked: the scan `figures/ch2/fig43.png` (zoomed at the clamp of (a), the rocket of (a) and the tail
T of (b)); the redraw `figures/v2/ch2/fig43.tex` / `.pdf` (PDF newer than the source; rendered at 400 and
800 dpi, with details at 1000, 1600 and 3200 dpi; `build/v2/png/ch2-fig43-compare.png`; an SVG export to
identify individual strokes); inventory row `ch2-fig43`; caption and citing text `chapters/ch2-sec5.tex:48-66,
83, 113, 135-150`; `backmatter/figure-credits.tex:114`; STYLE.md section 16 (type: italic panel letters at
the lower right of a drawing's panel); `corrections/v2-figures.md` standing rule 2; `figures/v2/tamrfig.sty`;
`figures/v2/ch2/fig50.tex` (the same local `circled` style); the round 1 report and the fixer's response.

Size and fonts: 328.0 x 429.0 pt (4.56 x 5.96 in), within 6.5 in, the same as round 1. One font,
TeXGyreTermesX-Italic, embedded.

Round 1 findings:
- Should-fix 1 (the separating rule half covered by panel (b)'s beam) is **resolved**. The rule is now the
  last command in the picture (`fig43.tex:113-114`), after the panel (b) scope. At 800 dpi the rule's six
  columns (1873-1878) are dark over 4764-4766 of the page's 4767 rows. Before the fix the right three
  columns lost about 465 rows. Where the (b) beam meets the rule, the beam's top and front edges now end
  cleanly on the rule. Nothing else moved. The (b) beam is still clipped at the rule's centre,
  `\apparatus{-134}` (line 101), and the rule covers the cut end.
- Notes 2-5 needed no action. Note 4 (no screw shank between the pad and the arm) was optional and was left
  as it was, which is fine. Note 5 (promote `circled` to the style) is repeated under style suggestions.

Re-checked in this round:
- Content: each panel has the beam, the C-clamp, the knurled screw with its threads, the swivel pad, the
  upper T, the wire and the rocket. Neither panel has any lettering except its circled letter, as printed.
  Circled lowercase italic *a*, *b* are kept (standing rule 2), at the lower right of each panel on one
  baseline (y = -644).
- Text: the wire hangs from the centre of the upper T's crossbar (x = -30 ... 44, wire at x = 7). In (a)
  the rocket is horizontal and parallel to the beam, and the wire meets its top between the two tape bands.
  In (b) the rocket hangs nose down from the T across its tail, with the T's ends taped to two opposite
  fins (one back fin, one front fin, as in the scan). The wire ends 0.7 units above the tail plane, on the
  T, and is drawn over everything (nothing lies above the tail).
- Projection: the true orthographic house view (elevation 32 deg, azimuth 45 deg) is unchanged.
- No new overlaps. The letter *a* sits about 3.5 mm left of the rule, and both panels' content stays
  inside the panel.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | The upper T's crossbar is drawn after the clamp's upper arm, so its back end (x = -30, 4 units behind the pad) shows through the arm's front face (y = 22). The crossbar end's centre projects to screen (1, 71.5), above the pad's top back edge (71.0) and inside the arm's front face (from 70.8 up). The 1.1pt butt end therefore leaves a nub about 0.15 mm across just above the pad's back corner, in both panels. In the 1973 art the T does not show behind the pad. This is far below what anyone sees at final size. | `fig43.tex:76` (crossbar), drawn after `:70-74` (arm repaint) | Optional. Draw the crossbar (line 76) before the clamp repaint (line 70), so the arm's front face hides its back end. The arm's faces cover only screen x -3 ... 9, and the crossbar's visible part starts at about 19, so nothing visible is lost. Do not shorten the crossbar: the wire must stay at its centre, x = 7. |
| 2 | note | The panel letters and the circled style are the same as in Ch2 Fig 50 and follow STYLE.md section 16 (italic, lower right of the drawing's panel, one baseline). | `fig43.tex:88-89, 98, 111` | None needed. |

## Verdict: pass (no must-fix)
