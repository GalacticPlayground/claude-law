# Louisiana — Legal Corpus Overview

**Code Name:** Louisiana Revised Statutes
**Capital:** Baton Rouge
**Court System:** Louisiana Judicial Branch
**Highest Court:** Louisiana Supreme Court
**Plugin:** `us-la-legal-corpus`
**Pulled:** 2026-06-05

## What this corpus contains

- **Statutes:** Canonical links to the Louisiana Revised Statutes at official and mirrored sources, with a sample of verbatim text pulled for representative titles.
- **Court rules:** Canonical links to the Louisiana court rules (rules of civil/criminal/appellate procedure, evidence, local rules, etc.).
- **Case law:** On-demand indexes — see `references/la-case-law.md`.

## Sources

### Statutes
- **LRS** — <https://www.legis.la.gov/legis/Law_Toc.aspx?folder=1>

### Court Rules
- **Louisiana Judicial Branch** — <https://www.lasc.org/Court_Rules>

## Architecture

This plugin follows the `*-legal-corpus/` convention. It is consumable by any cross-jurisdiction `*-consumer-debt`, `*-family-law`, or `*-pro-se` skills layer that wants the Louisiana corpus as its venue-specific reference.

## Coverage targets

- [x] Canonical statute index (links to all titles/chapters)
- [ ] Verbatim statute text (sample for the most-litigated titles; expand quarterly)
- [x] Court rules canonical link
- [ ] Verbatim court rules (sample for the rules most-cited in consumer-debt / family-law / housing matters)
- [x] Case law API index
