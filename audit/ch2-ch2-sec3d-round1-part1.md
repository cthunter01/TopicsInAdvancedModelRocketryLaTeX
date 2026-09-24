# Audit ch2-sec3d, round 1, part 1 (scan PDF 193-203)

## (1) Scope and item counts

Scan pages: figures/pages/p193.png to p203.png, one Read per page. On p193 only the text from the
3.2.2 heading down is in this unit. I also read zooms at 300 dpi of p195 (the rewritten
initial-condition set and A1 sin phi1), p196 (A1 cos phi1 to A2 cos phi2), p199 (the H/I_L pair and (65a)),
p200 ((67)), p202 (the forcing functions and the paragraph after them) and p203 (the second "we can
obtain" pair). The zooms are in build/zoom/audit_ch2-sec3d_r1_p1-*.

Render pages: build/unit/ch2-sec3d-01.png to -07.png. Pages 01 to 07 carry the content of PDF 193-203.
Page 07 also holds the seam into PDF 204 ("From the second equation we see that"), and nothing is
missing or duplicated there. There is no render page before 01.

What I checked:
- Headings: 3 (3.2.2 on p193, 3.2.3 on p197, 3.2.4 on p200, which wraps onto two lines in the scan).
  The wording and numbers match.
- Numbered equations: 12. These are (61), (62a), (62b), (63a), (63b), (64a), (64b), (65a), (65b), (66a),
  (66b) and (67). Each matches symbol by symbol. The numbers run in sequence with no offset.
- Unnumbered displays: 23, checked symbol by symbol:
  - p194: 3 (the pre-step pair, alpha_X = alpha_Y = 0, and the post-step pair).
  - p195: 3 (the four initial conditions with "= 0" lines, the rewritten set of four, and
    A1 sin phi1).
  - p196: 4 (A1 cos phi1, the A2 relations, A2 sin phi2 and A2 cos phi2).
  - p197: 1 (the impulse response pair).
  - p199: 2 (the H/I_L pair and the A2 relations).
  - p202: 4 (f_x/f_y, the dynamical equations, the particular solution and the four derivatives).
  - p203: 6 (two algebraic equations, the trig identities, two "we can obtain" equations and the
    "first relation" pair).
- Inline formulas: about 35. All match.
- Figure captions: 2. The captions of Figure 28 (p198) and Figure 29 (p201) match word for word.
- Prose: all paragraphs on the 11 pages, checked sentence by sentence. This covered wording, the
  emphasis on "not" (p197), the cross-references (all "??", as intended) and the paragraph
  indentation.
- The render has no editorial footnotes and no draft notes on these pages.

Readings I resolved with zooms. None of them is a discrepancy.
- p195: the faint mark before M_s/C_1 in the rewritten set is a minus sign. The render has a minus.
- p195: the "+" with a speck in "0 = A1 cos phi1 + A2 cos phi2" is a plus.
- p199 (65a): the crossed subscript in the denominator is the digit 2 (omega_2 - omega_1).
- p203: the speck in "C_1 - omega_Z^2" is a minus.

Readings kept as printed. These are not discrepancies.
- "statically-stable" (p200). The authors hyphenate this compound in the middle of a line elsewhere
  (p114, p179, p180).
- The missing full stop after "terms on I_L" (p200).

## (2) Discrepancies

| where | scan reading | compiled reading | severity |
|---|---|---|---|
| PDF 202, "The dynamical equations that must be solved become, in this case," | The line is indented: it starts a new paragraph after the f_x(t), f_y(t) display | The line is flush left: it continues the previous paragraph, with no paragraph break after the display | text |
