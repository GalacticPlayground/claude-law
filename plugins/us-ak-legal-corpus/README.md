# Alaska State Legal Corpus

Comprehensive, curated corpus of **Alaska** state law.

## Coverage
- **Alaska Statutes (AS)** — the state's statutory code
- State-level administrative regulations
- State precedent: Alaska Supreme Court + Court of Appeals
- All embedded county/municipal law layers (Alaska county-by-county)

## Structure

```
us-ak-legal-corpus/
  references/
    ak_statutes/             # Alaska Statutes (AS) organized by chapter
    ak_court_rules/          # Statewide + county-specific court rules
  skills/                     # Subject matter + procedural + venue skills
  .claude-plugin              # Plugin manifest
  README.md
```

## How this works
This plugin provides reference corpora for legal research and document production.
All statutory/textual content is kept in `references/` as curated, sourced documents.
