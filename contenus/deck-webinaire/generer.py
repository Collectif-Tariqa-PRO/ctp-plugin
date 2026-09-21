# -*- coding: utf-8 -*-
import json, os, html

ROOT = "/tmp/claude-0/-home-user-ctp-plugin/5bde7487-de28-5f85-acc6-6f6c831c1436/scratchpad/deck"
SL = os.path.join(ROOT, "project", "slides")
os.makedirs(SL, exist_ok=True)

INK    = "#1A2420"
BODY   = "#4E5B55"
PAPER  = "#FAF7F0"
PAPER2 = "#F1ECE1"
DEEP   = "#19342C"
DEEP2  = "#12261F"
OCHRE  = "#8A5A28"
OCHRE_L= "#D9A96A"
LIGHTTX= "#F3EFE6"
LIGHTBD= "#C3D2CA"
LINE   = "#DDD5C6"

DISP = "'EB Garamond', Georgia, serif"
SANS = "'IBM Plex Sans', Arial, sans-serif"

ORDER = []
SLIDES = {}
NOTES = {}

def add(sid, body, notes=None):
    ORDER.append(sid)
    SLIDES[sid] = body
    if notes: NOTES[sid] = notes

def esc(t): return t

def sec(sid, style, inner, notes=None, transition="fade"):
    a = ("\n  <aside>%s</aside>" % notes) if notes else ""
    return '<section id="%s" data-transition="%s" style="%s">\n%s%s\n</section>' % (sid, transition, style, inner, a)

def light_style(pad="128px", bg=PAPER, extra="display:flex; flex-direction:column; gap:40px"):
    return "background:%s; color:%s; font-family:%s; padding:%s; %s" % (bg, INK, SANS, pad, extra)

def dark_style(pad="128px", bg=DEEP, extra="display:flex; flex-direction:column; gap:40px"):
    return "background:%s; color:%s; font-family:%s; padding:%s; %s" % (bg, LIGHTTX, SANS, pad, extra)

def eyebrow(t, color=OCHRE):
    return '  <p style="font-size:26px; font-weight:600; letter-spacing:3px; text-transform:uppercase; color:%s">%s</p>' % (color, t)

def h2(t, color=None):
    c = color or INK
    return '  <h2 style="font-family:%s; font-size:68px; font-weight:500; line-height:1.1; color:%s">%s</h2>' % (DISP, c, t)

def footer(t, color=BODY):
    return '  <p style="position:absolute; left:128px; bottom:64px; font-size:24px; letter-spacing:2px; text-transform:uppercase; color:%s">%s</p>' % (color, t)

def card(title, text, bg="#FFFFFF", bd=LINE, tc=INK, bodyc=BODY, flex="1"):
    inner = '      <h3 style="font-family:%s; font-size:36px; font-weight:600; line-height:1.2; color:%s">%s</h3>\n' % (DISP, tc, title)
    if text:
        inner += '      <p style="font-size:29px; line-height:1.45; color:%s">%s</p>\n' % (bodyc, text)
    return ('    <div style="flex:%s; display:flex; flex-direction:column; gap:18px; background:%s; padding:40px; '
            'border:1px solid %s; border-radius:14px">\n%s    </div>' % (flex, bg, bd, inner))

def bullets(items, size=32, color=BODY, gap=16):
    li = "\n".join('      <li style="font-size:%dpx; line-height:1.45; color:%s">%s</li>' % (size, color, i) for i in items)
    return '    <ul style="display:flex; flex-direction:column; gap:%dpx">\n%s\n    </ul>' % (gap, li)

# ---------------------------------------------------------------- templates

def slide_bullets(sid, eb, title, items, foot=None, notes=None, bg=PAPER, size=32):
    pad = "128px 128px 160px" if foot else "128px"
    inner = eyebrow(eb) + "\n" + h2(title) + "\n" + bullets(items, size=size)
    if foot: inner += "\n" + footer(foot)
    return sec(sid, light_style(pad, bg), inner, notes)

def slide_cards(sid, eb, title, cards, foot=None, notes=None, bg=PAPER, lead=None):
    pad = "128px 128px 160px" if foot else "128px"
    inner = eyebrow(eb) + "\n" + h2(title)
    if lead:
        inner += '\n  <p style="font-size:32px; line-height:1.45; color:%s">%s</p>' % (BODY, lead)
    inner += '\n  <div style="display:flex; gap:32px; align-items:stretch">\n' + "\n".join(cards) + "\n  </div>"
    if foot: inner += "\n" + footer(foot)
    return sec(sid, light_style(pad, bg), inner, notes)

def slide_contrast(sid, eb, title, l_title, l_items, r_title, r_items, foot=None, notes=None):
    pad = "128px 128px 160px" if foot else "128px"
    def col(t, items, bg, bd, tc, bc, lab, labc):
        li = "\n".join('        <li style="font-size:27px; line-height:1.45; color:%s">%s</li>' % (bc, i) for i in items)
        return ('    <div style="flex:1; display:flex; flex-direction:column; gap:18px; background:%s; padding:36px; '
                'border:1px solid %s; border-radius:14px">\n'
                '      <p style="font-size:24px; font-weight:600; letter-spacing:3px; text-transform:uppercase; color:%s">%s</p>\n'
                '      <h3 style="font-family:%s; font-size:36px; font-weight:600; line-height:1.15; color:%s">%s</h3>\n'
                '      <ul style="display:flex; flex-direction:column; gap:12px">\n%s\n      </ul>\n'
                '    </div>' % (bg, bd, labc, lab, DISP, tc, t, li))
    left  = col(l_title, l_items, PAPER2, LINE, INK, BODY, "Le paradigme dominant", OCHRE)
    right = col(r_title, r_items, DEEP, DEEP, LIGHTTX, LIGHTBD, "Notre paradigme", OCHRE_L)
    inner = eyebrow(eb) + "\n" + h2(title) + '\n  <div style="display:flex; gap:32px; align-items:stretch">\n' + left + "\n" + right + "\n  </div>"
    if foot: inner += "\n" + footer(foot)
    return sec(sid, light_style(pad, PAPER), inner, notes)

def slide_quote(sid, quote, attrib, notes=None, bg=DEEP, sub=None):
    inner = ('  <div style="flex:1"></div>\n'
             '  <p style="font-family:%s; font-size:76px; font-weight:400; font-style:italic; line-height:1.18; color:%s">%s</p>\n'
             % (DISP, LIGHTTX, quote))
    if sub:
        inner += '  <p style="font-size:32px; line-height:1.45; color:%s">%s</p>\n' % (LIGHTBD, sub)
    inner += ('  <p style="font-size:28px; letter-spacing:2px; text-transform:uppercase; color:%s">%s</p>\n'
              '  <div style="flex:1"></div>' % (OCHRE_L, attrib))
    return sec(sid, dark_style("128px", bg, "display:flex; flex-direction:column; gap:36px; justify-content:center"), inner, notes)

def slide_divider(sid, num, title, question, notes=None):
    inner = ('  <div style="flex:1"></div>\n'
             '  <p style="font-size:30px; font-weight:600; letter-spacing:5px; text-transform:uppercase; color:%s">Axe %s</p>\n'
             '  <h1 style="font-family:%s; font-size:132px; font-weight:500; line-height:1.02; color:%s">%s</h1>\n'
             '  <hr style="width:280px; height:3px; border:none; background:%s">\n'
             '  <p style="font-size:44px; line-height:1.3; font-style:italic; color:%s">%s</p>\n'
             '  <div style="flex:1"></div>'
             % (OCHRE_L, num, DISP, LIGHTTX, title, OCHRE_L, LIGHTBD, question))
    return sec(sid, dark_style("128px", DEEP2, "display:flex; flex-direction:column; gap:32px; justify-content:center"), inner, notes, transition="push")

