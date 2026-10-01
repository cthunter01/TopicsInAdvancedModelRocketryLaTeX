# v2 audit: ch3/fig45 (round 1)

Sources checked: scan `figures/ch3/fig45.png` (cells zoomed x3, the nose tips x8); redraw
`figures/v2/ch3/fig45.tex` and its current PDF (5.21 x 3.41 in, fonts embedded, clean log), rendered at 400 dpi;
`build/v2/png/ch3-fig45-compare.png`; inventory row `ch3-fig45`; caption and citing text
`chapters/ch3-sec6a.tex:210-235` (fineness ratio ell_b/d_m, ell_n/d_n); STYLE.md sections 14 and 16; Figure 43
and Figure 44 redraws (family conventions).

Checks run:
- Overlay per cell (PDF at 115.45 dpi, 1 unit = 1 scan pixel, registered by cross-correlation): body outlines
  on the scan's ink (median 0-1 px); the larger 95th percentiles (5-7 px) come from the dimensions and labels,
  which are re-laid out, not from the bodies.
- Shapes: Closed body (semi-ellipse to the maximum at 90, parabola to a point at 232) and Blunt base II (same
  forebody, parabola to a flat base of radius 17.5 at 177) match the scan. Blunt base I: the og() function
  checked: 0 at the tip, 18.25 at 67.5, radius 133.95 = (18.25^2 + 67.5^2)/36.5, a true tangent ogive.
  Nose: a semi-ellipse 180 x 36; measured on the scan, radius against distance from the tip (scan mean of upper
  and lower) 6.0, 9.3, 14.8, 24.5, 30.8, 34.3 at 4.5, 9.5, 18.5, 48.5, 78.5, 108.5 px, against the ellipse's
  8.0, 11.5, 15.9, 24.6, 29.7, 33.0 and a tangent ogive's 1.8, 3.8, 7.3, 17.2, 24.9, 30.5: the ellipse is the
  better fit, as the drafter found.
- Lettering: Closed body ell_b, d_m; Nose ell_n, d_n; Blunt base I ell_b, d_m, d_b, "(d_m = d_b)"; Blunt base II
  ell_b, d_m, d_b, "(d_m \ne d_b)"; the four names; roman I and II. All present; d_m = d_b true of Blunt base I
  (both 18.25) and d_m != d_b of II (36 against 17.5); caption's ell_n/d_n for the nose holds (d_n at its base).
- Dimensions: lengths as \dimline above with extension lines (4 units clear, 4 beyond, as Figure 43);
  diameters by \dimout, labels upright beside the upper stubs' tails (where the 1973 leaders put them); base
  diameters between extension lines beyond the base. No overlaps; label-to-rule clearances about 3 mm.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | Nose tip: the semi-ellipse has a vertical tangent at the tip, so at final size the tip reads as round; the printed nose is somewhat sharper in its first 5 px (radius 6 against 8 at 4.5 px from the tip), though still blunt and within tolerance. The fit is justified (the ogive is far worse). | fig45.tex:13-14, 45-46 | none (optional: a slightly sharper superellipse if the owner wants the nose to look pointed) |
| 2 | note | The base-diameter dimensions stand 22, 17 and 20 units beyond the base (Nose, Blunt base I, Blunt base II): 4.8, 3.7, 4.4 mm. Barely visible across cells. | fig45.tex:48, 58, 70 | Optional: one offset (e.g. 20) for all three. |
| 3 | note | The d labels sit beside the upper stubs' tails here and beside the lower ones in Figure 43; each follows its 1973 art, but Figure 43's comment wrongly says its placement is "as Figure 45" (reported there). | fig45.tex:5-6 | none here |
| 4 | note | Extension lines at the round nose tips (Closed body, Nose, Blunt base II) start 4 units above the tip, where the outline is still nearly vertical, so they almost touch the outline for about 1 mm, as in the print. | fig45.tex:25 | none |

## Verdict: pass (no must-fix)
