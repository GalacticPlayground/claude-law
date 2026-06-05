# UT Court Rules — Canonical Index (with verbatim where reachable)

**Source:** <https://www.utcourts.gov/rules/>
**Plugin:** `us-ut-legal-corpus`
**Pulled:** 2026-06-05
**Fetch status:** HTTP 200

## Verbatim source text

The source page was successfully fetched and the visible text is archived below
for reference. The actual rule PDFs (which are the authoritative source) live
on the same site; the URLs of those PDFs are usually linked from the page
content.

```
Utah Court Rules  - Utah Courts

		Utah State Courts

					Website Links 
					
						Home Page

						About Us

						Self-Help

						Forms

						Legal Help

						Records

						Careers

						Media

						Contact Information

						Privacy Policy

					Search Website 
					
						Go

				You need to have JavaScript enabled to use this system.

 -->
 -->

			Utah Court Rules

	Search

	Find this exact phrase: 
	Search:
	
		All rules
		Rules of Civil Procedure
		Rules of Small Claims Procedure
		Rules of Court-Annexed Alternative Dispute Resolution
		Rules of Criminal Procedure
		Rules of Appellate Procedure
		Rules of Juvenile Procedure
		Rules of Evidence
		Rules of Business and Chancery Court Procedure
		Code of Judicial Administration
		Supreme Court Rules of Professional Practice

					This application allows you to search public case information.

 -->

	Rules

	Notices of Rule Changes

	Rule History Resources

	Rule Committees

Rules

	Rules of Civil Procedure

	Rules of Criminal Procedure

	Rules of Appellate Procedure

	Rules of Juvenile Procedure

	Rules of Small Claims Procedure

	Rules of Court-Annexed Alternative Dispute Resolution

	Rules of Evidence

	Rules of Business and Chancery Court Procedure

	Code of Judicial Administration

	Supreme Court Rules of Professional Practice

Notices of Rule Changes

All Utah attorneys receive automatic email notification of rule changes. If you are not a Utah attorney and would like to receive automatic notifications of rule changes please email Appellate Court Administrator, Nick Stiles, at nicks@utcourts.gov to be placed on the listserv. 

	Redline text of proposed amendments published for comment
 
	Redline text of approved amendments

 An RSS Feed is available for Approved Rules and Rules Published for Comment.

Rule History Resources

History of rule amendments (November 2003 - current) can be found on the right side of the published for comment and approved amendments pages under Categories. Click on the rule number to get a list references to that rule.

Older versions of the court rules are available in print at the Utah State Law Library.

Rule Committees

Click on a committee name for more information.

Supreme Court Advisory Committee on Rules of Appellate Procedure

Supreme Court Advisory Committee on Rules of Appellate Procedure

	Committee members

	Committee information

Date range

Available material

August 1997 - June 2013

Minutes

August 2013 - current

Minutes and other meeting materials

Supreme Court Advisory Committee on Rules of Civil Procedure

Supreme Court Advisory Committee on Rules of Civil Procedure

	Committee members

	Committee information

Date range

Available material

September 1990 - current

Minutes and other meeting materials

Supreme Court Advisory Committee on Rules of Criminal Procedure

Supreme Court Advisory Committee on Rules of Criminal Procedure

	Committee members

	Committee information

Date range

Available material

July 1987 - November 1994 and June 1998 - November 2001 (gaps)

Contact Jeni Wood / 801-578-3806

2001 - current

Minutes and other meeting materials

Supreme Court Advisory Committee on Rules of Evidence

Supreme Court Advisory Committee on Rules of Evidence

	Committee members

Date range

Available material

October 1991 - September 2011

Minutes and other meeting materials – contact the Utah State Law Library

2012 - current

Contact Nancy Merrill / 801-578-3820

Supreme Court Advisory Committee on Rules of Juvenile Procedure

Supreme Court Advisory Committee on Rules of Juvenile Procedure

	Committee members

Date range

Available material

September 1987 - February 1991

Contact Katie Gregory / 801-578-3929

Supreme Court Advisory Committee on Rules of Professional Conduct

Supreme Court Advisory Committee on Rules of Professional Conduct

	Committee members

	Committee information

Date range

Available material

October 1988 - current

Minutes and other meeting materials

Empty Table

			© 2017-2026 Utah Courts

			Privacy Policy | 
 
			Contact Information | 

			Website Comments

	Close ×
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

This corpus's CI workflow runs `python3 scripts/pull_ut_court_rules.py` quarterly. That script's contract is to:

1. Fetch the canonical rules index at <https://www.utcourts.gov/rules/>
2. Identify the rules PDFs / HTML pages linked from the index
3. Extract verbatim text via the appropriate format (PDF→text, HTML→text)
4. Write one MD file per rule family under `references/ut-court-rules/verbatim/`
5. Update the `index.md` with the latest amendment dates

