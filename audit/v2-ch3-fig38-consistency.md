# v2 audit: ch3/fig38 (consistency pass, verification)

Issue checked: mixed vector lettering across the chapter (Figs 1, 12, 39 used overbars). Fig 38 is the reference
form the issue cites ($\vec{L}$, $\vec{F}$, $\vec{D}_i$), so no change was expected here.

Sources checked:
- figures/v2/ch3/fig38.tex and .pdf: both 22:12, the same build the round-1 audit checked.
- `make fig F=ch3/fig38`: 4.97 x 2.16 in, unchanged from round 1 (357.7 x 155.6 pt).
- The scan figures/ch3/fig38.png, zoomed 2x and 8x on the force letters.
- Inventory row ch3-fig38 and the round-1 audit (audit/v2-ch3-fig38-round1.md).
- Caption chapters/ch3-sec5a.tex:269-272, which sets $\vec{F}$, $\vec{L}$, $\vec{D}_i$.

## Resolution

No change needed, and none was made; the fixer correctly declined. fig38.tex:45-47 set `$\vec{D}_i$`, `$\vec{L}$`
and `$\vec{F}$`, which matches the caption, the inventory lettering and STYLE s14 ("Vectors": `\vec{D}_i` named
explicitly). Zoomed, the 1973 accents are short strokes with a hook at the right end, as on Ch4 Fig 1. These read
as arrows, so the letters are as printed. Ch3 Figs 1, 12 and 39 now also use `\vec{}`, so Fig 38 agrees with the
rest of the chapter.

## Regression check

The .tex and .pdf have not been modified since round 1. The build size is identical, and the round-1 findings (C.P.
by Ch2 eq. (89), hatched section, alpha_i by two outside arrows, F vs the text's N) still hold.

## Findings

None.

## Verdict: pass (no change needed, no regression)
