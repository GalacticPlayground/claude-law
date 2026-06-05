# Oklahoma — Legal Corpus Overview

**Code Name:** Oklahoma Statutes
**Capital:** Oklahoma City
**Court System:** Oklahoma Judicial System
**Highest Court:** Supreme Court of Oklahoma
**Plugin:** `us-ok-legal-corpus`
**Pulled:** 2026-06-05

## What this corpus contains

- **Statutes:** Canonical links to the Oklahoma Statutes at official and mirrored sources, with a sample of verbatim text pulled for representative titles.
- **Court rules:** Canonical links to the Oklahoma court rules (rules of civil/criminal/appellate procedure, evidence, local rules, etc.).
- **Case law:** On-demand indexes — see `references/ok-case-law.md`.

## Sources

### Statutes
- **O.S.** — <https://www.oklegislature.gov/osstatuestitle.aspx>
- **OSCN** — <https://www.oscn.net/applications/oscn/index.asp?level=1&ftdb=STOKST>

### Court Rules
- **Oklahoma Judicial System** — <https://www.oscn.net/rules>

## Architecture

This plugin follows the `*-legal-corpus/` convention. It is consumable by any cross-jurisdiction `*-consumer-debt`, `*-family-law`, or `*-pro-se` skills layer that wants the Oklahoma corpus as its venue-specific reference.

## Coverage targets

- [x] Canonical statute index (links to all titles/chapters)
- [ ] Verbatim statute text (sample for the most-litigated titles; expand quarterly)
- [x] Court rules canonical link
- [ ] Verbatim court rules (sample for the rules most-cited in consumer-debt / family-law / housing matters)
- [x] Case law API index
