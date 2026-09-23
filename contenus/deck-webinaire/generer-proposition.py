# -*- coding: utf-8 -*-
import base64, html, os, json

BG = base64.b64encode(open("/tmp/claude-0/deckassets/bg.png","rb").read()).decode()
BG2 = base64.b64encode(open("/tmp/claude-0/deckassets/bg2.png","rb").read()).decode()

G, GD, W, DIM, INK = "#E3A94F", "#B8862B", "#FFFFFF", "#CFCFCF", "#141414"
ARCH = "'Archivo',Arial,sans-serif"
OSW  = "'Oswald',Arial,sans-serif"
POP  = "'Poppins',Arial,sans-serif"
AR   = "'Noto Naskh Arabic',Georgia,serif"

def T(t): return html.escape(t, quote=False).replace("&amp;","&")

def slide(kind, data, bg=1):
    """retourne le HTML interne d'une slide 1920x1080"""
    out = ['<div class="%s"></div>' % ("bg" if bg == 1 else "bg2")]
    if kind == "titre":
        lines = data
        joined = " ".join(lines)
        if len(lines) == 1 and len(joined) <= 26:
            out.append('<div class="ctr"><div class="box"><h1 class="grad">%s</h1></div></div>' % T(lines[0].upper()))
        else:
            sz = 104 if len(joined) <= 42 else (82 if len(joined) <= 70 else 64)
            out.append('<div class="ctr"><h1 class="disp" style="font-size:%dpx">%s</h1></div>'
                       % (sz, "<br>".join(T(l.upper()) for l in lines)))
    elif kind == "partie":
        num, rest = data[0], data[1:]
        out.append('<div class="left"><p class="eyeb">%s</p><h1 class="disp l" style="font-size:112px">%s</h1>'
                   '<div class="rule"></div></div>' % (T(num.upper()), "<br>".join(T(l.upper()) for l in rest)))
    elif kind == "punch":
        lines = data
        joined = " ".join(lines)
        if len(lines) == 1 and len(joined) <= 46:
            out.append('<div class="ctr"><h2 class="disp" style="font-size:88px">%s</h2></div>' % T(lines[0].upper()))
        else:
            sz = 54 if len(joined) <= 130 else 44
            ps = "".join('<p class="pp" style="font-size:%dpx;color:%s">%s</p>'
                         % (sz, G if (i == len(lines)-1 and len(lines) > 1) else W, T(l))
                         for i, l in enumerate(lines))
            out.append('<div class="ctr">%s</div>' % ps)
    elif kind == "citation":
        q, src, ar = data
        sz = 60 if len(q) <= 110 else (48 if len(q) <= 200 else 40)
        s = '<p class="q" style="font-size:%dpx">%s</p>' % (sz, T(q.upper()))
        if src: s += '<p class="src">— %s —</p>' % T(src)
        if ar:  s += '<p class="ar">%s</p>' % T(ar)
        out.append('<div class="ctr">%s</div>' % s)
    elif kind == "liste":
        title, items = data[0], data[1:]
        n = max(1, len(items))
        sz = 38 if n <= 4 else (33 if n <= 6 else 29)
        li = "".join('<p class="li" style="font-size:%dpx;color:%s">%s</p>'
                     % (sz, G if it.startswith(("👉","✅","1️⃣","2️⃣","3️⃣","1.","2.","3.","4.")) else (DIM if it.startswith("❌") else W), T(it))
                     for it in items)
        out.append('<div class="top"><p class="disp l" style="font-size:46px">%s</p>'
                   '<div class="rule sm"></div><div class="stack" style="gap:%dpx">%s</div></div>'
                   % (T(title.upper()), 20 if n <= 5 else 14, li))
    elif kind == "vs":
        lt, li, rt, ri, sep = data
        def col(t, items, c):
            x = "".join('<p class="vli">%s</p>' % T(i) for i in items)
            return ('<div class="vcol"><p class="vt" style="color:%s">%s</p>'
                    '<div class="rule xs" style="background:%s"></div>%s</div>' % (c, T(t.upper()), c, x))
        out.append('<div class="ctr"><div class="vrow">%s<div class="vsep">%s</div>%s</div></div>'
                   % (col(lt, li, W), T(sep), col(rt, ri, G)))
    return "".join(out)

