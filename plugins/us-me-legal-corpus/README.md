# Maine — Legal Corpus Overview

**Code Name:** Maine Revised Statutes
**Capital:** Augusta
**Court System:** Maine Judicial Branch
**Highest Court:** Maine Supreme Judicial Court
**Plugin:** `us-me-legal-corpus`
**Pulled:** 2026-06-05

## What this corpus contains

- **Statutes:** Canonical links to the Maine Revised Statutes at official and mirrored sources, with a sample of verbatim text pulled for representative titles.
- **Court rules:** Canonical links to the Maine court rules (rules of civil/criminal/appellate procedure, evidence, local rules, etc.).
- **Case law:** On-demand indexes — see `references/me-case-law.md`.

## Sources

### Statutes
- **MRS** — <https://legislature.maine.gov/statutes/1/title1ch1sec0.html>

### Court Rules
- **Maine Judicial Branch** — <https://www.courts.maine.gov/rules/index.html>

## Architecture

This plugin follows the `*-legal-corpus/` convention. It is consumable by any cross-jurisdiction `*-consumer-debt`, `*-family-law`, or `*-pro-se` skills layer that wants the Maine corpus as its venue-specific reference.

## Coverage targets

- [x] Canonical statute index (links to all titles/chapters)
- [ ] Verbatim statute text (sample for the most-litigated titles; expand quarterly)
- [x] Court rules canonical link
- [ ] Verbatim court rules (sample for the rules most-cited in consumer-debt / family-law / housing matters)
- [x] Case law API index
