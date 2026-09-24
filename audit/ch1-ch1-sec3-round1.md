# Audit: ch1-sec3 (Chapter 1, Section 3 "Description of the Perturbing Forces"), round 1

## Scope checked

- Scan pages: figures/pages/p073.png through p080.png (PDF 73-80, book pages -43- to -50-),
  one Read call per page.
- Render pages: build/unit/ch1-sec3-1.png, ch1-sec3-2.png, ch1-sec3-3.png.
- Items checked (each compared word by word / symbol by symbol against the scan):
  - 3 headings: "3. Description of the Perturbing Forces" (PDF 73), "3.1 Aerodynamic
    Disturbances" (PDF 75), "3.2 Mechanical Disturbances" (PDF 77) - text and numbers match.
  - 7 prose paragraphs, sentence by sentence: Section 3 (1 paragraph, PDF 73-75), Section 3.1
    (3 paragraphs, PDF 75-77), Section 3.2 (3 paragraphs, PDF 77-80). Wording, sentence order,
    paragraph breaks and emphasis all match.
  - 3 captions, word by word: Figure 8 (PDF 74), Figure 9 (PDF 76), Figure 10 (caption PDF 78,
    drawing PDF 79; rendered as one figure with one image and one caption, as instructed).
  - 3 inline formulas (all in the Figure 9 caption): vector V, vector U, vector V + (-vector U);
    arrows and minus sign present.
  - 0 displayed equations, 0 symbol-list rows in this unit.
  - Cross-references: "Figure 9", "Figure 10" and "Section 3.1" resolve within the unit;
    "Section 2.3", "Chapter 2", "Chapter 4" render as "??" (other units), as intended.
- The paragraph "In Figure 8 a complete vector diagram ..." at the top of PDF 73 precedes the
  Section 3 heading and is correctly NOT part of this unit.

## Observations that are NOT discrepancies (intended per STYLE.md)

- Underlined "free-body diagram" (previous unit), "perturbing forces", "weathercocking", "gust",
  "periodic", "sinusoidal", "easy", "angular frequency" rendered as italics.
- "--" in "local wind phenomena -- all of which" rendered as an em dash.
- Typewriter double quotes ("fluttering", "rolling", "inputs", "forcing functions",
  "weathercocks") rendered as curly quotes.
- End-of-line hyphenations rejoined (Weather-/cocking); real compounds kept (disturbance-resistant,
  Wind-free, roll-coupled, blow-through/ignition, point-mass, rigid-body).
- Placeholder figure boxes; page numbers, running title and line/page breaks differ.

## Discrepancies

| where | scan reading | compiled reading | severity |
|---|---|---|---|
| PDF 74, Figure 8 (whole figure environment); first reference is the paragraph "In Figure 8 a complete vector diagram ..." at the top of PDF 73, which precedes the "3." heading | Figure 8 is first referred to in the paragraph that belongs to the preceding unit (STYLE.md section 2: boundary paragraph belongs to the unit whose heading precedes it; section 7: figure goes right after the paragraph that first refers to it) | Figure 8 (placeholder + caption) is placed inside this unit, after the first paragraph of Section 3; caption text itself is correct. Verify the preceding unit does not also carry Figure 8 (duplicate would shift Figures 9 and 10 in the chapter build); if it does, remove it here, otherwise leave and record the decision | layout |
