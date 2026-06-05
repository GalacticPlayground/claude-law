# Kentucky Revised Statutes — Comprehensive Chapter Index

## Overview

The **Kentucky Revised Statutes** is the codification of all permanent general and local laws enacted by the state legislature, organized by title/chapter/subchapter. References use the convention **KRS § X.X** for citations.

## Property/Family Law Classification: equitable distribution

## Key Practice Areas — Chapter Index

### Civil Practice & Procedure
- **Trial court rules** — Rules of Civil Procedure / Rules of Court
- **Evidence code** — admissibility rules per state practice
- **Appellate procedure** — rules governing appeals in state appellate courts
- **Statutes of limitations** — comparative fault + civil action time limits
- **Tort reform** — any state-specific damage caps or modified joint and several liability

### Family Law
- **Dissolution/divorce** — state-specific grounds (no-fault + fault-based where applicable)
- **Custody/parenting plans** — best interest of child standards + parenting time frameworks
- **Child support** — state guidelines worksheet + deviation standards
- **Spousal support/maintenance** — factors, durational limits
- **Adoption** — termination of parental rights + adoption decree procedures
- **Paternity** — parentage establishment + UPA adoption where applicable

### Property Law
- **Real property** — recording acts, adverse possession, easements
- **Probate** — intestate succession + will execution
- **Trusts** — UTC adoption status + trust code framework
- **Family-specific property**: equitable distribution

### Consumer Protection
- **UDAP/Deceptive trade practices** — state-level framework analogous to FTC §5
- **Statutory damages** — treble/punitive damages where authorized
- **Lemon law** — new + used car protections
- **Credit reporting** — any state enhancements to federal FCRA

### Landlord-Tenant
- **Residential tenancies** — state-specific rent control / just-cause eviction
- **Eviction procedures** — summary process standards
- **Security deposits** — cap + return timeline
- **Warranty of habitability** — implied warranty + enforcement

### Employment
- **Minimum wage** — state-level floor (must be ≥ federal $7.25)
- **Discrimination** — state-level protected classes beyond federal Title VII
- **Wage payment** — final paycheck timing, paid sick leave
- **Workers' comp** — exclusive remedy framework

### Tax
- **Income tax** — applies where state has personal income tax
- **Sales/use tax** — state + local rate structure
- **Property tax** — assessment + appeal framework

## Pull Strategy
- Use HTTPS_PROXY=http://192.168.8.21:9091 for all upstream fetches
- Pull verbatim from official state legislature website where available
- Cache locally at /tmp/claude-legal-cache/
- Quarterly refresh via .github/workflows/refresh-references.yml
