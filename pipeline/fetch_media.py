"""Download real images per scene and record license/credit.
Generic everyday-life scenes (query with no capitalised word, e.g. "1950s family dinner table") take frames from real
1945-1969 films of the Prelinger Archives on archive.org (public domain); scenes naming something specific
(e.g. "1955 Chevrolet Bel Air", "Jonas Salk") use Wikimedia Commons photos. Either source falls back to the other."""
import json, os, random, re, subprocess, sys, time, pathlib, requests

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


# ---------- Prelinger Archives film frames ----------
IA = "https://archive.org"
STOP = {"vintage", "american", "america", "old", "retro", "the", "a", "of", "and", "in", "with", "to", "for", "on", "at", "from", "your"}
FILMS = pathlib.Path("/tmp/films"); _films, _used_frames = {}, set()


def wants_film(query):
    # a named subject (Levittown, Chevrolet Bel Air) goes to Commons; "American" alone does not count
    return not re.search(r"\b(?!America\b|American\b)[A-Z][a-z]", query)


# films about war, crime, disease or disaster: wrong mood for a nostalgia scene unless the query asks for it
DARK = re.compile(r"prison|warfare|biological|psycholog|military|army|navy|tornado|gun|crime|criminal|delinquen|venereal|"
                  r"drug|narcotic|alcohol|poverty|disease|accident|death|police|riot|atomic|bomb|nuclear|enemy|soviet|commun", re.I)


def film_terms(query):
    words = [w for w in re.sub(r"\b(19\d\ds?|\d{2}s)\b", " ", query.lower()).split() if w not in STOP]
    return words[:3]


def ia_search(words):
    q = "collection:prelinger AND year:[1945 TO 1969] AND (" + " AND ".join(f"(title:{w} OR subject:{w} OR description:{w})" for w in words) + ")"
    for attempt in range(5):
        try:
            r = requests.get(f"{IA}/advancedsearch.php", params={"q": q, "fl[]": ["identifier", "title", "year"], "rows": 15,
                             "sort[]": "downloads desc", "output": "json"}, headers=HEADERS, timeout=60)
            if r.ok: return r.json()["response"]["docs"]
        except (requests.RequestException, ValueError, KeyError):
            pass
        time.sleep(5 * (attempt + 1))
    return []


def film_file(ident):
    """Smallest h.264/MPEG4 derivative of the film, downloaded once per run."""
    if ident in _films: return _films[ident]
    _films[ident] = None
    try:
        files = requests.get(f"{IA}/metadata/{ident}", headers=HEADERS, timeout=60).json().get("files", [])
    except (requests.RequestException, ValueError):
        return None
    mp4 = [f for f in files if f.get("name", "").endswith(".mp4") and 1e6 < int(f.get("size", 0) or 0) < 400e6]
    if not mp4: return None
    f = min(mp4, key=lambda f: int(f["size"]))
    if DRY: _films[ident] = (f"{IA}/download/{ident}/{f['name']}", 600.0); return _films[ident]
    FILMS.mkdir(exist_ok=True); path = FILMS / f"{ident}.mp4"
    if not path.exists(): path.write_bytes(download(f"{IA}/download/{ident}/{f['name']}"))
    try:
        dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(path)],
                                   capture_output=True, text=True).stdout.strip())
    except ValueError:
        return None
    _films[ident] = (path, dur); return _films[ident]


def pick_film(query):
    words = film_terms(query)
    docs = []
    while words and not docs:
        docs = ia_search(words); words = words[:-1]
    docs = [d for d in docs if not (DARK.search(str(d.get("title", ""))) and not DARK.search(query))]
    random.shuffle(docs)
    for d in docs[:6]:
        ff = film_file(d["identifier"])
        if not ff: continue
        src, dur = ff
        for _ in range(12):
            t = round(random.uniform(dur * 0.06, dur * 0.94), 1)
            key = (d["identifier"], int(t // 4))  # never two frames from the same 4 seconds
            if key in _used_frames: continue
            _used_frames.add(key)
            return {"title": f"{d.get('title', d['identifier'])} ({d.get('year', '')}) at {t}s", "src": src, "t": t,
                    "page": f"{IA}/details/{d['identifier']}", "dur": dur, "license": "Public domain (Prelinger Archives)",
                    "artist": "Prelinger Archives"}
    return None


def brightness(src, t):
    """Mean luma (0-255) of the frame at t, read from a 32x18 grey thumbnail."""
    raw = subprocess.run(["ffmpeg", "-loglevel", "error", "-ss", str(t), "-i", str(src), "-frames:v", "1",
                          "-vf", "scale=32:18,format=gray", "-f", "rawvideo", "-"], capture_output=True).stdout
    return sum(raw) / len(raw) if raw else 0


def save_frame(m, f):
    """One frame from the film, cropped to 16:9 and upscaled so the slow zoom stays sharp enough.
    Black frames (fades, night scenes, dark leader) are skipped for another moment of the same film."""
    for _ in range(6):
        if brightness(m["src"], m["t"]) >= 30: break
        m["t"] = round(random.uniform(m["dur"] * 0.06, m["dur"] * 0.94), 1)
    else:
        return False
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-ss", str(m["t"]), "-i", str(m["src"]), "-frames:v", "1",
                    "-vf", "crop=iw:min(ih\\,iw*9/16),scale=2880:-2:flags=lanczos", "-q:v", "2", str(f)], check=True)
    return f.exists() and f.stat().st_size > 5000


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
            if s.get("film", wants_film(q)):
                fm = pick_film(q)
                if fm and (DRY or save_frame(fm, f)):
                    if DRY: print("SCENE", i, k, "|", q, "| FILM", fm["title"]); last = last or True; continue
                    last = f; credits.append({k2: v for k2, v in fm.items() if k2 not in ("src", "t")} | {"scene": i, "cut": k})
                    print(i, k, "film", fm["title"]); continue
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
