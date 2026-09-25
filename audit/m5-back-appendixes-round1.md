# M5 audit: back matter, appendixes A-D (round 1)

Method: scan pages read from figures/pages/p647.png to p654.png, with zoomed 300 dpi crops of every
text area (build/zoom/audit_back-appendixes_r1-p649a/b, p650a/b, p651a, p652a, p653a/b, p654a/b).
The compiled unit renders (build/unit/appendix-{a,b,c,d}-1.png, re-rendered from the unit PDFs at
200 to 300 dpi into build/zoom/audit_back-appendixes_r1-render*) were compared with them visually and,
for the text, by a word diff of my own reading of the scan against pdftotext of the unit PDFs.
No .tex file was opened. Labels and TOC entries were checked in the unit .aux files; the unit logs
have no LaTeX warnings and no overfull or underfull boxes.

## Pages and items checked

- **PDF 647** (divider "APPENDIXES") and **PDF 648** (blank): not transcribed, as specified.
- **PDF 649, Appendix A** (label appA): heading "Correspondence Between Metric and English Units";
  subheads "1. Centimeter-Gram-Second (CGS) to English Units" and "2. Meter-Kilogram-Second (MKS) to
  English Units" (underlined in the typescript, set as numbered section headings, labels appA:sec:1,
  appA:sec:2); all 12 conversion lines: .0353 ounce-mass, .0022 pound-mass, 6.84 x 10^-5 slug,
  2.248 x 10^-6 pound-force, .0328 foot, .3937 inch, 35.27 ounce-mass, 2.204 pound-mass, .0684 slug,
  .2248 pound-force, 3.28 feet, 39.37 inches; the unit names and abbreviations "(g.)", "(dn.)", "(cm.)",
  "(Kg.)", "(nt.)", "(m.)"; exponent signs and digits. All match.
- **PDF 650-651, Appendix B** (label appB): heading "Physical Constants and Parameters"; all seven
  quantity cells with their two-line wording and symbols (g), (rho), (p), (mu), (nu), (T), (c); all 23
  value lines, including every superscript (second^2, meter^3, centimeter^3, foot^3, meter^2,
  centimeter^2, inch^2, foot^2), every exponent (10^-5, 10^-4, 10^-7, 10^-5, 10^-1, 10^-4), the
  thousands commas (101,325; 1,013,250; 34,030), "Kg./(m.-sec.)", "g./(cm.-sec.)",
  "slug/(ft.-sec.)", "centimeter^2/sec.", and the degree values 288.16 K, 15.0 C, 518.69 R, 59.09 F.
  All match.
- **PDF 652, Appendix C** (label appC): heading "Correspondence Between Scientific and Decimal
  Notation"; column heads "Scientific Notation" and "Decimal Notation" (underlined, set in italics);
  all 17 rows 10^-8 ... 10^8 with their decimal forms (the zeros counted in each of 0.00000001 ...
  0.1, and the commas in 10,000 ... 100,000,000). The decimal column keeps the typescript's alignment
  (fractions flush from the "0.", integers ending at the decimal-point position). All match.
- **PDF 653-654, Appendix D** (label appD): heading "A Word About the National Association of
  Rocketry"; the four paragraphs, word for word (word diff: no differences), including the quoted
  "lobby" and "recognized authority" with the comma outside the closing quote, "Admin-/istration"
  rejoined, "Federation Aeronautique Internationale" without accent (as typed), "aeromodelling",
  "U.S.", "and/or", "high-quality", "nationally-recognized", "internationally-recognized",
  "Box 178, McLean, Virginia 22101." Paragraph breaks at "The NAR is affiliated", "The NAR also
  maintains a system" and "The authors, NAR members themselves" match.

## Discrepancies

| where | scan reading | compiled reading | severity |
|---|---|---|---|
| none | | | |

## Observation (not a transcription discrepancy)

- Appendix B, sea-level temperature: the typescript prints "= 59.09° F", which does not agree with
  its own 15.0° C (59.0° F) or 518.69° R (518.69 - 459.67 = 59.02° F). The transcription keeps the
  printed value, which is correct under STYLE.md section 3; whether it deserves an \edcap note is an
  editorial choice (no note is present, and none is required by the conventions).
