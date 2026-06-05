# Connecticut State Legal Corpus

Comprehensive, curated corpus of **Connecticut** state law.

## Coverage
- **Connecticut General Statutes (CGS)** — the state's statutory code
- State-level administrative regulations
- State precedent: Connecticut Supreme Court + Court of Appeals
- All embedded county/municipal law layers (Connecticut county-by-county)

## Structure

```
us-ct-legal-corpus/
  references/
    ct_statutes/             # Connecticut General Statutes (CGS) organized by chapter
    ct_court_rules/          # Statewide + county-specific court rules
  skills/                     # Subject matter + procedural + venue skills
  .claude-plugin              # Plugin manifest
  README.md
```

## How this works
This plugin provides reference corpora for legal research and document production.
All statutory/textual content is kept in `references/` as curated, sourced documents.
