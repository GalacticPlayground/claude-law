# North Dakota — Legal Corpus Overview

**Code Name:** North Dakota Century Code
**Capital:** Bismarck
**Court System:** North Dakota Judicial Branch
**Highest Court:** North Dakota Supreme Court
**Plugin:** `us-nd-legal-corpus`
**Pulled:** 2026-06-05

## What this corpus contains

- **Statutes:** Canonical links to the North Dakota Century Code at official and mirrored sources, with a sample of verbatim text pulled for representative titles.
- **Court rules:** Canonical links to the North Dakota court rules (rules of civil/criminal/appellate procedure, evidence, local rules, etc.).
- **Case law:** On-demand indexes — see `references/nd-case-law.md`.

## Sources

### Statutes
- **NDCC** — <https://www.legis.nd.gov/cencode/t01c01.pdf>

### Court Rules
- **North Dakota Judicial Branch** — <https://www.ndcourts.gov/legal-resources/rules>

## Architecture

This plugin follows the `*-legal-corpus/` convention. It is consumable by any cross-jurisdiction `*-consumer-debt`, `*-family-law`, or `*-pro-se` skills layer that wants the North Dakota corpus as its venue-specific reference.

## Coverage targets

- [x] Canonical statute index (links to all titles/chapters)
- [ ] Verbatim statute text (sample for the most-litigated titles; expand quarterly)
- [x] Court rules canonical link
- [ ] Verbatim court rules (sample for the rules most-cited in consumer-debt / family-law / housing matters)
- [x] Case law API index
