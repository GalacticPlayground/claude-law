# Virginia — Legal Corpus Overview

**Code Name:** Code of Virginia
**Capital:** Richmond
**Court System:** Virginia Judicial System
**Highest Court:** Supreme Court of Virginia
**Plugin:** `us-va-legal-corpus`
**Pulled:** 2026-06-05

## What this corpus contains

- **Statutes:** Canonical links to the Code of Virginia at official and mirrored sources, with a sample of verbatim text pulled for representative titles.
- **Court rules:** Canonical links to the Virginia court rules (rules of civil/criminal/appellate procedure, evidence, local rules, etc.).
- **Case law:** On-demand indexes — see `references/va-case-law.md`.

## Sources

### Statutes
- **Va. Code** — <https://law.lis.virginia.gov/vacode/title1/chapter1/>

### Court Rules
- **Virginia Judicial System** — <https://www.vacourts.gov/courts/scc/rules_of_court.pdf>

## Architecture

This plugin follows the `*-legal-corpus/` convention. It is consumable by any cross-jurisdiction `*-consumer-debt`, `*-family-law`, or `*-pro-se` skills layer that wants the Virginia corpus as its venue-specific reference.

## Coverage targets

- [x] Canonical statute index (links to all titles/chapters)
- [ ] Verbatim statute text (sample for the most-litigated titles; expand quarterly)
- [x] Court rules canonical link
- [ ] Verbatim court rules (sample for the rules most-cited in consumer-debt / family-law / housing matters)
- [x] Case law API index
