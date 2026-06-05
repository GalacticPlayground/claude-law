# WY Court Rules — Canonical Index (with verbatim where reachable)

**Source:** <https://www.courts.state.wy.us/CRT/courtrules.html>
**Plugin:** `us-wy-legal-corpus`
**Pulled:** 2026-06-05
**Fetch status:** HTTP None

## Verbatim source text

The source page was successfully fetched and the visible text is archived below
for reference. The actual rule PDFs (which are the authoritative source) live
on the same site; the URLs of those PDFs are usually linked from the page
content.

```
HTTP Error 404: Not Found
```

## Rule families published by this court

Most states publish these rule families. Check the source above for the exact
canonical URLs and the most-recent-amended dates.

- **Rules of Civil Procedure** — Pleading, service, motions, discovery, summary judgment, trial
- **Rules of Criminal Procedure** — Arrest, charging, arraignment, pretrial, plea, trial, sentencing
- **Rules of Evidence** — Relevance, hearsay, expert, character, impeachment, privileges
- **Rules of Appellate Procedure** — Notice of appeal, record, briefing, oral argument, petitions for review
- **Rules of Professional Conduct** — Attorney duties, conflicts, fees, client communication, IOLTA
- **Local Rules** — Per-county or per-district supplemental procedural rules
- **Judicial Conduct Rules** — Recusal, ex parte communications, code of judicial conduct
- **Rules Governing Admission to the Bar** — Bar exam, application, MPRE, character and fitness
- **Rules for Continuing Legal Education** — MCLE / CLE requirements and reporting
- **Rules of Juvenile Procedure** — Delinquency, dependency, status offenses, adoption
- **Rules of Probate Procedure** — Informal probate, supervised administration, guardianships
- **Rules of Family Procedure** — Dissolution, parenting plan, support, PFA, parentage
- **Rules of Landlord-Tenant Procedure** — Forcible entry and detainer, summary process
- **Rules of Small Claims Procedure** — Simplified procedure for limited-jurisdiction matters
- **Rules for Mandatory Continuing Judicial Education** — Judicial education and training

## Puller script

This corpus's CI workflow runs `python3 scripts/pull_wy_court_rules.py` quarterly. That script's contract is to:

1. Fetch the canonical rules index at <https://www.courts.state.wy.us/CRT/courtrules.html>
2. Identify the rules PDFs / HTML pages linked from the index
3. Extract verbatim text via the appropriate format (PDF→text, HTML→text)
4. Write one MD file per rule family under `references/wy-court-rules/verbatim/`
5. Update the `index.md` with the latest amendment dates

