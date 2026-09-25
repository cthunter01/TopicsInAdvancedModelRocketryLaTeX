# M5 audit: 1973 front matter, part 2 (Publisher's Foreword and Preface), round 1

Unit: frontmatter/original-1973 (the .tex file was not opened; images only).
Scan pages: figures/pages/p018.png to p022.png (PDF 18 to 22), plus zoomed 300 dpi crops of the scan
(build/zoom/audit_front-1973_r1_p2-p019-019.png for "model rockey industry", -p020-020.png for the underlined
"Model Rocketry", -p022-022.png for the underlined "is", "not" and "Handbook of Model Rocketry").
Render: build/unit/original-1973-5.png (foreword), -6.png and -7.png (preface), with -4.png (dedication,
the page before) read as the neighbouring page; no render page follows -7. As a cross-check, pdftotext of
build/unit/original-1973.pdf pages 5 to 7 was diffed word by word against my own reading of the scan images.
After normalizing quotes, dashes and ligatures, and mapping "??" to the printed chapter numbers, the diff
shows only the page numbers and running head (v, vi, "PREFACE vii") and "rockey" -> "rocket".
The unit log has no overfull or underfull boxes. Its only warnings are the eight undefined chapter references
expected in a standalone build.

## Pages and items checked

| scan | content | render | result |
|---|---|---|---|
| PDF 18 | heading "PUBLISHER'S FOREWORD"; two paragraphs ("The aim of this format ..." and "The text of this book ... A detailed table of contents is included."); signature "The MIT Press" set to the right | page 5 | matches: heading as the required unnumbered \chapter "Publisher's Foreword", in the TOC and labelled front:foreword (aux); every word and punctuation mark; "ex-/pense" rejoined; two paragraphs, with "A detailed table of contents is included." kept in the second one (in the scan it continues flush left, not indented); "author's" singular as printed; signature "The MIT Press" set to the right |
| PDF 19 | heading "PREFACE"; paragraph 1 ("To some members ... so technical?"); paragraph 2 begins ("The answer becomes self-evident ... National Association") | page 6 | matches: heading as the required unnumbered \chapter "Preface", in the TOC and labelled front:preface (aux); every word; "twelve-/year-old" rejoined as "twelve-year-old"; "miscon-/ception" rejoined; "technically-oriented" hyphen kept; "(of which this book is one)" kept. The typing slip "model rockey industry" (confirmed on the zoom) is fixed silently to "model rocket industry" |
| PDF 20 | paragraph 2 continued ("of Rocketry; the establishment of Model Rocketry magazine ... slot-car racing in 1967."); paragraph 3 ("The treatments presented herein ... model rocket hobby."); paragraph 4 begins ("Though the various chapters ... Chapter 2 are used in Chapter 4 to provide") | pages 6 | matches: underlined "Model Rocketry" becomes italic; "exclusively -- all" and "1970 -- research" become em dashes; ``senior problem'', with the comma outside the closing quote, and ``boom-and-bust'', as printed; "insure" kept; "Massa-/chusetts" rejoined; names "James S. Barrowman, Dr. Gerald M. Gregorek, Douglas J. Malewicki, and Mark Mercer" correct; paragraph breaks at "The treatments" and "Though the various" correct; "Chapter 2 ... Chapter 4" print as "??", which the log shows are refs to ch2 and ch4 |
| PDF 21 | paragraph 4 continued ("estimates of the effects ... knowledge permits."); paragraph 5 ("The results of Chapter 2 ... in this area."); paragraph 6 begins ("No preface to this volume would be complete without a") | pages 6 and 7 | matches every word; "thrusting-phase" hyphen kept; "coefficient -- and" becomes an em dash; the chapter references (Chapter 3; Chapters 2 and 4; Chapter 2; Chapter 3; Chapter 4) print as "??", which the log shows are refs to ch3, ch2, ch4, ch2, ch3 and ch4 in that order, matching the printed numbers (labels ch2, ch3 and ch4 exist in chapters/*.tex); paragraph breaks at "The results of Chapter" and "No preface" correct |
| PDF 22 | paragraph 6 continued ("word of caution: this book is highly technical and it is not for everyone ... Centuri Engineering Company)."); paragraph 7 ("If, on the other hand ... model rocket vehicles."); signature "George J. Caporaso / Gordon K. Mandell", a gap, then "Cambridge, Massachusetts / May, 1971", set right of centre | page 7 | matches: underlined "is" and "not" become italic; underlined "Handbook of Model Rocketry" (all four words) becomes italic; "caution:" colon kept; "(most notably Estes Industries and the Centuri Engineering Company)." kept; every word of paragraph 7; the signature has two lines, a gap and then the place and date, "May, 1971" with its comma, set to the right |

Typing slips fixed silently: one, "model rockey industry" -> "model rocket industry" (PDF 19). Editorial notes: none
on these pages, and none are needed. Figures, tables and mathematics: none on these pages. Emphasis: the three
underlined passages (PDF 20 and 22) all print in italics; no other underlining on PDF 18 to 22. The signature
blocks sit a little further right than in the typescript. This is an allowed layout difference.

## Discrepancies

none