# ---------------------------------------------------------------- contenu
BLOCKS = [
("A", "Le programme", "Slide 4 remplacée",
 "Le point 2 annonçait un inventaire de thèmes. Il annonce maintenant des situations. Le point 3 "
 "devient la méthodologie, comme tu l'as demandé.", [
 ("titre", ["CE SOIR, TU REPARS AVEC TROIS CHOSES"]),
 ("liste", ["1️⃣ Ce que notre dîn dit du business",
   "Pas de ton produit. Pas de ton financement.",
   "Du business lui-même : à quoi il sert, quand il est réussi, ce qu'il te demande."]),
 ("liste", ["2️⃣ Six décisions que tu prendras autrement dès lundi",
   "Comment tu fixes ton prix. Ce que tu fais quand un concurrent s'installe.",
   "Ce que tu proposes à un client qui va mieux. Quand tu décides de grandir.",
   "👉 Pour chacune : ce que tu changes concrètement, dès cette semaine."]),
 ("liste", ["3️⃣ Notre méthodologie pour entreprendre",
   "Six piliers, et les techniques modernes qui s'y branchent —",
   "marketing digital, vente, IA — une fois orientées par le bon cap.",
   "👉 Pas une philosophie. Un mode d'emploi."]),
]),
("B", "La laïcité cérébrale", "À insérer après les images de ce qu'on vend sur internet",
 "Le bloc qui te manquait. Il vient avant le mot « paradigme » : on montre la séparation avant de "
 "la nommer.", [
 ("titre", ["LA LAÏCITÉ CÉRÉBRALE"]),
 ("punch", ["Tu pries.", "Tu jeûnes.", "Et tu ouvres ton business plan."]),
 ("punch", ["Et à ce moment-là, sans t'en rendre compte,", "tu as fermé une porte."]),
 ("liste", ["Deux tiroirs, et on n'ouvre jamais les deux en même temps",
   "Le tiroir du dîn — la prière, le jeûne, le licite et l'illicite",
   "Le tiroir du business — le prix, la marge, la croissance, la concurrence",
   "On vérifie que le second ne contredit pas le premier",
   "👉 Mais on ne demande jamais au premier ce qu'il a à dire sur le second"]),
 ("punch", ["Ce n'est pas de l'hypocrisie.", "C'est une habitude de séparation",
   "qu'on a prise sans la décider."]),
 ("punch", ["Sauf que notre dîn n'a pas un avis sur le business.",
   "Il a une vision de la vie.", "Et le business est dedans."]),
 ("vs", ("Où on va chercher", ["Elon Musk", "Alex Hormozi", "Un podcast américain",
   "Des méthodes qui ont dix ans"],
   "Ce qu'on a chez nous", ["ʿAbd ar-Rahmān ibn ʿAwf", "ʿUthmān ibn ʿAffān",
   "Quatorze siècles de fiqh al-muʿāmalāt", "Une bibliothèque qu'on n'a pas ouverte"], "→")),
 ("punch", ["Ce n'est pas un procès de ceux qu'on écoute.", "C'est une question :",
   "pourquoi on ne lit jamais les nôtres ?"]),
]),
("C", "Le syndrome de la réplication", "Déplacé dans la partie paradigme",
 "Tu avais raison : il concluait une partie au lieu d'illustrer le paradigme. Il vient juste après "
 "« la question est lequel ».", [
 ("titre", ["LE SYNDROME DE LA RÉPLICATION"]),
 ("punch", ["On prend un modèle qui vient d'ailleurs.",
   "On en retire ce qui est visiblement interdit.", "Et on croit qu'on l'a fait nôtre."]),
 ("titre", ["LE CAS LE PLUS EMBLÉMATIQUE", "LE DÉVELOPPEMENT PERSONNEL"]),
 ("vs", ("Ce qu'on a enlevé", ["La loi d'attraction", "Le vocabulaire ésotérique",
   "La visualisation créatrice", "On a ajouté bismillah en ouverture"],
   "Ce qui n'a pas bougé", ["Tout est organisé autour d'un seul centre : toi",
   "Tu es un projet inachevé", "Ta responsabilité est de te perfectionner",
   "Le sens se trouve à l'intérieur de toi"], "→")),
 ("punch", ["Dieu n'y est pas absent parce qu'on l'aurait chassé.",
   "Il n'y est pas parce que l'architecture", "n'a pas prévu de place pour Lui."]),
 ("liste", ["Et les outils, on les avait déjà",
   "Se lever avant l'aube — le fajr",
   "Se priver volontairement pour reprendre la main — le jeûne",
   "La gratitude — le shukr", "Le bilan de soi — la muhāsaba", "La réflexion — le tafakkur"]),
 ("punch", ["On ne t'a pas vendu une méthode nouvelle.", "On t'a revendu la tienne,",
   "en lui retirant son destinataire."]),
]),
("D", "Le filtre", "Le principe, puis sa limite",
 "Tu avais la conclusion sans la démonstration. On montre d'abord que le filtre marche, sinon la "
 "critique passe pour du mépris.", [
 ("titre", ["LE FILTRE"]),
 ("liste", ["Ce réflexe, on l'a tous appris, et il est bon",
   "Une pratique se présente", "Tu demandes : est-ce que c'est licite ?",
   "Selon la réponse, tu gardes ou tu jettes",
   "👉 Il a protégé des milliers d'entrepreneurs. Rien ici ne vise à l'affaiblir."]),
 ("punch", ["Mais il a une limite,", "et elle est structurelle."]),
 ("punch", ["Il opère sur les actes, un par un.", "Jamais sur le cadre qui les produit."]),
 ("punch", ["Et pendant ce temps, on a tout ce qu'il faut.",
   "On ne l'a simplement jamais sorti de la bibliothèque."]),
]),
("E", "La transition vers les axes", "Entre 46 et 47",
 "La marche qui manquait. Et la PARTIE 2 qui n'existe pas dans ton deck — tu as une partie 1 et une "
 "partie 3.", [
 ("titre", ["ON ARRÊTE LA THÉORIE"]),
 ("punch", ["Tout ce qu'on vient de dire ne vaut rien", "si tu ne peux pas le voir",
   "dans ton agenda de la semaine dernière."]),
 ("punch", ["Alors regardons où ça se voit.", "Six endroits précis."]),
 ("partie", ["Partie 2", "Les six axes"]),
]),
("F", "Axe 1 — le moteur et le Riḍā", "Deux ajouts",
 "Une slide avant Friedman pour nommer le moteur, une avant Ibn ʿAwf pour nommer le nôtre.", [
 ("titre", ["LE MOTEUR DE LA MODERNITÉ"]),
 ("punch", ["Toute civilisation tourne autour d'un moteur.",
   "Le nôtre s'appelait la recherche de Son agrément.",
   "Celui qu'on nous a donné s'appelle l'accumulation."]),
 ("titre", ["NOUS, LE BUT, C'EST LE RIḌĀ"]),
 ("citation", ("Dis : en vérité, ma prière, mes actes d'adoration, ma vie et ma mort appartiennent à Allah, Seigneur des mondes.",
   "Sourate Al-Anʿām, 6:162", "﴿ قُلْ إِنَّ صَلَاتِي وَنُسُكِي وَمَحْيَايَ وَمَمَاتِي لِلَّهِ رَبِّ الْعَالَمِينَ ﴾")),
 ("punch", ["Le commerce est un des chemins qui y mènent.",
   "L'argent est un moyen puissant d'y avancer.",
   "Ce n'est pas un renoncement. C'est un changement de rang."]),
]),
("G1", "Ce qui te manque n'est pas ce que tu crois", "Ouverture du bloc transversal",
 "Le bloc entier qui manquait. Il vient après les six axes et avant la méthodologie — au moment "
 "précis où le public se demande « concrètement, qu'est-ce qu'il me manque ? »", [
 ("titre", ["CE QUI TE MANQUE N'EST PAS CE QUE TU CROIS"]),
 ("punch", ["Tu penses qu'il te manque une compétence métier.", "Presque jamais."]),
 ("vs", ("L'expertise métier", ["Elle est propre à ton métier",
   "Le couscous, le béton, le code", "C'est souvent ce que tu maîtrises le mieux",
   "Elle ne suffit jamais à elle seule"],
   "Les compétences transversales", ["Elles servent quel que soit le métier",
   "Vendre, se faire connaître, décider", "C'est presque toujours ce qui bloque",
   "Elles ne dépendent d'aucun secteur"], "→")),
 ("punch", ["Le meilleur pâtissier du quartier", "peut fermer boutique.",
   "Ce n'est pas la pâtisserie qui l'a tué."]),
 ("liste", ["Quatre compétences, quel que soit ton projet",
   "1. Le marketing digital — être trouvé", "2. La vente — être choisi",
   "3. Le dîn — connaître les règles du jeu", "4. L'IA — augmenter ta portée"]),
 ("punch", ["Et les quatre changent de nature", "selon le paradigme qui les tient."]),
]),
("G2", "Le marketing digital", "Compétence transversale 1", "", [
 ("titre", ["1. LE MARKETING DIGITAL"]),
 ("punch", ["Le monde où tu vends", "est déjà numérique.", "Que ça te plaise ou non."]),
 ("liste", ["Ce qui se passe quand tu ne parles pas",
   "Ton client cherche ton métier, et il trouve quelqu'un d'autre",
   "Ton concurrent explique ce qu'est un bon produit — et c'est le sien",
   "Celui qui parle le plus fort devient la référence, même s'il est moins bon",
   "👉 Ne pas communiquer, c'est aussi communiquer."]),
 ("punch", ["« Je ne veux pas me mettre en avant. »", "Vérifie que c'est de l'humilité,",
   "et pas une peur qui a trouvé un joli nom."]),
 ("liste", ["Orienté par le bon paradigme, ça donne",
   "La légitimité vient de l'expertise, pas de la capacité à convaincre",
   "Ne pas tout montrer pour se faire connaître — le principe du voile s'applique ici aussi",
   "Une promesse vraie ET adaptée au palier de celui qui l'écoute",
   "👉 On se rend trouvable. On ne se transforme pas en produit."]),
]),
("G3", "La vente", "Compétence transversale 2", "", [
 ("titre", ["2. LA VENTE"]),
 ("punch", ["Il faut qu'on parle", "de ce mot qui te dérange."]),
 ("liste", ["Ce qu'on se dit tous, plus ou moins",
   "« Vendre, c'est forcer la main »", "« Si le produit est bon, il se vend tout seul »",
   "« Je ne veux pas être ce commercial-là »",
   "👉 Et pendant ce temps, personne n'achète."]),
 ("punch", ["La manipulation, c'est de faire faire à quelqu'un", "ce qui te sert à toi.",
   "Ce n'est pas la même chose que convaincre."]),
 ("punch", ["Si tu es convaincu que ton offre aide vraiment la personne en face,",
   "ne rien faire pour l'aider à franchir le pas,",
   "ce n'est pas de la délicatesse. C'est une trahison par timidité."]),
 ("liste", ["Deux questions, avant chaque mécanique",
   "1. Est-ce que c'est vrai ?", "2. Est-ce que ça sert vraiment cette personne-là ?",
   "👉 Deux oui : tu peux pousser fort. Un seul non : on jette."]),
]),
("G4", "Le dîn", "Compétence transversale 3", "", [
 ("titre", ["3. LE DÎN"]),
 ("punch", ["Les règles du jeu.", "Pas un supplément d'âme :", "une compétence technique."]),
 ("liste", ["Ce qu'un entrepreneur devrait savoir nommer",
   "Le gharar — l'aléa, ce que ton client ne peut pas évaluer",
   "Le tadlîs — dissimuler le défaut",
   "Le ghubn — le déséquilibre excessif, même consenti",
   "L'iqāla — défaire une vente à la demande de celui qui regrette"]),
 ("punch", ["Tu n'as pas besoin d'être savant.", "Tu as besoin de savoir à qui demander,",
   "et de savoir que la question existe."]),
]),
("G5", "L'intelligence artificielle", "Compétence transversale 4", "", [
 ("titre", ["4. L'INTELLIGENCE ARTIFICIELLE"]),
 ("punch", ["Un outil donne de la vitesse.", "Pas une direction."]),
 ("punch", ["Et un outil sans direction", "t'emmène simplement plus vite",
   "là où tu ne voulais pas aller."]),
 ("vs", ("Éteindre son cerveau", ["Tu demandes quoi penser",
   "Tu ne sais plus pourquoi tu fais ce que tu fais",
   "Ton jugement se déplace dans la machine", "C'est le levier de l'aveuglement"],
   "Augmenter sa portée", ["Tu sais ce que tu veux dire",
   "Elle te fait aller dix fois plus vite pour le dire",
   "Ton jugement reste chez toi", "C'est le levier de l'impact"], "→")),
 ("punch", ["Le risque n'est pas qu'elle écrive à ta place.", "C'est qu'elle décide à ta place."]),
 ("liste", ["Ce qu'elle fait vraiment bien",
   "Elle t'oblige à formuler — et formuler est le travail que la plupart évitent",
   "Elle produit du générique, donc elle rend ton point de vue plus précieux",
   "Elle exécute pendant que tu réfléchis, jamais l'inverse",
   "👉 Et elle fabrique aussi de la fausse preuve. La frontière avec le tadlîs est à un clic."]),
]),
("G6", "La bascule", "Vers la méthodologie", "", [
 ("punch", ["Six axes pour le cap.", "Quatre compétences pour avancer.",
   "Reste à savoir dans quel ordre."]),
 ("partie", ["Partie 3", "La méthodologie"]),
]),
]

