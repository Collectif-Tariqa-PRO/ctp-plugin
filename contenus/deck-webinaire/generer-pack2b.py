# -*- coding: utf-8 -*-
exec(open("/tmp/claude-0/webi/gabarits.py").read())
OUT = "/tmp/claude-0/-home-user-ctp-plugin/5bde7487-de28-5f85-acc6-6f6c831c1436/scratchpad/art/Pack-2b-plan-de-la-soiree.pptx"

def s_consigne(titre, lignes, nb):
    sl = prs.slides.add_slide(BLANK)
    rect(sl, 0, 0, W, H, GOLD)
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
    para(tf4, "La slide qui suit remplace l'ancienne. Cette page-ci ne va pas dans le deck.",
         POP, 28, INK, italic=True, align=PP_ALIGN.LEFT, first=True)
    sl.notes_slide.notes_text_frame.text = "CONSIGNE — ne pas conserver cette page dans le deck final."

s_consigne("Plan de la soirée", [
 ("REMPLACE", "la slide « QUATRE PARTIES » du pack 2 — celle avec les quatre descriptions"),
 ("LA SLIDE TITRE", "« LE PLAN DE LA SOIRÉE » qui la précède ne change pas, garde-la"),
], 1)

s_liste(["CE SOIR, EN QUATRE PARTIES",
 "1. POSER LE CADRE — ce que notre dîn dit du business, et pourquoi vérifier le halal ne suffit pas",
 "2. LES SIX AXES — ton prix, ton concurrent, ton client, ta croissance, ton associé",
 "3. LES COMPÉTENCES — marketing digital, vente, dîn, intelligence artificielle",
 "4. LA MÉTHODE — comment on travaille tout ça, étape par étape, au Collectif"],
 "Annonce les durées à l'oral, elles ne sont pas sur la slide : environ 25 minutes pour le cadre, "
 "une heure pour les six axes, 25 minutes pour les compétences, 15 pour la méthode. Les gens se "
 "perdent moins quand ils savent combien de temps dure chaque partie. Et précise tout de suite que "
 "la partie 2 est celle où ils vont noter le plus de choses.")

prs.save(OUT)
print("2 pages ->", OUT, os.path.getsize(OUT), "octets")
