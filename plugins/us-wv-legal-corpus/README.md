# West Virginia — Legal Corpus Overview

**Code Name:** West Virginia Code
**Capital:** Charleston
**Court System:** West Virginia Judiciary
**Highest Court:** Supreme Court of Appeals of West Virginia
**Plugin:** `us-wv-legal-corpus`
**Pulled:** 2026-06-05

## What this corpus contains

- **Statutes:** Canonical links to the West Virginia Code at official and mirrored sources, with a sample of verbatim text pulled for representative titles.
- **Court rules:** Canonical links to the West Virginia court rules (rules of civil/criminal/appellate procedure, evidence, local rules, etc.).
- **Case law:** On-demand indexes — see `references/wv-case-law.md`.

## Sources

### Statutes
- **W. Va. Code** — <https://code.wvlegislature.gov/1-1-1/>

### Court Rules
- **West Virginia Judiciary** — <https://courtswv.gov/legal-community/court-rules>

## Architecture

This plugin follows the `*-legal-corpus/` convention. It is consumable by any cross-jurisdiction `*-consumer-debt`, `*-family-law`, or `*-pro-se` skills layer that wants the West Virginia corpus as its venue-specific reference.

## Coverage targets

- [x] Canonical statute index (links to all titles/chapters)
- [ ] Verbatim statute text (sample for the most-litigated titles; expand quarterly)
- [x] Court rules canonical link
- [ ] Verbatim court rules (sample for the rules most-cited in consumer-debt / family-law / housing matters)
- [x] Case law API index