# ---------------------------------------------------------------- page
CSS = """
*{box-sizing:border-box}
body{margin:0;background:#0A0A0A;color:#EDEDED;font-family:'Poppins',Arial,sans-serif}
.wrap{max-width:1100px;margin:0 auto;padding-inline:16px;padding-block:0 96px}
header{padding-block:56px 34px;border-bottom:1px solid #262626}
.eyebrow{font-family:'Archivo',sans-serif;font-size:13px;font-weight:700;letter-spacing:4px;
  text-transform:uppercase;color:#E3A94F;margin:0 0 16px}
h1.page{font-family:'Archivo',sans-serif;font-style:italic;font-weight:900;text-transform:uppercase;
  font-size:clamp(30px,6.4vw,54px);line-height:1.04;margin:0 0 18px;text-wrap:balance}
.sub{font-size:16px;line-height:1.65;color:#A8A8A8;margin:0;max-width:62ch}
.legend{display:flex;flex-wrap:wrap;gap:8px 18px;margin:22px 0 0;padding:0;list-style:none;
  font-size:13px;color:#8C8C8C}
.legend b{color:#E3A94F;font-weight:600}
section.block{margin-block:62px 0}
.bh{display:flex;align-items:baseline;gap:14px;flex-wrap:wrap;margin:0 0 6px}
.bid{font-family:'Archivo',sans-serif;font-weight:900;font-style:italic;font-size:30px;color:#E3A94F}
.bt{font-family:'Archivo',sans-serif;font-weight:700;font-size:23px;text-transform:uppercase;
  letter-spacing:.5px;margin:0}
.bw{font-size:13px;color:#8C8C8C;letter-spacing:1.5px;text-transform:uppercase}
.bn{font-size:15px;line-height:1.65;color:#A8A8A8;margin:10px 0 26px;max-width:66ch;
  border-left:2px solid #E3A94F;padding-left:16px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(420px,1fr));gap:26px}
@media(max-width:640px){.grid{grid-template-columns:1fr}}
.card{min-width:0}
.frame{position:relative;width:100%;aspect-ratio:16/9;overflow:hidden;border-radius:8px;
  border:1px solid #2A2A2A;background:#0E0E0E}
.stage{position:absolute;left:0;top:0;width:1920px;height:1080px;transform-origin:top left}
.cap{display:flex;justify-content:space-between;gap:10px;margin-top:8px;font-size:12px;
  color:#7D7D7D;letter-spacing:1.4px;text-transform:uppercase;font-family:'Archivo',sans-serif}
.cap .n{color:#E3A94F;font-weight:700}
/* --- slide internals (1920x1080) --- */
.bg,.bg2{position:absolute;inset:0;background-size:cover;background-position:center}
.ctr{position:absolute;inset:0;padding:128px;display:flex;flex-direction:column;
  justify-content:center;align-items:center;gap:36px}
.top{position:absolute;inset:0;padding:128px;display:flex;flex-direction:column;justify-content:center;gap:30px}
.left{position:absolute;inset:0;padding:128px;display:flex;flex-direction:column;
  justify-content:center;gap:26px}
h1.disp,h2.disp,p.disp{font-family:'Archivo',sans-serif;font-weight:900;font-style:italic;
  text-transform:uppercase;line-height:1.06;text-align:center;color:#fff;margin:0}
.disp.l{text-align:left}
.box{background:#fff;padding:26px 58px}
h1.grad{font-family:'Archivo',sans-serif;font-weight:900;font-style:italic;text-transform:uppercase;
  font-size:132px;line-height:1.04;text-align:center;margin:0;
  background:linear-gradient(90deg,#131313 0%,#1E1E1E 32%,#B8862B 100%);
  -webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}
.eyeb{font-family:'Poppins',sans-serif;font-size:34px;font-weight:600;letter-spacing:7px;
  text-transform:uppercase;color:#E3A94F;margin:0}
.rule{width:300px;height:5px;background:#E3A94F}
.rule.sm{width:180px;height:4px}
.rule.xs{width:110px;height:4px}
.pp{margin:0;font-weight:400;line-height:1.34;text-align:center}
.q{font-family:'Oswald',sans-serif;font-weight:500;text-transform:uppercase;line-height:1.18;
  text-align:center;color:#fff;margin:0}
.src{font-size:28px;font-style:italic;text-align:center;color:#E3A94F;margin:0}
.ar{font-family:'Noto Naskh Arabic',serif;font-size:48px;line-height:1.9;text-align:center;
  color:#fff;margin:0}
.stack{display:flex;flex-direction:column}
.li{margin:0;font-weight:400;line-height:1.42}
.vrow{display:flex;gap:20px;align-items:stretch;width:100%}
.vcol{flex:1;display:flex;flex-direction:column;gap:16px}
.vt{font-family:'Oswald',sans-serif;font-size:44px;font-weight:600;text-transform:uppercase;
  line-height:1.12;margin:0}
.vli{font-size:31px;line-height:1.4;color:#CFCFCF;margin:0}
.vsep{width:120px;display:flex;align-items:center;justify-content:center;
  font-family:'Archivo',sans-serif;font-weight:900;font-style:italic;font-size:72px;color:#fff}
"""

