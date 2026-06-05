# Texas State Legal Corpus

Comprehensive, curated corpus of **Texas** state law.

## Coverage
- **Texas Statutes (Tex.)** — the state's statutory code
- State-level administrative regulations
- State precedent: Texas Supreme Court + Court of Appeals
- All embedded county/municipal law layers (Texas county-by-county)

## Structure

```
us-tx-legal-corpus/
  references/
    tx_statutes/             # Texas Statutes (Tex.) organized by chapter
    tx_court_rules/          # Statewide + county-specific court rules
  skills/                     # Subject matter + procedural + venue skills
  .claude-plugin              # Plugin manifest
  README.md
```

## How this works
This plugin provides reference corpora for legal research and document production.
All statutory/textual content is kept in `references/` as curated, sourced documents.
