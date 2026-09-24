# Audit: ch3-refs, round 1

## 1. What was checked

- Scan pages: figures/pages/p527.png (printed -495-) and figures/pages/p528.png (printed -496-). I also looked at
  300 dpi zoomed crops of both pages (build/zoom/audit_ch3-refs_r1-p527{a,b,c}-527.png and
  build/zoom/audit_ch3-refs_r1-p528{a,b}-528.png) to check underline extents, punctuation and digits.
- Render: build/unit/ch3-refs-1.png and build/unit/ch3-refs-2.png, plus the unit's aux file for its labels.
- Items: 1 heading ("REFERENCES", set as the unnumbered "References", label ch3:sec:refs present) and 20 numbered
  entries (1-11 on PDF 527, 12-20 on PDF 528), labels ch3:ref:1 to ch3:ref:20 present and numbered 1-20 in order.
  There are no equations, inline formulas, figures, tables, captions or footnotes on these pages.
- Survey (build/ch3-notes/ch3-refs.md): "REFERENCES (printed p.495): entries 1-11 on p527 and 12-20 on p528, 20 in
  all" matches the scan.
- For each entry I checked, word by word: author names and initials, commas (including the missing comma after
  "Charles E." in entry 4, which the render keeps), the extent of the underlining against the italics (entry 1 ends at
  "Charts"; entry 3 includes "0 to 5"; entry 6 includes "Datcom"; entry 8 includes the colon and "A General Review of
  Progress"; entries 12-13 include the "Hydro- and" with its suspended hyphen; entry 17 includes the colon; entry 19 is
  underlined through "1962"; entry 20 underlines only "Model Rocketry"), report numbers and digits (TIR-33, 4363,
  CP-10, D-4821, 148 Busteed Drive, TIR-100, D-3337), dates, the typed capital in "Prepared" (entry 6), "(Ed.)",
  "4th Edition", and the quotation marks with the comma after them in entry 20.

## 2. Discrepancies

none

Note, not counted as a discrepancy: entry 8 prints the volume range "Volumes I - VI" (a spaced typewriter hyphen) and
the render sets "Volumes I–VI" (an en dash without spaces). The range is unchanged. This is the same kind of
typographic normalisation as "--" becoming an em dash.