KINDNAME = {"titre":"titre","partie":"partie","punch":"punchline","citation":"citation",
            "liste":"liste","vs":"deux colonnes"}

def words(kind, data):
    if kind == "citation": return len((data[0] + " " + data[1]).split())
    if kind == "vs":
        lt, li, rt, ri, _ = data
        return len((lt + " " + rt + " " + " ".join(li) + " " + " ".join(ri)).split())
    return len(" ".join(data).split())

parts = ['<title>Proposition webinaire</title>',
 '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:ital,wght@0,400..900;1,400..900&family=Oswald:wght@300..700&family=Poppins:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&family=Noto+Naskh+Arabic:wght@400..700&display=swap">',
 '<style>%s\n.bg{background-image:url(data:image/png;base64,%s)}\n.bg2{background-image:url(data:image/png;base64,%s)}</style>' % (CSS, BG, BG2), '<div class="wrap">',
 '<header><p class="eyebrow">Héritage &amp; Modernité · proposition</p>',
 '<h1 class="page">Ce que j\'ajoute,<br>et où ça tombe</h1>',
 '<p class="sub">Soixante-deux slides proposées, rendues à l\'échelle dans la charte du deck, '
 'pour que tu juges la densité avant qu\'on touche au fichier. Rien n\'est encore intégré : '
 'c\'est une maquette.</p>',
 '<ul class="legend"><li><b>A</b> le programme</li><li><b>B</b> la laïcité cérébrale</li>'
 '<li><b>C</b> le syndrome de la réplication</li><li><b>D</b> le filtre</li>'
 '<li><b>E</b> la transition</li><li><b>F</b> axe 1</li>'
 '<li><b>G</b> les compétences transversales</li></ul></header>']

