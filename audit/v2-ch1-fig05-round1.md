# v2 audit: ch1/fig05 (round 1)

Sources checked: figures/ch1/fig05.png (scan, overlays upscaled 3x); figures/v2/ch1/fig05.pdf (rendered 300 dpi);
figures/v2/ch1/fig05.tex:1-27; figures/v2/common/engines.py, engines.calib.json, b14.csv, e62.csv, b4.csv;
figures/v2/inventory.csv row ch1-fig05; caption chapters/ch1-sec2a.tex:403-412 and citing text
ch1-sec2a.tex:388-401, 415-430; corrections/v2-figures.md (standing rule 5); figures/v2/tamrfig.sty.

Overlays with `digitize.py overlay engines.calib.json`: B14 95% 0.0 px (max 1.0 px), E62 95% 0.0 px (max 1.0
px). Both also check visually along their whole length, including the E62's initial peak and dip and both
burnout legs. The calibration points agree with the tick positions found by `digitize.py ticks` (B14 y ticks at
rows 280, 326, 371.5, 417, 462.5; x ticks at columns 326, 397, 470.5).

Checked and correct:
- **(a).**
  - Axes: y 0-16 step 4; x 0-1.2 step 0.2.
  - Curve: the shared B4 (rule 5, as intended). Spike 12.96 N at 0.145 sec, plateau 3.7 N, burnout 1.2 sec.
  - "B4" is set inside the curve.
- **(b).**
  - Axes: y 0-40 step 10; x 0-0.4 step 0.1.
  - Curve: B14 single peak 32.3 N at 0.203 sec, which matches the nominal 32 N of ch4-sec2b.tex:204-205.
    Burnout 0.35 sec; area 4.71 N-sec (class B).
  - "B14" is set inside the curve.
- **(c).**
  - Axes: y 0-120 step 30; x 0-0.6 step 0.1.
  - Curve: E62 initial peak 38.8 N at 0.025 sec, dip 21.7 N at 0.05 sec, linear rise to 118.4 N at 0.448
    sec, burnout 0.537 sec.
  - Area 34.1 N-sec, i.e. an average of 63.5 N, consistent with the designation E62.
  - "E62" is set inside the curve.
- **All panels.** $F$ (N) is rotated and $t$ (sec) is present. Panel letters (a), (b), (c) are present.
- **Caption and text.** The end-burner spike then near-constant thrust (a), the single high-thrust spike (b),
  and the peak reached gradually near the end of burning (c) are all as the caption and text describe.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | should-fix | The three panel letters are placed three different ways. (a) sits inside its axes at the upper right corner, at x = 4.2 in. (b) and (c) sit outside their axes (`rel axis cs:1.12,1`), at about x = 1.55 in and 2.35 in, floating in the white space beside each narrow plot. The 1973 art sets all three circled letters in one column at the right. | fig05.tex:12, 18, 24 | Put all three at one x (e.g. the right edge of (a)'s axes, `anchor=north east` at the same absolute x for each panel), or all inside their axes' upper right corners with `rel axis cs:1,1`. |
| 2 | should-fix | In (a) the burnout drop at t = 1.2 sec lies on the clip edge (xmax = 1.2), so half of the stroke is clipped and the drop renders at about half the curve's width. | fig05.tex:9-10 | `clip=false` on axis (a) (same as fig04a finding 2). |
| 3 | note | The redraw puts all three panels on one time scale (3.5 in per sec: widths 4.2, 1.4 and 2.1 in), where the 1973 panels each had their own. This is a layout change with no change of content, and it makes the burn times directly comparable. | fig05.tex:7, 15, 21 | None. |

## Verdict

pass (0 must-fix, 2 should-fix)
