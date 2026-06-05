# Washington State Constitution

Source: Washington State Legislature, <https://app.leg.wa.gov/Constitution/>

Combined full-text source: <https://app.leg.wa.gov/documents/laws/Constitution/State%20Constitution%20Articles%20and%20Amendments%20Combined/WA%20CONSTITUTION.htm>

Status: source record created from the official Legislature endpoint. The local shell sandbox could not resolve `app.leg.wa.gov`, so the combined HTML could not be downloaded directly into this workspace during corpus creation. Use the combined full-text source above as the canonical refresh target.

## Source Table of Contents

- Preamble
- Article I - Declaration of Rights
- Article II - Legislative Department
- Article III - The Executive
- Article IV - The Judiciary
- Article V - Impeachment
- Article VI - Elections and Elective Rights
- Article VII - Revenue and Taxation
- Article VIII - State, County, and Municipal Indebtedness
- Article IX - Education
- Article X - Militia
- Article XI - County, City, and Township Organization
- Article XII - Corporations Other Than Municipal
- Article XIII - State Institutions
- Article XIV - Seat of Government
- Article XV - Harbors and Tide Waters
- Article XVI - School and Granted Lands
- Article XVII - Tide Lands
- Article XVIII - State Seal
- Article XIX - Exemptions
- Article XX - Public Health and Vital Statistics
- Article XXI - Water and Water Rights
- Article XXII - Legislative Apportionment
- Article XXIII - Amendments
- Article XXIV - Boundaries
- Article XXV - Jurisdiction
- Article XXVI - Compact With the United States
- Article XXVII - Schedule
- Article XXVIII - Compensation of State Officers
- Article XXIX - Investments of Public Pension and Retirement Funds
- Article XXX - Compensation of Public Officers
- Article XXXI - Nuclear Energy and Radiation
- Article XXXII - Jurisdiction Over Indian Lands

## Refresh Command

When network access is available, refresh this file from the official combined HTML:

```sh
curl -L 'https://app.leg.wa.gov/documents/laws/Constitution/State%20Constitution%20Articles%20and%20Amendments%20Combined/WA%20CONSTITUTION.htm' \
  | pandoc -f html -t gfm \
  > plugins/us-wa-legal-corpus/references/wa_constitution/full_text.md
```