n = 0
for bid, btitle, bwhere, bnote, slides in BLOCKS:
    parts.append('<section class="block"><div class="bh"><span class="bid">%s</span>'
                 '<h2 class="bt">%s</h2><span class="bw">%s</span></div>' % (bid, T(btitle), T(bwhere)))
    if bnote: parts.append('<p class="bn">%s</p>' % T(bnote))
    parts.append('<div class="grid">')
    for kind, data in slides:
        n += 1
        bgn = 2 if kind in ("partie",) else 1
        parts.append('<div class="card"><div class="frame"><div class="stage">%s</div></div>'
                     '<div class="cap"><span class="n">%02d</span><span>%s · %d mots</span></div></div>'
                     % (slide(kind, data, bgn), n, KINDNAME[kind], words(kind, data)))
    parts.append('</div></section>')

parts.append('</div><script>')
parts.append("""
function fit(){document.querySelectorAll('.frame').forEach(function(f){
  var s=f.querySelector('.stage'); if(!s) return;
  s.style.transform='scale('+(f.clientWidth/1920)+')';});}
fit(); window.addEventListener('resize',fit);
if(document.fonts&&document.fonts.ready){document.fonts.ready.then(fit);}
""")
parts.append('</script>')

out = "/tmp/claude-0/-home-user-ctp-plugin/5bde7487-de28-5f85-acc6-6f6c831c1436/scratchpad/art/proposition.html"
open(out, "w").write("\n".join(parts))
print(n, "slides,", os.path.getsize(out), "octets ->", out)
