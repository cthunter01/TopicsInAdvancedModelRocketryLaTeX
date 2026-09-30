# v2 audit: ch1/fig04a (round 1)

Sources checked: figures/ch1/fig04a.png (scan, upscaled 4x); figures/v2/ch1/fig04a.pdf (rendered 400 dpi);
figures/v2/ch1/fig04a.tex:1-29; figures/v2/common/b4.py, b4.csv, b4.calib.json;
figures/supplement/ch4-fig04-1994.png (the tracing source); figures/v2/inventory.csv row ch1-fig04a; caption
chapters/ch1-sec2a.tex:343-355 and citing text ch1-sec2a.tex:324-338; corrections/v2-figures.md (standing rule 5
and the minor item on Fig 4(b)); figures/v2/tamrfig.sty.

Overlays: b4.csv against the 1994 crop (b4.calib.json) gives 95% 0.0 px. For this audit I also wrote a
calibration for both panels of the 1973 crop and overlaid b4.csv and the eight rectangle tops of (b) on it. I
computed the area under b4.csv and under the curve over each rectangle's width.

Checked and correct:
- **Axes.** Both panels run y 0-16 step 4 and x 0-1.2 step 0.4 (printed 0, 0.4, 0.8, 1.2). $F$ (N) is rotated;
  $t$ (sec) is present.
- **Panel letters.** (a) and (b) are present.
- **B4 curve.** It is the shared 1994 tracing (rule 5, as intended). Peak 12.96 N at 0.145 sec, plateau 3.70 N,
  burnout 1.2 sec, area 5.09 N-sec.
- **Lettered sum.** Set above (b) in the printed order and line breaks: $I_t \cong .160 + .348 + .234 + .213$ /
  $+ .360 + .440 + .330 + 3.115$ / $= 5.20$ N-sec. The sum is 5.200. The `\cong` matches Fig 3.
- **Rectangles of (b).**
  - There are eight, adjacent over [0, 1.2].
  - Each rectangle's area equals a lettered value: .160, .234, .360, .440, .348, .330, 3.115, .213 from left
    to right (heights 2.25, 6.32, 10.00, 12.94, 9.94, 5.16, 3.65, 3.04 N).
  - Their tops overlay the printed rectangle tops at 95% 1.0 px, so the rectangles are the 1973 ones.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | must-fix | In (b) the rectangles no longer approximate the curve drawn with them. The text says the curve "has been approximated by a series of eight adjacent rectangles ... by eye" (ch1-sec2a.tex:328-331). The rectangles are the 1973 ones, cut to the 1973 tracing, whose spike falls about 0.02-0.03 sec later than the shared 1994 tracing (rule 5). Against the drawn curve: rectangle 3 [0.108, 0.144] at 10.0 N lies under the rise (curve 9.2 to 12.95 N). Rectangle 4 [0.144, 0.178] at 12.94 N stands up to 5.7 N (14 mm) above the fall at its right edge (curve 12.95 to 7.26 N). Rectangle 5 [0.178, 0.213] at 9.94 N lies wholly above the curve (curve 7.26 to 4.92 N, 2.7-5.0 N below its top); its lettered area .348 is 67% more than the 0.209 under the curve. Rectangle 6 [0.213, 0.277] at 5.16 N is wholly above too (curve 4.92 to 3.80 N). In the 1973 print every spike rectangle straddles its curve. The redraw makes the "by eye" method look wrong, a distortion the original does not have. | fig04a.tex:17-22; common/b4.csv | Gate decision (rule 5 did not consider (b)). Either (i) exempt Fig 4 from rule 5 and draw the 1973 tracing in all four panels (panel (a) of the scan reads 8.3 N at 0.20 sec and 6.7 N at 0.22 sec, against 5.6 and 4.9 N for the shared curve); or (ii) keep the shared curve and re-cut the rectangle widths, which are not lettered, so each straddles it with its lettered area. For example, edges at equal cumulative area are 0, .067, .102, .136, .177, .243, .330, 1.13, 1.20, giving heights 2.40, 6.56, 10.73, 10.63, 5.28, 3.81, 3.89, 3.04 N; the staircase then loses the printed 13 N step. Option (i) keeps the print's look; option (ii) changes it. |
| 2 | should-fix | The burnout drop at t = 1.2 sec (and rectangle 8's right side in (b)) lies exactly on the plot's clip edge (xmax = 1.2). Half of each stroke is clipped away, so the drop renders at about half the curve's width (checked at 400 dpi); the corner at (1.2, 3.64) looks thin. | fig04a.tex:9 (`xmax=1.2`), 13, 22 | Add `clip=false` to the `b4 panel` style (the data stay inside [0, 1.2] x [0, 16]), or set `xmax=1.2` with `enlarge x limits={upper, abs=1pt}`. The same fix applies to fig04b (c) and fig05 (a). |

## Verdict

fix (1 must-fix, 1 should-fix)
