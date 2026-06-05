# Illinois State Legal Corpus

Comprehensive, curated corpus of **Illinois** state law.

## Coverage
- **Illinois Compiled Statutes (ILCS)** — the state's statutory code
- State-level administrative regulations
- State precedent: Illinois Supreme Court + Court of Appeals
- All embedded county/municipal law layers (Illinois county-by-county)

## Structure

```
us-il-legal-corpus/
  references/
    il_statutes/             # Illinois Compiled Statutes (ILCS) organized by chapter
    il_court_rules/          # Statewide + county-specific court rules
  skills/                     # Subject matter + procedural + venue skills
  .claude-plugin              # Plugin manifest
  README.md
```

## How this works
This plugin provides reference corpora for legal research and document production.
All statutory/textual content is kept in `references/` as curated, sourced documents.
