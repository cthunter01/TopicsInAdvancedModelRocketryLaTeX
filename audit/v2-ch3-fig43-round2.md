# v2 audit: ch3/fig43 (round 2)

Sources checked: scan `figures/ch3/fig43.png`; redraw `figures/v2/ch3/fig43.tex` and its current PDF (374.6 x 171.6 pt
= 5.20 x 2.38 in, fonts NewTXMI/NewTXMI7 embedded, clean log `build/v2/ch3/fig43.log`), rendered at 400 dpi (whole
figure and the t / d_b region zoomed x2) and at 115.45 dpi without anti-aliasing (1 unit = 1 scan pixel) for the
overlay; inventory row `ch3-fig43`; caption and citing text `chapters/ch3-sec6a.tex:69-83`; round-1 audit
`audit/v2-ch3-fig43-round1.md` and the round-1 fix report; kit `\dimout`, `dim stub length`, `leader`, `edge fin`.

Checks run:
- Round-1 should-fix 1 (t as a plain leader): resolved. t is now dimensioned across the edge-on strip at x 419 (the
  printed station, scan x 463): `\dimout{(419,2.2)}{(419,-2.2)}{}` with a local `dim stub length=2.6mm` (11.82
  units), so the tails sit at y +-14.02, 3.7 units (0.8 mm) inside the body lines (R 17.75). Both heads point at the
  strip's faces and are clearly visible at 400 dpi. A straight `leader` continues the lower stub from (419,-14) to
  (419,-56), and t is anchored north below it. The leader crosses the lower body line, the fin root and the fin's
  leading edge at y -34.0, as the 1973 line does. At final size t clears the lower fin's leading edge by about
  5.5 mm and the l_t extension line (x 441.5) by about 4 mm. No overlaps.
- Round-1 note 2 (the header comment said "as Figure 45"): resolved. Lines 7-10 now say "as printed" and describe
  the t construction accurately.
- Regression check, outline overlay. I ran my own overlay: ink-colour pixels only (outlines; dimensions, extensions
  and leaders are ink2 and excluded), labels masked, registered on the scan at offset (10, 22) as in round 1.
  Results (median / 95th percentile / max, px): nose 0.0 / 1.0 / 1.4, body tube 0.0 / 1.0 / 1.0, upper fin
  0.0 / 1.0 / 1.4, lower fin 0.0 / 2.2 / 3.2, edge-on strip 1.0 / 2.0 / 2.8. 100% of the outline ink is within
  3 px. The outlines are unchanged from round 1.
- Lettering complete and unchanged: ell_n, ell_s, ell_t, ell_b, c_r, c_t, b, d_m, d_b, t, all upright.
  ell_n and ell_t are kept as printed (D36).

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | The t stubs are 2.6 mm long against the default 3.6 mm of the d_m and d_b stubs. This is needed so that both tails stay inside the body, and it is not noticeable at final size. The fixer's style suggestion (a far-stub option for \dimout) is reasonable kit work for later. | fig43.tex:54-57 | none |
| 2 | note | The t leader runs through the lower fin's interior and crosses its leading edge, as the 1973 line does. It is thin ink2 and does not read as a fin edge. | fig43.tex:57 | none |

## Verdict: pass (no must-fix)
