"""Make 5 vertical Shorts from an ALREADY RENDERED long video (final mp4 with burned captions),
without re-rendering. Layout: the 16:9 video centred on a blurred copy of itself, so the captions
burned into the long video stay fully visible and in sync.
usage: shorts_from_final.py <final.mp4> <captions.srt> <chapters.txt> <outdir> """
import re, subprocess, sys, pathlib

MAX = 58.0


def tsec(x):
    h, m, s = x.replace(",", ".").split(":"); return int(h) * 3600 + int(m) * 60 + float(s)


def main(final, srt, chapters, outdir):
    cues = [(tsec(a), tsec(b)) for _, a, b, _ in re.findall(r"(\d+)\n(\S+) --> (\S+)\n(.*?)(?:\n\n|\Z)", pathlib.Path(srt).read_text(), re.S)]
    ch = []
    for line in pathlib.Path(chapters).read_text().splitlines():
        m = re.match(r"(\d+):(\d+) (.*)", line)
        if m: ch.append((int(m[1]) * 60 + int(m[2]), re.sub(r"^\d+\.\s*", "", m[3])))
    mid = [c for c in ch[1:-1]] or ch[1:]
    pick = [(0.0, "The Real Story")] + [mid[round(k * (len(mid) - 1) / 3)] for k in range(4)] if len(mid) >= 4 else [(0.0, "The Real Story")] + mid[:4]
    out = pathlib.Path(outdir); out.mkdir(parents=True, exist_ok=True)
    meta = []
    for n, (a, title) in enumerate(pick, 1):
        a = min(cues, key=lambda c: abs(c[0] - a))[0]                       # start exactly on a caption
        b = max((c[1] for c in cues if c[1] - a <= MAX and c[1] > a), default=a + MAX)  # end on a caption
        vf = ("[0:v]split[a][b];[a]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=30:5[bg];"
              "[b]scale=1080:-2[fg];[bg][fg]overlay=(W-w)/2:(H-h)/2,"
              "drawtext=text='AMERICA THAT WE LOVE':fontcolor=white:fontsize=64:borderw=4:bordercolor=black:"
              "box=1:boxcolor=0x8B4513@0.9:boxborderw=18:x=(w-text_w)/2:y=140[v]")
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-ss", f"{a:.2f}", "-t", f"{b-a:.2f}", "-i", final,
                        "-filter_complex", vf, "-map", "[v]", "-map", "0:a", "-c:v", "libx264", "-preset", "veryfast", "-crf", "26",
                        "-maxrate", "3000k", "-bufsize", "6000k", "-c:a", "aac", "-b:a", "96k", str(out / f"short{n}.mp4")], check=True)
        meta.append(f"short{n}.mp4 ({b-a:.0f}s)\nTitle: {title} #Shorts #nostalgia\n"
                    f"Description: {title}. Full video on the America That We Love channel.\n")
    (out / "shorts.md").write_text("\n".join(meta))
    print("shorts done", len(meta))


if __name__ == "__main__":
    main(*sys.argv[1:5])
