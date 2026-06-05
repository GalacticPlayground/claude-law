# Nevada State Legal Corpus

Comprehensive, curated corpus of **Nevada** state law.

## Coverage
- **Nevada Revised Statutes (NRS)** — the state's statutory code
- State-level administrative regulations
- State precedent: Nevada Supreme Court + Court of Appeals
- All embedded county/municipal law layers (Nevada county-by-county)

## Structure

```
us-nv-legal-corpus/
  references/
    nv_statutes/             # Nevada Revised Statutes (NRS) organized by chapter
    nv_court_rules/          # Statewide + county-specific court rules
  skills/                     # Subject matter + procedural + venue skills
  .claude-plugin              # Plugin manifest
  README.md
```

## How this works
This plugin provides reference corpora for legal research and document production.
All statutory/textual content is kept in `references/` as curated, sourced documents.
