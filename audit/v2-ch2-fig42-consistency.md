# v2 consistency check: ch2/fig42

The issues to resolve:
1. Set $r_o$, $r_i$, $r_t$ and $s$ horizontal beside their arrows, as Fig 38 and Figs 33-36 do, not rotated.
2. Use the house `hidden` style instead of a local definition.
3. Optional, to match the approved Fig 39: end the "Hollow cylinder" and "Planform area of one fin" leaders
   straight at the label, without shelves.

Sources checked:
- figures/v2/ch2/fig42.tex, against the fixer's pre-change copy (scratch `orig/fig42.tex`, diffed line by line).
- Both versions compiled separately in the verify scratch dir. The page was 350.65 x 169.13 pt and is now
  352.40 x 169.13 pt = 4.89 x 2.35 in.
- Renders at 300 and 800 dpi, with crops of the left half and of the fin, $r_o$/$r_i$/$r_t$/$s$ region.
- A red/blue pixel overlay of the old render against the new one.
- `make fig F=ch2/fig42`, which writes build/v2/png/ch2-fig42-compare.png, beside the scan figures/ch2/fig42.png.
- `pdftotext -bbox`, `pdffonts` and the build log.
- Inventory row ch2-fig42, audit/v2-ch2-fig42-round1.md, tamrfig.sty (`hidden`, `\dimline`) and STYLE.md
  section 16.
- For the conventions: fig38.tex:30-33, fig34.tex:26-31 and fig39.tex:23-27.

## Checks

- **(1) Horizontal labels: resolved.** No `rotate` is left in the file.
  - $r_o$ and $r_i$ are upright above the tails of their upper arrows (`anchor=south`, both tails at y = 38),
    on one baseline. The arrows moved apart (x 497 to 495, and 516.5 to 520), so the labels are 7.4 pt apart
    and each sits squarely over its arrow.
  - $r_t$ hangs under the tail of its lower arrow (`anchor=north`, tail at -30). This is Fig 38's $r_r$ and
    $d_{\max}$ form. It is centred on the arrow: 333 pt, against 329.1-335.7 pt.
  - $s$ is a plain `\dimline` with the label upright in the gap, as Figs 33-36 do. It moved from x 552.5 to
    557.
  - $r_t$ and $s$ are 8.6 pt apart. Each clearly belongs to its own vertical line.
- **The dimensions are unchanged in what they measure.**
  - $r_o$ runs to the outer wall (13.5) and $r_i$ to the bore (11).
  - $r_t$ runs from the centre line to the fin root (13.5).
  - $s$ runs from the root to the tip (-13.5 to -72). Its extension lines were lengthened to 567.
  - $c_t$ and $c_r$ are untouched.
- **(2) House style: resolved.** The local `hidden` is gone, and only `dim arrow` stays local. The house
  `hidden` is identical to the old one, and the overlay shows the bore lines pixel-identical.
- **(3) Leaders: done, and they read at least as well.**
  - "Hollow cylinder": (220,13.5)--(245,54), ending 1.5 pt to the left of the "H" at mid x-height, with no
    shelf. The label moved 2 units left.
  - "Planform area of one fin $= A_f$": the long elbow and its shelf back to "Planform" are replaced by one
    straight leader. It runs from the bottom centre of the third line (`pf3.south`) to (452,36) inside the
    upper fin.
    - It crosses the leading edge about 75% of the way out from the root, about 4 mm clear of the tip corner.
      This is further out than the fixer's "about midway", but still well clear of the corner.
    - It no longer passes the $r_o$/$r_i$ labels, and it crosses no lettering.
    - It is shorter and more direct than before.
  - The "$R$ of ellipsoidal nose" and "$R$ of solid cylinder" lines keep their short tick to the name. These
    are dimension lines carried up to their names, as printed, and were not part of issue 3.
- **No regressions.**
  - The overlay shows the rest of the figure pixel-identical. That covers:
    - the nose, shoulder, tube and fins;
    - both $R$ dimensions;
    - the $c_t$ and $c_r$ dimensions;
    - the "Planform" label block, which keeps its position.
  - The extracted text is the same multiset before and after: all ten inventory lettering items. $r_o$ and
    $r_i$ stay lowercase (rule 2), and $A_f$ is unchanged.
  - Nothing is clipped. The width is within 6.5 in, all fonts are embedded, and the log has no warnings.
  - The repository PDF matches a fresh compile of the current source.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | The inventory lettering column still lists $r_o$, $r_i$, $r_t$ and $s$ as "(rotated)", and round 1 says "labels rotated" and "label rotated in the gap". Both describe the 1973 lettering. The redraw now sets all four horizontal, as the consistency review decided. | figures/v2/inventory.csv row ch2-fig42 | Optional, for the orchestrator: note "set horizontal (consistency pass)" in the inventory row. It is outside this group's files. |
| 2 | note | Round 1 note 1 still stands, unchanged by this pass. The lower $r_o$ and $r_i$ arrows start at y = -12, 1.5 units above the $r_t$/$s$ extension line at -13.5. | fig42.tex:43,45 | Optional, as in round 1: start them at -10. |

## Verdict: pass

Issues 1 and 2 are resolved as asked, and the optional issue 3 is done with leaders that read at least as
well. Nothing regressed against the scan, the inventory or round 1.
