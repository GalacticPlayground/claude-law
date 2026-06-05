# North Carolina State Legal Corpus

Comprehensive, curated corpus of **North Carolina** state law.

## Coverage
- **North Carolina General Statutes (NCGS)** — the state's statutory code
- State-level administrative regulations
- State precedent: North Carolina Supreme Court + Court of Appeals
- All embedded county/municipal law layers (North Carolina county-by-county)

## Structure

```
us-nc-legal-corpus/
  references/
    nc_statutes/             # North Carolina General Statutes (NCGS) organized by chapter
    nc_court_rules/          # Statewide + county-specific court rules
  skills/                     # Subject matter + procedural + venue skills
  .claude-plugin              # Plugin manifest
  README.md
```

## How this works
This plugin provides reference corpora for legal research and document production.
All statutory/textual content is kept in `references/` as curated, sourced documents.
