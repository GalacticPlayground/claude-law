# OR Court Rules — Canonical Index (with verbatim where reachable)

**Source:** <https://www.courts.oregon.gov/programs/utcr/Pages/index.aspx>
**Plugin:** `us-or-legal-corpus`
**Pulled:** 2026-06-05
**Fetch status:** HTTP 200

## Verbatim source text

The source page was successfully fetched and the visible text is archived below
for reference. The actual rule PDFs (which are the authoritative source) live
on the same site; the URLs of those PDFs are usually linked from the page
content.

```
Oregon Judicial Department : 404 Page Not Found : State of Oregon

                Skip to main content

                    An official website of the State of Oregon
                         Learn
                        How you know »
                        (how to identify a Oregon.gov website)
                    
                    An official website of the State of Oregon »

                            Translate this site into other Languages

                    Toggle Main Menu

		Main Navigation
	
		How Do I? 
			Become an Interpreter
File a Case
Find a Case or Court Record
Find a Court
Find a Court Fee
Find a Court Date
Find Court Rules
Find Divorce Information
Find Information About a Remote Hearing
Find Juror Information
Get a Restraining Order
Make a Payment
Request ADA Accommodation
Request an Interpreter (Opens in new window)
Sign-up For Text Message Hearing Notifications
Apply To Become a Pro Tem and/or Reference Judge

Online Services 
			Online Services Home
Appellate eFile
Live Stream Proceedings
OJCIN Online
OJD Courts ePay
OJD eFile
OJD iForms (Interactive Forms)
OJD Records and Calendar Search
Online Legal Service Posting
Remote Hearings

Forms/Rules/Fees 
			Forms Center
Rules Center
Court Fees

Self-Help 
			Self-Help Center
Divorce, Separation, Annulment
Protective (Restraining) Orders
Family Law
Free Help for Family Law Cases

Opinions & Law Library 
			Supreme Court Opinions
Court of Appeals Opinions
Tax Court Decisions
Law Library (Opens in new window)
Other Publications

Programs & Committees 
			Programs & Committees Home
Alternative Dispute Resolution
Appellate Court Records
Behavioral Health
Certified Shorthand Reporters
Citizen Review Board
Commission on Judicial Fitness and Disability
Court Language Access Services
Current & Prospective Interpreters
Family Law
Inclusion & Fairness
Jury Task Force
Juvenile Court Program
Pretrial Programs
Remote Child Support Court
Treatment Courts
Uniform Trial Court Rules & Committee

            Search this site

                Submit

                close

                                        Back to Home

                                        Oregon Judicial Department

                            You are here:

	Oregon Judicial Department
404 Page Not Found

                             tag, as divs are not allowed in 's -->

                                404 Page Not Found

                                 Site Navigation

Whoops! This page cannot be found. 

Possible causes for this error:

The page has been moved, deleted or never existed.

The link that brought you here was incorrect. Please let us know more information via our Website Feedback form.

If you typed in the page address, you may have made an error.

Please Visit Our Main Website or Site Map to find what you are looking for

	Footer

			Site Information

Job Opportunities

Judge & Employee Sign In

FAQs

Policies

Privacy

Site Map

			Accessibility and Language Access

Language Access

Request an Interpreter

한국어 (Korean)

Pусский (Russian)

Español (Spanish)

繁體中文 (Traditional Chinese)

Việt (Vietnamese)

Contact Language Access Services

Accessibility

Website Accessibility

ADA

			Administration & Contact Us

Administration

About Us

Court Hours & Holidays

Office of the State Court Administrator

News & Media Resources

Public Records Requests

Reports, Stats & Performance Measures

Contact

For questions about your case, jury duty, payments, or other business at a specific court:

Contact the Courts

For questions about Oregon’s state court system:

Office of the State Court Administrator

Submit Website Feedback

			About Oregon

                             Back to Top

                            ×
                        
                        How to recognize an official Oregon website

                                .gov
                            
                            Official websites use .gov

                            A .gov website belongs to an official government organization in the United States.

                            Secure .gov websites use HTTPS

                            A lock icon ( ) or https:// means you’ve safely connected to the .gov website.

                        Only share sensitive information on official, secure websites.

                        Close

        Hidden Submit

        Your browser is out-of-date! It has known security flaws and may not display all features of this and other websites. Learn how

        ×
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

This corpus's CI workflow runs `python3 scripts/pull_or_court_rules.py` quarterly. That script's contract is to:

1. Fetch the canonical rules index at <https://www.courts.oregon.gov/programs/utcr/Pages/index.aspx>
2. Identify the rules PDFs / HTML pages linked from the index
3. Extract verbatim text via the appropriate format (PDF→text, HTML→text)
4. Write one MD file per rule family under `references/or-court-rules/verbatim/`
5. Update the `index.md` with the latest amendment dates

