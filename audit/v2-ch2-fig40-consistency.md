# v2 audit: ch2/fig40 (chapter consistency fix, verification)

Issue to resolve: the exhaust jet was a bundle of grey wavy streaks with a transparency fading (and a faded
`wash` envelope), the only gradient or transparency in the book. It should stay a set of wavy streaks leaving the
nozzle, drawn as plain `ink2` 0.3-0.45pt lines with no fading, ending at a fixed length or clipped to a
plume envelope. Nothing else should change.

Sources checked: `figures/v2/ch2/fig40.tex` against the fixer's pre-fix snapshot (`diff`); an independent compile
into scratch, which is pixel-identical at 300 dpi to `figures/v2/ch2/fig40.pdf`; `make fig F=ch2/fig40` (5.07 x
1.89 in, no warnings in the log); `build/v2/png/ch2-fig40-compare.png` against the scan `figures/ch2/fig40.png`;
600 dpi before/after renders with a crop of the jet and the right edge, and a pixel diff; the PDF objects (qpdf
`--qdf`); inventory row `ch2-fig40`; `audit/v2-ch2-fig40-round1.md`; caption `chapters/ch2-sec4.tex:676-680`.

Checks made:
- **Fading removed.** The source no longer loads `fadings`, and the `\tikzfading` definition and the faded `wash`
  envelope are gone. Before the fix the PDF had 1 `/SMask` and 2 `/Shading` entries; it now has none, and no
  `/ca` or `/CA`. The figure is flat line art.
- **Streaks.** There are six wavy streaks with the same waveforms as before, drawn `draw=ink2, line width=0.4pt`
  (within 0.3-0.45pt), each with its own fixed length of 186-205 behind the exit. They end in a ragged line, and
  the two longest run to the right page edge, as the 1973 jet runs off the drawing. At 600 dpi their round caps
  are complete, not cut. The bundle widens from about ±5 at the exit to about ±15. At 0.4pt the streaks sit
  just under the 0.45pt `ink2` leader, and the straight leader is still distinct from the wavy streaks.
- **No regression.** The only diff `diff` shows is the jet block and its comment. The 600 dpi pixel diff
  changes nothing outside x 3.37-5.07 in, y 0.96-1.19 in, the band behind the nozzle exit. The page width changed
  by 0.024 bp and the height not at all. The rocket outline, centre line, fins, the C.G. mark and leader, the
  $\bar W$ and $L_{ne}$ dimensions and their extensions, and the "$\dot m$ g/sec / expelled from / nozzle" callout
  are unchanged. The jet leader still ends inside the bundle at (414, -4), on the lower streaks. Nothing is
  clipped or overlapping. The caption names no line style.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | The streaks end at staggered fixed lengths instead of being clipped to a `\plumeshape` envelope. The issue allows either. The fixer's reason for rejecting the clip (it cuts streaks mid-wave and narrows the jet against the scan's widening one) is sound. | fig40.tex:15-18 | None. |

## Verdict: pass
