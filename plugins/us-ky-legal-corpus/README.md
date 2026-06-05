# Kentucky State Legal Corpus

Comprehensive, curated corpus of **Kentucky** state law.

## Coverage
- **Kentucky Revised Statutes (KRS)** — the state's statutory code
- State-level administrative regulations
- State precedent: Kentucky Supreme Court + Court of Appeals
- All embedded county/municipal law layers (Kentucky county-by-county)

## Structure

```
us-ky-legal-corpus/
  references/
    ky_statutes/             # Kentucky Revised Statutes (KRS) organized by chapter
    ky_court_rules/          # Statewide + county-specific court rules
  skills/                     # Subject matter + procedural + venue skills
  .claude-plugin              # Plugin manifest
  README.md
```

## How this works
This plugin provides reference corpora for legal research and document production.
All statutory/textual content is kept in `references/` as curated, sourced documents.
