# Audit: ch4-sec3, round 1

Unit: "3. The Non-Oscillating Rocket: Solutions for Vehicles Launched at Any Angle from the Vertical"
(3.1, 3.2, 3.3), PDF 596 (after the four closing lines of 2.5) to mid-PDF 610 (before "4.").
Compared scan images only. I did not open the .tex source.

## 1. Pages and items checked

- Scan pages read: p596, p597, p598, p599, p600, p601, p602, p603, p604, p605, p606, p607, p608, p609,
  p610. There is one Read per page. The render is build/unit/ch4-sec3-1.png to -8.png, all 8 pages read.
- Zoomed crops (build/zoom/audit_ch4-sec3_r1-*): (16)-(17) and (90)-(91) on p596, including the dot of the ẏ
  in (16); (92)-(97) on p597; (98)-(105), the where-list and (106)-(110) on p598; (116)-(120) on p599;
  (125)-(127) on p600; the captions of Figures 10-14 on p603-p605.
- Headings (4): 3, 3.1, 3.2, 3.3. The wording, the lowercase "from" and the numbers all match.
- Displayed equations (44): the re-displayed (16) and (17) with their tags, and (90)-(131). I checked 42 numbered
  equations symbol by symbol. The sequence (90)-(131) is continuous, with no gaps or letters.
- Assignment statements (40): (92)-(131), in four runs: (92)-(105), (106)-(115), (116)-(124) and (125)-(131).
  The row order, "=" as printed, and stacked vs. slashed fractions all match.
- Where-list (4 items plus the closing line "and the other variables are as in Section 2.4."): matches.
- Inline formulas (about 25): θ_o (p599, p601, p606 twice, p608); m_o (p601, three times); k (p601 twice, p608);
  g sinθ_o, θ, g sinθ, F(t)cosθ (p606); 30° (p601 twice, p608); x-direction (p609); k/m_b (p610); plus the
  caption symbols m_o, k, x_b, y_b, θ_o and F. All match.
- Figure captions (6): Figures 10-15. I checked every number, unit and punctuation mark: .00005, .00012, .002,
  .00007, .00017, .0027, .0003, .0045; m_o .020/.050/.140, .021/.050/.100, .032/.065/.125, .110/.230/.453,
  .110/.230/.300; x_b, y_b; burning times 0.35 second, 1.20, 2.90, 0.50 and 9.00 sec.; 6.84 seconds. All match.
  I did not audit the artwork.
- Tables: none in this unit.
- Prose (15 paragraph blocks, including the continuations after displays): checked sentence by sentence.
  Wording, paragraph breaks, emphasis (iteration; best-performing, typical, worst-performing; normal, greater,
  increase, decreased, further, undesirable, safety hazard), quoted terms, dashes and "0.453 Kg" all match.
- Survey briefing (build/ch4-notes/ch4-sec3.md): verified. The equation pages, figure pages, headings and
  figure files are correct. There is one inaccurate remark, and it does not affect the render. The survey says
  PDF 610 "opens a new paragraph", but the first line of p610 ("The asymmetry, ...") is typed flush left with no
  paragraph indent (indented paragraphs on the same page start about 65 px further right). It therefore continues
  the p609 paragraph. The render joins the two passages into one paragraph, which is faithful. The briefing's
  range header "PDF 596-609" omits the p610 tail, which does belong to this unit.

## 2. Discrepancies

none
