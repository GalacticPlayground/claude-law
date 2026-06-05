# Minnesota State Legal Corpus

Comprehensive, curated corpus of **Minnesota** state law.

## Coverage
- **Minnesota Statutes** — the state's statutory code
- State-level administrative regulations
- State precedent: Minnesota Supreme Court + Court of Appeals
- All embedded county/municipal law layers (Minnesota county-by-county)

## Structure

```
us-mn-legal-corpus/
  references/
    mn_statutes/             # Minnesota Statutes organized by chapter
    mn_court_rules/          # Statewide + county-specific court rules
  skills/                     # Subject matter + procedural + venue skills
  .claude-plugin              # Plugin manifest
  README.md
```

## How this works
This plugin provides reference corpora for legal research and document production.
All statutory/textual content is kept in `references/` as curated, sourced documents.
