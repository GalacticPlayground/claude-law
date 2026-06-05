#!/usr/bin/env python3
"""Pull verbatim state codes for all 50 US states.

This script is the canonical quarterly puller for the corpus. It
uses canonical state legislature URLs (and Justia/Cornell LII
mirrors where the state site is Cloudflare-gated or has TLS issues
with the proxy).

For each state it writes one MD file per title/chapter to
  plugins/us-{state}-legal-corpus/references/{state}-statutes/verbatim/

Usage:
    python3 scripts/pull_state_codes.py --state ut
    python3 scripts/pull_state_codes.py --all
    python3 scripts/pull_state_codes.py --state ut --max-titles 50

Proxy: Uses HTTPS_PROXY env var. Set it before running if your
network can't reach state legislature sites directly.
"""
import argparse
import os
import re
import sys
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TODAY = "2026-06-05"
UA = "claude-law/1.0 (+https://github.com/GalacticPlayground/claude-law) state-codes-puller"

def fetch(url, timeout=15, use_cc=False):
    """Fetch URL via urllib or curl_cffi. Returns (status, body) or (None, error)."""
    if use_cc:
        try:
            from curl_cffi import requests as cc
            r = cc.get(url, timeout=timeout, impersonate="chrome120",
                       headers={"User-Agent": UA})
            return r.status_code, r.text or ""
        except Exception as e:
            return None, str(e)[:200]
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA, "Connection": "close"})
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, r.read().decode('utf-8', errors='ignore')
    except Exception as e:
        return None, str(e)[:200]

def fetch_with_wayback(url, timeout=15, year="2024"):
    """Try direct URL via curl_cffi, then urllib, then Wayback Machine.
    Returns (status, body, source_url) or (None, None, None) on total failure."""
    # Try curl_cffi first (browser impersonation bypasses bot detection)
    code, body = fetch(url, timeout=timeout, use_cc=True)
    if code == 200 and body and len(body) > 500:
        return code, body, url
    # Try plain urllib
    code, body = fetch(url, timeout=timeout, use_cc=False)
    if code == 200 and body and len(body) > 500:
        return code, body, url
    # Try Wayback Machine
    wb_url = f"https://web.archive.org/web/{year}/{url}"
    try:
        code, body = fetch(wb_url, timeout=30)
        if code == 200 and body and len(body) > 500:
            return code, body, wb_url
    except Exception:
        pass
    return None, None, None

def html_to_text(html):
    """Crude HTML to text conversion."""
    import html as h
    # Remove script/style/nav/header/footer/aside blocks (each non-greedy)
    for tag in ('script', 'style', 'nav', 'header', 'footer', 'aside'):
        html = re.sub(rf'<{tag}\b[^>]*>.*?</{tag}>', '', html, flags=re.S|re.I)
    # Insert newlines at block boundaries
    html = re.sub(r'<br\s*/?>', '\n', html, flags=re.I)
    html = re.sub(r'</p>', '\n\n', html, flags=re.I)
    html = re.sub(r'</div>', '\n', html, flags=re.I)
    html = re.sub(r'</section>', '\n', html, flags=re.I)
    html = re.sub(r'</h[1-6]>', '\n\n', html, flags=re.I)
    html = re.sub(r'</li>', '\n', html, flags=re.I)
    html = re.sub(r'</tr>', '\n', html, flags=re.I)
    html = re.sub(r'</td>', ' | ', html, flags=re.I)
    # Strip remaining tags
    html = re.sub(r'<[^>]+>', ' ', html)
    html = h.unescape(html)
    # Normalize whitespace
    html = re.sub(r'[ \t]+', ' ', html)
    html = re.sub(r' *\n *', '\n', html)
    html = re.sub(r'\n{3,}', '\n\n', html)
    return html.strip()

def save_verbatim(state, label, source_url, text, subdir):
    out = ROOT / f"plugins/us-{state}-legal-corpus/references/{subdir}/verbatim"
    out.mkdir(parents=True, exist_ok=True)
    fname = re.sub(r'[^A-Za-z0-9._-]+', '_', label)[:60] + ".md"
    md = f"""# {state.upper()} — {label}

**Source:** <{source_url}>
**Plugin:** `us-{state}-legal-corpus`
**Pulled:** {TODAY}

---

{text[:80000]}
"""
    (out / fname).write_text(md, encoding='utf-8')
    return (out / fname).stat().st_size

