# v2 consistency check: ch3/fig31

The two issues in this pass are:
1. the round-bar break should be redrawn as `\breakline`;
2. labelled velocity arrows should be `vec`.

Fig 31 was not named in either issue. I checked that neither applies.

Sources checked:
- figures/v2/ch3/fig31.tex and figures/v2/ch3/fig31.pdf. The .tex is dated 21:57:55 and the PDF 21:57:56, both
  earlier than this pass's edits (23:12 onwards). The PDF measures 399.848 x 304.503 pt = 5.55 x 4.23 in, the same
  as round 1, and all fonts are embedded. I rendered it at 300 dpi.
- The scan figures/ch3/fig31.png.
- The round-1 audit.

## Checks

- **Issue 1 does not apply.** The twelve icons are free-standing nose cones and stubs, each closed by a square
  base line, as on the scan. None is a body tube broken off, and the scan shows no break symbol. fig31.tex has no
  `\breakline` and needs none.
- **Issue 2 does not apply.** The figure is a table with icons. It has no flow or velocity arrow, either on the
  scan or in fig31.tex.
- **No regression.** The file was not edited in this pass. The render still matches round 1:
  - the booktabs table;
  - all twelve rows of values, including 0.43 (0.70) and 2.15 (2.35) [2.76];
  - the icons pointing right, on one diameter.

## Findings

None.

## Verdict: pass (neither issue applies; unchanged since round 1)
