# Washington — Legal Corpus Overview

**Code Name:** Revised Code of Washington
**Capital:** Olympia
**Court System:** Washington Courts
**Highest Court:** Washington Supreme Court
**Plugin:** `us-wa-legal-corpus`
**Pulled:** 2026-06-05

## What this corpus contains

- **Statutes:** Canonical links to the Revised Code of Washington at official and mirrored sources, with a sample of verbatim text pulled for representative titles.
- **Court rules:** Canonical links to the Washington court rules (rules of civil/criminal/appellate procedure, evidence, local rules, etc.).
- **Case law:** On-demand indexes — see `references/wa-case-law.md`.

## Sources

### Statutes
- **RCW** — <https://app.leg.wa.gov/RCW/default.aspx?cite=1>

### Court Rules
- **Washington Courts** — <https://www.courts.wa.gov/court_rules/>

## Architecture

This plugin follows the `*-legal-corpus/` convention. It is consumable by any cross-jurisdiction `*-consumer-debt`, `*-family-law`, or `*-pro-se` skills layer that wants the Washington corpus as its venue-specific reference.

## Coverage targets

- [x] Canonical statute index (links to all titles/chapters)
- [ ] Verbatim statute text (sample for the most-litigated titles; expand quarterly)
- [x] Court rules canonical link
- [ ] Verbatim court rules (sample for the rules most-cited in consumer-debt / family-law / housing matters)
- [x] Case law API index
