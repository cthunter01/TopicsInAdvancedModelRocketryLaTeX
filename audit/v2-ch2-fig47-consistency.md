# v2 audit: ch2/fig47 (chapter consistency fix, verification)

Issue to resolve: replace the local `phantom` definition (0.6pt, on 8pt off 1.6pt and two 1.6pt dots) with the
house `phantom` (0.6pt, long dash and two short) drawn in `ink`. Nothing else should change.

Sources checked: `figures/v2/ch2/fig47.tex` against the fixer's pre-fix snapshot (`diff`); an independent compile
into scratch, which is pixel-identical at 300 dpi to `figures/v2/ch2/fig47.pdf`; `make fig F=ch2/fig47` (5.22 x
2.00 in, no warnings); `build/v2/png/ch2-fig47-compare.png` against the scan `figures/ch2/fig47.png`; 600 dpi
before/after renders with crops of the noses and the tails, and a pixel diff; the PDF dash arrays and line
widths (qpdf `--qdf`); inventory row `ch2-fig47`; `audit/v2-ch2-fig47-round1.md` (its finding 3 asked for this
shared style); caption `chapters/ch2-sec5.tex:364-369`.

Checks made:
- **House style in use.** `diff` shows only two changes: the local `\tikzset{phantom/.style=...}` is gone, and
  the overshoot scope sets `outline/.style={phantom, draw=ink}` (with its comment updated). The PDF confirms
  it: the overshoot rocket's six paths (two body and nose sides, the nose-base and tail joints, two fins) now
  use [13.95 2.19 2.39 2.19 2.39 2.19] bp, i.e. 14pt, 2.2pt, 2.4pt, which is the house pattern. They are still
  0.6pt (0.598 bp) and in ink.
- **Reading.** At 600 dpi and at the 150 dpi compare size, the overshoot outline reads as a phantom (long dash,
  two short). It is distinct from the solid original position and from the thinner `ink2` dash-dot centre lines
  and wind axis. The joints at the nose base and tail are short (about 11pt) and fall inside one 14pt dash, so
  they draw solid. The old pattern also left them nearly solid, and they read correctly as joints of the
  phantom outline.
- **No regression.** The pixel diff changes nothing outside the overshoot rocket's area (x 1.08-4.04 in, y
  0.49-1.53 in). The labels next to it ("Position at / greatest / overshoot", $\alpha_1$) do not change, and
  neither does any line width other than the dash. The page size is unchanged (375.88 x 143.95 bp). The solid
  original position, both axis extensions, the angle arcs $\alpha_0$ (17.55 deg) and $\alpha_1$ (12.74 deg),
  "Wind axis" and both position labels are unchanged. Nothing is clipped or overlapping. The inventory's "drawn
  in dash-dot phantom lines" is still true in substance, and the caption names no line style.

## Findings

None.

## Verdict: pass
