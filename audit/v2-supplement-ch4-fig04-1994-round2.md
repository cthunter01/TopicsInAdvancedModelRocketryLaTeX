# v2 audit: supplement/ch4-fig04-1994 (round 2)

Chapter 4's Figure 4 (the 1994 replacement), also shown in the Errata and Supplement Part.

Sources checked:
- Scan `figures/supplement/ch4-fig04-1994.png`.
- Redraw `figures/v2/supplement/ch4-fig04-1994.pdf`:
  - a 400 dpi render, and `build/v2/png/supplement-ch4-fig04-1994-compare.png`;
  - `pdffonts`, and a scan of the decompressed streams for transparency;
  - a recompile of the current `.tex` in scratch, compared with the committed PDF.
- Sources `ch4-fig04-1994.tex`, `.py`, `.csv` and `.calib.json`, plus `figures/v2/ch4/fig04.py`,
  `trajectory.py` (`B4`) and `common/b4.csv`.
- Inventory row `sup-ch4-fig04-1994`.
- Text: `chapters/ch4-sec2b.tex`:166-225, `backmatter/supplement/s-ch4-fig-table.tex`:1-27 and
  `frontmatter/about-this-edition.tex`:214, 249-252.
- `corrections/v2-figures.md`: rule 5, Minor "Ch4 Fig 4 (1973 and 1994)", and the legend item under "Style
  suggestions". Also the uncommitted `tamrfig.sty` change, which removes the legend's fill opacity.

## Round 1 follow-up

All four round 1 findings were notes; none was a must-fix or should-fix.

| r1 # | status |
|------|--------|
| 1 (approximation overlay 3.16 px) | Still accurate; already logged as Minor. Nothing to do. |
| 2 (supplement Part shows two identical drawings) | Still an open gate item. It is not yet in `corrections/v2-figures.md`, and the drafter has passed it to the orchestrator as a doubt. Carried as note 2 below. |
| 3 (legend `\footnotesize`, lettering `\small`) | A kit-wide question, already under "Style suggestions". Nothing to do here. |
| 4 (`.py` imports `ch4/fig04.py`) | Declined with a sound reason (one function keeps the two forms identical). Accepted. |

No regressions: the source is the same as in round 1, and a recompile in scratch renders identically to the committed PDF.

## Checks made

- **Data reproduce.** I reran `ch4-fig04-1994.py` (with `fig04.py` and `trajectory.py`) in a scratch tree. The
  CSV is byte-identical to the committed one (608 points). The script reports eq. (75) I_t = 5.000 N-sec and
  area 5.000 N-sec. The corners are exact: (0.14, 13.0), (0.22, 3.5), (1.20, 3.5), then the drop to 0.
- **Equations.** `B4.thrust` is eqs. (73a)-(73c) with the lettered F_m 13.0, F_s 3.5, t_1 = t_m 0.14,
  t_2 = t_s 0.22 and t_b 1.20. Eq. (75) gives 13.0(0.22)/2 + 3.5(1.20 - 0.07 - 0.11) = 5.0, the lettered I_t.
- **Overlay**, rerun with the drafter's calibration (residual 0.00 px). The calibration's gridlines agree with
  the scan's axes and ticks.
  - Actual (`common/b4.csv`): 658 points, mean 0.06 px, 95% 0.00 px, max 5.10 px (at the burnout corner). ok.
  - Approximation: 608 points, mean 0.88 px, 95% 3.16 px (0.54 mm), max 5.00 px. This is the bent drawn
    descending leg, already logged as Minor.
- **Lettering** (checked against 4x crops of the scan). All of it is present and as printed:
  - the legend "Actual curve" (solid) and "Approximation" (dashed), top left;
  - the block $I_t$ = 5.0 N-sec, $F_m$ = 13.0 N, $F_s$ = 3.5 N, $t_1$ = 0.14 sec, $t_2$ = 0.22 sec,
    $t_b$ = 1.20 sec, aligned on "=" and on the decimal points;
  - "B4" inside the curve;
  - $F$ (N) (rotated), $t$ (sec), y ticks 0-16 step 2, and x ticks 0, 0.2, ..., 1.0, 1.2 as printed.
- **Caption and text.**
  - "parameters ... shown along with the actual and approximate thrust-time curves" holds.
  - "$t_1$ as shown here is $t_m$ ... $t_2$ ... is $t_s$" holds: the block letters $t_1$ and $t_2$, and the
    computed corners are at t_m and t_s.
  - The citing sentence (ch4-sec2b.tex:206-207) holds.
  - "the same drawing, reproduced larger" (edcap) and About This Edition :214 still describe the 1994
    document truly.
- **Style.**
  - Kit `tamr` frame at 4.2 in wide, as in Ch1 Fig 5(a); the page is 4.82 x 3.15 in.
  - s1 solid for the measured curve and s2 dashed for the approximation, as in the fig06a template. The
    approximation is drawn first, so the measured curve lies over it at the peak and at t_b.
  - Text is in ink (#0B0B0B, sampled from the render) and tick labels in ink2.
  - No transparency: the only ExtGState is pgf's empty default, with no /ca, /CA, /SMask or shadings.
  - Fonts are embedded and the log is clean.
- **Legibility** at final size (4.82 in wide, unscaled): labels `\small`, ticks and legend `\footnotesize`.
  Nothing overlaps.
- **Family.** The 400 dpi render is pixel-identical to `ch4/fig04`'s. The two CSVs are byte-identical, and the
  sources differ only in the CSV path and the header comments.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | The approximation overlays at 95% 3.16 px (0.54 mm), because the drawn descending leg bends. This is unchanged and already logged (Minor, "Ch4 Fig 4 (1973 and 1994)"). | descending leg | None. |
| 2 | note | Open gate item, carried from round 1: once the switch drops the scan widths (0.75 and 0.6 `\textwidth`), the supplement Part shows this figure and "The 1973 Figure 4, which this figure replaces" as two identical vector drawings at the same size. It is not yet recorded in `corrections/v2-figures.md`. | `backmatter/supplement/s-ch4-fig-table.tex`:6, :20 | Orchestrator: list it for the Chapter 4 gate (keep both identical redraws, as the brief and the Ch1 Fig 2 / Ch2 Fig 36 precedent do). |

## Verdict

pass
