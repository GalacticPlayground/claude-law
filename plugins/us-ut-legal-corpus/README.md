# Utah State Legal Corpus

Comprehensive, curated corpus of **Utah** state law.

## Coverage
- **Utah Code** — the state's statutory code
- State-level administrative regulations
- State precedent: Utah Supreme Court + Court of Appeals
- All embedded county/municipal law layers (Utah county-by-county)

## Structure

```
us-ut-legal-corpus/
  references/
    ut_statutes/             # Utah Code organized by chapter
    ut_court_rules/          # Statewide + county-specific court rules
  skills/                     # Subject matter + procedural + venue skills
  .claude-plugin              # Plugin manifest
  README.md
```

## How this works
This plugin provides reference corpora for legal research and document production.
All statutory/textual content is kept in `references/` as curated, sourced documents.
