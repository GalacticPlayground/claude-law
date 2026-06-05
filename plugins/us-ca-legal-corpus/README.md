# California — Legal Corpus Overview

**Code Name:** California Codes (29 codes)
**Capital:** Sacramento
**Court System:** California Judicial Branch
**Highest Court:** Supreme Court of California
**Plugin:** `us-ca-legal-corpus`
**Pulled:** 2026-06-05

## What this corpus contains

- **Statutes:** Canonical links to the California Codes (29 codes) at official and mirrored sources, with a sample of verbatim text pulled for representative titles.
- **Court rules:** Canonical links to the California court rules (rules of civil/criminal/appellate procedure, evidence, local rules, etc.).
- **Case law:** On-demand indexes — see `references/ca-case-law.md`.

## Sources

### Statutes
- **California Legislative Information** — <https://leginfo.legislature.ca.gov/faces/codes.xhtml>

### Court Rules
- **California Judicial Branch** — <https://www.courts.ca.gov/rules.htm>

## Architecture

This plugin follows the `*-legal-corpus/` convention. It is consumable by any cross-jurisdiction `*-consumer-debt`, `*-family-law`, or `*-pro-se` skills layer that wants the California corpus as its venue-specific reference.

## Coverage targets

- [x] Canonical statute index (links to all titles/chapters)
- [ ] Verbatim statute text (sample for the most-litigated titles; expand quarterly)
- [x] Court rules canonical link
- [ ] Verbatim court rules (sample for the rules most-cited in consumer-debt / family-law / housing matters)
- [x] Case law API index
