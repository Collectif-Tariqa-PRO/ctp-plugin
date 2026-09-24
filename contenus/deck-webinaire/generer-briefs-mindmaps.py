# -*- coding: utf-8 -*-
import base64, html, os
BG = base64.b64encode(open("/tmp/claude-0/deckassets/bg.png","rb").read()).decode()
def T(t): return html.escape(t, quote=False).replace("&amp;","&")

STYLE_BLOCK = """Format 16:9, 1920 x 1080 px.

FOND — noir #0E0E0E recouvert d'une texture low-poly : triangles irréguliers de tailles
inégales, gris très sombres allant de #0A0A0A à #2E2E2E, avec un halo diffus légèrement
plus clair décalé vers le haut-gauche. Aucune couleur autre que ces gris dans le fond.

COULEURS — or clair #E3A94F pour les accents, les traits de liaison et le noeud central.
Or profond #B8862B pour les dégradés de titre. Blanc #FFFFFF pour le texte sur fond sombre.
Gris clair #CFCFCF pour le texte secondaire. Noir #141414 pour le texte sur fond clair.
Aucune autre couleur. Pas de bleu, pas de vert, pas de rouge, pas de dégradé arc-en-ciel.

TYPOGRAPHIE — trois familles seulement.
· Titres et noeud central : Archivo 900 italique, EN CAPITALES.
· Noeuds : Poppins 600.
· Textes secondaires et feuilles : Poppins 400.
Jamais de police à empattement, jamais de script, jamais de condensé.

NOEUDS — pavés à coins arrondis (rayon environ 16 px), jamais de cercles, jamais de nuages.
· Noeud central : rempli or #E3A94F, texte noir, Archivo 900 italique capitales.
· Noeuds de niveau 1 : remplis blanc #FFFFFF, texte noir #141414, Poppins 600.
· Noeuds de niveau 2 : fond transparent, contour or 2 px, texte blanc, Poppins 400.

LIAISONS — traits droits or #E3A94F de 2,5 px. Pas de courbes décoratives, pas de flèches
sauf si le sens de lecture l'exige, pas de traits en pointillés.

MISE EN PAGE — marges de 100 px sur les quatre bords. Titre de la slide en haut à gauche,
Archivo 900 italique capitales 40 px blanc, souligné d'un filet or de 150 x 4 px.
Composition symétrique et aérée, jamais plus de deux niveaux de profondeur.

INTERDITS — pas d'icônes génériques, pas d'ombres portées, pas d'effets de lueur,
pas de pictogrammes d'entreprise, pas de personnages, pas d'emoji dans les noeuds.
Le contenu est du texte et des traits. Rien d'autre."""

