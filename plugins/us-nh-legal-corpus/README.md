# New Hampshire State Legal Corpus

Comprehensive, curated corpus of **New Hampshire** state law.

## Coverage
- **New Hampshire Revised Statutes (RSA)** — the state's statutory code
- State-level administrative regulations
- State precedent: New Hampshire Supreme Court + Court of Appeals
- All embedded county/municipal law layers (New Hampshire county-by-county)

## Structure

```
us-nh-legal-corpus/
  references/
    nh_statutes/             # New Hampshire Revised Statutes (RSA) organized by chapter
    nh_court_rules/          # Statewide + county-specific court rules
  skills/                     # Subject matter + procedural + venue skills
  .claude-plugin              # Plugin manifest
  README.md
```

## How this works
This plugin provides reference corpora for legal research and document production.
All statutory/textual content is kept in `references/` as curated, sourced documents.
