"""Tiny helper for phase-2 make_script.py files: sc() adds a scene, ch() marks the next scene as a chapter
start, save() writes script.json + sources.md next to the calling script and prints the estimated length."""
import json, pathlib, sys

S, _next = [], [None]
SCALE = 1.45


def ch(name):
    _next[0] = name


def sc(text, query, caption, cuts=3, **extra):
    """extra keys go straight into the scene, e.g. modern=True lets fetch_media use a recent photo (a dead mall)."""
    s = {"text": " ".join(text.split()), "query": query, "caption": caption, "cuts": cuts, **extra}
    if _next[0]:
        s["chapter"] = _next[0]; _next[0] = None
    S.append(s)


def save(vid, title, sources, angle, minutes=(20.2, 60), voice=None):
    """minutes: allowed estimated length. Channels without phone verification cap uploads at 15 min, so short
    videos use minutes=(12, 14.5): renders came out about 7% shorter than this estimate (video01: 32.5 est, 30.2 real)."""
    d = pathlib.Path(sys.argv[0]).resolve().parent
    if S and "chapter" not in S[0]:
        S[0]["chapter"] = "Intro"
    for i, c in enumerate((8, 8, 5)):
        if i < len(S): S[i]["cuts"] = c
    json.dump({"id": vid, "angle": angle, "length_scale": SCALE, "title": title, "scenes": S, **({"voice": voice} if voice else {})},
              open(d / "script.json", "w"), indent=1)
    (d / "sources.md").write_text("".join(f"- {s}\n" for s in sources))
    words = sum(len(s["text"].split()) for s in S)
    mins = round(words * SCALE / 212, 1)
    print(vid, len(S), "scenes", words, "words", mins, "min")
    if not minutes[0] <= mins <= minutes[1]:  # keep the estimate conservative
        raise SystemExit(f"{vid}: {mins} min is outside {minutes[0]}-{minutes[1]} min")
