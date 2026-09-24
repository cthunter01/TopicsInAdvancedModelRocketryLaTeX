# Audit: ch2-sec2 corrections, round 1

Unit: chapters/ch2-sec2.tex (PDF 111-122). Item to apply: D2 (PDF 121).

## What was checked

- `git diff HEAD -- chapters/ch2-sec2.tex`: one hunk only, at the "where $f_x(t)$ is read ..." sentence
  after equation (13). The printed sentence is unchanged: the diff adds one `\ednote` after its full stop,
  and the following sentence ("With the presence of a constant roll rate the equations become") is re-wrapped
  with its wording unchanged. No equation, label, figure or other prose changed (item 3 of the check).
- 1973 page PDF 121 (printed p.91): the sentence reads "where f_x(t) is read, "function of time, about the
  X-axis" and f_y(t) is read, "function of time, about the Y-axis"." It matches HEAD and the working file.
- Symbols list, PDF 89 (printed p.59): "f_x(t) pitch forcing function", "f_y(t) yaw forcing function";
  PDF 90 (printed p.60): "α_X yaw angle", "α_Xm maximum yaw angle", "α_X0 yaw angle at t = 0", "α_Y pitch
  angle". The note quotes both glosses and both angle definitions accurately.
- The note's claim "Here, as throughout this section, f_x(t) is the forcing about the X axis, which drives
  the yaw angle α_X" was checked against the unit. f_x(t) is the right-hand side of the α_X equation in (13) and (14).
  The sentence introducing (13) says "forcing in yaw and pitch", in the order α_X, α_Y. Section 2 treats the
  X quantities as yaw ("our case of yaw displacement" before (10); the Figure 9 caption "yaw deflection
  α_X"). The inference that the list's two glosses are interchanged is supported by the scan.
- "Neither the errata nor the supplements correct this": the 1973 errata sheet (PDF 664) has only
  pp.108, 113 and 144-145 for Chapter 2, and the 1994/2022 supplements (PDF 676-687) cover pp.186-196,
  Figure 36, pp.251-254 and 259. None touches p.59 or p.91. The statement is accurate.
- Placement (STYLE.md section 9): the note is in prose, attached to the sentence that the item names. It is
  not inside a display or a caption. It is one note, as the item asks. At about 75 words it is longer than a
  one-line remark but has no redundant content.
- Cross-reference constraint: the note refers to "the chapter's Symbols list" itself, not to the other agent's
  note in ch2-symbols.tex. Its content agrees with that note (f_x/f_y glosses interchanged).
- Notation (STYLE.md section 13): `$f_x(t)$`, `$f_y(t)$` keep typewritten lowercase subscripts; `\alpha_X`,
  `\alpha_Y` use uppercase axis subscripts; the note writes "X axis" as the section's prose does (lines 14,
  136).
- Labels: no label added, removed or changed. `ch2:eq:13` and `ch2:eq:14` are intact.
- Rendering: build/unit/ch2-sec2.pdf (05:25:16) postdates the edit (05:25:09). On build/unit/ch2-sec2-6.png the
  marker E1 follows "Y-axis”." and the footnote "Editor's note: ..." appears at the bottom of the same page with
  correct math. Equations (13), (14) are numbered in sequence. The PDF text has no "??". The log has no warnings
  and no overfull boxes.

## Discrepancies

none
