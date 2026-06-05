# Alabama — Legal Corpus Overview

**Code Name:** Code of Alabama 1975
**Capital:** Montgomery
**Court System:** Unified Judicial System
**Highest Court:** Supreme Court of Alabama
**Plugin:** `us-al-legal-corpus`
**Pulled:** 2026-06-05

## What this corpus contains

- **Statutes:** Canonical links to the Code of Alabama 1975 at official and mirrored sources, with a sample of verbatim text pulled for representative titles.
- **Court rules:** Canonical links to the Alabama court rules (rules of civil/criminal/appellate procedure, evidence, local rules, etc.).
- **Case law:** On-demand indexes — see `references/al-case-law.md`.

## Sources

### Statutes
- **Alabama Legislature Code Search** — <https://alison.legislature.state.al.us/>

### Court Rules
- **Unified Judicial System** — <https://judicial.alabama.gov/Resources/rules>

## Architecture

This plugin follows the `*-legal-corpus/` convention. It is consumable by any cross-jurisdiction `*-consumer-debt`, `*-family-law`, or `*-pro-se` skills layer that wants the Alabama corpus as its venue-specific reference.

## Coverage targets

- [x] Canonical statute index (links to all titles/chapters)
- [ ] Verbatim statute text (sample for the most-litigated titles; expand quarterly)
- [x] Court rules canonical link
- [ ] Verbatim court rules (sample for the rules most-cited in consumer-debt / family-law / housing matters)
- [x] Case law API index
