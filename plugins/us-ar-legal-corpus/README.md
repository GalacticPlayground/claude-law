# Arkansas State Legal Corpus

Comprehensive, curated corpus of **Arkansas** state law.

## Coverage
- **Arkansas Code** — the state's statutory code
- State-level administrative regulations
- State precedent: Arkansas Supreme Court + Court of Appeals
- All embedded county/municipal law layers (Arkansas county-by-county)

## Structure

```
us-ar-legal-corpus/
  references/
    ar_statutes/             # Arkansas Code organized by chapter
    ar_court_rules/          # Statewide + county-specific court rules
  skills/                     # Subject matter + procedural + venue skills
  .claude-plugin              # Plugin manifest
  README.md
```

## How this works
This plugin provides reference corpora for legal research and document production.
All statutory/textual content is kept in `references/` as curated, sourced documents.
