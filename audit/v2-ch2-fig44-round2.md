# v2 audit: ch2/fig44 (round 2)

Sources checked: the scan `figures/ch2/fig44.png` (zoomed at the angle indicator, the plug and afterbody,
and the wheel, counterweight and pan); the redraw `figures/v2/ch2/fig44.tex` / `.pdf` (PDF newer than the
source; rendered at 400 dpi, with details at 1000 and 1200 dpi; `build/v2/png/ch2-fig44-compare.png`;
`pdftotext` of the lettering); inventory row `ch2-fig44`; caption and citing text
`chapters/ch2-sec5.tex:178-230`; `chapters/ch2-sec6.tex:76-78`; `backmatter/figure-credits.tex:117`;
STYLE.md section 16; `figures/v2/tamrfig.sty`; the round 1 report and the fixer's response.

Size and fonts: 338.7 x 357.2 pt (4.70 x 4.96 in), within 6.5 in, the same as round 1. One font,
TeXGyreTermesX-Regular, embedded.

Round 1 findings:
- Should-fix 1 (the "Angle indicator assembly" leader meeting the near bearing support plate's left edge
  on the collar) is **resolved**. The leader now ends at (-63, 17, 0), on the pointer just beyond the collar
  (`fig44.tex:159-160`), which is where the scan's leader ends. Checks:
  - The end point is on the pointer's centreline. The pointer's half-width there is 2.4 x 35/47 = 1.8.
  - It is 3.3 screen units outside the collar's silhouette (the collar's radius is 8). So the leader ends on
    the pointer, not on the collar's outline.
  - It is about 9 screen units left of the plate's left edge (x = -5, y = +62, at screen x = -47.4; the end
    point is at -56.6), so the leader no longer crosses or meets that edge.
  - At 1200 dpi the leader crosses the pointer's upper edge only just before its end. It ends inside the
    pointer's outline and stays clear of the pointer's tip (about 18 units to its left) and of the pulley
    wheel's rim.
- Notes 2-4 (three pan strings, the box panels flush with the plates, the shaft's end arc at the hub)
  needed no action and are unchanged (`fig44.tex:148-149, 111-116, 103`).
- Regression: the source differs from round 1 only by the leader's end point and one added comment line,
  so the lines cited in round 1 have shifted by at most one. The 400 dpi render shows no other change.

Re-checked in this round:
- All eleven callouts, spelled as printed (checked with `pdftotext`).
- Leaders:
  - forebody tube top (`Xr`, 165, 10);
  - the plug's forward shoulder (`Xr`, 14, 7.6);
  - the pointer;
  - the lower (-z) fin of the afterbody (inside the fin at y = -100, z = -30: leading edge -79.8, trailing
    edge -110);
  - the far bearing's near face between bore and rim (radius 8.9);
  - the shaft inside the box;
  - the near plate's lower edge.
- Afterbody fins: the +x and -z fins are drawn behind the body and the +z and -x fins in front, matching the
  scan's four fins (up, right, lower left, down).
- Cord, counterweight and pan:
  - Both cords leave the wheel at the rim's y-extremes, where a vertical line is tangent to the rim's ellipse.
  - The cord shows over the rim from the silhouette (48.5 deg) to 180 deg.
  - The counterweight hangs on the left and the pan on the right, as printed.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | Round 1 should-fix 1 is resolved as described above. No new issues found. | `fig44.tex:159-160` | None needed. |

## Verdict: pass (no must-fix)
