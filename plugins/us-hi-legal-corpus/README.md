# Hawaii State Legal Corpus

Comprehensive, curated corpus of **Hawaii** state law.

## Coverage
- **Hawaii Revised Statutes (HRS)** — the state's statutory code
- State-level administrative regulations
- State precedent: Hawaii Supreme Court + Court of Appeals
- All embedded county/municipal law layers (Hawaii county-by-county)

## Structure

```
us-hi-legal-corpus/
  references/
    hi_statutes/             # Hawaii Revised Statutes (HRS) organized by chapter
    hi_court_rules/          # Statewide + county-specific court rules
  skills/                     # Subject matter + procedural + venue skills
  .claude-plugin              # Plugin manifest
  README.md
```

## How this works
This plugin provides reference corpora for legal research and document production.
All statutory/textual content is kept in `references/` as curated, sourced documents.
