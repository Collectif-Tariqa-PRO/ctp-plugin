# -*- coding: utf-8 -*-
import re, os
from pptx import Presentation
from pptx.util import Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR

PX = Emu(6350)            # 1 px (base 1920) -> EMU  (1920px = 13.333in)
def px(v): return Emu(int(round(v * 6350)))
def pt(v): return Pt(v * 0.5)   # 1 px -> 0.5 pt

W, H = 1920, 1080
M = 128
GOLD  = RGBColor(0xE3, 0xA9, 0x4F)
GOLDD = RGBColor(0xB8, 0x86, 0x2B)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
DIM   = RGBColor(0xCF, 0xCF, 0xCF)
INK   = RGBColor(0x14, 0x14, 0x14)
BLACK = RGBColor(0x0E, 0x0E, 0x0E)

ARCH, OSW, POP, AR = "Archivo", "Oswald", "Poppins", "Noto Naskh Arabic"
ASSETS = "/tmp/claude-0/deckassets"

prs = Presentation()
prs.slide_width, prs.slide_height = px(W), px(H)
BLANK = prs.slide_layouts[6]

def newslide(bg="bg.png", notes=None):
    s = prs.slides.add_slide(BLANK)
    s.shapes.add_picture(os.path.join(ASSETS, bg), 0, 0, px(W), px(H))
    if notes:
        s.notes_slide.notes_text_frame.text = notes
    return s

def tb(s, x, y, w, h, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE):
    box = s.shapes.add_textbox(px(x), px(y), px(w), px(h))
    tf = box.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    tf.vertical_anchor = anchor
    return box, tf

def para(tf, text, font, size, color, bold=False, italic=False,
         align=PP_ALIGN.CENTER, space=0, lh=None, first=False):
    p = tf.paragraphs[0] if first else tf.add_paragraph()
    p.alignment = align
    if space: p.space_after = pt(space)
    if lh: p.line_spacing = lh
    r = p.add_run(); r.text = text
    f = r.font
    f.name, f.size, f.bold, f.italic = font, pt(size), bold, italic
    f.color.rgb = color
    return p

def grad_para(tf, text, size, first=False, align=PP_ALIGN.CENTER):
    """Dégradé noir -> or, caractère par caractère (reste éditable dans Canva)."""
    p = tf.paragraphs[0] if first else tf.add_paragraph()
    p.alignment = align
    p.line_spacing = 1.0
    n = max(1, len(text) - 1)
    a, b = (0x13, 0x13, 0x13), (0xB8, 0x86, 0x2B)
    for i, ch in enumerate(text):
        t = min(1.0, max(0.0, (i / n - 0.22) / 0.78))
        col = RGBColor(*[int(a[k] + (b[k] - a[k]) * t) for k in range(3)])
        r = p.add_run(); r.text = ch
        f = r.font
        f.name, f.size, f.bold, f.italic = ARCH, pt(size), True, True
        f.color.rgb = col
    return p

def rect(s, x, y, w, h, color):
    from pptx.enum.shapes import MSO_SHAPE
    sh = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, px(x), px(y), px(w), px(h))
    sh.fill.solid(); sh.fill.fore_color.rgb = color
    sh.line.fill.background()
    sh.shadow.inherit = False
    return sh

def is_ar(t): return bool(re.search(r"[؀-ۿ]", t))
def est_w(text, size, factor=0.56): return len(text) * size * factor

