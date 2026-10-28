"""Search Wikimedia Commons and save public-domain photos for review (python grab_photos.py OUT "query" ...)."""
import json, sys, time, pathlib, requests
H = {"User-Agent": "growing-up-america/1.0 (photo review)"}
out = pathlib.Path(sys.argv[1]); out.mkdir(parents=True, exist_ok=True)
meta, n = [], 0
for q in sys.argv[2:]:
    r = requests.get("https://commons.wikimedia.org/w/api.php", headers=H, params={
        "action": "query", "format": "json", "generator": "search", "gsrnamespace": 6, "gsrlimit": 20,
        "gsrsearch": q + " filetype:bitmap", "prop": "imageinfo", "iiprop": "url|size|extmetadata", "iiurlwidth": 1600}).json()
    for p in (r.get("query", {}).get("pages", {}) or {}).values():
        ii = p["imageinfo"][0]; lic = ii.get("extmetadata", {}).get("LicenseShortName", {}).get("value", "")
        if "public domain" not in lic.lower() and "pd" not in lic.lower(): continue
        if min(ii["width"], ii["height"]) < 1000: continue
        n += 1; f = out / f"{n:03d}.jpg"
        f.write_bytes(requests.get(ii["thumburl"], headers=H).content); time.sleep(0.5)
        meta.append({"file": f.name, "title": p["title"], "license": lic, "page": ii["descriptionurl"], "size": [ii["width"], ii["height"]], "query": q})
(out / "meta.json").write_text(json.dumps(meta, indent=1))
print(n, "photos")
