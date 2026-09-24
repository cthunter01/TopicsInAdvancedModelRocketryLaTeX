# Audit: corrections applied to chapters/ch3-sec5a.tex (round 1)

Scope: `git diff HEAD -- chapters/ch3-sec5a.tex` (HEAD = 7e2087d, the faithful 1973 transcription), against
the errata sheet (PDF 664), the supplement page for Section 5.2.2 (PDF 690), the 1973 pages PDF 436, 438,
441 and 444, STYLE.md sections 4, 8, 9, 10, 11, 14, the Decisions in corrections/ch3.md, and the rendered
pages build/unit/ch3-sec5a-2.png, -5.png, -6.png, -7.png (built 09:35:14, after the last edit to the .tex
at 09:35:13). No rebuild.

## Authors and dates shown by the sources

- Errata sheet (PDF 664): headed "ERRATA / TOPICS IN ADVANCED MODEL ROCKETRY by Gordon K. Mandell, George J.
  Caporaso, and William P. Bengen (Cambridge, Massachusetts: The MIT Press, 1973)". It names the book's
  authors; it gives no author of the sheet and no date. No Chapter 3 entry touches printed pages 404 or 412.
- Chapter 3 supplement pages PDF 688-698 (including PDF 690, "Corrections and additions to Section 5.2.2 of
  Chapter 3"): no author, signature or date on any page. The note correctly names the supplement by its title
  only.

## What was checked

1. Item 9 (PDF 690), extent. The 1973 second paragraph of 5.2.2 (PDF 444) is "As in the case of the body ...
   it produces. One cannot, however, ... on the fin. We shall assume ...". Only the second sentence is removed;
   the first sentence and "We shall assume ..." are kept. Nothing else of the 1973 page is touched.
2. Item 9, text sentence by sentence against PDF 690: "The induced drag coefficient of a fin flying at an
   angle of attack alpha such that its lift coefficient is C_L is given by"; the where-list (AR = aspect ratio
   ... "wing" ... diametrically-opposed ... also equal to (span)^2/(area)); "and e = span efficiency factor";
   "The quantity e AR is the **effective aspect ratio** of an "equivalent" wing whose lift is distributed across
   its span in the shape of an ellipse. In practice, e is almost always less than 1.0. Since"; "equation (144A)
   can also be written in terms of alpha as". All match. "effective aspect ratio" is \textbf. The where/and
   lists use the unit's existing itemize form.
3. Item 9, equations symbol by symbol: (144A) C_Di = C_L^2/(pi e AR); unnumbered C_L = (dC_L/dalpha) alpha;
   (144B) C_Di = (dC_L/dalpha)^2 alpha^2/(pi e AR). All match PDF 690. Both tagged displays are
   `equation*` + `\tag{144A}\label{ch3:eq:n144A}` / `\tag{144B}\label{ch3:eq:n144B}`; the aux gives 144A and
   144B; the 1973 label ch3:eq:144 is kept on (144) C_DB(alpha) = 1.94alpha^2 + 8.86alpha^3.
4. Item 9, row of constants: set as d alpha deg/dC_L = 18.6, dC_D/dC_L^2 = 0.123, e = 0.863, which is the
   supplement's "revised row of constants" as shown ("0.123" with leading zero is the supplement's form; 1973
   printed ".123").
5. Note E2 (the item 9 note), sentence by sentence against HEAD and PDF 444: it quotes the removed 1973
   sentence in full (underlined "distribution" as \emph, as in HEAD). It states the 1973 row correctly (18.6 and
   .123 only). It names the supplement by title. Arithmetic: 1/(pi x 0.863 x 3) = 1/8.134 = 0.1229, i.e. .123,
   so the claim that e makes 1/(pi e AR) equal to .123 holds. Placement: after "is given by", in the sentence that
   introduces (144A), outside any display (section 9). The \ref to ch3:sec:5.2.2 resolves.
6. D16 (PDF 436). Zoomed scan: (139) ends "... S_o / S_m alpha", with no exponent. Note E1 checked:
   alpha x [2(k2-k1)S_o/S_m] alpha gives alpha^2. (142) on PDF 438 prints alpha^2 in its first term. PDF 441
   prints 2(k2-k1)(S_o/S_m)alpha^2 = 1.94alpha^2 (2 x 0.97 x 1.0 = 1.94). The errata sheet has no entry for p.404
   and the supplements have none either, so "Neither the errata nor the supplements correct this; the equation
   is kept as printed" holds. The equation is kept as printed. The note is after "we then have", before the
   display. It follows the Chapter 2 style required by the Decisions.
7. D4 (PDF 436). Zoomed scan: (140) prints l_B. It is now \ell_b, silently, as the Decisions require. It is the
   same quantity: the example x_o = .55(8.9) + .36(33) = 16.8 cm uses the body length 33 = l_b (and Figure 37
   gives x_o = .51 l_b).
8. Item 6: line 32 reads "is usually small compared to that due to the mechanism which" (already in HEAD).
   The diff does not touch it.
9. Scope: the diff has exactly three hunks, the E1 note, (140), and the item 9 block with the row of constants.
   Nothing else changed.
10. Section 14 notation in the corrected passages: C_{Di} (one subscript level), C_L, \AR, italic e, \alpha,
    italic d, \pi, \dg. All conform.
11. Render (build/unit/ch3-sec5a-2.png, -5.png, -6.png, -7.png): E1 marker after "we then have" and the note at
    the foot of p.2. (140) shows l_b. The paragraph runs on from p.5 to p.6: (144A), the where/and lists, the bold
    "effective aspect ratio", the unnumbered C_L display, (144B), and the three-constant row. E2 is at the foot
    of p.6, and p.7 continues unchanged. There are no overfull boxes. The only log warnings are the expected
    cross-unit undefined references.

## Observations (no change required)

- The E2 note ends "equal to that .123" while the revised row directly above it now reads 0.123 (the
  supplement's form). The note's statement of the 1973 reading (.123) is accurate and the change is formatting
  only, so this is left as it is.
- corrections/ch3.md still shows status "todo" for items 9, D4 and D16 (the checklist diff adds only the
  Decisions block). This is outside the unit file and is presumably updated at the end of the step.

## Discrepancies

| where | expected (source/1973) | found | severity |
|---|---|---|---|

none