SLIDES = [
 dict(
  n="01", titre="Les six axes",
  ou="À la fin de la partie 2, juste avant le résumé « Qu'est-ce que je change chez moi ».",
  but="Donner d'un seul regard les six endroits où le paradigme se voit. C'est la slide que "
      "les gens photographient. Elle doit être lisible en trois secondes et tenir sur un écran "
      "de téléphone.",
  forme="Hub central, trois branches à gauche, trois à droite. Le hub au centre exact. "
        "Les six noeuds alignés sur deux colonnes verticales, à égale distance du hub. "
        "Six traits droits partant des bords gauche et droit du hub.",
  hub=("LES SIX AXES", "où le paradigme se voit dans ton agenda"),
  branches=[
   ("1 · LA FINALITÉ", "C'est quoi le but du jeu ?"),
   ("2 · LA MESURE", "Qu'est-ce que tu comptes le lundi matin ?"),
   ("3 · LE PROFIT ET LE RISQUE", "La marge, ou la transaction ? Qui perd quoi ?"),
   ("4 · LA CROISSANCE ET LA DETTE", "Tu grandis parce que tu veux, ou parce que tu dois ?"),
   ("5 · LA CONCURRENCE", "Écraser, ou l'abondance ?"),
   ("6 · LE CLIENT ET L'EFFET", "« Il était d'accord » suffit-il ?"),
  ],
  note="Ordre imposé, de haut en bas : 1, 2, 3 à gauche puis 4, 5, 6 à droite. "
       "Le numéro en or, le nom de l'axe en noir, la question en gris sous le nom, en plus petit.",
 ),
 dict(
  n="02", titre="Les compétences transversales",
  ou="En ouverture de la partie 3, juste après « Ce qui te manque n'est pas ce que tu crois ».",
  but="Montrer que l'expertise métier est une impasse courte et que tout le chemin est de "
      "l'autre côté. Le déséquilibre entre les deux branches EST le message.",
  forme="Hub à gauche, à mi-hauteur. Deux branches vers la droite. La branche haute est "
        "courte et se termine tout de suite : c'est l'impasse. La branche basse s'ouvre en "
        "quatre feuilles alignées verticalement sur la droite. Le contraste de longueur "
        "entre les deux branches doit sauter aux yeux.",
  hub=("CE QUI TE MANQUE", None),
  branches=[
   ("L'EXPERTISE MÉTIER", "Tu l'as déjà. Elle ne suffit jamais à elle seule."),
   ("LES COMPÉTENCES TRANSVERSALES", "Elles servent quel que soit le métier"),
  ],
  feuilles=[
   ("MARKETING DIGITAL", "être trouvé"),
   ("LA VENTE", "être choisi"),
   ("LE DÎN", "connaître les règles du jeu"),
   ("L'IA", "augmenter ta portée"),
  ],
  note="La branche « expertise métier » est traitée en gris #CFCFCF, contour gris, pour "
       "signaler qu'elle n'est pas le sujet. Les quatre feuilles sont en contour or, texte "
       "blanc, et portent leur numéro de 1 à 4.",
 ),
 dict(
  n="03", titre="Les six piliers",
  ou="Dans la partie 4, en ouverture de la méthodologie.",
  but="Poser la méthode comme une progression ordonnée et non comme un catalogue. "
      "Le pilier 1 doit visiblement porter les cinq autres.",
  forme="Hub en haut au centre. En dessous, les six piliers en deux rangées de trois. "
        "Le pilier 1 se distingue : il est le seul à porter trois feuilles sous lui. "
        "Un trait descend du hub vers chaque pilier ; les traits du pilier 1 continuent "
        "vers ses trois feuilles.",
  hub=("MÉTHODOLOGIE TARIQA PRO", "six piliers, dans cet ordre"),
  branches=[
   ("ÉTAPE 1 · MINDSET", "le cap avant la technique"),
   ("ÉTAPE 2 · SALES", "savoir vendre ce qu'on fait"),
   ("ÉTAPE 3 · PRODUCT", "construire ce qui sert vraiment"),
   ("ÉTAPE 4 · MARKETING", "se rendre trouvable"),
   ("ÉTAPE 5 · OPERATIONS", "tenir dans la durée"),
   ("ÉTAPE 6 · FINANCE", "piloter sans se mettre en dette"),
  ],
  feuilles=[
   ("LE RAPPORT À ALLAH", "an-niyya · at-tawakkul · ar-rizq"),
   ("LE RAPPORT À SOI", "al-mas'ûliyya · al-ihsân · al-ibtilâ' · jihâd an-nafs"),
   ("LE RAPPORT AUX AUTRES", "husn al-khuluq · al-waqt · al-mâl · al-jamâ'a"),
  ],
  note="Les trois feuilles ne pendent QUE sous le pilier 1. C'est ce qui montre que le "
       "mindset est le socle et non une étape parmi six.",
 ),
 dict(
  n="04", titre="Tout le webinaire sur une page",
  ou="Juste avant « Ce que tu emportes », en clôture.",
  but="La carte mère. Elle doit permettre à quelqu'un qui arrive à la fin de reconstituer "
      "les deux heures. C'est la slide la plus dense du deck et c'est assumé.",
  forme="Hub au centre exact. Quatre branches vers les quatre coins, à 45 degrés. "
        "Chaque coin est un bloc rectangulaire portant un titre et ses éléments en liste "
        "courte. Les quatre blocs ont exactement la même taille et la même distance au hub. "
        "Symétrie parfaite : c'est ce qui rend une carte dense lisible.",
  hub=("ENTREPRENDRE EN MUSULMAN", None),
  quadrants=[
   ("EN HAUT À GAUCHE — LE PARADIGME",
    ["Invisible · global · hérité · résistant",
     "Le filtre licite/illicite regarde les actes",
     "Le paradigme, lui, les produit",
     "Halal = ai-je le droit. Pas = que dois-je faire."]),
   ("EN HAUT À DROITE — LES SIX AXES",
    ["1. La finalité · 2. La mesure",
     "3. Le profit et le risque",
     "4. La croissance et la dette",
     "5. La concurrence · 6. Le client et l'effet"]),
   ("EN BAS À GAUCHE — LES TROIS LEVIERS",
    ["Est-ce que ça crée de la DÉPENDANCE ?",
     "Est-ce que ça crée de l'AVEUGLEMENT ?",
     "Est-ce que ça crée de l'EXCÈS ?",
     "Le test qui s'applique à n'importe quel outil"]),
   ("EN BAS À DROITE — LA MÉTHODE",
    ["Quatre compétences transversales",
     "marketing digital · vente · dîn · IA",
     "Six piliers, dans l'ordre",
     "mindset · sales · product · marketing · ops · finance"]),
  ],
  note="Les quatre titres de bloc sont en or, les lignes en blanc. Aucun trait entre les "
       "blocs eux-mêmes : seulement les quatre traits qui partent du hub. Toute liaison "
       "supplémentaire rendrait la carte illisible.",
 ),
 dict(
  n="05", titre="L'écosystème du Collectif",
  ou="Dans la partie 4, après les six piliers, avant « Book un call ».",
  but="Montrer que le Collectif n'est pas une formation de plus mais un ensemble de "
      "dispositifs qui se tiennent. La vision est au-dessus, pas à côté : c'est elle qui "
      "commande le reste.",
  forme="Hub au centre. Un noeud LA VISION placé seul au-dessus du hub, relié par un trait "
        "plus épais (4 px) que les autres, pour marquer qu'il est d'un autre ordre. "
        "Les cinq dispositifs répartis en éventail sous le hub, à égale distance, "
        "reliés par des traits de 2,5 px.",
  hub=("LE COLLECTIF TARIQA PRO", None),
  branches=[
   ("LA VISION", "une richesse qualitative, marquée par la bénédiction divine"),
   ("HALAQA", "1x par semaine — sens, spiritualité, alignement"),
   ("COACHING COLLECTIF", "3x par semaine — intelligence collective"),
   ("COACHING INDIVIDUEL", "clarté, tracer le chemin"),
   ("FORMATION", "dîn · marketing digital · sales · soft skills · leadership"),
   ("MASTERCLASS", "les temps forts, ouverts"),
  ],
  note="LA VISION est le seul noeud au-dessus du hub, et le seul relié par un trait épais. "
       "Les cinq autres sont strictement au même niveau entre eux : aucune hiérarchie "
       "entre les dispositifs.",
 ),
]

