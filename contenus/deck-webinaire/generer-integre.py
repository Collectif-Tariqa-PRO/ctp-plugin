# -*- coding: utf-8 -*-
import re, sys
sys.path.insert(0, "/tmp/claude-0/webi")

SRC = "/tmp/claude-0/webi/script.md"
text = open(SRC).read()
B = "═" * 56

def vs_text(lt, li, rt, ri, sep):
    """rend un bloc VS en colonnes alignées pour le script lisible"""
    L = [lt.upper()] + list(li)
    R = [rt.upper()] + list(ri)
    # wrap doux à 38 colonnes
    def wrap(s, w=38):
        out, cur = [], ""
        for word in s.split():
            if len(cur) + len(word) + 1 > w:
                out.append(cur); cur = word
            else:
                cur = (cur + " " + word).strip()
        if cur: out.append(cur)
        return out or [""]
    Lw, Rw = [], []
    for i, (a, b) in enumerate(zip(L + [""] * max(0, len(R) - len(L)),
                                   R + [""] * max(0, len(L) - len(R)))):
        aw, bw = wrap(a), wrap(b)
        n = max(len(aw), len(bw))
        aw += [""] * (n - len(aw)); bw += [""] * (n - len(bw))
        Lw += aw; Rw += bw
    lines = []
    for i, (a, b) in enumerate(zip(Lw, Rw)):
        mid = sep if i == 0 else ""
        lines.append(("%-40s%-8s%s" % (a, mid, b)).rstrip())
    return "\n".join(l.rstrip() for l in lines)

def S(typ, lines, note=None):
    b = "SLIDE X — [%s]\n%s" % (typ, "\n".join(lines))
    if note: b += "\n\nÀ L'ORAL : " + note
    return b + "\n"

def VS(lt, li, rt, ri, sep="VS", note=None):
    return S("VS", vs_text(lt, li, rt, ri, sep).split("\n"), note)

# ---------------------------------------------------------------- blocs
A = [
 S("LISTE", ["1️⃣ CE QUE NOTRE DÎN DIT DU BUSINESS",
   "Pas de ton produit. Pas de ton financement.",
   "Du business lui-même : à quoi il sert, quand il est réussi, ce qu'il te demande."]),
 S("LISTE", ["2️⃣ SIX DÉCISIONS QUE TU PRENDRAS AUTREMENT DÈS LUNDI",
   "Comment tu fixes ton prix. Ce que tu fais quand un concurrent s'installe.",
   "Ce que tu proposes à un client qui va mieux. Quand tu décides de grandir.",
   "👉 Pour chacune : ce que tu changes concrètement, dès cette semaine."]),
 S("LISTE", ["3️⃣ NOTRE MÉTHODOLOGIE POUR ENTREPRENDRE",
   "Six piliers, et les techniques modernes qui s'y branchent —",
   "marketing digital, vente, IA — une fois orientées par le bon cap.",
   "👉 Pas une philosophie. Un mode d'emploi."],
   "Ne pas énumérer les six axes ici : on annonce ce que ça change, pas la table des matières. "
   "La liste complète arrive au moment de la transition."),
]

