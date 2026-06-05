# Texas — Legal Corpus Overview

**Code Name:** Texas Statutes
**Capital:** Austin
**Court System:** Texas Judicial Branch
**Highest Court:** Supreme Court of Texas
**Plugin:** `us-tx-legal-corpus`
**Pulled:** 2026-06-05

## What this corpus contains

- **Statutes:** Canonical links to the Texas Statutes at official and mirrored sources, with a sample of verbatim text pulled for representative titles.
- **Court rules:** Canonical links to the Texas court rules (rules of civil/criminal/appellate procedure, evidence, local rules, etc.).
- **Case law:** On-demand indexes — see `references/tx-case-law.md`.

## Sources

### Statutes
- **Tex. Statutes** — <https://statutes.capitol.texas.gov/Docs/AS/htm/AS.1.htm>

### Court Rules
- **Texas Judicial Branch** — <https://www.txcourts.gov/rules-forms/rules-of-court/>

## Architecture

This plugin follows the `*-legal-corpus/` convention. It is consumable by any cross-jurisdiction `*-consumer-debt`, `*-family-law`, or `*-pro-se` skills layer that wants the Texas corpus as its venue-specific reference.

## Coverage targets

- [x] Canonical statute index (links to all titles/chapters)
- [ ] Verbatim statute text (sample for the most-litigated titles; expand quarterly)
- [x] Court rules canonical link
- [ ] Verbatim court rules (sample for the rules most-cited in consumer-debt / family-law / housing matters)
- [x] Case law API index
