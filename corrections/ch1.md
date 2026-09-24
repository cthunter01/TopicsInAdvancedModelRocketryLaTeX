# Chapter 1 — corrections checklist

Sources: 1973 errata sheet (PDF 664/665); "Vector notation for pressure term" (PDF 666, Mandell 1 June 1994);
"Changes to text of Chapter 1" (PDF 667-674, Mandell June 1994); "Correction to original page 40" (PDF 675).
Printed page = PDF page − 30.

Status: todo / applied (with \ednote location) / deferred (reason)

| # | Source (PDF) | Original location | Change | Status |
|---|---|---|---|---|
| 1 | 664 | p.5 Symbols (PDF 35) | second "Δ( )  sum of all ( )" should read "Σ( )  sum of all ( )" (typo fix; no footnote needed) | todo |
| 2 | 673 | Symbols table | add symbols $\vec{A}_e$, $A_e$, $P_a$, $P_e$, $c_{\mathrm{eff}}$ with the meanings given on PDF 673; place alphabetically | todo |
| 3 | 674 | p.14 Figure 2 (PDF 44) | replace drawing and caption with the new Figure 2 (drawing + caption + NOTE paragraph on PDF 674). Keep the 1973 figure for the supplement Part | todo |
| 4 | 668 | p.16 (PDF 46) after line 3 | insert the new paragraph about the nozzle exit plane | todo |
| 5 | 668-669 | p.16 from "Now the connection…" to end of page | replace with the new text, new eq. (1) and its "where" list, ending "…the exhaust stream" | todo |
| 6 | 669-670 | p.18 (PDF 48), whole page | replace with the new page: eq. (2) $F = c\,(dm_e/dt) + (P_e - P_a)A_e$ and the paragraph on over- and under-expansion | todo |
| 7 | 671 | p.19 (PDF 49), whole page | replace with the new page, adding eq. (2a) $\dot m = F/c$ | todo |
| 8 | 672-673 | pp.30-31 (PDF 60-61), from just after "How powerful is it?" to the end of §2.1 | replace with the new text and new eqs. (5), (6), (7); the old (5) $I_{sp} = I_t/m_f$ disappears | todo |
| 9 | 675 | p.40 (PDF 70), paragraph "According to the method… Barrowman…" through "…shown in Figure 7" | replace with the new paragraph and new eqs. (20), (21), (22); "[All subsequent equation numbers must be increased by 2]" → old (21), (22) on p.42 become (23), (24); update the p.42 sentence citing "(19), (20), and (21)" and note the $C_n$ → $C_{N\alpha}$ notation change with an \ednote | todo |
| 10 | 666 | everywhere the pressure term appears | write $(P_e - P_a)\vec{A}_e$ with the arrow over $A_e$ only, never over the whole term | todo |

Notes
- Items 3-9 are substantive: each gets an `\ednote` stating what the 1973 text read. Item 1 is a pure typo fix.
- Item 9 changes displayed numbers: after it, `check_numbering.py` needs the renumber map `{21: 23, 22: 24}` in `inventory/ch1-renumber.json`.
- The symbol table's entry "$C_n$ normal force coefficient" is not updated by any correction; flag with an \ednote when item 9 is applied.
