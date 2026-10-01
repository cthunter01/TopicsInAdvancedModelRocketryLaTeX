# v2 audit: ch2/fig50 (round 1)

Sources checked: scan `figures/ch2/fig50.png` (zoomed 2-6x); redraw `figures/v2/ch2/fig50.tex` / `.pdf`
(5.17 x 5.84 in, fonts embedded), rendered at 400 dpi and at 105.8 dpi (one scan pixel = one redraw unit) for
an overlay; `build/v2/png/ch2-fig50{,-compare}.png`; inventory row `ch2-fig50`; caption
`chapters/ch2-sec6.tex:168-173`; citing text ch2-sec6.tex:155-157 (A), 192 (B), 222-225 (C), 256-259 (D),
273-275 (E), 287-290 (F); `corrections/v2-figures.md` standing rule 2; STYLE.md sections 13 and 16; sibling
`figures/v2/ch2/fig43.tex` (the other circled-letter figure under rule 2).

Checks:
- **Lettering.** All six notes match the inventory and the scan word for word: $I_L$ too large: / $\zeta$ too
  small / resonance severe / too heavy; $I_L$ too small: / easily disturbed / $\zeta$ too large / too light;
  $C_1$ too large: / weathercocking severe; $C_1$ negative: / statically unstable; $C_2$ too large: / $\zeta$ too
  large / drag excessive; $C_2$ too small: / $\zeta$ too small / resonance severe. The panel letters are circled
  lowercase a-f, as rule 2 requires (the text cites A-F).
- **C.G./C.P. order** (what the text relies on). The C.G. is ahead of the C.P. in (a), (b), (c), (e) and (f).
  The C.P. is ahead in (d) only: 156.5 against 169, nose on the left, so the rocket is statically unstable as
  ch2-sec6.tex:256-259 says.
  - (c): the fins are far aft and the C.P. is far behind the C.G. (54.5 px), giving a large static margin.
  - (e): fins both fore (57-83.5) and aft (166.5-220) of the C.G. (144.5).
  - (f): small fins (160-201) close behind the C.G. (142.5), ending ahead of the tail.
  - (a) is long and (b) short and stubby with oversized fins.
  - The marks use the house `cg mark` and `cp mark` styles.
- **Overlay (my own check).** I rendered the redraw at 105.8 dpi and aligned each rocket separately.
  - Redraw ink within 3 px of the scan's ink: 99.8% (a), 100% (b)-(f).
  - Scan ink within 3 px of the redraw's ink: 98.3% (a), 98.9% (b), 100% (c), (d), (f), 99.9% (e).
  - The only misses are the lower fins of (a) and (b): the 1973 art draws the two fins of each slightly
    differently, and the redraw mirrors them.
  - This confirms the drafter's figures.
- **Legibility.** Nothing overlaps or is clipped. The notes sit 9 px (2.2 mm) below the lowest fin in every
  row. The letters share one baseline per row. Width 5.17 in.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | The circled letters use a local `circled` style (12.5pt circle, 0.5pt, \small italic) rather than the house `curve tag` (11pt, 0.4pt, \footnotesize upright), which STYLE.md section 16 names for "circled reference letters the text cites". The current `figures/v2/ch2/fig43.tex:88` defines the identical `circled` style, so the two rule-2 figures agree with each other. Italic also matches the house `panel` letters. | fig50.tex:21 | Style suggestion: add this as a shared `circled panel` style in tamrfig.sty and mention it in STYLE.md section 16, so the rule-2 figures do not each carry a private copy. No change needed to the figure. |
| 2 | note | The letters sit above each rocket, centred, where the 1973 art puts them, not at the lower right of the panel as in the generic panel rule. This follows the printed placement, and the notes occupy the space beneath. | fig50.tex:44-56 | None. |
| 3 | note | The (b) nose is drawn as a pointed ogive where the 1973 art has a slightly blunt tip. The difference is under 1 px at the printed size and does not change the overlay. | fig50.tex:43 | None. |

## Verdict: pass (no must-fix)
