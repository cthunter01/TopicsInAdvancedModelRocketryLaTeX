# v2 audit: ch2/fig39 (round 2)

Sources checked: scan `figures/ch2/fig39.png`; redraw `figures/v2/ch2/fig39.pdf` (rebuilt 16:55 for the style
change; rendered at 400 dpi whole, 600 dpi of the mark row, 1600 dpi crops of C.P.$_n$ and C.G.); source
`figures/v2/ch2/fig39.tex`:1-30 (unchanged since round 1, mtime 15:46); round-1 report; inventory row `ch2-fig39`
(`figures/v2/inventory.csv`:52); caption and citing text `chapters/ch2-sec4.tex`:660-672;
`figures/v2/tamrfig.sty` (current `\dimline`, `dimension`, `extension`, `leader`, `cp mark`, `cg mark`);
STYLE.md section 16.

The source is unchanged. The render still has everything round 1 checked:
- all ten labels, in the text's notation;
- five dimension lines from the nose-tip extension line, stacked longest on top, each ending on its point's
  extension line;
- body stations and point stations as measured in round 1;
- the C.P. marks are circles with a centre dot and the C.G. is a quartered circle.

The current `\dimline` sets each label in a gap at the middle (\small, white fill). No label meets an extension
line. $\bar Z_n$ sits just right of its extension line, clear of the $\bar Z_{CS}$ line. The C.P.$_{T(B)}$ label
ends inside the bounding box. The figure has no panels.

| round-1 # | severity | status | evidence |
|---|---|---|---|
| 1 | note | accepted: note, no action | The C.G. leader still runs straight down (fig39.tex:25) and continues the $\bar W$ extension line through the body. The C.G. label at its foot keeps the meaning clear. |
| 2 | note | accepted: note, no action | The simplifications are unchanged: one ogive nose to 54, a fin tip chord of 15 against about 19, and leaders without elbows (fig39.tex:9-10, 23-27). None of them affects the notation. |

## New findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | should-fix | Each leader shows a short stub inside the mark it points to. The marks are drawn first (lines 20-21) and the leaders after (lines 23-27). The leaders start 3 units (1.8pt) from the mark centre, inside the rim: `cp mark` radius 2.5pt, `cg mark` 2.75pt. So each leader crosses the ring and runs into the white interior, almost reaching the centre dot of C.P.$_n$, C.P.$_{CS}$, C.P.$_{CB}$ and C.P.$_{T(B)}$. It also runs down the lower half of the C.G. quartering. The stubs show at 600 dpi and blur the circle-dot C.P. symbol. The 1973 leaders start at the circle's rim. (The extension lines above the marks also start inside, at 4 units, but they are drawn first and are covered.) | fig39.tex:20-21, 23-27 | Draw the marks after the leaders: move lines 20-21 below the scope (after line 28), so their white fill covers the leader ends. Alternatively, start the leaders at the rim (y = -4.8). |

## Verdict

pass (0 must-fix, 1 should-fix)
