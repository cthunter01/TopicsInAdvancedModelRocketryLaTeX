# v2 audit: ch3/fig39 (consistency pass, verification)

Issue checked: mixed vector lettering across the chapter. Fig 39 set $\bar{U}$ while Ch1 Fig 6, Ch3 Figs 11 and 38
and the Symbols list use $\vec{}$. Suggested fix: $\vec{U}$ at fig39.tex:43.

Sources checked:
- figures/v2/ch3/fig39.tex and .pdf (the .pdf is newer than the .tex). `make fig F=ch3/fig39` gives 5.17 x 6.25 in
  (371.9 x 450.2 pt), with fonts embedded.
- A 400 dpi render, plus the scan figures/ch3/fig39.png zoomed 16x on the U.
- Inventory row ch3-fig39 and the round-1 audit (audit/v2-ch3-fig39-round1.md).
- Caption chapters/ch3-sec5a.tex:372-383.
- The book's vector notation: ch3-symbols.tex:106 ($\vec{V}$ vector velocity), ch3-sec8.tex:137 (eq. (222),
  $d\vec{U}/dt$), ch1-sec3.tex:53-55 ($\vec{U}$ wind), ch1/fig06.tex, ch3/fig11.tex, ch3/fig38.tex.
- STYLE.md s14 and s15 "Vectors".
- Regression test: the current .tex and a copy with only `\vec{U}` changed back to `\bar{U}`, both compiled in
  scratch with one fixed bounding box and diffed pixel by pixel at 400 dpi.

## Resolution

Resolved. fig39.tex:44 now sets `$\vec{U}$`; the node, its anchor and its position are unchanged. The header
(lines 5-6) records that the 1973 letter is U-bar and is set as $\vec{U}$ in the book's vector notation. At 16x the
1973 accent is a plain overbar with no barb, so the header describes it correctly. Figs 1 and 12 were switched in
the same pass (fig01.tex:26-27 $\vec{V}$, $\vec{D}$; fig12.tex:81 $\vec{V}$). No Chapter 3 figure source now
contains `\bar` or `\overline`, so the chapter uses one vector style.

## Regression check

| check | result |
|---|---|
| Drawing | The two fixed-bbox renders differ in 170 pixels, all inside a 25 x 12 px box at the accent. The U glyph, the flow arrow, the wing, the helices, the rings and all of panel (b) are pixel-identical. |
| Source | Diffed against the drafter's 22:15 copy. The only changes are the U accent and header comments; fig39.py, the CSVs and the calib are unchanged (22:15-22:16). |
| Digitized data | `digitize.py overlay` re-run on all 11 CSVs. Tips 2-6 are 95% within 0-1 px (max 1 px); cores 1-6 are 95% within 2 px (max 2.2-3.0 px); all ok. These are the same as round 1. |
| Size | The page is 1.5 pt taller (448.7 -> 450.2 pt) because the arrow accent is now the topmost ink. At 400 dpi the accent ends about 0.6 mm below the page edge and 0.7 mm from the flow arrow, with no clipping or contact. |
| Placement vs scan | The label sits above and right of the flow arrow's midpoint, as in 1973. |
| Inventory / round 1 | All other lettering still matches the inventory row (tip numbers, $y$, the six $\Delta\AR$ labels with = and $\cong$, (a), (b)). The round-1 notes (findings 1-6) still hold. |

## Findings
| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | This departs from the printed letter, because the 1973 accent is an overbar. STYLE s14 ("\vec{} wherever an arrow is drawn; a letter printed without an arrow stays plain") does not cover a printed overbar. STYLE s15 says "The overbars of Figure 1 stay in the artwork" for Ch4 Fig 1, and the inventory flags that figure "choose one form". The orchestrator should record a single gate item covering Ch1 Fig 6, Ch3 Figs 1, 11, 12, 39 and Ch4 Fig 1, with a one-line revert for each. | fig39.tex:44 | orchestrator: corrections/v2-figures.md Ch3 gate item; inventory ch3-fig39 lettering still reads $\bar{U}$ |

## Verdict: pass (issue resolved, no regression)
