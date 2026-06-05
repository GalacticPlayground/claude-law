# Alaska — Legal Corpus Overview

**Code Name:** Alaska Statutes
**Capital:** Juneau
**Court System:** Alaska Court System
**Highest Court:** Alaska Supreme Court
**Plugin:** `us-ak-legal-corpus`
**Pulled:** 2026-06-05

## What this corpus contains

- **Statutes:** Canonical links to the Alaska Statutes at official and mirrored sources, with a sample of verbatim text pulled for representative titles.
- **Court rules:** Canonical links to the Alaska court rules (rules of civil/criminal/appellate procedure, evidence, local rules, etc.).
- **Case law:** On-demand indexes — see `references/ak-case-law.md`.

## Sources

### Statutes
- **Alaska Statutes** — <https://www.akleg.gov/basis/statutes.asp>

### Court Rules
- **Alaska Court System** — <https://courts.alaska.gov/rules/index.htm>

## Architecture

This plugin follows the `*-legal-corpus/` convention. It is consumable by any cross-jurisdiction `*-consumer-debt`, `*-family-law`, or `*-pro-se` skills layer that wants the Alaska corpus as its venue-specific reference.

## Coverage targets

- [x] Canonical statute index (links to all titles/chapters)
- [ ] Verbatim statute text (sample for the most-litigated titles; expand quarterly)
- [x] Court rules canonical link
- [ ] Verbatim court rules (sample for the rules most-cited in consumer-debt / family-law / housing matters)
- [x] Case law API index
