# -*- coding: utf-8 -*-
exec(open("/tmp/claude-0/webi/gabarits.py").read())
OUT = "/tmp/claude-0/-home-user-ctp-plugin/5bde7487-de28-5f85-acc6-6f6c831c1436/scratchpad/art/Pack-2f-deux-savants.pptx"

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

s_consigne("Deux savants — version tenable", [
 ("REMPLACE", "l'ancienne slide VS « LE PREMIER / AL-GHAZÂLÎ »"),
 ("SE PLACE", "dans la partie 3, juste après la citation de Chauki Lazhar"),
 ("", "« L'idée n'est pas de tout rejeter… »"),
 ("LE PREMIER", "reste sans nom — c'est volontaire, et c'est fidèle à la source."),
], "Les 4 slides qui suivent forment le bloc. Cette page-ci ne va pas dans le deck.")

s_titre(["DEUX SAVANTS,", "LA MÊME BIBLIOTHÈQUE"],
 "Poser le décor : au Xe et XIe siècle, toute la philosophie grecque est traduite en arabe et "
 "disponible. Aristote, Platon, les néoplatoniciens. Tous les savants de l'époque y ont accès. "
 "La question n'est pas s'ils l'ont lue — ils l'ont tous lue. La question est COMMENT.")

s_vs(dict(
 lt="Il y entre sans cadre",
 li=["Il cherche la vérité dans ces textes",
     "Il adopte leurs questions — puis leurs réponses",
     "« Il est rentré dans le ventre des philosophes,",
     "il a voulu en sortir, il n'a pas réussi »"],
 rt="Al-Ghazâlî y entre avec un cadre",
 ri=["Il apprend leur système à fond, et l'expose",
     "Il le réfute, point par point",
     "Puis il garde l'outil — la logique —",
     "et l'intègre aux fondements du droit"],
 sep="VS"),
 "Ce que Ghazâlî a réellement fait, dans l'ordre, si on te pose la question : il écrit d'abord un "
 "exposé fidèle des doctrines des philosophes, puis leur réfutation, puis il place un traité de "
 "logique en ouverture de son grand ouvrage de usūl al-fiqh. Il prend l'outil, il le détache de sa "
 "métaphysique d'origine, il le remet au service du droit musulman. C'est exactement le geste "
 "qu'on demande aux entrepreneurs avec les techniques modernes.")

s_punch(["Même matière. Deux issues opposées.",
         "La différence n'est pas l'intelligence.",
         "C'est d'avoir un cadre avant d'entrer."],
 "C'est la charnière de toute la partie 3. Le dire lentement.")

s_punch(["Sans cadre, tu ne recycles pas les outils.",
         "Ce sont eux qui te recyclent."],
 "Formule tirée du corpus Chauki Lazhar. Enchaîner sur les deux questions à poser avant "
 "d'adopter un outil.")

prs.save(OUT)
print("5 pages ->", OUT, os.path.getsize(OUT), "octets")
