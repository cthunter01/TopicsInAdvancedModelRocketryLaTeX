# Audit: ch1-symbols (Chapter 1 Symbols list), round 1

## Scope checked

- Scan pages: figures/pages/p033.png, p034.png, p035.png (PDF 33-35, book pages -3- to -5-).
- Render pages: build/unit/ch1-symbols-1.png, build/unit/ch1-symbols-2.png.
- Items checked: 1 heading ("SYMBOLS" -> "Symbols"), table head ("Symbol" / "Meaning", repeated on
  each scan page and each render page), 56 symbol rows (symbol and meaning, every row compared
  individually):
  - PDF 33: 21 rows (A ... c)
  - PDF 34: 26 rows (c-vector ... y)
  - PDF 35: 9 rows (Delta( ) ... integral)
- Order of entries: identical (uppercase Roman, lowercase Roman, Greek/operators).
- No displayed equations, figures or captions in this unit.

## Observations that are NOT discrepancies (intended per STYLE.md)

- Typewriter subscript "o" in C_Do, R_o, g_o, m_o rendered as subscript zero (C_{D_0}, R_0, g_0,
  m_0): follows the `\CDo` -> `C_{D_0}` macro convention in STYLE.md.
- Hand-lettered "Lim" over "n -> infinity" rendered as the standard `\lim` operator with the limit
  below.
- Underlined "also" in the v entry rendered as italics.
- Second "sum of all ( )" entry printed with a Delta in the scan and transcribed with a Delta, as
  instructed (known printed error, kept).
- Row spacing, page breaks and repeated table heads differ (longtable), as expected.

## Discrepancies

none
