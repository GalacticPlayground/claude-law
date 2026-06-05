# South Carolina State Legal Corpus

Comprehensive, curated corpus of **South Carolina** state law.

## Coverage
- **South Carolina Code** — the state's statutory code
- State-level administrative regulations
- State precedent: South Carolina Supreme Court + Court of Appeals
- All embedded county/municipal law layers (South Carolina county-by-county)

## Structure

```
us-sc-legal-corpus/
  references/
    sc_statutes/             # South Carolina Code organized by chapter
    sc_court_rules/          # Statewide + county-specific court rules
  skills/                     # Subject matter + procedural + venue skills
  .claude-plugin              # Plugin manifest
  README.md
```

## How this works
This plugin provides reference corpora for legal research and document production.
All statutory/textual content is kept in `references/` as curated, sourced documents.
