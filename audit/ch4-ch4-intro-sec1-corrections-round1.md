# Audit: ch4-intro-sec1 corrections, round 1

Unit: chapters/ch4-intro-sec1.tex (Introduction, Section 1, 1.1 and 1.2; PDF 537-552, printed pp. 505-520).
Items for this unit:
- Item 5 (PDF 700-702, pressure term per PDF 666): the June 1994 thrust text after (7) and at the top of p.514.
- D9 (PDF 552): note on $F_p$ of (10).

Read: STYLE.md sections 4, 7, 8, 9, 10, 11 and 15; corrections/ch4.md; `git diff HEAD -- chapters/ch4-intro-sec1.tex`.
Source pages read: p664 (errata), p666, p699-p702, p703 and p710 (the Summary's first and last pages), p545, p546, p550 and p552.
Zoomed crops (300 dpi): PDF 700 (7a)-(7b) (build/zoom/audit_ch4-intro-sec1_r1-p700a-700.png); PDF 700, the "Equation (7)
above ..." paragraph through (7d) (build/zoom/audit_ch4-intro-sec1_corr_r1-p700b-700.png); PDF 701, (8) and its "Where"
line (build/zoom/audit_ch4-intro-sec1_corr_r1-p701a-701.png).

## What was checked

1. **Item 5 applied as the source specifies.**
   - **Extent.** The replaced text runs from "The term $-\vec{c}(dm_e/dt)$ is just the thrust ..." (p.513, after (7)) to
     "... aerodynamic resistance, or drag." (top of p.514). That matches PDF 700's "[Change text after equation 7 on page 513]"
     and PDF 701's "[Change text at the top of page 514]". Section 1.1 and the rest of p.514 are byte-identical to HEAD.
     Nothing from the 1973 text is left behind: the 1973 sentence "The thrust can be denoted by the single symbol $\vec{F}(t)$,
     so we can write" is gone, as in the source. Nothing was added that the source does not give, apart from the \ednote.
   - **Prose, sentence by sentence against PDF 700-701.** Every sentence matches:
     - the "optimum expansion" paragraph and "That is,";
     - the "not equal" sentence;
     - the "Where / (blank) / and" list;
     - the convergent/divergent paragraph (five sentences);
     - the "Equation (7) above includes ..." paragraph;
     - "and to write the equation for thrust in the form";
     - the "Since the effective exhaust velocity ..." paragraph;
     - the "Where $\vec{E}_o$ ..." line;
     - "Both the engine thrust ... Chapter 1, in the following discussion" (no comma after "flight forces", as in the source);
     - the new top of p.514.

     The underlines are set as \emph, as printed: exit plane, ambient, thrust; not; backward, negative, positive (twice),
     increase; other than; flight forces; weight, drag. The quotation marks and their punctuation also match the source
     (`correct expansion'',` and `pressure component of thrust''.`).
   - **Equations, symbol by symbol (zoomed).** Each equation matches the source:
     - (7a) `F(t) = -\vec{c}(dm_e/dt)`. PDF 700 prints F(t) with no arrow (confirmed at 300 dpi). It is kept plain, and the
       note says so.
     - (7b) `\vec{F}(t) = -\vec{c}(dm_e/dt) + (P_e - P_a)\vec{A}_e`.
     - (7c) `\vec{c}_{\mathrm{eff}} = \vec{c} - (P_e - P_a)\vec{A}_e/(dm_e/dt)`.
     - (7d) `\vec{F}(t) = -\vec{c}_{\mathrm{eff}}(dm_e/dt)`.
     - (8) `m(t)(d\vec{v}/dt) = \vec{F}(t) + \vec{E}_o`, slashed as printed.

     The pressure term follows PDF 666, with the arrow over $A_e$ only, in (7b), (7c) and both times in the prose. PDF 700
     draws the arrow over the whole term, and the note records this.
   - **Mathematics.** I redid it:
     - $\vec{F} = -\vec{c}\,\dot{m} + (P_e-P_a)\vec{A}_e = -[\vec{c} - (P_e-P_a)\vec{A}_e/\dot{m}]\,\dot{m} = -\vec{c}_{\mathrm{eff}}\,\dot{m}$,
       so (7c) and (7d) are consistent with (7b).
     - The signs agree with the prose: $\vec{A}_e$ points forward (PDF 702), so $P_e > P_a$ adds forward thrust and
       $P_e < P_a$ reduces it.
2. **Notes.**
   - **Item 5 \ednote.** It is placed in "That is,", the sentence that introduces (7a). It is not inside a display, which
     section 9 allows. It names Mandell's June 1994 "Changes to text of Chapter 4" and states their purpose correctly
     (PDF 699). It also cites the 1 June 1994 note on the arrow and records the unarrowed F(t) of (7a).
   - **The 1973 text in the item 5 note.** Checked word by word against PDF 545-546 and git HEAD:
     - the paragraph from "The term ..." to "so we can write";
     - the 1973 (8), `m(t)\frac{d\vec{v}}{dt} = \vec{F}(t) + \vec{E}`, with arrows on v, F and E as printed;
     - "Both the engine thrust ... or drag.", including the underlines (\emph) and "flight forces, as per".

     The note says the 1973 E on p.514 has no arrow (PDF 546: "represented by E") and that the supplement's $E_o$ there also
     has none (PDF 701). Both statements are accurate.
   - **Problem found.** The note's opening words, "From this sentence", are imprecise (table below).
3. **D9 note.**
   - **Placement and style.** It is in "in the form", the sentence that introduces (16)-(17), which is legal. It follows the
     chapter's doubt-note style ("Neither the errata nor the supplements correct this; the text is kept as printed").
   - **Mathematics.** I redid it:
     - PDF 550 prints (12)-(13) with $F_t\cos\theta$ and $F_t\sin\theta$ only.
     - PDF 552 says "Substituting (9), (10), (14) and (15)". Its (16)-(17) contain only $F(t)\cos\alpha\,(\dot{y}/v)$ and
       $F(t)\cos\alpha\,(\dot{x}/v)$.
     - $F_p = F(t)\sin\alpha$ appears nowhere. PDF 549 defines it as the component "perpendicular to the trajectory", which
       the note's "normal to the trajectory" matches.
     - The only nearby justification (PDF 549) concerns aerodynamic side force, not thrust, so "dropped without comment"
       holds.
   - **"Neither the errata nor the supplements correct this."** Verified:
     - The errata's Chapter 4 entries are for pp. 534, 583, 590 and 591.
     - The 1994 changes cover pp. 513-514 and the Symbols list.
     - The Summary covers Sections 2.2 and 3 (PDF 703 and 710).
     - PDF 711-712 cover Figure 4 and Table 1.
   - **Other notes.** No other doubts or "check" items belong to this unit. D12 (the unarrowed E) is covered by item 5's
     note, as corrections/ch4.md specifies. No minor-slip notes were added.
4. **Scope.** The whole diff has three parts: the header comment (two comment lines), the item 5 block and the D9 \ednote.
   Nothing else changed. The 1973 uses of $\vec{E}$ before (7) (lines 107, 161-181) are untouched, as instructed.
5. **Labels.**
   - (7a)-(7d) are `equation*` with `\tag{7a}`-`\tag{7d}` and `\label{ch4:eq:n7a}`-`n7d`, as section 4 requires.
   - (8) keeps `\label{ch4:eq:8}` in a numbered `equation`.
   - build/unit/ch4-intro-sec1.aux has `{{7a}}`...`{{7d}}` with distinct anchors AMS.4-AMS.7. (8) is `equation.4.8` and
     (9) is `equation.4.9`, so there is no anchor collision.
6. **Section 15 notation.** $\vec{A}_e$, $P_e$, $P_a$ (italic letter subscripts), $\vec{c}_{\mathrm{eff}}$ (upright word
   subscript, arrow over the letter only), $\vec{E}_o$ (letter o), $dm_e/dt$, $\mdot$ and $\vec{F}(t)$ in (8) all match.
   The unarrowed $E_o$ on the p.514 line is kept plain, per the vector rule for a letter printed without an arrow.
7. **Render.** build/unit/ch4-intro-sec1.pdf and the PNGs (18:31:00-18:31:12) are newer than the source (18:30:48).
   - Page 4 ends in the new first paragraph.
   - Page 5 shows (7a)-(7d) with their tags, the "Where / and" list, the three new paragraphs, (8) numbered (8) and note E1
     in full.
   - Page 6 opens with the (8) "Where" line, then the new p.514 sentence and Section 1.1.
   - Page 9 shows (16)-(17) with note E2.

   There are no overfull boxes. The "Chapter ??" references are expected in a unit build. Two layout effects come from the
   unit build and are not discrepancies: the (8) "Where" line falls on the next page, and the (7b) list is followed at once
   by the indented "Most practical ..." paragraph, because of `nosep`.

## Discrepancies

| where | expected (source/1973) | found | severity |
|---|---|---|---|
| chapters/ch4-intro-sec1.tex l.187, item 5 \ednote (E1, rendered p.5) | The 1994 text begins with the paragraph's first sentence, "If the nozzle ... as it would be measured in a static test stand." (PDF 700). That sentence replaces the 1973 "The term ... is just the thrust ...". The note's extent should say so, e.g. "From the beginning of this paragraph to the end of the paragraph before Section 1.1 ...". | "From this sentence to the end of the paragraph before Section 1.1 ...", with the marker after "That is,". "This sentence" reads as beginning at "That is,", so the note seems to leave "If the nozzle ... static test stand." as 1973 text. | note |
