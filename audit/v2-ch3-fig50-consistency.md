# v2 audit: ch3/fig50 (chapter consistency fix, verification)

Issue to resolve: none for this figure. The family's only consistency issue, the legend transparency, concerns
Fig 52, and the fixer did not touch Fig 50. This check confirms that nothing changed and that the figure meets
the flat-art rule.

Sources checked:
- `figures/v2/ch3/fig50.tex` (22:14) and `fig50.pdf` (22:14). Both are the round-1 fix state, which predates the
  round-2 audit (22:20). The PDF is up to date (`make -n` shows only the compare step).
- A 400 dpi render compared with the round-2 auditor's 400 dpi render.
- `qpdf --qdf` resources.
- `pdffonts` (all embedded) and `pdfinfo` (356.14 x 211.13 pt = 4.95 in).
- `audit/v2-ch3-fig50-round1.md` and `-round2.md`.

Checks made:
- **Unchanged.** The current render is pixel-identical to the round-2 render (empty difference bounding box).
  The round-2 verdict therefore stands as written, including the boattail leader fix verified there.
- **Flat art.** No `/ca`, `/CA` or `/SMask`. The only ExtGState is pgf's empty default dict.

## Findings
| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | Round-2 note 2 is still open and optional: "boattail" sits about 0.8 mm above the $\ell_b$ line, as in the scan. It does not belong to this consistency pass. | label at (432,-147) | optional |

## Verdict: pass
