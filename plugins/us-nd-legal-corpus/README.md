# North Dakota State Legal Corpus

Comprehensive, curated corpus of **North Dakota** state law.

## Coverage
- **North Dakota Century Code (NDCC)** — the state's statutory code
- State-level administrative regulations
- State precedent: North Dakota Supreme Court + Court of Appeals
- All embedded county/municipal law layers (North Dakota county-by-county)

## Structure

```
us-nd-legal-corpus/
  references/
    nd_statutes/             # North Dakota Century Code (NDCC) organized by chapter
    nd_court_rules/          # Statewide + county-specific court rules
  skills/                     # Subject matter + procedural + venue skills
  .claude-plugin              # Plugin manifest
  README.md
```

## How this works
This plugin provides reference corpora for legal research and document production.
All statutory/textual content is kept in `references/` as curated, sourced documents.