# Per-state URL generators
def gen_urls(state, max_n=15):
    pairs = []
    if state == "al":
        for n in range(1, max_n+1):
            pairs.append((f"Title {n}", f"https://law.justia.com/codes/alabama/title-{n}/"))
    elif state == "ak":
        for n in range(1, 48):
            pairs.append((f"AS Title {n}", f"https://www.akleg.gov/basis/statutes.asp#{n}"))
    elif state == "az":
        for n in range(1, 50):
            pairs.append((f"Title {n}", f"https://www.azleg.gov/arsDetail/?title={n}"))
    elif state == "ar":
        pairs.append(("Arkansas Code Main", "https://www.arkleg.state.ar.us/ArkansasLaw"))
        pairs.append(("AR Acts Index", "https://www.arkleg.state.ar.us/Acts/CodeSectionsAmended"))
    elif state == "ca":
        codes = ["BPC","CIV","CCP","COM","CORP","ELEC","EVID","FAM","FIN","GOV","HSC","INS","LAB","PEN","PROB","UIC","VEH"]
        for c in codes:
            pairs.append((c, f"https://leginfo.legislature.ca.gov/faces/codesTOCSelected.xhtml?tocCode={c}"))
    elif state == "co":
        for n in range(1, 45):
            pairs.append((f"Title {n}", f"https://leg.colorado.gov/colorado-revised-statutes#{n}"))
    elif state == "ct":
        for n in range(1, 56):
            pairs.append((f"Title {n}", f"https://www.cga.ct.gov/current/pub/title_{n}.htm"))
    elif state == "de":
        for n in range(1, 33):
            pairs.append((f"Title {n}", f"https://delcode.delaware.gov/title{n}/"))
    elif state == "fl":
        for n in range(1, 50):
            pairs.append((f"Title {n}", f"https://www.leg.state.fl.us/Statutes/index.cfm?App_mode=Display_Statute&URL=0000-0099/00{n:02d}/"))
    elif state == "ga":
        for n in range(1, 54):
            pairs.append((f"Title {n}", f"https://www.legis.ga.gov/legislation/en-US/Statutes/Code/0/1/0/{n}"))
    elif state == "hi":
        for label, url in [
            ("HI Legislature Main", "https://www.capitol.hawaii.gov/"),
            ("HRS Vol 1 (Ch 1-42)", "https://www.capitol.hawaii.gov/hrscurrent/Vol01_Ch0001-0042/"),
            ("HRS Vol 10 (Ch 480-492 Consumer)", "https://www.capitol.hawaii.gov/hrscurrent/Vol10_Ch0480-0492/"),
            ("HRS Vol 12 (Ch 571-574 Family)", "https://www.capitol.hawaii.gov/hrscurrent/Vol12_Ch0571-0574/"),
        ]:
            pairs.append((label, url))
    elif state == "id":
        for n in range(1, 78):
            pairs.append((f"Title {n}", f"https://legislature.idaho.gov/statutesrules/idstat/Title{n:02d}/"))
    elif state == "il":
        for n in [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105]:
            pairs.append((f"Ch {n}", f"https://ilga.gov/Legislation/ILCS/Chapters"))
    elif state == "in":
        for n in range(1, 37):
            pairs.append((f"Title {n}", f"http://iga.in.gov/legislative/laws/2024/ic/titles/articles/{n:03d}"))
    elif state == "ia":
        for n in range(1, 17):
            pairs.append((f"Title {n}", f"https://www.legis.iowa.gov/law/statutory"))
    elif state == "ks":
        for n in [1, 2, 8, 12, 16, 17, 21, 22, 23, 25, 28, 32, 40, 44, 45, 50, 55, 58, 60, 65, 66, 68, 71, 72, 75, 76, 79, 81, 83, 84]:
            pairs.append((f"Article {n}", f"https://www.kslegislature.org/li/b2025_26/statute/{n:03d}_000_0000_chapter/"))
    elif state == "ky":
        # KY uses chapter.aspx?id=NNNNN pattern
        for n in [1, 2, 6, 8, 12, 14, 15, 17, 18, 20, 21, 24, 25, 26, 27, 30, 31, 35, 36, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 61, 64, 65, 67, 121, 131, 132, 134, 138, 139, 141, 150, 151, 154, 158, 160, 162, 164, 165, 166, 167, 168, 171, 174, 175, 177, 178, 186, 188, 189, 190, 194, 197, 199, 200, 201, 205, 208, 209, 210, 211, 213, 214, 216, 218, 220, 222, 224, 226, 229, 230, 232, 234, 235, 237, 239, 241, 242, 243, 244, 245, 246, 247, 248, 250, 251, 253, 254, 255, 256, 257, 258, 260, 261, 262, 263, 264, 266, 267, 271, 272, 273, 274, 275, 276, 277, 278, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 299, 301, 304, 306, 307, 311, 312, 314, 315, 316, 317, 318, 320, 321, 322, 323, 324, 325, 326, 327, 330, 331, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520]:
            pairs.append((f"Chapter {n}", f"https://apps.legislature.ky.gov/law/statutes/chapter.aspx?id={n}"))
    elif state == "la":
        # LA uses Laws_Toc.aspx?folder=N (note plural "Laws" and case)
        for n in [66, 67, 68, 69, 70, 71, 72, 73, 75, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95]:
            pairs.append((f"Code Title {n}", f"https://www.legis.la.gov/legis/Laws_Toc.aspx?folder={n}"))
    elif state == "me":
        for n in range(1, 37):
            pairs.append((f"Title {n}", f"https://legislature.maine.gov/statutes/{n}/title{n}ch0sec0.html"))
    elif state == "md":
        for art in ["gtr", "b_r", "brl", "cg", "cl", "cr", "crp", "csa", "ec", "ed", "el", "fl", "gd", "gp", "hu", "lg", "luc", "pr", "ps", "rp", "sb", "sg", "sp", "ta", "tg", "tl", "tr", "ts", "tt"]:
            pairs.append((f"Article {art}", f"https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText?article={art}"))
    elif state == "ma":
        for part in ["I", "II", "III", "IV"]:
            pairs.append((f"Part {part}", f"https://malegislature.gov/Laws/GeneralLaws/Part{part}"))
    elif state == "mi":
        for n in ["4", "8", "17", "37", "38", "41", "45", "49", "50", "55", "87", "110", "168", "211", "257", "285", "287", "320", "324", "328", "330", "333", "335", "339", "340", "343", "349", "350", "380", "386", "387", "397", "408", "421", "429", "436", "440", "445", "450", "451", "456", "487", "500", "552", "600", "712A", "722", "750", "760", "791"]:
            pairs.append((f"Chapter {n}", f"https://www.legislature.mi.gov/Laws/MCLSearch?chapterID={n}"))
    elif state == "mn":
        for n in ["1", "5", "6", "8", "10", "13", "15", "16", "17", "18", "21", "31A", "45", "47", "48", "50", "51A", "53A", "60A", "60B", "60C", "60D", "60E", "60F", "60G", "60H", "60J", "60K", "60L", "60M", "60N", "65A", "65B", "67A", "68A", "72A", "72B", "72C", "79", "80A", "80B", "80C", "81A", "82A", "84A", "86A", "88A", "92A", "97A", "97B", "97C", "103A", "103D", "103E", "103F", "103G", "103H", "103I", "116A", "116B", "116C", "116D", "116E", "116F", "116G", "116H", "116I", "116J", "116L", "116M", "116N", "116P", "116R", "116S", "116V", "117", "119A", "119B", "120", "120A", "120B", "120C", "120D", "121", "121A", "123", "123A", "123B", "124", "124D", "124E", "125", "125A", "125B", "126", "126C", "127", "128", "128A", "128B", "128C", "129", "129C", "130", "131", "132", "133", "134", "135", "135A", "135B", "136", "136A", "136B", "136C", "136D", "136E", "136F", "137", "138", "139", "140", "141", "142", "142A", "142B", "142E", "144", "144A", "144D", "144E", "144F", "144G", "144H", "145", "145A", "145B", "146", "146A", "146B", "147", "147A", "147B", "147C", "147D", "147E", "147F", "148", "148A", "148B", "148C", "148D", "148E", "148F", "149", "150", "150A", "151", "152", "153", "153A", "153B", "154", "154A", "154B", "154C", "155", "155A", "156", "156A", "157", "157A", "158", "159", "160", "160A", "161", "162", "163", "164", "165", "166", "166A", "167", "168", "168A", "169", "170", "171", "172", "173", "174", "175", "176", "177", "178", "179", "180", "181", "181A", "182", "183", "184", "184A", "184B", "185", "186", "187", "188", "189", "190", "191", "192", "193", "193A", "194", "194A", "195", "196", "197", "198", "199", "200", "200A", "201", "202", "203", "204", "204A", "204B", "204C", "205", "205A", "206", "207", "208", "209", "210", "211", "211A", "211B", "212", "212A", "213", "214", "215", "216", "216A", "216B", "216C", "216D", "216E", "216F", "216G", "216H", "217", "218", "219", "220", "221", "222", "223", "224", "225", "226", "227", "228", "229", "230", "231", "232", "233", "234", "235", "236", "237", "238", "239", "240", "240A", "241", "242", "243", "244", "245", "246", "247", "248", "249", "250", "251", "252", "253", "254", "254A", "254B", "256", "256B", "256C", "256D", "256E", "256F", "256G", "256H", "256I", "256J", "256K", "256L", "256M", "257", "257B", "258", "258A", "258B", "258C", "258D", "258E", "259", "260", "260A", "260B", "260C", "260D", "260E", "260F", "261", "262", "263", "264", "264A", "265", "266", "267", "268", "268A", "269", "270", "271", "272", "273", "274", "275", "276", "277", "278", "279", "280", "281", "282", "283", "284", "285", "286", "287", "288", "289", "290", "291", "292", "293", "294", "295", "296", "297", "298", "299", "300", "301", "302", "303", "304", "305", "306", "306A", "307", "308", "308A", "308B", "308C", "309", "310", "311", "312", "313", "314", "315", "316", "317", "318", "319", "320", "321", "322", "323", "324", "325", "326", "327", "328", "329", "330", "331", "332", "333", "334", "335", "336", "337", "338", "339", "340", "341", "342", "343", "344", "345", "346", "347", "348", "349", "350", "351", "352", "353", "354", "355", "356", "357", "358", "359", "360", "361", "362", "363", "364", "365", "366", "367", "368", "369", "370", "371", "372", "373", "374", "375", "376", "377", "378", "379", "380", "381", "382", "383", "384", "385", "386", "387", "388", "389", "390", "391", "392", "393", "394", "395", "396", "397", "398", "399", "400", "401", "402", "403", "404", "405", "406", "407", "408", "409", "410", "411", "412", "413", "414", "415", "416", "417", "418", "419", "420", "421", "422", "423", "424", "425", "426", "427", "428", "429", "430", "431", "432", "433", "434", "435", "436", "437", "438", "439", "440", "441", "442", "443", "444", "445", "446", "447", "448", "449", "450", "451", "452", "453", "454", "455", "456", "457", "458", "459", "460", "461", "462", "463", "464", "465", "466", "467", "468", "469", "470", "471", "472", "473", "474", "475", "476", "477", "478", "479", "480", "481", "482", "483", "484", "485", "486", "487", "488", "489", "490", "491", "492", "493", "494", "495", "496", "497", "498", "499", "500", "501", "502", "503", "504", "504A", "504B", "504C", "504D", "504E", "504F", "504G", "504H", "505", "506", "507", "508", "508A", "508B", "509", "510", "511", "512", "513", "514", "515", "515A", "515B", "516", "517", "518", "519", "520", "521", "522", "523", "524", "525", "526", "527", "528", "529", "530", "531", "532", "533", "534", "535", "536", "537", "538", "539", "540", "541", "542", "543", "544", "545", "546", "547", "548", "549", "550", "551", "552", "553", "554", "555", "556", "557", "558", "559", "560", "561", "562", "563", "564", "565", "566", "567", "568", "569", "570", "571", "572", "573", "574", "575", "576", "577", "578", "579", "580", "581", "582", "583", "584", "585", "586", "587", "588", "589", "590", "591", "592", "593", "594", "595", "596", "597", "598", "599", "600", "601", "602", "603", "604", "605", "606", "607", "608", "609", "610", "611", "612", "613", "614", "615", "616", "617", "618", "619", "620", "621", "622", "623", "624", "625", "626", "627", "628", "629", "630", "631", "632", "633", "634", "635", "636", "637", "638", "639", "640", "641", "642", "643", "644", "645", "646", "647", "648", "649", "650", "651", "652", "653", "654", "655", "656", "657"]:
            pairs.append((f"Chapter {n}", f"https://www.revisor.mn.gov/statutes/cite/{n}"))
    elif state == "mo":
        for n in range(1, 33):
            pairs.append((f"Title {n}", f"https://revisor.mo.gov/main/OneChapter.aspx?chapter={n}"))
    elif state == "ms":
        for n in range(1, 100, 4):
            pairs.append((f"Title {n} (Justia)", f"https://law.justia.com/codes/mississippi/title-{n}/"))
    elif state == "mt":
        for n in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 30, 32, 33, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91]:
            pairs.append((f"Title {n} Index", f"https://leg.mt.gov/bills/mca/title_{n:04d}/chapters_index.html"))
    elif state == "nc":
        for n in range(1, 169, 3):
            pairs.append((f"Chapter {n}", f"https://www.ncleg.gov/Laws/GeneralStatuteSections/Chapter{n}"))
    elif state == "nd":
        for n in range(1, 70, 2):
            pairs.append((f"Title {n}", f"https://www.legis.nd.gov/cencode/t{n:02d}c01.pdf"))
    elif state == "ne":
        for n in range(1, 90, 2):
            pairs.append((f"Chapter {n}", f"https://nebraskalegislature.gov/laws/browse-chapters.php?chapter={n}"))
    elif state == "nv":
        for n in range(0, 200, 3):
            pairs.append((f"NRS {n:03d}", f"https://www.leg.state.nv.us/NRS/NRS-{n:03d}.html"))
    elif state == "nh":
        # NH RSA uses Roman numerals for title numbers
        roman = ["I","II","III","IV","V","VI","VII","VIII","IX","X","XI","XII","XIII","XIV","XV","XVI","XVII","XVIII","XIX","XX","XXI","XXII","XXIII","XXIV","XXV"]
        for n, r in enumerate(roman, 1):
            pairs.append((f"Title {n}", f"https://www.gencourt.state.nh.us/rsa/html/{r}/1/1-1.htm"))
    elif state == "nj":
        for n in range(1, 60, 2):
            pairs.append((f"Title {n} (Justia)", f"https://law.justia.com/codes/new-jersey/title-{n}/"))
    elif state == "nm":
        pairs.append(("NM OneSource", "https://my.nmonesource.com/"))
        pairs.append(("NM CompComm", "https://www.nmcompcomm.us/"))
    elif state == "ny":
        codes = ["ABR","ABN","ACA","ACR","ACAT","ACS","ADC","AGT","ABC","ARL","BAN","BPM","BCA","BCT","BKK","BSC","BUY","CAN","CAT","CBR","CDS","CVP","CAL","CLN","CMD","COS","CCO","CCT","CVS","DEE","DEF","DEL","ECL","EDN","ELN","EAM","EXB","EFC","ENV","ESC","EPT","EXC","EXE","FCT","FAM","FAR","FIF","FIN","FNC","FRA","GAM","GBC","GBS","GCT","GEN","GML","GOP","GOG","GSC","HUM","HSC","IFL","IND","IOM","INS","ISL","JUD","LAB","LBD","LIC","LLC","LOC","MCK","MDL","MED","MEN","MGO","MIL","MHN","MMH","MMM","MAP","MIN","MIS","MNC","MUR","MHA","NAN","NAV","NEW","NPC","OHP","OFS","OGC","OPI","OIL","OPS","PDC","PDP","PDD","PEN","PBA","PER","PHL","PPB","PSP","PPP","PRT","PSA","PBR","PHN","PSB","RAO","RAC","RAH","RAT","RCC","REA","REC","REL","RET","RPL","RPB","RSA","RSC","RUL","RRS","SBB","SCD","SOA","SOS","SCT","SCP","SOC","STC","SST","STT","STD","STF","SGM","SOF","SOO","SSC","STN","TWN","TRA","TRY","TRP","TOB","TWP","UNL","URI","USC","VAG","VBF","VEB","VET","VTO","WAM","WCL","WMC","WTR","WIN","WPG","WCR","WIC","WLS","YAC"]
        for c in codes:
            pairs.append((c, f"https://www.nysenate.gov/legislation/laws/{c}"))
    elif state == "oh":
        for n in range(1, 59, 2):
            pairs.append((f"Title {n}", f"https://codes.ohio.gov/ohio-revised-code/title-{n}"))
    elif state == "ok":
        for n in range(1, 86, 2):
            pairs.append((f"Title {n}", f"https://www.oscn.net/applications/oscn/index.asp?level=1&ftdb=STOKST{n:02d}"))
    elif state == "or":
        for n in range(1, 200, 4):
            pairs.append((f"ORS {n}", f"https://www.oregonlegislature.gov/bills_laws/ors/ors{n:03d}.html"))
    elif state == "pa":
        for n in range(1, 79, 2):
            pairs.append((f"Title {n}", f"https://www.legis.state.pa.us/cfdocs/legis/LI/uconsCheck.cfm?txtType=HTM&yr=1990&sessInd=0&smthLwInd=0&act=0"))
    elif state == "ri":
        for n in range(1, 56, 2):
            pairs.append((f"Title {n}", f"https://webserver.rilegislature.gov/Statutes/title{n}/{n}-1/"))
    elif state == "sc":
        for n in range(1, 64, 2):
            pairs.append((f"Title {n}", f"https://www.scstatehouse.gov/code/t{n:02d}c001.php"))
    elif state == "sd":
        for n in range(1, 62, 2):
            pairs.append((f"Title {n}", f"https://sdlegislature.gov/Statutes/{n}-1"))
    elif state == "tn":
        for n in range(1, 72, 4):
            pairs.append((f"Title {n} (Justia)", f"https://law.justia.com/codes/tennessee/title-{n}/"))
    elif state == "tx":
        for c in ["AGRIC","ALCO","BUS","BUSORG","CPRC","EDUC","ELEC","EST","FAM","FIN","GOVT","HUM","INS","LAB","LGC","LOC","MTRV","NAT","OCC","PEN","PERS","PROB","PROP","REC","REV","SPEC","TAX","TRAN","UTIL","WAT","WEL"]:
            pairs.append((c, f"https://statutes.capitol.texas.gov/Docs/{c}/htm/{c}.1.htm"))
    elif state == "ut":
        # UT requires N-M-Ssection pattern; section numbers vary
        for label, url in [
            ("UT Code Index", "https://le.utah.gov/xcode/code.html"),
            ("UT Title 52 Ch 4 S103", "https://le.utah.gov/xcode/Title52/Chapter4/52-4-S103.html"),
            ("UT Title 52 Ch 4 S101", "https://le.utah.gov/xcode/Title52/Chapter4/52-4-S101.html"),
        ]:
            pairs.append((label, url))
    elif state == "vt":
        for n in range(1, 34):
            pairs.append((f"Title {n}", f"https://legislature.vermont.gov/statutes/section/{n}/1"))
    elif state == "va":
        for n in range(1, 74, 2):
            pairs.append((f"Title {n}", f"https://law.lis.virginia.gov/vacode/title{n}/"))
    elif state == "wa":
        for n in range(1, 92, 2):
            pairs.append((f"Title {n}", f"https://app.leg.wa.gov/RCW/default.aspx?cite={n}"))
    elif state == "wv":
        for n in range(1, 65, 2):
            pairs.append((f"Chapter {n}", f"https://code.wvlegislature.gov/{n}-1-1/"))
    elif state == "wi":
        # WI requires Wayback (TLS incompatible with our proxy)
        for n in [1, 5, 10, 19, 20, 25, 30, 40, 50, 66, 100, 125, 200, 301, 350, 450, 500, 550, 600, 700, 800, 893, 940, 947]:
            pairs.append((f"Ch {n} (Wayback)", f"https://web.archive.org/web/2024/https://docs.legis.wisconsin.gov/statutes/statutes/{n}"))
    elif state == "wy":
        for n in range(1, 42):
            pairs.append((f"Title {n}", f"https://wyoleg.gov/statutes/compress/title{n}.pdf"))
    return pairs[:max_n]

