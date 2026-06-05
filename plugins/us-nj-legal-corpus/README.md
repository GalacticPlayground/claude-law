# New Jersey State Legal Corpus

Comprehensive, curated corpus of **New Jersey** state law.

## Coverage
- **New Jersey Statutes (NJS)** — the state's statutory code
- State-level administrative regulations
- State precedent: New Jersey Supreme Court + Court of Appeals
- All embedded county/municipal law layers (New Jersey county-by-county)

## Structure

```
us-nj-legal-corpus/
  references/
    nj_statutes/             # New Jersey Statutes (NJS) organized by chapter
    nj_court_rules/          # Statewide + county-specific court rules
  skills/                     # Subject matter + procedural + venue skills
  .claude-plugin              # Plugin manifest
  README.md
```

## How this works
This plugin provides reference corpora for legal research and document production.
All statutory/textual content is kept in `references/` as curated, sourced documents.
