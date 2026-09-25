# M5 chktex review

Command (from the project root; chktex follows `\input` and `\include`):

    chktex -q -n1 -n2 -n3 -n8 -n9 -n12 -n13 -n19 -n21 -n22 -n24 -n25 -n26 -n27 -n29 -n30 -n36 -n38 -n44 -n46 main.tex

ChkTeX 1.7.9. **84 warnings, all reviewed; none is a genuine problem.** The same 84 remain after the fixes
below, because those fixes concern warning 2 (missing `~`), which the command disables.

| warning | count | where | verdict |
|---:|---:|:---|:---|
| 37 space after/before parenthesis | 36 | Symbols lists of Chapters 1-4 (`$d(\ )$`, `$\Delta(\ )$`, `$\int [\ ]\, d(\ )$`, "differential of ( )") | noise: the book's empty-argument notation, set as printed |
| 35 "use `\sec`" | 35 | ch4-sec3 (captions), ch4-sec4 (Tables 1-2), appendix-b, s-ch1:177, s-ch3:115 | noise: "sec" is the unit (seconds), in text. chktex raises 35 only in math mode: the whole-document run carries its lost math-mode state (see 49) into these files, and a per-file run of the same files gives none |
| 49 expected math mode | 3 | ch3-sec3a:275 (`alignat*` with `\text{\phantom{(}...}`), ch4-sec2a:91 and :365 (the evaluation bar `\Big]_{0,0}^{y_b,v_b}`) | false positive: chktex loses track of math mode at the unmatched `]`/`(` |
| 23 `'''` | 3 | ch3-sec3a:356, 362, 366 (`f'''`) | noise: the Blasius third derivative in math |
| 10 solo `]` | 3 | ch1-sec2a:307 (`At\bigr]_{t=t_b} - At\bigr]_{t=0}`), ch3-sec2b:396 (`label=\arabic*)`) | noise: evaluation brackets and an enumerate label |
| 17 unbalanced `(` / `[` | 2 | main.tex (document totals) | noise: the brackets above, `\phantom{(}` and the Summary's `\Big]`. A per-paragraph count of `(` and `)` in all 64 front, back and chapter files found no unclosed parenthesis in the prose |
| 6 no italic correction | 1 | s-ch2-2022:10 (`{\itshape ... text.\par}`) | noise: the paragraph ends before the group closes |
| 40 punctuation inside math | 1 | s-ch1:177 (`meters/sec.$^{2}$`) | noise: the period belongs to the abbreviation; the scan (PDF 671, 400 dpi crop) prints "meters/sec.²" |

A per-file run (`-I0`) over the 64 files of frontmatter/, backmatter/ and chapters/ gives no warning 35 or 40 (and reports
the two evaluation bars of ch4-sec2a as warning 10 instead of 49); it adds
only more noise: warning 11 at ch4-sec2a:397 and :400 (`y_1 + \ldots + y_{n-1}` in an editor's note, the form
STYLE.md section 15 prescribes), warning 15 at ch3-sec3a:269-273 (the `\phantom{(}` of the `alignat*`), warning 10
at s-ch4-summary:62 (the evaluation bar `\Big]_{0,v_1}^{y_2,v_2}`) and per-file warnings 17 for the same brackets.

## Checks the command leaves out, done by grep

- **`~` before `\ref`/`\eqref` after its noun** (warning 2 is disabled): a search for Figure(s), Table(s),
  Section(s), Chapter(s), equation(s), Reference(s), Plate(s), Appendix, page(s), Step(s) followed by a space or
  a line break and `\ref`, `\eqref` or `\hyperref` found 9 cases, all fixed:
  - frontmatter/about-this-edition.tex:149 `new equations~\eqref{ch1:eq:5}`
  - :152 `normal force equation~\eqref{ch1:eq:20}`
  - :153 `adds equations~\eqref{ch1:eq:n21}`
  - :173 `its coefficients, equations~\eqref{ch2:eq:115}`
  - :181 `with equations~\eqref{ch3:eq:97}`
  - :183-184 `the induced-drag equations~\eqref{ch3:eq:n144A}` (the noun ended the previous line)
  - :198 `the new equations~\eqref{ch4:eq:n7a}`
  - :204-205 `Equations~\eqref{ch4:eq:40}` (same)
  - backmatter/supplement/s-ch2-1994.tex:76 `the 1973 equations~\eqref{ch2:eq:89}`

  The remaining untied references are the second members of lists and ranges ("\eqref{a} to \eqref{b}",
  "Figures~\ref{a}, \ref{b}"), which is the usual practice.
- **Ellipses**: no `...` in the text (warning 11 is enabled and found none either); `\ldots` is used.
- **Quotes**: no straight `"`, no Unicode quotes or ellipsis characters (warnings 18 and 32-34 found none).
- **Space before a note**: no space or line break before `\footnote` or `\ednote` (warning 42 found none).