# ---------------------------------------------------------------- gabarits
def s_cover(notes):
    s = newslide("bg.png", notes)
    _, tf = tb(s, M, 150, W - 2*M, 190)
    para(tf, "MARHABA", POP, 36, WHITE, bold=True, italic=True, space=18, first=True)
    para(tf, "🕐 LE WEBINAIRE commence à 20h incha Allah !", POP, 31, WHITE, italic=True, space=8)
    para(tf, "🦊 N'oubliez pas de prendre des notes, vous risquez", POP, 31, WHITE, italic=True, space=0)
    para(tf, "d'apprendre des choses inchaAllah", POP, 31, WHITE, italic=True)
    bw = 1180
    rect(s, (W-bw)/2, 400, bw, 300, WHITE)
    _, tf2 = tb(s, (W-bw)/2 + 40, 408, bw - 80, 284)
    grad_para(tf2, "HÉRITAGE &", 118, first=True)
    grad_para(tf2, "MODERNITÉ", 118)
    _, tf3 = tb(s, M, 736, W - 2*M, 60)
    para(tf3, "Zaki Chairi  ·  Oussama Jammal  ·  24 septembre 2026", POP, 28, DIM, first=True)
    _, tf4 = tb(s, M, 880, W - 2*M, 110)
    para(tf4, "TARIQA PRO", ARCH, 40, GOLD, bold=True, first=True)
    return s

def s_titre(lines, notes):
    joined = " ".join(lines)
    if len(lines) == 1 and len(joined) <= 26:
        s = newslide("bg.png", notes)
        size = 132
        bw = min(W - 160, est_w(lines[0].upper(), size, 0.60) + 140)
        bh = size * 1.30
        rect(s, (W-bw)/2, (H-bh)/2, bw, bh, WHITE)
        _, tf = tb(s, (W-bw)/2 + 30, (H-bh)/2, bw - 60, bh)
        grad_para(tf, lines[0].upper(), size, first=True)
        return s
    s = newslide("bg.png", notes)
    size = 100 if len(joined) <= 42 else (78 if len(joined) <= 70 else 62)
    _, tf = tb(s, M, M, W - 2*M, H - 2*M)
    for i, ln in enumerate(lines):
        para(tf, ln.upper(), ARCH, size, WHITE, bold=True, italic=True, lh=1.06, first=(i == 0))
    return s

def s_partie(lines, notes):
    s = newslide("bg2.png", notes)
    _, tf = tb(s, M, 320, W - 2*M, 120, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.BOTTOM)
    para(tf, lines[0].upper(), POP, 34, GOLD, bold=True, align=PP_ALIGN.LEFT, first=True)
    rest = lines[1:] or lines
    _, tf2 = tb(s, M, 452, W - 2*M, 260, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP)
    for i, ln in enumerate(rest):
        para(tf2, ln.upper(), ARCH, 110, WHITE, bold=True, italic=True,
             align=PP_ALIGN.LEFT, lh=1.04, first=(i == 0))
    rect(s, M, 740, 300, 5, GOLD)
    return s

def s_punch(lines, notes):
    joined = " ".join(lines)
    s = newslide("bg.png", notes)
    if len(lines) == 1 and len(joined) <= 46:
        _, tf = tb(s, M, M, W - 2*M, H - 2*M)
        para(tf, lines[0].upper(), ARCH, 86, WHITE, bold=True, italic=True, lh=1.06, first=True)
        return s
    size = 52 if len(joined) <= 130 else 42
    _, tf = tb(s, M, M, W - 2*M, H - 2*M)
    for i, ln in enumerate(lines):
        col = GOLD if (i == len(lines) - 1 and len(lines) > 1) else WHITE
        para(tf, ln, POP, size, col, lh=1.34, space=18, first=(i == 0))
    return s

def s_citation(lines, notes):
    s = newslide("bg.png", notes)
    ar = [l for l in lines if is_ar(l)]
    rest = [l for l in lines if not is_ar(l)]
    quote, src = (rest[:-1], rest[-1]) if len(rest) > 1 else (rest, "")
    q = " ".join(quote)
    size = 60 if len(q) <= 110 else (48 if len(q) <= 200 else 38)
    _, tf = tb(s, M, M, W - 2*M, H - 2*M)
    para(tf, q.upper(), OSW, size, WHITE, bold=True, lh=1.18, space=30, first=True)
    if src:
        para(tf, "— %s —" % src.replace(" — ", " · "), POP, 28, GOLD, italic=True, space=34)
    for a in ar:
        para(tf, a, AR, 46, WHITE, lh=1.7, space=10)
    return s

