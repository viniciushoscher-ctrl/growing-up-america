"""Thumbnail in the 1M+ model: archival photo with big text on the left, Grandma Ruth's face on the right.
python grandma/ruth_thumb.py <out.jpg> <archival photo> <line 1> <line 2> <ruth photo> <tag>"""
import sys
from PIL import Image, ImageDraw, ImageEnhance, ImageFont, ImageOps

out, arch, L1, L2, ruth, tag = sys.argv[1:7]
W, H = 1280, 720
bg = ImageOps.fit(Image.open(arch).convert("RGB"), (W, H))
bg = ImageOps.colorize(ImageEnhance.Contrast(ImageOps.grayscale(bg)).enhance(1.2), (18, 12, 8), (250, 236, 210))
bg = ImageEnhance.Brightness(bg).enhance(0.55)
r = Image.open(ruth).convert("RGB")
rw = 620
box = (120, 280, 640, 884) if r.height > 1300 else (190, 250, 700, 842)  # tight on her face (ruth-retrato / ruth-contando)
r = r.crop(box).resize((rw, H), Image.LANCZOS)
r = ImageEnhance.Contrast(r).enhance(1.08)
mask = Image.linear_gradient("L").rotate(-90).resize((rw, H)).point(lambda p: min(255, p * 3))  # fade in from the left
bg.paste(r, (W - rw, 0), mask)
d = ImageDraw.Draw(bg)
F = "/usr/share/fonts/opentype/inter/Inter-Black.otf"
def fit(t, maxw, s):
    while d.textlength(t, font=ImageFont.truetype(F, s)) > maxw:
        s -= 4
    return ImageFont.truetype(F, s)
y = 150
for t, col, s in ((L1, (255, 255, 255), 160), (L2, (255, 214, 0), 140)):
    f = fit(t, 650, s)
    d.text((44, y), t, font=f, fill=col, stroke_width=8, stroke_fill=(0, 0, 0))
    y += f.size + 28
f = ImageFont.truetype(F, 38)
d.rectangle((36, 606, 36 + d.textlength(tag, font=f) + 40, 668), fill=(200, 16, 30))
d.text((56, 612), tag, font=f, fill=(255, 255, 255))
bg.save(out, quality=92)
