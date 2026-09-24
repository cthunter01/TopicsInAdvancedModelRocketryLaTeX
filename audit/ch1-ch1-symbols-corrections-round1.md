# Audit: ch1-symbols corrections (items 1, 2, 9), round 1

## Sources compared

- Diff: `git diff HEAD -- chapters/ch1-symbols.tex` (3 hunks, 11 insertions, 3 deletions).
- Errata: figures/pages/p664.png ("Page 5, line 3, should read Σ( ) sum of all ( )").
- Supplement: p666.png (vector notation note, 1 June 1994), p667.png (cover note "Changes to text of
  Chapter 1", June 1994), p673.png (page 6: the five symbols to add), p675.png (correction to page 40).
- 1973 pages: p033.png (Symbols page -3-, the $C_n$ row), p035.png (page -5-, the two Delta rows),
  p070.png (page 40, the 1973 normal-force paragraph).
- Render: build/unit/ch1-symbols-1.png, -2.png (built 18:46:06, after the last edit of the .tex at
  18:46:05; the pages show the E1/E2 notes and the Sigma row, so they are the corrected version).
  Log: no Overfull hbox, no undefined references; `pdftotext` finds no "??".

## What was checked (21 items)

Item 1 (errata p664)
1. Second "sum of all ( )" row: symbol now `$\Sigma(\ )$`; matches the errata. Renders as "Σ( )".
2. Meaning "sum of all ( )" unchanged.
3. Preceding row `$\Delta(\ )$ increment of ( ), change in ( )` unchanged (p035 confirms it is a Delta).
4. No \ednote added (pure typo fix); the old "transcribed as printed" comment replaced by a comment citing the errata.

Item 2 (supplement p673) -- each row compared word by word with the typescript
5. `$A_e$` "magnitude of nozzle exit plane area" -- exact.
6. `$\vec{A}_e$` "nozzle exit plane area written as a vector whose direction is forward along the vehicle centerline" -- exact.
7. `$P_a$` "ambient pressure" -- exact.
8. `$P_e$` "pressure of exhaust gas at nozzle exit plane" -- exact.
9. `$c_{\mathrm{eff}}$` "magnitude of effective exhaust velocity (\emph{also} called equivalent exhaust velocity), whose direction is assumed to be rearward along the vehicle centerline" -- exact; the underlined "also" is set in italics as the 1973 $v$ row does.
10. Position, A block: between $A$ and $A_r$ (uppercase Roman block, e < r).
11. Position, P block: between $N$ and $R$.
12. Position, c block: after $\vec{c}$, before $d(\ )$ (lowercase block).
13. ONE \ednote (E1), in the Meaning cell of the first added row in table order ($A_e$); it names all five symbols, cites "Changes to text of Chapter 1", p. 6 (p673 carries page number 6; the cover p667 carries that title and "June 1994"), and states they are absent from the 1973 list (true: p033-p035).

Item 9 (note only)
14. E2 on the existing `$C_n$ normal force coefficient` row: says the 1994 correction to page 40 rewrites the discussion in terms of the normal force curve slope $\CNa$, "the slope of the normal force coefficient (there written $C_N$) versus angle of attack" -- matches p675 ("where C_Nα is the slope of the curve of the normal force coefficient versus angle of attack ... normal force curve slope"; p675 writes $C_N$).
15. E2 says the supplement does not update the table and the 1973 entry is kept as printed -- true: p673 lists no $C$ symbol; the row text is unchanged and matches p033.

Pressure-term notation (p666)
16. The only vector-area symbol in this unit is `$\vec{A}_e$`: arrow over $A_e$ only (renders with the arrow over the A, e as subscript), consistent with `$\vec{F}$`, `$\vec{c}$`, `$\vec{g}$`.

Scope
17. Whole diff inspected: only the Sigma row (+ comment), the five new rows, the two \ednote cells, and one explanatory comment block (lines 8-10). No other row, the table preamble, heading or label touched.
18. Labels: this unit has no equations, figures or tables with numbers; `ch1:sec:symbols` unchanged. Nothing to renumber; no \tag.

Render
19. Page 1: E1 mark after "magnitude of nozzle exit plane area", E2 mark after "normal force coefficient"; both footnotes typeset at the foot of page 1 with the "Editor's note:" prefix; $\vec{A}_e$, $P_a$, $P_e$, $c_{\mathrm{eff}}$ rows in place; column alignment of the two `\multicolumn{1}{l@{}}` cells identical to the p{} cells.
20. Page 2: "Σ( ) sum of all ( )" follows "Δ( ) increment of ( ), change in ( )"; no broken layout, no "??".
21. Build log clean (no Overfull > 20pt, no undefined references, no lost-footnote warning).

## Observations that are NOT discrepancies

- $A_e$ is placed before $\vec{A}_e$ although the typescript lists the vector first. This follows the
  1973 table's own convention (scalar before vector: $F$/$\vec{F}$, $c$/$\vec{c}$, $g$/$\vec{g}$) and
  keeps "first added row" = $A_e$, which carries the note as instructed.
- STYLE.md section 9 prefers \edcap inside table rows; the task explicitly asked for an \ednote in the
  Meaning cell. The applier found that a manyfoot footnote inside a longtable p{} cell is dropped and
  set the two note-bearing cells as one-line `\multicolumn{1}{l@{}}` cells. The render confirms both
  footnotes appear. The workaround depends on those two cell texts staying short enough not to wrap
  (they are 6 and 3 words); the comment in the file documents this.
- p675 carries no date of its own; E2's attribution "Mandell's June 1994 supplement" follows the
  framing in corrections/ch1.md and the task (the page is in the same typescript series as p668-673).
- The 1973 page 40 itself (p070) already writes $C_{n\alpha}$ and calls it the "normal force
  coefficient", so the Symbols row $C_n$ never matched the 1973 text exactly either. E2 does not say
  this; item 9 did not ask for it. It could be added to E2 in a later pass if wanted, but it is not a
  discrepancy in what was asked for.

## Discrepancies

| where | expected (supplement/1973) | found | severity |
|---|---|---|---|

none
