# Wisconsin State Legal Corpus

Comprehensive, curated corpus of **Wisconsin** state law.

## Coverage
- **Wisconsin Statutes** — the state's statutory code
- State-level administrative regulations
- State precedent: Wisconsin Supreme Court + Court of Appeals
- All embedded county/municipal law layers (Wisconsin county-by-county)

## Structure

```
us-wi-legal-corpus/
  references/
    wi_statutes/             # Wisconsin Statutes organized by chapter
    wi_court_rules/          # Statewide + county-specific court rules
  skills/                     # Subject matter + procedural + venue skills
  .claude-plugin              # Plugin manifest
  README.md
```

## How this works
This plugin provides reference corpora for legal research and document production.
All statutory/textual content is kept in `references/` as curated, sourced documents.
