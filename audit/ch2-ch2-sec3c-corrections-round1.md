# Audit: ch2-sec3c corrections, round 1

Unit: chapters/ch2-sec3c.tex. Items: errata item 3 (PDF 664, "Page 144 and 145") and doubt D9 (PDF 178).
Compared against: git HEAD (faithful 1973 transcription), figures/pages/p664.png and p665.png (both errata
sheets), p174.png, p175.png, p178.png, and a 300 dpi zoom of the a^2/b^2 displays on PDF 178
(build/zoom/audit_ch2-sec3c_r1-p178-178.png). Rendered pages build/unit/ch2-sec3c-04.png and -06.png
(built 05:25:41, after the last edit at 05:25:36).

## What was checked

1. **Item 3, extent and symbols.** The equations on printed p.144 (PDF 174) are: omega^2(omega^2+Y+Z)=0,
   the two omega = +-sqrt forms, the quartic with Y=Z=0, the factored form, (omega-A')(omega-B')(omega-C')=0,
   the expanded cubic, and -(A+B+C)=2X omega_Z. The last two are the expanded cubic and -(A+B+C)=2X omega_Z.
   The first two on p.145 (PDF 175) are (A+B)C+AB = 5/4 X^2 omega_Z^2 and -ABC = X^3/4 omega_Z^3.
   The diff primes every A, B and C in exactly these four equations: the cubic
   omega^3 - (A'+B'+C')omega^2 + [(A'+B')C' + A'B']omega - A'B'C' = 0, and the three coefficient equations.
   Nothing else is touched: the factored product (already primed in 1973), the A'/B'/C' root values on p.145,
   and the quartic roots A, B, C, D (roots (54) and after) are unchanged. Both errata sheets (p664 and p665)
   give the same instruction.
2. **Item 3 note.** There is one \ednote, in "which, when expanded, becomes", which is the sentence introducing the first corrected
   display. It is outside the display (STYLE.md section 9). It says the correction follows the 1973 errata sheet and that the 1973 printing had
   no primes. It quotes the four 1973 equations, and each one matches p174/p175 and git HEAD symbol by symbol.
   "This equation and the three coefficient equations that follow" is the right count.
3. **D9, 1973 reading.** The zoom of PDF 178 confirms that the a^2 display has "+- 1/2 sqrt(...)" and the b^2 display
   has "-+ sqrt(...)" with no 1/2. The transcription keeps the b^2 display as printed (not changed).
4. **D9, algebra.** From the book's own step after (53b), b^2 = -(Y+Z) + X^2 omega_Z^2/4 - a^2. With
   a^2 = X^2 omega_Z^2/8 - (Y+Z)/2 +- (1/2) sqrt((Y+Z-X^2 omega_Z^2/4)^2 + Z X^2 omega_Z^2), this gives
   b^2 = X^2 omega_Z^2/8 - (Y+Z)/2 -+ (1/2) sqrt(...). So the missing 1/2 is confirmed. Roots C and D of (54) carry
   "- 1/2 sqrt(...)", as the note says. Neither errata sheet (p664, p665) has a page 148 entry, and the 1994/2022 supplements
   cover pp.186-196, 251-254 and 259 only, so the note's statement "Neither the errata sheet nor the 1994 and 2022 supplements correct it"
   is accurate. The note is in the introducing sentence "Solving for b^2 as obtained in (53b), we have", which
   is correct placement. It states only what the scan and the algebra support. Minor wording: "gives -+ 1/2 sqrt(...)" means "gives the radical term -+ 1/2 sqrt(...)".
   The context ("The radical in this expression ...") makes that clear, so it is not flagged.
5. **Scope.** `git diff HEAD -- chapters/ch2-sec3c.tex` has exactly two hunks, the two items above. No other
   line of the unit changed.
6. **Labels.** No labels were added or removed. The D9 note's \eqref{ch2:eq:54} resolves to (54) in the unit build.
   The log's only undefined references are ch2:sec:2.3 and ch2:eq:25, which belong to other units (expected).
7. **Notation (STYLE.md section 13).** Corrected passages use \omega_Z (uppercase), and the primes are typed as A', B', C'.
8. **Rendering.** Page 4 shows the note marker E2 after "becomes", the primed cubic and the aligned primed coefficient
   equations, and a correct footnote E2. Page 6 shows E3 after "we have", the b^2 display unchanged, and the footnote E3
   with a working (54) link. There is no ?? inside this unit and the layout is not broken.

Observation (outside the unit, not a discrepancy): corrections/ch2.md still shows item 3 and D9 as "todo".
The status column still needs its update: item 3 "applied (\ednote "This equation and the three coefficient equations ...")", D9 "\ednote added ("The radical in this expression ...")".

## Discrepancies

none

| where | expected (source/1973) | found | severity |
|---|---|---|---|
| none | | | |
