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

P = []
def block(label, where, slides):
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

for i, (label, k, d, note) in enumerate(P, 1):
    add(k, d, "[%02d / %s]  %s" % (i, label, note))
prs.save(OUT)
print(len(P), "slides ->", OUT, os.path.getsize(OUT), "octets")