# ---------------------------------------------------------------- page HTML
CSS = """
*{box-sizing:border-box}
body{margin:0;background:#0A0A0A;color:#E6E6E6;font-family:'Poppins',Arial,sans-serif;
 font-size:16px;line-height:1.6}
.hero{position:relative;padding-block:64px 44px;border-bottom:1px solid #262626;overflow:hidden}
.hero .tex{position:absolute;inset:0;background-size:cover;background-position:center;opacity:.55}
.hero .in{position:relative}
.wrap{max-width:900px;margin:0 auto;padding-inline:16px}
.eyebrow{font-family:'Archivo',sans-serif;font-size:12px;font-weight:700;letter-spacing:4px;
 text-transform:uppercase;color:#E3A94F;margin:0 0 14px}
h1{font-family:'Archivo',sans-serif;font-style:italic;font-weight:900;text-transform:uppercase;
 font-size:clamp(28px,6vw,50px);line-height:1.04;margin:0 0 16px;color:#fff;text-wrap:balance}
.lede{font-size:17px;color:#B9B9B9;margin:0;max-width:62ch}
section{padding-block:52px 0}
h2{font-family:'Archivo',sans-serif;font-style:italic;font-weight:900;text-transform:uppercase;
 font-size:26px;margin:0 0 4px;color:#fff}
.num{font-family:'Archivo',sans-serif;font-style:italic;font-weight:900;font-size:30px;
 color:#E3A94F;margin:0 0 2px}
.rule{width:130px;height:4px;background:#E3A94F;margin:12px 0 22px}
h3{font-family:'Poppins',sans-serif;font-size:12px;font-weight:600;letter-spacing:2.6px;
 text-transform:uppercase;color:#E3A94F;margin:26px 0 8px}
p{margin:0 0 12px;color:#CFCFCF}
pre{background:#131313;border:1px solid #2A2A2A;border-left:3px solid #E3A94F;border-radius:6px;
 padding:20px;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word;
 font-family:'IBM Plex Mono',ui-monospace,monospace;font-size:13.5px;line-height:1.62;color:#DCDCDC;
 margin:0 0 14px}
table{width:100%;border-collapse:collapse;margin:0 0 14px;font-size:15px}
td{padding:9px 12px;border-bottom:1px solid #242424;vertical-align:top;color:#DCDCDC}
td:first-child{color:#fff;font-weight:600;width:44%}
.note{border-left:2px solid #E3A94F;padding:10px 0 10px 16px;color:#B9B9B9;font-size:15px;
 margin:0 0 14px}
footer{padding-block:56px 90px;color:#8A8A8A;font-size:14px}
"""

