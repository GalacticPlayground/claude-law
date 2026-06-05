# Kentucky — Legal Corpus Overview

**Code Name:** Kentucky Revised Statutes
**Capital:** Frankfort
**Court System:** Kentucky Court of Justice
**Highest Court:** Kentucky Supreme Court
**Plugin:** `us-ky-legal-corpus`
**Pulled:** 2026-06-05

## What this corpus contains

- **Statutes:** Canonical links to the Kentucky Revised Statutes at official and mirrored sources, with a sample of verbatim text pulled for representative titles.
- **Court rules:** Canonical links to the Kentucky court rules (rules of civil/criminal/appellate procedure, evidence, local rules, etc.).
- **Case law:** On-demand indexes — see `references/ky-case-law.md`.

## Sources

### Statutes
- **KRS** — <https://apps.legislature.ky.gov/law/statutes/>

### Court Rules
- **Kentucky Court of Justice** — <https://kycourts.net/Courts/Supreme-Court/Supreme-Court-Rules>

## Architecture

This plugin follows the `*-legal-corpus/` convention. It is consumable by any cross-jurisdiction `*-consumer-debt`, `*-family-law`, or `*-pro-se` skills layer that wants the Kentucky corpus as its venue-specific reference.

## Coverage targets

- [x] Canonical statute index (links to all titles/chapters)
- [ ] Verbatim statute text (sample for the most-litigated titles; expand quarterly)
- [x] Court rules canonical link
- [ ] Verbatim court rules (sample for the rules most-cited in consumer-debt / family-law / housing matters)
- [x] Case law API index
