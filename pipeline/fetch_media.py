"""Download real photos per scene from Wikimedia Commons (several per scene for fast cuts) and record license/credit."""
import json, os, sys, time, pathlib, requests

API = "https://commons.wikimedia.org/w/api.php"
HEADERS = {"User-Agent": "growing-up-america-channel/1.0 (github.com/viniciushoscher-ctrl/growing-up-america)"}
_cache = {}


def api_pages(params):
    """Wikimedia rate-limits bursts; retry with backoff and cache identical searches."""
    key = json.dumps(params, sort_keys=True)
    if key in _cache:
        return _cache[key]
    for attempt in range(8):
        time.sleep(1.5)
        r = requests.get(API, params=params, headers=HEADERS, timeout=60)
        if r.status_code == 200:
            try:
                pages = r.json().get("query", {}).get("pages", {})
                _cache[key] = pages
                return pages
            except ValueError:
                pass
        time.sleep(5 * (attempt + 1))
    raise SystemExit(f"Commons API kept failing for {params['gsrsearch']}")


def download(url):
    for attempt in range(8):
        r = requests.get(url, headers=HEADERS, timeout=120)
        if r.status_code == 200:
            return r.content
        time.sleep(5 * (attempt + 1))
    raise SystemExit(f"download failed: {url}")


def pick(query, used):
    params = {
        "action": "query", "format": "json", "generator": "search",
        "gsrsearch": f"{query} filetype:bitmap", "gsrnamespace": 6, "gsrlimit": 30,
        "prop": "imageinfo", "iiprop": "url|size|mime|extmetadata", "iiurlwidth": 1920,
    }
    pages = api_pages(params)
    for p in sorted(pages.values(), key=lambda x: x.get("index", 0)):
        info = (p.get("imageinfo") or [{}])[0]
        if info.get("mime") != "image/jpeg" or info.get("width", 0) < 2000:
            continue
        if info["width"] < info.get("height", 0) * 1.3 or p["title"] in used:
            continue
        meta = info.get("extmetadata", {})
        lic = meta.get("LicenseShortName", {}).get("value", "")
        if not lic.startswith(("CC", "Public domain", "PD")):
            continue
        artist = meta.get("Artist", {}).get("value", "unknown")
        return {"title": p["title"], "url": info["thumburl"], "page": info["descriptionurl"],
                "license": lic, "artist": artist}
    return None


DRY = bool(os.environ.get("DRY"))  # DRY=1: only search and print which photo each scene would get (no downloads)


def main(video):
    d = pathlib.Path("videos") / video
    script = json.loads((d / "script.json").read_text())
    (d / "media").mkdir(exist_ok=True)
    used, credits, last = set(), [], None
    for i, s in enumerate(script["scenes"]):
        for k in range(s.get("cuts", 2)):
            f = d / "media" / f"{i}_{k}.jpg"
            q = s["query"]
            m = pick(q, used)
            while m is None and len(q.split()) > 2:  # query too narrow: drop the last word and retry
                q = " ".join(q.split()[:-1]); m = pick(q, used)
            if m is None:  # search exhausted: reuse the last photo rather than fail the whole video
                if DRY: print("SCENE", i, k, "|", s["query"], "|", "REUSE" if last else "NONE"); last = last or True; continue
                if last is None: raise SystemExit("no photo found for scene %d: %s" % (i, s["query"]))
                f.write_bytes(last.read_bytes()); print(i, k, "reuse"); continue
            used.add(m["title"])
            if DRY:
                print("SCENE", i, k, "|", s["query"], "|", m["title"]); last = True; continue
            f.write_bytes(download(m["url"])); last = f
            credits.append({**m, "scene": i, "cut": k})
            print(i, k, m["title"], m["license"])
    if not DRY: (d / "credits.json").write_text(json.dumps(credits, indent=2))


if __name__ == "__main__":
    main(sys.argv[1])
