# Audit: ch4-sec5, round 1

Unit: "5. Recapitulation and Qualitative Features of the Analytical Results" to the end of the Chapter 4 text
(PDF 634-645). Compared scan images against the compiled render `build/unit/ch4-sec5-1.png` ... `-5.png`
(images only, the .tex source not opened).

## 1. Pages and items checked

- Scan pages: PDF 634 (from the "5." heading down), 635, 636, 637, 638, 639, 640, 641 (Figure 16), 642, 643, 644, 645.
  That is 12 pages. Render pages: 5.
- Headings: 9. They are 5 (634), 5.1 Bengen's Maxima (635), 5.2 Model Rocket Design Optimization (638), 5.2.1 Initial Design
  Definition and 5.2.2 Drag Coefficient (639), 5.2.3 Weight Optimization (640), 5.2.4 Dynamic Stability Optimization (642),
  5.2.5 Reduction of Drag at Angle of Attack and 5.2.6 Philosophy of Design and Flight (643). Numbers and wording match.
- Displayed equations: 0 (numbered or not). This confirms the survey's "Numbered equations: none". Assignment statements: 0. Tables: 0.
- Inline formulas: about 37, all matching.
  - k: 16 times, including 3 in the caption.
  - (ΔC_D)_lug with upright "lug"; C_D twice; ½ρC_DA_r; A_r; ρ twice.
  - C_1, C_2, I_L, I_R; ζ; ω_n (the lettered ω_m-like glyph, per STYLE section 15); ω_cres.
  - 0.002v, 0.01v, v, 0.2v, 1.0v; ε (\epsilon).
  - The numbers 1965, 1966, 0.25, 0.4, 1.225, 0.05 and 0.3 were zoom-checked.
- Prose: 15 paragraphs, checked sentence by sentence, with the paragraph breaks and page-top continuations checked too
  (636, 637, 638, 639, 642, 644 and 645 continue their paragraphs). A word-level diff of the OCR layer against the compiled
  text found no missing, duplicated or reordered words. The only differences are OCR noise and math tokens.
- Emphasis: 27 underlined items, all set in italics.
  - p634: parameter.
  - p635: the "total altitude ... drag constant k" phrase, "or lighter", "the optimum weight decreases as the value of k
    decreases", "is", "too light", and the title Handbook of Model Rocketry.
  - p636: 10 items.
  - p637: greater, intent, and the titles Altitude Prediction Charts and Model Rocket Altitude Performance.
  - p638: altitude capability. p639: all, size. p642: centimeters. p643: airplane wing. p644: iterations.
- Quoted terms: 8, with the comma or period outside the closing quote as typed. They are "closed-form solution", "superior",
  "best", "pop-off", "shuck-off", "home in", "pass" and "Malewicki charts".
- Other checks:
  - "performance!" on p635 is right.
  - The "--" on p637 is set as an em dash.
  - "A Malewicki chart" (p640) is printed with a capital A in mid-sentence and is set as "a". This is a silently fixed
    typing slip, as intended.
- Figure 16 caption (1): full text matches.
- Editorial note E1 (stale "Figure 19", p635): it is placed as STYLE section 15 requires. Its statement about the scan is true:
  there is no Figure 19, and Section 5.2.3 (p640) cites Figure 16 twice.
- References to other chapters and to Section 2 are set as "??". They are items in other units, so this is intended.

## 2. Discrepancies

none