def slide_sources(sid, eb, title, entries, foot=None, notes=None):
    """entries: list of (texte, référence)"""
    pad = "128px 128px 160px" if foot else "128px"
    rows = []
    for t, r in entries:
        rows.append('    <div style="display:flex; flex-direction:column; gap:10px; padding:0 0 0 32px; border-left:3px solid %s">\n'
                    '      <p style="font-family:%s; font-size:34px; font-style:italic; line-height:1.3; color:%s">%s</p>\n'
                    '      <p style="font-size:26px; letter-spacing:1px; color:%s">%s</p>\n'
                    '    </div>' % (OCHRE, DISP, INK, t, BODY, r))
    inner = eyebrow(eb) + "\n" + h2(title) + '\n  <div style="display:flex; flex-direction:column; gap:32px">\n' + "\n".join(rows) + "\n  </div>"
    if foot: inner += "\n" + footer(foot)
    return sec(sid, light_style(pad, PAPER), inner, notes)

def slide_lundi(sid, axe, items, notes=None):
    li = "\n".join('      <li style="font-size:36px; line-height:1.4; color:%s">%s</li>' % (BODY, i) for i in items)
    inner = (eyebrow("Ce que ça change lundi") + "\n" +
             h2(axe) + "\n"
             '  <div style="background:%s; padding:56px; border:1px solid %s; border-radius:14px">\n'
             '    <ul style="display:flex; flex-direction:column; gap:26px">\n%s\n    </ul>\n  </div>' % (PAPER2, LINE, li))
    return sec(sid, light_style("128px", PAPER), inner, notes)

def slide_table(sid, eb, title, headers, rows, widths, foot=None, notes=None, size=28):
    pad = "128px 128px 160px" if foot else "128px"
    th = "".join('<th style="width:%s; text-align:left; font-size:%dpx; font-weight:600; color:%s">%s</th>' % (w, size, INK, h) for w, h in zip(widths, headers))
    trs = ['    <tr style="background:%s">%s</tr>' % (PAPER2, th)]
    for i, r in enumerate(rows):
        tds = "".join('<td style="font-size:%dpx; color:%s">%s</td>' % (size, BODY, c) for c in r)
        trs.append('    <tr style="background:%s">%s</tr>' % ("#FFFFFF" if i % 2 == 0 else PAPER, tds))
    tbl = ('  <table style="font-family:%s; font-size:%dpx; border:1px solid %s; border-radius:10px; padding:16px">\n%s\n  </table>'
           % (SANS, size, LINE, "\n".join(trs)))
    inner = eyebrow(eb) + "\n" + h2(title) + "\n" + tbl
    if foot: inner += "\n" + footer(foot)
    return sec(sid, light_style(pad, PAPER), inner, notes)

# ================================================================ CONTENU

# ---------- OUVERTURE
add("cover", sec("cover", dark_style("128px", DEEP, "display:flex; flex-direction:column; justify-content:space-between"),
 '  <p style="font-size:28px; font-weight:600; letter-spacing:5px; text-transform:uppercase; color:%s">Collectif Tariqa PRO &middot; Webinaire</p>\n'
 '  <div style="display:flex; flex-direction:column; gap:32px">\n'
 '    <h1 style="font-family:%s; font-size:150px; font-weight:500; line-height:1.0; color:%s">Héritage<br>&amp; Modernité</h1>\n'
 '    <hr style="width:320px; height:3px; border:none; background:%s">\n'
 '    <p style="font-size:46px; line-height:1.3; color:%s">Le paradigme de l\'entrepreneur musulman</p>\n'
 '  </div>\n'
 '  <div style="display:flex; justify-content:space-between; align-items:end">\n'
 '    <p style="font-size:30px; color:%s">Zaki Chairi &nbsp;&middot;&nbsp; Oussama Jammal</p>\n'
 '    <p style="font-size:30px; color:%s">Jeudi 24 septembre 2026 &middot; 20h</p>\n'
 '  </div>' % (OCHRE_L, DISP, LIGHTTX, OCHRE_L, LIGHTBD, LIGHTBD, LIGHTBD),
 "Accueil. Deux minutes : qui on est, pourquoi ce format long, et la promesse de la soirée. Dire d'emblée : ce soir on ne parle pas de techniques, on parle de ce qui commande les techniques."))

add("pourquoi", slide_cards("pourquoi", "Ouverture", "Pourquoi ce sujet, et pourquoi maintenant",
 [card("On a nettoyé la surface", "Le riba, l'associé douteux, le produit illicite. Ce travail était nécessaire et il a été fait sérieusement."),
  card("Les racines n'ont pas bougé", "La définition de la réussite, du client, de la croissance, du concurrent. Personne ne l'a jamais posée sur la table."),
  card("Et ça se paie", "Des entrepreneurs irréprochables sur le licite, épuisés par un modèle qu'ils n'ont pas choisi.")],
 notes="Le constat de départ. Insister : ce n'est pas un procès de ceux qui ont fait le travail du halal. C'est la suite de ce travail. On a fait le comment, on n'a pas fait le vers quoi. Raconter un ou deux cas vus en accompagnement cette année, sans nommer."))

add("deja", slide_bullets("deja", "Ouverture", "Où ça te touche déjà, sans que tu l'aies décidé",
 ['<b style="color:%s">La valeur d\'une personne se mesure à sa notoriété.</b> On évalue un formateur au nombre de ses abonnés. On se compare, le soir, à des gens dont on ne connaît qu\'un compteur.' % INK,
  '<b style="color:%s">L\'impact se mesure en chiffres.</b> Un accompagnement qui a changé trois familles ne pèse rien face à une capture d\'écran de tableau de bord.' % INK,
  '<b style="color:%s">« Montre-moi ton chiffre d\'affaires et je saurai qui tu es. »</b> C\'est devenu la pièce d\'identité du milieu. On la présente avant de parler.' % INK],
 notes="Trois convictions que tout le monde partage et que personne n'a choisies. Demander à la salle en direct : qui a déjà jugé quelqu'un sur son nombre d'abonnés cette semaine ? Laisser le silence faire. Ce ne sont pas des techniques : ce sont des réponses à la question « qu'est-ce qui donne de la valeur à une vie »."))

add("prophetes", slide_quote("prophetes",
 "Un prophète sans un seul disciple n'est pas un mauvais prophète.",
 "Il a accompli sa mission. Le résultat n'était pas son département.",
 notes="Le moment le plus important de l'introduction. Rappeler qu'il est rapporté que certains prophètes sont venus avec une poignée de suiveurs, certains avec deux ou trois, certains avec personne. Si la valeur d'une mission se mesurait à l'audience, ce serait faux de l'affirmer. Donc la valeur se mesure ailleurs. Puis appliquer : la publication qui n'a pas marché ne dit rien de toi. Le lancement raté ne dit rien de toi. Le concurrent qui a dix fois ton audience n'a pas dix fois ta valeur — il a dix fois ton audience.",
 sub=None))

add("paradigme", slide_cards("paradigme", "Ouverture", "Un paradigme, c'est ce avec quoi tu penses",
 [card("Invisible", "Tu ne le regardes pas : tu regardes à travers."),
  card("Global", "Il ne dit pas quoi penser sur un sujet. Il dit ce qui compte."),
  card("Hérité", "Personne ne t'a demandé ton avis. Tu l'as attrapé."),
  card("Résistant", "Il encaisse les objections sans bouger, parce qu'il définit ce qui compte comme objection.")],
 notes="Court : 3 minutes. Le mot vient de Kuhn, il décrit ce qu'une communauté scientifique tient pour évident sans le discuter. Analogie des lunettes : tu ne les vois pas, tu vois avec. Et surtout : un paradigme contient toujours quatre choses — une anthropologie (c'est quoi un humain), une finalité (pour quoi il est là), une théorie de la valeur (qu'est-ce qui compte), une eschatologie (qu'est-ce qui reste à la fin)."))

