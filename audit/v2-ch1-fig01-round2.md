# v2 audit: ch1/fig01 (round 2)

Sources checked: figures/ch1/fig01.png (scan); figures/v2/ch1/fig01.pdf (current, rendered 150, 300 and 1200 dpi);
figures/v2/ch1/fig01.tex:1-34; audit/v2-ch1-fig01-round1.md; figures/v2/inventory.csv row ch1-fig01; caption
chapters/ch1-sec1.tex:17-19 and citation :13; STYLE.md section 16 (panel letters); figures/v2/tamrfig.sty
(`cg mark`, `thin vec`, `centerline`, `pic rocket`).

| round-1 # | severity | status | evidence |
|---|---|---|---|
| 1 | should-fix | resolved | fig01.tex:16 now `shorten >=3.5pt`; the `cg mark` reaches 3.0pt from the centre (2.75pt radius + half its 0.5pt line), so the arrow tip stops 0.5pt short of the rim. At 1200 dpi the whole 5pt Stealth head shows beside C.G. 2, as in the scan. |
| 2 | should-fix | resolved | fig01.tex:26 passes `centerline=false` to both rockets of (b); only the explicit lines of :24-25 are drawn. At 1200 dpi the rotated axis reads as a clean dash-dot line through the C.G. and aft of it, and the vertical reference line as a thin solid line, as printed. |
| 3 | should-fix | resolved | (a) at (5.9, -2.7) (fig01.tex:20) and (b) at (9.3+1.9, 0.4-3.1) = (11.2, -2.7) (:31): one baseline, each at the lower right of its own panel ((a) just right of rocket 2's fins, x 4.6-5.8; (b) under the right edge of panel (b), whose arc and axis end at x 11.3-11.5). Matches STYLE.md section 16. |
| 4 | note | accepted: note, no action required | The comment (fig01.tex:2) still calls it the rocket of Figures 6-8 and the body keeps L = 4.4, d = 0.3, C.G. at 0.65L; not noticeable, as round 1 said. |

## New findings

None. Checked again: two equal upright rockets in (a) with the thin vector from C.G. 1 to C.G. 2; in (b) rocket 2
turned 30 degrees clockwise about the common C.G. (9.3, 0.4) without translation, the arc from the vertical line
to the rotated axis with its head on the axis; labels 1 and 2 on the right rockets in both panels; nothing added
or lost against the inventory lettering (1, 2, (a), (b)) and the caption.

## Verdict

pass (0 must-fix, 0 should-fix open)
