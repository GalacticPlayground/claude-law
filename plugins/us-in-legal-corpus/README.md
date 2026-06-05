# Indiana — Legal Corpus Overview

**Code Name:** Indiana Code
**Capital:** Indianapolis
**Court System:** Indiana Judicial Branch
**Highest Court:** Indiana Supreme Court
**Plugin:** `us-in-legal-corpus`
**Pulled:** 2026-06-05

## What this corpus contains

- **Statutes:** Canonical links to the Indiana Code at official and mirrored sources, with a sample of verbatim text pulled for representative titles.
- **Court rules:** Canonical links to the Indiana court rules (rules of civil/criminal/appellate procedure, evidence, local rules, etc.).
- **Case law:** On-demand indexes — see `references/in-case-law.md`.

## Sources

### Statutes
- **Indiana Code** — <http://iga.in.gov/legislative/laws/2024/ic/titles/001#001-1-1>

### Court Rules
- **Indiana Judicial Branch** — <https://www.in.gov/courts/rules/>

## Architecture

This plugin follows the `*-legal-corpus/` convention. It is consumable by any cross-jurisdiction `*-consumer-debt`, `*-family-law`, or `*-pro-se` skills layer that wants the Indiana corpus as its venue-specific reference.

## Coverage targets

- [x] Canonical statute index (links to all titles/chapters)
- [ ] Verbatim statute text (sample for the most-litigated titles; expand quarterly)
- [x] Court rules canonical link
- [ ] Verbatim court rules (sample for the rules most-cited in consumer-debt / family-law / housing matters)
- [x] Case law API index
