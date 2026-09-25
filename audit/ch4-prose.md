# Audit: Chapter 4 prose check (tools/prose_diff.py)

Every page that tools/prose_diff.py did not pass was checked against the scan by the assembly step; its conclusions are recorded here because build/prose-ch4.md is regenerated on every build.

Chapter 4 (build/prose-ch4.md): 106 pages checked. 70 pass, 35 inspect, 1 missing (PDF 628, now excused), 12 skipped under 30 tokens (529, 530, 536, 551, 574, 581, 595, 604, 609, 615, 630, 631).

Method: I aligned every OCR token of PDF 531-646 against the compiled Chapter 4 text (difflib, in build order). I listed every run of 3 or more OCR tokens that had no compiled counterpart, and every run of compiled text not in the OCR. I spell-checked the compiled Chapter 4 text with aspell; it found only technical words and names. I looked at the scans of 567, 611 and 627-631 and matched them line by line. Result: no prose was dropped, garbled or duplicated anywhere in Chapter 4. Every run the alignment flagged was one of four things:
- a float that LaTeX moved
- the running head
- the two prescribed \ednotes (PDF 625 on (200a), PDF 635 on "Figure 19")
- lettering inside a figure

Conclusion for each non-pass page:
- 537, 538, 539 (introduction): OCR noise ("asslllllption", "traj ectory ctlct ations", "malewlcki", "tecbnic"). All the prose is present, including "Model Rocket Flight Calculations", "nonvertical launch" and "necessary either to apply".
- 543: Figure 1 page. The "time / rocket mass / rocket velocity / rocket momentum" labels are lettering inside fig01.png. The caption matches the scan.
- 544, 545, 546, 547, 548, 550 (Section 1): OCR splits and noise ("xhau veloci", "tenn", "ttack", "thrllst", "woight ... alwnys", "fonned"). Every sentence is present. The window on 550 includes the dotted-notation paragraph, which is compiled before the Figure 2 float.
- 554, 561, 562, 563: OCR noise ("resnect", "obtainp", "statta", "throupH", "burninp") and pasted hand-lettered symbols. Text complete.
- 566, 567, 568, 569, 570 (multistage sections 2.2.1-2.2.2): heavily garbled OCR ("weathercockinp tennency", "rockp", "comnetjtion", "throuff cation canoraso ricoatj") around lettered displays (52)-(60). Checked against the scan of 567. All prose is present: the passage on weathercocking and the NAR three-stage rule, the "upper limit ... could have been taken" passage, the cosh identity and the terminal-velocity discussion.
- 572, 576: OCR noise ("chrrge", "negli ible", "mcti representinp", "nlassea", "throuv lnical"). Text complete.
- 585: OCR noise ("general1?.ation", "phRse", "calcul attonf"). Present: "The generalization of the method to the coasting phase or a second burning phase is entirely analogous...", the heading of Section 2.5, and "Five engine types were considered: the B14, B4, D4, F100, and F7".
- 588, 589, 591, 592, 593, 594: pages of Figures 5(a)-9(c). The unmatched tokens are the "Fehskens-Malewicki / Caporaso-Bengen" legends and k_min/k_max labels inside the crops. All 15 panel captions match the OCR and the scan, including the F100 note "An additional error is incurred for values of m_o below 0.17 kg due to transonic drag divergence, in the k_min cases."
- 607: Figure 15 caption ("Rocket undergoing a gravity turn ..."). Complete; its low score is only because the float is placed elsewhere.
- 610, 611, 612 (start of Section 4 and 4.1): OCR noise ("aningful", "shnll", "nuuntions", "eouat", "hlillatin"). Checked 611 against its scan: complete, with the underlined passage in \emph.
- 618: OCR noise ("formu", "responaea", "angu"). Complete.
- 627: Table 1. Every row checked against the scan.
- 628 ("missing"): Table 2, first half. The OCR letter-spaces the typed cells ("descri ption", "i ntensi ty", "I mpulse"), so almost no 3-grams match. I checked the header and all 17 rows against the scan, and the columns 5-10 of PDF 630-631 as well; all match the ch4:tab:2 longtable. Excused in artwork_pages (see open).
- 629: Table 2, continued. 9 rows plus the caption, checked against the scan; complete.

Skipped pages were also checked the same way: all are figure lettering or text that is present (581 "proceed to the discussion of actual iteration schemes"; 615 "arithmetic assignment statements").

Repeated 8-grams involving Chapter 4: all legitimate, none fixed.
- Table-of-contents entries repeating the Chapter 4 headings (Selection of a Coordinate System..., Oscillating Rocket Solutions..., Validity of the Approximate Methods..., Numerical Method..., Effect of Dynamic Oscillations...).
- Symbols-list definitions shared with Chapters 1 and 2 (e, Napierian logarithm; omega, omega_f, omega_n).
- References shared with other chapters' lists (Thomas, Calculus; Stine, Handbook; Malewicki TIR).
- v_1/v_2 in the Symbols list and again in the "where" list after (48)-(49).
- Parallel sentences as printed on PDF 560 ("To use the ... method, compute the burnout velocity using equation ... and the burnout altitude ...").
- "altitude increment gained during the second-stage burn ... then" (PDF 565 and 567).
- The PDF 579 sentence against the Figure 4 caption ("approximating the thrust-time curve of a typical model rocket engine").
- The PDF 616 list "C_1 is the corrective moment coefficient; C_2 ...; I_L ...; I_R ..." against the Chapter 2 headings in the TOC.
- The formulaic captions of Figures 5(a)-9(c) and 10-14, which differ only in engine type and numbers.
- Table 2's repeated description cells ("Homogeneous response to", "Step of intensity", "Impulse of strength", "Coupled sinusoidal forcing ... omega_cres") and its repeated continuation header.

