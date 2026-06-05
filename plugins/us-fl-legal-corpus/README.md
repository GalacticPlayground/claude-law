# Florida State Legal Corpus

Comprehensive, curated corpus of **Florida** state law.

## Coverage
- **Florida Statutes** — the state's statutory code
- State-level administrative regulations
- State precedent: Florida Supreme Court + Court of Appeals
- All embedded county/municipal law layers (Florida county-by-county)

## Structure

```
us-fl-legal-corpus/
  references/
    fl_statutes/             # Florida Statutes organized by chapter
    fl_court_rules/          # Statewide + county-specific court rules
  skills/                     # Subject matter + procedural + venue skills
  .claude-plugin              # Plugin manifest
  README.md
```

## How this works
This plugin provides reference corpora for legal research and document production.
All statutory/textual content is kept in `references/` as curated, sourced documents.
