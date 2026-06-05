# FL Court Rules — Canonical Index (with verbatim where reachable)

**Source:** <https://www.flcourts.org/Supreme-Court/Procedures-Rules.shtml>
**Plugin:** `us-fl-legal-corpus`
**Pulled:** 2026-06-05
**Fetch status:** HTTP 200

## Verbatim source text

The source page was successfully fetched and the visible text is archived below
for reference. The actual rule PDFs (which are the authoritative source) live
on the same site; the URLs of those PDFs are usually linked from the page
content.

```
- Florida CourtsSkip to main contentFlorida Courts

Supported by the Office of the State Courts Administrator

SearchWe're sorry, the page you have requested cannot be found.

What went wrong?

You may have an out-of-date bookmark
You may have arrived here from a search engine which needs to update its index
The page may no longer exist
You may have mis-typed the address
How can I find the information I was seeking?

Search our site
Visit the home page
Courts Newsletter

Subscribe to receive important updates and news from Florida Courts.

Subscribe NowPrivacy Statement|Accessibility Statement|Legal Notice|(850) 922-5081500 South Duval Street, Tallahassee, FL, 32399-1925

All Content Copyright 2026 Florida Courts
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

This corpus's CI workflow runs `python3 scripts/pull_fl_court_rules.py` quarterly. That script's contract is to:

1. Fetch the canonical rules index at <https://www.flcourts.org/Supreme-Court/Procedures-Rules.shtml>
2. Identify the rules PDFs / HTML pages linked from the index
3. Extract verbatim text via the appropriate format (PDF→text, HTML→text)
4. Write one MD file per rule family under `references/fl-court-rules/verbatim/`
5. Update the `index.md` with the latest amendment dates

