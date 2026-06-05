# oh_statutes Corpus — Ohio

Verbatim Markdown pulls of selected Ohio Revised Code chapters from the Ohio Legislative Service Commission HTML publisher at `codes.ohio.gov`.

## Scope

This corpus covers Ohio civil practice, consumer debt, landlord-tenant, family law, juvenile practice, municipal courts, county courts, and small claims. Each `RC-Chapter-*.md` file contains the source URL, fetch date, and verbatim converted chapter text.

The `_manifest.json` file records the pull date, source root, and puller version.

## Refresh

```sh
python3 scripts/pull_ohio_statutes.py --output plugins/us-oh-legal-corpus/references/oh_statutes/
```

Use `--only RC-Chapter-1345` or another chapter stem to refresh a single chapter.
