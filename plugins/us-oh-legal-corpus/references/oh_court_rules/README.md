# oh_court_rules Corpus — Ohio

Verbatim Markdown conversions of official Ohio court-rule PDFs.

## Scope

This corpus covers the Ohio Rules of Civil Procedure, Evidence, Appellate Procedure, Criminal Procedure, Juvenile Procedure, Traffic Rules, Rules of Superintendence, Supreme Court practice rules, professional and judicial conduct rules, bar and judiciary governance rules, reporting rules, and Ohio Court of Claims local rules.

Each Markdown file contains the source URL, fetch date, and a layout-preserving `pdftotext` conversion of the official PDF.

The `_manifest.json` file records the pull date, source root, and puller version.

## Refresh

```sh
python3 scripts/pull_ohio_court_rules.py --output plugins/us-oh-legal-corpus/references/oh_court_rules/
```

Use `--only CivilProcedure` or another rule stem to refresh a single rule set.
