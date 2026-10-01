# v2 consistency check: ch2/fig17

Issue resolved here: (1) the lines from the peak to the axes use the house `peak line` style; the local
definition is deleted. Verifier only (no edits).

Sources checked: `figures/v2/ch2/fig17.tex` against the fixer's pre-fix copy (`scratchpad/ch2fix/g1-peaks/before/`);
`figures/v2/tamrfig.sty`; STYLE.md section 16; scan `figures/ch2/fig17.png`; inventory row `ch2-fig17`;
`audit/v2-ch2-fig17-round1.md`; `build/v2/png/ch2-fig17-compare.png`; my own scratch build and 300 dpi renders
of the pre-fix and current PDFs.

Checks made:
- Source diff: only the local `\tikzset{peak line/...}` (and its comment line) is removed, and the header comment
  is updated. No `\tikzset` remains in the file. The house `peak line` is identical to the deleted one.
- Render: the current and pre-fix PDFs at 300 dpi (1552 x 831 px) differ in 0 pixels. Size 372.365 x 199.403 pt
  (5.17 x 2.77 in), unchanged.
- Lettering: the same 23 words at the same positions before and after. The peak tick
  $\frac{M_s}{C_1}\bigl(1 + e^{-\frac{\pi D}{\omega}}\bigr)$ keeps its minus sign and the art's parentheses.
  $\frac{M_s}{C_1}$, 0, $\frac{\pi}{\omega}$, $\alpha_X$ (rad) and $t$ (sec) are all present.
- Against the scan and the inventory: the solid lines run to the peak level and from the peak down to
  $\pi/\omega$, as printed. The $M_s/C_1$ level stays dashed (`guide`).
- Build: compiles cleanly; no warnings; all fonts embedded.
- The `peak line` part of round-1 finding 4 is resolved. The y-label override is out of scope and unchanged.

## Findings

None.

## Verdict: pass
