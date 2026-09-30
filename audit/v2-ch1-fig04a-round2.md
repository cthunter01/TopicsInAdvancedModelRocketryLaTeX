# v2 audit: ch1/fig04a (round 2)

Sources checked: figures/ch1/fig04a.png (scan, zoomed 8x at the spike); figures/v2/ch1/fig04a.pdf (rendered 300
and 600 dpi, stroke widths measured in pixels); figures/v2/ch1/fig04a.tex:1-29; figures/v2/common/b4-1973.py,
b4-1973.csv, b4-1973.calib.json; figures/v2/inventory.csv row ch1-fig04a; caption chapters/ch1-sec2a.tex:345-355;
corrections/v2-figures.md (rule 5 and its exception; minor items on Fig 4); STYLE.md section 16. Overlays:
`digitize.py overlay b4-1973.calib.json` (panel (a)), and a calibration of panel (b) written for this audit
(ticks at columns 394.5, 449.5, 503.5, 558.5 and rows 297, 253, 207.5, 162, 118) with b4-1973.csv and the eight
rectangle tops. Areas integrated from b4-1973.csv.

| round-1 # | severity | status | evidence |
|---|---|---|---|
| 1 | must-fix | resolved | Both panels now draw figures/v2/common/b4-1973.csv (fig04a.tex:13, 22), the rule-5 exception. The tracing overlays the scan's panel (a) at 95% 0.0 px (max 2.2 px) and the curve printed in panel (b) at 95% 1.0 px; the rectangle tops overlay the printed tops at 95% 1.0 px. Peak 13.16 N at 0.162 sec, plateau 3.68 N, area 5.189 N-sec. Every spike rectangle now straddles the curve (height; curve at left -> right edge; area under the curve over its width vs lettered): 1: 2.25 N; 0 -> 4.60; .160 vs .160. 2: 6.32; 4.60 -> 7.75; .226 vs .234. 3: 10.00; 7.75 -> 12.39; .354 vs .360. 4: 12.94; 12.39 -> 12.62 (max 13.16); .440 vs .440. 5: 9.94; 12.62 -> 6.83; .339 vs .348. 6: 5.16; 6.83 -> 3.74; .284 vs .330. 7: 3.65; 3.74 -> 3.68 (min 3.61); 3.131 vs 3.115. Rectangle 8 (3.04 N) lies below the plateau (3.64-3.68 N; .256 vs .213), as printed. The staircase keeps the printed 13 N step. |
| 2 | should-fix | resolved | `clip=false` is in the `b4 panel` style (fig04a.tex:11). At 600 dpi the burnout drop at t = 1.2 sec is 8 px wide in both panels, the same as the plateau stroke (8 px). |

Also checked, unchanged and correct: axes of both panels; the lettered sum and its line breaks; panel letters (a),
(b) at the upper right inside each plot's axes, on one baseline (same panel style and height).

## New findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | should-fix | The new tracing gives the spike a bulb-shaped cap with shoulders at about 11 N on both flanks, visible at final size (300 dpi 1:1) in (a) and (b) (and in fig04b (c) and (d)). On the fall the curve drops almost vertically from 11.5 to 10.8 N at t = 0.1875 sec, between stretches of about 155 and 140-220 N/sec; on the rise the slope climbs from about 100 N/sec (7-10 N) to about 290 N/sec (11-11.4 N) and drops back to about 90 N/sec above 12 N. The printed flanks are straight: measured at the ink's centre, the fall runs 0.1843, 0.1882, 0.1922, 0.1961 sec at 12, 11, 10, 9 N (a uniform 256 N/sec; the tracing is at 0.1844, 0.1876, 0.1915, 0.1989), with a small rounded tip. The shoulders are sub-pixel quantization of the 150 dpi crop (under 0.5 px, so the overlay passes) kept by the light spline smoothing and made visible by the 2.1x enlargement. | common/b4-1973.py (the `splprep` smoothing, s = n x 0.6^2); b4-1973.csv t 0.13-0.19 | Smooth the spike more (e.g. a larger `s` for the rise and fall points, or a straight or low-order fit to each flank's row samples, joined by a small rounded tip), then recheck: overlay within 3 px, area about 5.19 N-sec, and each spike rectangle still straddling the curve. |

## Verdict

pass (0 must-fix, 1 should-fix)
