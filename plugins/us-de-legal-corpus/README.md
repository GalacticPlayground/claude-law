# Delaware State Legal Corpus

Comprehensive, curated corpus of **Delaware** state law.

## Coverage
- **Delaware Code** — the state's statutory code
- State-level administrative regulations
- State precedent: Delaware Supreme Court + Court of Appeals
- All embedded county/municipal law layers (Delaware county-by-county)

## Structure

```
us-de-legal-corpus/
  references/
    de_statutes/             # Delaware Code organized by chapter
    de_court_rules/          # Statewide + county-specific court rules
  skills/                     # Subject matter + procedural + venue skills
  .claude-plugin              # Plugin manifest
  README.md
```

## How this works
This plugin provides reference corpora for legal research and document production.
All statutory/textual content is kept in `references/` as curated, sourced documents.
