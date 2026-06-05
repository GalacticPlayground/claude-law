# Minnesota — Legal Corpus Overview

**Code Name:** Minnesota Statutes
**Capital:** Saint Paul
**Court System:** Minnesota Judicial Branch
**Highest Court:** Minnesota Supreme Court
**Plugin:** `us-mn-legal-corpus`
**Pulled:** 2026-06-05

## What this corpus contains

- **Statutes:** Canonical links to the Minnesota Statutes at official and mirrored sources, with a sample of verbatim text pulled for representative titles.
- **Court rules:** Canonical links to the Minnesota court rules (rules of civil/criminal/appellate procedure, evidence, local rules, etc.).
- **Case law:** On-demand indexes — see `references/mn-case-law.md`.

## Sources

### Statutes
- **Minn. Statutes** — <https://www.revisor.mn.gov/statutes/>

### Court Rules
- **Minnesota Judicial Branch** — <https://www.mncourts.gov/SupremeCourt/Rules.aspx>

## Architecture

This plugin follows the `*-legal-corpus/` convention. It is consumable by any cross-jurisdiction `*-consumer-debt`, `*-family-law`, or `*-pro-se` skills layer that wants the Minnesota corpus as its venue-specific reference.

## Coverage targets

- [x] Canonical statute index (links to all titles/chapters)
- [ ] Verbatim statute text (sample for the most-litigated titles; expand quarterly)
- [x] Court rules canonical link
- [ ] Verbatim court rules (sample for the rules most-cited in consumer-debt / family-law / housing matters)
- [x] Case law API index
