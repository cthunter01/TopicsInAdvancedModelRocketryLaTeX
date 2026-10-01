# v2 consistency check: ch4/fig14

The issue in this round was that tag (c) did not sit by its own curve. It stood beside the 3.80 label, raised
2.17 mm to clear 6.84, so it floated by the ascending branch of curve (b): its edge was 2.0 mm from (b) and
10.8 mm from (c). The fixer used the issue's first option. The tag now stands on the 3.80 baseline (no yshift),
with 6.84 below it, as in the 1973 art. I am the verifier only and made no edits.

Sources checked:
- `figures/v2/ch4/fig14.tex`, diffed against the fixer's pre-fix copy (scratch `polish/fig14.tex.orig`). Three
  places changed:
  - the header comment, lines 6-8;
  - the two (c) leaders, lines 38-39 (3.80: 15 deg, 6.5 mm to 19 deg, 9.5 mm; 6.84: 12 deg, 7.7 mm to
    10 deg, 6 mm);
  - the tag node and its comment, lines 42-45 (the 2.17 mm yshift removed; the base shift follows the 3.80
    leader).
- `figures/v2/ch4/fig14.pdf` and `build/v2/png/ch4-fig14-compare.png`. Both were written at 09:22, from the
  current source.
- The scan `figures/ch4/fig14.png`, read at 2x, 5x and 8x around the (c) corner.
- Inventory row `ch4-fig14` (`figures/v2/inventory.csv`:145).
- `audit/v2-ch4-fig14-round1.md` and `-round2.md`.
- `fig14.py` and `fig10.py` (the family's `tag()`), `fig14-b.csv` and `fig14-c.csv`, `fig14-marks.csv`.
- Scratch builds of the current and pre-fix sources, at 400 and 600 dpi. I also rendered element-masked
  variants, with each curve, tag, time label and leader drawn alone, to measure ink-to-ink distances
  (scratch `polish-verify/masks.py`, `dist.py`).

Checks made:
- **Only the placement changed.**
  - This round wrote `fig14.tex` and `fig14.pdf` only.
  - `fig14.py`, the CSVs, the marks and the calibration date from 08:42-08:48, before the round-2 audit.
  - My build of the current source is pixel-identical to the PDF in the tree at 400 dpi. The page is still
    347.431 x 225.531 pt (4.83 x 3.13 in).
  - Compared with the pre-fix build, the changed pixels lie in one 20 x 9 mm box at the (c) corner (400 dpi
    columns 308-626, rows 925-1072). Curves (a) and (b), their tags and their four time labels are
    pixel-unchanged.
- **The issue is resolved.**
  - The tag now reads as part of "3.80 (c)". Its centre is 0.19 mm below the middle of the 3.80 digits, with a
    1.21 mm gap after the "0".
  - In data units its centre is at (452, 134) m. The printed tag is at about (473, 136) m; before the fix the
    tag was at (396, 149) m. It now stands where 1973 put it, to within 1 mm at final size.
  - The tag no longer hugs curve (b). Its edge is 3.72 mm from (b) (was 2.11) and its centre 5.73 mm (was
    4.12), so it keeps at least 2.75 mm from (b) by either reading of the issue.
- **Clearances.** Ink to ink, in mm at final size, before the fix and after it:

  | pair | before | after |
  |------|--------|-------|
  | tag (c) to curve (b) | 2.11 | 3.72 |
  | tag (c) to curve (c) | 9.86 | 11.76 |
  | tag (c) to "3.80" | 1.51 | 1.21 |
  | tag (c) to "6.84" | 1.02 | 0.91 |
  | "3.80" to curve (b) | 1.73 | 1.67 |
  | the 3.80 leader to curve (b) | 1.21 | 1.21 |
  | "3.80" to "6.84" | 2.16 | 1.96 |
  | "6.84" to the 3.80 leader | 7.57 | 3.87 |
  | "3.80" to the 6.84 leader | 2.80 | 4.51 |

  - The tightest gap, the tag to 6.84 at 0.91 mm, is legible. Round 1 accepted 0.47 mm there.
  - Every label still clears every curve by at least 1.5 mm (the round-1 benchmark).
  - The fixer's figures agree with mine to within 0.1 mm. That difference comes from the threshold.
- **The second option was declined, and the reason holds.**
  - The family's `fig10.tag()` on `fig14-c.csv` puts the tag centre at (10.2, 2.9) mm for a height of 10 m,
    (9.0, 3.5) mm for 20 m and (7.6, 4.1) mm for 30 m. These are measured from the origin; the tag radius is
    1.94 mm.
  - Curve (b) is 7.3-8.1 mm high over x = 9-10 mm. That leaves about 2 mm or less above the tag, and the 3.80
    label alone is 2.16 mm tall.
  - So the family placement cannot carry both time labels, as the fixer reports. Option 1 was the issue's own
    first suggestion, so the issue is resolved, not declined.
- **Lettering.** Unchanged and complete against the inventory and the scan:
  - the axis titles and ticks;
  - tags a, b, c;
  - the times 15.20, 41.03, 10.40, 20.01, 3.80 and 6.84.
- **House rules.**
  - The tag uses `curve tag` and the leaders use `leader`. There is no local style.
  - The PDF has no `/SMask`, `/ca` or `/CA`, and its fonts are embedded.
  - The 6.84 leader, now at 10 deg, separates cleanly from the x axis at its foot (600 dpi). The print has it at
    about 12 deg.
- **Documentation.**
  - The header comment ("on the baseline of its apex time, as printed, the curve (2 mm high)") is correct. Apex
    (c) is 41.2 m, which is 2.0 mm.
  - The `fig14.py` docstring ("beside the 3.80 label, as printed") still holds.
  - In the tag comment, 0.9 mm and 1.7 mm match my ink measurements. The "3.9 mm clear of curve (b)" is
    path-to-path; ink to ink it is 3.7 mm.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | The tag's edge is 11.8 mm from curve (c), so the family's 2.75 mm rule is not met for this one tag. The exception is documented (fig14.tex header and tag comment; the fig14.py docstring) and matches the 1973 placement. The geometry rules out the family placement (see above). | fig14.tex:42-45 | none |
| 2 | note | At 9.5 mm, the 3.80 leader is now the longest time leader in Figs 10-14 (the others run 4.5-8.5 mm), and at 19 deg it is shallower than the printed one (about 29 deg and 6 mm at this scale). The extra length is what lifts "3.80 (c)" clear of 6.84; it reads cleanly. | fig14.tex:38 | none |
| 3 | note | "6.84" sits about 3 mm left of its printed place relative to the tag: it lies under "80" and the left half of the tag, where 1973 runs it from under the "0" to past the tag. The 6.84-below-(c) arrangement reads as printed. | fig14.tex:39 | none |
| 4 | note | The tag comment's "3.9 mm clear of curve (b)" is path to path. Ink to ink it is 3.7 mm, while the comment's other two figures are ink measurements. This is cosmetic. | fig14.tex:44 | optional: "3.7 mm" |

## Verdict: pass

The issue is resolved by its first suggested option. Tag (c) stands on the 3.80 baseline as printed and well
clear of curve (b), and every element clears every other by at least 0.9 mm. Nothing outside the (c) corner
moved.
