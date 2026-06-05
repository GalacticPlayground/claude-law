# Nebraska — Legal Corpus Overview

**Code Name:** Nebraska Revised Statutes
**Capital:** Lincoln
**Court System:** Nebraska Judicial Branch
**Highest Court:** Nebraska Supreme Court
**Plugin:** `us-ne-legal-corpus`
**Pulled:** 2026-06-05

## What this corpus contains

- **Statutes:** Canonical links to the Nebraska Revised Statutes at official and mirrored sources, with a sample of verbatim text pulled for representative titles.
- **Court rules:** Canonical links to the Nebraska court rules (rules of civil/criminal/appellate procedure, evidence, local rules, etc.).
- **Case law:** On-demand indexes — see `references/ne-case-law.md`.

## Sources

### Statutes
- **NRS** — <https://nebraskalegislature.gov/laws/browse-chapters.php?chapter=1>

### Court Rules
- **Nebraska Judicial Branch** — <https://supremecourt.nebraska.gov/court-rules>

## Architecture

This plugin follows the `*-legal-corpus/` convention. It is consumable by any cross-jurisdiction `*-consumer-debt`, `*-family-law`, or `*-pro-se` skills layer that wants the Nebraska corpus as its venue-specific reference.

## Coverage targets

- [x] Canonical statute index (links to all titles/chapters)
- [ ] Verbatim statute text (sample for the most-litigated titles; expand quarterly)
- [x] Court rules canonical link
- [ ] Verbatim court rules (sample for the rules most-cited in consumer-debt / family-law / housing matters)
- [x] Case law API index
