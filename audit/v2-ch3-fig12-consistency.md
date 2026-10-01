# v2 audit: ch3/fig12 (consistency fix verification)

Issues checked:
- Vector lettering is mixed across Chapter 3 (keys ch3/fig01, fig12, fig39). For Fig 12 the suggestion was
  $\vec{V}$ in place of $\bar{V}$.
- All nine callout leaders in Fig 12 end in arrowheads. The suggestion was the plain, headless `leader`.

Sources checked: redraw `figures/v2/ch3/fig12.tex`. I rebuilt it with `make fig F=ch3/fig12` (6.20 x 2.00 in,
fonts embedded) and rendered it at 300 and 600 dpi (every leader end zoomed, and the base zoomed further). Also
checked: `build/v2/png/ch3-fig12-compare.png` beside the scan `figures/ch3/fig12.png`; inventory row
`ch3-fig12`; audits `audit/v2-ch3-fig12-round1.md` and `-round2.md`; `tamrfig.sty:79` (`leader`: ink2, 0.45pt,
no head) and `:110` (`leader arrow`); STYLE.md s.14 and s.16; the vector lettering of Ch1 Fig 6 and Ch3 Figs 1,
11, 38 and 39; and the use of `leader arrow` across Ch3 (only fig34.tex:43 is left, the kit's intended use).

## Issue 1 (vector lettering): resolved

- fig12.tex:81 sets $\vec{V}$ on the free-stream `thin vec`, which has a head. This matches STYLE s.14 and
  Figs 1, 11, 38 and 39, Ch1 Fig 6, the Symbols list and eqs. (26)-(27).
- At 600 dpi the accent is clear of the arrowhead and of the line, and the label sits below the head, as before.
- The header comment (fig12.tex:10-11) records the choice. Like Fig 1, it is a gate item against standing rule 2.

## Issue 2 (leaders): resolved

- All nine leaders (fig12.tex:85, 87, 89, 91, 93, 95, 99, 101, 103) are now `leader`. No `leader arrow` is left in
  the file. They are headless as printed, and they match the callouts of Ch2 Figs 39, 44, 48 and Ch3 Figs 17, 18,
  25, 27, 30, 37, 41, 43 and 50.
- The end points are unchanged. At 600 dpi each one still ends on its subject:
  - pressure foredrag on the nose outline;
  - laminar boundary layer inside the laminar wash (2.2, 0.245);
  - transition on the top of the transition tick (2.90, 0.304);
  - turbulent boundary layer inside the turbulent wash (4.85, 0.34);
  - fin-body interference drag on the fin-root junction (5.45, 0.2);
  - fin tip vortex on a loop of the vortex;
  - skin friction drag on the lower body line (3.6, -0.2);
  - the lug callout on the lug's lower edge (4.6, -0.27);
  - base drag inside the base bubble.
  No leader stops short or crosses a label.

## Regression check: none found from this pass

- The data is unchanged (the edge and eddy CSVs date from before round 2). The boundary layer, the wake, the base
  bubble, the lug, the edge-on fin and the alpha arc look as they did in round 2. The size is unchanged
  (6.20 x 2.00 in).
- All lettering from the inventory is present with the printed wording: ten callouts, $\alpha$, and $\vec{V}$ for
  the printed $\bar{V}$. "drag due to angle of attack" stays clear of $\alpha$ (round-1 should-fix 1).

## Findings

| # | severity | finding | where | suggested fix |
|---|---|---|---|---|
| 1 | should-fix | Still open from round 2 (should-fix 1), and not caused by this pass: the centre line runs to x = 6.45, past the base at 6.4. At 600 dpi a grey dash about 0.4 mm long shows just behind the base line, inside the base bubble. Figs 1 and 10 end their centre lines at 6.3. | fig12.tex:69 | `\draw[centerline] (0.1,0) -- (6.3,0);` (the white edge-on fin from 5.45 already hides the aft part). |
| 2 | note | The 1973 leaders are headless but elbowed (hand leaders with right angles; the inventory says "right-angled hand leaders"). The redraw's straight leaders follow the house rule (straight leaders, as Ch2 Fig 39), as accepted in rounds 1 and 2. | fig12.tex:84-103 | None. |
| 3 | note | The inventory lettering column still records $\bar{V}$. That is the 1973 printing, so the record is still accurate. The house choice is recorded in the figure header and goes to the gate with Figs 1, 11 and 39. | inventory.csv ch3-fig12 | None for the figure. |

## Verdict: pass (no must-fix; one should-fix carried over from round 2)
