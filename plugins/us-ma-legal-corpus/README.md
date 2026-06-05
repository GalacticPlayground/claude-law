# Massachusetts — Legal Corpus Overview

**Code Name:** Massachusetts General Laws
**Capital:** Boston
**Court System:** Massachusetts Court System
**Highest Court:** Massachusetts Supreme Judicial Court
**Plugin:** `us-ma-legal-corpus`
**Pulled:** 2026-06-05

## What this corpus contains

- **Statutes:** Canonical links to the Massachusetts General Laws at official and mirrored sources, with a sample of verbatim text pulled for representative titles.
- **Court rules:** Canonical links to the Massachusetts court rules (rules of civil/criminal/appellate procedure, evidence, local rules, etc.).
- **Case law:** On-demand indexes — see `references/ma-case-law.md`.

## Sources

### Statutes
- **MGL** — <https://malegislature.gov/Laws/GeneralLaws/PartI/TitleI/Chapter1/Section1>

### Court Rules
- **Massachusetts Court System** — <https://www.mass.gov/info-details/massachusetts-rules-of-court>

## Architecture

This plugin follows the `*-legal-corpus/` convention. It is consumable by any cross-jurisdiction `*-consumer-debt`, `*-family-law`, or `*-pro-se` skills layer that wants the Massachusetts corpus as its venue-specific reference.

## Coverage targets

- [x] Canonical statute index (links to all titles/chapters)
- [ ] Verbatim statute text (sample for the most-litigated titles; expand quarterly)
- [x] Court rules canonical link
- [ ] Verbatim court rules (sample for the rules most-cited in consumer-debt / family-law / housing matters)
- [x] Case law API index
