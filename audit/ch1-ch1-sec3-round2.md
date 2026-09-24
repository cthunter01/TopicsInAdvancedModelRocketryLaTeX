# Audit: ch1-sec3 (Chapter 1, Section 3 "Description of the Perturbing Forces"), round 2

## Scope checked

- Scan pages: figures/pages/p073.png through p080.png (PDF 73-80, book pages -43- to -50-),
  one Read call per page. Render pages: build/unit/ch1-sec3-1.png, -2.png, -3.png (built
  2026-09-23 18:26, six seconds after the last edit of chapters/ch1-sec3.tex, so not stale).
- No .tex file was opened. Only occurrence counts of fixed strings (fig08.png, label{ch1:fig:8},
  ref{ch1:fig:8}) were taken in chapters/ch1-sec2b.tex and chapters/ch1-sec3.tex to settle the
  round-1 duplicate question.
- Items checked, each compared word by word / symbol by symbol against the scan (29 in all):
  - 3 headings: "3. Description of the Perturbing Forces" (PDF 73), "3.1 Aerodynamic
    Disturbances" (PDF 75), "3.2 Mechanical Disturbances" (PDF 77): text and numbers match.
  - 7 prose paragraphs, sentence by sentence: Section 3 (1 paragraph, PDF 73-75); Section 3.1
    (3 paragraphs, PDF 75-77: "Aerodynamic effects ...", "Fin flutter ...", "Misaligned fins
    ..."); Section 3.2 (3 paragraphs, PDF 77-80: "Mechanical perturbing forces ...", "Mechanical
    disturbances arising ...", "All the perturbing effects ..."). Wording, sentence order,
    paragraph breaks and emphasis (perturbing forces, weathercocking, gust, periodic, sinusoidal,
    easy, angular frequency) all match.
  - 3 captions, word by word: Figure 8 (PDF 74), Figure 9 (PDF 76), Figure 10 (caption PDF 78,
    six-panel drawing PDF 79; one figure, one image, one caption).
  - 3 inline formulas (Figure 9 caption): vector V, vector U, vector V + (-vector U): arrows,
    plus sign, parentheses and minus sign present.
  - 9 cross-references: Section 2.3, Chapters 2 and 4, Chapter 2 (3.1), Chapter 2 twice (3.2)
    render as "??" (other units, intended); Figure 9, Section 3.1, Figure 10 resolve in the unit.
  - 3 figure placements: Figures 9 and 10 follow the paragraph that first refers to them;
    Figure 8 see below.
  - 0 displayed equations, 0 symbol-list rows in this unit.
  - 1 round-1 discrepancy re-verified (below).

## Round-1 discrepancy: Figure 8 placement (PDF 74) -- resolved

Round 1 asked the fixer to verify that the preceding unit does not also carry Figure 8 and, if it
does not, to leave the figure in this unit and record the decision. Verified in round 2:
- chapters/ch1-sec2b.tex contains 0 occurrences of "fig08.png" and 0 of "label{ch1:fig:8}",
  and 2 of "ref{ch1:fig:8}" (the two "Figure 8" mentions of the boundary paragraph "In Figure 8
  a complete vector diagram ...", which correctly stays in the preceding unit and is absent from
  this render).
- chapters/ch1-sec3.tex contains exactly 1 "fig08.png" and 1 "label{ch1:fig:8}".
- figures/manifest.csv row "ch1-fig08,74,...,ch1-sec3,figures/ch1/fig08.png" assigns the figure
  to owner unit ch1-sec3.
So Figure 8 is included exactly once in the chapter, its number sequence 8, 9, 10 is preserved,
and the render (Figure 8 after the first paragraph of Section 3, caption correct) is the
recorded decision. No further action.

## Observations that are NOT discrepancies (intended per STYLE.md)

- Underlining rendered as italics; "--" rendered as an em dash; typewriter double quotes
  ("fluttering", "rolling", "inputs", "forcing functions", "weathercocks") as curly quotes.
- End-of-line hyphenations rejoined (Weather-/cocking, disturbance-/resistant kept as a real
  compound, Wind-/free kept as a real compound); clipped "othe" at the margin of PDF 75 read as
  "other".
- Placeholder figure boxes; page numbers, running title, line and page breaks differ.

## Discrepancies

none

| where | scan reading | compiled reading | severity |
|---|---|---|---|