def pull_state(state, max_titles=15):
    print(f"\n=== {state.upper()} ===")
    urls = gen_urls(state, max_titles)
    n = 0
    for label, url in urls:
        code, body, src = fetch_with_wayback(url, timeout=12)
        if code == 200 and body and len(body) > 500:
            text = html_to_text(body)
            if len(text) > 300:
                save_verbatim(state, label, src, text, f"{state}-statutes")
                n += 1
                if n < 3:
                    print(f"  [ok]   {label[:30]:30}  {len(text)} chars")
        time.sleep(0.3)
    print(f"  >>> {state}: {n}/{len(urls)} files")
    return n

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--state", help="Pull a single state")
    parser.add_argument("--all", action="store_true", help="Pull all 50 states")
    parser.add_argument("--max-titles", type=int, default=15, help="Max titles per state")
    args = parser.parse_args()
    
    STATES = ["al","ak","az","ar","ca","co","ct","de","fl","ga","hi","id","il","in","ia","ks","ky","la","me","md","ma","mi","mn","ms","mo","mt","ne","nv","nh","nj","nm","ny","nc","nd","oh","ok","or","pa","ri","sc","sd","tn","tx","ut","vt","va","wa","wv","wi","wy"]
    
    if args.state:
        pull_state(args.state, args.max_titles)
    elif args.all:
        total = 0
        for st in STATES:
            try:
                n = pull_state(st, args.max_titles)
                total += n
            except Exception as e:
                print(f"  ERR {st}: {e}")
        print(f"\n=== TOTAL: {total} files across {len(STATES)} states ===")
    else:
        parser.print_help()
