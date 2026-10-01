# v2 consistency check: ch2/fig33

Issue: the dimension labels (2/3 L, .466L, 1/2 L, 1/3 L, L) were reported as sitting beside the vertical
dimension lines, where every other drawing uses `\dimline` with the label in a gap at the middle of the line
(as Figs 34 and 35 do for L).

Sources checked:
- figures/v2/ch2/fig33.tex:1-54, rebuilt with `make fig F=ch2/fig33` (4.77 x 2.36 in, 343.641 x 170.205 pt, the
  same as round 2). Rendered at 300 and 1200 dpi.
- build/v2/png/ch2-fig33-compare.png and the scan figures/ch2/fig33.png.
- The round-1 and round-2 audits, inventory row ch2-fig33, and the Chapter 2 Fig 33 entry in
  corrections/v2-figures.md.
- tamrfig.sty `\dimline` and `dimension`, and figures/v2/ch2/fig34.tex:31 and fig35.tex:32 (L).

## Checks

- **The issue: already resolved before this pass.** All five dimensions are drawn with `\dimline`, with no
  options:
  - the four C.P. dimensions through `\cpdim` (fig33.tex:27);
  - L on (d) (fig33.tex:52).

  The 1200 dpi render shows each label centred on its line, in a white gap that breaks the line, with the line
  and an arrowhead visible above and below the label. Centring, measured on the render:

  | label | label centre (px) | line (px) |
  |---|---|---|
  | .466L | about 317 | 315 |
  | 2/3 L | about 135 | 128 |

  This is the same form as the L in Fig 34.

  The report most likely came from the scan (where .466L does sit beside its line) or from the low-resolution
  compare image.

- **The figure is unchanged.** I did not run git, so I checked the modification time instead:
  - fig33.tex was last modified at 17:53:27, the time the round-2 audit recorded.
  - The four CSVs were last modified at 17:46.
  - The rebuilt PDF has the same page size as in round 2.

  This agrees with the fixer's report that the file was not edited.

- **No regressions** against the scan, the inventory row and rounds 1-2:
  - **Lettering:** all of it is present and exact: 2/3 L, .466L, 1/2 L and 1/3 L (stacked fractions), four
    C.P.$_n$, L on (d) only, (a)-(d) in italic, and Conical, Tangent ogive, Paraboloidal, Ellipsoidal on one
    baseline.
  - **C.P. marks:** at 2/3, .466, 1/2 and 1/3 L from the tip.
  - **Centre lines:** drawn under the outlines (the round-1 fix still holds), with the tips solid black.
  - **Extension lines:** they reach the tip and C.P. rows.
  - **Overlaps and clipping:** none. The leftmost label (2/3 L) sits inside the page edge. The .466L label is
    clear of the cone in (a).
  - **Fonts:** all embedded.

## Verdict: pass

There is nothing to fix, and the figure is unchanged since round 2.
