from PIL import Image, ImageDraw
import random, math, os
random.seed(7)
W,H = 1920,1080
OUT = "/tmp/claude-0/deckassets"

def lowpoly(path, seed, cols=13, rows=8, base=(17,17,17), spread=16, glow=(0.42,0.30), glowamt=26):
    random.seed(seed)
    img = Image.new("RGB",(W,H),base)
    d = ImageDraw.Draw(img)
    cw, ch = W/cols, H/rows
    pts = [[None]*(cols+1) for _ in range(rows+1)]
    for r in range(rows+1):
        for c in range(cols+1):
            jx = random.uniform(-0.42,0.42)*cw
            jy = random.uniform(-0.42,0.42)*ch
            x = c*cw + (0 if c in (0,cols) else jx)
            y = r*ch + (0 if r in (0,rows) else jy)
            pts[r][c] = (x,y)
    gx, gy = glow[0]*W, glow[1]*H
    maxd = math.hypot(W,H)*0.62
    def shade(tri):
        cx = sum(p[0] for p in tri)/3.0
        cy = sum(p[1] for p in tri)/3.0
        dist = math.hypot(cx-gx, cy-gy)
        g = max(0.0, 1.0 - dist/maxd)
        v = base[0] + g*glowamt + random.uniform(-spread*0.5, spread*0.5)
        v = max(6, min(58, v))
        # légère dominante neutre froide
        return (int(v), int(v), int(v*1.02))
    for r in range(rows):
        for c in range(cols):
            a,b,cc,dd = pts[r][c], pts[r][c+1], pts[r+1][c+1], pts[r+1][c]
            if (r+c) % 2 == 0:
                t1,t2 = (a,b,cc),(a,cc,dd)
            else:
                t1,t2 = (a,b,dd),(b,cc,dd)
            for t in (t1,t2):
                col = shade(t)
                d.polygon(t, fill=col, outline=col)
    img.save(path, optimize=True)
    return path

lowpoly(os.path.join(OUT,"bg.png"), 7)
lowpoly(os.path.join(OUT,"bg2.png"), 31, cols=11, rows=7, glow=(0.66,0.62), glowamt=20)

# logo : recadrage depuis 20.png (coin haut gauche)
src = Image.open("/tmp/claude-0/webisept/20.png").convert("RGB")
logo = src.crop((40,24,156,84)).resize((116*4,60*4), Image.LANCZOS)
logo.save(os.path.join(OUT,"logo.png"))

# photos propres réutilisables (sans texte incrusté)
for name, f in (("cardone","9.png"), ("meeting","30.png")):
    im = Image.open("/tmp/claude-0/webisept/%s" % f).convert("RGB").resize((1920,1080), Image.LANCZOS)
    im.save(os.path.join(OUT,"%s.jpg"%name), quality=88, optimize=True)

for f in sorted(os.listdir(OUT)):
    print(f, os.path.getsize(os.path.join(OUT,f)))
