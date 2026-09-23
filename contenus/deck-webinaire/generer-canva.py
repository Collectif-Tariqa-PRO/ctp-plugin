# -*- coding: utf-8 -*-
import re, os, json, html

ROOT = "/tmp/claude-0/-home-user-ctp-plugin/5bde7487-de28-5f85-acc6-6f6c831c1436/scratchpad/deck2"
SL = os.path.join(ROOT, "project", "slides")
os.makedirs(SL, exist_ok=True)

BLOB = json.load(open("/tmp/claude-0/blobs.json")) if os.path.exists("/tmp/claude-0/blobs.json") else {}

GOLD="#E3A94F"; GOLD_D="#B8862B"; W="#FFFFFF"; DIM="#CFCFCF"; BG="#0E0E0E"
ARCH="'Archivo', Arial, sans-serif"
OSW="'Oswald', Arial, sans-serif"
POP="'Poppins', Arial, sans-serif"
AR="'Noto Naskh Arabic', Georgia, serif"

def bg(which="bg"):
    u = BLOB.get(which, "")
    out = ('  <img src="%s" alt="" style="position:absolute; left:0px; top:0px; '
           'width:1920px; height:1080px; object-fit:cover">' % u)
    if which in SCRIM:
        out += ('\n  <div style="position:absolute; left:0px; top:0px; width:1920px; height:1080px; '
                'background:linear-gradient(90deg, #000000 0%, #000000 48%, rgba(0,0,0,0.30) 100%); '
                'opacity:0.88"></div>')
    return out

def scrim(op=0.55, col="#000000"):
    return ('  <div style="position:absolute; left:0px; top:0px; width:1920px; height:1080px; '
            'background:%s; opacity:%s"></div>' % (col, op))

def logo(left=128, top=76, size=1.0):
    s = size
    return ('  <div style="position:absolute; left:%dpx; top:%dpx; width:360px; display:flex; '
            'align-items:center; gap:%dpx">\n'
            '    <svg aria-label="Logo Tariqa PRO" width="%d" height="%d" viewBox="0 0 40 52">'
            '<path d="M4 3 H36 M4 49 H36 M6 4 L34 48 M34 4 L6 48" fill="none" stroke="%s" stroke-width="3.2"/></svg>\n'
            '    <div style="display:flex; flex-direction:column">\n'
            '      <p style="font-family:%s; font-size:%dpx; font-weight:700; line-height:1.02; color:%s; letter-spacing:1px">TARIQA</p>\n'
            '      <p style="font-family:%s; font-size:%dpx; font-weight:700; line-height:1.02; color:%s; letter-spacing:1px">PRO</p>\n'
            '    </div>\n  </div>' % (left, top, int(14*s), int(40*s), int(52*s), GOLD,
                                      ARCH, int(34*s), GOLD, ARCH, int(34*s), GOLD))

def sec(sid, inner, notes=None, extra="", trans="fade"):
    a = ("\n  <aside>%s</aside>" % notes) if notes else ""
    style = ("background:%s; color:%s; font-family:%s; padding:128px; %s" % (BG, W, POP, extra))
    return '<section id="%s" data-transition="%s" style="%s">\n%s%s\n</section>' % (sid, trans, style, inner, a)

CENTER = "display:flex; flex-direction:column; justify-content:center; align-items:center; gap:40px"
TOPLEFT = "display:flex; flex-direction:column; gap:34px"

def is_ar(t): return bool(re.search(r"[؀-ۿ]", t))

# ---------------------------------------------------------------- gabarits
def g_titre(sid, lines, notes, which="bg"):
    joined = " ".join(lines)
    if len(lines) == 1 and len(joined) <= 26:
        inner = (bg(which) + "\n" +
                 '  <div style="background:#FFFFFF; padding:26px 58px">\n'
                 '    <h1 style="font-family:%s; font-size:140px; font-weight:900; font-style:italic; '
                 'text-transform:uppercase; line-height:1.02; text-align:center; '
                 'background:linear-gradient(90deg, #131313 0%%, #1E1E1E 34%%, %s 100%%); '
                 'background-clip:text; -webkit-text-fill-color:transparent">%s</h1>\n  </div>'
                 % (ARCH, GOLD_D, lines[0]))
    else:
        size = 104 if len(joined) <= 42 else (82 if len(joined) <= 70 else 64)
        body = "<br>".join(lines)
        inner = (bg(which) + "\n" +
                 '  <h1 style="font-family:%s; font-size:%dpx; font-weight:900; font-style:italic; '
                 'text-transform:uppercase; line-height:1.06; text-align:center; color:%s">%s</h1>'
                 % (ARCH, size, W, body))
    return sec(sid, inner, notes, CENTER)

