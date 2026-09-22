# -*- coding: utf-8 -*-
import re, os, html, subprocess, json

SRC  = "/tmp/claude-0/webi/script.md"
OUT  = "/tmp/claude-0/-home-user-ctp-plugin/5bde7487-de28-5f85-acc6-6f6c831c1436/scratchpad/chapitres"
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
os.makedirs(OUT, exist_ok=True)

TYPES = {"REPRISE":"slide de reprise","TITRE":"titre plein","PUNCHLINE":"punchline",
         "CITATION":"citation sourcée","VS":"comparaison en deux colonnes",
         "LISTE":"liste","PARTIE":"séparateur de partie","LUNDI":"action concrète"}

# --- découpage en chapitres
text = open(SRC).read()
B = "═" * 56
parts = re.split(r"%s\n(.+?)\n%s\n" % (B, B), text)
bands = []          # (titre, contenu)
for i in range(1, len(parts), 2):
    bands.append((parts[i].strip(), parts[i+1]))

CHAPTERS = [
 ("01", "Ouverture et cadre", ["AVANT LE LIVE", "PARTIE 1 — POSER LE CADRE (20 min)"],
  "Cette partie installe le problème avant d'installer le vocabulaire. Elle pose une question "
  "au public — quelle est la vision de l'islam sur l'entrepreneuriat — puis met en évidence, par "
  "trois situations concrètes auxquelles chacun répond sans réfléchir, que les réponses spontanées "
  "viennent toutes du même endroit. Le mot « paradigme » n'arrive qu'après cette démonstration. "
  "Elle établit ensuite pourquoi le filtre licite/illicite, nécessaire, ne suffit pas : il opère "
  "sur des actes isolés et jamais sur la logique qui les produit. Elle se referme sur la position "
  "du Collectif : le patrimoine juridique existe, il est simplement inaccessible aux praticiens."),
 ("02", "Axe 1 — La finalité", ["AXE 1 — LA FINALITÉ (18 min)"],
  "L'axe qui commande les cinq autres. Il oppose deux réponses à la question du but : le score, "
  "assumé depuis Friedman et repris par la culture entrepreneuriale dominante, contre l'agrément "
  "de Dieu, dont le commerce est l'un des chemins. Le point central est un changement de rang et "
  "non de montant : la piété n'est pas la pauvreté, et Ibn ʿAwf est mort immensément riche."),
 ("03", "Axe 2 — La mesure", ["AXE 2 — LA MESURE (18 min)"],
  "Le tableau de bord comme objet idéologique déguisé en outil de suivi. Ce qui n'est pas mesurable "
  "disparaît faute de case, non faute de valeur. L'axe articule la critique de la quantification "
  "avec la question de la réussite : orienté résultat contre orienté commandement, et l'avertissement "
  "du hadith des trois premiers jugés, où trois résultats visibles spectaculaires sont rejetés."),
 ("04", "Axe 3 — Le profit et le risque", ["AXE 3 — LE PROFIT ET LE RISQUE (18 min)"],
  "Deux questions qu'on ne relie jamais et qui n'en font qu'une. D'un côté la logique de marge "
  "contre la logique de circulation, où la bénédiction porte sur l'opération et non sur le solde. "
  "De l'autre le portage du risque : la ligne ne sépare pas le revenu actif du revenu passif, elle "
  "sépare le gain qui a une cause de celui qui n'en a pas."),
 ("05", "Axe 4 — La croissance et la dette", ["AXE 4 — LA CROISSANCE ET LA DETTE (18 min)"],
  "La partie la plus démonstrative. Elle transforme un interdit en explication : le système fondé "
  "sur la dette et l'intérêt implique une croissance obligatoire, ce qui se démontre par le calcul. "
  "L'interdiction de l'intérêt devient alors le retrait du moteur qui rend la croissance obligatoire. "
  "Elle se conclut sur la distinction entre grandir par décision et grandir par obligation."),
 ("06", "Axe 5 — La concurrence", ["AXE 5 — LA CONCURRENCE (18 min)"],
  "L'axiome de rareté présenté comme un postulat et non comme une donnée du monde, démonté par le "
  "texte et par les chiffres. La partie contient le matériel le plus opérationnel du webinaire : "
  "trois interdictions techniques de concurrence, nommées depuis quatorze siècles, traduites en "
  "pratiques contemporaines parfaitement courantes. Garde-fou explicite : l'islam n'est pas "
  "anti-marché, il est anti-nuisance."),
 ("07", "Axe 6 — Le client et l'effet", ["AXE 6 — LE CLIENT ET L'EFFET (18 min)"],
  "Le consentement est nécessaire mais non suffisant : un contrat protège juridiquement sans "
  "dédouaner. Puis l'axe le plus dérangeant, celui de l'effet — non pas ce que tu vends, mais ce "
  "que ton dispositif installe chez les gens. Il est adossé à des fondements du droit et débouche "
  "sur l'outil central du webinaire : le test des trois leviers, dépendance, aveuglement, excès."),
 ("08", "Clôture", ["CLÔTURE (20 min)", "À VÉRIFIER AVEC OUSSAMA AVANT LE LIVE"],
  "Comment emprunter les outils modernes sans être emporté par eux : le contraste entre les deux "
  "savants face à la philosophie grecque, les idées mortes et les idées mortelles de Malek Bennabi, "
  "et la méthode en deux passes. Puis la distinction entre pression et tromperie, la méthode en "
  "cinq questions, les trois choses à emporter, les questions laissées ouvertes, et le quiz."),
]


