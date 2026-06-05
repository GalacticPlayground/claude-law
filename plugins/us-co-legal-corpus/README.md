# Colorado — Legal Corpus Overview

**Code Name:** Colorado Revised Statutes
**Capital:** Denver
**Court System:** Colorado Judicial Branch
**Highest Court:** Colorado Supreme Court
**Plugin:** `us-co-legal-corpus`
**Pulled:** 2026-06-05

## What this corpus contains

- **Statutes:** Canonical links to the Colorado Revised Statutes at official and mirrored sources, with a sample of verbatim text pulled for representative titles.
- **Court rules:** Canonical links to the Colorado court rules (rules of civil/criminal/appellate procedure, evidence, local rules, etc.).
- **Case law:** On-demand indexes — see `references/co-case-law.md`.

## Sources

### Statutes
- **Colorado Revised Statutes** — <https://leg.colorado.gov/colorado-revised-statutes>

### Court Rules
- **Colorado Judicial Branch** — <https://www.courts.state.co.us/Courts/Supreme_Court/Index.cfm>

## Architecture

This plugin follows the `*-legal-corpus/` convention. It is consumable by any cross-jurisdiction `*-consumer-debt`, `*-family-law`, or `*-pro-se` skills layer that wants the Colorado corpus as its venue-specific reference.

## Coverage targets

- [x] Canonical statute index (links to all titles/chapters)
- [ ] Verbatim statute text (sample for the most-litigated titles; expand quarterly)
- [x] Court rules canonical link
- [ ] Verbatim court rules (sample for the rules most-cited in consumer-debt / family-law / housing matters)
- [x] Case law API index
