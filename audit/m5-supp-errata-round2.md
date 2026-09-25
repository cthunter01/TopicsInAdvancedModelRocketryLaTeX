# M5 audit: supplement, Errata (1973), round 2

Scan pages: PDF 664 (the typeset 1973 errata sheet) and PDF 665 (the second typing of the list),
figures/pages/p664.png and p665.png. Zoomed crops in build/zoom/audit_supp-errata_r2-*.
Render: build/unit/s-errata-1.png and s-errata-2.png (built 19:26, not rebuilt). No .tex file was opened.
Labels were checked in build/unit/s-errata.aux and s-errata.log and with the permitted label grep over chapters/*.tex.

## Round 1 items re-examined

1. "differs in six entries" (round 1 said p665 has "430" for the page-480 entry). **Withdrawn: the round 1 reading was wrong.**
   p665 is a 150 dpi JPX (pdfimages -list), so I dumped the native pixels of figures/pages/p665.png
   (x 235-305, y 1088-1118) and compared them with the 3s and 8s on the same page:
   - On this typewriter the 3 has a flat top bar ("#########") and its tail drops 2-3 px below the baseline.
     Checked: the 3 of "113" (y 449-468), "23" in the vii entry (y 250-268), "583" (y 1243-1261) and "382" (y 945-963).
   - The 8 has a round top loop, a pinched waist and sits on the baseline. Checked: "line 8" in the same row
     (y 1092-1110), "583" and "382".
   - The disputed middle digit has a round top ("+###+", ".##++###+"), a waist ("###++##") and ink on the left just
     below the waist (the upper left of the lower loop, which a 3 does not have), and it ends on the baseline of the
     4 and the 0. It is an 8 whose left strokes printed lightly. So p665 reads "On page 480, line 8 should read:",
     the same as p664, and the note's count of six differing entries is correct.
2. "each entry in the form ...". **Fixed.** The note now says "most entries in the form 'On page ... should read:'"
   and names the three entries without quotation marks (113, 144 and 145, 534). Checked against p665: exactly
   these three have no quotation marks. The 144-145 entry quoted in the note matches p665 word for word
   ("On pages 144 and 145, A, B, and C in the last two equations on page 144 and the first two equations on
   page 145 should be A', B', and C'."). The 113 entry's lead-in "On page 113, equation (30) should read:" matches.

## Everything else re-checked

- Heading "Errata (1973)", label supp:errata (in the .aux). No other \newlabel in the .aux, so the (30) display has no label.
- Sheet head (p664): "ERRATA"; "TOPICS IN ADVANCED MODEL ROCKETRY"; "by Gordon K. Mandell, George J. Caporaso,
  and William P. Bengen"; "(Cambridge, Massachusetts: The MIT Press, 1973)". Match.
- All 16 p664 entries, word by word, with each locator line and corrected line: vii ("line 2 from bottom", no
  "the"); 5 ("line 3, should read"); 108 ("last line of figure caption, should read"); 113 ("Page 113: Equation (30)
  should read"); 144 and 145 ("The A, B, and C ..."; "A', B' and C'." with no comma after B'); 268; 270 ("the last
  line"); 342; 364 (down-/stream rejoined; p665 types "downstream"); 382 (corre-/sponding rejoined); 401; 480;
  534 ("righthand", as printed; v_{n-1}); 583 ("line 4 from the bottom, should read"); 590 ("line 3 of Section
  4.3.3"); 591. All match, commas and final periods included.
- Equation (30), zoomed: alpha_x = A e^{-Dt} sin(omega t + phi) + M_s / C_1, number (30) at the left. Compiled
  alpha_X = Ae^{-Dt} sin(omega t + varphi) + M_s/C_1 with the tag (30) at the right. Matches (the uppercase X follows
  STYLE.md section 13; the number at the right is the convention).
- Hand-lettered symbols (zoomed): Sigma( ), n with an arrow, infinity; typed subscript "xo" in the 108 entry set as
  alpha_{X0} (STYLE.md section 13 form). Match.
- References: the log lists ch2:eq:30, ch4:eq:51, ch4:sec:2.4, ch4:eq:139, ch4:sec:4.3.3, ch4:eq:154 and
  ch4:eq:160 (and ch2:eq:30 and ch4:eq:51 again in the note). Each label exists once in chapters/*.tex. "??" is expected in the standalone build.
- The p665 editorial note, sentence by sentence:
  - headed "TOPICS IN ADVANCED MODEL ROCKETRY" and underlined "Errata" (italic in the note), without the authors and the publisher: true.
  - same sixteen corrections, same order, same corrected text: true (the only differences in corrected text are
    punctuation: no final period after "conventions" in vii, "B', and C'" in 144-145).
  - six differing entries: vii "line 23", 108 "line 7", 270 "line 14", 583 "line 17", 590 "line 15", and the 534
    wording. The other ten entries (5, 113, 144-145, 268, 342, 364, 382, 401, 480, 591) have the same line counts and text.
    "23" and "15" were checked in the pixels ("23": the 3 has a flat top and a descender, not a 5's left stem;
    "15": the 5 has a left stem). The 144-145 entry drops "The", but the note quotes that entry in full as one of the
    entries not in the usual form, so the count is not misleading.
  - the five line counts name the same 1973 lines: re-verified 270 (PDF 300: "infinity" is line 14 counting the
    Symbol/Meaning heading, and it is the last line) and 590 (PDF 622: line 15 = "quiescent prior rotational state
    ...", line 3 of 4.3.3 counting the heading). The other three were verified in round 1.
  - the 534 quotation matches p665 ("right-/hand" split at a line end, set as "right-hand"; v_{n-1}).

## Discrepancies

none