def s_liste(lines, notes):
    s = newslide("bg.png", notes)
    title, items = lines[0], lines[1:]
    n = max(1, len(items))
    size = 37 if n <= 4 else (32 if n <= 6 else 28)
    _, tf = tb(s, M, M, W - 2*M, 110, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP)
    para(tf, title.upper(), ARCH, 40, WHITE, bold=True, italic=True,
         align=PP_ALIGN.LEFT, lh=1.14, first=True)
    rect(s, M, 296, 180, 4, GOLD)
    _, tf2 = tb(s, M, 350, W - 2*M, H - 350 - M, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP)
    for i, it in enumerate(items):
        col = GOLD if it.startswith(("👉", "✅", "1️⃣", "2️⃣", "3️⃣")) else WHITE
        if it.startswith("❌"): col = DIM
        para(tf2, it, POP, size, col, align=PP_ALIGN.LEFT, lh=1.42,
             space=18 if n <= 5 else 12, first=(i == 0))
    return s

def s_lundi(lines, notes):
    s = newslide("bg2.png", notes)
    title, items = lines[0], lines[1:]
    lw = est_w(title.upper(), 34, 0.62) + 68
    rect(s, M, 260, lw, 80, GOLD)
    _, tf = tb(s, M + 34, 260, lw - 68, 80, align=PP_ALIGN.LEFT)
    para(tf, title.upper(), ARCH, 34, INK, bold=True, italic=True, align=PP_ALIGN.LEFT, first=True)
    rect(s, M, 420, 5, 340, GOLD)
    _, tf2 = tb(s, M + 46, 420, W - 2*M - 46, 340, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP)
    for i, it in enumerate(items):
        para(tf2, it, POP, 37, WHITE, align=PP_ALIGN.LEFT, lh=1.42, space=24, first=(i == 0))
    return s

def s_vs(d, notes):
    s = newslide("bg.png", notes)
    colw = 810
    for side, (t, items, col, x) in enumerate((
            (d["lt"], d["li"], WHITE, M),
            (d["rt"], d["ri"], GOLD, W - M - colw))):
        _, tf = tb(s, x, 240, colw, 130, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.BOTTOM)
        para(tf, t.upper(), OSW, 44, col, bold=True, align=PP_ALIGN.LEFT, lh=1.12, first=True)
        rect(s, x, 392, 110, 4, col)
        _, tf2 = tb(s, x, 440, colw, 420, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP)
        for i, it in enumerate(items):
            para(tf2, it, POP, 30, DIM, align=PP_ALIGN.LEFT, lh=1.4, space=16, first=(i == 0))
    _, tfv = tb(s, (W - 160)/2, 480, 160, 120)
    para(tfv, d.get("sep", "VS"), ARCH, 70, WHITE, bold=True, italic=True, first=True)
    return s

def s_whatsapp(notes):
    s = newslide("bg.png", notes)
    s.shapes.add_picture("/tmp/claude-0/-home-user-ctp-plugin/5bde7487-de28-5f85-acc6-6f6c831c1436/scratchpad/qr/qr-whatsapp-panneau-blanc.png",
                         px(M), px(230), px(620), px(620))
    x = M + 620 + 76
    w = W - M - x
    _, tf = tb(s, x, 210, w, 150, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.BOTTOM)
    para(tf, "REJOIGNEZ LE GROUPE", ARCH, 58, WHITE, bold=True, italic=True, align=PP_ALIGN.LEFT, lh=1.1, first=True)
    para(tf, "WHATSAPP DU LIVE", ARCH, 58, WHITE, bold=True, italic=True, align=PP_ALIGN.LEFT, lh=1.1)
    rect(s, x, 392, 180, 4, GOLD)
    _, tf2 = tb(s, x, 440, w, 420, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP)
    para(tf2, "C'est là qu'on va :", POP, 32, GOLD, align=PP_ALIGN.LEFT, space=18, first=True)
    for it in ("🎁 partager des cadeaux exclusifs",
               "📚 envoyer les ressources mentionnées",
               "🎯 vous aider à passer à l'action après le webinaire",
               "🤝 garder le lien avec le Collectif"):
        para(tf2, it, POP, 33, WHITE, align=PP_ALIGN.LEFT, lh=1.45, space=12)
    para(tf2, "Le webinaire se termine… mais l'accompagnement continue là-bas.",
         POP, 29, DIM, align=PP_ALIGN.LEFT, lh=1.45, space=0)
    return s


