# v2 audit: ch2/fig45 (chapter consistency fix, verification)

Issue to resolve: replace the figure's local `hidden` style (0.5pt, on 3pt off 2pt) with the house `hidden`
(`draw=ink`, 0.45pt, on 2.6pt off 1.6pt). Nothing else should change.

Sources checked: `figures/v2/ch2/fig45.tex` against the fixer's pre-fix snapshot (`diff`); an independent compile
into scratch, which is pixel-identical at 300 dpi to `figures/v2/ch2/fig45.pdf`; `make fig F=ch2/fig45` (4.95 x
2.82 in, no warnings); `build/v2/png/ch2-fig45-compare.png` against the scan `figures/ch2/fig45.png`; 600 dpi
before/after renders with a crop of the wheel, and a pixel diff; the PDF dash arrays and line widths (qpdf
`--qdf`); inventory row `ch2-fig45`; `audit/v2-ch2-fig45-round1.md` (its finding 4 asked for this shared
style); caption `chapters/ch2-sec5.tex:270-276`.

Checks made:
- **House style in use.** The only change `diff` shows is the removed local `\tikzset{hidden/.style=...}` line.
  The body lines behind the wheel (`\draw[hidden, ...]`, line 22) now take the house style. The PDF confirms
  it: the dash array changed from [2.99 1.99] bp to [2.59 1.59] bp (2.6pt/1.6pt), and that path's width changed
  from 0.498 bp to 0.448 bp (0.45pt). It is the same hidden line as Figs 41, 42 and 48.
- **Reading.** At 600 dpi the two body lines inside the wheel are clearly dashed in ink. They stay distinct
  from the `ink2` dash-dot wind axis, the rocket axis and the wheel's vertical centre line, and they still show
  the rocket passing behind the wheel, as printed.
- **No regression.** The pixel diff changes nothing outside x 1.91-2.95 in, y 1.29-1.64 in, the inside of the
  wheel. The page size is unchanged (356.66 x 202.83 bp). The two formula lines, "$R$ (cm)" with its leader to
  the rim, $\alpha^\circ$ and its arc, "Wind axis", the cords, counterweight, pan, weight and "$M$ (g)" are
  unchanged. Nothing is clipped or overlapping. The caption names no line style.

## Findings

None.

## Verdict: pass
