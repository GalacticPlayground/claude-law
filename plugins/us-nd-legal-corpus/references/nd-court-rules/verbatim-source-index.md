# ND Court Rules — Canonical Index (with verbatim where reachable)

**Source:** <https://www.ndcourts.gov/legal-resources/rules>
**Plugin:** `us-nd-legal-corpus`
**Pulled:** 2026-06-05
**Fetch status:** HTTP 200

## Verbatim source text

The source page was successfully fetched and the visible text is archived below
for reference. The actual rule PDFs (which are the authoritative source) live
on the same site; the URLs of those PDFs are usually linked from the page
content.

```
North Dakota Court System - Rules 

        How Do I

            Search Records & Pay Fines

            Self-Help

            Court Locations

            Supreme Court Opinions

            Jury Duty

            Lawyer Search

        Search North Dakota Courts

        Search Tips

            Home

Supreme Court

                Supreme Court

            Docket Search            

            Opinions            

            Watch/Listen to Court            

            View Calendar            

            Filing With the Supreme Court            

            Notices            

                Committees and Boards

            Administrative Council            

            Board of Law Examiners            

            Disciplinary Board            

            Joint Procedure            

            Judicial Conduct Commission            

            more...            

                Get Connected

            Subscribe            

            Taking the Courts to Schools            

                Publications

            Current Justices            

            Surrogate Judges            

            History of the Supreme Court            

            Appealing a Case            

            About Us            

District Courts

                District Court

            Case Search & Pay Fines            

            Jury Service            

            Court Locations            

            District Court Information            

            District Court Judges            

            District Administration            

                Court Resources

            E-Filing - resources            

            E-File Portal            

            Find an Attorney            

            Court Fees            

            Court Interpreters            

            Access to Court Records            

                Court Resources (cont.)

            Alternative Dispute Resolution Roster            

            Parenting Coordinator Roster            

            Parenting Inv/GAL Roster            

            Interest Rate on Judgments            

            Summons by Publication            

Other Courts

                Municipal Courts

            Bismarck            

            Fargo            

            Grand Forks            

            Minot            

            Williston            

            more...            

                Juvenile

            Juvenile Court            

            Contact Juvenile Court            

            Juvenile Programs and Services            

            Juvenile Treatment Court            

            Contact Juvenile Treatment Court            

                Other Courts

            Domestic Violence Court            

            Treatment Courts            

            Office of Administrative Hearings            

            Federal Courts            

            Tribal Courts            

            Veterans Treatment Court            

Legal Resources

                Court Rules

            Administrative Rules            

            Appellate Procedure            

            Civil Procedure            

            Criminal Procedure            

            Rules of Court            

            more...            

                Resources

            Notices            

            Legal Research            

            Law Library            

            North Dakota Administrative Code            

            North Dakota Century Code            

            North Dakota Constitution            

            Federal Laws and Regulations            

            U.S. Supreme Court Opinions            

                Legal Self Help Center

            Answering a Summons and Complaint            

            Divorce            

            Establishing Custody & Visitation            

            Probate an Estate            

            Small Claims            

            more...            

Court Administration

                Departments

            State Court Administration            

            Education            

            Family Law Mediation Program            

            Finance            

            Human Resources            

            Information Technology            

            Juvenile Court            

            Research and Planning            

                Publications

            Departures from Mandatory Minimums            

            Annual Report            

            Annual Report - Juvenile            

            State of the Judiciary            

                Online Resources

            Governor            

            Legislature            

            State Bar Assoc. of N.D.            

            Schedule of Meetings and Events            

                Administrative Policies

            Personnel Policy Manual            

            Chart - Salary Grade and Class Specification            

            Pay Ranges (07-25)            

            Supplement I            

            more...            

Lawyers

                Lawyers

            Attorney Search            

            Board of Law Examiners            

            E-Filing Portal            

            Attorney Subscription Management            

            Rural Attorney Recruitment Program            

            Judicial Conduct Commission            

            Disciplinary Board            

      How Do I 

                        Home
                        
                        Legal Resources
                        
                        Rules

Rules

        Search

Appellate Procedure

Civil Procedure

Criminal Procedure

Juvenile Procedure

Evidence

Rules of Court

Local Court Procedural and Administrative Rules

Administrative Rules

Administrative Orders

Admission to Practice Rules

Continuing Legal Education

Professional Conduct

Lawyer Discipline

Standards for Imposing Lawyer Sanctions

Code of Judicial Conduct

Judicial Conduct Commission

Rules on Procedural Rules, Administrative Rules and Administrative Orders

Rules on Local Court Procedural Rules and Administrative Rules

Limited Practice of Law by Law Students

    North Dakota Supreme Court

600 E Boulevard Ave
Bismarck, ND 58505-0530

    District Courts

Municipal Courts

    About Us

Contact Us

Jobs With Us

    Privacy Statement

Security Policy

Disclaimer
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

This corpus's CI workflow runs `python3 scripts/pull_nd_court_rules.py` quarterly. That script's contract is to:

1. Fetch the canonical rules index at <https://www.ndcourts.gov/legal-resources/rules>
2. Identify the rules PDFs / HTML pages linked from the index
3. Extract verbatim text via the appropriate format (PDF→text, HTML→text)
4. Write one MD file per rule family under `references/nd-court-rules/verbatim/`
5. Update the `index.md` with the latest amendment dates

