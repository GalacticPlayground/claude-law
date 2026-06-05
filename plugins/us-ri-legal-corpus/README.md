# Rhode Island — Legal Corpus Overview

**Code Name:** Rhode Island General Laws
**Capital:** Providence
**Court System:** Rhode Island Judiciary
**Highest Court:** Rhode Island Supreme Court
**Plugin:** `us-ri-legal-corpus`
**Pulled:** 2026-06-05

## What this corpus contains

- **Statutes:** Canonical links to the Rhode Island General Laws at official and mirrored sources, with a sample of verbatim text pulled for representative titles.
- **Court rules:** Canonical links to the Rhode Island court rules (rules of civil/criminal/appellate procedure, evidence, local rules, etc.).
- **Case law:** On-demand indexes — see `references/ri-case-law.md`.

## Sources

### Statutes
- **R.I. Gen. Laws** — <https://webserver.rilegislature.gov/Statutes/title1/1-1/1-1-1.htm>

### Court Rules
- **Rhode Island Judiciary** — <https://www.courts.ri.gov/Courts/SupremeCourt/Pages/Rules.aspx>

## Architecture

This plugin follows the `*-legal-corpus/` convention. It is consumable by any cross-jurisdiction `*-consumer-debt`, `*-family-law`, or `*-pro-se` skills layer that wants the Rhode Island corpus as its venue-specific reference.

## Coverage targets

- [x] Canonical statute index (links to all titles/chapters)
- [ ] Verbatim statute text (sample for the most-litigated titles; expand quarterly)
- [x] Court rules canonical link
- [ ] Verbatim court rules (sample for the rules most-cited in consumer-debt / family-law / housing matters)
- [x] Case law API index
