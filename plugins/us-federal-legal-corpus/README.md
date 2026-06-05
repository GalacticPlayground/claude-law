# US Federal Legal Corpus — Venue Scope: Nation-Wide

## Overview

This is the foundational federal legal corpus for the entire United States. It provides the constitutional and statutory framework that applies nationwide, serving as the "source of truth" layer for federal law across all state-level plugins.

### What's Included
| Category | Corpus Content | Coverage |
|----------|---------------|----------|
| **US Constitution** | Article I-VII + Amendments I-XXVII | Complete constitutional framework |
| **United States Code (USC)** | Titles 1-50+ by subject matter | Full federal statute code |
| **Code of Federal Regulations (CFR)** | Titles 1-50+ by agency/subject | Executive branch regulations |
| **State-Federal Interface** | Supremacy Clause framework + preemption analysis | When federal vs. state law controls |

## Plugin Configuration
```json
{
  "name": "us-federal-legal-corpus",
  "venue_scope": "nation-wide",
  "dependencies": [],
  "composes_with": ["us-*-legal-corpus/*"]
}
```

## Key USC Titles (Federal Statute Corpus)
| Title | Subject Matter | Practice Relevance |
|-------|---------------|-------------------|
| USC 1-5 | General Provisions/Constitution | Framework for all federal law |
| USC 12 | Banks & Finance | Banking regulation, FDIC, Fed oversight |
| USC 15 | Commerce & Trade | FTC authority, consumer protection, antitrust |
| **USC 18** | **Crimes & Criminal Procedure** | Federal criminal code, federal enforcement |
| USC 26 | Internal Revenue Code (IRC) | Tax law framework |
| **USC 28** | **Judiciary & Judicial Procedure** | Federal court jurisdiction, FRCP/FRCrP |
| USCS 9 | Shipping (Maritime) | Jones Act, maritime liability limits |
| USC 1.47 | Communications + FCC/FCA framework | Wireless/internet neutrality authority |
| **USC 29** | **Labor/Employment** | NLRB, OSHA, FLSA, union/collective bargaining rights |
| **USC 31** | **Money & Treasury (Federal Debt)** | Federal debt collection via Treasury/CFA framework |
| **USCS 42** | **Public Health/Welfare + Civil Rights (§1981-§1988)** | ADA, civil rights statutes, Medicare/Medicaid |

## CFR Cross-referencing
Each USC Title maps to corresponding CFR Titles (executive agency implementing regulations). For example:
- USC Title 26 → CFR Title 26 (Treasury/IRS)  
- USC Title 18 → CFR Title 28 (Judiciary/FRCP)

**Reference index:** Complete table of USC-to-CFR mappings available in `/usc_titles/` and `/cfr_regulations/`.
