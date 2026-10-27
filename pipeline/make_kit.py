"""Build a manual-upload kit for one rendered video (used while the channel uploads by hand in YouTube Studio).

    python3 pipeline/make_kit.py video04 OUT_DIR [day] [slot]

Reads the deliveries-<video> branch (git fetch must already work), joins the video parts and writes to OUT_DIR:
<video>.mp4, <video>.srt and <video>.md (title, description with chapters and photo credits, tags)."""
import html, json, pathlib, re, subprocess, sys, tempfile

HASHTAGS = "#nostalgia #americana #vintageamerica"
TAGS = ("nostalgia, american nostalgia, 1950s, 1960s, 1970s, vintage america, old america, americana, baby boomers, "
        "memory lane, small town america, documentary, america that we love")


def git(*a, **kw):
    return subprocess.run(["git", *a], check=True, capture_output=True, **kw).stdout


def main(vid, out, day="", slot=""):
    out = pathlib.Path(out); out.mkdir(parents=True, exist_ok=True)
    git("fetch", "-q", "origin", f"deliveries-{vid}")
    tmp = pathlib.Path(tempfile.mkdtemp())
    tar = git("archive", "FETCH_HEAD", f"deliveries/{vid}", "--format=tar")
    subprocess.run(["tar", "-x", "-C", str(tmp)], input=tar, check=True)
    d = tmp / "deliveries" / vid
    with open(out / f"{vid}.mp4", "wb") as f:
        for p in sorted((d / "parts").glob("*.part*")): f.write(p.read_bytes())
    (out / f"{vid}.srt").write_bytes((d / "captions.srt").read_bytes())
    dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0",
                                str(out / f"{vid}.mp4")], capture_output=True, text=True).stdout)
    script = json.loads(pathlib.Path(f"videos/{vid}/script.json").read_text())
    credits = json.loads((d / "credits.json").read_text())
    hook = " ".join(s["text"] for s in script["scenes"][:2])
    chapters = (d / "chapters.txt").read_text().strip()
    seen, photo = set(), []
    for c in credits:
        if "Prelinger" in c["license"] or c["title"] in seen: continue
        seen.add(c["title"])
        artist = re.sub(r"<[^>]+>", "", html.unescape(c.get("artist", ""))).strip()[:40]
        photo.append(f"- {c['title'].replace('File:', '').rsplit('.', 1)[0][:60]}, {artist}, {c['license']}")
    sources = pathlib.Path(f"videos/{vid}/sources.md").read_text().strip()
    desc = (f"{hook}\n\nWhat year did this bring back for you? Tell us in the comments. We read every one.\n\n"
            f"Chapters\n{chapters}\n\nSources\n{sources}\n\n"
            "Film footage: Prelinger Archives (public domain), via the Internet Archive.\n"
            + (f"Photos: Wikimedia Commons\n" + "\n".join(photo) + "\n" if photo else "")
            + f"\n{HASHTAGS}")
    if len(desc) > 4900:  # YouTube limit is 5000 characters
        desc = desc[:4900].rsplit("\n", 1)[0]
    head = f"Dia {day} · {slot}\n\n" if day else ""
    (out / f"{vid}.md").write_text(
        f"# {vid}\n\n{head}Duração: {int(dur // 60)}:{int(dur % 60):02d}\n\n## Título\n{script['title']}\n\n"
        f"## Descrição\n{desc}\n\n## Tags\n{TAGS}\n")
    print(vid, f"{int(dur // 60)}:{int(dur % 60):02d}", len(desc), "chars")


if __name__ == "__main__":
    main(*sys.argv[1:])
