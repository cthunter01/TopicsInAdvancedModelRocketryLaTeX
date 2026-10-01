# v2 audit: ch2/fig40 (round 1)

Sources checked: scan `figures/ch2/fig40.png` (3x upscale; 5x crop of the jet and the $\dot m$ callout); redraw
`figures/v2/ch2/fig40.pdf` (400 dpi render, crop of the tail and jet) and `build/v2/png/ch2-fig40-compare.png`;
build log `build/v2/ch2/fig40.log` (no warnings); `pdfinfo`/`pdffonts` (365.4 x 135.8 pt = 5.07 in wide, all
fonts embedded); source `figures/v2/ch2/fig40.tex`; inventory row `ch2-fig40`; `chapters/ch2-sec4.tex`:614-680
(text on $L_{ne}$, eqs. (99), (100), (101), the citing sentence and caption); STYLE.md sections 13 and 16;
`corrections/v2-figures.md`; the approved `figures/v2/ch2/fig39.tex` and the Ch1 plumes (`figures/v2/ch1/fig02.tex`,
`fig10.tex`).

Checks made:
- **Outline** (tex units are scan pixels from the nose tip, 1.25 times printed size, as Fig 39). Nose base 53.5
  (scan about 53); radius 13.5 (scan about 14); fin root leading edge 328, tip leading edge 356.5, trailing edge
  384.5 (scan about 330 / 357 / 385); span 42 (scan 42). The fin trailing edge is flush with the aft end. It is a
  one-tube rocket with an ogive nose, not the Fig 39 outline, as the family note asks.
- **Dimensions.** $L_{ne}$ runs from the nose-tip datum to the aft end, i.e. the nozzle exit. That matches
  ch2-sec4.tex:616-617 ("nozzle exit ... a distance $L_{ne}$ from the tip of the nose"). $\bar W$ runs from the tip
  to the C.G. at 264 (scan about 263), with $L_{ne}$ above $\bar W$ as printed. The $L_{ne}$ extension at the aft
  end starts above the fin tip (59 > 55.5).
- **Lettering.** Every inventory item is present: $L_{ne}$ (italic letter subscripts, STYLE.md 13), $\bar W$,
  C.G. (`\CG`), and "$\dot m$ g/sec / expelled from / nozzle" in three lines, with its leader ending inside the jet
  bundle at (414, -4). The jet half-width there is about 6.8.
- **Jet.** Six wavy streaks and a light envelope widen from half-width 6 at the exit to 15.5 and fade out
  downstream. This is the stylised ragged bundle the inventory note asks for, and it runs off the drawing as in
  1973.
- **Legibility.** No overlaps: the C.G. leader (to (300, -66)) clears the lower fin, which starts at x = 328.
  Nothing is clipped; "nozzle" sits inside the standalone border. Width is within 6.5 in.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | The jet streaks are `ink2` grey at 0.45pt with a fade. That is the colour and weight of the leader that points at them, so the exhaust reads a little like annotation. The Ch1 plumes are drawn as objects in `thin line`, which is `ink`. The streaks remain distinct from the straight leader in the 400 dpi render, so this is optional. | fig40.tex:20-21 (`draw=ink2`) | Optionally draw the streaks in `ink` (keeping the fade) so the jet reads as an object, not as dimension work. |
| 2 | note | The callout is set in three lines ("expelled from" on one line) where 1973 has four. This follows the inventory row and is not content. | fig40.tex:39-40 | None. |
| 3 | note | The C.G. callout is now a straight leader with the label at its end; 1973 has a dog-leg with the label to the left. This is the same convention as the approved Fig 39. | fig40.tex:37 | None. |

## Verdict: pass

No must-fix or should-fix items. Content, geometry and lettering match the scan, the inventory and the text.
