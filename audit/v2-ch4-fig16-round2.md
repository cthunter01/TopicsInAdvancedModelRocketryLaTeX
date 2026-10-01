# v2 audit: ch4/fig16 (round 2)

Sources checked:
- Scan `figures/ch4/fig16.png`.
- Redraw `figures/v2/ch4/fig16.pdf`:
  - 400 and 600 dpi renders, with crops of the k labels, the lower end of the Bengen line, the callout and the
    engine-mass label;
  - `build/v2/png/ch4-fig16-compare.png`;
  - `pdffonts` and a transparency scan;
  - a recompile of the current `.tex` in scratch, compared with the committed PDF.
- Sources `fig16.tex`, `fig16.py`, `fig16.csv`, `fig16-bengen.csv` and `fig16.calib.json`, plus `trajectory.py`.
- Inventory row `ch4-fig16`.
- Text: `chapters/ch4-sec5.tex`:15-86 and :140-169 (the citing text and the caption); `chapters/ch4-sec2a.tex`:25,
  55-64 (the mean mass, eqs. (20), (21)); `chapters/ch4-sec2b.tex`:56-57 (eq. (67)).
- `corrections/v2-figures.md`, all of it, for the round 1 entry.

## Round 1 follow-up

| r1 # | status |
|------|--------|
| 1 should-fix (log the Bengen-line overlay and the FM evidence in `corrections/v2-figures.md`) | **Still open.** The drafter properly declined it, since that file is outside what they may edit, and passed the text to the orchestrator. The entry is still absent: `corrections/v2-figures.md` has no "Ch4 Fig 16" or "Bengen" line. Carried as finding 1, for the orchestrator. |
| 2 note ("one line away" overstated) | Resolved. The `fig16.py` docstring, the METHOD comment (line 42) and the `fig16.tex` header now say that METHOD switches the data only and that the six labels and the callout would have to move. |
| 3 note (lowest ~15 m of the locus turns vertical) | Unchanged. It is a true property of the FM locus (the m_o of the maxima peaks at .0379, row 56 of 60), and it is under 0.1 mm. |
| 4 note (s2 dashed against the printed long-dash-short-dash) | Unchanged. The caption names no line style. |

No regressions: the drawing is unchanged. The recompile in scratch renders identically to the committed PDF, and
the label and callout coordinates are those audited in round 1.

## Checks made

- **Data reproduce.** I reran `fig16.py` in a scratch tree. `fig16.csv` and `fig16-bengen.csv` are byte-identical
  to the committed files.
- **Equations, checked independently.** I wrote my own eqs. (20), (21) with the mean mass (ch4-sec2a.tex:25),
  F = I_t/t_b, and the coast (67) at m_b, using I_t 5.0, t_b 1.20, m_p .00833 and g 9.8. I did not use
  `trajectory.py`.
  - All 159 x 6 CSV values agree within 0.005 m, which is the CSV's rounding.
  - The Bengen locus agrees within 9e-7 kg in m_o.
  - The top point (k .00003208, m_o .023135) gives 699.95 m.
- **Values.**
  - Engine alone (.021 kg): 526.9, 340.6, 221.7, 146.3, 98.0 and 66.6 m.
  - Maxima: (.0250, 536.8), (.0282, 354.0), (.0316, 233.4), (.0348, 154.2), (.0373, 102.4) and
    (.0378, 68.6).
  - These match the scan's readings in the inventory (~528/537, ~340/352, max ~232, ~153, ~101, ~65-68).
- **Overlay**, with the drafter's calibration (residual 0.00 px). I first measured the gridlines myself: the
  calibration's xgrid and ygrid match the ruled lines within 1 px at y 250 m and m_o .05, and the grid is
  keystoned, as the calibration's note says.
  - The six curves: 95% within 1.00, 1.41, 1.00, 1.00, 1.00 and 1.00 px (at most 0.24 mm). ok.
  - Bengen line: 60 points, 95% 3.63 px (0.61 mm), max 5.00 px. Over tolerance; see finding 1.
  - Engine-alone line at .021: 95% 2.24 px. ok.