BB = [
 S("TITRE", ["LA LAÏCITÉ CÉRÉBRALE"]),
 S("PUNCHLINE", ["Tu pries.", "Tu jeûnes.", "Et tu ouvres ton business plan."]),
 S("PUNCHLINE", ["Et à ce moment-là, sans t'en rendre compte,", "tu as fermé une porte."]),
 S("LISTE", ["DEUX TIROIRS, ET ON N'OUVRE JAMAIS LES DEUX EN MÊME TEMPS",
   "Le tiroir du dîn — la prière, le jeûne, le licite et l'illicite",
   "Le tiroir du business — le prix, la marge, la croissance, la concurrence",
   "On vérifie que le second ne contredit pas le premier",
   "👉 Mais on ne demande jamais au premier ce qu'il a à dire sur le second"]),
 S("PUNCHLINE", ["Ce n'est pas de l'hypocrisie.", "C'est une habitude de séparation",
   "qu'on a prise sans la décider."],
   "Le dire sans accuser personne. Cette habitude a une histoire : une conception laïque de "
   "l'espace professionnel, qui précède largement toute influence américaine."),
 S("PUNCHLINE", ["Sauf que notre dîn n'a pas un avis sur le business.",
   "Il a une vision de la vie.", "Et le business est dedans."]),
 VS("Où on va chercher", ["Elon Musk", "Alex Hormozi", "Un podcast américain",
    "Des méthodes qui ont dix ans"],
    "Ce qu'on a chez nous", ["ʿAbd ar-Rahmān ibn ʿAwf", "ʿUthmān ibn ʿAffān",
    "Quatorze siècles de fiqh al-muʿāmalāt", "Une bibliothèque qu'on n'a pas ouverte"], "→",
    "Ne pas caricaturer. Ces gens-là ont produit des choses qui marchent, et on n'est pas là pour "
    "les diaboliser. Le problème n'est pas qu'on les écoute, c'est qu'on n'écoute qu'eux."),
 S("PUNCHLINE", ["Ce n'est pas un procès de ceux qu'on écoute.", "C'est une question :",
   "pourquoi on ne lit jamais les nôtres ?"]),
]

CC = [
 S("TITRE", ["LE SYNDROME DE LA RÉPLICATION"]),
 S("PUNCHLINE", ["On prend un modèle qui vient d'ailleurs.",
   "On en retire ce qui est visiblement interdit.", "Et on croit qu'on l'a fait nôtre."]),
 S("TITRE", ["LE CAS LE PLUS EMBLÉMATIQUE", "LE DÉVELOPPEMENT PERSONNEL"]),
 VS("Ce qu'on a enlevé", ["La loi d'attraction", "Le vocabulaire ésotérique",
    "La visualisation créatrice", "On a ajouté bismillah en ouverture"],
    "Ce qui n'a pas bougé", ["Tout est organisé autour d'un seul centre : toi",
    "Tu es un projet inachevé", "Ta responsabilité est de te perfectionner",
    "Le sens se trouve à l'intérieur de toi"], "→"),
 S("PUNCHLINE", ["Dieu n'y est pas absent parce qu'on l'aurait chassé.",
   "Il n'y est pas parce que l'architecture", "n'a pas prévu de place pour Lui."],
   "Citer ici Chauki Lazhar : du maquillage et du mascara islamiques. Et Sofiane Meziani sur la "
   "règle du filtre — on peut prendre les outils, tant que c'est la foi qui filtre, et pas l'inverse."),
 S("LISTE", ["ET LES OUTILS, ON LES AVAIT DÉJÀ",
   "Se lever avant l'aube — le fajr",
   "Se priver volontairement pour reprendre la main — le jeûne",
   "La gratitude — le shukr", "Le bilan de soi — la muhāsaba", "La réflexion — le tafakkur"]),
 S("PUNCHLINE", ["On ne t'a pas vendu une méthode nouvelle.", "On t'a revendu la tienne,",
   "en lui retirant son destinataire."],
   "L'objection va venir : donc travailler sur soi, c'est mal ? Non. Le jihād an-nafs est un combat "
   "central de notre tradition. L'un te met au centre, l'autre te met à ta place — et c'est le "
   "second qui repose."),
]

