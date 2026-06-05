# Missouri — Legal Corpus Overview

**Code Name:** Missouri Revised Statutes
**Capital:** Jefferson City
**Court System:** Missouri Court System
**Highest Court:** Missouri Supreme Court
**Plugin:** `us-mo-legal-corpus`
**Pulled:** 2026-06-05

## What this corpus contains

- **Statutes:** Canonical links to the Missouri Revised Statutes at official and mirrored sources, with a sample of verbatim text pulled for representative titles.
- **Court rules:** Canonical links to the Missouri court rules (rules of civil/criminal/appellate procedure, evidence, local rules, etc.).
- **Case law:** On-demand indexes — see `references/mo-case-law.md`.

## Sources

### Statutes
- **MRS** — <https://revisor.mo.gov/main/OneChapter.aspx?chapter=1>

### Court Rules
- **Missouri Court System** — <https://www.courts.mo.gov/page.jsp?id=836>

## Architecture

This plugin follows the `*-legal-corpus/` convention. It is consumable by any cross-jurisdiction `*-consumer-debt`, `*-family-law`, or `*-pro-se` skills layer that wants the Missouri corpus as its venue-specific reference.

## Coverage targets

- [x] Canonical statute index (links to all titles/chapters)
- [ ] Verbatim statute text (sample for the most-litigated titles; expand quarterly)
- [x] Court rules canonical link
- [ ] Verbatim court rules (sample for the rules most-cited in consumer-debt / family-law / housing matters)
- [x] Case law API index
