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


## After the corrections step (2026-09-24)

The prose check was re-run after the errata and supplements were applied. The assembly step compared every window with the committed faithful state (HEAD built separately):

Method: I extracted HEAD with `git archive` into the scratchpad (read-only, no stash), built it, and scored every OCR window against both PDFs with prose_diff's own functions. Totals: the committed state (and audit/ch2-prose.md) had 122 pass, 60 inspect, 1 missing, 163 windows and 119 repeated 8-grams. Now there are 121 pass, 61 inspect, 1 missing (p274, excused artwork page), 167 windows and 208 repeated 8-grams. Verdicts changed on three pages: p113 inspect to pass; p221 and p231 pass to inspect. 21 windows on 18 pages scored below 0.6 and lower than in HEAD. For each one I listed the trigrams that were in HEAD's text but are missing now, and found the phrase in the current pdftotext output. No prose was lost.

Supplement-replaced pages (216-226, 281-284, 289). Pages 216-219, 222-224, 226, 282 and 289 pass. The non-pass windows are:
- p220@15: unchanged (0.57 in both states); OCR garble ("fotmd", "darrowman", "volullle"), as the audit found.
- p221@30 (0.68 to 0.57): the item-4 renames "normal force curve slope" in the conical-shoulder sentences. Also, the new D15 footnote now falls between (82) and "Figure 35 illustrates".
- p225@15 and @30: the 1973 prose around (86)-(88) is replaced by the 1994 text (item 5). @15 improved (0.50 to 0.54); @30 went from 0.57 to 0.54.
- p281@0-@60 and @120/@122: scores unchanged; garbled OCR that the audit read on the scan.
- p281@75/@90: the 2022 rewording (item 7): "flywheel-like devices have been installed" replaces "from time to time ... have appeared".
- p283@0/@15/@91: the 2022 text (item 9): "refer back to Figure 36 in Section 4.1", "of a proposed rocket, the designer", and "The range of beta_c ..." replacing "The selection of available relations".
- p284@0: item 9 ("very low roll-coupled resonant frequency"), plus a page break between "see the" and "danger". p284@130 is unchanged.

In every case the lost trigrams are exactly the replaced 1973 wording shown in `git diff` against HEAD.

Other pages that got worse, each checked in the current PDF text:
- A running head or page break now falls inside the phrase: p96 ("basic as possible. / Certain portions"), p136 ("formulae are [display] / Substituting"), p163 ("identities ... / then permit"), p172 ("then becomes / Now since this"), p195 ("following manner: / By analogy"), p257 ("such that / edge is tangent"), p280 ("Well-designed / sounding rockets").
- p140: the Figure 14 caption is no longer directly followed by the Figure 15 caption (float placement). The Figure 15 caption is present.
- p204: the new D10 ednote mark is glued to the word ("intoE14").
- p231: after reflow, pdftotext interleaves the overbar line ("¯ is referred to as the") into "this is just the equation's way of telling us / that the C.P. must lie behind".

All phrases are present. No source change was needed.

The 89 new repeated 8-grams come from:
- ednotes that quote replaced 1973 text in full, as the Decisions require (the Barrowman-intro paragraph, the (86)-(88) prose, the canted-fin sentence, the Figure 36 caption, the body-tube sentence, the fin-canting sentences);
- the renamed parallel captions of Figures 34-36, as before with "coefficient";
- the Figure 36 edcap opening, which matches Chapter 1's Figure 2 edcap;
- the repeated note ending "Neither the errata nor the supplements correct this; the display is kept as printed";
- running-head coincidences.

None is duplicated body prose.
