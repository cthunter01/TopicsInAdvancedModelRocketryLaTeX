# v2 consistency verification: ch3/fig18

Issue checked: labelled free-stream velocity arrows were drawn at two weights across Chapter 3 (`vec` in some
figures, `thin vec` in Figs 16, 25, 30 and 34). Fig 18 was not named in the issue. The fixer checked it and left it
unchanged, and this report verifies that decision.

Sources checked:
- the scan `figures/ch3/fig18.png`
- the redraw `figures/v2/ch3/fig18.pdf`, current by `make -q` (304.16 x 168.83 pt = 4.22 x 2.34 in; all fonts embedded), rendered at 400 dpi
- `figures/v2/ch3/fig18.tex`
- the inventory row `ch3-fig18`
- STYLE.md section 16
- the round-1 and round-2 reports

Checks made:
- **No labelled velocity arrow, so the issue does not apply.** The two $U_\infty$ labels (fig18.tex:51) stand over the profiles' top arrows and name the outer velocity. They have no separate arrow, as in the inventory and the scan. The velocity arrows are the family's blue profile arrows. The only `thin vec` arrows are the two y axes (:49), which are coordinate axes, drawn that way throughout the chapter.
- **Unchanged since round 2.** fig18.tex (22:17) predates the round-2 audit (22:44), and the PDF is current by `make -q`. The render matches round 2: same size, panel letters, inflection circle and delta dimension.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | Not affected: Fig 18 has no labelled free-stream velocity arrow. U_inf labels the profiles' outer arrows, and y is an axis. Leaving it unchanged is correct. | fig18.tex:48-52 | none |
| 2 | note (gate) | Carried from rounds 1 and 2: the inflection circle, placed by the equation, is about 21 px from the 1973 circle. There is still no entry in `corrections/v2-figures.md`. | fig18.tex:5-7 | orchestrator: log with the Ch3 items |

## Verdict: pass (no must-fix)