# --- extraits du syllabus, par chapitre
SYL = open("/tmp/claude-0/syl.txt").read().split("\n")
def syl(a, b):
    """lignes 1-indexées, bornes incluses -> paragraphes nettoyés"""
    raw = [l.strip() for l in SYL[a-1:b]]
    out, buf = [], []
    for l in raw:
        if not l:
            if buf: out.append(" ".join(buf)); buf = []
        else:
            buf.append(l)
    if buf: out.append(" ".join(buf))
    merged, cur = [], ""
    for para in out:
        if len(para) < 90 and not para.endswith((".", "»", "?", "!", ":")):
            if cur: merged.append(cur); cur = ""
            merged.append("### " + para)
        else:
            cur = (cur + " " + para).strip() if cur and len(cur) < 300 else para
            merged.append(cur); cur = ""
    seen, res = set(), []
    for x in merged:
        if x not in seen:
            seen.add(x); res.append(x)
    return res

FOND = {
 "01": [("Introduction", 44, 379), ("Partie I — Qu'est-ce qu'un paradigme", 380, 601),
        ("Partie II — Le paradigme qu'on nous propose", 602, 1017),
        ("Partie III — Ce que notre héritage dit du commerce", 1018, 1250)],
 "02": [("Axe 0 — La finalité", 1270, 1361)],
 "03": [("Axe 1 — La réussite", 1362, 1422), ("Axe 2 — La mesure", 1423, 1496)],
 "04": [("Axe 3 — Le profit", 1497, 1560), ("Axe 4 — Le risque", 1561, 1616)],
 "05": [("Axe 5 — La croissance et la dette", 1617, 1708)],
 "06": [("Axe 6 — La concurrence", 1709, 1799), ("Axe 10 — Le collectif", 2060, 2119)],
 "07": [("Axe 7 — Le consentement", 1800, 1878), ("Axe 8 — Le client", 1879, 1939),
        ("Axe 9 — L'effet", 1940, 2059)],
 "08": [("Partie V — Les outils modernes", 2120, 2331), ("Partie VI — Ce qui reste ouvert", 2332, 2456)],
}

def parse(body):
    out = []
    for m in re.finditer(r"SLIDE (\d+) — \[([A-ZÉ]+)\]\n(.*?)(?=\nSLIDE \d+ — \[|\Z)", body, re.S):
        n, typ, b = int(m.group(1)), m.group(2), m.group(3)
        note = ""
        mm = re.search(r"^À L'ORAL\s*:\s*", b, re.M)
        if mm:
            note = " ".join(b[mm.end():].split()); b = b[:mm.start()]
        lines = [l.rstrip() for l in b.strip("\n").split("\n") if l.strip()]
        out.append((n, typ, lines, note))
    return out

CSS = """
@page { size: A4; margin: 20mm 18mm 18mm 18mm; }
* { box-sizing: border-box; }
body { margin:0; font-family: Georgia, 'Times New Roman', serif; color:#1B211D;
       background:#FFFFFF; font-size:11.5pt; line-height:1.55; }
.cover { page-break-after: always; padding-top: 38mm; }
.kicker { font-family: Helvetica, Arial, sans-serif; font-size:9pt; letter-spacing:2.4px;
          text-transform:uppercase; color:#8A6021; margin:0 0 10mm; }
h1 { font-size:27pt; line-height:1.12; font-weight:normal; margin:0 0 8mm; }
.lead { font-size:12pt; line-height:1.6; color:#333B36; margin:0 0 10mm; }
.meta { font-family: Helvetica, Arial, sans-serif; font-size:9.5pt; color:#5B665E;
        border-top:1px solid #DDD5C6; padding-top:4mm; }
h2 { font-family: Helvetica, Arial, sans-serif; font-size:10pt; letter-spacing:1.6px;
     text-transform:uppercase; color:#8A6021; margin:9mm 0 4mm; font-weight:600;
     border-bottom:1px solid #DDD5C6; padding-bottom:2mm; }
.slide { page-break-inside: avoid; margin:0 0 7mm; }
.sn { font-family: Helvetica, Arial, sans-serif; font-size:8.5pt; letter-spacing:1.2px;
      text-transform:uppercase; color:#8F9A92; margin:0 0 1.5mm; }
.txt { margin:0; white-space:pre-wrap; font-size:12.5pt; line-height:1.42; }
.txt.first { font-weight:bold; }
.note { margin:2.5mm 0 0; padding:2.5mm 0 2.5mm 5mm; border-left:2px solid #C8A24E;
        font-size:10.5pt; line-height:1.5; color:#454F49; }
.fond { page-break-before: always; }
.fond h2 { margin-top:0; }
.fond h3 { font-family: Georgia, serif; font-size:13pt; font-weight:normal; font-style:italic;
           color:#1B211D; margin:6mm 0 2mm; }
.fond p { margin:0 0 3.2mm; text-align:justify; hyphens:auto; }
.fondlead { font-size:10.5pt; color:#5B665E; font-style:italic; margin:0 0 6mm;
            border-bottom:1px solid #DDD5C6; padding-bottom:3mm; }
.note b { font-family: Helvetica, Arial, sans-serif; font-size:8.5pt; letter-spacing:1.2px;
          text-transform:uppercase; color:#8A6021; display:block; margin-bottom:1mm; font-weight:600; }
"""

