# v2 consistency check: ch2/fig16

Issue resolved here: (1) the lines from the peak to the axes use the house `peak line` style; the local
definition is deleted. Verifier only (no edits).

Sources checked: `figures/v2/ch2/fig16.tex` against the fixer's pre-fix copy (`scratchpad/ch2fix/g1-peaks/before/`);
`figures/v2/tamrfig.sty` (`peak line`, `guide`); STYLE.md section 16; scan `figures/ch2/fig16.png`; inventory row
`ch2-fig16`; `audit/v2-ch2-fig16-round1.md`; `build/v2/png/ch2-fig16-compare.png`; my own build into the scratch
dir (pdflatex as in the Makefile) and 300 dpi renders of the pre-fix and current PDFs.

Checks made:
- Source diff: only the local `\tikzset{peak line/...}` (and its comment line) is removed, and the header comment
  now names `guide` and `peak line`. No `\tikzset` remains in the file. `\draw[peak line]` now resolves to the
  house style (draw=ink2, 0.4pt, solid), which is identical to the old local definition.
- Render: the current and pre-fix PDFs at 300 dpi (1391 x 837 px) differ in 0 pixels. Size 333.714 x 200.708 pt
  (4.63 x 2.79 in), unchanged.
- Lettering: pdftotext gives the same 17 words at the same positions before and after ($\alpha_X$ (rad),
  $\frac{2M_s}{C_1}$, $\frac{M_s}{C_1}$, 0, $\frac{\pi}{\omega_n}$, $t$ (sec)).
- Against the scan and the inventory: the solid lines from the axis to the $2M_s/C_1$ peak and from the peak down
  to $\pi/\omega_n$ are as printed. The asymptote $M_s/C_1$ stays dashed (`guide`), as the inventory and caption require.
- Build: compiles cleanly; no warnings, no overfull boxes; all fonts embedded.
- Round-1 finding 2 (the local `peak line`) is resolved by the house style. Finding 1 (the y-label override) is
  out of scope and unchanged.

## Findings

None.

## Verdict: pass
