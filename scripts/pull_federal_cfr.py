#!/usr/bin/env python3
"""Pull verbatim CFR text for all 50 titles from the free eCFR API.

Output: plugins/us-federal-legal-corpus/references/cfr/verbatim/
One MD file per title, named cfr-title-NN.md

eCFR API (no key required):
  Index:  https://www.ecfr.gov/api/versioner/v1/titles.json
  Full:   https://www.ecfr.gov/api/versioner/v1/full/{date}/title-{N}.xml
"""
import json
import re
import sys
import urllib.request
from pathlib import Path
from html import unescape

ROOT = Path("/Users/jgarland/claude-law")
TODAY = "2026-06-05"
UA = "claude-law/1.0 federal-cfr-puller"

def fetch(url, timeout=60):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.status, r.read()

def xml_to_markdown(xml_bytes):
    """Convert eCFR XML to readable Markdown."""
    text = xml_bytes.decode('utf-8', errors='ignore')
    # Strip XML tags but keep HEAD/P/AUTH content visible
    text = re.sub(r'<\?xml[^?]*\?>', '', text)
    # Convert paragraph breaks
    text = re.sub(r'<P>', '\n\n', text)
    text = re.sub(r'</P>', '', text)
    # Convert headings
    def heading_repl(m):
        level = int(m.group(1))
        content = m.group(2).strip()
        return f"\n{'#' * level} {content}\n"
    # DIV8 = section, DIV5 = part, DIV3 = chapter, etc.
    text = re.sub(r'<DIV(\d+)[^>]*>(.*?)</DIV\1>', heading_repl, text, flags=re.S)
    # Strip remaining tags
    text = re.sub(r'<[^>]+>', ' ', text)
    text = unescape(text)
    text = re.sub(r'\n\s*\n\s*\n+', '\n\n', text)
    text = re.sub(r'[ \t]+', ' ', text)
    return text.strip()

def main():
    # Get titles index
    status, idx = fetch("https://www.ecfr.gov/api/versioner/v1/titles.json")
    if status != 200:
        print(f"Failed to fetch titles index: {status}", file=sys.stderr)
        return 1
    titles = json.loads(idx)['titles']

    out_dir = ROOT / "plugins/us-federal-legal-corpus/references/cfr/verbatim"
    out_dir.mkdir(parents=True, exist_ok=True)

    # Use a known recent date for full-content snapshot
    pull_date = "2026-06-03"

    saved = []
    failed = []
    for t in titles:
        n = t['number']
        if t.get('reserved'):
            continue
        name = t['name']
        url = f"https://www.ecfr.gov/api/versioner/v1/full/{pull_date}/title-{n}.xml"
        try:
            status, body = fetch(url, timeout=120)
            if status != 200:
                failed.append((n, name, f"HTTP {status}"))
                continue
            text = xml_to_markdown(body)
            if len(text) < 100:
                failed.append((n, name, f"tiny ({len(text)} chars)"))
                continue
            md = f"""# CFR Title {n} — {name}

**Source:** <{url}>
**Plugin:** `us-federal-legal-corpus`
**Pulled:** {TODAY}
**eCFR as of:** {t.get('up_to_date_as_of', pull_date)}
**Latest amendment:** {t.get('latest_amended_on', 'unknown')}

---

{text[:200000]}
"""
            fname = f"cfr-title-{n:02d}.md"
            (out_dir / fname).write_text(md, encoding='utf-8')
            saved.append((n, name, len(text)))
            print(f"  [ok]   Title {n:2d} {name:50s} {len(text):>9,} chars")
        except Exception as e:
            failed.append((n, name, str(e)[:100]))
            print(f"  [FAIL] Title {n:2d} {name:50s} {str(e)[:100]}")

    print(f"\nSaved {len(saved)} titles, {len(failed)} failed")
    if failed:
        print("Failed:")
        for n, name, err in failed:
            print(f"  Title {n}: {name} — {err}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
