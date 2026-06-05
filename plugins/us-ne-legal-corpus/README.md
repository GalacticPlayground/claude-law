# Nebraska State Legal Corpus

Comprehensive, curated corpus of **Nebraska** state law.

## Coverage
- **Nebraska Revised Statute (NRS)** — the state's statutory code
- State-level administrative regulations
- State precedent: Nebraska Supreme Court + Court of Appeals
- All embedded county/municipal law layers (Nebraska county-by-county)

## Structure

```
us-ne-legal-corpus/
  references/
    ne_statutes/             # Nebraska Revised Statute (NRS) organized by chapter
    ne_court_rules/          # Statewide + county-specific court rules
  skills/                     # Subject matter + procedural + venue skills
  .claude-plugin              # Plugin manifest
  README.md
```

## How this works
This plugin provides reference corpora for legal research and document production.
All statutory/textual content is kept in `references/` as curated, sourced documents.
