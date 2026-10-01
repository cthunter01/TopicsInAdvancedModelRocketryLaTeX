# v2 audit: ch3/fig54 (round 2)

Sources checked: round 1 report `audit/v2-ch3-fig54-round1.md` and the fixer's reply; redraw
`figures/v2/ch3/fig54.tex`; `figures/v2/ch3/fig54.pdf` (3.90 x 2.73 in, fonts embedded, newer than the .tex)
rendered at 400 and 900 dpi (both shoulders of (a), both bases, all of (b)); `build/v2/png/ch3-fig54-compare.png`;
scan `figures/ch3/fig54.png`; inventory row `ch3-fig54`; caption and citing text `chapters/ch3-sec7.tex:172-183,
199-208`; standing rule 1 in `corrections/v2-figures.md`; kit `dotted guide`, `outline`, `thin line`, `panel`.

Checks run:
- Round 1 note 1 (start offsets differ): the (a) shoulder expansions now start at 1.5 pt
  (fig54.tex:48), the same offset as every (b) expansion (64-66). **Resolved.**
- Round 1 note 2 (first dots fuse): the starts are now staggered by half the dot period (2.6 pt / 2). The
  (a) shoulder lines start at 1.5, 2.8 and 4.1 pt (48-50), and the base fans at 4, 5.3 and 6.6 pt from the base
  corner (32-33). At 900 dpi every first dot is a separate dot at both (a) shoulders and at all four base
  corners. The base fans' first dots sit about 3.9 pt from the corner and do not touch the wavy shear
  layer. **Resolved.**
- Round 1 note 3 (neck line colour): the neck line is now `[outline, thin line]` (39), so it is ink at 0.45 pt.
  **Resolved.**
- Regressions: none. The shock geometry is unchanged: attached cone shock from the tip, ending at y = 89 (45);
  the hyperbolic bow shock stands ahead of the ellipsoid nose (61). Neck, recompression shocks and wake lines
  are unchanged. The caption's line styles still hold (shocks solid, expansions dotted, wakes wavy, standing
  rule 1). Panel letters (a), (b) are at the lower right on one baseline. The width is still 3.90 in.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | All three optional notes from round 1 are applied. Offsets match across the panels, fan starts are staggered so no first dots fuse (checked at 900 dpi), and the neck line is in ink. The header comment (13-15) records the staggering. | fig54.tex:13-15, 32-33, 39, 48-50 | none |
| 2 | note | The local `shock`, `expansion` and `wake` styles are new names over kit styles plus a snake decoration, and no kit name is redefined. The fixer's style suggestions (a kit "wavy" style; a staggered "dotted fan" helper) are for the orchestrator. | fig54.tex:21-26 | none |

## Verdict: pass (no must-fix)
