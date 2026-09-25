# M5 audit: 1973 front matter, part 1 (half-title, title page, copyright page, dedication), round 1

Unit: frontmatter/original-1973 (the .tex file was not opened; images only).
Scan pages: figures/pages/p013.png to p017.png (PDF 13 to 17), plus zoomed 300 dpi crops of the scan
(build/zoom/audit_front-1973_r1_p1-p16top-016.png, -p16mid-016.png, -p16lc-016.png, -p17ded-017.png).
Render: build/unit/original-1973-1.png to -5.png (render page 5, the Publisher's Foreword, is the page
after the last of mine; there is no page before render page 1), a 300 dpi crop of the compiled copyright
page (build/zoom/audit_front-1973_r1_p1-render3-3.png), and pdftotext of build/unit/original-1973.pdf
pages 1 to 4 as a character-level cross-check. Bookmarks and TOC entries read from
build/unit/original-1973.out and .aux. The unit log has no overfull or underfull boxes; its only warnings
are undefined \ref{ch2}/\ref{ch3}/\ref{ch4} on page vi (the Preface, not in this part; expected in a
standalone build).

## Pages and items checked

| scan | content | render | result |
|---|---|---|---|
| (before PDF 13) | TOC entry "The 1973 Edition" with label front:1973 | page 1 | present: .aux has `\contentsline {chapter}{The 1973 Edition}{i}{section*.1}` and `\newlabel{front:1973}` on page i (the half-title page); PDF bookmark "The 1973 Edition" is the first bookmark, ahead of "Publisher's Foreword" and "Preface" |
| PDF 13 | half-title "TOPICS IN ADVANCED MODEL ROCKETRY", centred, alone on the page, about a third of the way down | page 1 | matches: every word, all capitals, centred, alone on its own page at about the same height, no page number |
| PDF 14 | blank verso | (none) | not transcribed, as the task specifies (13, 15, 16 and 17 each on their own page) |
| PDF 15 | title "TOPICS IN ADVANCED MODEL ROCKETRY"; "Gordon K. Mandell" / "George J. Caporaso" / "William P. Bengen"; lower on the page "The MIT Press" / "Cambridge, Massachusetts, and London, England"; centred | page 2 | matches: every word, initial, full stop and comma; the three author lines in order; the large gap before the imprint; the two imprint lines; centred; no page number |
| PDF 16 | "Copyright © 1973 by" / "The Massachusetts Institute of Technology"; paragraph "All rights reserved. No part of this book may be reproduced in any form or by any means, electronic or mechanical, including photocopying, recording, or by any information storage and retrieval system, without permission in writing from the publisher."; "This book was printed on Fernwood Opaque" / "and bound in Columbia Milbank Vellum" / "by The Colonial Press, Inc." / "in the United States of America."; "Library of Congress Cataloging in Publication Data"; "Mandell, Gordon K" (no full stop after K); indented "Topics in advanced model rocketry."; indented "1. Rockets (Aeronautics)--Models.  2. Rockets" / "(Aeronautics)--Performance.  I. Caporaso, George J." / "II.  Bengen, William P.  III.  Title." / "TL844.M36   629.47'52   72-10386" / "ISBN 0-262-02096-3"; left-aligned block below mid-height | page 3 | matches: every word, capital and punctuation mark; © is U+00A9; the rights paragraph as one paragraph (its line breaks differ, which is allowed); the four printing lines as separate lines; "Mandell, Gordon K" without a full stop, as printed; the two indents of the catalogue record; "--" set as em dashes (allowed); the catalogue record's line breaks as printed; call number, Dewey number with its typewriter apostrophe (straight ', U+0027) and LC card number on one line spaced apart; ISBN digits and hyphens; left-aligned block; no page number. The isolated dot below the rights paragraph on the scan is a speck (zoomed), correctly not transcribed |
| PDF 17 | dedication "To Orville H. Carlisle and G. Harry Stine, / without whom model rocketry could not have / begun; and to the advanced model rocketeers / of the world, without whom it could not / continue."; left-aligned block, double-spaced, centred on the page, about a third of the way down | page 4 | matches: every word, initial, comma, the semicolon after "begun" and the final full stop; one paragraph with the scan's own line breaks and double spacing; block placed centrally at about the same height; no page number |

Typing slips: none on these pages. Emphasis/underlining: none on these pages. Editorial notes: none, and none are
needed. Figures, tables and mathematics: none. Headings: none on these pages (the TOC entry "The 1973 Edition"
is the only heading-like item and is present with its label).

## Discrepancies

none
