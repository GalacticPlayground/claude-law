# Pennsylvania — Legal Corpus Overview

**Code Name:** Pennsylvania Consolidated Statutes
**Capital:** Harrisburg
**Court System:** Unified Judicial System of Pennsylvania
**Highest Court:** Supreme Court of Pennsylvania
**Plugin:** `us-pa-legal-corpus`
**Pulled:** 2026-06-05

## What this corpus contains

- **Statutes:** Canonical links to the Pennsylvania Consolidated Statutes at official and mirrored sources, with a sample of verbatim text pulled for representative titles.
- **Court rules:** Canonical links to the Pennsylvania court rules (rules of civil/criminal/appellate procedure, evidence, local rules, etc.).
- **Case law:** On-demand indexes — see `references/pa-case-law.md`.

## Sources

### Statutes
- **Pa.C.S.** — <https://www.legis.state.pa.us/cfdocs/legis/LI/uconsCheck.cfm?txtType=HTM&yr=1990&sessInd=0&smthLwInd=0&act=0>

### Court Rules
- **Unified Judicial System of Pennsylvania** — <https://www.pacourts.us/courts/supreme-court/rules-of-court>

## Architecture

This plugin follows the `*-legal-corpus/` convention. It is consumable by any cross-jurisdiction `*-consumer-debt`, `*-family-law`, or `*-pro-se` skills layer that wants the Pennsylvania corpus as its venue-specific reference.

## Coverage targets

- [x] Canonical statute index (links to all titles/chapters)
- [ ] Verbatim statute text (sample for the most-litigated titles; expand quarterly)
- [x] Court rules canonical link
- [ ] Verbatim court rules (sample for the rules most-cited in consumer-debt / family-law / housing matters)
- [x] Case law API index
