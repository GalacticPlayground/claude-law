# Delaware — Legal Corpus Overview

**Code Name:** Delaware Code
**Capital:** Dover
**Court System:** Delaware Judicial Branch
**Highest Court:** Delaware Supreme Court
**Plugin:** `us-de-legal-corpus`
**Pulled:** 2026-06-05

## What this corpus contains

- **Statutes:** Canonical links to the Delaware Code at official and mirrored sources, with a sample of verbatim text pulled for representative titles.
- **Court rules:** Canonical links to the Delaware court rules (rules of civil/criminal/appellate procedure, evidence, local rules, etc.).
- **Case law:** On-demand indexes — see `references/de-case-law.md`.

## Sources

### Statutes
- **Delaware Code** — <https://delcode.delaware.gov/>

### Court Rules
- **Delaware Judicial Branch** — <https://courts.delaware.gov/supreme/>

## Architecture

This plugin follows the `*-legal-corpus/` convention. It is consumable by any cross-jurisdiction `*-consumer-debt`, `*-family-law`, or `*-pro-se` skills layer that wants the Delaware corpus as its venue-specific reference.

## Coverage targets

- [x] Canonical statute index (links to all titles/chapters)
- [ ] Verbatim statute text (sample for the most-litigated titles; expand quarterly)
- [x] Court rules canonical link
- [ ] Verbatim court rules (sample for the rules most-cited in consumer-debt / family-law / housing matters)
- [x] Case law API index
