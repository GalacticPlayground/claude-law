# Rhode Island State Legal Corpus

Comprehensive, curated corpus of **Rhode Island** state law.

## Coverage
- **Rhode Island General Laws (RIGL)** — the state's statutory code
- State-level administrative regulations
- State precedent: Rhode Island Supreme Court + Court of Appeals
- All embedded county/municipal law layers (Rhode Island county-by-county)

## Structure

```
us-ri-legal-corpus/
  references/
    ri_statutes/             # Rhode Island General Laws (RIGL) organized by chapter
    ri_court_rules/          # Statewide + county-specific court rules
  skills/                     # Subject matter + procedural + venue skills
  .claude-plugin              # Plugin manifest
  README.md
```

## How this works
This plugin provides reference corpora for legal research and document production.
All statutory/textual content is kept in `references/` as curated, sourced documents.
