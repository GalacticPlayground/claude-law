# Mississippi — Legal Corpus Overview

**Code Name:** Mississippi Code
**Capital:** Jackson
**Court System:** Mississippi Judicial Branch
**Highest Court:** Mississippi Supreme Court
**Plugin:** `us-ms-legal-corpus`
**Pulled:** 2026-06-05

## What this corpus contains

- **Statutes:** Canonical links to the Mississippi Code at official and mirrored sources, with a sample of verbatim text pulled for representative titles.
- **Court rules:** Canonical links to the Mississippi court rules (rules of civil/criminal/appellate procedure, evidence, local rules, etc.).
- **Case law:** On-demand indexes — see `references/ms-case-law.md`.

## Sources

### Statutes
- **MS Code** — <https://www.sos.ms.gov/Education-Publications/Pages/Code.aspx>

### Court Rules
- **Mississippi Judicial Branch** — <https://courts.ms.gov/rules/rules.php>

## Architecture

This plugin follows the `*-legal-corpus/` convention. It is consumable by any cross-jurisdiction `*-consumer-debt`, `*-family-law`, or `*-pro-se` skills layer that wants the Mississippi corpus as its venue-specific reference.

## Coverage targets

- [x] Canonical statute index (links to all titles/chapters)
- [ ] Verbatim statute text (sample for the most-litigated titles; expand quarterly)
- [x] Court rules canonical link
- [ ] Verbatim court rules (sample for the rules most-cited in consumer-debt / family-law / housing matters)
- [x] Case law API index
