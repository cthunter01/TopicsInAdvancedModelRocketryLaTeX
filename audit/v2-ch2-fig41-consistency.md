# v2 consistency check: ch2/fig41

The issues to resolve:
1. Set $R$, $R_o$ and $R_i$ horizontal beside their arrows, as Fig 38 and Figs 33-36 do, not rotated.
2. Use the house `phantom` style (`draw=ink2`, context only) and the house `hidden` style instead of local
   definitions, with the same visual meaning.
3. Optional, to match the approved Fig 39: end the "Solid cylinder" and "Hollow cylinder" leaders straight at
   the label, without shelves.

Sources checked:
- figures/v2/ch2/fig41.tex, against the fixer's pre-change copy (scratch `orig/fig41.tex`, diffed line by line).
- Both versions compiled separately in the verify scratch dir. Both have the same page size,
  364.709 x 138.644 pt = 5.07 x 1.93 in.
- Renders at 300 and 800 dpi, with crops of the left end (nose, payload, $R$) and the right end (casing, fins,
  $R_o$/$R_i$).
- A red/blue pixel overlay of the old render against the new one.
- `make fig F=ch2/fig41`, which writes build/v2/png/ch2-fig41-compare.png, beside the scan figures/ch2/fig41.png.
- `pdftotext -bbox`, `pdffonts` and the build log.
- Inventory row ch2-fig41, audit/v2-ch2-fig41-round1.md, tamrfig.sty (`phantom`, `hidden`, `dimension`) and
  STYLE.md section 16.
- For the conventions: fig38.tex:30-33 (labels at the arrow tails, horizontal) and fig39.tex:23-27 (straight
  leaders to `anchor=west`).

## Checks

- **(1) Horizontal labels: resolved.**
  - $R$, $R_o$ and $R_i$ are now upright nodes (`anchor=south`) at the tails of their upper outside arrows. All
    three tails are at y = 30, so the labels share one baseline. No `rotate` is left in the file.
  - This is Fig 38's form (a label at the arrow tail), set above the tail instead of below it.
  - Each label is centred on its arrow: $R_o$'s centre is at 338.3 pt, against its arrow at 338.4 pt.
  - $R_o$ and $R_i$ are 8.5 pt (3 mm) apart (343.5 to 352.0 pt), so each reads with its own arrow.
  - $R$ clears the C.G.$_{cs}$ extension line by about 1.5 mm and the $\bar W_{cs}$ line by about 10 pt.
- **The dimensions are unchanged.**
  - $R$ still runs from the centre line to the payload's top (y = 11), at x = 108.
  - $R_o$ (x 546 to 543) and $R_i$ (x 569 to 573) moved a little apart, and their extension lines were
    lengthened to 547 and 577. They still reach the outer wall (11) and the bore (7.25).
  - The lower arrows are unchanged (-13 to 0). $R_i$'s upper arrow is 3.75 units longer.
- **(2) House styles: resolved.**
  - The local `phantom` and `hidden` definitions are gone; only `dim arrow` and `\dimoutv` stay local.
  - The tube and fins use `phantom, draw=ink2`. The 0.6pt line width replaces the old 0.55pt, and the dash
    pattern is unchanged.
  - The bore uses the house `hidden`, which is identical to the old local style.
  - At 800 dpi the phantom lines still clearly differ from the lighter dash-dot centre line: one long dash
    and two short against one long dash and one short.
- **(3) Leaders: done, and they read at least as well.**
  - "Solid cylinder": (127,11)--(152,50), ending at the label's west point at mid-height. The label moved
    3 units left.
  - "Hollow cylinder": (436,11)--(417,56). It ends 1.5 pt to the right of the "w" of "Hollow", at the middle
    of its x-height. The label moved 3 units right.
  - Neither leader has a shelf, so both match the approved Fig 39. Neither crosses any lettering.
- **No regressions.**
  - The overlay shows the rest of the figure pixel-identical. That covers:
    - the nose, shoulder, payload and casing;
    - the four $\bar W$ dimensions;
    - $L_{cs}$ and $L_{ch}$;
    - the four C.G. marks and their leaders.
  - The only differences are the changes above and the thicker phantom lines.
  - The extracted text is the same multiset before and after: all 15 inventory lettering items, with cs/ch
    subscripts and $R_i$ as printed (rule 2).
  - Nothing is clipped. The page's right edge (364.7 pt) clears $R_i$ (360.5 pt) and C.G.$_{ch}$.
  - The width is within 6.5 in, all fonts are embedded, and the log has no warnings.
  - The repository PDF matches a fresh compile of the current source.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | The inventory lettering column still lists $R$, $R_o$ and $R_i$ as "(rotated)", and round 1 says "labels rotated". Both describe the 1973 lettering. The redraw now sets them horizontal, as the consistency review decided. | figures/v2/inventory.csv row ch2-fig41 | Optional, for the orchestrator: note "set horizontal (consistency pass)" in the inventory row. It is outside this group's files. |

## Verdict: pass

Issues 1 and 2 are resolved as asked, and the optional issue 3 is done with leaders that read at least as
well. Nothing regressed against the scan, the inventory or round 1.
