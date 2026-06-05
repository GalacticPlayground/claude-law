# Alabama State Legal Corpus

Comprehensive, curated corpus of **Alabama** state law.

## Coverage
- **Code of Alabama** — the state's statutory code
- State-level administrative regulations
- State precedent: Alabama Supreme Court + Court of Appeals
- All embedded county/municipal law layers (Alabama county-by-county)

## Structure

```
us-al-legal-corpus/
  references/
    al_statutes/             # Code of Alabama organized by chapter
    al_court_rules/          # Statewide + county-specific court rules
  skills/                     # Subject matter + procedural + venue skills
  .claude-plugin              # Plugin manifest
  README.md
```

## How this works
This plugin provides reference corpora for legal research and document production.
All statutory/textual content is kept in `references/` as curated, sourced documents.
