# West Virginia State Legal Corpus

Comprehensive, curated corpus of **West Virginia** state law.

## Coverage
- **West Virginia Code** — the state's statutory code
- State-level administrative regulations
- State precedent: West Virginia Supreme Court + Court of Appeals
- All embedded county/municipal law layers (West Virginia county-by-county)

## Structure

```
us-wv-legal-corpus/
  references/
    wv_statutes/             # West Virginia Code organized by chapter
    wv_court_rules/          # Statewide + county-specific court rules
  skills/                     # Subject matter + procedural + venue skills
  .claude-plugin              # Plugin manifest
  README.md
```

## How this works
This plugin provides reference corpora for legal research and document production.
All statutory/textual content is kept in `references/` as curated, sourced documents.
