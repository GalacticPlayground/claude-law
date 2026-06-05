# Arkansas — Legal Corpus Overview

**Code Name:** Arkansas Code
**Capital:** Little Rock
**Court System:** Arkansas Judicial Branch
**Highest Court:** Arkansas Supreme Court
**Plugin:** `us-ar-legal-corpus`
**Pulled:** 2026-06-05

## What this corpus contains

- **Statutes:** Canonical links to the Arkansas Code at official and mirrored sources, with a sample of verbatim text pulled for representative titles.
- **Court rules:** Canonical links to the Arkansas court rules (rules of civil/criminal/appellate procedure, evidence, local rules, etc.).
- **Case law:** On-demand indexes — see `references/ar-case-law.md`.

## Sources

### Statutes
- **Arkansas Code** — <https://arkleg.state.ar.us/ArkansasLaw/>

### Court Rules
- **Arkansas Judicial Branch** — <https://arcourts.gov/court-rules>

## Architecture

This plugin follows the `*-legal-corpus/` convention. It is consumable by any cross-jurisdiction `*-consumer-debt`, `*-family-law`, or `*-pro-se` skills layer that wants the Arkansas corpus as its venue-specific reference.

## Coverage targets

- [x] Canonical statute index (links to all titles/chapters)
- [ ] Verbatim statute text (sample for the most-litigated titles; expand quarterly)
- [x] Court rules canonical link
- [ ] Verbatim court rules (sample for the rules most-cited in consumer-debt / family-law / housing matters)
- [x] Case law API index
