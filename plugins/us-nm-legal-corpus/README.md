# New Mexico — Legal Corpus Overview

**Code Name:** New Mexico Statutes Annotated
**Capital:** Santa Fe
**Court System:** New Mexico Judicial Branch
**Highest Court:** New Mexico Supreme Court
**Plugin:** `us-nm-legal-corpus`
**Pulled:** 2026-06-05

## What this corpus contains

- **Statutes:** Canonical links to the New Mexico Statutes Annotated at official and mirrored sources, with a sample of verbatim text pulled for representative titles.
- **Court rules:** Canonical links to the New Mexico court rules (rules of civil/criminal/appellate procedure, evidence, local rules, etc.).
- **Case law:** On-demand indexes — see `references/nm-case-law.md`.

## Sources

### Statutes
- **NMSA** — <https://www.nmcompcomm.us/>

### Court Rules
- **New Mexico Judicial Branch** — <https://nmcourts.gov/rules/>

## Architecture

This plugin follows the `*-legal-corpus/` convention. It is consumable by any cross-jurisdiction `*-consumer-debt`, `*-family-law`, or `*-pro-se` skills layer that wants the New Mexico corpus as its venue-specific reference.

## Coverage targets

- [x] Canonical statute index (links to all titles/chapters)
- [ ] Verbatim statute text (sample for the most-litigated titles; expand quarterly)
- [x] Court rules canonical link
- [ ] Verbatim court rules (sample for the rules most-cited in consumer-debt / family-law / housing matters)
- [x] Case law API index
