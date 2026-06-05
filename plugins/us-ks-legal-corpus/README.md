# Kansas — Legal Corpus Overview

**Code Name:** Kansas Statutes Annotated
**Capital:** Topeka
**Court System:** Kansas Judicial Branch
**Highest Court:** Kansas Supreme Court
**Plugin:** `us-ks-legal-corpus`
**Pulled:** 2026-06-05

## What this corpus contains

- **Statutes:** Canonical links to the Kansas Statutes Annotated at official and mirrored sources, with a sample of verbatim text pulled for representative titles.
- **Court rules:** Canonical links to the Kansas court rules (rules of civil/criminal/appellate procedure, evidence, local rules, etc.).
- **Case law:** On-demand indexes — see `references/ks-case-law.md`.

## Sources

### Statutes
- **KSA** — <https://www.kslegislature.org/li/b2025_26/statute/001_000_0000_chapter/>

### Court Rules
- **Kansas Judicial Branch** — <https://www.kscourts.org/Court-Rules>

## Architecture

This plugin follows the `*-legal-corpus/` convention. It is consumable by any cross-jurisdiction `*-consumer-debt`, `*-family-law`, or `*-pro-se` skills layer that wants the Kansas corpus as its venue-specific reference.

## Coverage targets

- [x] Canonical statute index (links to all titles/chapters)
- [ ] Verbatim statute text (sample for the most-litigated titles; expand quarterly)
- [x] Court rules canonical link
- [ ] Verbatim court rules (sample for the rules most-cited in consumer-debt / family-law / housing matters)
- [x] Case law API index
