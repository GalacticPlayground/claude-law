# Nevada — Legal Corpus Overview

**Code Name:** Nevada Revised Statutes
**Capital:** Carson City
**Court System:** Nevada Judicial Branch
**Highest Court:** Nevada Supreme Court
**Plugin:** `us-nv-legal-corpus`
**Pulled:** 2026-06-05

## What this corpus contains

- **Statutes:** Canonical links to the Nevada Revised Statutes at official and mirrored sources, with a sample of verbatim text pulled for representative titles.
- **Court rules:** Canonical links to the Nevada court rules (rules of civil/criminal/appellate procedure, evidence, local rules, etc.).
- **Case law:** On-demand indexes — see `references/nv-case-law.md`.

## Sources

### Statutes
- **NRS** — <https://www.leg.state.nv.us/NRS/NRS-001.html>

### Court Rules
- **Nevada Judicial Branch** — <https://nvcourts.gov/AOC/Templates/LegalAuthority/CourtRules>

## Architecture

This plugin follows the `*-legal-corpus/` convention. It is consumable by any cross-jurisdiction `*-consumer-debt`, `*-family-law`, or `*-pro-se` skills layer that wants the Nevada corpus as its venue-specific reference.

## Coverage targets

- [x] Canonical statute index (links to all titles/chapters)
- [ ] Verbatim statute text (sample for the most-litigated titles; expand quarterly)
- [x] Court rules canonical link
- [ ] Verbatim court rules (sample for the rules most-cited in consumer-debt / family-law / housing matters)
- [x] Case law API index
