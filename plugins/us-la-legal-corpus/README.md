# Louisiana State Legal Corpus

Comprehensive, curated corpus of **Louisiana** state law.

## Coverage
- **Louisiana Revised Statutes (LRS)** — the state's statutory code
- State-level administrative regulations
- State precedent: Louisiana Supreme Court + Court of Appeals
- All embedded county/municipal law layers (Louisiana county-by-county)

## Structure

```
us-la-legal-corpus/
  references/
    la_statutes/             # Louisiana Revised Statutes (LRS) organized by chapter
    la_court_rules/          # Statewide + county-specific court rules
  skills/                     # Subject matter + procedural + venue skills
  .claude-plugin              # Plugin manifest
  README.md
```

## How this works
This plugin provides reference corpora for legal research and document production.
All statutory/textual content is kept in `references/` as curated, sourced documents.
