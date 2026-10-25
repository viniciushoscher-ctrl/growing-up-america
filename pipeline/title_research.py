"""Read-only title research: which nostalgia videos get views, compared with their channel (outliers).
usage: title_research.py  (runs on the Actions runner; uses yt-dlp page listings only, no API key)
Outlier score = video views / median views of that channel's last 30 uploads. Also views / subscribers.
Writes research/titles/latest.json and latest.md."""
import datetime as dt, json, pathlib, statistics, subprocess, sys

QUERIES = [
    "growing up in the 1950s", "growing up in 1960s america", "growing up in the 1970s america",
    "if you turned 18 in", "if you were a teenager in 1965", "if you grew up in the 1960s",
    "life in the 1950s america", "what life was like in 1955", "things every 1960s kid did",
    "only baby boomers remember", "boomer nostalgia", "1950s america nostalgia documentary",
    "1960s america memories", "1970s nostalgia things we did", "american kitchen 1950s",
    "america in the 1950s what it was really like", "small town america 1950s", "1980s nostalgia america",
    "if you were born in the 1950s", "forgotten things from the 1960s",
]
OUT = pathlib.Path("research/titles")
MAX_CHANNELS = 150


def ytdlp(*args):
    r = subprocess.run(["yt-dlp", "--no-warnings", "--ignore-errors", *args], capture_output=True, text=True, timeout=600)
    return r.stdout


def main():
    vids = {}
    for q in QUERIES:
        for l in ytdlp("--flat-playlist", "-j", f"ytsearch50:{q}").splitlines():
            if not l.startswith("{"): continue
            e = json.loads(l)
            if e.get("id") and (e.get("duration") or 0) >= 300:
                vids.setdefault(e["id"], {"title": e.get("title"), "views": e.get("view_count") or 0,
                                          "minutes": round((e.get("duration") or 0) / 60), "channel": e.get("channel"),
                                          "channel_id": e.get("channel_id"), "url": f"https://www.youtube.com/watch?v={e['id']}", "query": q})
        print(q, len(vids), flush=True)
    # channel baseline: subscribers and median views of the latest uploads (page listing, no player requests)
    by_ch = {}
    for v in vids.values():
        if v["channel_id"]: by_ch[v["channel_id"]] = max(by_ch.get(v["channel_id"], 0), v["views"])
    chans = {}
    for cid in sorted(by_ch, key=lambda c: -by_ch[c])[:MAX_CHANNELS]:
        out = ytdlp("--flat-playlist", "-J", "--playlist-items", "1:30", f"https://www.youtube.com/channel/{cid}/videos")
        try: j = json.loads(out)
        except ValueError: continue
        views = [e.get("view_count") for e in j.get("entries") or [] if e.get("view_count")]
        chans[cid] = {"subs": j.get("channel_follower_count") or 0, "median": int(statistics.median(views)) if views else 0,
                      "recent": [{"title": e.get("title"), "views": e.get("view_count") or 0} for e in (j.get("entries") or [])[:30]]}
        print("channel", len(chans), j.get("channel"), chans[cid]["subs"], chans[cid]["median"], flush=True)
    rows = []
    for v in vids.values():
        c = chans.get(v["channel_id"])
        if not c: continue
        rows.append({**v, "subs": c["subs"], "channel_median": c["median"],
                     "outlier": round(v["views"] / c["median"], 1) if c["median"] else None,
                     "per_sub": round(v["views"] / c["subs"], 1) if c["subs"] else None})
    rows.sort(key=lambda r: -(r["outlier"] or 0))
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "latest.json").write_text(json.dumps({"videos": rows, "channels": chans}, indent=1, ensure_ascii=False))
    md = [f"# Nostalgia title research ({dt.date.today()}, {len(rows)} long videos, {len(chans)} channels)", "",
          "outlier = views ÷ median views of the channel's last 30 uploads · per sub = views ÷ subscribers", "",
          "| outlier | per sub | views | subs | channel median | min | channel | title |", "|---|---|---|---|---|---|---|---|"]
    for r in rows[:300]:
        md.append(f"| {r['outlier']} | {r['per_sub']} | {r['views']:,} | {r['subs']:,} | {r['channel_median']:,} | {r['minutes']} | "
                  f"{(r['channel'] or '').replace('|', '/')} | [{(r['title'] or '').replace('|', '/')}]({r['url']}) |")
    (OUT / "latest.md").write_text("\n".join(md) + "\n")
    print("done", len(rows))
    if not rows: sys.exit("no results (YouTube may be blocking the runner)")


if __name__ == "__main__":
    main()
