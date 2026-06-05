# Maryland — Legal Corpus Overview

**Code Name:** Maryland Code
**Capital:** Annapolis
**Court System:** Maryland Judicial Branch
**Highest Court:** Maryland Supreme Court
**Plugin:** `us-md-legal-corpus`
**Pulled:** 2026-06-05

## What this corpus contains

- **Statutes:** Canonical links to the Maryland Code at official and mirrored sources, with a sample of verbatim text pulled for representative titles.
- **Court rules:** Canonical links to the Maryland court rules (rules of civil/criminal/appellate procedure, evidence, local rules, etc.).
- **Case law:** On-demand indexes — see `references/md-case-law.md`.

## Sources

### Statutes
- **MD Code** — <https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText?article=gtr&section=1-101>

### Court Rules
- **Maryland Judicial Branch** — <https://www.mdcourts.gov/rules>

## Architecture

This plugin follows the `*-legal-corpus/` convention. It is consumable by any cross-jurisdiction `*-consumer-debt`, `*-family-law`, or `*-pro-se` skills layer that wants the Maryland corpus as its venue-specific reference.

## Coverage targets

- [x] Canonical statute index (links to all titles/chapters)
- [ ] Verbatim statute text (sample for the most-litigated titles; expand quarterly)
- [x] Court rules canonical link
- [ ] Verbatim court rules (sample for the rules most-cited in consumer-debt / family-law / housing matters)
- [x] Case law API index
