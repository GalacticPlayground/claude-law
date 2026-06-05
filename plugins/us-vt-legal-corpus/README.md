# Vermont — Legal Corpus Overview

**Code Name:** Vermont Statutes Annotated
**Capital:** Montpelier
**Court System:** Vermont Judiciary
**Highest Court:** Vermont Supreme Court
**Plugin:** `us-vt-legal-corpus`
**Pulled:** 2026-06-05

## What this corpus contains

- **Statutes:** Canonical links to the Vermont Statutes Annotated at official and mirrored sources, with a sample of verbatim text pulled for representative titles.
- **Court rules:** Canonical links to the Vermont court rules (rules of civil/criminal/appellate procedure, evidence, local rules, etc.).
- **Case law:** On-demand indexes — see `references/vt-case-law.md`.

## Sources

### Statutes
- **V.S.A.** — <https://legislature.vermont.gov/statutes/section/1/1>

### Court Rules
- **Vermont Judiciary** — <https://www.vermontjudiciary.org/court-rules>

## Architecture

This plugin follows the `*-legal-corpus/` convention. It is consumable by any cross-jurisdiction `*-consumer-debt`, `*-family-law`, or `*-pro-se` skills layer that wants the Vermont corpus as its venue-specific reference.

## Coverage targets

- [x] Canonical statute index (links to all titles/chapters)
- [ ] Verbatim statute text (sample for the most-litigated titles; expand quarterly)
- [x] Court rules canonical link
- [ ] Verbatim court rules (sample for the rules most-cited in consumer-debt / family-law / housing matters)
- [x] Case law API index
