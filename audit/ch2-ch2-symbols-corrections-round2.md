# Audit: ch2-symbols corrections (item 4 note, D1), round 2

## Sources compared

- Diff: `git diff HEAD -- chapters/ch2-symbols.tex`: two hunks only, a two-line LaTeX comment and the
  `$\CNa$` row (item 4 note), and the `$F(\alpha_X)$` row (D1 note). Every other row, the header and the
  longtable spec are identical to HEAD.
- 1973 Symbols list: figures/pages/p085.png ($\CNa$, $(\CNa)_B$ ... $(\CNa)_{T(B)}$), p086.png
  ($(\CNa)_1$, $F(\alpha_X)$, $G(\Omega_X)$), p089.png ($f_x(t)$, $f_y(t)$), p090.png ($\Omega_{X0}$,
  $\Omega_{Y0}$, $\alpha_X$, $\alpha_{Xm}$, $\alpha_{X0}$, $\alpha_Y$), p091.png ($\alpha_{Y0}$), p092.png
  (no further pitch/yaw entries).
- 1994 supplement p676.png-p677.png ("Correction to original pages 186 through 196 of Chapter 2"); the
  1973 page 186 (p216.png) for where the replacement starts inside Section 4.1.
- Current chapters/ch2-sec4.tex (Section 4.1 opening as corrected) for consistency with the note.
- Render build/unit/ch2-symbols-1.png, -2.png (built 05:30:34, after the last edit of the .tex at
  05:30:32) and build/unit/ch2-symbols.log. Not rebuilt.

## Round-1 finding (scope of the rename in the item-4 note)

Now fixed. The note reads: "It rewrites the passages that introduce the normal force at the start of
Section 4.1, where ``normal force coefficient'' still names $C_N$, and in the rest of that section (1973
pages 189--196) and in the captions of Figures 34, 35 and 36 it replaces ``normal force coefficient'' by
``normal force curve slope'', except in the paragraph on body tube sections."

- p676: the rewritten opening keeps "normal force coefficient" for $C_N$ ("the concept of the normal force
  coefficient $C_N$", the $A_r$ gloss, "the curve of the normal force coefficient versus angle of
  attack"); the replaced paragraph "Now the normal force curve slope of the rocket ..." (bottom of 1973
  page 187) no longer contains the phrase. So "still names $C_N$" is true wherever the phrase remains.
- p216: Section 4.1's first paragraph ("In March, 1967, ...") is not replaced; the replacement starts with
  "Barrowman's method is based on ...". "the passages that introduce the normal force at the start of
  Section 4.1" reads correctly as the opening passages that deal with the normal force.
- p677: "In the rest of Section 4.1, from page 189 thorough page 196 and in the captions of Figures 34,
  35, and 36 ... except in the paragraph discussing body tube sections on page 193": the note's scope,
  page range, figures and exception match exactly.
- The note agrees with the item-4 note already in chapters/ch2-sec4.tex (Section 4.1 opening).

## What was checked

Item 4 note
1. One note, on the `$\CNa$` row only; 1973 gloss "normal force coefficient" kept (p085).
2. "(correction to pages 186--196)" matches the supplement heading; "Mandell's June 1994 supplement" is the
   wording used by the ch1 notes and the ch2-sec4 note.
3. Definition "the slope of the curve of the normal force coefficient $C_N$ versus angle of attack at
   $\alpha = 0$" agrees with p676 (derivative of the curve measured at $C_N = 0$, $\alpha = 0$; "often
   referred to as the normal force curve slope").
4. Rename scope, page range, captions and exception: see above, now exact.
5. "The supplement does not update this Symbols list" true (p676-p679); the seven $\CNa$ rows are
   byte-identical to HEAD and read as on p085-p086; "$(\CNa)_B$ through $(\CNa)_1$" covers B, n, S, T,
   T(B), 1 in list order.

D1 note
6. Glosses re-verified on the scan: $F(\alpha_X)$ "function of pitch angle", $G(\Omega_X)$ "function of
   pitch angular velocity" (p086); $f_x(t)$ "pitch forcing function", $f_y(t)$ "yaw forcing function"
   (p089); $\Omega_{X0}$ "yaw angular velocity at t = 0", $\Omega_{Y0}$ "pitch angular velocity at t = 0",
   $\alpha_X$ "yaw angle", $\alpha_{Xm}$ "maximum yaw angle", $\alpha_{X0}$ "yaw angle at t = 0",
   $\alpha_Y$ "pitch angle" (p090); $\alpha_{Y0}$ "pitch angle at t = 0" (p091). The note's lists are
   exact and complete ($\Omega_X$, $\Omega_Y$ are glossed by axis, not pitch/yaw).
7. Text evidence: "our case of yaw displacement" is chapters/ch2-sec2.tex line 177, inside Section 2.2
   (lines 80-202); "impulsive input in yaw" with $f_x(t)$ is chapters/ch2-sec3b.tex lines 20-24, inside
   3.1.3. The inference "evidently interchanged" in the F, G, $f_x$, $f_y$ entries is supported.
8. "Neither the errata nor the supplements correct this; the entries are kept as printed": true; the rows
   are unchanged from HEAD. Unchanged since round 1.

Placement, scope, labels, notation
9. Both notes in one-line `\multicolumn{1}{l@{}}{...}` cells (STYLE.md section 9, ch1-symbols precedent);
   the comment is not typeset.
10. No other change in the unit; no labels added, removed or changed; all `\ref` targets exist
    (ch2:sec:4.1, ch2:fig:34-36 in ch2-sec4.tex; ch2:sec:2.2 in ch2-sec2.tex; ch2:sec:3.1.3 in
    ch2-sec3b.tex).
11. Notation per STYLE.md section 13 (`\CNa`, `C_N`, `\alpha_{X0}`, `\Omega_{Y0}`, typewritten `f_x(t)`).

Render
12. Page 1: "normal force coefficient^E1", "function of pitch angle^E2", in sequence; E1 printed in full;
    E2 continues at the foot of page 2 (ordinary TeX footnote split, text complete). No Overfull box in
    the log; the only `??` are the six other-unit references (expected in a unit build).

## Discrepancies

none
