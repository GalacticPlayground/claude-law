# New York — Legal Corpus Overview

**Code Name:** Consolidated Laws of New York
**Capital:** Albany
**Court System:** New York State Unified Court System
**Highest Court:** New York Court of Appeals
**Plugin:** `us-ny-legal-corpus`
**Pulled:** 2026-06-05

## What this corpus contains

- **Statutes:** Canonical links to the Consolidated Laws of New York at official and mirrored sources, with a sample of verbatim text pulled for representative titles.
- **Court rules:** Canonical links to the New York court rules (rules of civil/criminal/appellate procedure, evidence, local rules, etc.).
- **Case law:** On-demand indexes — see `references/ny-case-law.md`.

## Sources

### Statutes
- **NY CLS** — <https://www.nysenate.gov/legislation/laws/CONN>

### Court Rules
- **New York State Unified Court System** — <https://nycourts.gov/rules/trialcourts.shtml>

## Architecture

This plugin follows the `*-legal-corpus/` convention. It is consumable by any cross-jurisdiction `*-consumer-debt`, `*-family-law`, or `*-pro-se` skills layer that wants the New York corpus as its venue-specific reference.

## Coverage targets

- [x] Canonical statute index (links to all titles/chapters)
- [ ] Verbatim statute text (sample for the most-litigated titles; expand quarterly)
- [x] Court rules canonical link
- [ ] Verbatim court rules (sample for the rules most-cited in consumer-debt / family-law / housing matters)
- [x] Case law API index
