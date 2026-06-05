# Massachusetts State Legal Corpus

Comprehensive, curated corpus of **Massachusetts** state law.

## Coverage
- **Massachusetts General Laws (MGL)** — the state's statutory code
- State-level administrative regulations
- State precedent: Massachusetts Supreme Court + Court of Appeals
- All embedded county/municipal law layers (Massachusetts county-by-county)

## Structure

```
us-ma-legal-corpus/
  references/
    ma_statutes/             # Massachusetts General Laws (MGL) organized by chapter
    ma_court_rules/          # Statewide + county-specific court rules
  skills/                     # Subject matter + procedural + venue skills
  .claude-plugin              # Plugin manifest
  README.md
```

## How this works
This plugin provides reference corpora for legal research and document production.
All statutory/textual content is kept in `references/` as curated, sourced documents.
