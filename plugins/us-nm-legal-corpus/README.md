# New Mexico State Legal Corpus

Comprehensive, curated corpus of **New Mexico** state law.

## Coverage
- **New Mexico Statutes** — the state's statutory code
- State-level administrative regulations
- State precedent: New Mexico Supreme Court + Court of Appeals
- All embedded county/municipal law layers (New Mexico county-by-county)

## Structure

```
us-nm-legal-corpus/
  references/
    nm_statutes/             # New Mexico Statutes organized by chapter
    nm_court_rules/          # Statewide + county-specific court rules
  skills/                     # Subject matter + procedural + venue skills
  .claude-plugin              # Plugin manifest
  README.md
```

## How this works
This plugin provides reference corpora for legal research and document production.
All statutory/textual content is kept in `references/` as curated, sourced documents.
