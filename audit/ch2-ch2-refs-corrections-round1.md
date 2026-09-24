# Audit: ch2-refs corrections (item 10), round 1

## Sources compared

- Diff: `git diff HEAD -- chapters/ch2-refs.tex` (2 hunks, 2 insertions, 1 deletion): the header
  comment and one new `\item` after Reference 11.
- 2022 correction: figures/pages/p686.png ("[Add Reference 12 to the List of References on Page 259:]"
  and the typed entry 12; signed Gordon K. Mandell, February 15, 2022).
- 1973 page: figures/pages/p289.png (printed page 259, References 1-11).
- Render: build/unit/ch2-refs-1.png and ch2-refs.pdf (built 05:25:02, after the last edit of the .tex
  at 05:25:01; the page shows item 12 and note E1, so it is the corrected version). Log: no Overfull
  hbox, no undefined references; `pdftotext` finds no "??". The .aux has `ch2:ref:12` = 12.

## What was checked (12 items)

Item 10 (2022, PDF 686)
1. Entry text compared word by word with p686: "Abbott, Ira H., and Von Doenhoff, Albert E., Theory of
   Wing Sections, Dover Publications, Inc., New York, 1959." -- exact, including the commas, "Inc.,"
   and the final full stop.
2. The underlined title "Theory of Wing Sections" is `\emph{}` (STYLE.md section 12); nothing else is
   underlined on p686.
3. Position: after Reference 11, the last item of the list (p289 ends with 11); numbered 12 by the
   enumerate, matching "12." on p686.
4. Label `ch2:ref:12` as specified; labels `ch2:ref:1`-`ch2:ref:11` unchanged.
5. \ednote present, placed at the end of the new item (after its full stop), not in a display,
   caption or longtable (STYLE.md section 9).
6. Note wording: "Reference 12 is added per Mandell's correction of 15 February 2022; the 1973 list
   ends with Reference 11." -- matches the item; the date agrees with p686's signature; the statement
   of the 1973 reading is true (p289 and git HEAD end with item 11).
7. The note's `\ref`s resolve (12 and 11 in the render); it is E1, the only note in the unit.

Scope
8. Whole diff inspected: the only other change is the header comment (adds "Reference 12 from the 2022
   correction, PDF 686"), a comment only, not typeset.
9. References 1-11 byte-identical to HEAD (no hunk touches them).

Notation / render
10. No mathematics in the unit; STYLE.md section 13 not applicable.
11. Render: the entry wraps to two lines with the correct hanging indent; E1 superscript after "1959.";
    footnote text in full at the foot of the page; no layout problems.
12. No `??` on the page; no labels from other units are referenced here.

## Discrepancies

none
