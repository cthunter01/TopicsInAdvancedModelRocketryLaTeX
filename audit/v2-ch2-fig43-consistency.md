# v2 consistency check: ch2/fig43

Issue: the circled panel letters used a local `circled` style (12.5pt circle, 0.5pt rule, `\small\itshape`). That
made them larger, heavier and italic compared with the house `curve tag` used by Fig 10 and the approved Ch3 Fig 22.
The fix was to switch to `curve tag`, keep the lowercase letters (standing rule 2) and delete the local style.

Sources checked:
- figures/v2/ch2/fig43.tex (current), and the pre-fix source the fixer saved in the scratch directory
  (`fig43.orig.tex`).
- A fresh compile in the scratch directory, with no warnings. Its 300 dpi raster is identical to that of the
  repository's figures/v2/ch2/fig43.pdf, so the built PDF is current.
- build/v2/png/ch2-fig43-compare.png and the scan figures/ch2/fig43.png.
- Rounds 1 and 2, inventory row ch2-fig43, and corrections/v2-figures.md (standing rule 2, and the Chapter 2
  entry "Fig 50 / Fig 43 circled letters: one form for both").
- tamrfig.sty `curve tag`, and the tags of figures/v2/ch2/fig10.tex and ch3/fig22.tex.

## Checks

- **The issue is resolved.** The source diff against the pre-fix file has three parts:
  - the local `\tikzset{circled/.style=...}` is deleted;
  - both nodes changed from `circled` to `curve tag`. Each keeps its `anchor=south east` and its point
    ((165,-644) and (164,-644)), so the letters stay on one baseline;
  - the header comment is updated.

  No `circled/.style` remains anywhere under figures/v2. The letters are still lowercase *a* and *b*.
- **Form matches the house tag.**
  - At 600 dpi both circles measure 95 x 95 px. That is 11pt plus the 0.4pt rule, the same as every Fig 10
    tag (95 px).
  - The old circles measured 109 px.
  - The letters are upright. The PDF now embeds only TeXGyreTermesX-Regular; the round-2 PDF used
    TeXGyreTermesX-Italic for these two letters.
  - A side-by-side crop of these tags and the Fig 10 tags shows the same form.
- **No regressions.** I compiled the old and new sources with the same fixed bounding box, rendered both at
  600 dpi and diffed them:
  - Exactly two regions differ, each the 17.9pt square around a tag.
  - Outside those regions the ink is identical, pixel for pixel (130213 dark pixels in both).
  - So the beam, clamp, screw, upper T, wire, both rockets, tape bands, lower T and separating rule are
    unchanged from round 2.
- **Page size.** 327.77 x 428.98 pt. That is 0.23pt narrower than round 2, because the smaller *b* circle
  sets the right edge.
- **Inventory lettering.** "circled a ; circled b (no other lettering)": the PDF's text is exactly "a b".
- **Placement against the scan.** Each letter sits at the lower right of its panel, as printed.
- **Clipping and overlaps.** None:
  - The *b* circle's full rule is inside the page; it is flush with the right edge, as the old circle was.
  - The *a* circle is 2.9 mm clear of the separating rule.
  - Both tags sit 1 mm above the bottom edge, in empty space, so the white fill covers nothing.

## Verdict: pass
