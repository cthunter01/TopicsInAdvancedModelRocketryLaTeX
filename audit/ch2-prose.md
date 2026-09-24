# Audit: Chapter 2 prose check (tools/prose_diff.py)

Every page that tools/prose_diff.py did not pass was checked against the scan by the assembly step. That step's conclusions are recorded here because build/prose-ch2.md is regenerated on every build.

prose_diff ch2 (PDF pages 83-290): 183 pages checked. 122 pass, 60 inspect, 1 missing (p274), 25 skipped (fewer than 30 tokens). 163 windows flagged.

Method. For every non-pass page I aligned the OCR tokens against the compiled text with fuzzy token matching (scratch scripts, nothing in the repo). I listed each unmatched stretch and each real-word OCR bigram that is absent from the PDF, then checked every candidate against the OCR line, the .tex and, where it was unclear, the scan. I read the scans in full for p246, p274 and p281, and zoomed on p096. I also spell-checked all of the compiled Chapter 2 text: the only flags were technical words, author spellings the book uses ("Naperian"/"Napierian", "miniscule") and ednote superscripts ("givesE"). No dropped, garbled or duplicated Chapter 2 prose was found, so no source change was needed.

Per-page conclusions:
- p274 (missing): the Figure 50 page. 25 of its 37 OCR tokens are the hand-lettered panel sub-captions ("I_L too large: zeta too small, resonance severe ...") inside the fig50.png artwork. The manifest note keeps them in the crop on purpose. The caption is transcribed in full at chapters/ch2-sec6.tex:171-172. This is a false positive; fine.
- Figure pages whose OCR is mostly artwork labels, all fine: p115 (Fig. 9 axis labels "Linear approximation / Range of validity"; caption present), p140 (Figs 14-15; caption verified word for word), p254 (Fig. 44 labels "pulley, rocket body, bearing support plate"), p260 (Fig. 46 table and graph labels).
- p85: Symbols list with hand-lettered symbols. OCR garbles such as "critical.ly" and "nozmal"; all meanings are present. Fine.
- Pages that are mostly hand-lettered maths, or tables of it, where the OCR is noise and every prose sentence is present. All fine: p100, p113, p116 and p129 (Present Treatment / Gurkin Report tables), p127, p134, p136, p137, p142, p146, p163, p172, p173, p182, p183, p195, p204, p206, p208, p232, p245, p270 (numeric parameter values), p283.
- Typed prose with badly degraded OCR. Examples: "llind twin" = wind tunnel, "rocicet encine" = rocket engine, "empiric.:u" = empirical, "tbat", "dampine rutio". The fuzzy alignment matched every sentence. p246 and p281 were read on the scan and are verbatim. Fine: p93 (also the running chapter title, which STYLE does not transcribe; "racketeers" is OCR for "rocketeers"), p96 ("approximations" confirmed on the scan), p97, p111, p119, p176, p220, p225, p242, p243, p246, p247, p250, p251, p252, p253, p255, p256, p257, p264, p265, p272, p275 (the footnote on optimum weight is typeset as \footnote), p276, p277, p278, p280, p281, p284, p285, p286, p287.

Repeated 8-grams that involve Chapter 2 text. None needed a fix:
- Table of contents vs body headings ("3.1 Dynamical Behavior at Zero Roll Rate / 3.1.1 Generalized Homogeneous Response", same for 3.2). The table of contents also repeats the book's parallel subsection titles, "Complete Response: Step Input / Impulse Input".
- A coincidence between the TOC entries "5.2 Corrective Moment Coefficient / 5.3 Damping Moment Coefficient / 6 Model Rocket Design" and the Fig. 9 caption words once short words are stripped.
- Parallel entries in the Symbols list: A_1/A_2, the AR entries, I_D/I_E/I_F, moments about the X/Y/Z axes, torsion periods, alpha_D/E/F and omega_D/E/F.
- The book's own repetitions: the omega_D/omega_E/omega_F definitions on p100; "square root of a negative number not occur, and that there be" twice on p137 (checked on the scan's OCR); "rocket from its intended direction of flight increases with time" on p191 and p208.
- Parallel captions, each checked against the OCR of its own page: Figs 13/14, 22/23, 24/25, 28/29, 30/31, 34/35/36 and 41/42.
- Layout artefacts: the running head "Chapter 2. A Unified Approach..." followed by a caption at the top of a page, or by "values of the dynamic parameters".
- Halfman's Dynamics is cited in both Chapter 1 and Chapter 2 references (book).

make final exited 0 with no leftover draft notes. There are no overfull hboxes over 20pt anywhere in build/main.log.

PDF 274 is excused in inventory/chapters.json ("artwork_pages").
