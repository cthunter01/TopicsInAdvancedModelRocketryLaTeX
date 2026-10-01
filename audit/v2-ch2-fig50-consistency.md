# v2 consistency check: ch2/fig50

Issue: the circled letters a-f used a local `circled` style (12.5pt circle, 0.5pt rule, `\small\itshape`). That
made them larger, heavier and italic compared with the house `curve tag` used by Fig 10 and the approved Ch3 Fig 22.
The fix was to switch to `curve tag`, keep the lowercase letters (standing rule 2) and delete the local style.

Sources checked:
- figures/v2/ch2/fig50.tex (current), and the pre-fix source the fixer saved in the scratch directory
  (`fig50.orig.tex`).
- A fresh compile in the scratch directory, with no warnings. Its 300 dpi raster is identical to that of the
  repository's figures/v2/ch2/fig50.pdf, so the built PDF is current.
- build/v2/png/ch2-fig50-compare.png and the scan figures/ch2/fig50.png.
- Round 1, inventory row ch2-fig50, and corrections/v2-figures.md (standing rule 2, and the Chapter 2 entry
  "Fig 50 / Fig 43 circled letters: one form for both").
- tamrfig.sty `curve tag`, and the tags of figures/v2/ch2/fig10.tex and ch3/fig22.tex.

## Checks

- **The issue is resolved.** The source diff against the pre-fix file has three parts:
  - the `circled` key is deleted from the `\tikzset` block, leaving only `note`;
  - `\tagnote` now sets `\node[curve tag] at (#1,#2) {#3};`;
  - the header comment is updated.

  No `circled/.style` remains anywhere under figures/v2. The six letters are still lowercase a-f, at their
  round-1 positions.
- **Form matches the house tag.**
  - At 600 dpi all six circles measure 95 x 95 px, the same as the Fig 10 tags.
  - The old circles measured 108-109 px.
  - The letters are upright. The TeXGyreTermesX-Italic font is gone from the PDF.
  - A side-by-side crop of these tags and the Fig 10 tags shows the same form.
- **No regressions.** I compiled the old and new sources with the same fixed bounding box, rendered both at
  600 dpi and diffed them:
  - Six regions differ, each the 17.9pt square around one tag.
  - Outside the regions the ink totals are equal (229232 dark pixels in both).
  - A seventh, tiny difference is the $\zeta$ of note (e). pdftotext places it 0.001pt (0 to 0.009pt across
    note (e)) from where it was. The likely cause is pdfTeX's relative text positioning, now that the tag font
    has changed. At 600 dpi this moves the glyph's raster by 0.7 px, which cannot be seen and is not a
    regression.
  - The rockets, fins, C.G. and C.P. marks are unchanged, including the order (C.P. ahead only in (d)).
- **Notes.** All six notes match the inventory word for word (checked with pdftotext).
- **Page size.** 372.08 x 419.69 pt. That is 0.8pt shorter than round 1, because the smaller *a* and *b*
  circles set the top edge.
- **Placement against the scan.** Each letter sits centred above its rocket, as printed, on one baseline per
  row.
- **Clipping and overlaps.** None:
  - The top circles' full 0.4pt rule is inside the page; they are flush with the top edge, as before.
  - Every tag sits in empty space well clear of its rocket's fins, so the white fill covers nothing.

Note (pre-existing, not part of this issue): the comment above the macro, fig50.tex:36, still names it
`\tag{...}`, but the macro is `\tagnote`. The fix is a one-word comment change, at the owner's discretion.

## Verdict: pass
