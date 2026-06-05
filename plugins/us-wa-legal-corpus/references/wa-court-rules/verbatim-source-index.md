# WA Court Rules — Canonical Index (with verbatim where reachable)

**Source:** <https://www.courts.wa.gov/court_rules/>
**Plugin:** `us-wa-legal-corpus`
**Pulled:** 2026-06-05
**Fetch status:** HTTP 200

## Verbatim source text

The source page was successfully fetched and the visible text is archived below
for reference. The actual rule PDFs (which are the authoritative source) live
on the same site; the URLs of those PDFs are usually linked from the page
content.

```
Washington State Courts  - Court Rules 

	 -->

Skip to main content

                  Washington State Court Rules

                  Courts Home

                  Court Rules

                    State Court Rules

                      Rules for Appellate Court Administration

                      Additional Matter

                      Rules on Appeal

                      Rules for Courts of Limited Jurisdiction

                      Rules of General Application

                      Rules for Superior Court

                      Rule-Related Court Orders

                      Proposed Rules Published for Comment

                      Disposition of Rules Formerly Published for Comment

                      GR 9 - Supreme Court Rulemaking and Schedule for Review

                      Supreme Court Rules Committee

                    Local Court Rules

                    Many local courts maintain their court rules on their own website.  While links are provided to these local sites, the Washington State Courts website does not have the responsibility for updating these local court sites and therefore, cannot verify that the links, or published versions, are current.  Per GR 7(d), the clerk of court maintains a complete set of local court rules.  Local court rules are published on this webpage for convenience but are not the official record of the local court.

                      Superior Court Rules

                      District Court Rules

                      Municipal Court Rules

          Please send questions or concerns about formatting or technical errors that appear on this web page to rulescomments@courts.wa.gov.

              Disclaimer

              Neither the State of Washington nor any of its agencies and officials (1) makes any representations or warranties as to the accuracy or completeness of this Internet site containing the Washington rules of court or any local court rules and (2) shall be held liable for any loss or damage whatsoever resulting from any use made of the Washington rules of court or local court rules.

		N1

		External Link Warning

			You are about to be redirected to another link that is outside of the Washington Courts website.

		Close
		Continue
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

This corpus's CI workflow runs `python3 scripts/pull_wa_court_rules.py` quarterly. That script's contract is to:

1. Fetch the canonical rules index at <https://www.courts.wa.gov/court_rules/>
2. Identify the rules PDFs / HTML pages linked from the index
3. Extract verbatim text via the appropriate format (PDF→text, HTML→text)
4. Write one MD file per rule family under `references/wa-court-rules/verbatim/`
5. Update the `index.md` with the latest amendment dates

