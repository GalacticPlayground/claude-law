# Federal Case Law — Public Data Sources

This is an on-demand index. No verbatim case text is snapshotted; the corpus
points at free public APIs that Claude can call at runtime.

## Primary sources (free, public domain)

- **CourtListener** (Free Law Project) — `https://www.courtlistener.com/`
  - All federal circuits + district courts + bankruptcy courts
  - 13M+ cases, full text, RECAP archive
  - Free API: `https://www.courtlistener.com/api/rest/v3/`
- **RECAP** — federal court documents (PACER mirror)
- **BIA (EOIR)** — `https://www.justice.gov/eoir/bia-decisions`
  - Board of Immigration Appeals precedent decisions
- **USCIS AAO** — `https://www.uscis.gov/administrative-appeals/aao-decisions`
  - Administrative Appeals Office non-precedent decisions
- **OLC (Office of Legal Counsel)** — `https://www.justice.gov/olc/opinions`
  - Executive-branch legal opinions
- **OLR (Office of Legal Research)** — GAO reports, etc.

## State case law (per state plugin)

Each `us-{state}-legal-corpus` plugin has its own
`references/{state}-case-law.md` indexing that state's appellate courts,
supreme court, and any official reporter.
