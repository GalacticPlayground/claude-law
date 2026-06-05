# Pennsylvania State Legal Corpus

Comprehensive, curated corpus of **Pennsylvania** state law.

## Coverage
- **Pennsylvania Consolidated Statutes** — the state's statutory code
- State-level administrative regulations
- State precedent: Pennsylvania Supreme Court + Court of Appeals
- All embedded county/municipal law layers (Pennsylvania county-by-county)

## Structure

```
us-pa-legal-corpus/
  references/
    pa_statutes/             # Pennsylvania Consolidated Statutes organized by chapter
    pa_court_rules/          # Statewide + county-specific court rules
  skills/                     # Subject matter + procedural + venue skills
  .claude-plugin              # Plugin manifest
  README.md
```

## How this works
This plugin provides reference corpora for legal research and document production.
All statutory/textual content is kept in `references/` as curated, sourced documents.
