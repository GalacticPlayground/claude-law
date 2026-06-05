# North Carolina — Legal Corpus Overview

**Code Name:** North Carolina General Statutes
**Capital:** Raleigh
**Court System:** North Carolina Judicial Branch
**Highest Court:** Supreme Court of North Carolina
**Plugin:** `us-nc-legal-corpus`
**Pulled:** 2026-06-05

## What this corpus contains

- **Statutes:** Canonical links to the North Carolina General Statutes at official and mirrored sources, with a sample of verbatim text pulled for representative titles.
- **Court rules:** Canonical links to the North Carolina court rules (rules of civil/criminal/appellate procedure, evidence, local rules, etc.).
- **Case law:** On-demand indexes — see `references/nc-case-law.md`.

## Sources

### Statutes
- **NCGS** — <https://www.ncleg.gov/Laws/GeneralStatutesTOC>

### Court Rules
- **North Carolina Judicial Branch** — <https://www.nccourts.gov/courts/supreme-court/rules>

## Architecture

This plugin follows the `*-legal-corpus/` convention. It is consumable by any cross-jurisdiction `*-consumer-debt`, `*-family-law`, or `*-pro-se` skills layer that wants the North Carolina corpus as its venue-specific reference.

## Coverage targets

- [x] Canonical statute index (links to all titles/chapters)
- [ ] Verbatim statute text (sample for the most-litigated titles; expand quarterly)
- [x] Court rules canonical link
- [ ] Verbatim court rules (sample for the rules most-cited in consumer-debt / family-law / housing matters)
- [x] Case law API index