add("filtre", slide_contrast("filtre", "Ouverture", "Pourquoi le filtre halal/haram ne suffit pas",
 "Le filtre opère sur les actes", [
   "On regarde une pratique, on demande si elle est licite, on garde ou on jette.",
   "Nécessaire. Rien ici ne vise à l'affaiblir.",
   "Mais il traite un acte à la fois — jamais le cadre qui les produit."],
 "Un modèle importé produit des actes indéfiniment", [
   "On peut en filtrer un, puis dix, puis cent : la logique, elle, continue de produire.",
   "Dr Chauki Lazhar : jusqu'à la modernité les changements étaient <i>micro</i>. Aujourd'hui ils sont <i>structurels</i>.",
   "Dr Talal Lahlou : l'économie qu'on enseigne est « coupée de son ancrage philosophique »."],
 notes="Le cœur du diagnostic. Formule à poser lentement : tant qu'on ne questionne pas la vision du monde qui a produit un modèle, on passe sa vie à corriger ses effets. Exemple concret : on enlève la loi d'attraction d'une formation de développement personnel, on ajoute bismillah — et l'architecture reste intégralement centrée sur toi."))

add("pont", slide_cards("pont", "Ouverture", "Le patrimoine existe. Il est simplement inaccessible.",
 [card("Ce n'est pas un vide", "Le <i>fiqh al-mu&#703;āmalāt</i> est l'un des domaines les plus travaillés du droit musulman. Des bibliothèques entières sur la vente, la dette, l'association, le prix juste."),
  card("C'est un fossé", "Cette littérature s'adresse à des chercheurs. Elle ne rencontre jamais quelqu'un qui doit facturer un client vendredi."),
  card("Notre rôle : le pont", "Faire descendre une réflexion qui existe déjà chez les savants jusqu'à ceux qui sont dans l'opérationnel — sans la trahir en la simplifiant.")],
 notes="Poser la place du Collectif, sans fausse modestie et sans prétention. Nous ne sommes pas des savants et on ne découvre rien. Nous ne sommes pas non plus de simples vulgarisateurs, parce que traduire pour un praticien oblige à trancher des choses qu'un théoricien peut laisser ouvertes. On est entre les deux, et c'est cette place-là qui manque."))

add("plan", slide_bullets("plan", "Ouverture", "Six axes, une soirée",
 ['<b style="color:%s">1 &middot; La finalité</b> &nbsp;— c\'est quoi le but du jeu ?' % INK,
  '<b style="color:%s">2 &middot; La mesure</b> &nbsp;— qu\'est-ce que tu comptes, et quand est-ce que tu as gagné ?' % INK,
  '<b style="color:%s">3 &middot; Le profit et le risque</b> &nbsp;— la marge, ou la transaction ? Qui perd quoi ?' % INK,
  '<b style="color:%s">4 &middot; La croissance et la dette</b> &nbsp;— tu grandis parce que tu veux, ou parce que tu dois ?' % INK,
  '<b style="color:%s">5 &middot; La concurrence</b> &nbsp;— écraser, ou l\'abondance ?' % INK,
  '<b style="color:%s">6 &middot; Le client et l\'effet</b> &nbsp;— « il était d\'accord » suffit-il ? Et que produis-tu chez les gens ?' % INK],
 size=30,
 notes="Annoncer la structure. Préciser : ce ne sont pas six sujets indépendants. Il y en a un qui commande — la finalité — et cinq qui en découlent. Pour chacun : une scène concrète, ce que dit le paradigme dominant avec ses références, ce que dit le nôtre avec ses sources, et ce que ça change lundi matin."))

# ---------- AXE 1 : LA FINALITÉ
F1 = "Axe 1 &middot; La finalité"
add("a1", slide_divider("a1", "1", "La finalité", "C'est quoi le but du jeu ?",
 "Transition. Dire : si on ne règle que celui-là ce soir, la soirée est rentable. Les cinq autres en découlent."))

add("a1-scene", slide_quote("a1-scene",
 "Quel est le premier chiffre que tu regardes le matin ?",
 "La scène",
 sub="Ce chiffre est ton tableau de score. Tu ne l'as pas choisi — personne ne t'a jamais demandé ton avis. Tu l'as attrapé.",
 notes="Faire répondre la salle dans le chat. Solde bancaire, ventes de la nuit, vues, abonnés, messages. Ne pas commenter tout de suite : laisser défiler. Puis : ce que tu regardes en premier, c'est ce que tu sers."))

add("a1-contrast", slide_contrast("a1-contrast", F1, "Deux réponses à la même question",
 "Le but, c'est le score", [
   "Milton Friedman, 1970 : « la responsabilité sociale de l'entreprise, c'est d'augmenter ses profits ».",
   "Alex Hormozi : une offre si bonne qu'on se sentirait bête de dire non. Tout est ramené au ratio.",
   "Grant Cardone : <i>Be obsessed or be average</i>. L'obsession devient une vertu.",
   "L'éthique, la santé, la famille, le sommeil ne sont pas niés. Ils deviennent des contraintes à optimiser autour du score."],
 "Le but, c'est l'agrément de Dieu", [
   "Le commerce est un des chemins qui y mènent — celui-ci est le tien.",
   "L'argent est un moyen puissant d'y avancer. Ce n'est pas un renoncement, c'est un changement de rang.",
   "La question n'est donc pas « comment faire entrer mon business dans le halal », mais « comment marche-t-on correctement sur ce chemin-là ».",
   "Ibn &#703;Awf est mort immensément riche. Ce n'était pas un accident de parcours."],
 foot=F1,
 notes="Attention au contresens : on ne demande à personne de gagner moins. La piété n'est pas la pauvreté. Ce qui change n'est pas le montant, c'est le rang qu'il occupe dans la hiérarchie de ce qui compte, et ce qu'on en fait. Sur Hormozi : ses techniques marchent, on en utilise. Le problème n'est pas la technique, c'est ce qu'elle suppose sur ce qu'est une vie réussie."))

add("a1-sources", slide_sources("a1-sources", F1, "Ce qui fonde ça",
 [("« On l'appelle capitalisme. On ne l'appelle pas <i>travaillisme</i> — parce qu'inconsciemment, ce qui a le plus de valeur, c'est le matériel, ce n'est pas l'humain. »",
   "Dr Mohamed Talal Lahlou &middot; un système dit ce qu'il met au centre par le mot qu'il choisit pour se nommer"),
  ("« Dire <i>je ne me soumets ni à Dieu ni à rien d'autre, je suis libre</i> — ça n'existe pas. »",
   "Dr Chauki Lazhar &middot; ou Dieu, ou le <i>tāghūt</i> : l'ego, l'argent, les passions"),
  ("« Que Dieu te bénisse dans ta famille et tes biens — indiquez-moi seulement le marché. »",
   "&#703;Abd ar-Rahmān ibn &#703;Awf, refusant la moitié de la fortune de Sa&#703;d ibn ar-Rabī&#703;")],
 foot=F1,
 notes="Développer l'histoire d'Ibn 'Awf : il arrive à Médine après l'exil, il n'a plus rien. Un Médinois lui propose de partager sa fortune en deux. Il refuse et demande le chemin du marché. Il achète du beurre clarifié et du fromage sec, et il reconstruit. Punchline : un homme qui joue au Monopoly ne refuse pas la moitié de la banque. Ce refus ne s'explique que par une définition de la richesse où ce qu'on détient n'est pas ce qu'on est. Sur Chauki Lazhar : tu ne choisis pas entre servir et ne pas servir. Tu choisis qui tu sers."))

add("a1-lundi", slide_lundi("a1-lundi", "La finalité",
 ["Écris en une phrase : « je fais ce business pour ______ ».",
  "Ouvre ton agenda de la semaine écoulée.",
  "Est-ce qu'il confirme la phrase, ou est-ce qu'il la contredit ?"],
 "Exercice à faire en direct, 90 secondes, chacun écrit sa phrase dans le chat s'il veut. Le décalage entre la phrase et l'agenda, c'est exactement la mesure de l'écart entre le paradigme qu'on croit avoir et celui qu'on a."))