def render(ch):
    num, title, bandnames, lead = ch
    slides = []
    for bn in bandnames:
        for t, body in bands:
            if t == bn:
                slides.append((bn, parse(body)))
    total = sum(len(s) for _, s in slides)
    nums = [n for _, ss in slides for n, _, _, _ in ss]
    rng = "slides %d à %d" % (min(nums), max(nums)) if nums else ""
    h = ['<meta charset="utf-8"><title>%s</title><style>%s</style>' % (html.escape(title), CSS)]
    h.append('<div class="cover">')
    h.append('<p class="kicker">Héritage &amp; Modernité · Chapitre %s sur 8</p>' % num)
    h.append('<h1>%s</h1>' % html.escape(title))
    h.append('<p class="lead">%s</p>' % html.escape(lead))
    h.append('<p class="meta">Webinaire du Collectif Tariqa PRO, jeudi 24 septembre 2026 · '
             'Zaki Chairi et Oussama Jammal<br>%d slides, %s du déroulé complet.<br><br>'
             'Ce document reprend le texte porté à l\'écran, slide par slide, ainsi que ce qui est '
             'dit à l\'oral et qui ne figure pas sur la slide.</p>' % (total, rng))
    h.append('</div>')
    for bn, ss in slides:
        h.append('<h2>%s</h2>' % html.escape(bn))
        for n, typ, lines, note in ss:
            h.append('<div class="slide">')
            h.append('<p class="sn">Slide %d — %s</p>' % (n, TYPES.get(typ, typ.lower())))
            for i, ln in enumerate(lines):
                h.append('<p class="txt%s">%s</p>' % (" first" if i == 0 and typ in ("LISTE","LUNDI","VS") else "",
                                                      html.escape(ln)))
            if note:
                h.append('<p class="note"><b>Ce qui se dit à l\'oral</b>%s</p>' % html.escape(note))
            h.append('</div>')
    blocks = FOND.get(num, [])
    if blocks:
        h.append('<div class="fond">')
        h.append('<h2>Le fond — extrait du syllabus</h2>')
        h.append('<p class="fondlead">Le texte de référence dont cette partie du webinaire est tirée. '
                 'Il porte le raisonnement complet, les sources nommées et les objections traitées, '
                 'là où les slides n\'en gardent que la pointe.</p>')
        for btitle, a, b in blocks:
            h.append('<h3>%s</h3>' % html.escape(btitle))
            for para in syl(a, b):
                if para.startswith("### "):
                    h.append('<h3>%s</h3>' % html.escape(para[4:]))
                else:
                    h.append('<p>%s</p>' % html.escape(para))
        h.append('</div>')
    return "\n".join(h), total

manifest = []
for ch in CHAPTERS:
    num, title, _, _ = ch
    page, total = render(ch)
    import unicodedata
    base = unicodedata.normalize("NFKD", title.lower()).encode("ascii", "ignore").decode()
    slug = re.sub(r"[^a-z0-9]+", "-", base).strip("-")
    hp = os.path.join(OUT, "%s-%s.html" % (num, slug))
    pp = os.path.join(OUT, "%s-%s.pdf" % (num, slug))
    open(hp, "w").write(page)
    subprocess.run([CHROME, "--headless", "--disable-gpu", "--no-sandbox",
                    "--no-pdf-header-footer", "--print-to-pdf=" + pp, "file://" + hp],
                   capture_output=True, timeout=180)
    manifest.append((num, title, total, pp, os.path.getsize(pp) if os.path.exists(pp) else 0))

for m in manifest:
    print("%s  %-36s %3d slides  %7d o  %s" % (m[0], m[1], m[2], m[4], os.path.basename(m[3])))
print("total slides:", sum(m[2] for m in manifest))
