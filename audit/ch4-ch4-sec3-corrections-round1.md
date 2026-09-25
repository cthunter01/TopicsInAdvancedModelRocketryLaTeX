# Audit: ch4-sec3 corrections, round 1

Unit: chapters/ch4-sec3.tex (Section 3, "The Non-Oscillating Rocket ...", PDF 596 to mid-610, printed pp. 564-578).
Items for this unit: D14 (PDF 601), "0.453 Kg" -> "0.453 kg", silently.

## What was checked

1. **Item applied as specified.** 1973 page PDF 601 (printed p. 569), last line, prints "as 453 grams (0.453 Kg), this being the
   maximum legal liftoff". git HEAD line 153 has "(0.453 Kg)"; the working tree has "(0.453 kg)". Only the case of K changed.
   The rest of the sentence is untouched. corrections/ch4.md (D14 and the Decisions: "'0.453 Kg' fixed silently") calls for
   no note, and none was added. The claim that the chapter writes kg everywhere else holds: `grep Kg chapters/ch4-*.tex`
   finds nothing now, and the Figure 10-14 captions in this unit use kg.
2. **Notes.** The unit has no `\ednote`, `\edcap` or `\draftnote`, before or after the change. No substantive change was
   made, so none is needed.
3. **Doubt notes.** The only other doubt on these pages is D15's "slightly more than doubled" (PDF 601), which is minor
   with no note. No note was added for it, which is correct. No "check" items belong to this unit.
4. **Scope.** `git diff HEAD --stat` shows 1 file, 1 line changed (1 insertion, 1 deletion), and `git status` shows only
   chapters/ch4-sec3.tex modified. No other source entry falls in pp. 564-578:
   - Errata (PDF 664): the Chapter 4 entries are for pp. 534, 583, 590 and 591.
   - The 1994 text changes (PDF 699-702): pp. 513-514 and the Symbols list.
   - The Summary (PDF 703-710): Section 2.2 only. Page 703 confirmed this.
   - Figure 4 (PDF 711): p. 548.
   - Table 1 (PDF 712): p. 595.
5. **Labels.** No label, equation or `\tag` was touched.
6. **Section 15 notation.** The prose unit stays as text ("0.453 kg"), as section 15 ("Numbers and units") requires.
   `$m_o$` in the same sentence was not changed.
7. **Render.** build/unit/ch4-sec3.pdf and the PNGs (18:25:59-18:26:09) are newer than the edit (18:25:49). Page
   build/unit/ch4-sec3-4.png shows "was taken as 453 grams (0.453 kg), this being the maximum legal liftoff mass for
   model rockets in the United States." It renders correctly and the layout is normal.

## Discrepancies

none

| where | expected (source/1973) | found | severity |
|---|---|---|---|
