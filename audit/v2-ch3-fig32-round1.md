# v2 audit: ch3/fig32 (round 1)

Sources checked: scan `figures/ch3/fig32.png` (548 x 379 px; inset zoomed 4x; the inset outline measured column
by column); redraw `figures/v2/ch3/fig32.pdf` (current: same time as the .tex; 350.9 x 247.3 pt = 4.87 x 3.44 in;
fonts embedded), rendered at 400 dpi, and `build/v2/png/ch3-fig32-compare.png`; `figures/v2/ch3/fig32.tex`,
`fig32.py`, `fig32.csv`, `fig32.calib.json`; inventory row `ch3-fig32` (`figures/v2/inventory.csv`:98); caption
`chapters/ch3-sec4b.tex`:234-235; citing text :222-229 (pressure drag falls significantly up to L/d ≈ 2, only
slightly beyond); `STYLE.md` sections 14 and 16; `tamrfig.sty` (tamr, series1, `\rocketoutline[parabolic]` = a
paraboloid r ~ sqrt(x), `\dimline`, extension, centerline).

Checks made:
- **Calibration.** `digitize.py ticks` puts the x ticks at columns 88, 145, 201, 258, 313, 368.5, 423, 477 and
  531.5 and the y ticks at rows 305.5, 269, 233, 197, 161.5, 124.5, 88.5, 52.5 and 17.5. These are exactly the
  calib's xgrid and ygrid, at every drawn tick including the minors.
- **Data.**
  - I re-ran `fig32.py` with its write intercepted. The CSV comes out byte-identical, so it is current.
  - `digitize.py overlay`, run myself: mean 0.00 px, 95% 0.00 px, max 1.0 px. It passes.
  - Sampled values: L/d 0: 1.501 (flat start); 0.25: 1.361; 0.4: 0.922; 0.5: 0.487; 0.75: 0.298; 1: 0.242;
    2: 0.125; 3: 0.070; 4: 0.044. The curve is monotone. These match the inventory's reading.
  - The text's "reduced significantly ... up to about 2.0; further extension ... only slightly" holds.
- **Lettering.**
  - The y title is $\CD$, horizontal, as printed (the text says pressure drag coefficient; kept, rule 2). The x
    title is $\dfrac{L}{d}$, stacked.
  - y ticks are labelled 0, 0.5, 1.0, 1.5 and 2.0, with minor ticks at the 0.25 steps. x ticks are labelled 0-4,
    with minor ticks at the 0.5 steps, as printed.
  - The inset has $L$ (a dimension below, in a gap) and $d$ (at the right, in a gap), both upright.
  - Nothing is added.
- **Inset geometry.** I measured the scan's outline. At x = 290, 300 and 385 px the half-widths are 7.0, 9.25 and
  19.0 px; a paraboloid r = 27.25 sqrt(s/219) gives 6.9, 9.0 and 19.3. So the scan is a true paraboloid, as the
  caption says. The redraw uses the kit's exact paraboloid (L = 219, d = 55, L/d = 4) with a flat base and a
  centre line beyond the tip, matching the scan's placement.
- **Frame.** The axes are 4.2 in wide (443.5 px x 0.024054 cm), the same as Fig 30 and the house size. There is
  one curve, s1, 1 pt. The width is 4.87 in.
- **Legibility.** Nothing overlaps or is clipped, and the dimension arrowheads are visible.

## Findings

| # | severity | finding | where | suggested fix |
|---|---|---|---|---|
| 1 | note | The centre line ends at x = 508, just short of the $d$ dimension at 520, so it runs towards the "d" label at the same height. This is the scan's arrangement (its axis also runs to the d dimension line) and it reads correctly. | fig32.tex:25, 36 | Optional: end the centre line at about 503 so it stops nearer the base. |

## Verdict: pass (no must-fix)
