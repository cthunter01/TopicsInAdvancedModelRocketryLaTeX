# M5 audit: Figure Credits, round 1, part 1 (scan PDF 655-659)

Compared the scan page images with the unit render only; no .tex file was opened.

## Sources compared

- Scan: figures/pages/p655.png, p656.png, p657.png, p658.png, p659.png (printed pages -623- to -627-).
- Zoomed crops (300 dpi): build/zoom/audit_back-credits_r1_p1-{p655fig10,p657fig39,p657note,p659fig51,p659ch3a,p659ch3b}-*.png.
- Render: build/unit/figure-credits-1.png, -2.png, -3.png (my content), plus -4.png (the page after).
- Reference targets: the undefined-reference list in build/unit/figure-credits.log, checked against the chapter labels (grep of `\label` in chapters/*.tex). The standalone build prints every number as "??", so the log is the only way to check the numbers.

## Items checked

- Heading "Figure Credits" (label `credits` present in the .aux).
- Subheadings "Chapter 2" and "Chapter 3" (underlined in the scan, set as unnumbered section headings; labels `credits:ch2` and `credits:ch3` present).
- Chapter 2: Figures 10-51 (42 entries) and Plate 1. Chapter 3: Figures 2, 3, 4, 6, 7, 8, 9, 13, 14 and 15. Checked for each entry:
  - the figure or plate word, and the reference label (ch2:fig:10 ... ch2:fig:51, ch2:plate:1, ch3:fig:2/3/4/6/7/8/9/13/14/15), in printed order. All of these labels exist in the chapters.
  - the author form (Figure 10: "G.K. Mandell"; the others: "Mandell"; "J.S. Barrowman"; "H. Schlichting").
  - the emphasis. \emph is used for *Model Rocketry* and *Boundary Layer Theory*. "Magazine" in Figure 10 and "U.S. Standard Atmosphere" are not underlined in the scan and are roman in the render.
  - the month and year of every Model Rocketry entry:
    - Oct. 1968: Figures 10-25
    - Nov. 1968: Figures 26-31
    - Jan. 1969: Figures 37-42
    - Apr. 1969: Figure 43 (as printed)
    - Feb. 1969: Figures 44-47
    - Mar. 1969: Figures 48-51
  - the text "by permission of Model Rocketry, Inc.".
  - the copyright line "copyright © 1968 by McGraw-Hill, Inc., Sixth Edition, by permission of McGraw-Hill Book Company".
- The Figure 32 asterisk ("author*)"), and the asterisk note checked word by word:
  - the underlined thesis title, *The Practical Calculation of the Aerodynamic Characteristics of Slender Finned Vehicles*, is italic up to "Vehicles";
  - "M.S.A.E. Thesis, March 1967";
  - both quoted titles, with the comma outside the closing quote as typed;
  - "NASA/Goddard Space Flight Center information pamphlet";
  - "TIR-33";
  - "Douglas J. Malewicki";
  - "copyright © 1968 by Space Graphics Division of Centuri Engineering Company, Inc."
- Plate 1: "(Prints by J. Nickerson from motion pictures by G. Mandell)".
- Paragraph breaks: one paragraph per entry, and the note is a separate paragraph after Figure 32.
- Entry count per render page, matched against the scan: render p1 = Figs 10-31 (22 entries); render p2 = Fig 32 to Ch. 3 Fig 3; render p3 = Ch. 3 Figs 4-15, then content for the part-2 auditor.

## Observed silent slip fix (not a discrepancy)

- Figure 39 (scan p657, printed -625-): the scan reads "Jan. 1969 by permission", with no comma after 1969 (confirmed in a zoomed crop). The render reads "Jan. 1969, by permission", the same as the other 41 Model Rocketry entries. This is an obvious typing slip, fixed silently, which the conventions allow. It is recorded here so that the transcriber's slip list can include it.

## Discrepancies

none