# ---------------------------------------------------------------- VS data
def vskey(lines):
    return re.split(r"\s{3,}", lines[0].strip())[0].strip().lower()

VS = {
 "le filtre": dict(lt="Le filtre", li=["Il regarde un acte, un seul","Licite ? on garde. Illicite ? on jette",
        "Nécessaire — rien ici ne vise à l'affaiblir","Mais il ne touche jamais au cadre"],
      rt="Le paradigme", ri=["Il produit les actes","Une logique génère des actes indéfiniment",
        "On en filtre un, puis dix, puis cent","La logique, elle, continue"], sep="VS"),
 "orienté résultat": dict(lt="Orienté résultat", li=["Tu as gagné quand le virement est arrivé",
        "Le chemin est un coût qu'on minimise","Chaque vente incertaine devient une angoisse",
        "Un mois creux remet en cause ta valeur"],
      rt="Orienté commandement", ri=["Tu dis le défaut en premier","L'acheteur part ? Tu n'as pas raté ta vente —",
        "tu as réussi ton commandement","Fais les causes. Le résultat appartient à Dieu."], sep="VS"),
 "logique de marge": dict(lt="Logique de marge", li=["Extraire le maximum de chaque transaction",
        "Le dernier euro laissé sur la table est une perte","Un rapport de force dont on sort gagnant ou perdant"],
      rt="Logique de circulation", ri=["La bénédiction est dans l'échange, pas dans la marge",
        "Ce qui tourne est béni","On laisse volontairement — non par faiblesse, par principe"], sep="VS"),
 "ce qui est interdit depuis 14 siècles": dict(lt="Interdit depuis 14 siècles", li=["Vendre par-dessus la vente de son frère",
        "Le najsh : faire monter une enchère sans vouloir acheter",
        "Intercepter les caravanes avant le marché",
        "Profiter de ce que le vendeur ignore des prix"],
      rt="Ce que ça donne en 2026", ri=["Intervenir quand une vente est sur le point de se conclure",
        "Le concurrent imaginaire invoqué en négociation",
        "L'achat opportuniste à qui ignore la valeur de son bien",
        "La fausse file d'attente, « il ne reste qu'une place »"], sep="→"),
 "la cible": dict(lt="La cible", li=["Panier moyen, valeur vie client, taux de rétention",
        "Le vocabulaire est explicite : tunnel, accroche, capture",
        "Reed Hastings : « notre concurrent, c'est le sommeil »"],
      rt="Celui dont tu réponds", ri=["Refus du rapport de dépendance",
        "La vente = aider quelqu'un à décider utile pour lui",
        "Un accompagnement réussi rend autonome"], sep="VS"),
 "le premier": dict(lt="Le premier", li=["Entré dans la philosophie grecque sans cadre",
        "« Il est rentré dans le ventre des philosophes,","il a voulu en sortir, il n'a pas réussi »"],
      rt="Al-Ghazâlî", ri=["Entré avec un cadre déjà constitué","Il a pris ce qui était utile",
        "Il l'a détaché de sa structure d'origine","Il l'a réintégré dans la sienne"], sep="VS"),
 "ce qu'on jette": dict(lt="Ce qu'on jette", li=["Le compte à rebours truqué","Le faux prix barré","Le chantage à la rareté",
        "Le concurrent inventé","L'upsell au pic émotionnel"],
      rt="Ce qui le remplace", ri=["L'urgence réelle, dite comme elle est","L'ancrage de valeur sincère",
        "La garantie qu'on peut tenir","Ta preuve réelle, même plus petite",
        "Le même message, trois jours plus tard"], sep="VS"),
 "où on va chercher": dict(lt="Où on va chercher", li=["Elon Musk","Alex Hormozi","Un podcast américain",
        "Des méthodes qui ont dix ans"],
      rt="Ce qu'on a chez nous", ri=["ʿAbd ar-Rahmān ibn ʿAwf","ʿUthmān ibn ʿAffān",
        "Quatorze siècles de fiqh al-muʿāmalāt","Une bibliothèque qu'on n'a pas ouverte"], sep="→"),
 "ce qu'on a enlevé": dict(lt="Ce qu'on a enlevé", li=["La loi d'attraction","Le vocabulaire ésotérique",
        "La visualisation créatrice","On a ajouté bismillah en ouverture"],
      rt="Ce qui n'a pas bougé", ri=["Tout est organisé autour d'un seul centre : toi",
        "Tu es un projet inachevé","Ta responsabilité est de te perfectionner",
        "Le sens se trouve à l'intérieur de toi"], sep="→"),
 "l'expertise métier": dict(lt="L'expertise métier", li=["Elle est propre à ton métier",
        "Le couscous, le béton, le code","C'est souvent ce que tu maîtrises le mieux",
        "Elle ne suffit jamais à elle seule"],
      rt="Les compétences transversales", ri=["Elles servent quel que soit le métier",
        "Vendre, se faire connaître, décider","C'est presque toujours ce qui bloque",
        "Elles ne dépendent d'aucun secteur"], sep="→"),
 "éteindre son cerveau": dict(lt="Éteindre son cerveau", li=["Tu demandes quoi penser",
        "Tu ne sais plus pourquoi tu fais ce que tu fais",
        "Ton jugement se déplace dans la machine","C'est le levier de l'aveuglement"],
      rt="Augmenter sa portée", ri=["Tu sais ce que tu veux dire",
        "Elle te fait aller dix fois plus vite pour le dire",
        "Ton jugement reste chez toi","C'est le levier de l'impact"], sep="→"),
}