def g_partie(sid, lines, notes):
    num = lines[0] if lines else ""
    rest = lines[1:] if len(lines) > 1 else []
    inner = (bg("bg2") + "\n" +
             '  <div style="flex:1"></div>\n'
             '  <p style="font-family:%s; font-size:34px; font-weight:600; letter-spacing:7px; '
             'text-transform:uppercase; color:%s">%s</p>\n'
             '  <h1 style="font-family:%s; font-size:118px; font-weight:900; font-style:italic; '
             'text-transform:uppercase; line-height:1.04; color:%s">%s</h1>\n'
             '  <div style="width:300px; height:5px; background:%s"></div>\n'
             '  <div style="flex:1"></div>'
             % (POP, GOLD, num, ARCH, W, "<br>".join(rest) or num, GOLD))
    return sec(sid, inner, notes, "display:flex; flex-direction:column; justify-content:center; gap:26px", trans="push")

def g_punch(sid, lines, notes, which="bg"):
    joined = " ".join(lines)
    if len(lines) == 1 and len(joined) <= 46:
        inner = (bg(which) + "\n" +
                 '  <h2 style="font-family:%s; font-size:88px; font-weight:900; font-style:italic; '
                 'text-transform:uppercase; line-height:1.06; text-align:center; color:%s">%s</h2>'
                 % (ARCH, W, lines[0]))
        return sec(sid, inner, notes, CENTER)
    size = 54 if len(joined) <= 130 else 44
    rows = []
    for k, ln in enumerate(lines):
        col = GOLD if k == len(lines) - 1 and len(lines) > 1 else W
        rows.append('  <p style="font-family:%s; font-size:%dpx; font-weight:400; line-height:1.34; '
                    'text-align:center; color:%s">%s</p>' % (POP, size, col, ln))
    inner = bg(which) + "\n" + "\n".join(rows)
    return sec(sid, inner, notes, CENTER)

def g_citation(sid, lines, notes):
    ar = [l for l in lines if is_ar(l)]
    rest = [l for l in lines if not is_ar(l)]
    quote, src = rest[:-1], (rest[-1] if len(rest) > 1 else "")
    if len(rest) == 1: quote, src = rest, ""
    q = " ".join(quote)
    size = 62 if len(q) <= 110 else (50 if len(q) <= 200 else 40)
    inner = [bg("bg")]
    inner.append('  <p style="font-family:%s; font-size:%dpx; font-weight:500; text-transform:uppercase; '
                 'line-height:1.18; text-align:center; color:%s">%s</p>' % (OSW, size, W, q))
    if src:
        inner.append('  <p style="font-family:%s; font-size:28px; font-style:italic; text-align:center; '
                     'color:%s">— %s —</p>' % (POP, GOLD, src))
    for a in ar:
        inner.append('  <p style="font-family:%s; font-size:48px; line-height:1.9; text-align:center; '
                     'color:%s">%s</p>' % (AR, W, a))
    return sec(sid, "\n".join(inner), notes, CENTER)

def g_liste(sid, lines, notes, which="bg"):
    title = lines[0]
    items = lines[1:]
    n = max(1, len(items))
    size = 38 if n <= 4 else (33 if n <= 6 else 29)
    rows = []
    for it in items:
        col = GOLD if it.startswith(("👉", "✅", "1️⃣", "2️⃣", "3️⃣")) else W
        if it.startswith("❌"): col = DIM
        rows.append('    <p style="font-family:%s; font-size:%dpx; font-weight:400; line-height:1.42; '
                    'color:%s">%s</p>' % (POP, size, col, it))
    inner = (bg(which) + "\n" +
             '  <p style="font-family:%s; font-size:40px; font-weight:900; font-style:italic; '
             'text-transform:uppercase; line-height:1.14; color:%s">%s</p>\n'
             '  <div style="width:180px; height:4px; background:%s"></div>\n'
             '  <div style="display:flex; flex-direction:column; gap:%dpx">\n%s\n  </div>'
             % (ARCH, W, title, GOLD, 20 if n <= 5 else 14, "\n".join(rows)))
    return sec(sid, inner, notes, TOPLEFT)

