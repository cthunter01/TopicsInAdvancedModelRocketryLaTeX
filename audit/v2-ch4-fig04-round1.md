# v2 audit: ch4/fig04 (round 1)

The 1973 form, shown only in the Errata and Supplement Part beside the 1994 replacement.

Sources checked:
- Scan `figures/ch4/fig04.png`, with 4x crops of the legend and the lettering block, compared with the 1994 scan.
- Redraw `figures/v2/ch4/fig04.pdf`: 300 dpi render, `build/v2/png/ch4-fig04-compare.png`, and a scan for
  opacity operators.
- Sources `fig04.tex`, `fig04.py`, `fig04.csv` and `fig04.calib.json`, plus `trajectory.py` (`B4`) and
  `common/b4.csv`.
- Inventory row `ch4-fig04`.
- Text: `backmatter/supplement/s-ch4-fig-table.tex`:15-27 (the 1973 caption), `chapters/ch4-sec2b.tex`:166-224 and
  `corrections/v2-figures.md` (rule 5; Minor "Ch4 Fig 4 (1973 and 1994)").

Checks made:
- **Lettering.**
  - Every item on the 1973 scan matches the 1994 scan: the legend "Actual curve" / "Approximation" with their
    solid and dashed samples; the block $I_t$ = 5.0 N-sec, $F_m$ = 13.0 N, $F_s$ = 3.5 N, $t_1$ = 0.14 sec,
    $t_2$ = 0.22 sec, $t_b$ = 1.20 sec; "B4"; $F$ (N); $t$ (sec); y ticks 0-16 step 2; x ticks 0, 0.2, ..., 1.2.
  - The redraw sets all of it. It is the same drawing, which is why the 1994 page calls itself "the same
    drawing, reproduced larger".
- **Approximation.**
  - Computed from eqs. (73a)-(73c) with the lettering: corners (0.14, 13.0), (0.22, 3.5), (1.20, 3.5), and the drop
    to 0 at t_b.
  - `fig04.check()` gives I_t = 5.000 by eq. (75) and 5.000 by area.
  - Rerunning `fig04.py` reproduces `fig04.csv` byte for byte. (It rewrote the file in place with identical bytes;
    I checked against the identical supplement copy by md5.)
- **Overlay on this scan.** I reran it with the drafter's calibration (residual 0.00 px):
  - Actual (`common/b4.csv`, traced from the 1994 scan): 658 points, mean 0.20 px, 95% 1.00 px (0.17 mm), max
    1.00 px. ok.
  - Approximation: 608 points, mean 0.52 px, 95% 2.00 px (0.34 mm), max 3.00 px. ok.
- **Caption** (1973, s-ch4-fig-table.tex:23-25): "parameters ... shown along with the actual and approximate
  thrust-time curves". True of the redraw.
- **Style.** Identical to `figures/v2/supplement/ch4-fig04-1994.tex` except for the CSV path, so the details are
  in that report:
  - The kit `tamr` frame at 4.2 in wide (as Ch1 Fig 5(a)), on a 4.82 x 3.15 in page.
  - s1 solid for the measured curve and s2 dashed for the approximation, as in the fig06a template.
  - Text in ink, an opaque legend and no transparency. The log is clean.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | The two v2 forms are the same figure (identical source apart from the CSV path; byte-identical CSVs and PDFs of equal size). The supplement's 1973 display therefore repeats the 1994 one at the same size once the includes are unscaled. That is correct, since the 1994 figure is "the same drawing", and it follows the brief. | `backmatter/supplement/s-ch4-fig-table.tex`:20 | Gate: confirm (see the supplement/ch4-fig04-1994 report, finding 2). |
| 2 | note | The drawn descending leg bends near 5 N, and the computed leg is straight. On this scan the overlay still passes (2.0 px). This is already logged as Minor. | descending leg | None. |

## Verdict: pass