D1 = [
 S("TITRE", ["LE FILTRE"]),
 S("LISTE", ["CE RÉFLEXE, ON L'A TOUS APPRIS, ET IL EST BON",
   "Une pratique se présente", "Tu demandes : est-ce que c'est licite ?",
   "Selon la réponse, tu gardes ou tu jettes",
   "👉 Il a protégé des milliers d'entrepreneurs. Rien ici ne vise à l'affaiblir."]),
 S("PUNCHLINE", ["Mais il a une limite,", "et elle est structurelle."]),
 S("PUNCHLINE", ["Il opère sur les actes, un par un.", "Jamais sur le cadre qui les produit."]),
]
D2 = [
 S("PUNCHLINE", ["Et pendant ce temps, on a tout ce qu'il faut.",
   "On ne l'a simplement jamais sorti de la bibliothèque."]),
]

E1 = [ S("PARTIE", ["PARTIE 2", "Les six axes"]) ]
E2 = [
 S("PUNCHLINE", ["Tout ce qu'on vient de dire ne vaut rien", "si tu ne peux pas le voir",
   "dans ton agenda de la semaine dernière."]),
 S("PUNCHLINE", ["Alors regardons où ça se voit.", "Six endroits précis."]),
]

F1 = [
 S("TITRE", ["LE MOTEUR DE LA MODERNITÉ"]),
 S("PUNCHLINE", ["Toute civilisation tourne autour d'un moteur.",
   "Le nôtre s'appelait la recherche de Son agrément.",
   "Celui qu'on nous a donné s'appelle l'accumulation."]),
]
F2 = [
 S("TITRE", ["NOUS, LE BUT, C'EST LE RIḌĀ"]),
 S("CITATION", ["« Dis : en vérité, ma prière, mes actes d'adoration, ma vie et ma mort",
   "appartiennent à Allah, Seigneur des mondes. »", "Sourate Al-Anʿām, 6:162",
   "﴿ قُلْ إِنَّ صَلَاتِي وَنُسُكِي وَمَحْيَايَ وَمَمَاتِي لِلَّهِ رَبِّ الْعَالَمِينَ ﴾"]),
 S("PUNCHLINE", ["Le commerce est un des chemins qui y mènent.",
   "L'argent est un moyen puissant d'y avancer.",
   "Ce n'est pas un renoncement. C'est un changement de rang."]),
]

