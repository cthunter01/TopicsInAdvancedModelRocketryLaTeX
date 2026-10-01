# v2 consistency verification: ch3/fig17

Issue checked: labelled free-stream velocity arrows were drawn at two weights across Chapter 3 (`vec` in some
figures, `thin vec` in Figs 16, 25, 30 and 34). Fig 17 was not named in the issue. The fixer checked it and left it
unchanged, and this report verifies that decision.

Sources checked:
- the scan `figures/ch3/fig17.png`
- the redraw `figures/v2/ch3/fig17.pdf` (321.60 x 187.66 pt = 4.47 x 2.61 in; all fonts embedded), rendered at 400 dpi
- `figures/v2/ch3/fig17.tex` and its CSVs
- the inventory row `ch3-fig17`
- STYLE.md section 16
- the round-1 and round-2 reports
- the labelled arrows in `figures/v2/ch3/*.tex`

Checks made:
- **No labelled velocity arrow, so the issue does not apply.** The three $U_\infty$ labels (fig17.tex:59) name the profiles' reference widths under their base lines and have no arrow. The inventory and the scan agree. The velocity arrows are the family's blue profile arrows (`profile arrow`, identical in Figs 16, 17, 18 and 25). The two curved arrows leaving through $A_1B_1$ (:61-62) are unlabelled flow marks, so `thin vec` is right for them, as for the outer-flow arrows of Fig 25. The x and y arrows (:75, :77) are coordinate axes, which are `thin vec` throughout the chapter.
- **tau_o.** The $\tau_o$ arrow (:69) is `thin vec`, as in Fig 16. These are the only Ch3 figures that draw tau_o, so they agree. The inventory describes it as "a short horizontal stroke on the plate, arrowhead not visible". The fixer suggests that stresses could be drawn as forces; that would be a change for both figures together, and the issue did not raise it.
- **Unchanged since round 2.** fig17.tex (22:17) predates the round-2 audit (22:44). The render matches round 2 in size and content. `make -q` still reports fig17.pdf out of date. This is the stale timestamp from round 1's identical CSV rewrite, recorded in round 2 (a scratch recompile was pixel-identical), and it is not a content change.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | Not affected: Fig 17 has no labelled free-stream velocity arrow. Its U_inf labels have no arrow, its flow marks are unlabelled, and x and y are axes. Leaving it unchanged is correct. | fig17.tex:59-77 | none |
| 2 | note | $\tau_o$ is `thin vec`, consistent with Fig 16 (the only other Ch3 figure with tau_o). | fig17.tex:69 | none (change Figs 16 and 17 together if the owner wants stresses heavy) |
| 3 | note | Carried from round 2: fig17.pdf's timestamp is older than its CSVs, so the next `make fig F=ch3/fig17` will rebuild it. The content is unchanged. | figures/v2/ch3/fig17.pdf | none |
| 4 | note (gate) | Carried from rounds 1 and 2: the eq. (80) edges and the momentum-balance wake depth have no entry in `corrections/v2-figures.md`, and the corner letters stay math italic rather than `curve tag` because Table 2 uses them as segment names. | fig17.tex:5-8, 64-68 | orchestrator: log and confirm |

## Verdict: pass (no must-fix)
