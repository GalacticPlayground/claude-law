# Connecticut — Legal Corpus Overview

**Code Name:** Connecticut General Statutes
**Capital:** Hartford
**Court System:** Connecticut Judicial Branch
**Highest Court:** Connecticut Supreme Court
**Plugin:** `us-ct-legal-corpus`
**Pulled:** 2026-06-05

## What this corpus contains

- **Statutes:** Canonical links to the Connecticut General Statutes at official and mirrored sources, with a sample of verbatim text pulled for representative titles.
- **Court rules:** Canonical links to the Connecticut court rules (rules of civil/criminal/appellate procedure, evidence, local rules, etc.).
- **Case law:** On-demand indexes — see `references/ct-case-law.md`.

## Sources

### Statutes
- **CGS Title Index** — <https://www.cga.ct.gov/current/pub/titles.htm>

### Court Rules
- **Connecticut Judicial Branch** — <https://www.jud.ct.gov/>

## Architecture

This plugin follows the `*-legal-corpus/` convention. It is consumable by any cross-jurisdiction `*-consumer-debt`, `*-family-law`, or `*-pro-se` skills layer that wants the Connecticut corpus as its venue-specific reference.

## Coverage targets

- [x] Canonical statute index (links to all titles/chapters)
- [ ] Verbatim statute text (sample for the most-litigated titles; expand quarterly)
- [x] Court rules canonical link
- [ ] Verbatim court rules (sample for the rules most-cited in consumer-debt / family-law / housing matters)
- [x] Case law API index
