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

FIL DE PROGRESSION — chaque carte porte, juste sous le titre, un bandeau horizontal de
quatre pastilles reliées par un trait or continu, dans cet ordre immuable :
PARADIGME · COMPÉTENCES · MÉTHODE · COLLECTIF
· Pastille déjà acquise : contour or 2 px, fond transparent, texte blanc.
· Pastille de la carte en cours : remplie or #E3A94F, texte noir, légèrement plus grande.
· Pastille pas encore atteinte : contour gris #4A4A4A, texte gris #6E6E6E.
Le bandeau fait toute la largeur utile, hauteur 56 px, et se trouve exactement au même
endroit sur les cinq cartes. C'est lui qui rend la construction visible sans un mot.

INTERDITS — pas d'icônes génériques, pas d'ombres portées, pas d'effets de lueur,
pas de pictogrammes d'entreprise, pas de personnages, pas d'emoji dans les noeuds.
Le contenu est du texte et des traits. Rien d'autre."""

SLIDES = [
 dict(
  n="01", titre="Le cap", brique="PARADIGME", fil=1,
  ou="À la fin de la partie 2, juste avant le résumé « Qu'est-ce que je change chez moi ».",
  but="Poser la première brique. Les six endroits où le paradigme se voit dans une semaine "
      "de travail. C'est la carte que les gens photographient.",
  forme="Bandeau de progression en haut, première pastille allumée. En dessous : hub central, "
        "trois branches à gauche, trois à droite, à égale distance. Six traits droits partant "
        "des bords gauche et droit du hub.",
  hub=("LE PARADIGME", "six endroits où il se voit dans ton agenda"),
  branches=[
   ("1 · LA FINALITÉ", "C'est quoi le but du jeu ?"),
   ("2 · LA MESURE", "Qu'est-ce que tu comptes le lundi matin ?"),
   ("3 · LE PROFIT ET LE RISQUE", "La marge, ou la transaction ? Qui perd quoi ?"),
   ("4 · LA CROISSANCE ET LA DETTE", "Tu grandis parce que tu veux, ou parce que tu dois ?"),
   ("5 · LA CONCURRENCE", "Écraser, ou l'abondance ?"),
   ("6 · LE CLIENT ET L'EFFET", "« Il était d'accord » suffit-il ?"),
  ],
  pied="Tu as le cap. Ça ne suffit pas encore.",
  note="Ordre imposé de haut en bas : 1, 2, 3 à gauche puis 4, 5, 6 à droite. Le numéro en or, "
       "le nom de l'axe en noir, la question en gris sous le nom, en plus petit. "
       "La phrase de pied de carte est en bas à droite, Poppins italique blanc 28 px.",
 ),
 dict(
  n="02", titre="Ce que tu as, ce qu'on ajoute", brique="COMPÉTENCES", fil=2,
  ou="En ouverture de la partie 3, juste après « Ce qui te manque n'est pas ce que tu crois ».",
  but="Deuxième brique. Montrer que l'expertise métier est un acquis réel — pas une erreur — "
      "et que ce qui manque se pose PAR-DESSUS. La carte doit se lire comme un empilement, "
      "pas comme une opposition.",
  forme="Bandeau de progression, deuxième pastille allumée, la première en contour or. "
        "En dessous, une construction en trois étages de bas en haut, comme un mur : "
        "étage du bas = LE PARADIGME, large, en contour or, texte blanc, marqué « acquis ». "
        "Étage du milieu = TON EXPERTISE MÉTIER, même largeur, contour blanc, marqué "
        "« tu l'as déjà ». Étage du haut = quatre pavés côte à côte, remplis or, texte noir : "
        "les quatre compétences. Aucun trait de liaison : les étages se touchent, c'est un mur.",
  hub=("LES COMPÉTENCES TRANSVERSALES", "elles servent quel que soit ton métier"),
  branches=[
   ("ÉTAGE 1 — LE PARADIGME", "acquis · le cap est posé"),
   ("ÉTAGE 2 — TON EXPERTISE MÉTIER", "tu l'as déjà · le couscous, le béton, le code"),
  ],
  feuilles=[
   ("MARKETING DIGITAL", "être trouvé"),
   ("LA VENTE", "être choisi"),
   ("LE DÎN", "connaître les règles du jeu"),
   ("L'IA", "augmenter ta portée"),
  ],
  pied="Le cap, ton métier, et les quatre compétences qui manquent.",
  note="IMPORTANT : l'expertise métier n'est PAS présentée comme une impasse ni comme une "
       "erreur. C'est un étage porteur, dessiné aussi large que les autres. Le message est "
       "additif : on ne remplace rien, on empile. Les quatre pavés du haut sont les seuls "
       "remplis en or, parce que ce sont eux la brique du jour.",
 ),
 dict(
  n="03", titre="L'ordre de travail", brique="MÉTHODE", fil=3,
  ou="Dans la partie 4, en ouverture de la méthodologie.",
  but="Troisième brique. Poser la méthode comme une progression ordonnée et non comme un "
      "catalogue. Le pilier 1 doit visiblement porter les cinq autres.",
  forme="Bandeau de progression, troisième pastille allumée, les deux premières en contour or. "
        "Hub en haut au centre. En dessous, les six piliers en deux rangées de trois. "
        "Le pilier 1 est le seul à porter trois feuilles sous lui.",
  hub=("LA MÉTHODE", "six piliers, dans cet ordre"),
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
  pied="Le cap, les compétences, et l'ordre dans lequel on les travaille.",
  note="Les trois feuilles ne pendent QUE sous le pilier 1. C'est ce qui montre que le mindset "
       "est le socle et non une étape parmi six. Faire un rappel discret, en gris, sous le hub : "
       "« le pilier 1, c'est le paradigme de la partie 2 » — le lien entre les deux briques.",
 ),
 dict(
  n="04", titre="Avec qui", brique="COLLECTIF", fil=4,
  ou="Dans la partie 4, après les six piliers, avant « Book un call ».",
  but="Quatrième et dernière brique. Montrer que rien de ce qui précède ne se tient seul. "
      "La vision est au-dessus, pas à côté : c'est elle qui commande les dispositifs.",
  forme="Bandeau de progression, quatrième pastille allumée, les trois premières en contour or. "
        "Hub au centre. Un noeud LA VISION seul au-dessus du hub, relié par un trait plus épais "
        "(4 px). Les cinq dispositifs en éventail sous le hub, à égale distance, traits 2,5 px.",
  hub=("LE COLLECTIF", "personne ne fait ça seul"),
  branches=[
   ("LA VISION", "une richesse qualitative, marquée par la bénédiction divine"),
   ("HALAQA", "1x par semaine — sens, spiritualité, alignement"),
   ("COACHING COLLECTIF", "3x par semaine — intelligence collective"),
   ("COACHING INDIVIDUEL", "clarté, tracer le chemin"),
   ("FORMATION", "dîn · marketing digital · sales · soft skills · leadership"),
   ("MASTERCLASS", "les temps forts, ouverts"),
  ],
  pied="Dieu a réparti les dotations à des degrés inégaux — pour qu'on ait besoin les uns des autres.",
  note="LA VISION est le seul noeud au-dessus du hub et le seul relié par un trait épais. "
       "Les cinq dispositifs sont strictement au même niveau entre eux : aucune hiérarchie. "
       "La phrase de pied fait écho au verset az-Zukhruf 43:32 vu dans la partie 2.",
 ),
 dict(
  n="05", titre="La carte complète", brique="TOUT", fil=5,
  ou="Juste avant « Ce que tu emportes », en clôture.",
  but="La somme. Les quatre briques réunies sur une page. Elle doit permettre à quelqu'un qui "
      "arrive à la fin de reconstituer les deux heures. C'est la carte la plus dense du deck, "
      "et c'est assumé.",
  forme="Bandeau de progression avec les QUATRE pastilles allumées en or. Hub au centre exact. "
        "Quatre branches vers les quatre coins, à 45 degrés. Chaque coin est un bloc "
        "rectangulaire de taille identique, à distance identique du hub. Symétrie parfaite : "
        "c'est ce qui rend une carte dense lisible.",
  hub=("ENTREPRENDRE EN MUSULMAN", None),
  quadrants=[
   ("EN HAUT À GAUCHE — LE PARADIGME",
    ["Invisible · global · hérité · résistant",
     "Le filtre regarde les actes. Le paradigme les produit.",
     "Les six axes : finalité, mesure, profit et risque,",
     "croissance et dette, concurrence, client et effet"]),
   ("EN HAUT À DROITE — LES COMPÉTENCES",
    ["Ton expertise métier, tu l'as déjà",
     "On ajoute par-dessus :",
     "marketing digital · vente · dîn · IA",
     "chacune réorientée par le cap"]),
   ("EN BAS À GAUCHE — LA MÉTHODE",
    ["Six piliers, dans cet ordre",
     "mindset · sales · product",
     "marketing · operations · finance",
     "Et le test : dépendance, aveuglement, excès"]),
   ("EN BAS À DROITE — LE COLLECTIF",
    ["Halaqa · coaching collectif",
     "coaching individuel · formation · masterclass",
     "Sous une vision : une richesse qualitative,",
     "marquée par la bénédiction divine"]),
  ],
  pied="Le cap. Ton métier. Les compétences. La méthode. Et les autres.",
  note="Les quatre titres de bloc sont en or, les lignes en blanc. AUCUN trait entre les blocs "
       "eux-mêmes : seulement les quatre traits qui partent du hub. Toute liaison supplémentaire "
       "rendrait la carte illisible.",
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
 '<h1>Cinq cartes,<br>une brique à la fois</h1>',
 '<p class="lede">Les cinq cartes ne sont pas cinq résumés : c\'est une seule construction qui '
 's\'élève. Chaque carte reprend ce qui précède et pose une brique de plus. Un descriptif de '
 'style commun à coller une fois, puis un descriptif détaillé par carte.</p>',
 '</div></div></div><div class="wrap">']

out.append('<section><p class="num">00</p><h2>Le style commun</h2><div class="rule"></div>')
out.append('<p>À coller en tête de chaque demande, avant le descriptif de la carte. '
           'Il fixe la charte du deck pour que les cinq cartes forment une série.</p>')
out.append(pre(STYLE_BLOCK))
out.append('</section>')

for s in SLIDES:
    out.append('<section><p class="num">%s</p><h2>%s</h2><div class="rule"></div>' % (s["n"], T(s["titre"])))
    out.append('<h3>Brique</h3><p>%s &nbsp;·&nbsp; pastille %s sur 4 allumée</p>'
               % (T(s["brique"]), s["fil"] if s["fil"] <= 4 else "les quatre"))
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
    out.append('<tr><td>PHRASE DE PIED DE CARTE</td><td>%s</td></tr>' % T(s["pied"]))
    out.append('</table>')
    out.append('<div class="note">%s</div>' % T(s["note"]))

    # prompt prêt à coller
    lines = ["Crée une mind map au format 16:9, 1920 x 1080 px.", "",
             "TITRE DE LA SLIDE (en haut à gauche) : " + s["titre"].upper(), "",
             "FIL DE PROGRESSION : pastille « %s » allumée en or, les précédentes en contour or, "
             "les suivantes en gris." % s["brique"], "",
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
    lines += ["", "PHRASE DE PIED DE CARTE (en bas à droite, italique blanc) : " + s["pied"],
              "", "CONTRAINTE PARTICULIÈRE : " + s["note"], "",
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
