# v2 audit: ch3/fig27 (consistency pass, verification)

Sources checked:
- The redraw `figures/v2/ch3/fig27.pdf`, built 22:15:05, after the tex (22:15:05), so it is current.
  - Rendered at 300 dpi.
  - `pdfinfo`: 368.9 x 120.2 pt (5.12 x 1.67 in).
  - `pdffonts`: all fonts embedded.
- `figures/v2/ch3/fig27.tex`.
- The round-1 and round-2 audits.
- The three consistency issues sent to this family: the velocity-profile convention, the label size, and the panel placement.

## Consistency issues

None of the issues names Fig 27, and the fixer did not touch it: the tex and pdf date from 22:15, before the round-2 audit (22:46). I checked whether any of the three conventions applies:
- **Velocity profiles.** There are none. $u_1$ and $u_2$ are kit `vec` arrows, which is the house form for velocity vectors.
- **Label size.** $p_1$, $p_2$, $u_1$, $u_2$, $A_1$ and $A_2$ take the picture default, `\small`. No `\footnotesize` is used.
- **Panel letters.** None; the figure has a single panel.

## Regression check

Nothing changed since round 2, so the round-2 pass stands. Its key features are still in place:
- the control surface in `dotted guide`;
- the walls in `hatch`;
- the Rankine half-body with its slot;
- the `\breakline` at the end of the body.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | No consistency issue applies, and the figure is unchanged since its round-2 pass. | fig27.tex | None. |

## Verdict: pass

No must-fix and no should-fix.
