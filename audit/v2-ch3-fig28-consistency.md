# v2 audit: ch3/fig28 (consistency pass, verification)

Sources checked:
- The redraw `figures/v2/ch3/fig28.pdf`, built 22:22:32, after the tex (22:22:31), so it is current.
  - Rendered at 300 dpi.
  - `pdfinfo`: 369.9 x 211.6 pt (5.14 x 2.94 in).
  - `pdffonts`: all fonts embedded.
- `figures/v2/ch3/fig28.tex`. `fig28.py` is dated 22:39, but its CSVs are dated 22:21 and were not regenerated. That edit is earlier than the round-2 audit (22:46), which covers it.
- The round-1 and round-2 audits.
- The three consistency issues sent to this family.

## Consistency issues

None of the issues names Fig 28, and the fixer did not touch it. I checked whether any of the three conventions applies:
- **Velocity profiles.** There are none. (b) shows the surface pressure as headless s1 strokes (`pressure stroke`, 0.35pt) normal to the body. That is a pressure distribution, not a velocity profile, so the `profile` family does not cover it.
- **Label size.** $u_o$ and $p/((\rho/2)u_o^2)$ are `\small`. The ordinate ticks 0.2-1.0 are `\footnotesize` in ink2, which is the house tick-label form (fig28.tex:76-79).
- **Panel letters.** (a) and (b) use the kit `panel` style at the lower right of each panel (fig28.tex:82, 98). Fig 28 is a drawing with hidden axes, so the lower-right drawing rule applies, not the inside-the-axes plot rule. The two panels are stacked, so the one-baseline rule does not apply.

## Regression check

Nothing changed since round 2, so the round-2 pass stands. The body, streamlines, pressure curve and envelopes are all as round 2 audited them.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | No consistency issue applies, and the figure is unchanged since its round-2 pass. | fig28.tex | None. |
| 2 | note | The (b) pressure strokes (s1, 0.35pt) are thinner than the velocity-profile family's `profile stroke` (s1, 0.5pt). They show a different quantity, and there are many of them close together, so they are left as they are. | fig28.tex:56 | None. Only if the owner wants one stroke weight for all such diagrams. |

## Verdict: pass

No must-fix and no should-fix.
