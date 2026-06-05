# South Carolina — Legal Corpus Overview

**Code Name:** South Carolina Code of Laws
**Capital:** Columbia
**Court System:** South Carolina Judicial Branch
**Highest Court:** Supreme Court of South Carolina
**Plugin:** `us-sc-legal-corpus`
**Pulled:** 2026-06-05

## What this corpus contains

- **Statutes:** Canonical links to the South Carolina Code of Laws at official and mirrored sources, with a sample of verbatim text pulled for representative titles.
- **Court rules:** Canonical links to the South Carolina court rules (rules of civil/criminal/appellate procedure, evidence, local rules, etc.).
- **Case law:** On-demand indexes — see `references/sc-case-law.md`.

## Sources

### Statutes
- **S.C. Code** — <https://www.scstatehouse.gov/code/t01c001.php>

### Court Rules
- **South Carolina Judicial Branch** — <https://www.sccourts.org/supreme-court/displaystatute.php?statute=rule>

## Architecture

This plugin follows the `*-legal-corpus/` convention. It is consumable by any cross-jurisdiction `*-consumer-debt`, `*-family-law`, or `*-pro-se` skills layer that wants the South Carolina corpus as its venue-specific reference.

## Coverage targets

- [x] Canonical statute index (links to all titles/chapters)
- [ ] Verbatim statute text (sample for the most-litigated titles; expand quarterly)
- [x] Court rules canonical link
- [ ] Verbatim court rules (sample for the rules most-cited in consumer-debt / family-law / housing matters)
- [x] Case law API index
