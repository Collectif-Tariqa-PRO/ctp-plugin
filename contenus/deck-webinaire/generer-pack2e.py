# -*- coding: utf-8 -*-
exec(open("/tmp/claude-0/webi/gabarits.py").read())
OUT = "/tmp/claude-0/-home-user-ctp-plugin/5bde7487-de28-5f85-acc6-6f6c831c1436/scratchpad/art/Pack-2e-az-Zukhruf-collectif.pptx"

def s_consigne(titre, lignes, pied):
    sl = prs.slides.add_slide(BLANK)
    rect(sl, 0, 0, W, H, GOLD)
    _, tf = tb(sl, 150, 120, W - 300, 150, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP)
    para(tf, "À INSÉRER DANS TON DECK", POP, 32, INK, bold=True, align=PP_ALIGN.LEFT, first=True)
    _, tf2 = tb(sl, 150, 240, W - 300, 200, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP)
    para(tf2, titre.upper(), ARCH, 74, INK, bold=True, italic=True, align=PP_ALIGN.LEFT, lh=1.06, first=True)
    rect(sl, 150, 480, 260, 8, INK)
    _, tf3 = tb(sl, 150, 540, W - 300, 360, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP)
    for i, (mot, txt) in enumerate(lignes):
        para(tf3, mot, POP, 30, INK, bold=True, align=PP_ALIGN.LEFT, space=6, first=(i == 0))
        para(tf3, txt, POP, 36, INK, align=PP_ALIGN.LEFT, lh=1.32, space=22)
    _, tf4 = tb(sl, 150, 935, W - 300, 70, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP)
    para(tf4, pied, POP, 28, INK, italic=True, align=PP_ALIGN.LEFT, first=True)
    sl.notes_slide.notes_text_frame.text = "CONSIGNE — ne pas conserver cette page dans le deck final."

s_consigne("az-Zukhruf 43:32", [
 ("LA SLIDE DEMANDÉE", "c'est la suivante, page 2 : le verset."),
 ("APRÈS ta slide", "« CE QUE L'ABONDANCE PERMET » — Ibn ʿAwf et le tiers de Médine"),
 ("AVANT ta slide", "« يَدُ اللَّهِ مَعَ الْجَمَاعَةِ / La Main d'Allah est avec le groupe »"),
 ("LES PAGES 3 À 6", "sont facultatives : elles déplient le verset si tu veux y passer du temps."),
], "Prends la page 2 seule, ou le bloc entier. Cette page-ci ne va pas dans le deck.")

s_citation(["« C'est Nous qui avons réparti entre eux leur subsistance dans la vie présente,",
            "et Nous avons élevé en grades les uns au-dessus des autres,",
            "afin que les uns prennent les autres à leur service. »",
            "Sourate az-Zukhruf, 43:32",
            "﴿ وَرَفَعْنَا بَعْضَهُمْ فَوْقَ بَعْضٍ دَرَجَاتٍ لِّيَتَّخِذَ بَعْضُهُم بَعْضًا سُخْرِيًّا ﴾"],
 "C'est le verset que cite le Dr Chauki Lazhar sur l'interdépendance. Attention au mot سخريا : "
 "il désigne ici le fait de prendre l'autre à son service, l'entraide fonctionnelle — pas la "
 "moquerie. C'est la lecture retenue par les traducteurs classiques, Hamidullah compris. "
 "Chaîne et traduction à faire confirmer par Oussama avant le direct.")

s_titre(["POURQUOI PERSONNE", "N'A TOUT ?"],
 "FACULTATIF — slide d'ouverture, à placer AVANT le verset si tu veux poser la question au chat. "
 "Pourquoi est-ce que personne, jamais, n'a toutes les compétences, tout le capital, tout le "
 "réseau ? Les réponses parleront de hasard, de chance, d'injustice. Le verset répond autre chose.")

s_liste(["LIRE CE QU'IL DIT EXACTEMENT",
 "Il ne dit pas : soyez solidaires",
 "Il dit que les dotations sont INÉGALES — et que c'est voulu",
 "Et il donne la raison : pour que les uns prennent les autres à leur service",
 "👉 L'inégalité n'est pas un défaut du monde. C'est une fonction."],
 "FACULTATIF. Insister sur la deuxième ligne. C'est contre-intuitif et c'est tout le poids du verset : "
 "l'inégalité des dotations est décrite comme intentionnelle, et sa fonction est de rendre les "
 "gens nécessaires les uns aux autres.")

s_punch(["Si tu avais tout,",
         "tu n'aurais besoin de personne.",
         "Et personne n'aurait besoin de toi."],
 "FACULTATIF. Le dire calmement : c'est la traduction du verset en une phrase que tout le monde "
 "comprend. Enchaîner sur : l'interdépendance n'est pas un accident du système, c'est le design.")

s_punch(["Alors le self-made man n'est pas seulement",
         "une erreur de fait.",
         "C'est une négation de la fonction de l'inégalité."],
 "FACULTATIF. Enchaîner sur le hadith « la Main d'Allah est avec le groupe ». Et rappeler que le Prophète ﷺ "
 "avait un associé, avait des compagnons, et pratiquait la choura — il demandait l'avis des "
 "autres malgré la révélation.")

prs.save(OUT)
print("6 pages ->", OUT, os.path.getsize(OUT), "octets")
