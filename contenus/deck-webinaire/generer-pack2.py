# -*- coding: utf-8 -*-
exec(open("/tmp/claude-0/webi/gabarits.py").read())
OUT = "/tmp/claude-0/-home-user-ctp-plugin/5bde7487-de28-5f85-acc6-6f6c831c1436/scratchpad/art/Pack-2-structure-et-conclusion.pptx"

def add(kind, data, note):
    if kind == "titre":     s_titre(data, note)
    elif kind == "partie":  s_partie(data, note)
    elif kind == "punch":   s_punch(data, note)
    elif kind == "liste":   s_liste(data, note)
    elif kind == "citation":
        q, src, ar = data
        s_citation([q, src] + ([ar] if ar else []), note)


# ------------------------------------------------ slide-consigne (fond or)
def s_consigne(titre, lignes, nb):
    sl = prs.slides.add_slide(BLANK)
    bgshape = rect(sl, 0, 0, W, H, GOLD)
    _, tf = tb(sl, 150, 120, W - 300, 150, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP)
    para(tf, "À INSÉRER DANS TON DECK", POP, 32, INK, bold=True, align=PP_ALIGN.LEFT, first=True)
    _, tf2 = tb(sl, 150, 250, W - 300, 220, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP)
    para(tf2, titre.upper(), ARCH, 84, INK, bold=True, italic=True, align=PP_ALIGN.LEFT, lh=1.06, first=True)
    rect(sl, 150, 500, 260, 8, INK)
    _, tf3 = tb(sl, 150, 560, W - 300, 330, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP)
    for i, (mot, txt) in enumerate(lignes):
        para(tf3, mot, POP, 30, INK, bold=True, align=PP_ALIGN.LEFT, space=6, first=(i == 0))
        para(tf3, txt, POP, 38, INK, align=PP_ALIGN.LEFT, lh=1.34, space=26)
    _, tf4 = tb(sl, 150, 930, W - 300, 70, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP)
    para(tf4, "Les %d slides qui suivent forment ce bloc. Cette page-ci ne va pas dans le deck." % nb,
         POP, 28, INK, italic=True, align=PP_ALIGN.LEFT, first=True)
    sl.notes_slide.notes_text_frame.text = "CONSIGNE — ne pas conserver cette page dans le deck final."
    return sl

P = []
BLOCKS_META = []
def block(label, where, slides, ancres=None):
    BLOCKS_META.append((label, ancres or [], len(slides)))
    for i, (k, d) in enumerate(slides):
        P.append((label, k, d, ("→ INSÉRER " + where) if i == 0 else ("↑ suite du bloc « %s »" % label)))

# ---------------------------------------------------------------- 1. le plan
block("1 · Le plan de la soirée",
 "APRÈS ta slide « Et à la fin : un QUIZ », donc juste avant PARTIE 1", [
 ("titre", ["LE PLAN DE LA SOIRÉE"]),
 ("liste", ["QUATRE PARTIES",
   "1. Poser le cadre — c'est quoi un paradigme, et pourquoi le tien n'est pas le tien",
   "2. Les six axes — où ça se voit dans ton agenda",
   "3. Les compétences transversales — ce qu'il te manque vraiment",
   "4. La méthodologie — comment on travaille ça ensemble"]),
])

# ---------------------------------------------------------------- 2. séparateurs
for n, (num, titre, where) in enumerate([
 ("PARTIE 1 SUR 4", "Poser le cadre",
  "EN REMPLACEMENT de ta slide « PARTIE 1 / POSER LE CADRE »"),
 ("PARTIE 2 SUR 4", "Les six axes",
  "AVANT « ON ARRÊTE LA THÉORIE » — remplace la slide PARTIE 2 du pack précédent"),
 ("PARTIE 3 SUR 4", "Les compétences transversales",
  "AVANT « CE QUI TE MANQUE N'EST PAS CE QUE TU CROIS » (début du bloc G du pack précédent)"),
 ("PARTIE 4 SUR 4", "La méthodologie Tariqa",
  "EN REMPLACEMENT de ta slide « PARTIE 3 / LA méthodologie »"),
], 1):
    block("2 · Séparateur partie %d" % n, where, [("partie", [num, titre])])

