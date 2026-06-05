# Montana — Legal Corpus Overview

**Code Name:** Montana Code Annotated
**Capital:** Helena
**Court System:** Montana Judicial Branch
**Highest Court:** Montana Supreme Court
**Plugin:** `us-mt-legal-corpus`
**Pulled:** 2026-06-05

## What this corpus contains

- **Statutes:** Canonical links to the Montana Code Annotated at official and mirrored sources, with a sample of verbatim text pulled for representative titles.
- **Court rules:** Canonical links to the Montana court rules (rules of civil/criminal/appellate procedure, evidence, local rules, etc.).
- **Case law:** On-demand indexes — see `references/mt-case-law.md`.

## Sources

### Statutes
- **MCA** — <https://mca.legmt.gov/bills/mca/index.html>

### Court Rules
- **Montana Judicial Branch** — <https://courts.mt.gov/courts/supreme/orders>

## Architecture

This plugin follows the `*-legal-corpus/` convention. It is consumable by any cross-jurisdiction `*-consumer-debt`, `*-family-law`, or `*-pro-se` skills layer that wants the Montana corpus as its venue-specific reference.

## Coverage targets

- [x] Canonical statute index (links to all titles/chapters)
- [ ] Verbatim statute text (sample for the most-litigated titles; expand quarterly)
- [x] Court rules canonical link
- [ ] Verbatim court rules (sample for the rules most-cited in consumer-debt / family-law / housing matters)
- [x] Case law API index
