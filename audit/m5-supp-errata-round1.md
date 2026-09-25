# M5 audit: supplement, Errata (1973), round 1

Scan pages: PDF 664 (the typeset 1973 errata sheet) and PDF 665 (the second typing of the list),
figures/pages/p664.png and p665.png, with zoomed crops in build/zoom/audit_supp-errata_r1-*.
Render: build/unit/s-errata-1.png, build/unit/s-errata-2.png (not rebuilt). No .tex file was opened.
Labels were checked in build/unit/s-errata.aux, s-errata.log and with the permitted label grep over chapters/*.tex.

## Items checked

- Heading: "Errata (1973)", label supp:errata (in the .aux).
- Sheet head (p664): "ERRATA"; "TOPICS IN ADVANCED MODEL ROCKETRY"; "by Gordon K. Mandell, George J. Caporaso,
  and William P. Bengen"; "(Cambridge, Massachusetts: The MIT Press, 1973)". All match.
- All 16 entries on p664, word by word, locator line and corrected line:
  vii; 5 (Σ( ) / sum of all ( )); 108 (α_xo ... glue or tar.); 113 (equation (30)); 144 and 145 (A, B, C → A′, B′ and C′);
  268 (vector n / unit normal vector); 270 (∞ / infinity); 342; 364 (the down-/stream hyphen rejoined); 382 (corre-/sponding rejoined);
  401; 480; 534 (v_{n-1}); 583; 590; 591. All match, commas included ("Page 5, line 3, should read";
  "Page 583, line 4 from the bottom, should read"; no comma in the others).
- Equation (30), symbol by symbol (zoomed): α_x = A e^{-Dt} sin(ωt + φ) + M_s / C_1, number (30). Compiled
  α_X = Ae^{-Dt} sin(ωt + φ) + M_s/C_1 with tag (30). Matches (number at the right is the convention;
  the hand-lettered x is case-ambiguous and uppercase follows STYLE.md section 13).
- Hand-lettered symbols (zoomed): Σ( ), n with arrow (\vec{n}), ∞. Match.
- Cross-references: \eqref/\ref targets in the log are ch2:eq:30 (book p. 113 = PDF 143, ch2 eq 30),
  ch4:eq:51 (book p. 534 = PDF 566), ch4:sec:2.4, ch4:eq:139, ch4:sec:4.3.3, ch4:eq:154, ch4:eq:160;
  all these labels exist in chapters/*.tex and point to the right chapter. "??" in the standalone build is expected.
- Editorial note on PDF 665, checked entry by entry against the p665 scan (zoomed) and against the 1973 pages:
  - heading "TOPICS IN ADVANCED MODEL ROCKETRY" / underlined "Errata" (italic in the note), no authors or publisher: true.
  - sixteen corrections, same order, same corrected text: true.
  - five different line counts naming the same 1973 line: verified on the book pages.
    vii (PDF 19): "model rockey industry" is line 23 counting the PREFACE heading and line 2 from the bottom.
    108 (PDF 138): the 7th text line, the last caption line. 270 (PDF 300): "infinity" is line 14 counting the
    Symbol/Meaning heading, the last line. 583 (PDF 615): 16 equation lines then "Again, ..." = line 17 and
    4th from the bottom. 590 (PDF 622): line 15 = line 3 of Section 4.3.3 (counting the heading). All true.
  - the p534 wording: "On page 534, the second term of equation (51) should have a right-hand brace to the right of
    the bracket after v_{n-1}." Matches p665 ("right-/hand" split at a line end; "right-hand" is a fair reading).
    "Describes the same place" is true: on PDF 566 the radical is in the second term of (51).
  - the count of differing entries and the "each entry in the form" sentence: see the table.

## Not discrepancies (checked)

- p664 108 entry: typed subscript "xo" (lowercase x, letter o; zoomed) is set α_{X0}. This is the Chapter 2 form
  that STYLE.md section 13 fixes for this symbol (the book's own caption on PDF 138 is typed "xo" too), so it is intended.
- Tab-aligned symbol/meaning columns in the 5, 268 and 270 entries are set with one common indent; this is layout only.
- A, B, C, A′, B′, C′ and v_{n-1} are set as math; the A, B, C of the p364 sentence stay upright text, as typed.

## Discrepancies

| where | scan reading | compiled reading | severity |
|---|---|---|---|
| editorial note on PDF 665 (render p. 2), "differs in six entries" | p665 also differs in a seventh entry: the page-480 entry is typed "On page 430, line 8 should read: ..." (zoomed at 600 dpi: the middle digit is an open 3, unlike the closed 8 of "108"; the line is on book p. 480 = PDF 512). This is a typing slip in p665 | "Apart from that form and from punctuation it differs in six entries." The 430 is not mentioned, so the count is false | text |
| editorial note on PDF 665 (render p. 2), "each entry in the form ..." | Three p665 entries are not in that form: p113 ("equation (30) should read:" then the display, no quotation marks); pp144-145 ("On pages 144 and 145, A, B, and C ... should be A', B', and C'.", no quotation marks, and "The" is dropped); p534 ("should have a right-hand brace ...", no quotation marks) | "each entry in the form 'On page ... should read:' with the corrected text in quotation marks" (states every entry; should say most entries, or name the exceptions) | text |