def g_lundi(sid, lines, notes):
    title = lines[0]
    items = lines[1:]
    rows = "\n".join('    <p style="font-family:%s; font-size:38px; line-height:1.42; color:%s">%s</p>'
                     % (POP, W, it) for it in items)
    inner = (bg("bg2") + "\n" +
             '  <div style="background:%s; padding:14px 34px">\n'
             '    <p style="font-family:%s; font-size:34px; font-weight:900; font-style:italic; '
             'text-transform:uppercase; color:#141414">%s</p>\n  </div>\n'
             '  <div style="display:flex; flex-direction:column; gap:26px; border-left:5px solid %s; '
             'padding:6px 0px 6px 40px">\n%s\n  </div>'
             % (GOLD, ARCH, title, GOLD, rows))
    return sec(sid, inner, notes, "display:flex; flex-direction:column; justify-content:center; align-items:flex-start; gap:44px")

def g_vs(sid, d, notes):
    def col(t, items, tc):
        li = "\n".join('      <p style="font-family:%s; font-size:31px; line-height:1.4; color:%s">%s</p>'
                       % (POP, DIM, x) for x in items)
        return ('    <div style="flex:1; display:flex; flex-direction:column; gap:16px">\n'
                '      <p style="font-family:%s; font-size:44px; font-weight:600; text-transform:uppercase; '
                'line-height:1.12; color:%s">%s</p>\n'
                '      <div style="width:110px; height:4px; background:%s"></div>\n%s\n    </div>'
                % (OSW, tc, t, tc, li))
    sep = ('    <div style="width:120px; display:flex; flex-direction:column; justify-content:center; align-items:center">\n'
           '      <p style="font-family:%s; font-size:72px; font-weight:900; font-style:italic; color:%s">%s</p>\n'
           '    </div>' % (ARCH, W, d.get("sep", "VS")))
    inner = (bg("bg") + "\n" +
             '  <div style="display:flex; gap:20px; align-items:stretch">\n'
             + col(d["lt"], d["li"], W) + "\n" + sep + "\n" + col(d["rt"], d["ri"], GOLD) + "\n  </div>")
    return sec(sid, inner, notes, "display:flex; flex-direction:column; justify-content:center")


def g_cover(sid, notes):
    inner = (bg("bg") + "\n"
      '  <div style="flex:1"></div>\n'
      '  <p style="font-family:%s; font-size:36px; font-style:italic; font-weight:500; text-align:center; color:%s">MARHABA</p>\n'
      '  <p style="font-family:%s; font-size:31px; font-style:italic; text-align:center; color:%s">🕐 LE WEBINAIRE commence à 20h incha Allah !</p>\n'
      '  <p style="font-family:%s; font-size:31px; font-style:italic; text-align:center; color:%s">🦊 N\'oubliez pas de prendre des notes, vous risquez<br>d\'apprendre des choses inchaAllah</p>\n'
      '  <div style="background:#FFFFFF; padding:22px 54px">\n'
      '    <h1 style="font-family:%s; font-size:126px; font-weight:900; font-style:italic; text-transform:uppercase; '
      'line-height:1.0; text-align:center; background:linear-gradient(90deg, #131313 0%%, #1C1C1C 30%%, %s 100%%); '
      'background-clip:text; -webkit-text-fill-color:transparent">Héritage &amp;<br>Modernité</h1>\n  </div>\n'
      '  <p style="font-family:%s; font-size:28px; text-align:center; color:%s">Zaki Chairi &nbsp;·&nbsp; Oussama Jammal &nbsp;·&nbsp; 24 septembre 2026</p>\n'
      '  <div style="flex:1"></div>\n' + logo(760, 930, 0.62)
      ) % (POP, W, POP, W, POP, W, ARCH, GOLD_D, POP, DIM)
    return sec(sid, inner, notes, "display:flex; flex-direction:column; justify-content:center; align-items:center; gap:22px")

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

SCRIM = {"cardone", "meeting"}


def g_whatsapp(sid, notes):
    items = ["🎁 partager des cadeaux exclusifs",
             "📚 envoyer les ressources mentionnées",
             "🎯 vous aider à passer à l'action après le webinaire",
             "🤝 garder le lien avec le Collectif"]
    li = "\n".join('      <p style="font-family:%s; font-size:34px; line-height:1.45; color:%s">%s</p>'
                   % (POP, W, x) for x in items)
    inner = (bg("bg") + "\n"
      '  <div style="display:flex; gap:76px; align-items:center">\n'
      '    <img src="%s" alt="QR code du groupe WhatsApp du live" style="width:620px; height:620px; '
      'object-fit:contain; border-radius:18px">\n'
      '    <div style="flex:1; display:flex; flex-direction:column; gap:26px">\n'
      '      <h2 style="font-family:%s; font-size:60px; font-weight:900; font-style:italic; '
      'text-transform:uppercase; line-height:1.1; color:%s">Rejoignez le groupe<br>WhatsApp du live</h2>\n'
      '      <div style="width:180px; height:4px; background:%s"></div>\n'
      '      <p style="font-family:%s; font-size:32px; color:%s">C\'est là qu\'on va :</p>\n'
      '%s\n'
      '      <p style="font-family:%s; font-size:30px; line-height:1.45; color:%s">Le webinaire se termine… '
      'mais l\'accompagnement continue là-bas.</p>\n'
      '    </div>\n  </div>') % (BLOB.get("qr",""), ARCH, W, GOLD, POP, GOLD, li, POP, DIM)
    return sec(sid, inner, notes, "display:flex; flex-direction:column; justify-content:center")

