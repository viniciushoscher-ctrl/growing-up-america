"""Builds the upload queue entry and thumbnail for one rendered Grandma Ruth video.
python grandma/queue.py <video> <publishAt UTC> <playlist> <thumb line 1> <thumb line 2> [media image]
Reads videos/<video>/ and the deliveries-<video> branch; writes into ../canal-dark-/grandma/."""
import json, pathlib, subprocess, sys
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont, ImageOps

V, AT, PL, L1, L2 = sys.argv[1:6]
OUT = pathlib.Path(__file__).resolve().parents[2] / "canal-dark-" / "grandma"
D = pathlib.Path(f"/tmp/deliv-{V}")
if not D.exists():
    subprocess.run(["git", "clone", "-q", "--depth", "1", "-b", f"deliveries-{V}",
                    "https://github.com/viniciushoscher-ctrl/growing-up-america", str(D)], check=True)
dv = D / "deliveries" / V
sj = json.load(open(f"videos/{V}/script.json"))
novela = V.startswith("ruth")

# thumbnail: archival photo, warm black and white, dark left side, big two-line text (1M+ nostalgia model)
img = sys.argv[6] if len(sys.argv) > 6 else "1_0.jpg"
im = Image.open(dv / img if (dv / img).exists() else dv / "media" / img).convert("RGB")
im = ImageOps.fit(im, (1280, 720), Image.LANCZOS)
g = ImageOps.grayscale(im)
im = ImageOps.colorize(ImageEnhance.Contrast(g).enhance(1.25), (20, 14, 8), (255, 240, 215))
shade = Image.linear_gradient("L").rotate(-90).resize((1280, 720))  # dark on the left
im = Image.composite(Image.new("RGB", im.size, (0, 0, 0)), im, shade.point(lambda p: int(p * 0.75)))
d = ImageDraw.Draw(im)
F = "/usr/share/fonts/opentype/inter/Inter-Black.otf"
def fit(text, maxw, start):
    s = start
    while ImageDraw.Draw(im).textlength(text, ImageFont.truetype(F, s)) > maxw:
        s -= 4
    return ImageFont.truetype(F, s)
y = 120
for text, col, size in ((L1, (255, 255, 255), 170), (L2, (255, 214, 0), 150)):
    f = fit(text, 760, size)
    d.text((48, y), text, font=f, fill=col, stroke_width=8, stroke_fill=(0, 0, 0))
    y += f.size + 30
tag = "GRANDMA RUTH'S STORY" if novela else "GRANDMA RUTH REMEMBERS"
f = ImageFont.truetype(F, 40)
w = d.textlength(tag, font=f)
d.rectangle((40, 600, 40 + w + 40, 664), fill=(200, 16, 30))
d.text((60, 606), tag, font=f, fill=(255, 255, 255))
(OUT / "thumbs").mkdir(parents=True, exist_ok=True)
im.save(OUT / "thumbs" / f"{V}.jpg", quality=90)

chapters = (dv / "chapters.txt").read_text().strip()
sources = pathlib.Path(f"videos/{V}/sources.md").read_text().strip()
first = sj["scenes"][0]["text"] if "text" in sj["scenes"][0] else ""
if novela:
    n = int(V[4:])
    intro = (f"Chapter {n} of Grandma Ruth's Story, the complete life of a girl born in Mansfield, Ohio, in 1944, "
             "told to her grandchildren Emma and Jack one chapter a night. Family secrets, betrayals and the America she lived through.\n\n"
             "New chapter every night at 9 PM Eastern. Watch the whole saga in order in the playlist.")
    tags = ["grandma ruth", "family saga", "life story", "1940s america", "world war 2 home front", "family secrets",
            "grandma stories", "american history", "storytime", "audio drama"]
else:
    intro = ("Grandma Ruth was born in 1944 in Mansfield, Ohio. Tonight she tells her grandchildren what it was really like, "
             "the good and the bad, with real prices, real events and the little things nobody writes down.\n\n"
             "New stories every day. Her life story continues every night at 9 PM Eastern in Grandma Ruth's Story.")
    tags = ["growing up in america", "1950s", "1960s", "nostalgia", "grandma stories", "life in the 1950s",
            "boomers", "american history", "the good old days", "vintage america"]
desc = (f"{intro}\n\nChapters\n{chapters}\n\n"
        "About this channel: Grandma Ruth is a fictional narrator. Her voice is synthetic and the family story is fiction, "
        "but the history, prices and events around it are real, and the photos and film are archival.\n\n"
        f"Sources\n{sources}\n\nArchival images and film: Prelinger Archives (public domain) and Wikimedia Commons (public domain or CC, see credits).\n\n"
        "#nostalgia #growingup #americanhistory")
(OUT / "queue").mkdir(exist_ok=True)
json.dump({"video": V, "source_branch": f"deliveries-{V}", "title": sj["title"], "description": desc[:4900],
           "tags": tags, "publishAt": AT, "playlist": PL}, open(OUT / "queue" / f"{V}.json", "w"), indent=1)
print("queued", V, AT, len(desc), "chars")
