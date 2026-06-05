# Maine State Legal Corpus

Comprehensive, curated corpus of **Maine** state law.

## Coverage
- **Maine Revised Statutes (MRSA)** — the state's statutory code
- State-level administrative regulations
- State precedent: Maine Supreme Court + Court of Appeals
- All embedded county/municipal law layers (Maine county-by-county)

## Structure

```
us-me-legal-corpus/
  references/
    me_statutes/             # Maine Revised Statutes (MRSA) organized by chapter
    me_court_rules/          # Statewide + county-specific court rules
  skills/                     # Subject matter + procedural + venue skills
  .claude-plugin              # Plugin manifest
  README.md
```

## How this works
This plugin provides reference corpora for legal research and document production.
All statutory/textual content is kept in `references/` as curated, sourced documents.
