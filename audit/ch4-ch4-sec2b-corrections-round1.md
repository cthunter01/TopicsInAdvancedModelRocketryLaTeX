# ch4-sec2b corrections audit, round 1

Unit: chapters/ch4-sec2b.tex (Sections 2.3-2.5, PDF 571-596). Diff audited: `git diff HEAD -- chapters/ch4-sec2b.tex`
(HEAD = faithful 1973 transcription). Items: 8 (replacement Figure 4, PDF 711) and D4 (legend line, PDF 587).

## What was checked

### Item 8: Figure 4 (PDF 711 against PDF 580 and git HEAD)
- Image: `figures/supplement/ch4-fig04-1994.png` (manifest row sup-ch4-fig04-1994, unit ch4-sec2b) replaces
  `figures/ch4/fig04.png` and is included exactly once. The manifest row for ch4-fig04 now names the unit
  "supplement". `\label{ch4:fig:4}` is kept, and the figure stays after the paragraph that cites it.
- Caption, checked against PDF 711 (with a 300 dpi zoom of the last two lines,
  build/zoom/audit_ch4-sec2b_r1-p711cap-711.png): the first two sentences are the same as in 1973. The added
  sentence "$t_1$ as shown here is $t_m$ as defined for equations (73) through (75), and $t_2$ as shown here is $t_s$
  as defined for equations (73) through (75)." matches the source word for word, including the comma and the final
  period. Both citations are `\eqref{ch4:eq:73}` through `\eqref{ch4:eq:75}`. (73) is a `subequations` group labelled
  ch4:eq:73, so it prints "(73)". The subscripts are italic, as section 15 requires ($t_1$, $t_2$, $t_m$, $t_s$; the
  source prints t_S with a small-capital-looking s).
- Mathematics: the figure's values agree with the 1994 identification. The peak time is $t_1 = 0.14 = t_m$ and the
  sustainer onset is $t_2 = 0.22 = t_s$. Equation (75) gives $I_t = 13.0(0.22)/2 + 3.5(1.20 - 0.07 - 0.11) = 1.43 + 3.57 = 5.00$
  N-sec, which is the $I_t = 5.0$ in the artwork. So the new caption needs no note.
- Artwork, PDF 580 against PDF 711: I aligned the two crops on their axes. The x scale runs from t = 0 to 1.2 and the
  y scale from F = 0 to 16. I then overlaid them (build/zoom/audit_ch4-sec2b_r1-overlay.png). Every element
  coincides: the curves, the dashes, the ticks, the legend, the parameter block ($I_t$ = 5.0 N-sec, $F_m$ = 13.0 N,
  $F_s$ = 3.5 N, $t_1$ = 0.14 sec, $t_2$ = 0.22 sec, $t_b$ = 1.20 sec) and "B4". It is the same drawing. On the page,
  the 1994 plot is about 1.8 times wider (384 pt against 213 pt) and about 6% taller relative to its width, which
  is a reproduction effect. The \edcap's "The artwork is unchanged: it is the same drawing, reproduced larger" is
  accurate.
- \edcap: it is inside `\caption`, which section 9 allows. Its quotation of the 1973 caption matches git HEAD and
  PDF 580 word for word. "Without the last sentence, which relates the figure's $t_1$ and $t_2$ to the $t_m$ and
  $t_s$ of the text" is accurate. The mention that the 1973 figure is reproduced in the supplement Part agrees with
  the manifest and the decisions. The `.'',` punctuation and the overall pattern match the Chapter 1 and Chapter 2
  replacement-figure \edcap's. One attribution point is listed in the table below.
- Rendering: the figure and caption appear on build/unit/ch4-sec2b-06.png (the render is newer than the source:
  18:29:08 against 18:29:02). The citations print (73) and (75) as links. The log shows no overfull boxes and no
  errors. The only undefined references come from outside the unit, as expected in a standalone build.

### D4: legend line (PDF 587)
- `\ednote` placement: after "Figures 5.5--5.9:" in a `\noindent` prose line, not in a display, caption or table.
  This is legal.
- Content: PDF 587 prints "Figures 5.5 - 5.9:". The paragraph below and the key table ("Figure number" 5-9) give
  5 through 9, and the panel captions give 5(a) to 9(c): PDF 588 onwards, labels ch4:fig:5a to ch4:fig:9c, all
  present. An OCR search of PDF 529-646 finds no other decimal figure numbering. The errata (PDF 664: pages 534,
  583, 590, 591) and the supplements (PDF 666, 699-712) do not touch printed page 555. The note's claims are
  therefore accurate. It follows the chapter's doubt-note style ("... is evidently meant: ... Neither the errata
  nor the supplements correct this; ... kept as printed."), and the legend line is kept as printed.
- Rendering: build/unit/ch4-sec2b-08.png shows "Figures 5.5–5.9:" with the note marker, and the footnote text is
  complete.

### Scope, labels, notation
- The whole diff consists of: the header comment (items listed), the \includegraphics path, the caption plus
  \edcap, the rewrapped PDF 587 comment ("kept as printed, with a note"), and the D4 \ednote. No other line
  changed.
- No new equations, so no n-labels are needed. The 1973 label ch4:fig:4 is kept. The notation in the new caption
  follows section 15.
- Check items for this unit: none besides D4. D15's last-digit rounding in the PDF 587 key table correctly has no
  note.

## Discrepancies

| where | expected (source/1973) | found | severity |
|---|---|---|---|
| ch4-sec2b.tex l.217, Figure 4 \edcap, first sentence | PDF 711 shows no author, title or date: only the page number "-548-", the drawing and the caption. It is not part of Mandell's signed "Changes to text of Chapter 4" (PDF 699-702, which cover only the thrust text and the Symbols). corrections/ch4.md lists it only as "the replacement Figure 4 (PDF 711)". The Table 1 \edcap in ch4-sec4 names its unsigned source (PDF 712) by title, without an author. A neutral wording would be "Figure and caption replaced per the replacement Figure 4 of the supplement (no author or date shown)". | "Figure and caption replaced per Mandell's replacement Figure 4." This wording was prescribed by the item text, so it is the orchestrator's call; the attribution is not supported by the page. | note |
