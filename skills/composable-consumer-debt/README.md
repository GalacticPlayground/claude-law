# Cross-Jurisdiction Composable Skills

These skills sit outside individual state plugins and compose against any installed legal corpus to produce venue-specific documents.

## Available Composers

### consumer-debt-composer/
Composes: Federal Debt Law (FDCPA, FCRA) + [State] Consumer Law + Venue-Specific Rules  
Produces: Demand letters, dispute templates, pro se filings for debt collection matters

### family-law-composer/
Composes: State Family Law Corpus + Venue-Specific Court Rules  
Produces: Petitions, parenting plans, child support worksheets

## How to use

These skills auto-discover the nearest installed legal corpus and compose against its references. Add `*-legal-corpus` plugins to make corresponding material available.
