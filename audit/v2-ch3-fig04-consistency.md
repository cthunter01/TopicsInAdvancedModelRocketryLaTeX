# v2 consistency check: ch3/fig04

The issue checked here: Fig 4's y title "c (m/sec)" was the only rotated y title among the five atmosphere charts
(Figs 2, 3, 4, 7, 8). The suggested fix was optional: add `ylabel style={rotate=-90, anchor=east}`, as Fig 3 has.
The fixer applied it. I only verified the fix and made no edits.

Sources checked:
- `figures/v2/ch3/fig04.tex` (current), and `fig04.py`, `fig04.csv` and `fig04.calib.json`, which are dated
  before the fix and unchanged.
- The pre-fix state, reconstructed: the current source with the new `ylabel style` removed, built in my scratch
  dir. Its 400 dpi render is pixel-identical to the round-1 auditor's render
  (`scratchpad/ch3/u01-atmosphere/audit1/fig04-400.png`). So that one option is the only change that affects
  the drawing; the rest of the edit is in the header comment.
- My own build of the current source (pdflatex as in the Makefile, output to scratch). It is pixel-identical at
  400 dpi to the repo's `figures/v2/ch3/fig04.pdf`.
- `build/v2/png/ch3-fig04-compare.png`; the scan `figures/ch3/fig04.png`; inventory row `ch3-fig04`;
  `audit/v2-ch3-fig04-round1.md`.
- Figs 2, 3, 7 and 8 (sources and PDFs) for the family comparison; STYLE.md section 16; corrections/v2-figures.md
  (standing rule 2).

Checks made:
- **Source diff.** Line 14 now reads `ylabel={$c$ (m/sec)}, ylabel style={rotate=-90, anchor=east}]`, the same
  option string as Figs 2, 3, 7 and 8. The header comment says the title is set upright for the set and that the
  1973 art rotates it, which is accurate. Nothing else changed. No `\tikzset` and no local styles were added.
- **Render.** Compared with the pre-fix PDF, the page is 383.58 x 212.27 pt (5.33 x 2.95 in) instead of
  354.90 x 212.27 pt (4.93 in). It is under 6.5 in, and the height is unchanged.
  - pdftotext word boxes: every tick label and the x title moved right by the same 28.68 pt, with no vertical
    change.
  - The axes, grid, curve and ticks are therefore a rigid translation of the round-1 drawing.
  - The only new element is the upright title.
- **Placement matches Fig 3.**
  - Gap from the title to the tick labels: 7.46 pt (Fig 4) and 7.48 pt (Fig 3).
  - Title vertical centre: y about 93.3 pt in both, on the middle tick (335 / 280).
  - Figs 2, 7 and 8 have a gap of 9.31 pt, because a `\dfrac` box is wider. That gap comes from the box, not from
    a different setting.
  - On a right-aligned sheet of Figs 3, 4, 7 and 8 at 400 dpi, the four y titles read as one set.
- **Lettering against the scan and the inventory.**
  - The y title is "c (m/sec)": c is lowercase italic (STYLE 14) and the unit is roman.
  - y ticks 330, 335, 340, with minor grid lines at 332.5 and 337.5.
  - x ticks 0-2500 in steps of 500; x title "Altitude (meters)".
  - Nothing is added or lost. The one difference from the art and from the inventory row's "(rotated)" is the
    orientation. Standing rule 2 covers symbols, not orientation, and the symbols are unchanged.
- **Curve.** I recomputed the CSV from eq. (213), c = 340 sqrt((288.15 - 0.0065 h)/288.15), over 51 rows. The
  maximum difference is 4.7e-5 m/s.
  - I re-ran `digitize.py overlay` (axes `main`). Mean 0.04 px, 95th percentile 0.00 px, max 1.00 px: ok, the
    same as round 1 and as the fixer reported.
- **Build.** Compiles cleanly, with no warnings and no overfull or underfull boxes. All three fonts are embedded
  Type 1 (TeXGyreTermesX-Regular x2, NewTXMI).
- **Earlier audit.** This resolves round-1 finding 2 (the optional family uniformity), at the "make it upright"
  option. Findings 1 and 3 (the eq. (213) choice and its reinterpretation) concern the curve, which is unchanged.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | The y title is now upright, while the 1973 art and the inventory row's lettering ("c (m/sec) (rotated)") have it rotated. This is a deliberate departure, made for the family's look. It is not yet recorded anywhere the owner will see it at the gate. | fig04.tex:14; figures/v2/inventory.csv row ch3-fig04 | Orchestrator: add it to the Chapter 3 gate list in corrections/v2-figures.md, e.g. "Ch3 Fig 4: y title set upright like Figs 2, 3, 7, 8 (1973 rotates it)". Optionally update the inventory lettering note at the status update. |
| 2 | note | The page is now 0.15 in wider than Fig 3 (5.33 in against 5.18 in) because "c (m/sec)" is a longer upright title than "T (°K)". If the figures are centred at natural size, Fig 4's axes sit about 5 pt (2 mm) right of Fig 3's. Before the fix they sat about 9 pt to the left, so the fix brings the set closer together. The axes size and scale are identical. | figure width | none |

## Verdict: pass

The issue is resolved, and nothing regressed against the scan, the inventory lettering (apart from the intended
orientation) or the round-1 audit.
