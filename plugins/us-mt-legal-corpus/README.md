# Montana State Legal Corpus

Comprehensive, curated corpus of **Montana** state law.

## Coverage
- **Montana Code Annotated (MCA)** — the state's statutory code
- State-level administrative regulations
- State precedent: Montana Supreme Court + Court of Appeals
- All embedded county/municipal law layers (Montana county-by-county)

## Structure

```
us-mt-legal-corpus/
  references/
    mt_statutes/             # Montana Code Annotated (MCA) organized by chapter
    mt_court_rules/          # Statewide + county-specific court rules
  skills/                     # Subject matter + procedural + venue skills
  .claude-plugin              # Plugin manifest
  README.md
```

## How this works
This plugin provides reference corpora for legal research and document production.
All statutory/textual content is kept in `references/` as curated, sourced documents.
