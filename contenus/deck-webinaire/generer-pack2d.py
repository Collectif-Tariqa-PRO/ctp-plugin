# -*- coding: utf-8 -*-
exec(open("/tmp/claude-0/webi/gabarits.py").read())
OUT = "/tmp/claude-0/-home-user-ctp-plugin/5bde7487-de28-5f85-acc6-6f6c831c1436/scratchpad/art/Pack-2d-Urwa-al-Bariqi.pptx"

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

s_consigne("ʿUrwa al-Bāriqī, version longue", [
 ("REMPLACE", "ta slide « ʿURWA AL-BĀRIQĪ » et sa liste de quatre lignes"),
 ("DONC APRÈS", "« QUE DIEU FASSE MISÉRICORDE À L'HOMME INDULGENT… »"),
 ("ET AVANT", "« C'est l'opération qui est bénie. L'acte d'échanger. Pas le solde. »"),
 ("CELLE-LÀ", "tu la gardes : elle clôt le bloc."),
], "Les 7 slides qui suivent forment le bloc. Cette page-ci ne va pas dans le deck.")

s_titre(["EST-CE QU'IL Y A UN PROBLÈME", "À BIEN MARGER ?"],
 "Poser la question franchement, en regardant la caméra. C'est la question que tout le monde se "
 "pose depuis le début de l'axe et que personne n'ose formuler. Si tu ne la poses pas toi-même, "
 "le public entendra tout le reste comme une condamnation du profit.")

s_liste(["CE QU'ON N'EST PAS EN TRAIN DE DIRE",
 "❌ Que le profit serait suspect",
 "❌ Qu'il faudrait vendre au prix coûtant",
 "❌ Qu'une grosse marge serait un péché",
 "👉 Rien de tout ça. Le profit est licite, et le commerce est un chemin noble."],
 "Insister : se sous-vendre trahit la valeur qu'on apporte, appauvrit l'entrepreneur, et finit par "
 "priver ses clients d'un service qui n'existera plus. Il ne faut pas se complexer avec l'argent "
 "gagné honnêtement.")

s_punch(["Alors prenons quelqu'un",
         "qui a doublé sa mise en une seule opération.",
         "Et regardons ce que le Prophète ﷺ lui a dit."],
 "Ménager le suspense : le public s'attend à un reproche.")

s_titre(["ʿURWA IBN AL-JAʿD", "AL-BĀRIQĪ"],
 "Compagnon du Prophète ﷺ. Le récit est rapporté par al-Bukhârî. Prendre le temps de le raconter "
 "comme une histoire, pas comme une référence.")

s_liste(["UN DINAR, ET CE QU'IL EN A FAIT",
 "Le Prophète ﷺ lui confie un dinar pour lui acheter une bête",
 "Il en achète deux pour ce même dinar",
 "Il en revend une, sur place, pour un dinar",
 "Il revient avec la bête demandée — et le dinar intact",
 "On rapporte qu'ensuite, s'il avait acheté de la poussière, il y aurait fait du profit"],
 "La dernière ligne est à vérifier dans sa formulation exacte (« لو اشترى التراب لربح فيه ») — "
 "à faire confirmer par Oussama avant le direct. Elle est magnifique mais ne la cite pas comme "
 "texte si le doute subsiste : dis simplement « on rapporte que ».")

s_punch(["Cent pour cent de marge.",
         "En une seule transaction.",
         "Et il n'a pas été repris."],
 "Laisser un temps. C'est la réponse à la question posée quatre slides plus haut.")

s_citation(["« Que Dieu te bénisse dans la transaction de ta main droite. »",
            "L'invocation du Prophète ﷺ pour ʿUrwa — rapporté par al-Bukhârî",
            "« بَارَكَ اللَّهُ لَكَ فِي صَفْقَةِ يَمِينِكَ »"],
 "Formulation de l'invocation à faire valider par Oussama : plusieurs versions circulent. "
 "Le point qui compte et qui ne fait pas débat : l'invocation porte sur le COMMERCE, sur "
 "l'opération — pas sur le montant obtenu. Il n'a pas été félicité d'avoir gagné un dinar. "
 "Il a été béni dans sa manière de commercer.")

s_punch(["Ce n'est pas le gain qui est béni.",
         "C'est la façon dont il a été fait."],
 "Enchaîner directement sur ta slide suivante : « C'est l'opération qui est bénie. L'acte "
 "d'échanger. Pas le solde. »")

prs.save(OUT)
print("8 pages ->", OUT, os.path.getsize(OUT), "octets")
