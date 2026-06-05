# Oregon — Legal Corpus Overview

**Code Name:** Oregon Revised Statutes
**Capital:** Salem
**Court System:** Oregon Judicial Department
**Highest Court:** Oregon Supreme Court
**Plugin:** `us-or-legal-corpus`
**Pulled:** 2026-06-05

## What this corpus contains

- **Statutes:** Canonical links to the Oregon Revised Statutes at official and mirrored sources, with a sample of verbatim text pulled for representative titles.
- **Court rules:** Canonical links to the Oregon court rules (rules of civil/criminal/appellate procedure, evidence, local rules, etc.).
- **Case law:** On-demand indexes — see `references/or-case-law.md`.

## Sources

### Statutes
- **ORS** — <https://www.oregonlegislature.gov/bills_laws/ors/ors001.html>

### Court Rules
- **Oregon Judicial Department** — <https://www.courts.oregon.gov/programs/utcr/Pages/index.aspx>

## Architecture

This plugin follows the `*-legal-corpus/` convention. It is consumable by any cross-jurisdiction `*-consumer-debt`, `*-family-law`, or `*-pro-se` skills layer that wants the Oregon corpus as its venue-specific reference.

## Coverage targets

- [x] Canonical statute index (links to all titles/chapters)
- [ ] Verbatim statute text (sample for the most-litigated titles; expand quarterly)
- [x] Court rules canonical link
- [ ] Verbatim court rules (sample for the rules most-cited in consumer-debt / family-law / housing matters)
- [x] Case law API index
