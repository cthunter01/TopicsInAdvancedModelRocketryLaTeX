# Audit ch2-sec3c, round 1, part 1 (PDF 168-180)

## Scope and counts

Scan pages checked: figures/pages/p168.png to p180.png (on p168 only the part from the 3.2 heading down).
Render pages checked: build/unit/ch2-sec3c-01.png to -08.png. The content of p168-p180 is on render pages 1-8 (up to the "Also," display at the top of page 8). Page 8 was also read past that point to check the seam.

- Headings: 2 (3.2 Dynamical Behavior at a Constant, Nonzero Roll Rate; 3.2.1 Generalized Homogeneous Response).
- Numbered equations: 8. (51) p168, (52a) p172, (52b) p173, (53a)-(53d) p173, (54) p178. The numbering is in sequence and has no offset. The survey was correct.
- Unnumbered display groups: 45, compared symbol by symbol. They include the homogeneous pair on p168, the four derivatives and both three-line substitutions on p169-170, the quartic on p171, X/Y/Z on p172, the reduced cubic work on p174-175, A-D in a, b on p177, the a^2/b^2 biquadratic solutions on p178, and the limiting-case root sets on p178-180. I zoomed into the scan for: (51) and the homogeneous pair (p168), the pitch substitution line 3 (p170), the quartic (p171), the (53c)/(53d) substitutions (p177), a^2/b^2 and (54) (p178).
- Inline formulas: about 40.
- Prose paragraphs: about 30. I compared them sentence by sentence and checked emphasis (quartic, physics, limiting behavior, approaches, in the limit, recover, more general, force-free precession, normalizing, roots, same, guess, sum, product, two, are, physical, both, biquadratic, irrevocably lost, absolute value).
- Figures and tables: none.
- Editorial and draft notes: 1 draft note ("0 clipped at margin", p170 pitch substitution, line 3). Its statement is true: the scan shows only the left arc of the final 0.

Checked and not reported:
- The dot over phi in "sin(wt + phi)" in line 3 of the p170 pitch substitution, and the dot on the Y of the p177 (53d) substitution, are specks.
- The b^2 radical on p178 has no factor 1/2, while the a^2 radical has one. The render reproduces this faithfully.
- The sentence "In the reduced case of Y = Z = 0 ..." on p176 starts a new line at the left margin after a short line. Whether that is a paragraph break is ambiguous, so the render's run-on is accepted.

## Discrepancies

| where | scan reading | compiled reading | severity |
|---|---|---|---|
| PDF 169, "Now it is clear that the derivative formulae ..." (after (51)) | flush left, continuing the paragraph after display (51) (no paragraph indent; x=70, same as the following lines) | set as a new indented paragraph | layout |
| PDF 171, "From the last equation above we can obtain D in terms of ω as" | flush left after the display (x=81, same as the following lines), not a new paragraph | set as a new indented paragraph | layout |
| PDF 171, "Now this is a quartic equation in ω, ..." (after the normalized quartic) | flush left after the display (x=81, same as the following lines), not a new paragraph | set as a new indented paragraph | layout |
| PDF 175, "I can now exercise on a reduced scale the techniques ..." | flush left after the -ABC display (x=87, same as the following lines), not a new paragraph | set as a new indented paragraph | layout |
