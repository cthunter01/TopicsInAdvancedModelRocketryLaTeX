# v2 audit: ch1/fig09 (round 2)

Sources checked: figures/ch1/fig09.png (scan; rocket and pad regions upscaled 6x, widths measured);
figures/v2/ch1/fig09.pdf (rendered 400 and 1200 dpi; pad, origin and rocket cropped); figures/v2/ch1/fig09.tex:1-37;
audit/v2-ch1-fig09-round1.md; figures/v2/inventory.csv row ch1-fig09; caption chapters/ch1-sec3.tex:50-58;
figures/v2/tamrfig.sty (`\pic{rocket}` plume keys, `\plumeshapeb`, `vec` 1.3pt, `panel`); STYLE.md section 16.

| round-1 # | severity | status | evidence |
|---|---|---|---|
| 1 | must-fix | resolved | fig09.tex:15-16 adds `plume=0.8` (half the 1.6 length) and fig09.tex:13 lowers the rod's top to 4.4. The pic's tail is at 5.3, the plume's point at 4.5, so a 1 mm gap stays open above the rod (scan: about 1.5 mm). The render shows the spindle hanging below the fins, pointed at the bottom, as printed. |
| 2 | should-fix | not resolved (in part) | fig09.tex:14 now draws a concave fillet, which reads as a brace, but its foot lands on the hub's top (y = 0.28), not on the plate: the white-filled shape runs from (0, 0.62) down to (0.3, 0.28) and back along y = 0.28, so from x = 0.1 (the hub's right side) to 0.3 it is a tongue floating 0.1 cm (1 mm) above the plate's top (0.18), with a white gap under it (1200 dpi crop). In the scan the fillet sweeps down onto the plate's top. |
| 3 | note | accepted: adopted | $\lvert\vec{U}\rvert$ = 1.1 against $\lvert\vec{V}\rvert$ = 2.2 (fig09.tex:18-22), ratio 0.50 against about 0.51 printed. |
| 4 | note | accepted: adopted | The label now starts inside the rectangle at (0.72, 8.25) with a white knock-out over the dashed side (fig09.tex:23), 0.24 cm right of the diagonal (at y = 8.25 the diagonal is at x = 0.48), as printed. |
| 5 | note | resolved by STYLE.md section 16 | Drawings take their panel letters at the lower right of the panel: (a) at (3.9, 0.1) and (b) at (11.5, 0.1), one baseline. |

## New findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | The plume of (a) is drawn with the pic's default bulge 1.3: it starts at the body's full width and widens to about 1.4 times it (0.16 cm against the 0.12 cm body). In the scan it is narrower than the body (about 3-4 px against 5 px). The rocket is 1.6 cm long, so the difference is under 0.1 cm and the reading (leaving the rod under thrust) is unchanged. Same shape question as Fig 10's plumes (see that report). | fig09.tex:16 (`plume=0.8`); tamrfig.sty `plume bulge` | Optional; if Fig 10's plumes are narrowed, narrow this one the same way. |

## Verdict

pass (0 must-fix, 1 should-fix open: round-1 #2, the fillet's foot floats above the plate; e.g.
`\draw[outline, fill=white] (0,0.6) .. controls (0,0.35) and (0.08,0.18) .. (0.3,0.18) -- (0,0.18) -- cycle;`
placed before the hub, line 12, so the hub box is drawn over the fillet's foot)
