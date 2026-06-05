# Idaho State Legal Corpus

Comprehensive, curated corpus of **Idaho** state law.

## Coverage
- **Idaho Statutes** — the state's statutory code
- State-level administrative regulations
- State precedent: Idaho Supreme Court + Court of Appeals
- All embedded county/municipal law layers (Idaho county-by-county)

## Structure

```
us-id-legal-corpus/
  references/
    id_statutes/             # Idaho Statutes organized by chapter
    id_court_rules/          # Statewide + county-specific court rules
  skills/                     # Subject matter + procedural + venue skills
  .claude-plugin              # Plugin manifest
  README.md
```

## How this works
This plugin provides reference corpora for legal research and document production.
All statutory/textual content is kept in `references/` as curated, sourced documents.