# ---------- AXE 2 : LA MESURE
F2 = "Axe 2 &middot; La mesure"
add("a2", slide_divider("a2", "2", "La mesure", "Qu'est-ce que tu comptes — et quand est-ce que tu as gagné ?",
 "Transition : la finalité se trahit toujours quelque part. Elle se trahit dans le tableau de bord."))

add("a2-scene", slide_quote("a2-scene",
 "Ouvre ton tableau de bord et compte les lignes. Combien sont des nombres ?",
 "La scène",
 sub="Si la réponse est « toutes », tu tiens là l'objet le plus idéologique de ton entreprise — et le plus invisible, parce qu'il a l'air d'un simple outil de suivi.",
 notes="Faire l'exercice en direct : que chacun ouvre vraiment son tableau, son Notion, son carnet. Compter. Le silence qui suit fait le travail."))

add("a2-contrast", slide_contrast("a2-contrast", F2, "Deux façons de savoir si tu as gagné",
 "Orienté résultat", [
   "« What gets measured gets managed » — la formule attribuée à Peter Drucker, devenue le catéchisme du pilotage.",
   "Ce qui n'est pas mesurable ne disparaît pas parce qu'on l'a jugé sans valeur. Il disparaît parce qu'il n'a pas de case.",
   "Tu as gagné quand le virement est arrivé. Le chemin est un coût qu'on minimise.",
   "Un mois creux devient une remise en cause de ta valeur personnelle."],
 "Orienté commandement", [
   "Tu vends ta voiture, elle a un défaut que l'acheteur ne verra pas. Tu le dis en premier.",
   "L'acheteur s'en va ? Tu n'as pas raté ta vente : tu as réussi ton commandement.",
   "Fais les causes — le résultat appartient à Dieu. Donc le résultat cesse d'être ton département.",
   "Très concrètement : c'est ce qui permet de traverser un trimestre difficile sans que ton identité soit en jeu."],
 foot=F2,
 notes="Couper tout de suite la dérive : « donc on peut être médiocre du moment qu'on est honnête ». Non. Être orienté commandement veut dire exécuter MIEUX, pas moins. L'ihsan fait partie de l'ordre reçu. Ce n'est pas un permis de bâcler, c'est une exigence de plus. Cet axe vient d'Oussama Al Shurafa : la réussite comme accomplissement de l'ordre plutôt que comme obtention du résultat."))

add("a2-sources", slide_sources("a2-sources", F2, "Ce qui fonde ça",
 [("« La course au <i>plus</i> vous a distraits, jusqu'à ce que vous visitiez les tombes. »",
   "Sourate at-Takāthur &middot; le mot désigne l'accumulation <i>comparative</i> — non pas le fait d'avoir, mais d'en vouloir plus que"),
  ("Un martyr, un savant qui a enseigné, un riche qui a beaucoup donné. Trois résultats spectaculaires. Les trois sont rejetés, pour la même raison : ils l'ont fait pour qu'on le dise, et on l'a dit.",
   "Le hadith des trois premiers jugés &middot; aucun texte ne dit plus durement que le résultat visible ne prouve rien"),
  ("« Le matériel ne donne pas de valeur. Le bois, le fer, les diamants ne vous disent pas ce qui est bien et ce qui est mal. Or on a besoin de morale dans le monde économique. »",
   "Dr Mohamed Talal Lahlou"),
  ("« Lorsque tu as de l'argent et que tu donnes facilement. »",
   "Dr Chauki Lazhar, interrogé sur le critère qui permet de juger de son propre équilibre")],
 foot=F2,
 notes="Le dernier est le plus utile : un indicateur d'état spirituel qui se vérifie dans un relevé bancaire, et qui ne peut pas être simulé longtemps. Mentionner aussi Ibn Khaldoun, qui pose des critères de succès non matériels. Et la formule du management prophétique enseigné par Médine Académie : quantification et primauté du nombre, marginalisation de l'intuition et de l'intelligence du cœur."))

add("a2-lundi", slide_lundi("a2-lundi", "La mesure",
 ["Ajoute une ligne <b>non chiffrable</b> à ton tableau de bord — et place-la en premier.",
  "Par exemple : à qui ai-je été utile cette semaine, sans contrepartie ?",
  "Chaque semaine, note une décision où tu as tenu alors que ça t'a coûté. Au même endroit que tes chiffres, pas ailleurs."],
 "Insister sur « au même endroit ». Une ligne éthique rangée dans un carnet séparé est une ligne qu'on ne lit jamais. Le simple fait de devoir la remplir déplace l'attention."))

# ---------- AXE 3 : LE PROFIT ET LE RISQUE
F3 = "Axe 3 &middot; Le profit et le risque"
add("a3", slide_divider("a3", "3", "Le profit<br>et le risque", "La marge, ou la transaction ? Et qui perd quoi, si ça tourne mal ?",
 "Transition : on passe du cap à l'argent. Deux questions qu'on ne relie jamais et qui sont la même."))

add("a3-scene", slide_cards("a3-scene", F3, "Deux scènes que tout le monde a vécues",
 [card("La négociation", "Tu sens qu'il reste encore un peu à prendre. L'autre cédera. Tu peux serrer. La question n'est pas de savoir si tu en as le droit — tu l'as. La question est de savoir ce que tu décides."),
  card("L'associé", "Il veut trente pour cent des bénéfices. Tu lui demandes s'il prend trente pour cent des pertes. Le silence qui suit est la matière de cet axe.")],
 foot=F3,
 notes="Prendre les deux scènes séparément, avec des exemples de la salle. La deuxième fait mal parce qu'elle est fréquente : énormément d'associations chez nous sont bancales sur exactement ce point, sans que personne ne l'ait formulé."))

add("a3-contrast", slide_contrast("a3-contrast", F3, "Extraire, ou faire tourner",
 "Logique de marge et de transfert", [
   "Jeff Bezos : « votre marge est mon opportunité ». Le dernier euro laissé sur la table est une perte.",
   "Robert Kiyosaki : que l'argent travaille pour toi. L'idéal devient le rendement garanti d'avance.",
   "Le risque se déplace : vers le client, le fournisseur, le salarié, l'emprunteur.",
   "La négociation est un rapport de force dont on sort gagnant ou perdant."],
 "Logique de circulation et de portage", [
   "La bénédiction est dans l'échange, pas dans la marge. Ce qui tourne est béni.",
   "On laisse volontairement quelque chose — non par faiblesse, par principe.",
   "Un revenu est légitime quand il a une contrepartie : un travail déjà fourni, ou un risque réellement porté.",
   "Ibn &#703;Awf ne recommence pas par un gros coup : beurre et fromage. Petites marges, beaucoup de rotations."],
 foot=F3,
 notes="Lever tout de suite le malentendu qui paralyse : la ligne ne passe PAS entre le revenu qui exige ta présence et celui qui tombe sans toi. Un bien loué que tu entretiens et que tu peux perdre, une part de société dont tu assumes les pertes, un produit construit une fois qui continue de se vendre — tous ont une contrepartie. La ligne passe entre le gain qui a une cause et celui qui n'en a pas. Et l'autre contresens : « donc il faut vendre moins cher ». Non. Se sous-vendre trahit la valeur qu'on apporte et finit par priver ses clients d'un service qui n'existera plus. La formule est étroite : on laisse volontairement, on ne se fait pas prendre."))

