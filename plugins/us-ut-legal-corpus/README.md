# Utah — Legal Corpus Overview

**Code Name:** Utah Code
**Capital:** Salt Lake City
**Court System:** Utah Judicial Council
**Highest Court:** Utah Supreme Court
**Plugin:** `us-ut-legal-corpus`
**Pulled:** 2026-06-05

## What this corpus contains

- **Statutes:** Canonical links to the Utah Code at official and mirrored sources, with a sample of verbatim text pulled for representative titles.
- **Court rules:** Canonical links to the Utah court rules (rules of civil/criminal/appellate procedure, evidence, local rules, etc.).
- **Case law:** On-demand indexes — see `references/ut-case-law.md`.

## Sources

### Statutes
- **Utah Code** — <https://le.utah.gov/xcode/code.html>

### Court Rules
- **Utah Judicial Council** — <https://www.utcourts.gov/rules/>

## Architecture

This plugin follows the `*-legal-corpus/` convention. It is consumable by any cross-jurisdiction `*-consumer-debt`, `*-family-law`, or `*-pro-se` skills layer that wants the Utah corpus as its venue-specific reference.

## Coverage targets

- [x] Canonical statute index (links to all titles/chapters)
- [ ] Verbatim statute text (sample for the most-litigated titles; expand quarterly)
- [x] Court rules canonical link
- [ ] Verbatim court rules (sample for the rules most-cited in consumer-debt / family-law / housing matters)
- [x] Case law API index