def pre(t): return '<pre>%s</pre>' % T(t)

out = ['<title>Briefs mind maps</title>',
 '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:ital,wght@0,400..900;1,400..900&family=Poppins:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&family=IBM+Plex+Mono:wght@400;500&display=swap">',
 '<style>%s\n.hero .tex{background-image:url(data:image/png;base64,%s)}</style>' % (CSS, BG),
 '<div class="hero"><div class="tex"></div><div class="in"><div class="wrap">',
 '<p class="eyebrow">Héritage &amp; Modernité · briefs de production</p>',
 '<h1>Cinq mind maps,<br>brief par brief</h1>',
 '<p class="lede">Un descriptif de style commun à coller une fois, puis un descriptif détaillé '
 'par carte. Chaque bloc encadré se copie tel quel dans l\'outil de génération.</p>',
 '</div></div></div><div class="wrap">']

out.append('<section><p class="num">00</p><h2>Le style commun</h2><div class="rule"></div>')
out.append('<p>À coller en tête de chaque demande, avant le descriptif de la carte. '
           'Il fixe la charte du deck pour que les cinq cartes forment une série.</p>')
out.append(pre(STYLE_BLOCK))
out.append('</section>')

for s in SLIDES:
    out.append('<section><p class="num">%s</p><h2>%s</h2><div class="rule"></div>' % (s["n"], T(s["titre"])))
    out.append('<h3>Où elle va</h3><p>%s</p>' % T(s["ou"]))
    out.append('<h3>Ce qu\'elle doit faire</h3><p>%s</p>' % T(s["but"]))
    out.append('<h3>Structure</h3><p>%s</p>' % T(s["forme"]))
    out.append('<h3>Contenu exact des noeuds</h3><table>')
    h = s["hub"]
    out.append('<tr><td>NOEUD CENTRAL — %s</td><td>%s</td></tr>' % (T(h[0]), T(h[1] or "—")))
    for a, b in s.get("branches", []):
        out.append('<tr><td>%s</td><td>%s</td></tr>' % (T(a), T(b)))
    for a, b in s.get("feuilles", []):
        out.append('<tr><td>↳ %s</td><td>%s</td></tr>' % (T(a), T(b)))
    for titre, items in s.get("quadrants", []):
        out.append('<tr><td>%s</td><td>%s</td></tr>' % (T(titre), T(" · ".join(items))))
    out.append('</table>')
    out.append('<div class="note">%s</div>' % T(s["note"]))

    # prompt prêt à coller
    lines = ["Crée une mind map au format 16:9, 1920 x 1080 px.", "",
             "TITRE DE LA SLIDE (en haut à gauche) : " + s["titre"].upper(), "",
             "INTENTION : " + s["but"], "",
             "STRUCTURE : " + s["forme"], "", "CONTENU :",
             "· Noeud central : " + h[0] + (" — " + h[1] if h[1] else "")]
    for a, b in s.get("branches", []):
        lines.append("· Noeud : " + a + " — " + b)
    for a, b in s.get("feuilles", []):
        lines.append("  · Feuille : " + a + " — " + b)
    for titre, items in s.get("quadrants", []):
        lines.append("· Bloc " + titre)
        for it in items:
            lines.append("    - " + it)
    lines += ["", "CONTRAINTE PARTICULIÈRE : " + s["note"], "",
              "Applique le style commun donné plus haut, sans aucune variation."]
    out.append('<h3>Prompt prêt à coller</h3>')
    out.append(pre("\n".join(lines)))
    out.append('</section>')

out.append('<footer>Les cinq cartes forment une série : garde le même bloc de style pour les '
           'cinq, ne le reformule pas d\'une carte à l\'autre. Si une carte revient trop chargée, '
           'retire des feuilles — jamais des branches.</footer></div>')

p = "/tmp/claude-0/-home-user-ctp-plugin/5bde7487-de28-5f85-acc6-6f6c831c1436/scratchpad/art/briefs-mindmaps.html"
open(p, "w").write("\n".join(out))
print(len(SLIDES), "briefs ·", os.path.getsize(p), "octets ->", p)