# ---------------------------------------------------------------- parse
src = open("/tmp/claude-0/webi/script.md").read()
slides = []
for m in re.finditer(r"SLIDE (\d+) — \[([A-ZÉ]+)\]\n(.*?)(?=\nSLIDE \d+ — \[|\n═|\Z)", src, re.S):
    n, typ, body = int(m.group(1)), m.group(2), m.group(3)
    note = ""
    mm = re.search(r"^À L'ORAL\s*:\s*", body, re.M)
    if mm:
        note = " ".join(body[mm.end():].split())
        body = body[:mm.start()]
    lines = [l.rstrip() for l in body.strip("\n").split("\n")]
    lines = [l for l in lines if l.strip()]
    slides.append((n, typ, lines, note))

print("slides parsés:", len(slides))

order = []
for n, typ, lines, note in slides:
    sid = "s%03d" % n
    order.append(sid)
    lines = [html.escape(l, quote=False).replace("&amp;", "&") for l in lines]
    if is_whatsapp(lines):
        htmlv = g_whatsapp(sid, note or "Scanner le QR à l'écran.")
        open(os.path.join(SL, sid + ".html"), "w").write(htmlv + "\n")
        continue
    if n == 1:
        htmlv = g_cover(sid, "Slide d'attente et d'ouverture. Reprends la tienne si tu préfères : c'est exactement le même gabarit que ton webinaire de septembre.")
        open(os.path.join(SL, sid + ".html"), "w").write(htmlv + "\n")
        continue
    if typ == "REPRISE":
        note = (note + "  ·  " if note else "") + "Slide déjà existante dans tes decks — tu peux reprendre la tienne telle quelle."
        htmlv = g_liste(sid, lines, note) if len(lines) > 1 else g_titre(sid, lines, note)
    elif typ == "TITRE":
        which = photo_of(lines)
        htmlv = g_titre(sid, lines, note, which)
    elif typ == "PARTIE":
        htmlv = g_partie(sid, lines, note)
    elif typ == "PUNCHLINE":
        htmlv = g_punch(sid, lines, note)
    elif typ == "CITATION":
        htmlv = g_citation(sid, lines, note)
    elif typ == "LISTE":
        htmlv = g_liste(sid, lines, note, photo_of(lines))
    elif typ == "LUNDI":
        htmlv = g_lundi(sid, lines, note)
    elif typ == "VS":
        htmlv = g_vs(sid, VS[vskey(lines)], note)
    else:
        htmlv = g_punch(sid, lines, note)
    open(os.path.join(SL, sid + ".html"), "w").write(htmlv + "\n")

deck = {
  "v": 4,
  "createdOnFiles": {"v": 1, "at": "2026-09-22T10:00:00Z"},
  "title": "Héritage & Modernité",
  "order": order,
  "cover": order[0],
  "sections": {},
  "faces": {
    "archivo": {"family": "Archivo", "href": "https://fonts.googleapis.com/css2?family=Archivo:ital,wght@0,400..900;1,400..900&display=swap"},
    "oswald": {"family": "Oswald", "href": "https://fonts.googleapis.com/css2?family=Oswald:wght@300..700&display=swap"},
    "poppins": {"family": "Poppins", "href": "https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&display=swap"},
    "noto-naskh-arabic": {"family": "Noto Naskh Arabic", "href": "https://fonts.googleapis.com/css2?family=Noto+Naskh+Arabic:wght@400..700&display=swap"}
  },
  "designSystems": []
}
# sections = les bandes du script
bands = re.findall(r"═{20,}\n(.+?)\n═{20,}\n\n(?:.*?)SLIDE (\d+) — \[", src, re.S)
seen = set()
for title, first in bands:
    key = re.sub(r"[^a-z0-9]+", "-", title.lower())[:40].strip("-")
    if key in seen: continue
    seen.add(key)
    deck["sections"][key] = {"description": title.strip(), "start": "s%03d" % int(first)}
json.dump(deck, open(os.path.join(ROOT, "project", "deck.json"), "w"), ensure_ascii=False, indent=2)
print("sections:", list(deck["sections"].values())[:3], "...")
print("ok", len(order))
