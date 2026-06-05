# Arizona — Legal Corpus Overview

**Code Name:** Arizona Revised Statutes
**Capital:** Phoenix
**Court System:** Arizona Judicial Branch
**Highest Court:** Arizona Supreme Court
**Plugin:** `us-az-legal-corpus`
**Pulled:** 2026-06-05

## What this corpus contains

- **Statutes:** Canonical links to the Arizona Revised Statutes at official and mirrored sources, with a sample of verbatim text pulled for representative titles.
- **Court rules:** Canonical links to the Arizona court rules (rules of civil/criminal/appellate procedure, evidence, local rules, etc.).
- **Case law:** On-demand indexes — see `references/az-case-law.md`.

## Sources

### Statutes
- **Arizona Revised Statutes** — <https://www.azleg.gov/arsDetail/?title=1>

### Court Rules
- **Arizona Judicial Branch** — <https://www.azcourts.gov/rules/>

## Architecture

This plugin follows the `*-legal-corpus/` convention. It is consumable by any cross-jurisdiction `*-consumer-debt`, `*-family-law`, or `*-pro-se` skills layer that wants the Arizona corpus as its venue-specific reference.

## Coverage targets

- [x] Canonical statute index (links to all titles/chapters)
- [ ] Verbatim statute text (sample for the most-litigated titles; expand quarterly)
- [x] Court rules canonical link
- [ ] Verbatim court rules (sample for the rules most-cited in consumer-debt / family-law / housing matters)
- [x] Case law API index
