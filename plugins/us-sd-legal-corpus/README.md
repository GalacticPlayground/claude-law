# South Dakota — Legal Corpus Overview

**Code Name:** South Dakota Codified Laws
**Capital:** Pierre
**Court System:** South Dakota Unified Judicial System
**Highest Court:** South Dakota Supreme Court
**Plugin:** `us-sd-legal-corpus`
**Pulled:** 2026-06-05

## What this corpus contains

- **Statutes:** Canonical links to the South Dakota Codified Laws at official and mirrored sources, with a sample of verbatim text pulled for representative titles.
- **Court rules:** Canonical links to the South Dakota court rules (rules of civil/criminal/appellate procedure, evidence, local rules, etc.).
- **Case law:** On-demand indexes — see `references/sd-case-law.md`.

## Sources

### Statutes
- **SDCL** — <https://sdlegislature.gov/Statutes/1-1>

### Court Rules
- **South Dakota Unified Judicial System** — <https://ujs.sd.gov/Court_Rules/default.aspx>

## Architecture

This plugin follows the `*-legal-corpus/` convention. It is consumable by any cross-jurisdiction `*-consumer-debt`, `*-family-law`, or `*-pro-se` skills layer that wants the South Dakota corpus as its venue-specific reference.

## Coverage targets

- [x] Canonical statute index (links to all titles/chapters)
- [ ] Verbatim statute text (sample for the most-litigated titles; expand quarterly)
- [x] Court rules canonical link
- [ ] Verbatim court rules (sample for the rules most-cited in consumer-debt / family-law / housing matters)
- [x] Case law API index
