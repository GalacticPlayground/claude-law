# Legal Corpus Plugin Migration

This refactor renames the existing court-docs and federal-law plugins to the
new legal-corpus naming pattern. Skill, reference, script, eval, and README
content is preserved in the renamed plugin directories.

## Rename Mapping

| Previous plugin | New plugin |
| --- | --- |
| `az-court-docs` | `us-az-legal-corpus` |
| `ca-court-docs` | `us-ca-legal-corpus` |
| `co-court-docs` | `us-co-legal-corpus` |
| `in-court-docs` | `us-in-legal-corpus` |
| `mi-court-docs` | `us-mi-legal-corpus` |
| `ny-court-docs` | `us-ny-legal-corpus` |
| `oh-court-docs` | `us-oh-legal-corpus` |
| `or-court-docs` | `us-or-legal-corpus` |
| `tn-court-docs` | `us-tn-legal-corpus` |
| `wa-court-docs` | `us-wa-legal-corpus` |
| `claude-legal-federal-laws` | `us-federal-debt-corpus` |
| `claude-legal-immigration-laws` | `us-federal-immigration-corpus` |

State corpus plugins now depend on `us-federal-debt-corpus`, and their
federal reference symlinks have been retargeted to that renamed plugin.
