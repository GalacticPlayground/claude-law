# Maryland State Legal Corpus

Comprehensive, curated corpus of **Maryland** state law.

## Coverage
- **Maryland Code** — the state's statutory code
- State-level administrative regulations
- State precedent: Maryland Supreme Court + Court of Appeals
- All embedded county/municipal law layers (Maryland county-by-county)

## Structure

```
us-md-legal-corpus/
  references/
    md_statutes/             # Maryland Code organized by chapter
    md_court_rules/          # Statewide + county-specific court rules
  skills/                     # Subject matter + procedural + venue skills
  .claude-plugin              # Plugin manifest
  README.md
```

## How this works
This plugin provides reference corpora for legal research and document production.
All statutory/textual content is kept in `references/` as curated, sourced documents.
