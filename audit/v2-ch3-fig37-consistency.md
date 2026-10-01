# v2 audit: ch3/fig37 (consistency pass, verification)

Issue checked: mixed vector lettering across the chapter, where Figs 1, 12 and 39 used overbars. Fig 37 is in this
family but not named in the issue.

Sources checked:
- figures/v2/ch3/fig37.tex and .pdf, both 22:12. This is the build the round-1 audit checked.
- `make fig F=ch3/fig37` gives 5.18 x 3.08 in. This is unchanged from round 1 (373.2 x 221.7 pt).
- Inventory row ch3-fig37 and the round-1 audit (audit/v2-ch3-fig37-round1.md).
- Caption chapters/ch3-sec5a.tex:216-217.

## Resolution

Not applicable, and no change was made; the fixer correctly declined. The figure has no vector letters. Its
lettering is $x$, "Tangent ogive", 8.9, 33.0, 2.06, $x_o = .51\ell_b$, 2.54 (twice), $\alpha$ and "Flow /
direction". The arrows are labelled $x$ or are not labelled, so neither \bar nor \vec occurs. The flow-direction
arrow of (b) is unlabelled as a vector, as printed.

## Regression check

The .tex and .pdf are unmodified since round 1, and the build size is identical. The round-1 findings still
hold, including the optional note 5 on the (b) panel-letter position, which was not part of this issue.

## Findings

None.

## Verdict: pass (not affected, no regression)