GG = [
 S("TITRE", ["CE QUI TE MANQUE N'EST PAS CE QUE TU CROIS"]),
 S("PUNCHLINE", ["Tu penses qu'il te manque une compétence métier.", "Presque jamais."]),
 VS("L'expertise métier", ["Elle est propre à ton métier", "Le couscous, le béton, le code",
    "C'est souvent ce que tu maîtrises le mieux", "Elle ne suffit jamais à elle seule"],
    "Les compétences transversales", ["Elles servent quel que soit le métier",
    "Vendre, se faire connaître, décider", "C'est presque toujours ce qui bloque",
    "Elles ne dépendent d'aucun secteur"], "→"),
 S("PUNCHLINE", ["Le meilleur pâtissier du quartier", "peut fermer boutique.",
   "Ce n'est pas la pâtisserie qui l'a tué."]),
 S("LISTE", ["QUATRE COMPÉTENCES, QUEL QUE SOIT TON PROJET",
   "1. Le marketing digital — être trouvé", "2. La vente — être choisi",
   "3. Le dîn — connaître les règles du jeu", "4. L'IA — augmenter ta portée"]),
 S("PUNCHLINE", ["Et les quatre changent de nature", "selon le paradigme qui les tient."]),

 S("TITRE", ["1. LE MARKETING DIGITAL"]),
 S("PUNCHLINE", ["Le monde où tu vends", "est déjà numérique.", "Que ça te plaise ou non."]),
 S("LISTE", ["CE QUI SE PASSE QUAND TU NE PARLES PAS",
   "Ton client cherche ton métier, et il trouve quelqu'un d'autre",
   "Ton concurrent explique ce qu'est un bon produit — et c'est le sien",
   "Celui qui parle le plus fort devient la référence, même s'il est moins bon",
   "👉 Ne pas communiquer, c'est aussi communiquer."]),
 S("PUNCHLINE", ["« Je ne veux pas me mettre en avant. »", "Vérifie que c'est de l'humilité,",
   "et pas une peur qui a trouvé un joli nom."],
   "À dire avec douceur : beaucoup de gens sincères se cachent derrière la pudeur. La question "
   "n'est pas de se montrer, c'est de se rendre trouvable par ceux qui te cherchent déjà."),
 S("LISTE", ["ORIENTÉ PAR LE BON PARADIGME, ÇA DONNE",
   "La légitimité vient de l'expertise, pas de la capacité à convaincre",
   "Ne pas tout montrer pour se faire connaître — le principe du voile s'applique ici aussi",
   "Une promesse vraie ET adaptée au palier de celui qui l'écoute",
   "👉 On se rend trouvable. On ne se transforme pas en produit."],
   "L'effet mécanique que personne ne relève : le personal branding concentre la valeur sur une "
   "personne plutôt que sur une œuvre. C'est de l'individualisme déguisé en communication."),

 S("TITRE", ["2. LA VENTE"]),
 S("PUNCHLINE", ["Il faut qu'on parle", "de ce mot qui te dérange."]),
 S("LISTE", ["CE QU'ON SE DIT TOUS, PLUS OU MOINS",
   "« Vendre, c'est forcer la main »", "« Si le produit est bon, il se vend tout seul »",
   "« Je ne veux pas être ce commercial-là »",
   "👉 Et pendant ce temps, personne n'achète."]),
 S("PUNCHLINE", ["La manipulation, c'est de faire faire à quelqu'un", "ce qui te sert à toi.",
   "Ce n'est pas la même chose que convaincre."]),
 S("PUNCHLINE", ["Si tu es convaincu que ton offre aide vraiment la personne en face,",
   "ne rien faire pour l'aider à franchir le pas,",
   "ce n'est pas de la délicatesse. C'est une trahison par timidité."]),
 S("LISTE", ["DEUX QUESTIONS, AVANT CHAQUE MÉCANIQUE",
   "1. Est-ce que c'est vrai ?", "2. Est-ce que ça sert vraiment cette personne-là ?",
   "👉 Deux oui : tu peux pousser fort. Un seul non : on jette."],
   "On vient de voir, deux slides plus haut, ce qu'on jette et ce qui le remplace. Le rappeler ici "
   "en une phrase : ce qu'on jette, ce n'est pas l'efficacité, c'est le mensonge."),

 S("TITRE", ["3. LE DÎN"]),
 S("PUNCHLINE", ["Les règles du jeu.", "Pas un supplément d'âme :", "une compétence technique."]),
 S("LISTE", ["CE QU'UN ENTREPRENEUR DEVRAIT SAVOIR NOMMER",
   "Le gharar — l'aléa, ce que ton client ne peut pas évaluer",
   "Le tadlîs — dissimuler le défaut",
   "Le ghubn — le déséquilibre excessif, même consenti",
   "L'iqāla — défaire une vente à la demande de celui qui regrette"]),
 S("PUNCHLINE", ["Tu n'as pas besoin d'être savant.", "Tu as besoin de savoir à qui demander,",
   "et de savoir que la question existe."]),

 S("TITRE", ["4. L'INTELLIGENCE ARTIFICIELLE"]),
 S("PUNCHLINE", ["Un outil donne de la vitesse.", "Pas une direction."]),
 S("PUNCHLINE", ["Et un outil sans direction", "t'emmène simplement plus vite",
   "là où tu ne voulais pas aller."]),
 VS("Éteindre son cerveau", ["Tu demandes quoi penser",
    "Tu ne sais plus pourquoi tu fais ce que tu fais",
    "Ton jugement se déplace dans la machine", "C'est le levier de l'aveuglement"],
    "Augmenter sa portée", ["Tu sais ce que tu veux dire",
    "Elle te fait aller dix fois plus vite pour le dire",
    "Ton jugement reste chez toi", "C'est le levier de l'impact"], "→"),
 S("PUNCHLINE", ["Le risque n'est pas qu'elle écrive à ta place.",
   "C'est qu'elle décide à ta place."]),
 S("LISTE", ["CE QU'ELLE FAIT VRAIMENT BIEN",
   "Elle t'oblige à formuler — et formuler est le travail que la plupart évitent",
   "Elle produit du générique, donc elle rend ton point de vue plus précieux",
   "Elle exécute pendant que tu réfléchis, jamais l'inverse",
   "👉 Et elle fabrique aussi de la fausse preuve. La frontière avec le tadlîs est à un clic."]),

 S("PUNCHLINE", ["Six axes pour le cap.", "Quatre compétences pour avancer.",
   "Reste à savoir dans quel ordre."]),
 S("PARTIE", ["PARTIE 3", "La méthodologie"]),
]