add("a3-sources", slide_sources("a3-sources", F3, "Ce qui fonde ça",
 [("« Que Dieu fasse miséricorde à l'homme indulgent quand il vend, quand il achète, <b>et quand il réclame son dû</b>. »",
   "Trois moments. Le troisième est le plus exigeant : l'indulgence est demandée y compris lorsqu'on est dans son bon droit"),
  ("Le Prophète &#65018; confie un dinar à &#703;Urwa al-Bāriqī pour acheter un mouton. Il en achète deux, en revend un, et revient avec un mouton <i>et</i> le dinar. L'invocation ne porte pas sur le montant : « ô Dieu, bénis son commerce ».",
   "C'est l'opération qui est bénie — l'acte d'échanger, pas le solde"),
  ("« Dieu a rendu licite le commerce et illicite l'intérêt. »",
   "Deux voies de faire de l'argent. Une seule porte le risque"),
  ("Une <i>rémunération sans risque</i>.",
   "Ibn Khaldoun, nommant le problème quatre siècles avant qu'on ait le vocabulaire pour le discuter")],
 foot=F3,
 notes="La conséquence opératoire : celui qui prend une part du profit prend une part de la perte. Sinon ce n'est pas un associé, c'est un créancier déguisé, et le montage est bancal avant même d'être injuste. Dire un mot de la mudaraba et de la musharaka : ce ne sont pas des curiosités historiques, ce sont les structures qui rendent l'association honnête. Précision de prudence à dire à l'oral : on ne tranche aucune divergence entre écoles ce soir, et on ne qualifie aucun montage précis."))

add("a3-lundi", slide_lundi("a3-lundi", "Le profit et le risque",
 ["Sur un devis cette semaine, affiche la structure : voilà ce que ça me coûte, voilà ma marge, voilà le prix.",
  "Relis ton pacte d'associés — ou écris-le si tu n'en as pas.",
  "Une seule question suffit à révéler tous les déséquilibres : <b>qui perd quoi, si ça tourne mal ?</b>"],
 "Sur le devis transparent : sur un marché où tout le monde cache, c'est un différenciateur. À condition de connaître son coût réel, ce qui est loin d'être acquis — et c'est déjà un exercice en soi. Le prix devient un contrat de confiance au lieu d'un rapport de force."))

# ---------- AXE 4 : LA CROISSANCE ET LA DETTE
F4 = "Axe 4 &middot; La croissance et la dette"
add("a4", slide_divider("a4", "4", "La croissance<br>et la dette", "Tu grandis parce que tu veux, ou parce que tu dois ?",
 "C'est l'axe où on transforme un interdit en explication. Prévenir la salle : ce qui suit change la façon de lire sa propre entreprise."))

add("a4-scene", slide_quote("a4-scene",
 "« Il faut scaler. »",
 "La scène",
 sub="C'est une phrase qu'on entend comme une évidence. Posons la question naïve : pourquoi, au juste ?",
 notes="Laisser la question flotter. Personne n'a de réponse qui ne soit pas circulaire. « Parce que sinon on stagne. » Et alors ?"))

add("a4-contrast", slide_contrast("a4-contrast", F4, "Un impératif, ou une décision",
 "La croissance comme définition", [
   "Paul Graham : « une startup est une entreprise conçue pour croître vite ». La croissance n'est pas un objectif, c'est la définition.",
   "Robert Kiyosaki : la « bonne dette », celle qui achète des actifs. On t'apprend à t'endetter pour grandir.",
   "Le vocabulaire est le même partout : scaler, lever, accélérer, x10.",
   "Celui qui s'est endetté pour croître doit croître pour rembourser. Il n'a pas choisi l'expansion : il l'a contractée."],
 "La croissance comme choix", [
   "« Grandir n'est pas un gage de réussite. » — une phrase qui devrait figurer dans tous les cours de business plan.",
   "Il existe un mode croisière : rentable, autofinancé, sans dette, un rythme qu'on tient encore dans deux ans.",
   "Ce n'est pas un lot de consolation. Et il existe un mode croissance, qui coûte, et qui se décide en connaissance de cause.",
   "« Ton Seigneur a un droit sur toi, ton être a un droit sur toi, ta famille a un droit sur toi : donne à chacun son droit. »"],
 foot=F4,
 notes="Sur la dernière ligne : quand trois compagnons voulurent faire PLUS que le Prophète ﷺ — prier toute la nuit, jeûner sans cesse, renoncer au mariage — ils furent repris. Si le sacrifice total n'est pas permis pour l'adoration, il ne l'est pas pour ton entreprise. Le mot qui ne va pas dans « sacrifie-toi totalement », ce n'est pas « sacrifie », c'est « totalement »."))

add("a4-meca", slide_sources("a4-meca", F4, "Le mécanisme, et il est chiffré",
 [("« Tant qu'on ne comprendra pas que le système basé sur la dette et les intérêts implique une croissance nécessaire, inéluctable — et donc une surproduction, une saturation, une pollution, plus d'inégalité, et donc un impérialisme, parce que les marchés sont limités… »",
   "Dr Mohamed Talal Lahlou"),
  ("Un pays dont la dette atteint 100&nbsp;% du PIB, avec un intérêt de 2&nbsp;%, doit croître d'au moins 2&nbsp;% pour simplement payer ses intérêts. En dessous, il réemprunte pour rembourser : « on est dans un cycle Ponzi, c'est la fin assurée ».",
   "« C'est pour ça que la croissance est au centre de tous les programmes politiques »"),
  ("L'interdiction de l'intérêt n'est pas seulement une règle à respecter. C'est le <b>retrait du moteur</b> qui rend la croissance obligatoire.",
   "Ce que ce raisonnement change : un interdit devient une explication")],
 foot=F4,
 notes="C'est le moment le plus intellectuel de la soirée, prendre le temps. Refaire le calcul à voix haute, lentement, au tableau si possible. Puis redescendre immédiatement à l'échelle de l'entrepreneur : le même mécanisme joue sur ton crédit pro. Tu devras croître, puis croître encore, et tu découvriras un jour de fatigue que tu ne peux plus t'arrêter."))

add("a4-alt", slide_cards("a4-alt", F4, "« Mais quelle est l'alternative au crédit ? »",
 [card("La question est mal posée", "Il n'y a pas d'alternative au crédit. Il y a une alternative au <b>besoin</b> que le crédit finance. — Dr Talal Lahlou"),
  card("Donc : spécifie le besoin", "Financer un stock ? Une machine ? Un recrutement ? Chaque besoin a ses solutions : prévente, participation, structure dédiée par projet."),
  card("Et le versant intérieur", "« Si le fils d'Adam possédait une vallée d'or, il en voudrait une seconde. » La description clinique d'un appétit qui ne se referme jamais par satisfaction.")],
 foot=F4,
 notes="Le retournement de la question débloque beaucoup de situations concrètes — le dire comme un outil, pas comme une théorie. Ajouter : le Prophète ﷺ demandait explicitement refuge contre « le poids de la dette et l'oppression des hommes ». On demande refuge contre ce que le système pose comme moteur. Et l'objection à couper : « c'est une excuse pour manquer d'ambition ». Non. Soutenable ne veut pas dire confortable. Mais un modèle qui n'existe que parce que son fondateur ne dort pas n'est pas un modèle — et il ne passe pas à l'échelle non plus."))

add("a4-lundi", slide_lundi("a4-lundi", "La croissance et la dette",
 ["Une seule question, posée honnêtement : <b>ce rythme-là, est-ce que je le tiens encore dans deux ans ?</b>",
  "Si la réponse est non, ce n'est pas un problème de discipline.",
  "C'est un problème de modèle."],
 "Terminer le bloc là-dessus et laisser un silence. C'est la phrase que les gens retiennent : « l'incohérence de vie vient du business model initial ». On ne répare pas par la discipline un modèle mal posé."))

# ---------- AXE 5 : LA CONCURRENCE
F5 = "Axe 5 &middot; La concurrence"
add("a5", slide_divider("a5", "5", "La concurrence", "Écraser, ou l'abondance ?",
 "On passe aux autres. Cet axe est le plus physique : il se sent dans le ventre avant de se penser."))

