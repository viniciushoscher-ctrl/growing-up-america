"""Upload and schedule America That We Love videos on YouTube following agendamento/calendar.json.
usage: yt_upload.py check | status | upload
Secrets: YT_CLIENT_ID, YT_CLIENT_SECRET, YT_REFRESH_TOKEN. Optional: YT_BUDGET (quota units per run), YT_SHORTS=1.
calendar.json: [{"date": "2026-11-03", "longs": [1, 2, 3], "shorts": [[1, 1], [2, 1]]}, ...]"""
import datetime as dt, json, os, subprocess, sys, pathlib, requests
from zoneinfo import ZoneInfo

STATE = pathlib.Path("agendamento/youtube-state.json")
COST_UPLOAD, COST_THUMB = 1600, 50
# New York time, so daylight saving is handled: three longs a day (morning, afternoon, evening), Shorts in between
NY = ZoneInfo("America/New_York")
LONG_SLOTS = [(9, 0), (14, 0), (19, 0)]
SHORT_SLOTS = [(12, 0), (17, 0), (21, 0)]


def token():
    r = requests.post("https://oauth2.googleapis.com/token", data={
        "client_id": os.environ["YT_CLIENT_ID"].strip(), "client_secret": os.environ["YT_CLIENT_SECRET"].strip(),
        "refresh_token": os.environ["YT_REFRESH_TOKEN"].strip(), "grant_type": "refresh_token"}, timeout=30)
    if not r.ok:
        sys.exit(f"token refresh failed: {r.status_code} {r.text}")
    return r.json()["access_token"]


def at_ny(date, hm):
    d = dt.date.fromisoformat(date)
    return dt.datetime(d.year, d.month, d.day, hm[0], hm[1], tzinfo=NY).astimezone(dt.timezone.utc)


def queue():
    """Every upload in calendar order: (key, video, file, publishAt, title, description, is_long)."""
    for day in json.load(open("agendamento/calendar.json")):
        for slot, v in enumerate(day.get("longs", [])):
            m = json.load(open(f"agendamento/meta/video{v:02d}.json"))
            yield f"v{v:02d}", v, f"video{v:02d}.mp4", at_ny(day["date"], LONG_SLOTS[slot]), m["title"], m["description"], True
        for slot, (v, s) in enumerate(day.get("shorts", [])):
            m = json.load(open(f"agendamento/meta/video{v:02d}.json"))
            sm = next((x for x in m["shorts"] if x["file"] == f"short{s}.mp4"), None)
            if sm:
                yield f"v{v:02d}-s{s}", v, sm["file"], at_ny(day["date"], SHORT_SLOTS[slot]), sm["title"], sm["description"], False


def upload(tok, path, title, desc, tags, at):
    body = {"snippet": {"title": title, "description": desc, "tags": tags, "categoryId": "27",
                        "defaultLanguage": "en", "defaultAudioLanguage": "en"},
            "status": {"privacyStatus": "private", "publishAt": at.strftime("%Y-%m-%dT%H:%M:%SZ"),
                       "selfDeclaredMadeForKids": False, "embeddable": True}}
    h = {"Authorization": f"Bearer {tok}", "X-Upload-Content-Type": "video/mp4",
         "X-Upload-Content-Length": str(path.stat().st_size)}
    r = requests.post("https://www.googleapis.com/upload/youtube/v3/videos?uploadType=resumable&part=snippet,status",
                      headers=h, json=body, timeout=60)
    if r.status_code == 403 and "quota" in r.text.lower(): return "QUOTA"
    r.raise_for_status()
    with open(path, "rb") as f:
        u = requests.put(r.headers["Location"], data=f, headers={"Authorization": f"Bearer {tok}", "Content-Type": "video/mp4"}, timeout=3600)
    u.raise_for_status(); return u.json()["id"]


def main(mode):
    tok = token()
    if mode == "check":
        r = requests.get("https://www.googleapis.com/youtube/v3/channels?part=snippet,status&mine=true",
                         headers={"Authorization": f"Bearer {tok}"}, timeout=30); r.raise_for_status()
        for c in r.json().get("items", []): print("channel:", c["snippet"]["title"], c["id"], c.get("status", {}))
        return
    if mode == "status":
        ids = [x["id"] for x in json.loads(STATE.read_text()).values() if "id" in x]
        for i in range(0, len(ids), 50):
            r = requests.get("https://www.googleapis.com/youtube/v3/videos", params={"part": "status", "id": ",".join(ids[i:i + 50])},
                             headers={"Authorization": f"Bearer {tok}"}, timeout=30); r.raise_for_status()
            for v in r.json()["items"]:
                st = v["status"]; print(v["id"], st["uploadStatus"], st["privacyStatus"], st.get("publishAt", "-"), st.get("rejectionReason", ""), st.get("failureReason", ""))
        return
    state = json.loads(STATE.read_text()) if STATE.exists() else {}
    budget = int(os.environ.get("YT_BUDGET") or 9900)
    now = dt.datetime.now(dt.timezone.utc); dl = pathlib.Path("/tmp/dl"); dl.mkdir(exist_ok=True)
    for key, v, fname, at, title, desc, is_long in queue():
        if key in state: continue
        if not is_long and os.environ.get("YT_SHORTS") != "1": continue  # Shorts are scheduled by hand
        if at < now + dt.timedelta(hours=2):
            print("skip (slot already passed):", key, at); state[key] = {"skipped": "slot passed"}; continue
        if budget < COST_UPLOAD + (COST_THUMB if is_long else 0): break
        f = dl / f"{v:02d}-{fname}"
        if not f.exists():
            subprocess.run(["gh", "release", "download", f"video{v:02d}", "-p", fname, "-O", str(f), "--clobber"], check=True)
        tags = json.load(open(f"agendamento/meta/video{v:02d}.json"))["tags"] + ([] if is_long else ["Shorts"])
        vid = upload(tok, f, title, desc, tags, at)
        if vid == "QUOTA": print("quota exhausted"); break
        budget -= COST_UPLOAD; state[key] = {"id": vid, "publishAt": at.isoformat()}
        print("uploaded", key, vid, "publishes", at.isoformat())
        thumb = pathlib.Path(f"agendamento/thumbs/video{v:02d}.jpg")
        if is_long and thumb.exists():
            t = requests.post(f"https://www.googleapis.com/upload/youtube/v3/thumbnails/set?videoId={vid}",
                              headers={"Authorization": f"Bearer {tok}", "Content-Type": "image/jpeg"}, data=thumb.read_bytes(), timeout=120)
            print("thumbnail", t.status_code, t.text[:200]); budget -= COST_THUMB
        f.unlink(missing_ok=True)
        STATE.write_text(json.dumps(state, indent=1))
    STATE.write_text(json.dumps(state, indent=1))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "check")
