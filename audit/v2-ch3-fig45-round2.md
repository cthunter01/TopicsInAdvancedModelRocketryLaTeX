# v2 audit: ch3/fig45 (round 2)

Sources checked: scan `figures/ch3/fig45.png`; redraw `figures/v2/ch3/fig45.tex` and its current PDF (375.1 x 245.4 pt
= 5.21 x 3.41 in, all fonts embedded, clean log), rendered at 400 dpi (whole figure, and the three base-diameter
dimensions zoomed x2) and at 115.45 dpi without anti-aliasing for the overlay; inventory row `ch3-fig45`; caption
and citing text `chapters/ch3-sec6a.tex:210-236`; round-1 audit `audit/v2-ch3-fig45-round1.md` and the round-1
fix report; the Figure 43 and 44 redraws (family conventions).

Checks run:
- Round-1 note 2 (base-diameter offsets 22, 17 and 20): taken. All three \basedim calls now use 20 (fig45.tex:48,
  58, 70). In the zoomed render the stubs, the extension lines (base + 4 to base + 27) and the d_n and d_b labels
  are clear of the centre lines, the length-dimension extension lines and the cell edges. The stubs now stand at
  the same distance beyond each base.
- Round-1 note 1 (nose tip slightly blunt): declined with a reason (within tolerance; the semi-ellipse fits the
  scan far better than an ogive). Acceptable.
- Regression check, per-cell overlay. The body outlines (ink colour, within 38 px of each axis) were registered on
  the scan separately. Median / 95th percentile / max, px: Closed body 0.0 / 1.0 / 2.2, Nose 0.0 / 2.0 / 3.2,
  Blunt base I 0.0 / 2.2 / 7.0 (the maximum is the d_m label, which falls inside the mask), Blunt base II
  0.0 / 2.0 / 4.2. The shapes are unchanged from round 1.
- Lettering complete and correct: ell_b and d_m (Closed body); ell_n and d_n (Nose; the caption's ell_n/d_n);
  ell_b, d_m and d_b with "(d_m = d_b)" and "(d_m \ne d_b)"; roman I and II in the names. d_m = d_b holds for Blunt
  base I (18.25 both) and d_m != d_b for II (36 against 17.5).

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | The d labels sit at the upper stubs' tails here and at the lower tails in Figure 43. Each follows its own 1973 art, and both header comments now say so correctly. | fig45.tex:5-6; fig43.tex:7-8 | none |

## Verdict: pass (no must-fix)
