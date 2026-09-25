# M5 audit, front matter: author photographs, round 1

Unit: The Authors (six author photographs with their captions), scan PDF pages 7-12.
Compared images only (no .tex file opened).

## Sources used

- Scan photos: figures/pages/p007.png ... p012.png (these hold only the embedded
  photograph, no caption).
- Scan pages with captions: build/render/p007-150.png ... p012-150.png (full MediaBox renders),
  plus the text layer (`pdftotext -layout -f N -l N`) to confirm every caption character.
- Compiled: build/unit/author-photos-1.png ... -6.png, plus `pdftotext` of
  build/unit/author-photos.pdf, its outline (pypdf), `pdfimages -list` and the unit .aux/.log.
- Crops: figures/front/photo01.jpg ... photo06.jpg and manifest rows front-photo01 ... 06
  (figures/manifest.csv lines 158-163, already present; not re-cropped, because row 158's note says
  --force would re-trim the pale sky of photo01).

## Items checked

| PDF page | photo | caption as printed (scan) | compiled | result |
|---|---|---|---|---|
| 7 | Mandell at the Apollo 11 pad | "Gordon K. Mandell at Apollo 11, 15 July 1969" / "Photo by Jay Apt (now Dr. Jerome Apt, III)" | identical, two lines | match |
| 8 | Mandell in woods | "Gordon K. Mandell, 2018" | identical | match |
| 9 | Caporaso at blackboard | "George J. Caporaso at first MIT Convention, 1968" / "Photo by Jay Apt (now Dr. Jerome Apt, III)" | identical, two lines | match |
| 10 | Caporaso in lab | "George J. Caporaso, 2019" | identical | match |
| 11 | Bengen with rocket on pad | "William P. Bengen, 1964" | identical | match |
| 12 | Bengen portrait (signature "Stan Lawrence" in image) | "William P. Bengen, 2006" | identical, signature kept inside the image | match |

Every caption was checked character by character against the scan text layer: capitals, initials
with full stops, commas, "first" (lower case), "MIT", dates, parentheses, "Dr.", "III".

Other checks:

- One photo per page, centred, caption below, in scan order (7 to 12): correct (6 compiled pages).
- No printed heading on the first page (the scan has none); the PDF outline and the .aux carry the
  table-of-contents entry "The Authors" (`\contentsline {chapter}{The Authors}`), and the label
  `front:photos` is defined.
- Placed sizes (from `pdfimages -list`; \textwidth = 469.8 pt, \textheight = 650.4 pt):
  photo01 232.8 x 343.2 pt, photo05 228.0 x 228.0 pt, photo06 332.6 x 460.8 pt (all three at the
  scan's own size, 150 ppi); photo02-04 374.5 pt wide (= 0.8\textwidth). All are within
  0.8\textwidth x 0.78\textheight (375.8 x 507.3 pt).
- Crops: aspect ratios of photo02, 03, 04, 06 match the embedded scan images (1.293, 1.533, 1.171,
  0.716); each crop is the whole picture with the tool's standard 10 px white margin, and no
  caption. Photo01 and photo05 exclude the snapshot print border (white and cream), as the
  manifest notes record. Profiling the embedded images shows the crop edges fall on the picture edge
  within 0-2 px (about 0.7 pt), so no picture content is lost; the mast top and the antenna line of
  photo01 are present. The unit PDF (19:19) is newer than the crops (19:17).
- Colour and orientation of all six photos agree with the scan.

Not reported (intended): the scan sets these captions in bold monospace (NimbusMonoPS-Bold), which
is also the face of the 2025 release's title pages (PDF 1, 3, 4). It is the typescript's typeface,
not emphasis, so the compiled roman captions are not a discrepancy. Other intended differences:
the vertical placement on the page, the gap between a caption and its credit line, and no page
numbers.

## Discrepancies

| where | scan reading | compiled reading | severity |
|---|---|---|---|

none
