# New Jersey — Legal Corpus Overview

**Code Name:** New Jersey Revised Statutes
**Capital:** Trenton
**Court System:** New Jersey Courts
**Highest Court:** Supreme Court of New Jersey
**Plugin:** `us-nj-legal-corpus`
**Pulled:** 2026-06-05

## What this corpus contains

- **Statutes:** Canonical links to the New Jersey Revised Statutes at official and mirrored sources, with a sample of verbatim text pulled for representative titles.
- **Court rules:** Canonical links to the New Jersey court rules (rules of civil/criminal/appellate procedure, evidence, local rules, etc.).
- **Case law:** On-demand indexes — see `references/nj-case-law.md`.

## Sources

### Statutes
- **NJRSA** — <https://lis.njleg.state.nj.us/nxt/gateway.dll?f=templates&fn=default.htm&vid=Publish%3A10.1048%2FEnu>

### Court Rules
- **New Jersey Courts** — <https://www.njcourts.gov/courts/supreme>

## Architecture

This plugin follows the `*-legal-corpus/` convention. It is consumable by any cross-jurisdiction `*-consumer-debt`, `*-family-law`, or `*-pro-se` skills layer that wants the New Jersey corpus as its venue-specific reference.

## Coverage targets

- [x] Canonical statute index (links to all titles/chapters)
- [ ] Verbatim statute text (sample for the most-litigated titles; expand quarterly)
- [x] Court rules canonical link
- [ ] Verbatim court rules (sample for the rules most-cited in consumer-debt / family-law / housing matters)
- [x] Case law API index
