# M5 audit: Historical Perspective (front matter), round 1

Unit: "Historical Perspective" (\chapter, label front:historical).
Scan pages: PDF 5-6 (figures/pages/p005.png, p006.png; zoomed crops
build/zoom/audit_front-historical_r1-p005a/p005b/p006a). The scan's embedded text
layer (DejaVu Sans, born digital) was used as a second check.
Render: build/unit/historical-perspective-1.png, -2.png (plus pdftotext of
build/unit/historical-perspective.pdf for a word-by-word diff).

## Items checked

- Heading "Historical Perspective": unnumbered \chapter. The label front:historical is present in the .aux.
- All seven paragraphs, checked word by word against the images and then diffed
  automatically against the scan's text layer: "Annual conventions...", "The idea for...",
  "The MIT Press published...", "To bring...", "When *Topics* was first published..."
  (runs on across the page break through "...printing the output."), "Today large sport
  rockets...", "As we look back...".
- Paragraph break at the page boundary (p005 "…bulky by modern standards." / p006
  "Model rocket instruments…"): in the scan's text layer the last line on p005 ends with the
  two spaces that follow a sentence inside a paragraph. Every paragraph-final line in the
  unit has no trailing space. So the paragraph continues across the page break, and the
  compiled text is right to run it on as one paragraph.
- Emphasis: *Topics in Advanced Model Rocketry* (paragraphs 2, 3, 4) and *Topics* (once in
  paragraph 2, three times in paragraph 3, once in paragraph 5). All nine italic spans match, and no other text is italic.
- Numbers and names: 1966, 1968, 1973, 1980, 1986, 2003, 2017, 2025 (x2), 454 grams, 113 grams,
  170 seconds, 80 seconds, F (80 newton-seconds maximum), 100 kilograms, O (40,960
  newton-seconds maximum), 224 seconds, 10,000 meters, 100 kilometers, 1960s, 1970s,
  1960s-vintage; Chapters 2, 3, and 4 / Chapter 1 (\ref, "??" in the standalone build, allowed);
  MITMRS, NAR, Christopher Feyerchak, George Caporaso, Hollerith, Winchester, Kármán,
  Fédération Aéronautique Internationale, GPS.
- Compounds whose hyphen falls at a line end in the scan are kept correctly: newton-seconds,
  model-rocket-mounted, high-resolution. Both "on-board" and "Onboard" are kept as printed.
- Quotes and apostrophes: “Classic”, “edge of space”, Press’, authors’.
- Date "January 12, 2025" and the three-line signature (William P. Bengen / George J. Caporaso /
  Gordon K. Mandell) match. The date and signature blocks are separate, as printed.
- Links: the labels ch1-ch4 and supp exist in the project, so the \ref/\hyperref targets resolve in the full book.
- No formulas, tables, figures or editorial notes in this unit.

## Silent typing-slip fix (allowed, not a discrepancy)

- p006, paragraph "Today…": the scan has "state-of-the art". The compiled text has "state-of-the-art".

## Discrepancies

none
