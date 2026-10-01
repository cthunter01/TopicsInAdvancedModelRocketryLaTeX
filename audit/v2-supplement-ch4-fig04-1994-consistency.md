# v2 audit: supplement/ch4-fig04-1994 (chapter consistency fix, verification)

Issue to resolve: none for this figure. Both of the family's consistency issues concern Ch4 Fig 16. The fixer did
not touch this figure. This check confirms that nothing changed and that the figure still meets the house rules.

Sources checked:
- `figures/v2/supplement/ch4-fig04-1994.tex` (07:54), `.csv` (07:56) and `.pdf` (07:56). All of them are newer
  than the last kit change (`tamrfig.sty`, 07:40, the opaque legend).
- A scratch recompile of the current `.tex`, rendered at 300 dpi and compared with the committed PDF.
- `pdffonts`, `pdfinfo`, and a stream scan for `/ca`, `/CA`, `/SMask` and shading.
- `audit/v2-supplement-ch4-fig04-1994-round1.md` and `-round2.md`.
- `corrections/v2-figures.md` line 381 (the bent leg of the approximation, computed straight).

Checks made:
- **Unchanged.** The scratch recompile is pixel-identical to the committed PDF (empty difference bounding box).
  The page is 347.05 x 226.61 pt, the same as `ch4/fig04`. There are no LaTeX warnings, and the fonts are
  embedded.
- **Flat art.** No transparency operators.
- **Same as the 1973 file.** The drawing code is identical to `ch4/fig04.tex`; only the header comments and the
  name of the CSV it reads differ. The CSVs are byte-identical, and both files use the shared `common/b4.csv`.

## Findings

None new. Round 2 note 2 (the supplement Part shows two identical drawings after the switch) is still an open
gate item for the orchestrator. It is not a regression.

## Verdict: pass
