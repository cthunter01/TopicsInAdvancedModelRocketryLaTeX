# v2 audit: ch2/fig48 (chapter consistency fix, verification)

Issue to resolve: replace the figure's local `hidden` style with the house `hidden` (`draw=ink`, 0.45pt, on
2.6pt off 1.6pt). Nothing else should change.

Sources checked: `figures/v2/ch2/fig48.tex` against the fixer's pre-fix snapshot (`diff`); an independent compile
into scratch, which is pixel-identical at 300 dpi to `figures/v2/ch2/fig48.pdf`; `make fig F=ch2/fig48` (4.64 x
7.11 in, no warnings); `build/v2/png/ch2-fig48-compare.png` against the scan `figures/ch2/fig48.png`; a 600 dpi
before/after pixel diff; the PDF dash arrays and line widths (qpdf `--qdf`); inventory row `ch2-fig48`;
`audit/v2-ch2-fig48-round1.md` (its finding 5 asked for this shared style); caption
`chapters/ch2-sec6.tex:63-68`.

Checks made:
- **House style in use.** The only change `diff` shows is the removed `hidden/.style=...` line in the
  `\tikzset` block. The local `dim arrow` and `lab` styles are kept. The four hidden paths (nose shoulder end,
  engine casing, its two inner lines, end-view casing circle) now resolve to the house style, which was already
  identical to the local one. The PDF has the same four [2.59 1.59] bp dash arrays and the same line-width set as
  before.
- **No regression.** The 600 dpi render is pixel-identical to the pre-fix render (0 changed pixels), and the page
  size is unchanged (334.19 x 511.57 bp). So the 13 dimension values, the five callouts, C.G. and C.P., the end
  view, the true-scale bar and the DTV-1 title are all exactly as audited in round 1. The caption names no line
  style.

## Findings

None.

## Verdict: pass
