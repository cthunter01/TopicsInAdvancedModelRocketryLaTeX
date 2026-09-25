# M5 audit: supplement, Chapter 1 documents, round 1, part 1

Scan pages: PDF 667-671 (figures/pages/p667.png to p671.png).
Render: build/unit/s-ch1-1.png to s-ch1-4.png carry this content; s-ch1-5.png (the symbols to add, PDF 672-673, the other auditor's part) was read as the neighbouring page. There is no page before s-ch1-1.
Zoomed crops (300 dpi): build/zoom/audit_supp-ch1_r1_p1-p668a/b/c, -p669a/b, -p671a/b (the Figure 2 caption, the displays on 668, equations (1) and (2) with the "where" list and the sign-convention displays on 669, and (2a) and (5)-(7) with the prose around them on 671).
The prose was also word-diffed: pdftotext of render pages 1-4 against the OCR of PDF 667-671. The only differences were OCR noise, math tokens, running heads, "??" for chapter, figure and equation references, and the one silent fix listed below.

## Items checked

- PDF 667: the heading "CHANGES TO TEXT OF CHAPTER 1", set as the chapter title "Changes to Text of Chapter 1". The cover note paragraph word for word, with the book title in italics, "optimal expansion" and "correct expansion" in quotes, and "Chapter 1" as a reference (?? in the standalone build). The signature "Gordon Mandell" and the date "June 1994" on separate lines.
- PDF 668: "[Change caption of Figure 2 on page 14 to read as follows]:" (Figure ?? in the standalone build). The new caption with bold "Figure 2:", Δt, Δm_e, dt, dm_e, dm_e/dt, ṁ, and the vectors c⃗ and −c⃗(dm_e/dt). The emphasis on *nozzle exit plane*, *ambient* (the underline's small run-in under "the" is a typing overrun) and *thrust*. The vector A⃗_e, and the long arrow over the whole of (P_e − P_a)A_e. Its apparent underline of "the nozzle" on the line above is in fact this arrow. Also checked: (+y) and (−y), "when P_e is greater than P_a" and "less than P_a", and the unnumbered display F⃗ = −c⃗(dm_e/dt) + arrow over (P_e − P_a)A_e. The "NOTE:" paragraph with NOTE in italics. "[Insert after the 3rd line on page 16]:" and its indented paragraph, with *nozzle exit plane*, *exhaust pressure* and *ambient*. "[Change the 4th and subsequent lines on page 16 to read as follows]:". The "Now the thrust ..." paragraph, with the whole underlined clause in italics and *rate* and *velocity*. "Chapter 4" is a reference.
- PDF 669: equation (1), symbol by symbol, including the extent of both arrows. The "where" list (F⃗, c⃗ with *as measured by an observer moving with the rocket*, dm_e/dt, P_e, P_a, A⃗_e). The "Students of physics ..." paragraph (*vector*, *scalar*), not indented. The indented "In a properly designed ..." paragraph. "[End of page 16 and beginning of page 18 of original text]". The "is directed dead astern ..." paragraph (*positive*, *negative*, "fore-and-aft"). The displays c = −c⃗, F = F⃗, and "and" A_e = A⃗_e "so that" (P_e − P_a)A_e = arrow over (P_e − P_a)A_e. "Then we can write". Equation (2), F = c(dm_e/dt) + (P_e − P_a)A_e. The "Professional rocket engineers ..." paragraph (*mass flow rate*, ṁ).
- PDF 670: the continuation paragraph (*throat area*, P_e = P_a, "equation (2)", the quoted terms, (P_e − P_a) as "overpressure"). "[End of text on page 18]" and "[Change page 19 of original text to the following:]". The indented "In theory, then, ..." paragraph (*thrust-time curves*). The start of the indented "In any given engine ..." paragraph.
- PDF 671: its continuation ("equation (2)", P_e = P_a). Equation (2a), ṁ = (dm_e)/(dt) = F/c, with its printed number. "if you are careful with units. Suppose, for". The two-line bracket "[End of text on page 19]" / "[Pages 20 through 29 are unchanged]", and the three-line bracketed instruction for pages 30 and 31 with the quoted question. The "The answer to this question ..." paragraph (*specific impulse*). Equation (5), I_sp = I_t/w_f = I_t/(m_f g). The "where m_f ..." paragraph (*mass*, *weight*, "(9.806 meters/sec.²)", "newton-seconds per newton — or simply *seconds*"). Equation (6), c + (P_e − P_a)A_e/ṁ = gI_sp. The inline c + A_e[(P_e − P_a)/ṁ] and c_eff. Equation (7), c_eff = c + (P_e − P_a)A_e/ṁ, then = gI_sp on a second line, with (7) on the first line. The paragraph "The specific impulse measured ..." up to "The highest".
- Paragraph indents: those of every paragraph on 667-671 match the scan.

## Intended forms (not discrepancies)

- "momemtum" (PDF 668, in the underlined clause) is set as "momentum": a typing slip fixed silently.
- The hand-drawn arrow over "Ae" (A⃗_e) covers the subscript, and it is set as `\vec{A}_e`. The STYLE.md vector rule puts the arrow over the letter only (`\vec{D}_i`, `\vec{p}_E`), and the meaning is the same.
- In the "where" list on 669 the typescript lines up the "=" signs. The render sets the entries one per line, left-aligned, and the wording and symbols are unchanged.
- "and", the connective printed at the left of the third sign-convention display, is set as a short prose line before that display (STYLE.md section 4).

## Discrepancies

| where | scan reading | compiled reading | severity |
|---|---|---|---|
| none | | | |
