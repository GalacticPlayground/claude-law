# Ohio — Legal Corpus Overview

**Code Name:** Ohio Revised Code
**Capital:** Columbus
**Court System:** Ohio Judicial System
**Highest Court:** Supreme Court of Ohio
**Plugin:** `us-oh-legal-corpus`
**Pulled:** 2026-06-05

## What this corpus contains

- **Statutes:** Canonical links to the Ohio Revised Code at official and mirrored sources, with a sample of verbatim text pulled for representative titles.
- **Court rules:** Canonical links to the Ohio court rules (rules of civil/criminal/appellate procedure, evidence, local rules, etc.).
- **Case law:** On-demand indexes — see `references/oh-case-law.md`.

## Sources

### Statutes
- **ORC** — <https://codes.ohio.gov/orc/1.1>

### Court Rules
- **Ohio Judicial System** — <https://www.supremecourt.ohio.gov/LegalResources/Rules/civilprocedure/civproc.pdf>

## Architecture

This plugin follows the `*-legal-corpus/` convention. It is consumable by any cross-jurisdiction `*-consumer-debt`, `*-family-law`, or `*-pro-se` skills layer that wants the Ohio corpus as its venue-specific reference.

## Coverage targets

- [x] Canonical statute index (links to all titles/chapters)
- [ ] Verbatim statute text (sample for the most-litigated titles; expand quarterly)
- [x] Court rules canonical link
- [ ] Verbatim court rules (sample for the rules most-cited in consumer-debt / family-law / housing matters)
- [x] Case law API index