add("a5-scene", slide_quote("a5-scene",
 "Un concurrent s'installe à deux cents mètres. Ton ventre se serre.",
 "La scène",
 sub="Cette réaction est antérieure à toute réflexion — et c'est précisément ce qui en fait le symptôme d'un paradigme, et non d'une opinion.",
 notes="Demander à la salle : qui a déjà ressenti ça ? Tout le monde. Puis : d'où vient cette contraction ? Elle a une cause précise, et on l'a déjà nommée."))

add("a5-contrast", slide_contrast("a5-contrast", F5, "Somme nulle, ou part assignée",
 "L'axiome de rareté", [
   "Peter Thiel : « la concurrence, c'est pour les perdants ». L'objectif avoué devient le monopole.",
   "Si les ressources sont structurellement insuffisantes, la part qu'il prend est celle que tu n'as pas.",
   "D'où : casser les prix, étouffer, verrouiller, racheter. L'école du requin a ses manuels et ses héros.",
   "La contraction de ton ventre devient une réponse rationnelle à une donnée du monde."],
 "Ce n'est pas une donnée du monde", [
   "« Toute chose a été créée à sa juste mesure. » Le <i>rizq</i> est déjà réparti ; la part de l'autre n'est pas dans ta poche.",
   "Les chiffres vont dans le même sens : on produit de quoi nourrir douze milliards de personnes pour huit milliards d'habitants — dont un milliard a faim.",
   "Le problème n'est pas la quantité disponible. C'est sa circulation.",
   "Dr Talal Lahlou y voit une mauvaise compréhension du risque autant qu'une erreur spirituelle."],
 foot=F5,
 notes="Poser le garde-fou tout de suite pour ne pas passer pour anti-marché : le Prophète ﷺ a refusé de fixer les prix quand on le lui a demandé, la propriété est protégée, le profit est licite. Talal Lahlou lui-même accorde que marchés, règles et concurrence forment un équilibre qu'on biaise en intervenant sans nécessité. L'islam n'est pas anti-marché. Il est anti-nuisance. La ligne rouge n'est pas la compétition, c'est l'ihtikar : accaparer des biens de première nécessité pour faire monter leur prix. Le critère est la nuisance."))

add("a5-regles", slide_table("a5-regles", F5, "Des règles techniques que presque personne ne connaît",
 ["Ce que la tradition interdit", "Ce que ça donne en 2026"],
 [["Vendre par-dessus la vente de son frère", "Intervenir au moment où une transaction est sur le point de se conclure"],
  ["Le <i>najsh</i> : faire monter une enchère sans intention d'acheter", "Le concurrent imaginaire invoqué en négociation, la fausse enchère"],
  ["Intercepter les caravanes avant leur arrivée au marché", "L'achat opportuniste à quelqu'un qui ignore encore la valeur de ce qu'il détient"],
  ["Profiter de ce que le vendeur ne sait pas encore des prix", "La fausse file d'attente, le « il ne me reste qu'une place » qui n'existe pas"]],
 ["50%", "50%"], foot=F5, size=28,
 notes="C'est le moment « ah ouais, ça veut dire ça en fait ». Ce sont des pratiques de croissance parfaitement courantes, enseignées dans des formations qu'on achète. Elles sont nommées et proscrites depuis quatorze siècles. Dire clairement : ce ne sont pas des principes vagues d'éthique, ce sont des règles techniques avec des noms."))

add("a5-ibnawf", slide_quote("a5-ibnawf",
 "Un tiers des commerçants d'une ville tournaient sur son capital.",
 "Ce que l'abondance permet concrètement",
 sub="On rapporte que les habitants de Médine vivaient tous d'Ibn &#703;Awf : un tiers lui empruntait son argent, un tiers avait ses dettes réglées par lui, un tiers recevait son aumône.",
 notes="Dans un monde à somme nulle, c'est littéralement inconcevable. Un homme dont la prospérité est la condition de celle des autres. C'est l'image à laisser sur cet axe. Préciser que la chaîne exacte de ce rapport est en cours de vérification avec Oussama — on le dit, ça ne coûte rien et ça vaut mieux."))

add("a5-lundi", slide_lundi("a5-lundi", "La concurrence",
 ["Recommande publiquement un concurrent, sur un cas précis où il est meilleur que toi.",
  "Ce n'est pas un exercice de générosité : c'est un diagnostic.",
  "Ce que tu ressens en le faisant t'apprendra où tu en es."],
 "Le proposer comme un défi de la semaine, avec retour dans la communauté. C'est l'action la plus simple et la plus révélatrice des six."))

# ---------- AXE 6 : LE CLIENT ET L'EFFET
F6 = "Axe 6 &middot; Le client et l'effet"
add("a6", slide_divider("a6", "6", "Le client<br>et l'effet", "« Il était d'accord » suffit-il ? Et que produis-tu chez les gens ?",
 "Le dernier axe, et le plus dérangeant. Prévenir : celui-là va toucher des choses que tout le monde fait."))

add("a6-scene", slide_quote("a6-scene",
 "Ton client vient de vivre un déclic. Il est ému, il t'appelle pour te le dire.",
 "La scène",
 sub="C'est, statistiquement, le meilleur moment pour lui vendre le niveau supérieur. Tous les manuels le disent, et ils ont raison sur les chiffres. Tu le fais&nbsp;?",
 notes="Ne pas répondre. Laisser la salle répondre. Beaucoup diront oui, et beaucoup l'ont fait. C'est le point d'entrée honnête de l'axe."))

add("a6-contrast", slide_contrast("a6-contrast", F6, "Une cible, ou quelqu'un dont tu réponds",
 "La cible", [
   "Le panier moyen, la valeur vie client, le taux de rétention.",
   "Le vocabulaire est explicite et personne ne s'en offusque : tunnel, accroche, capture, <i>lead</i>.",
   "Reed Hastings, Netflix : « notre concurrent, c'est le sommeil ».",
   "Sean Parker, cofondateur de Facebook : ces produits exploitent « une vulnérabilité de la psychologie humaine »."],
 "Celui dont tu réponds", [
   "Refus du rapport de dépendance et d'asservissement du client.",
   "La vente s'y définit autrement : aider quelqu'un à prendre une décision utile <b>pour lui</b>.",
   "Un accompagnement réussi rend autonome. Si ton modèle ne tient que parce que ton client ne s'en sort jamais, ce n'est pas un modèle.",
   "« Aime pour ton frère ce que tu aimes pour toi-même » — appliqué ici : voudrais-tu qu'on te vende ceci, à ce moment-là, dans cet état ?"],
 foot=F6,
 notes="Les deux citations du côté gauche sont précieuses : ce ne sont pas des critiques extérieures, ce sont les gens qui construisent ces produits qui le disent eux-mêmes. Personne ne peut dire qu'on caricature."))

add("a6-consent", slide_sources("a6-consent", F6, "« Il était d'accord » ne suffit pas",
 [("« Il n'est pas suffisant que deux personnes soient d'accord sur un contrat pour que ce contrat soit licite : le contrat doit porter sur un objet licite. »",
   "Dr Mohamed Talal Lahlou &middot; le consentement est <i>nécessaire</i> — un échange sans accord est une spoliation. Il n'est pas <i>suffisant</i>"),
  ("Le <i>ghubn</i> : un déséquilibre excessif dans l'échange reste problématique <b>même consenti</b>.",
   "Le droit musulman protège aussi contre soi-même"),
  ("Que ton client ait signé ne clôt pas la question. Qu'il ait dit oui à la fin d'un appel de vente de quatre-vingt-dix minutes ne dit rien de sa liberté au moment où il l'a dit.",
   "Le contrat te protège juridiquement ; il ne te dédouane pas")],
 foot=F6,
 notes="C'est l'axe le plus subversif pour un esprit formé à l'école dominante, parce qu'il touche au fondement moral de tout l'édifice libéral : la légitimité par le seul accord des parties. C'est ce raisonnement qui permet de défendre à peu près n'importe quoi. Objection à traiter : « alors qui décide à la place des gens ? » Personne, et surtout pas nous. Il s'agit de reconnaître que le vendeur porte une part de la responsabilité de l'échange et qu'il ne peut pas la transférer entièrement en faisant signer quelque chose. C'est une exigence sur soi, pas un pouvoir sur l'autre."))

