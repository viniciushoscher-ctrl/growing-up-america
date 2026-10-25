"""Read-only title research: which nostalgia videos get views, and how big the channel is (outliers = views far above subscribers).
usage: title_research.py  (runs on the Actions runner; uses yt-dlp, no API key)
Writes research/titles/latest.json and latest.md."""
import datetime as dt, json, pathlib, subprocess, sys

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


def ytdlp(*args):
    r = subprocess.run(["yt-dlp", "--no-warnings", "--ignore-errors", *args], capture_output=True, text=True, timeout=1800)
    return [json.loads(l) for l in r.stdout.splitlines() if l.startswith("{")]


def main():
    seen = {}
    for q in QUERIES:
        for e in ytdlp("--flat-playlist", "-j", f"ytsearch40:{q}"):
            if e.get("id") and (e.get("duration") or 0) >= 300:  # long videos only
                seen.setdefault(e["id"], q)
        print(q, len(seen), flush=True)
    rows = []
    ids = list(seen)
    for i in range(0, len(ids), 25):
        batch = [f"https://www.youtube.com/watch?v={v}" for v in ids[i:i + 25]]
        for v in ytdlp("-j", "--skip-download", *batch):
            up = v.get("upload_date")
            age = (dt.date.today() - dt.date(int(up[:4]), int(up[4:6]), int(up[6:]))).days if up else None
            views, subs = v.get("view_count") or 0, v.get("channel_follower_count") or 0
            rows.append({"title": v.get("title"), "url": v.get("webpage_url"), "channel": v.get("channel"),
                         "subs": subs, "views": views, "ratio": round(views / subs, 1) if subs else None,
                         "age_days": age, "views_per_day": int(views / max(age or 1, 1)),
                         "minutes": round((v.get("duration") or 0) / 60), "query": seen[v["id"]]})
        print("details", len(rows), flush=True)
    rows.sort(key=lambda r: -(r["ratio"] or 0))
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "latest.json").write_text(json.dumps(rows, indent=1, ensure_ascii=False))
    md = [f"# Nostalgia title research ({dt.date.today()}, {len(rows)} long videos)", "",
          "Sorted by views ÷ subscribers (outliers first).", "",
          "| views/subs | views | subs | age (d) | views/day | min | channel | title |", "|---|---|---|---|---|---|---|---|"]
    for r in rows[:250]:
        md.append(f"| {r['ratio']} | {r['views']:,} | {r['subs']:,} | {r['age_days']} | {r['views_per_day']:,} | {r['minutes']} | "
                  f"{(r['channel'] or '').replace('|', '/')} | [{(r['title'] or '').replace('|', '/')}]({r['url']}) |")
    (OUT / "latest.md").write_text("\n".join(md) + "\n")
    print("done", len(rows))
    if not rows: sys.exit("no results (YouTube may be blocking the runner)")


if __name__ == "__main__":
    main()