# ---------------------------------------------------------------- 3. résumé des six axes
block("3 · Résumé des six axes",
 "À LA FIN DE LA PARTIE 2, après ton dernier axe et AVANT la partie 3", [
 ("titre", ["UNE SEULE QUESTION"]),
 ("titre", ["QU'EST-CE QUE JE CHANGE", "CHEZ MOI, DÈS LUNDI ?"]),
 ("liste", ["LES SIX AXES, ET L'ACTION QUI VA AVEC",
   "1. La finalité → écris pour quoi tu fais ça, puis ouvre ton agenda",
   "2. La mesure → une ligne non chiffrable, tout en haut du tableau de bord",
   "3. Le profit et le risque → qui perd quoi, si ça tourne mal ?",
   "4. La croissance et la dette → ce rythme, je le tiens encore dans deux ans ?",
   "5. La concurrence → recommande un concurrent, publiquement",
   "6. Le client et l'effet → qu'est-ce que j'installe chez mes clients ?"]),
 ("punch", ["Prends-en une.", "Une seule.", "Celle qui t'a le plus gêné ce soir."]),
])

# ---------------------------------------------------------------- 4. et mes outils ?
block("4 · Et mes outils actuels ?",
 "JUSTE APRÈS le résumé des six axes, en ouverture de la partie 3", [
 ("titre", ["ET TOUT CE QUE J'AI DÉJÀ APPRIS ?"]),
 ("punch", ["On ne jette rien.", "On règle."]),
 ("citation", ("L'idée n'est pas de tout rejeter. On ne peut qu'emprunter. La question, c'est comment.",
   "Dr Chauki Lazhar, spécialiste des fondements du droit", None)),
 ("liste", ["DEUX QUESTIONS AVANT D'ADOPTER UN OUTIL",
   "1. D'où il vient ? Quelle idée de la réussite il transporte sans le dire ?",
   "2. Qu'est-ce qu'il produit chez les gens ?",
   "👉 Et c'est tout. Deux questions, sur n'importe quelle formation, n'importe quelle méthode."]),
])

# ---------------------------------------------------------------- 5. ce que tu emportes
block("5 · Ce que tu emportes",
 "À LA PLACE de ta séquence « CE QUE TU EMPORTES » actuelle (les trois slides 1️⃣ 2️⃣ 3️⃣)", [
 ("titre", ["CE QUE TU EMPORTES"]),
 ("punch", ["Tu es venu chercher des techniques.", "Tu repars avec une question",
   "à te poser avant chaque technique."]),
 ("liste", ["TROIS QUESTIONS, SUR TON ACTIVITÉ ET SUR CHACUN DE TES OUTILS",
   "👉 Est-ce que ça crée de la DÉPENDANCE ?",
   "👉 Est-ce que ça crée de l'AVEUGLEMENT ?",
   "👉 Est-ce que ça crée de l'EXCÈS ?"]),
 ("punch", ["Trois questions.", "Aucune compétence religieuse nécessaire.",
   "Tu peux les poser dès lundi matin."]),
 ("punch", ["Halal répond à : est-ce que j'ai le droit ?",
   "Ça ne répond pas à :", "est-ce que c'est ce que je dois faire ?"]),
])

