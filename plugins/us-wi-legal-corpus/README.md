# Wisconsin — Legal Corpus Overview

**Code Name:** Wisconsin Statutes
**Capital:** Madison
**Court System:** Wisconsin Court System
**Highest Court:** Wisconsin Supreme Court
**Plugin:** `us-wi-legal-corpus`
**Pulled:** 2026-06-05

## What this corpus contains

- **Statutes:** Canonical links to the Wisconsin Statutes at official and mirrored sources, with a sample of verbatim text pulled for representative titles.
- **Court rules:** Canonical links to the Wisconsin court rules (rules of civil/criminal/appellate procedure, evidence, local rules, etc.).
- **Case law:** On-demand indexes — see `references/wi-case-law.md`.

## Sources

### Statutes
- **Wis. Stat.** — <https://docs.legis.wisconsin.gov/statutes/prefaces/toc>

### Court Rules
- **Wisconsin Court System** — <https://www.wicourts.gov/courts/supreme/viewrules.jsp>

## Architecture

This plugin follows the `*-legal-corpus/` convention. It is consumable by any cross-jurisdiction `*-consumer-debt`, `*-family-law`, or `*-pro-se` skills layer that wants the Wisconsin corpus as its venue-specific reference.

## Coverage targets

- [x] Canonical statute index (links to all titles/chapters)
- [ ] Verbatim statute text (sample for the most-litigated titles; expand quarterly)
- [x] Court rules canonical link
- [ ] Verbatim court rules (sample for the rules most-cited in consumer-debt / family-law / housing matters)
- [x] Case law API index
