"""Download real images per scene and record license/credit.
Generic everyday-life scenes (query with no capitalised word, e.g. "1950s family dinner table") take frames from real
1945-1969 films of the Prelinger Archives on archive.org (public domain); scenes naming something specific
(e.g. "1955 Chevrolet Bel Air", "Jonas Salk") use Wikimedia Commons photos. Either source falls back to the other."""
import io, json, os, random, re, subprocess, sys, time, pathlib, requests
from PIL import Image, ImageStat

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


def taken_year(meta):
    """Year the photo was taken, from Commons metadata (None when unknown)."""
    m = re.search(r"\b(1[89]\d\d|20\d\d)\b", re.sub(r"<[^>]+>", "", meta.get("DateTimeOriginal", {}).get("value", "")))
    return int(m.group(1)) if m else None


def pick(query, used, old=False):
    """old=True: only photos dated before 1990, so a 1950s scene does not get today's Disneyland."""
    params = {
        "action": "query", "format": "json", "generator": "search",
        "gsrsearch": f"{query} filetype:bitmap", "gsrnamespace": 6, "gsrlimit": 30,
        "prop": "imageinfo", "iiprop": "url|size|mime|extmetadata", "iiurlwidth": 1920,
    }
    pages = api_pages(params)
    cands = []
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
        if old and (taken_year(meta) or 9999) >= 1990:  # undated photos are usually recent uploads too
            continue
        artist = meta.get("Artist", {}).get("value", "unknown")
        cands.append({"title": p["title"], "url": info["thumburl"], "page": info["descriptionurl"],
                      "license": lic, "artist": artist})
        if len(cands) >= (6 if CLIP else 1): break
    if not cands or not CLIP: return cands[0] if cands else None
    imgs = []
    for c in cands:  # score small thumbnails, download the full one only for the winner
        try:
            r = requests.get(c["url"].replace("/1920px-", "/330px-"), headers=HEADERS, timeout=30); r.raise_for_status()
            imgs.append(Image.open(io.BytesIO(r.content)).convert("RGB"))
        except Exception:
            imgs.append(Image.new("RGB", (330, 186)))
    scores = fit(imgs, query)
    best = max(range(len(cands)), key=lambda i: scores[i])
    return cands[best] | {"fit": scores[best]}


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
# travelogues and films about other countries: their frames slip past CLIP on generic queries (a Thai temple in video06)
FOREIGN = re.compile(r"\b(orient|asia|japan|china|siam|thailand|india|europe|germany|italy|rome|paris|france|mexico|wonderful world|shrinking world)\b", re.I)


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
    docs = [d for d in docs if not any(R.search(str(d.get("title", ""))) and not R.search(query) for R in (DARK, FOREIGN))]
    random.shuffle(docs)
    cands = []  # (doc, src, dur, t, small image): a few moments from up to 3 films, CLIP keeps the one that fits best
    for d in docs[:6]:
        if len({c[0]["identifier"] for c in cands}) >= 3: break
        ff = film_file(d["identifier"])
        if not ff: continue
        src, dur = ff
        for _ in range(5 if CLIP else 1):
            t = round(random.uniform(dur * 0.06, dur * 0.94), 1)
            if (d["identifier"], int(t // 4)) in _used_frames: continue  # never two frames from the same 4 seconds
            img = None if DRY else small_frame(src, t)
            if not DRY and (img is None or ImageStat.Stat(img.convert("L")).mean[0] < 30): continue
            cands.append((d, src, dur, t, img))
        if cands and not CLIP: break
    if not cands: return None
    best = max(zip(fit([c[4] for c in cands], query), cands), key=lambda x: x[0]) if CLIP else (None, cands[0])
    score, (d, src, dur, t, _) = best
    _used_frames.add((d["identifier"], int(t // 4)))
    return {"title": f"{d.get('title', d['identifier'])} ({d.get('year', '')}) at {t}s", "src": src, "t": t,
            "page": f"{IA}/details/{d['identifier']}", "dur": dur, "license": "Public domain (Prelinger Archives)",
            "artist": "Prelinger Archives", "fit": score}


def small_frame(src, t):
    png = subprocess.run(["ffmpeg", "-loglevel", "error", "-ss", str(t), "-i", str(src), "-frames:v", "1",
                          "-vf", "crop=iw:min(ih\\,iw*9/16),scale=336:-2", "-f", "image2pipe", "-vcodec", "png", "-"],
                         capture_output=True).stdout
    try:
        return Image.open(io.BytesIO(png)).convert("RGB")
    except Exception:
        return None


# ---------- CLIP: does the picture actually show what the scene talks about? ----------
# the last two catch travel films and industrial films that match a generic query (video07: a Thai temple, Rome, a circuit board)
NEG = ["a cartoon or animated drawing", "a title card or a screen full of text", "a dark blurry frame",
       "a temple, palace or landmark in Asia or Europe", "a close-up of machinery or electronic parts"]


def load_clip():
    if DRY or os.environ.get("CLIP") == "0": return None
    try:
        import open_clip, torch
        model, _, prep = open_clip.create_model_and_transforms("ViT-B-32", pretrained="laion2b_s34b_b79k")
        return model.eval(), prep, open_clip.get_tokenizer("ViT-B-32"), torch
    except Exception as e:  # no CLIP: fall back to the first frame found, as before
        print("CLIP unavailable:", e); return None


def fit(imgs, query):
    """For each image, the probability that it is "a photo of <query>" rather than a cartoon, a text card or a black
    frame."""
    model, prep, tok, torch = CLIP
    texts = [f"an old photo of {re.sub(r'[0-9]{4}s?', '', query).strip()}"] + NEG
    with torch.no_grad():
        im = model.encode_image(torch.stack([prep(i) for i in imgs])); tx = model.encode_text(tok(texts))
        im = im / im.norm(dim=-1, keepdim=True); tx = tx / tx.norm(dim=-1, keepdim=True)
        return (100 * im @ tx.T).softmax(dim=-1)[:, 0].tolist()


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


# objects that survive in museums and car shows: a photo taken today still shows the real 1950s thing
OBJECT = re.compile(r"vintage|museum|Chevrolet|Cadillac|Ford|Plymouth|Edsel|Mustang|Schwinn|Lionel|Sputnik|Explorer 1|Pyrex|"
                    r"Corning|Tupperware|Mixmaster|Princess telephone|Mason jars|Formica", re.I)

DRY = bool(os.environ.get("DRY"))  # DRY=1: only search and print which photo each scene would get (no downloads)
CLIP = load_clip()


def main(video):
    d = pathlib.Path("videos") / video
    script = json.loads((d / "script.json").read_text())
    (d / "media").mkdir(exist_ok=True)
    used, credits, last = set(), [], None
    for i, s in enumerate(script["scenes"]):
        for k in range(s.get("cuts", 2)):
            f = d / "media" / f"{i}_{k}.jpg"
            q, fm = s["query"], None
            if s.get("film", wants_film(q)):
                fm = pick_film(q)
                if fm and (DRY or save_frame(fm, f)):
                    if DRY: print("SCENE", i, k, "|", q, "| FILM", fm["title"]); last = last or True; continue
                    last = f; credits.append({k2: v for k2, v in fm.items() if k2 not in ("src", "t")} | {"scene": i, "cut": k})
                    print(i, k, "film", fm["title"], "fit", fm.get("fit")); continue
                fm = None
            m = None
            # period photos first; a modern photo only when nothing else exists ("modern": true allows it, e.g. a restored car)
            for old in ((False,) if s.get("modern", bool(OBJECT.search(s["query"]))) else (True, False)):
                q = s["query"]; m = pick(q, used, old)
                while m is None and len(q.split()) > 2:  # query too narrow: drop the last word and retry
                    q = " ".join(q.split()[:-1]); m = pick(q, used, old)
                if m or not old: break
                if not s.get("film", wants_film(s["query"])):  # no period photo on Commons: try a film frame
                    fm = pick_film(s["query"])
                    if fm and (DRY or save_frame(fm, f)):
                        break
                    fm = None
            if m is None and fm:
                if DRY: print("SCENE", i, k, "|", s["query"], "| FILM", fm["title"]); last = last or True; continue
                last = f; credits.append({k2: v for k2, v in fm.items() if k2 not in ("src", "t")} | {"scene": i, "cut": k})
                print(i, k, "film", fm["title"], "fit", fm.get("fit")); continue
            if m is None:  # search exhausted: reuse the last photo rather than fail the whole video
                if DRY: print("SCENE", i, k, "|", s["query"], "|", "REUSE" if last else "NONE"); last = last or True; continue
                if last is None: raise SystemExit("no photo found for scene %d: %s" % (i, s["query"]))
                f.write_bytes(last.read_bytes()); print(i, k, "reuse"); continue
            used.add(m["title"])
            if DRY:
                print("SCENE", i, k, "|", s["query"], "|", m["title"]); last = True; continue
            f.write_bytes(download(m["url"])); last = f
            credits.append({**m, "scene": i, "cut": k})
            print(i, k, m["title"], m["license"], "fit", m.get("fit"))
    if not DRY: (d / "credits.json").write_text(json.dumps(credits, indent=2))


if __name__ == "__main__":
    main(sys.argv[1])