# ---------------------------------------------------------------- montage
# découpe en unités : bandes (texte brut) et slides
units = []          # ("band", txt) | ("slide", num, txt)
pos = 0
pat = re.compile(r"SLIDE (\d+) — \[[A-ZÉ]+\]\n.*?(?=\nSLIDE \d+ — \[|\n═|\Z)", re.S)
for m in pat.finditer(text):
    if m.start() > pos:
        units.append(("raw", text[pos:m.start()]))
    units.append(("slide", int(m.group(1)), m.group(0).rstrip("\n") + "\n"))
    pos = m.end()
if pos < len(text):
    units.append(("raw", text[pos:]))

def idx(n):
    for i, u in enumerate(units):
        if u[0] == "slide" and u[1] == n: return i
    raise KeyError(n)

def slides_of(nums):
    return [units[idx(n)] for n in nums]

def wrap(blocks):
    return [("slide", -1, b) for b in blocks]

# 1. programme : remplace 7,8,9
for n in (9, 8, 7):
    units.pop(idx(n))
units[idx(6)+1:idx(6)+1] = wrap(A)

# 2. laïcité cérébrale : après 17
units[idx(17)+1:idx(17)+1] = wrap(BB)

# 3. réplication : après 24
units[idx(24)+1:idx(24)+1] = wrap(CC)

# 4. filtre : 30, [32], D1, [31], 33..35, D2, 36
u30, u31, u32 = units[idx(30)], units[idx(31)], units[idx(32)]
for n in (32, 31):
    units.pop(idx(n))
i = idx(30) + 1
units[i:i] = [u32] + wrap(D1) + [u31]
units[idx(35)+1:idx(35)+1] = wrap(D2)

# 5. transition : PARTIE 2 avant 38 ; deux punchlines entre 38 et 39
units[idx(38):idx(38)] = wrap(E1)
units[idx(38)+1:idx(38)+1] = wrap(E2)

# 6. axe 1 : moteur avant 44 ; Riḍā après 49
units[idx(44):idx(44)] = wrap(F1)
units[idx(49)+1:idx(49)+1] = wrap(F2)

# 7. compétences transversales : après 170, avant 171
units[idx(170)+1:idx(170)+1] = wrap(GG)

# ---------------------------------------------------------------- écriture
out, n = [], 0
for u in units:
    if u[0] == "raw":
        out.append(u[1]); continue
    n += 1
    body = re.sub(r"^SLIDE (\d+|X) — ", "SLIDE %d — " % n, u[2], count=1)
    out.append(body if body.endswith("\n\n") else body.rstrip("\n") + "\n\n")
s = "".join(out)
s = re.sub(r"^\d+ slides\. Découpage.*$",
           "%d slides. Découpage : ouverture 15 min, cadre 25 min, six axes 18 min chacun, "
           "compétences transversales 20 min, clôture 20 min." % n, s, flags=re.M)
s = re.sub(r"\n{4,}", "\n\n\n", s)
open(SRC, "w").write(s)
print("slides:", n)
