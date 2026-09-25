# Audit: ch4-sec5 corrections, round 1

Unit: chapters/ch4-sec5.tex (PDF 634-645, printed pp. 602-613). Items: D8 (PDF 642) and D3 (PDF 635).
Diff inspected: `git diff HEAD -- chapters/ch4-sec5.tex` (two hunks, lines 25-29 and 176-181; nothing else changed).

## What was checked

1. **D3, "Figure 19" (PDF 635, p.603).** The scan reads "from the sample plot presented in Figure 19, that the
   optimum weight decreases ...". The text is unchanged and still typed literally ("Figure 19,"). Only the
   faithful-pass note was reworded. The new note follows the doubt-note pattern used in Chapters 2 and 3: it gives
   the 1973 reading, names the evident target, gives a reason, then says "Neither the errata nor the supplements
   correct this; the reference is kept as printed." Each claim was checked:
   - "the chapter has no Figure 19": the Chapter 4 labels run ch4:fig:1 to ch4:fig:16, and inventory/ch4.csv ends
     at Figure 16 (PDF 641).
   - "the chapter's one plot of altitude against liftoff mass for several values of $k$": Figures 5(c)-9(c) are
     also plotted against $m_o$, but they show the *percent error* in $y_{\max}$ (checked on fig05c.png), not
     altitude. Figures 10-14 are trajectories. So the claim holds.
   - "its caption calls it an example of Bengen's maxima": the caption of Figure 16 says so.
   - "Neither the errata nor the supplements correct this": the errata sheet (PDF 664) lists only pp. 534, 583, 590
     and 591 for Chapter 4. The Chapter 4 supplements (PDF 666, 699-712) cover pp. 513-514, the multistage
     equations, Figure 4 and Table 1. The text layer of PDF 647-712 has no Chapter 4 "Figure 19" (the Figure 19
     hits on PDF 655 and 660 belong to other chapters).
2. **D8, "Section 5 of Chapter 2" (PDF 642, p.610).** The scan reads "for your tentative design according to the
   methods presented in Section 5 of Chapter 2." The text is now `Section~5 of Chapter~\ref{ch2}`, typed literally
   as the item specifies. The \ednote comes after the sentence's period. Each claim was checked:
   - The quoted 1973 reading matches the scan exactly.
   - `ch2:sec:4` is "Analytical Determination of the Dynamic Parameters" (chapters/ch2-sec4.tex). Its introduction
     computes the parameters "from a knowledge of the rocket's size, shape, and mass distribution", so that "a
     rocket design can be completely evaluated ... before construction is started". Its subsections 4.3-4.6 cover
     $C_1$, $C_2$, $I_L$ and $I_R$.
   - `ch2:sec:5` is "Experimental Determination of the Dynamic Parameters": "observations of the dynamic responses
     of actual vehicles" (torsion wire for the moments of inertia; $C_1$ and $C_2$).
   - The sentence's "tentative design" and the next sentence's "Adjust these values by altering the mass
     distribution, length, fin size ..." both point to working on paper, so "evidently meant" is supported.
   - "Neither the errata nor the supplements correct this": the same check as for D3 (p.610 is in neither source).
3. **Placement (section 9).** Both notes are in running prose, not in a display, caption or longtable. No
   \draftnote remains.
4. **Scope.** Only these two hunks changed. No other wording, labels or macros were altered.
5. **Labels.** No labels were added, removed or changed. There are no new equations, so no n-labels are needed.
6. **Section 15 notation.** $k$, $C_1$, $C_2$, $I_L$ and $I_R$ are in the listed forms.
7. **Render.** build/unit/ch4-sec5-1.png shows the note on "Figure 19" as E1 and build/unit/ch4-sec5-3.png shows the
   D8 note as E2. The text reads correctly, and the footnote marks come after the comma and the period. The PNGs
   (18:27:50) are newer than the source (18:27:43). The "??" marks are cross-chapter references
   (ch2, ch2:sec:4, ch2:sec:5), which the standalone unit build is expected to leave unresolved. The labels exist
   in chapters/ch2-sec4.tex and chapters/ch2-sec5.tex.

## Observation (not a discrepancy)

The D8 item asks for literal typing ("not \ref, per STYLE.md section 6"), and the unit does that. STYLE.md
section 6 requires literal typing only for a stale reference that does not exist in the book. It also says "Never
type a bare number for anything that has a label", and Section 5 of Chapter 2 does have one (`ch2:sec:5`). Chapter 2
handled a comparable wrong but existing target differently: `equation~\eqref{ch2:eq:25}` in chapters/ch2-sec3a.tex
kept the link, with the note naming (24). The rendered text is the same either way; only the hyperlink is lost. I
left this out of the table because the item is explicit. It is a consistency point for the chapter gate.

## Discrepancies

| where | expected (source/1973) | found | severity |
|---|---|---|---|
| none | | | |
