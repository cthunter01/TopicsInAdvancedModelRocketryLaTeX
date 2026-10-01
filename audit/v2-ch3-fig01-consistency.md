# v2 audit: ch3/fig01 (consistency fix verification)

Issue checked: vector lettering is mixed across Chapter 3 (keys ch3/fig01, fig12, fig39). For Fig 1 the
suggestion was $\vec{V}$ and $\vec{D}$ in place of $\bar{V}$ and $\bar{D}$, as in Ch1 Fig 6, Ch3 Figs 11 and 38
and the Symbols list, and to raise the question at the Chapter 3 gate.

Sources checked: redraw `figures/v2/ch3/fig01.tex`, rebuilt with `make fig F=ch3/fig01` (3.79 x 3.54 in, fonts
embedded) and rendered at 300 and 600 dpi (both vector labels zoomed); `build/v2/png/ch3-fig01-compare.png` beside
the scan `figures/ch3/fig01.png`; inventory row `ch3-fig01`; audits `audit/v2-ch3-fig01-round1.md` and
`-round2.md`; STYLE.md s.14 ("Vectors: `\vec{}` wherever an arrow is drawn") and s.16; `chapters/ch3-symbols.tex:106`
($\vec{V}$ vector velocity); eqs. (26)-(27) at `chapters/ch3-sec2b.tex:324-327`. I also checked the vector lettering
of the other figures: Ch1 fig06.tex:15, Ch3 fig11.tex:72, fig38.tex:45 and fig39.tex:44 now all use `\vec`. No
Ch3 figure source still sets a `\bar` vector.

## Issue (vector lettering): resolved

- fig01.tex:26-27 set $\vec{V}$ and $\vec{D}$. Both lines are drawn as house `vec` vectors with heads, so the
  STYLE s.14 rule (`\vec` wherever an arrow is drawn) applies. The lettering now agrees with the Symbols list,
  eqs. (26)-(27), Ch3 Figs 11, 12, 38 and 39, and Ch1 Fig 6.
- At 600 dpi, both arrow accents stand clear of their vector heads and of the axis. Each label still reads at the
  tip of its own vector: $\vec{V}$ above the V head, $\vec{D}$ below the D head.
- The header comment (fig01.tex:6-9) states the choice and its reason, and no longer says that the overbars are
  kept as printed.

## Regression check: none found

- The geometry is unchanged: the axis at 52 deg, alpha 23 deg, the C.G. at 0.72 L and the C.P. at 0.813 L
  (three-fin Barrowman, as in round 1). The `\anglemark` and the axis extensions are unchanged.
- The height grew from 3.52 to 3.54 in, because the arrow accent is taller than a bar. The width is the same
  (3.79 in).
- All other lettering is as before and as in the inventory: $\alpha$, C.G., C.P., and the heading over a rule with
  the eight bullet items in the printed order.
- The round-1 and round-2 notes (three-fin C.P., `\anglemark`, the 1973 headless lines drawn as house vectors) are
  still recorded and need no action.

## Findings

| # | severity | finding | where | suggested fix |
|---|---|---|---|---|
| 1 | note | The 1973 art prints overbars on lines without heads. The redraw adds heads and so uses `\vec`. Standing rule 2 (lettering as printed) argues the other way, so this stays a Chapter 3 gate item, as the issue asked. The choice is now the same across Figs 1, 11, 12, 38 and 39. | fig01.tex:26-27 | Raise it at the gate (it is in the fixer's doubts). |
| 2 | note | The inventory lettering column still records $\bar{V}$ and $\bar{D}$ (overbar). That column records the 1973 printing, so it is still accurate. Its notes already ask for a house vector style to be chosen, and the figure header now records that choice. | inventory.csv ch3-fig01 | Optional: the inventory owner can note the decision. No figure change. |

## Verdict: pass (no must-fix)
