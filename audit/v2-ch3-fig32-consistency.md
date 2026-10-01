# v2 consistency check: ch3/fig32

The two issues in this pass are:
1. the round-bar break should be redrawn as `\breakline`;
2. labelled velocity arrows should be `vec`.

Fig 32 was not named in either issue. I checked that neither applies.

Sources checked:
- figures/v2/ch3/fig32.tex, fig32.py, fig32.csv, fig32.calib.json and fig32.pdf. They are dated 22:00-22:01,
  earlier than this pass's edits (23:12 onwards). The PDF measures 350.85 x 247.34 pt = 4.87 x 3.44 in, the same
  as round 1, and all fonts are embedded. I rendered it at 300 dpi.
- The scan figures/ch3/fig32.png.
- The round-1 audit.

## Checks

- **Issue 1 does not apply.** The inset is a whole paraboloid, with its tip, a flat base and the $L$ and $d$
  dimensions. No tube is broken off.
- **Issue 2 does not apply.** There is no flow or velocity arrow, either on the scan or in fig32.tex.
- **No regression.**
  - The file was not edited in this pass.
  - I re-ran `digitize.py overlay` myself and got round 1's numbers exactly: mean 0.00 px, 95% 0.00 px, max
    1.0 px.
  - The render still matches round 1:
    - the $\CD$ and $\dfrac{L}{d}$ titles;
    - the ticks;
    - the s1 curve;
    - the exact paraboloid inset, with $L$ and $d$ in gaps.

## Findings

None. Round 1's optional note on where the centre line ends still stands. It is not affected by this pass.

## Verdict: pass (neither issue applies; unchanged since round 1)