add("a6-mots", slide_cards("a6-mots", F6, "Quatre mots qui remplacent tous les débats vagues sur l'éthique",
 [card("<i>Gharar</i>", "L'aléa, la zone d'ombre : ce que le client ne peut pas évaluer."),
  card("<i>Tadlīs</i>", "Dissimuler le défaut."),
  card("<i>Ghubn</i>", "La lésion : le déséquilibre excessif."),
  card("<i>Iqāla</i>", "Défaire une vente à l'amiable, à la demande de celui qui regrette — et l'accepter est tenu pour une vertu.")],
 foot=F6,
 notes="Les trois premiers : l'essentiel des pratiques discutables du marché tombe sous l'un des trois. Le quatrième est un droit que presque personne n'utilise. Un entrepreneur qui inscrit l'iqala dans ses conditions ferait mieux que se protéger : il signalerait qu'il n'a pas besoin de retenir ses clients pour vivre."))

add("a6-effet", slide_quote("a6-effet",
 "Son contenu parle de baraka. Son dispositif enseigne à rater le fajr.",
 "Le cas",
 sub="Un frère anime un direct tous les soirs. Il parle d'islam, de sens — le contenu est irréprochable. L'audience est meilleure en fin de soirée, alors il pousse : minuit, une heure, deux heures du matin.",
 notes="Le cas le plus important de la soirée. Il n'a rien fait d'interdit. Son intention est bonne. Et il installe, chez des milliers de personnes, une habitude qui les abîme. Aucun filtre licite/illicite ne détecte cela, parce qu'il n'y a rien à détecter dans l'acte — le problème est dans ce que l'acte produit. La formule qui nomme le mécanisme : le vecteur de communication fait partie du message. Ton créneau est ton message. Ton format est ton message. Ton modèle de prix est ton message."))

add("a6-fondements", slide_sources("a6-fondements", F6, "Et ce n'est pas une intuition morale : c'est un chapitre du droit",
 [("<i>Lā ḍarar wa lā ḍirār</i> — pas de préjudice, ni de préjudice en retour.",
   "L'une des maximes qui structurent tout le droit des transactions"),
  ("<i>Sadd adh-dharā&#702;i&#703;</i> — la fermeture des moyens. Un acte licite devient problématique par ce à quoi il conduit régulièrement.",
   "Et sa jumelle : <i>al-wasā&#702;il lahā aḥkām al-maqāṣid</i> — les moyens prennent le statut des fins"),
  ("« Chacun de vous est un berger, et chacun est responsable de son troupeau. »",
   "La <i>ri&#703;āya</i> : l'assistance jointe à l'observation. Tu ne réponds pas seulement de ce que tu vends ; tu réponds de ceux que tu conduis"),
  ("Celui qui indique un bien en a la récompense ; celui qui appelle à un égarement en porte la charge, et autant que ceux qui le suivent.",
   "L'ancrage le plus direct : ta responsabilité inclut le comportement que tu déclenches chez autrui")],
 foot=F6,
 notes="C'est l'axe qu'on croirait le plus fragile et qui est le mieux armé. Conclure par la formule de Talal Lahlou : le légal n'est pas forcément éthique. Et l'objection : « on ne peut pas être responsable de tout ce que les gens font ». Exact, et ce n'est pas ce qui est demandé. Il s'agit de ce que ton dispositif rend PROBABLE, systématiquement, par construction. C'est la différence entre un accident et un design."))

add("a6-leviers", sec("a6-leviers", dark_style("128px", "#5E3A18", "display:flex; flex-direction:column; gap:48px; justify-content:center"),
 '  <p style="font-size:28px; font-weight:600; letter-spacing:5px; text-transform:uppercase; color:%s">L\'outil de la soirée &middot; les trois leviers</p>\n'
 '  <h2 style="font-family:%s; font-size:72px; font-weight:500; line-height:1.15; color:%s">Est-ce que ce que je fais crée, chez la personne en face&nbsp;:</h2>\n'
 '  <div style="display:flex; gap:32px">\n'
 '    <div style="flex:1; background:#FAF7F0; padding:56px; border-radius:14px"><h3 style="font-family:%s; font-size:56px; font-weight:600; color:%s">De la dépendance&nbsp;?</h3></div>\n'
 '    <div style="flex:1; background:#FAF7F0; padding:56px; border-radius:14px"><h3 style="font-family:%s; font-size:56px; font-weight:600; color:%s">De l\'aveuglement&nbsp;?</h3></div>\n'
 '    <div style="flex:1; background:#FAF7F0; padding:56px; border-radius:14px"><h3 style="font-family:%s; font-size:56px; font-weight:600; color:%s">De l\'excès&nbsp;?</h3></div>\n'
 '  </div>'
 % ("#F0D9B8", DISP, "#FFFFFF", DISP, INK, DISP, INK, DISP, INK),
 "L'outil le plus utile de tout le travail, parce qu'il est court, qu'il se retient, et qu'il ne demande aucune compétence religieuse pour être employé. Le donner explicitement comme ce qu'on emporte ce soir. Il vient des trois leviers de perdition enseignés dans le management prophétique de Médine Académie."))

add("a6-cas", slide_table("a6-cas", F6, "Passons quelques cas parfaitement ordinaires",
 ["Ce que tu fais", "Ce que ça installe", "Levier"],
 [["Le direct jusqu'à deux heures du matin", "Tu entraînes ton audience à rater la prière", "Excès"],
  ["Le contenu conçu pour retenir l'attention", "Tu formes, et tu fabriques des gens qui défilent", "Aveuglement"],
  ["L'accompagnement dont on ne sort jamais", "Le client ne devient jamais autonome", "Dépendance"],
  ["Le paiement en quatre fois", "Une dette qu'il n'aurait pas contractée", "Excès"],
  ["La fausse urgence", "Tu as entraîné ton audience à ne plus te croire", "Aveuglement"],
  ["Le prix cassé pour prendre le marché", "Trois concurrents qui nourrissaient des familles", "Excès"],
  ["Le contenu qui fait peur pour convertir", "Tu as ajouté de l'anxiété à un monde qui n'en manquait pas", "Aveuglement"]],
 ["38%", "44%", "18%"], foot=F6, size=26,
 notes="Passer la liste vite, sans moraliser, et en assumant qu'on a fait plusieurs de ces choses. Dire lesquelles on a faites soi-même : c'est ce qui rend le tableau supportable et utile. Puis inviter chacun à en ajouter une de son propre business dans le chat."))

add("a6-lundi", slide_lundi("a6-lundi", "Le client et l'effet",
 ["Écris les trois comportements que ton activité <b>installe</b> chez tes clients. Pas ce que tu leur vends : ce qu'ils font différemment à cause de toi.",
  "Passe chacun aux trois leviers : dépendance, aveuglement, excès.",
  "Puis ajoute une porte de sortie explicite à ton offre, et dis-la à voix haute dans ton prochain appel de vente."],
 "L'exercice le plus inconfortable et le plus rentable. Sur la porte de sortie : l'expérience de tous ceux qui l'ont fait est la même, elle vend davantage qu'elle ne coûte."))

