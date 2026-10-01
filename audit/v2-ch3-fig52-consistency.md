# v2 audit: ch3/fig52 (chapter consistency fix, verification)

Issue to resolve: the printed key is a pgfplots legend that inherits the kit's `fill opacity=0.9`. So fig52.pdf was
the only Ch3 PDF with transparency (/ca 0.9), and the gridlines showed faintly through the key. Suggested fix:
`fill=white, fill opacity=1` in the figure's legend style. Nothing else should change.

Sources checked:
- `figures/v2/ch3/fig52.tex` (23:13) and `figures/v2/ch3/fig52.pdf` (23:13). The PDF is up to date: `make -n`
  shows only the compare step.
- A diff against a pre-fix reconstruction (round-2 `legend style={nodes={inner sep=1pt}, font=\small}`).
  Compiled in scratch, its 400 dpi render is pixel-identical to the round-2 auditor's render of the pre-fix PDF,
  so the reconstruction is exact.
- Independent compiles in scratch of the current file, the pre-fix file and the issue's suggested one-line fix.
- `qpdf --qdf` content streams and resources.
- Renders at 400 and 1200 dpi.
- `build/v2/png/ch3-fig52-compare.png` against the scan `figures/ch3/fig52.png`.
- Inventory row `ch3-fig52`; `audit/v2-ch3-fig52-round1.md` and `-round2.md`; `tamrfig.sty` line 177.
- `pdffonts` (all embedded) and `pdfinfo` (452.43 x 292.62 pt = 6.28 in, unchanged).

Checks made:
- **Issue resolved.** qpdf finds no `/ca`, `/CA` or `/SMask` in fig52.pdf. The only ExtGState is pgf's empty
  default dict, the same as in Figs 48, 50 and 51. A sweep of every `figures/v2/ch3/*.pdf` finds no opacity entry
  below 1, so Ch3 is now flat throughout. At 1200 dpi the key's interior is pure white. Near-white,
  non-white pixels in the key crop fell from 13,145 before to 250 now, and those 250 are anti-aliasing at glyph,
  swatch and frame edges. The gridline ghosts are gone.
- **The fixer's stronger fix is justified.** The suggested `fill=white, fill opacity=1` renders identically to the
  current file at 400 dpi. But its content stream still sets `/pgf@ca0.9 gs` and then `/pgf@ca1 gs` right before
  the key's `re f`, so the PDF keeps a /ca 0.9 resource. I reproduced this in scratch. The kit's option comes
  first and a figure can only override it, not remove it. So replacing `every axis legend/.style` is the only
  local way to keep the opacity key out entirely.
- **No regression.** The page content stream differs from the pre-fix one in three hunks, all of them
  graphics-state lines. Before the key fill, the two `/pgf@ca0.9 gs`, two unused `0 G` (draw=none) and two
  repeated `1 g` are gone. Before the two entry texts, the `/pgf@ca1 gs` / `/pgf@CA1 gs` pairs are gone. Every
  path, mark, glyph and coordinate is byte-identical. That covers both curves, both axes and their lettering, the printed rulings, the key rectangle
  (`856.10 7.76 39.25 24.26 re`), the s1 solid and s2 dashed swatches, and the ink entry text. At 400 dpi,
  1,526 pixels change, all inside the key's box (218 x 135 px), by at most 5 levels: these are the removed ghosts.
  So the computed curves (eq. (210) with the GCR-x (C_Do)_FB; 0.473 for D_a), the true log x axis shared with
  Fig 51, the overlay figures of rounds 1 and 2 (95% within 2.24 px for D_e and 2.00 px for D_a), and the inventory
  lettering (`$D$ (N)`, `$R_\ell$`, ticks, key entries `$D_e$` solid and `$D_a$` dashed at the lower right) are all
  exactly as audited.
- **Against the scan and the inventory.** The key sits at the lower right with the grid blanked behind it, as
  printed and as the inventory notes ask. The blanking is now complete instead of 90%.

## Findings
| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | The fix replaces pgfplots' `every axis legend` style wholesale. It restates the kit's draw=none, fill=white and left-aligned cells, and drops only the opacity. This is a pgfplots key, not a kit style or macro, and a comment explains it. The cost: if the kit's legend style changes later, this figure will not follow. The fixer's kit suggestion stands: drop `fill opacity=0.9, text opacity=1` at `tamrfig.sty:177`, then shorten this back to `legend style={nodes={inner sep=1pt}, font=\small}`. | fig52.tex lines 24-26 | kit owner; revert locally after |
| 2 | note | Outside the family: `ch4/fig06a.pdf` still carries /ca 0.9 from the same kit style, and it is the only other pgfplots legend. The kit change fixes both. | ch4/fig06a.tex line 13 | kit owner |
| 3 | note | Round-1 note 3 (the key in `\small` against the kit's `\footnotesize`) is unchanged, kept as before. It is a gate choice. | | none |

## Verdict: pass