- **Method variant**, run with METHOD = "interval" in scratch (eqs. (83)-(87)):
  - The curves differ from FM by -3.1 to +3.9 m, which bears out "1-4 m".
  - The .0016 maximum moves to .0407 kg, nearer the drawn end of about .040.
  - Overlay: the six curves 95% 2.0-3.16 px; the Bengen line 5.41 px (max 6.0). FM remains the better fit
    overall, which supports the drafter's choice and the round 1 evidence.
- **Lettering.** Everything is present:
  - $y_{\max}$ (m) (upright max) and $m_o$ (kg);
  - y ticks 0-700 step 100, x ticks 0, 0.02, ..., 0.10, and the grid every .01 kg and every 100 m;
  - the six k labels with leading dots as printed;
  - "Line of Bengen's maxima" with a straight `\callout`, whose point is on the computed line;
  - "$m_o$ of engine alone" set along the guide.
- **Caption and text.**
  - The k values (kg/m) are noted on the curves.
  - The Bengen line lies right of the engine-mass line everywhere (m_o >= .0231 against .021).
  - The optimum falls as k falls (ch4-sec5.tex:28-31).
  - The curves start at the loaded engine's mass (:84-86).
  - It reads as a Malewicki chart for locating Bengen's maximum for a given k (:145-149).
- **Style.**
  - `tamr grid`; six curves in one colour (s1), labelled; the locus in s2 dashed; the reference line a `guide`.
  - Text in ink (#0B0B0B, sampled) and ticks in ink2.
  - Knock-outs are drawn after the curves. At 600 dpi none covers a curve or the Bengen line: the closest are
    ".0001" and ".0004"/".0008" beside the Bengen line, and ".00005" beside its own curve, each about 1 mm
    clear.
  - The engine label is drawn before the curves.
  - No transparency, fonts embedded, clean log.
  - x tick labels as in the fig06a template (0.02 ... 0.10).
- **Legibility** at final size (4.52 x 5.75 in, unscaled): tick labels `\footnotesize`, labels `\small`. Every
  label is clear of the others.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | should-fix (orchestrator; no figure change) | Carried from round 1. The Bengen line's overlay (95% 3.63 px, 0.61 mm, max 5.0 px; lower end .0378 kg against about .040 drawn) exceeds the 3 px tolerance. STYLE s16 says such a mismatch goes to `corrections/v2-figures.md`, and it is still not there. Also unrecorded: the use of Fehskens-Malewicki rather than the interval method of the Fig 11 decision, and the overlay evidence for that choice. The drafter cannot edit that file. | `corrections/v2-figures.md`, Chapter 4 | Orchestrator: add a Chapter 4 Minor entry, as round 1 suggested. Optionally add the round 2 numbers: "Ch4 Fig 16: computed by Fehskens-Malewicki (20), (21) with the coast (67), as Section 5.1 says such charts are made (ch4-sec5.tex:82-84). The 1973 curves are this solution: 95% within 1.0-1.4 px, against 2.0-3.2 px for the interval method (83)-(87) and 4-13 px for Caporaso-Bengen. The Bengen line is the locus of the computed maxima (k .000032 at 700 m to .0016): 95% 3.6 px, lower end .0378 kg against about .040 drawn (the interval method's .0407 is nearer, but its line overlays at 5.4 px)." Put the method question (FM here, the interval method for Fig 11) to the Chapter 4 gate, as the drafter asks. |
| 2 | note | The `fig16.py` docstring gives the interval variant's Bengen-line overlay as "5.1 px". Running the script's own METHOD = "interval" gives 5.41 px (round 1's separate run gave 5.08). This is a comment only, about the variant that is not used. | `fig16.py` docstring ("interval method 5.1 px") | Optional: write "about 5 px" or "5.4 px". |

## Verdict

pass. The figure itself needs no change. Finding 1 is an entry the orchestrator must add to
`corrections/v2-figures.md`.