# ---------- CLÔTURE
add("outils", slide_cards("outils", "Clôture", "Alors on jette les outils modernes ?",
 [card("Non. On ne peut qu'emprunter.", "« L'idée n'est pas de tout rejeter. On ne peut qu'emprunter. La question, c'est <b>comment</b>. » — Dr Chauki Lazhar"),
  card("Deux savants, la même matière", "L'un est entré dans la philosophie grecque sans cadre : « il est rentré dans le ventre des philosophes, il a voulu en sortir, il n'a pas réussi ». Al-Ghazālī y est entré avec un cadre déjà constitué — il a pris ce qui était utile et l'a réintégré dans le sien."),
  card("Les deux dangers, par Malek Bennabi", "Les <b>idées mortes</b> : les nôtres, sans validité dans le contexte présent. Les <b>idées mortelles</b> : venues d'ailleurs, efficaces, séduisantes, et qui dénaturent la nôtre de l'intérieur.")],
 notes="Ce bloc évite que la soirée se termine en rejet. Le conservatisme et l'imitation échouent pour des raisons opposées. La méthode qui en découle tient en deux passes et s'applique à n'importe quel outil : 1) de quel cadre vient-il — quelle idée de l'humain, de la valeur, de la réussite porte-t-il dans ses réglages par défaut ? 2) le test des trois leviers."))

add("jumeau", slide_table("jumeau", "Clôture", "Presque chaque mécanique manipulatoire a un jumeau honnête",
 ["Ce qu'on jette", "Ce qui le remplace, et qui marche souvent mieux"],
 [["Le compte à rebours truqué", "L'urgence réelle, dite comme elle est"],
  ["Le faux prix barré", "L'ancrage de valeur sincère"],
  ["Le chantage à la rareté", "La garantie qu'on peut tenir"],
  ["Le concurrent inventé, la fausse file d'attente", "Ta preuve réelle, même si elle est plus petite"],
  ["La vente additionnelle placée au pic émotionnel", "Le même message, envoyé trois jours plus tard"]],
 ["44%", "56%"], size=30,
 notes="Lever le malentendu qui paralyse les entrepreneurs scrupuleux : la ligne de partage ne passe PAS entre la pression et la douceur. Elle passe entre la vérité et la tromperie. Si tu es convaincu que ton offre aide réellement la personne en face, ne rien faire pour l'aider à franchir le pas, c'est la trahir par timidité. Deux questions avant chaque mécanique : est-ce que c'est vrai ? est-ce que ça sert vraiment CETTE personne-là ? Deux oui : tu peux pousser fort. Un seul non : on jette. Ce qu'on jette, ce n'est pas l'efficacité — c'est le mensonge."))

add("emporter", slide_bullets("emporter", "Clôture", "Trois choses à emporter",
 ['<b style="color:%s">Un paradigme, c\'est ce avec quoi tu penses.</b> Tu en as un. La seule question utile n\'est pas de savoir si tu en as attrapé un, mais lequel, et où il opère.' % INK,
  '<b style="color:%s">Le halal, c\'est le comment ; le paradigme, c\'est le vers quoi.</b> La question juste n\'est pas « comment faire entrer mon business dans le halal », mais « comment marche-t-on correctement sur ce chemin-là ».' % INK,
  '<b style="color:%s">Dépendance, aveuglement, excès.</b> Trois questions, sur ton activité et sur chacun de tes outils. Elles ne règlent pas tout, et elles suffisent à commencer.' % INK],
 size=34,
 notes="Les redire lentement. Ce sont les trois phrases qu'on veut entendre répétées dans la communauté la semaine prochaine."))

add("ouvert", slide_cards("ouvert", "Clôture", "Et ce qu'on ne sait pas encore",
 [card("Le prix juste", "Le Prophète &#65018; a refusé de fixer les prix — donc pas de barème. Mais le <i>ghubn</i> existe — donc tout prix consenti n'est pas légitime. Entre les deux, un espace qu'on ne sait pas encore baliser."),
  card("Le numérique", "L'abonnement, où l'objet du contrat se renouvelle indéfiniment. Les places de marché, où l'intermédiaire ne possède rien et engage pourtant sa responsabilité."),
  card("La question qu'on ne tranche pas", "Que faire lorsqu'un marché entier repose sur une pratique qu'on refuse ? Se retirer, c'est laisser le terrain. Rester, c'est participer. Nous n'avons pas de réponse satisfaisante — et nous nous méfions de ceux qui en ont une immédiatement.")],
 notes="Assumer les questions ouvertes, c'est ce qui distingue ce travail d'un argumentaire. Un texte qui conclut sur une certitude est un argumentaire ; un texte qui conclut sur un inventaire est un document de travail. C'est aussi une invitation : ces chantiers sont collectifs."))

add("fin", sec("fin", dark_style("128px", DEEP, "display:flex; flex-direction:column; gap:40px; justify-content:center"),
 '  <p style="font-size:28px; font-weight:600; letter-spacing:5px; text-transform:uppercase; color:%s">La suite</p>\n'
 '  <h1 style="font-family:%s; font-size:104px; font-weight:500; line-height:1.08; color:%s">On ne clôt pas le sujet.<br>On donne la grille.</h1>\n'
 '  <hr style="width:280px; height:3px; border:none; background:%s">\n'
 '  <ul style="display:flex; flex-direction:column; gap:20px">\n'
 '    <li style="font-size:34px; line-height:1.4; color:%s">Le syllabus complet — onze axes, les sources nommées, les objections traitées.</li>\n'
 '    <li style="font-size:34px; line-height:1.4; color:%s">Les cinq axes qu\'on n\'a pas eu le temps de faire ce soir y sont en entier.</li>\n'
 '    <li style="font-size:34px; line-height:1.4; color:%s">Et le travail continue avec vous : c\'est un chantier collectif, pas un cours.</li>\n'
 '  </ul>'
 % (OCHRE_L, DISP, LIGHTTX, OCHRE_L, LIGHTBD, LIGHTBD, LIGHTBD),
 "Le CTA se décide avec Oussama avant le direct : lien du syllabus, inscription, prochaine session. Rappeler que les onze axes du document couvrent aussi la réussite, le consentement séparé du client, et le collectif — qui mériterait une soirée à lui seul."))

# ================================================================ ÉCRITURE
for sid in ORDER:
    with open(os.path.join(SL, sid + ".html"), "w") as f:
        f.write(SLIDES[sid] + "\n")

deck = {
  "v": 4,
  "createdOnFiles": {"v": 1, "at": "2026-09-21T10:00:00Z"},
  "title": "Héritage & Modernité — Le paradigme de l'entrepreneur musulman",
  "order": ORDER,
  "cover": "cover",
  "sections": {
    "ouverture": {"description": "Pourquoi ce sujet, où il touche déjà chacun, et ce qu'est un paradigme", "start": "cover"},
    "axe1": {"description": "La finalité : c'est quoi le but du jeu", "start": "a1"},
    "axe2": {"description": "La mesure : ce que tu comptes et quand tu as gagné", "start": "a2"},
    "axe3": {"description": "Le profit et le risque : la marge ou la transaction, qui perd quoi", "start": "a3"},
    "axe4": {"description": "La croissance et la dette : grandir par décision ou par obligation", "start": "a4"},
    "axe5": {"description": "La concurrence : somme nulle ou part assignée", "start": "a5"},
    "axe6": {"description": "Le client et l'effet : le consentement ne suffit pas, et ce que ton dispositif installe", "start": "a6"},
    "cloture": {"description": "Comment emprunter les outils modernes, ce qu'on emporte, ce qui reste ouvert", "start": "outils"}
  },
  "faces": {
    "eb-garamond": {"family": "EB Garamond", "href": "https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400..700;1,400..600&display=swap"},
    "ibm-plex-sans": {"family": "IBM Plex Sans", "href": "https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:ital,wght@0,300..600;1,400&display=swap"}
  },
  "designSystems": []
}
with open(os.path.join(ROOT, "project", "deck.json"), "w") as f:
    json.dump(deck, f, ensure_ascii=False, indent=2)

print(len(ORDER), "slides")
print(" ".join(ORDER))