# ---------------------------------------------------------------- 6. soyons honnêtes
block("6 · Soyons honnêtes",
 "APRÈS « CE QUE TU EMPORTES », avant le quiz", [
 ("titre", ["SOYONS HONNÊTES"]),
 ("punch", ["On n'est pas venus vous définir",
   "le paradigme de l'entrepreneur musulman.", "On n'en est pas là."]),
 ("liste", ["CE QU'ON A FAIT CE SOIR",
   "On vous a posé les questions qui nous travaillent",
   "On vous a montré où on en est de notre propre réflexion",
   "On essaie nous-mêmes d'incarner tout ça, et on n'y arrive pas tous les jours",
   "👉 C'est un chantier. Pas une conclusion."]),
 ("punch", ["Un paradigme, ce n'est pas un document",
   "qu'on adopte et qu'on applique.", "C'est une remise en question qui ne s'arrête pas."]),
 ("liste", ["ET CE QU'ON NE SAIT PAS ENCORE",
   "Le prix juste — pas de barème possible, et pourtant le déséquilibre excessif existe",
   "L'abonnement, les places de marché — le droit des transactions n'a pas fini d'y répondre",
   "Et la question qu'on ne tranche pas : que faire quand un marché entier",
   "repose sur une pratique qu'on refuse ?"]),
])

ANCRES = {'1 · Le plan de la soirée': [('APRÈS ta slide', '« Et à la fin : un QUIZ. Avec des cadeaux pour ceux qui répondent. »'), ('AVANT ta slide', '« PARTIE 1 / POSER LE CADRE »')], '2 · Séparateur partie 1': [('REMPLACE ta slide', '« PARTIE 1 / POSER LE CADRE »')], '2 · Séparateur partie 2': [('REMPLACE ta slide', '« PARTIE 2 / LES SIX AXES »  (celle du pack précédent)')], '2 · Séparateur partie 3': [('AVANT ta slide', "« CE QUI TE MANQUE N'EST PAS CE QUE TU CROIS »")], '2 · Séparateur partie 4': [('REMPLACE ta slide', '« PARTIE 3 / LA MÉTHODOLOGIE »')], '3 · Résumé des six axes': [('REMPLACE ta slide', '« LES SIX SONT PASSÉS »'), ('DONC APRÈS', "« Il s'agit de ce que ton dispositif rend probable. »"), ('ET AVANT', "« D'accord. Et demain, je fais quoi de tout ce que j'ai déjà appris ? »")], '4 · Et mes outils actuels ?': [('APRÈS ta slide', "« D'accord. Et demain, je fais quoi de tout ce que j'ai déjà appris ? »"), ('REMPLACE', '« ALORS ON JETTE TOUT ? » et tout le bloc Ghazâlî / Bennabi / méthode en deux passes')], '5 · Ce que tu emportes': [('REMPLACE', 'ta séquence « CE QUE TU EMPORTES » : le titre et les trois slides 1️⃣ 2️⃣ 3️⃣')], '6 · Soyons honnêtes': [('APRÈS', 'le bloc « CE QUE TU EMPORTES » que tu viens de poser'), ('REMPLACE aussi', "« ET CE QU'ON NE SAIT PAS ENCORE »"), ('AVANT ta slide', '« LE QUIZ »')]}

# page d'ouverture
s_consigne("Mode d'emploi", [
 ("CE FICHIER", "Ce sont uniquement les nouvelles slides. Ton deck n'est pas touché."),
 ("AVANT CHAQUE BLOC", "une page dorée comme celle-ci te dit où le poser."),
 ("LES REPÈRES", "sont donnés par le TEXTE de tes slides, pas par un numéro de page :"),
 ("POURQUOI", "tes numéros bougent à chaque insertion, le texte ne bouge pas."),
], 0)

cur = None
for i, (label, k, d, note) in enumerate(P, 1):
    if label != cur:
        cur = label
        meta = [m for m in BLOCKS_META if m[0] == label][0]
        titre = label.split(" · ", 1)[1]
        s_consigne(titre, ANCRES.get(label, [("À PLACER", "voir les notes de la slide suivante")]), meta[2])
    add(k, d, "[%02d / %s]  %s" % (i, label, note))
prs.save(OUT)
print(len(P), "slides ->", OUT, os.path.getsize(OUT), "octets")