After the fix, prose_diff printed "artwork page 628 (below 0.3 everywhere, excused)", with no likely dropped pages in any chapter.


## After the corrections step (2026-09-24)

Chapter 4 now has 68 pass, 37 inspect and 1 missing (628, still excused), with 12 skipped. audit/ch4-prose.md recorded 70/35/1. There are 100 windows to inspect (was 99) and 586 repeated 8-grams (was 472). To find the cause, I rebuilt the committed HEAD (git archive into the scratchpad) and compared every OCR 3-gram of PDF 529-646 between the two PDFs, then located each lost 3-gram in the new pdftotext output.

(1) The pages whose text the sources replaced barely changed. prose_diff cannot see most of these corrections, for two reasons. First, each \ednote or \edcap quotes the 1973 wording word for word, and the tool matches 3-grams anywhere in the document. Second, the tokenizer drops digits and tokens shorter than 4 letters.
- 545 (min 0.43, mean 0.67, was 0.68): the one lost 3-gram, "symbol write both", is replaced text. The 1973 "...single symbol F(t), so we can write (8) Both the engine thrust..." now survives only in the note, split by "then gave equation (8)". The other uncovered tokens are the OCR noise recorded in the audit ("motton", "subjact", "tenn", "statio", "di-rected", "long-itudinal", "rofessional ... ineers").
- 546 (0.46/0.56): unchanged. The uncovered tokens are OCR noise ("external.ly", "fu.nctiona", "~ttack", "con~tructed", "iormed exn11citly"). The replaced 1973 top of p.514 is still matched through the note's quotation.
- 563-569 (566 0.25/0.51, 567 0.14/0.26, 568 0.29/0.50, 569 0.11/0.51, 563 0.39/0.55; 564-565 pass): the rewritten (40) and (44)-(53) are hand-lettered displays that the OCR garbles. The upper-limit wording change (t to t-hat, t_1 to 0, t_1+t_2 to t_2) touches only tokens shorter than 4 characters, so the new sentence is token-identical to the 1973 one. The non-pass windows are the audited OCR noise ("weathercockinp tennency", "rockp", "comnetjtion", "throuff cation canoraso ricoatj"). The only other losses on 563-565 come from note markers glued to a word: "writeE6" and "yieldingE8" tokenize as "writee" and "yieldinge". On 565, a note continuation also falls between "(27) and (28)." and "The generalization". None of these is missing text.
- 580 (1 window, 0.61, pass, as before): the uncovered tokens are the legend lettering inside the artwork. The 1994 caption and its \edcap are present.
- 615: skipped (25 tokens).
- 622 and 623: pass. Errata items 2-4 change only equation numbers, and I confirmed (139), (154) and (160) in the output.
- 627 (0.36/0.46): unchanged. The table's header and row-label OCR noise ("wcres", "cilz lores", "rlthout"). The new cant angles and k values are digits.
- 531-535 (Symbols) also changed because item 6 inserted entries and notes (A_e, E_o, P_a, P_e; F(t)). All still pass.

(2) Other pages. The inserted footnotes moved the page breaks. Every 3-gram lost on a page not changed by the sources is now split by a running head or page number, or by a footnote or its continuation. I checked each one: 541, 552, 554, 556, 558, 582, 587, 599, 601, 608, 613, 614, 616, 619, 621, 626, 633, 635, 638, 640 and 644. Some of those footnotes are the new doubt notes: D9 (552), D6 (556), D4 (587), D5 (613), D7 (616), D1 (619), D3 (635) and D8 (644). The same effect raised other pages (538, 554, 597, 602, 636, 638). Two pages fell from pass to inspect, and both are layout only, with all text present:
- 541 (min 0.61 to 0.57): "mathematically inclined. / General Differential Equations" now spans a page break. The remaining uncovered tokens are OCR noise ("eguat", "balli", "classi mechrntcs").
- 558 (0.61 to 0.57): "the following form (29) / where the constants" spans a page break. The rest is OCR noise ("methematics scienr", "napierlan", "veloc").
No window lost prose. The new repeated 8-grams are all legitimate:
- the \ednote quotations of 1973 text that the 1994 text keeps
- the standard "Neither the errata nor the supplements correct this ... kept as printed" wording, repeated in several notes
- the A_e Symbols entry shared by Chapters 1 and 4
- the 1994 Figure 4 caption against its \edcap quotation of the 1973 caption
- the Figures 5-9 captions and Table 2 cells, rejoined across the moved running heads
- the upper-limit sentence against its quotation.
