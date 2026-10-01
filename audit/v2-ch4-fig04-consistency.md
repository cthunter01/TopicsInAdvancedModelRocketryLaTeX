# v2 audit: ch4/fig04 (chapter consistency fix, verification)

Issue to resolve: none for this figure. Both of the family's consistency issues concern Fig 16. The fixer did not
touch Fig 4. This check confirms that nothing changed and that the figure still meets the house rules.

Sources checked:
- `figures/v2/ch4/fig04.tex` (07:54), `fig04.csv` (08:00) and `fig04.pdf` (08:09). All of them are newer than the
  last kit change: `tamrfig.sty` at 07:40 dropped the legend `fill opacity`.
- A scratch recompile of the current `.tex`, rendered at 300 dpi and compared with the committed PDF.
- `pdffonts`, `pdfinfo`, and a stream scan for `/ca`, `/CA`, `/SMask` and shading.
- `audit/v2-ch4-fig04-round1.md` and `-round2.md`.
- `corrections/v2-figures.md`.

Checks made:
- **Unchanged.** The scratch recompile is pixel-identical to `figures/v2/ch4/fig04.pdf` (empty difference
  bounding box). The page is 347.05 x 226.61 pt, there are no LaTeX warnings, and all fonts are embedded.
- **Flat art.** No transparency operators. The legend uses the kit's opaque white fill.
- **Same drawing as the 1994 form.**
  - `fig04.tex` and `supplement/ch4-fig04-1994.tex` differ only in their header comments and in the CSV each
    reads.
  - `fig04.csv` and `ch4-fig04-1994.csv` are identical (cmp).
  - Both read the shared `common/b4.csv` (rule 5).
- **Consistent with Fig 16's fix.** The legend is `\footnotesize` (kit), as the Fig 16 k labels now are. The
  lettering block and B4 label are `\small`, like text labels elsewhere.

## Findings

None new. The round 2 note is still open, as a gate item for the orchestrator: after the switch, the supplement
Part shows two identical drawings. It is not a regression.

## Verdict: pass
