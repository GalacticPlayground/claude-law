# Hawaii — Legal Corpus Overview

**Code Name:** Hawaii Revised Statutes
**Capital:** Honolulu
**Court System:** Hawaii State Judiciary
**Highest Court:** Hawaii Supreme Court
**Plugin:** `us-hi-legal-corpus`
**Pulled:** 2026-06-05

## What this corpus contains

- **Statutes:** Canonical links to the Hawaii Revised Statutes at official and mirrored sources, with a sample of verbatim text pulled for representative titles.
- **Court rules:** Canonical links to the Hawaii court rules (rules of civil/criminal/appellate procedure, evidence, local rules, etc.).
- **Case law:** On-demand indexes — see `references/hi-case-law.md`.

## Sources

### Statutes
- **HRS Vol 1** — <https://www.capitol.hawaii.gov/hrscurrent/Vol01_Ch0001-0042/>

### Court Rules
- **Hawaii State Judiciary** — <https://www.courts.state.hi.us/>

## Architecture

This plugin follows the `*-legal-corpus/` convention. It is consumable by any cross-jurisdiction `*-consumer-debt`, `*-family-law`, or `*-pro-se` skills layer that wants the Hawaii corpus as its venue-specific reference.

## Coverage targets

- [x] Canonical statute index (links to all titles/chapters)
- [ ] Verbatim statute text (sample for the most-litigated titles; expand quarterly)
- [x] Court rules canonical link
- [ ] Verbatim court rules (sample for the rules most-cited in consumer-debt / family-law / housing matters)
- [x] Case law API index
