# Audit ch2-sec3c, round 2, part 2 (scan PDF 181-193)

## Scope and counts

I read each scan page, figures/pages/p181.png through p193.png, in its own Read call. On p193 I
checked only the part above the 3.2.2 heading. I also made zoomed 300 dpi crops of the scan,
saved as build/zoom/audit_ch2-sec3c_r2_p2-*. They cover:

- p182: (56a) and (56b)
- p184: the "Multiplying alpha_Y0 ..." bracketed equation and the A_1 cos phi_1 fraction
- p185: (58a)
- p189: the squared inequality

Render pages checked: build/unit/ch2-sec3c-07.png through -15.png.

- Page 7 is the seam page and holds only p180 material.
- My content starts at "so that if omega_Z > 0," on render page 8.
- It ends with "for any model rocket, rolling or not." on render page 15, the last page of the unit.

Verification of the round-1 findings:

- PDF 181, "Thus A and B are the physical roots ...": the paragraph is now flush left and
  continues after the display, with no indent. This matches the scan (render page 8). Fixed.
- PDF 189, the squared inequality: the render now prints "- F . I_R^2 omega_Z^2/I_L^2" with a
  multiplication point after the script F. This matches the scan (render page 14). Fixed.

Items checked again in full:

- Headings: 0 in range. The 3.2.2 heading on p193 belongs to the next unit, and the render
  correctly leaves it out.
- Numbered equations: 11, all present and in sequence. They are (55), (56a), (56b), (57a),
  (57b), (58a), (58b), (59a), (59b), (60a) and (60b). The standalone build shows no offset in the
  numbering. I checked each one symbol by symbol: radicals and what they cover, fraction bars,
  brackets, subscripts, superscripts, signs, and the two-row numerator and denominator of (58a).
- Unnumbered displays: 32, checked symbol by symbol.
  - p181: 3
  - p182: 2
  - p183: 4
  - p184: 5
  - p185: 1
  - p186: 2
  - p187: 1
  - p189: 4
  - p191: 3
  - p192: 5
  - p193: 2
- Inline formulas: about 60, all matching.
- Cross-references: (51) 4 times, (55) 3 times, (59) twice, and Figures 26 and 27.
- Captions: 2, checked word by word (Figure 26, p188; Figure 27, p190). I did not audit the
  artwork. Both captions render at the same line pitch.
- Prose: about 25 paragraphs, checked sentence by sentence for wording, emphasis and paragraph
  breaks. I checked the indentation after every display. All underlined emphasis is rendered as
  italics.
- Editorial footnotes and draft notes: none on these render pages.
- Accepted and not reported:
  - p183: the missing closing parenthesis in the second right-hand row of the first bracketed
    equation is silently fixed. This is an obvious slip.
  - p183: I read the faint specks as specks, not symbols. This is unchanged from round 1.

## Discrepancies

| where | scan reading | compiled reading | severity |
|---|---|---|---|

none
