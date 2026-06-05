# us-federal-immigration-corpus

Shared, venue-independent plugin for **U.S. immigration law** — the federal counterpart to `us-federal-debt-corpus`, built for immigration practice.

> **NOT LEGAL ADVICE.** Generated content is a drafting/research aid, not legal advice, and creates no attorney-client relationship. Immigration consequences are severe and often irreversible — verify against current law and consult a licensed attorney or EOIR-accredited representative before filing. Beware notario fraud.

## What it covers

Snapshots the canonical **rules** verbatim:

- **INA** — the Immigration and Nationality Act, 8 U.S.C. Chapter 12, one file per subchapter, with an INA-section ↔ 8 U.S.C.-section crosswalk.
- **Regulations** — curated **8 CFR** (DHS/USCIS/CBP/ICE chapter I + the DOJ/EOIR chapter V for the immigration courts and the Board of Immigration Appeals) and the State-Department **22 CFR** visa/passport/exchange parts.
- **Foreign Affairs Manual (FAM)** — verbatim 9 FAM 100/302/402/502/504 + 8 FAM 300 + 7 FAM 000/1400.
- **EOIR court rules** — the binding 8 CFR Part 1003/1240/1208 regs (in `cfr/`) plus pointer stubs for the Immigration Court Practice Manual and the BIA Practice Manual.

**Case law is indexed for on-demand lookup, not snapshotted** (it is too large/fast-moving to mirror): the federal **circuit courts** (petitions for review under INA § 242 / 8 U.S.C. § 1252, via CourtListener), the **Board of Immigration Appeals** (I&N Dec., via the EOIR Virtual Law Library), and the USCIS **Administrative Appeals Office (AAO)**.

**As of v0.3.0** it also ships an **11-skill, venue-independent, document-producing self-help layer** (matter-neutral, documents-not-advice, with prominent get-a-lawyer / notario-fraud warnings): `immigration-pro-se`, `eoir-immigration-courts`, `immigration-deadlines`, `immigration-fact-check`, `eoir-removal-defense`, `eoir-motions-to-reopen-reconsider`, `bia-appeals`, `uscis-benefit-requests`, `immigration-foia`, `circuit-petition-for-review`, `consular-visa-refusal`.

## Reference corpora

Each lives under `references/` with its own README (scope, pull mechanics, access posture):

- `ina/` — INA / 8 U.S.C. Chapter 12
- `cfr/` — curated 8 CFR and 22 CFR immigration regulations
- `fam/` — selected Foreign Affairs Manual immigration and nationality material
- `eoir/` — EOIR Immigration Court and BIA practice manual pointers

The migrated corpus also retains the legacy reference directory names (`immigration-statutes/`, `immigration-regulations/`, `foreign-affairs-manual/`, `court-rules/`) for compatibility with existing skills and prompts. `legal-data-apis.md` indexes on-demand case-law sources, and `online-sources.md` lists primary online immigration sources.

## Refresh

Use the configured HTTPS proxy for all network access:

```bash
HTTPS_PROXY=http://192.168.8.21:9091 python3 scripts/pull_ina.py --out plugins/us-federal-immigration-corpus/references/ina/
HTTPS_PROXY=http://192.168.8.21:9091 python3 scripts/pull_immigration_cfr.py --out plugins/us-federal-immigration-corpus/references/cfr/
HTTPS_PROXY=http://192.168.8.21:9091 python3 scripts/pull_fam.py --out plugins/us-federal-immigration-corpus/references/fam/
HTTPS_PROXY=http://192.168.8.21:9091 python3 scripts/pull_eoir_manuals.py --out plugins/us-federal-immigration-corpus/references/eoir/
```

`pull_fam.py` AIA-chases fam.state.gov's omitted TLS intermediate, then crawls its JSON TOC API. In a no-network sandbox, FAM and EOIR pullers may write stubs; refresh in a network-enabled environment before treating those outputs as updated source snapshots.

---
Part of the [claude-legal](../../README.md) marketplace. Skills are indexed in [CLAUDE.md](../../CLAUDE.md).
