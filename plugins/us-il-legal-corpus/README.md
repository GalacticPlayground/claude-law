# Illinois — Legal Corpus Overview

**Code Name:** Illinois Compiled Statutes
**Capital:** Springfield
**Court System:** Illinois Judicial Branch
**Highest Court:** Illinois Supreme Court
**Plugin:** `us-il-legal-corpus`
**Pulled:** 2026-06-05

## What this corpus contains

- **Statutes:** Canonical links to the Illinois Compiled Statutes at official and mirrored sources, with a sample of verbatim text pulled for representative titles.
- **Court rules:** Canonical links to the Illinois court rules (rules of civil/criminal/appellate procedure, evidence, local rules, etc.).
- **Case law:** On-demand indexes — see `references/il-case-law.md`.

## Sources

### Statutes
- **ILCS** — <https://ilga.gov/Legislation/ILCS/Chapters>

### Court Rules
- **Illinois Judicial Branch** — <https://www.illinoiscourts.gov/courts/supreme-court/rules/>

## Architecture

This plugin follows the `*-legal-corpus/` convention. It is consumable by any cross-jurisdiction `*-consumer-debt`, `*-family-law`, or `*-pro-se` skills layer that wants the Illinois corpus as its venue-specific reference.

## Coverage targets

- [x] Canonical statute index (links to all titles/chapters)
- [ ] Verbatim statute text (sample for the most-litigated titles; expand quarterly)
- [x] Court rules canonical link
- [ ] Verbatim court rules (sample for the rules most-cited in consumer-debt / family-law / housing matters)
- [x] Case law API index
