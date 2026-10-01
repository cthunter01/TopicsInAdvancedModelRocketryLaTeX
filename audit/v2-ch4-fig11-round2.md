# v2 audit: ch4/fig11 (round 2)

Sources checked:
- Scan `figures/ch4/fig11.png`, read at 2x.
- Redraw `figures/v2/ch4/fig11.pdf`:
  - 200 and 600 dpi renders;
  - a fresh compile in a scratch tree (clean; pixel-identical to the committed PDF);
  - `pdffonts` (all embedded); no transparency.
- Sources `fig11.py`, `fig11.tex`, `fig11-a/b/c.csv`, `fig11-marks.csv` and `fig11.calib.json`, plus
  `trajectory.py` (B4).
- Inventory row `ch4-fig11` (`figures/v2/inventory.csv`:142).
- Caption `chapters/ch4-sec3.tex`:185-192 and the text at :78-168.
- `corrections/v2-figures.md`:69-73.
- Round-1 report and fix notes, and the round-1 sources in `fix1/orig/`.

Checks made:
- **Round-1 note 2 (CSV column order): resolved.**
  - The CSVs are now x, y, t. `digitize.py overlay` reads them as they are: (c) 95% within 1.00 px (ok); (a)
    94.4 px and (b) 9.2 px, the approved departure after burnout.
  - `fig11.tex` reads its columns by name, so it is unchanged (identical to `fix1/orig/fig11.tex`).
- **Round-1 should-fix 1 (the stale corrections record): still open.** corrections/v2-figures.md:69-73 still:
  - cites eqs. (83)-(87);
  - records only the apex of (a);
  - ends "Recompute ... or digitize the printed curves. **gate**".

  The fixer correctly declined, since the file is outside the figure, and drafted a replacement entry (round-1 fix
  notes, fig11 "changes"). I checked every number in that draft against the rerun. All are right.
- **Data reproduce.** The rerun in the scratch tree reproduces all four CSVs byte for byte.
- **Independent recomputation.** I wrote my own loop:
  - eqs. (125)-(131) for 1 m of rod, then (106)-(115), dt .001 s;
  - mass as m_o minus the integrated thrust over c = I_t/m_f, instead of the closed form (74);
  - thrust (73) from `trajectory.B4`.

  Results:
  - burnout (81.5, 131.0), (34.7, 51.2), (15.1, 18.7) m;
  - apex 7.07 s at (338, 418), 6.02 s at (207, 194), 2.72 s at (39, 33);
  - impact 19.16 s at 487 m, 13.06 s at 348 m, 5.70 s at 63 m.

  These are identical to `fig11-marks.csv` at the printed precision.
- **Times lettered: the computed ones (owner decision).** 7.07/19.16, 6.02/13.06, 2.72/5.70. Two decimals,
  including the trailing zero of 5.70. Printed values, for the record: 5.60/16.70, 6.20/14.30, 2.80/5.70. The
  burnout points round to the caption's 82/131, 35/51, 15/19.
- **Lettering.**
  - Titles $x$ (m), $y$ (m); x ticks 0-600 by 100; y ticks 0-400 by 100. The axis runs to 450 for the 418 m apex.
  - Tags a, b, c. Six time labels on leaders from the computed apexes and impacts.
- **Legibility** (600 dpi, masked renders):
  - Labels to curves: at least 3.48 mm.
  - Tags to curves: 0.57-0.58 mm (the family offset, although Fig 11's tags are placed in the .tex).
  - Tags to leaders: at least 1.84 mm. Labels to labels: at least 5.8 mm.
- **House rules and family.** The template is identical to Figs 10 and 12-14 (4.2 in axes, 0.007 in/m, s1-s3 solid,
  `curve tag`, `leader`, `\footnotesize` ink times). No local styles; flat art.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | should-fix | Carried over from round 1, still open: the Fig 11 record in corrections/v2-figures.md is stale. It names the vertical method (83)-(87), records only (a)'s apex, and still ends with the gate question although it opens "DECIDED". The figure itself is correct. | corrections/v2-figures.md:69-73 (orchestrator) | Replace it with the entry the round-1 fixer drafted (all six computed/printed time pairs, the computed apex and impact points, eqs. (125)-(131), (106)-(115), (73), (74)). I verified every number in it against the rerun. |
| 2 | note | The tags are placed by hand in fig11.tex rather than computed as in Figs 10 and 12-14. They sit at the family's 0.57-0.58 mm from their curves, and the curves are computed and fixed, so they cannot go stale unless fig11.py changes. | fig11.tex:39-41 | none |
| 3 | note | The leaders of 7.07 (below the apex) and 13.06 (to the right) run in different directions from the printed 5.60 and 14.30 leaders. The computed curves differ from the 1973 ones after burnout, so the printed placements do not carry over. All labels are clear. | fig11.tex:32-37 | none |
| 4 | note | The burnout points are not marked, as printed (editorial option; `fig11-marks.csv` has them). | - | none |

## Verdict

pass (0 must-fix, 1 should-fix, which lies outside the figure's files)
