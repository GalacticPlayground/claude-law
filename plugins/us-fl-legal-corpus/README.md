# Florida — Legal Corpus Overview

**Code Name:** Florida Statutes
**Capital:** Tallahassee
**Court System:** Florida State Courts
**Highest Court:** Florida Supreme Court
**Plugin:** `us-fl-legal-corpus`
**Pulled:** 2026-06-05

## What this corpus contains

- **Statutes:** Canonical links to the Florida Statutes at official and mirrored sources, with a sample of verbatim text pulled for representative titles.
- **Court rules:** Canonical links to the Florida court rules (rules of civil/criminal/appellate procedure, evidence, local rules, etc.).
- **Case law:** On-demand indexes — see `references/fl-case-law.md`.

## Sources

### Statutes
- **Florida Statutes** — <https://www.leg.state.fl.us/Statutes/index.cfm?App_mode=Display_Statute&URL=0000-0099/0001/Sections/0001.001.html>

### Court Rules
- **Florida State Courts** — <https://www.flcourts.org/Supreme-Court/Procedures-Rules.shtml>

## Architecture

This plugin follows the `*-legal-corpus/` convention. It is consumable by any cross-jurisdiction `*-consumer-debt`, `*-family-law`, or `*-pro-se` skills layer that wants the Florida corpus as its venue-specific reference.

## Coverage targets

- [x] Canonical statute index (links to all titles/chapters)
- [ ] Verbatim statute text (sample for the most-litigated titles; expand quarterly)
- [x] Court rules canonical link
- [ ] Verbatim court rules (sample for the rules most-cited in consumer-debt / family-law / housing matters)
- [x] Case law API index