def photo_of(lines):
    t = lines[0].upper()
    if "JAMAIS CHANGÉ" in t: return "cardone"
    if "IL ÉTAIT D'ACCORD" in t: return "meeting"
    return "bg"

def is_whatsapp(lines):
    return "whatsapp" in lines[0].lower()

# ---------------------------------------------------------------- build
import html as _h
text = open("/tmp/claude-0/webi/script.md").read()
count = 0
for m in re.finditer(r"SLIDE (\d+) — \[([A-ZÉ]+)\]\n(.*?)(?=\nSLIDE \d+ — \[|\n═|\Z)", text, re.S):
    n, typ, body = int(m.group(1)), m.group(2), m.group(3)
    note = ""
    mm = re.search(r"^À L'ORAL\s*:\s*", body, re.M)
    if mm:
        note = " ".join(body[mm.end():].split()); body = body[:mm.start()]
    lines = [l.rstrip() for l in body.strip("\n").split("\n") if l.strip()]
    if typ == "REPRISE":
        note = (note + "  ·  " if note else "") + "Slide déjà existante dans tes decks — tu peux reprendre la tienne."
    if is_whatsapp(lines):
        s_whatsapp(note or "Scanner le QR à l'écran.")
        count += 1
        continue
    if n == 1:
        s_cover("Slide d'attente et d'ouverture. " + note)
    elif typ == "PARTIE":      s_partie(lines, note)
    elif typ == "TITRE":       s_titre(lines, note)
    elif typ == "PUNCHLINE":   s_punch(lines, note)
    elif typ == "CITATION":    s_citation(lines, note)
    elif typ == "LUNDI":       s_lundi(lines, note)
    elif typ == "VS":          s_vs(VS[vskey(lines)], note)
    elif typ in ("LISTE", "REPRISE"):
        (s_liste if len(lines) > 1 else s_titre)(lines, note)
    else:                      s_punch(lines, note)
    count += 1

out = "/tmp/claude-0/-home-user-ctp-plugin/5bde7487-de28-5f85-acc6-6f6c831c1436/scratchpad/art/Heritage-Modernite-webinaire.pptx"
prs.save(out)
print(count, "slides ->", out, os.path.getsize(out), "octets")
