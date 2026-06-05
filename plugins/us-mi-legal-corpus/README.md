# Michigan — Legal Corpus Overview

**Code Name:** Michigan Compiled Laws
**Capital:** Lansing
**Court System:** Michigan Judicial Branch
**Highest Court:** Michigan Supreme Court
**Plugin:** `us-mi-legal-corpus`
**Pulled:** 2026-06-05

## What this corpus contains

- **Statutes:** Canonical links to the Michigan Compiled Laws at official and mirrored sources, with a sample of verbatim text pulled for representative titles.
- **Court rules:** Canonical links to the Michigan court rules (rules of civil/criminal/appellate procedure, evidence, local rules, etc.).
- **Case law:** On-demand indexes — see `references/mi-case-law.md`.

## Sources

### Statutes
- **MCL Chapter Index** — <https://www.legislature.mi.gov/Laws/ChapterIndex>

### Court Rules
- **Michigan Judicial Branch** — <https://courts.michigan.gov/courts/supremecourt/clerks/rules-court-orders>

## Architecture

This plugin follows the `*-legal-corpus/` convention. It is consumable by any cross-jurisdiction `*-consumer-debt`, `*-family-law`, or `*-pro-se` skills layer that wants the Michigan corpus as its venue-specific reference.

## Coverage targets

- [x] Canonical statute index (links to all titles/chapters)
- [ ] Verbatim statute text (sample for the most-litigated titles; expand quarterly)
- [x] Court rules canonical link
- [ ] Verbatim court rules (sample for the rules most-cited in consumer-debt / family-law / housing matters)
- [x] Case law API index
