# -*- coding: utf-8 -*-
exec(open("/tmp/claude-0/webi/gabarits.py").read())
OUT = "/tmp/claude-0/-home-user-ctp-plugin/5bde7487-de28-5f85-acc6-6f6c831c1436/scratchpad/art/Pack-2c-at-Talaq-axe-mesure.pptx"

def s_consigne(titre, lignes, pied):
    sl = prs.slides.add_slide(BLANK)
    rect(sl, 0, 0, W, H, GOLD)
    _, tf = tb(sl, 150, 120, W - 300, 150, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP)
    para(tf, "À INSÉRER DANS TON DECK", POP, 32, INK, bold=True, align=PP_ALIGN.LEFT, first=True)
    _, tf2 = tb(sl, 150, 250, W - 300, 220, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP)
    para(tf2, titre.upper(), ARCH, 78, INK, bold=True, italic=True, align=PP_ALIGN.LEFT, lh=1.06, first=True)
    rect(sl, 150, 500, 260, 8, INK)
    _, tf3 = tb(sl, 150, 560, W - 300, 330, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP)
    for i, (mot, txt) in enumerate(lignes):
        para(tf3, mot, POP, 30, INK, bold=True, align=PP_ALIGN.LEFT, space=6, first=(i == 0))
        para(tf3, txt, POP, 38, INK, align=PP_ALIGN.LEFT, lh=1.34, space=26)
    _, tf4 = tb(sl, 150, 930, W - 300, 70, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP)
    para(tf4, pied, POP, 28, INK, italic=True, align=PP_ALIGN.LEFT, first=True)
    sl.notes_slide.notes_text_frame.text = "CONSIGNE — ne pas conserver cette page dans le deck final."

s_consigne("At-Talaq 65:2-3", [
 ("APRÈS ta slide", "du verset at-Takāthur « LA COURSE AU “PLUS” VOUS A DISTRAITS… »"),
 ("AVANT ta slide", "« QUAND EST-CE QUE TU AS GAGNÉ ? »"),
 ("POURQUOI LÀ", "les deux versets se répondent : l'un sur le piège de compter,"),
 ("", "l'autre sur ce qui arrive hors de tout calcul."),
], "Les 3 slides qui suivent forment le bloc. Cette page-ci ne va pas dans le deck.")

s_punch(["Si tu ne comptes que ce qui se compte,",
         "tu ne verras venir",
         "que ce que tu avais déjà prévu."],
 "Poser la slide lentement. C'est le pivot de l'axe : un tableau de bord ne modélise que le connu. "
 "Tout ce qui arrive par une porte que tu n'avais pas dessinée n'a, par construction, aucune ligne "
 "où s'inscrire.")

s_citation(["« Et quiconque craint Allah, Il lui donnera une issue,",
            "et lui accordera Sa subsistance d'où il ne s'y attend pas. »",
            "Sourate At-Talaq, 65:2-3",
            "﴿ وَمَن يَتَّقِ اللَّهَ يَجْعَل لَّهُ مَخْرَجًا ۝ وَيَرْزُقْهُ مِنْ حَيْثُ لَا يَحْتَسِبُ ﴾"],
 "ATTENTION À NE PAS SURINTERPRÉTER EN DIRECT. La condition posée par le verset est la taqwa, "
 "la crainte de Dieu — ce n'est pas « arrête de mesurer ». Le verset ne dit pas que mesurer est "
 "mauvais. Ce qu'il établit, c'est que la source de la subsistance n'est pas enfermée dans ce que "
 "tu sais prévoir. Dis-le dans ce sens-là, sinon un auditeur attentif aura raison de tiquer. "
 "À faire valider par Oussama avant le direct.")

s_punch(["Ton tableau de bord n'a pas de colonne",
         "pour ce qui vient d'où tu ne l'attendais pas."],
 "Enchaîner directement sur l'action de l'axe : ajoute une ligne non chiffrable, et place-la en "
 "premier. Ce n'est pas de la décoration — c'est la seule façon de garder une place pour ce que "
 "le tableau ne sait pas voir.")

prs.save(OUT)
print("4 pages ->", OUT, os.path.getsize(OUT), "octets")
