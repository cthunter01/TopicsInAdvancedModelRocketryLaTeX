# v2 audit: ch3/fig12 (round 1)

Sources checked: figures/v2/ch3/fig12.tex, fig12.py, fig12-edge.csv, fig12-eddies.csv, fig12.calib.json and the
PDF (rendered at 300 and 600 dpi; `make fig F=ch3/fig12`: 6.06 x 2.00 in, fonts embedded); the scan
figures/ch3/fig12.png (zoomed 2x, and 4x and 8x around the fins, the lug and the base); inventory row ch3-fig12;
caption chapters/ch3-sec3a.tex:28-45 and citing text chapters/ch3-sec2b.tex:420-430; eqs. (54) and (80); STYLE.md
sections 14 and 16; tamrfig.sty (`model` rocket, `edge fin`, `leader arrow`, `\anglemark`, `wash`). I ran the
overlay myself.

Checks that passed:
- Every printed callout is present with its printed wording: pressure foredrag; laminar boundary layer; transition;
  turbulent boundary layer; fin-body interference drag; drag due to angle of attack; skin friction drag; parasitic
  pressure drag due to launch lug; base drag; fin tip vortex. Also $\alpha$ and $\bar V$ (overbar, as printed). The
  scanner specks (the dot under "attack", the blob near the nose joint) are not reproduced.
- One coherent rocket (the house `model`) with straight leaders. Each leader ends on its subject: the ogive nose, the
  laminar layer, the transition mark at x = 2.90, the turbulent layer, the fin-root junction, the lug, the lower
  surface (skin friction), the base bubble and the tip vortex.
- Boundary layer: laminar $\delta = 0.0611\sqrt{x}$ (eq. (54)) to x = 2.90, then turbulent
  $\delta = 0.0803(x-1.519)^{4/5}$ (eq. (80)), continuous at transition (0.1040 and 0.1040). Overlay of the
  edges on the scan from x = 1.2 to the fins: upper 95% 1.0 px, lower 95% 1.2 px (max 2 px), ok. The wake alone (from
  the base): 95% 4.1 and 4.0 px, max 10 and 8 px, against the freehand 1973 wake. That is a sketch continuation; the
  drafter's combined figures (1.0 and 2.2 px) agree with this.
- $\alpha$ lies between the axis extended ahead of the nose and the free-stream line. The arc is centred at their
  intersection (5.8, 0), so both of its ends land on the lines (checked at (-0.306, -1.077)). The sense agrees with
  the scan (free stream up and aft).
- The recirculating base flow runs aft along the outside and forward along the axis (physically right). Flat fills
  only (`wash`), no transparency. Width within 6.5 in; no label clipped.

## Findings
| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | should-fix | The $\alpha$ of the angle mark sits on the baseline of the middle line "angle of" of the left-hand label, only about 1.4 mm after "of" (a normal word space is about 0.9 mm). The label therefore reads "drag due to / angle of $\alpha$ / attack". In the 1973 art $\alpha$ stands about 10 mm clear of the word column. | fig12.tex:80, 94 | Separate them: move the label's east anchor left to about (-0.68,-0.55), or move $\alpha$ off that line (`\anglemark[at={(\vx,0)}, pos=0.3]...`), so that no label line shares its baseline. |
| 2 | note | The 1973 drawing read closely. The slender shape on the centre line (scan px 474-522, row 148, x = 5.57-6.31 in model units) spans the fin root chord: it is the near fin seen edge-on, and the wavy line trailing on the axis behind the base is its tip vortex (the 1973 "fin tip vortex" leader ends there, px (597,148)). The 1973 launch lug is the small rectangle under the lower surface at x of about 5.83-6.39 (px 491-527, rows 161-168), beside the lower fin root, with fanning flow lines; the lug leader ends just behind it (px (511,174)). The inventory row reads the centre-line shape as the lug. The redraw reads it as the edge-on fin, which agrees with this reading, but it moves the lug ahead of the fins (x 4.25-4.85) and takes the tip vortex from the upper fin's tip. Both are coherent and change no meaning. | fig12.tex:2-3, 69-76; inventory ch3-fig12 notes | Record the reading and the moved lug in the drafter's doubts, so the gate (and the inventory notes) see them. |
| 3 | note | All nine leaders end in heads (`leader arrow`), while the house callouts of Ch2 Figs 32, 37, 39, 41 and 44 use the headless `leader`. The kit keeps heads for pointing at a line, and most targets here are lines or regions inside the wash, where a head helps. | fig12.tex:83-100 | Confirm in the chapter consistency pass; no change asked. |
| 4 | note | The family's rocket has four fins here (edge-on fin), while Fig 1 places its C.P. for three fins and draws the two-fin profile (see the Fig 1 audit). | fig12.tex:69 | None here. |

## Verdict: pass (no must-fix)
