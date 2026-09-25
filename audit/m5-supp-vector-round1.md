# M5 audit: supplement, "Vector Notation for Pressure Term of Rocket Thrust" (round 1)

Scan pages: PDF 666 (figures/pages/p666.png), plus zoomed crops at 300 dpi
(build/zoom/audit_supp-vector_r1-p666-disp-666.png, build/zoom/audit_supp-vector_r1-p666-inline-666.png).
Render: build/unit/s-vector-note-1.png, plus zoomed crops at 400 dpi of build/unit/s-vector-note.pdf
(build/zoom/audit_supp-vector_r1-render-disp2-1.png, build/zoom/audit_supp-vector_r1-render-disp-1.png).
No .tex file was opened.

## Items checked

- Heading: "VECTOR NOTATION FOR PRESSURE TERM OF ROCKET THRUST" (typescript capitals) set as the
  unnumbered chapter title "Vector Notation for Pressure Term of Rocket Thrust" (the specified form).
- Paragraph 1, every word: "In the parts of Chapters 1 and 4 that have been rewritten to account for
  the presence of a pressure term in the equation for rocket thrust, that pressure term should be
  written" (no colon, as printed). "1" and "4" render as "??", which is expected in the standalone
  build; the unit log shows they are \ref{ch1} and \ref{ch4}, the correct chapters.
- Display 1: (P_e - P_a) with vector arrow over A_e. Compiled (P_e − P_a)\vec{A}_e. Subscripts e, a, e
  correct; parentheses correct; minus sign correct. The typewriter arrow spans the whole
  "Ae" glyph pair; the compiled arrow sits over A with the subscript outside, which is the
  project's vector notation (\vec{A}_e) and means the same thing (the vector is A_e). Not a discrepancy.
- Connective line "rather than", flush left, as printed.
- Display 2: arrow over the whole term (P_e - P_a)A_e. Compiled \overrightarrow{(P_e − P_a)A_e}:
  the arrow runs from the opening parenthesis to past the subscript e, as in the scan. Symbols
  and subscripts correct.
- Paragraph 1 continued, every word: "as I originally wrote it. On rereading these Chapter 1 and 4
  corrections and additions, I concluded that it is unnecessary and redundant to continue the
  vector arrow over the entire expression because all the directional information necessary to
  define the pressure term as a vector quantity is carried by the unit vector normal to the
  exhaust plane which makes it possible to write the exhaust plane area A_e [arrow] as a vector.
  The pressures P_e and P_a are intended to be regarded as essentially hydrostatic rather than as
  components of a pressure tensor, and therefore convey no directional information."
  Singular "Chapter" kept as printed; references go to ch1/ch4. Inline \vec{A}_e, $P_e$ and $P_a$ are correct.
  The mark under the "t" of "exhaust" in the scan is the arrow over A_e on the next typed line, not
  underlining. Not a discrepancy.
- No emphasis/underlining in the note; none in the render.
- Paragraph structure: one paragraph broken by the two displays, then the signature. The continuation
  "as I originally wrote it" is not indented, which matches the scan.
- Signature and date: "Gordon Mandell" / "June 1, 1994" on two lines, flush left. Matches.
- No figures, tables, equation numbers or editorial notes on this page; the render has none either.

## Discrepancies

none
