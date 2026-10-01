# v2 audit: ch4/fig04 (round 2)

The 1973 form of Figure 4, shown only in the Errata and Supplement Part beside the 1994 replacement.

Sources checked:
- Scan `figures/ch4/fig04.png`, with 4x crops of the legend and the lettering block.
- Redraw `figures/v2/ch4/fig04.pdf`:
  - a 400 dpi render and `build/v2/png/ch4-fig04-compare.png`;
  - `pdffonts` and a transparency scan;
  - a recompile of the current `.tex` in scratch, compared with the committed PDF.
- Sources `fig04.tex`, `fig04.py`, `fig04.csv` and `fig04.calib.json`, plus `trajectory.py` (`B4`) and
  `common/b4.csv`.
- Inventory row `ch4-fig04`.
- Text: `backmatter/supplement/s-ch4-fig-table.tex`:15-27 (the 1973 caption) and `chapters/ch4-sec2b.tex`:166-225.

## Round 1 follow-up

| r1 # | status |
|------|--------|
| 1 (same drawing as the 1994 form; duplicate display in the supplement Part) | Still correct. The gate item is still open: see the supplement/ch4-fig04-1994 round 2 report, note 2. |
| 2 (descending leg bends; overlay passes on this scan) | Unchanged, and already logged as Minor. |
| 3 (rerun touched the CSV's mtime only) | Resolved: the drafter rebuilt the PDF, which is now newer than every input. |

No regressions: the source is unchanged, and the recompile renders identically to the committed PDF.

## Checks made

- **Data reproduce.** I reran `fig04.py` in a scratch tree, so this time the repository was not touched. The
  output is byte-identical to `fig04.csv`, and identical (by md5) to the supplement copy. Eq. (75) and the
  area both give 5.000 N-sec, the lettered I_t.
- **Overlay on this scan**, with the drafter's calibration (residual 0.00 px):
  - Actual: 658 points, mean 0.20 px, 95% 1.00 px (0.17 mm), max 1.00 px. ok.
  - Approximation: 608 points, mean 0.52 px, 95% 2.00 px (0.34 mm), max 3.00 px. ok.
- **Lettering.** The 1973 scan's legend, block, "B4", axis titles and ticks are the same as the 1994 scan's
  (checked on crops: $t_b$, the $F_s$ blob read as s, and "N-sec"). The redraw sets every item.
- **Caption** (1973): "parameters ... shown along with the actual and approximate thrust-time curves" holds.
- **Style and consistency.**
  - The 400 dpi render is pixel-identical to the supplement/ch4-fig04-1994 render.
  - Same frame (4.2 in, as in Ch1 Fig 5(a)), s1 solid / s2 dashed as in the fig06a template, text in ink,
    ticks in ink2.
  - No transparency operators, fonts embedded, clean log.
- **Tick labels.** The x tick labels are "0, 0.2, ..., 1.2", as printed here and as in Ch1 Fig 3. Ch1 Fig 5
  writes "0.0" at the origin. Both forms are approved, so this is not raised.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | Same open gate item as supplement/ch4-fig04-1994 note 2: the supplement Part shows two identical drawings at the same size after the switch. | `backmatter/supplement/s-ch4-fig-table.tex`:20 | Orchestrator: list it for the Chapter 4 gate. |

## Verdict

pass
