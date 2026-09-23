# -*- coding: utf-8 -*-
exec(open("/tmp/claude-0/webi/gabarits.py").read())

OUT = "/tmp/claude-0/-home-user-ctp-plugin/5bde7487-de28-5f85-acc6-6f6c831c1436/scratchpad/art/Nouvelles-slides-a-inserer.pptx"

def add(kind, data, note):
    if kind == "titre":     s_titre(data, note)
    elif kind == "partie":  s_partie(data, note)
    elif kind == "punch":   s_punch(data, note)
    elif kind == "liste":   s_liste(data, note)
    elif kind == "citation":
        q, src, ar = data
        s_citation([q, src] + ([ar] if ar else []), note)
    elif kind == "vs":
        lt, li, rt, ri, sep = data
        s_vs(dict(lt=lt, li=li, rt=rt, ri=ri, sep=sep), note)

def WHERE(where): return "→ INSÉRER " + where

# ============================================================== le pack
P = []
def block(label, where, slides):
    for i, (k, d) in enumerate(slides):
        note = WHERE(where) if i == 0 else "↑ suite du bloc « %s »" % label
        P.append((label, k, d, note))

block("A · Programme",
 "EN REMPLACEMENT de tes trois slides 1️⃣ 2️⃣ 3️⃣ qui suivent « CE SOIR, TU REPARS AVEC TROIS CHOSES »", [
 ("liste", ["1️⃣ CE QUE NOTRE DÎN DIT DU BUSINESS",
   "Pas de ton produit. Pas de ton financement.",
   "Du business lui-même : à quoi il sert, quand il est réussi, ce qu'il te demande."]),
 ("liste", ["2️⃣ SIX DÉCISIONS QUE TU PRENDRAS AUTREMENT DÈS LUNDI",
   "Comment tu fixes ton prix. Ce que tu fais quand un concurrent s'installe.",
   "Ce que tu proposes à un client qui va mieux. Quand tu décides de grandir.",
   "👉 Pour chacune : ce que tu changes concrètement, dès cette semaine."]),
 ("liste", ["3️⃣ NOTRE MÉTHODOLOGIE POUR ENTREPRENDRE",
   "Six piliers, et les techniques modernes qui s'y branchent —",
   "marketing digital, vente, IA — une fois orientées par le bon cap.",
   "👉 Pas une philosophie. Un mode d'emploi."]),
])

block("B · Laïcité cérébrale",
 "APRÈS ta slide « On a tous appris à vérifier le comment. Personne ne nous a appris à vérifier le vers quoi. »", [
 ("titre", ["LA LAÏCITÉ CÉRÉBRALE"]),
 ("punch", ["Tu pries.", "Tu jeûnes.", "Et tu ouvres ton business plan."]),
 ("punch", ["Et à ce moment-là, sans t'en rendre compte,", "tu as fermé une porte."]),
 ("liste", ["DEUX TIROIRS, ET ON N'OUVRE JAMAIS LES DEUX EN MÊME TEMPS",
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
])

block("C · Syndrome de la réplication",
 "APRÈS ta slide « Tu en as un. La question n'est pas si. La question est lequel. »", [
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
 ("liste", ["ET LES OUTILS, ON LES AVAIT DÉJÀ",
   "Se lever avant l'aube — le fajr",
   "Se priver volontairement pour reprendre la main — le jeûne",
   "La gratitude — le shukr", "Le bilan de soi — la muhāsaba", "La réflexion — le tafakkur"]),
 ("punch", ["On ne t'a pas vendu une méthode nouvelle.", "On t'a revendu la tienne,",
   "en lui retirant son destinataire."]),
])

block("D · Le filtre",
 "APRÈS ta slide « MAIS MOI J'AI DÉJÀ NETTOYÉ », donc AVANT ta slide VS « LE FILTRE / LE PARADIGME »", [
 ("titre", ["LE FILTRE"]),
 ("liste", ["CE RÉFLEXE, ON L'A TOUS APPRIS, ET IL EST BON",
   "Une pratique se présente", "Tu demandes : est-ce que c'est licite ?",
   "Selon la réponse, tu gardes ou tu jettes",
   "👉 Il a protégé des milliers d'entrepreneurs. Rien ici ne vise à l'affaiblir."]),
 ("punch", ["Mais il a une limite,", "et elle est structurelle."]),
 ("punch", ["Il opère sur les actes, un par un.", "Jamais sur le cadre qui les produit."]),
])
block("D bis · Le filtre",
 "APRÈS ta slide « Alors il n'y a rien chez nous ? Si. Énormément. »", [
 ("punch", ["Et pendant ce temps, on a tout ce qu'il faut.",
   "On ne l'a simplement jamais sorti de la bibliothèque."]),
])

block("E · Transition",
 "AVANT ta slide « ON ARRÊTE LA THÉORIE ». Ta PARTIE 2 n'existe pas : c'est celle-ci.", [
 ("partie", ["PARTIE 2", "Les six axes"]),
])
block("E bis · Transition",
 "ENTRE ta slide « ON ARRÊTE LA THÉORIE » et ta slide « SIX ENDROITS OÙ ÇA SE VOIT DANS TON AGENDA »", [
 ("punch", ["Tout ce qu'on vient de dire ne vaut rien", "si tu ne peux pas le voir",
   "dans ton agenda de la semaine dernière."]),
 ("punch", ["Alors regardons où ça se voit.", "Six endroits précis."]),
])

block("F · Axe 1, le moteur",
 "AVANT ta slide Milton Friedman « LA RESPONSABILITÉ SOCIALE DE L'ENTREPRISE… »", [
 ("titre", ["LE MOTEUR DE LA MODERNITÉ"]),
 ("punch", ["Toute civilisation tourne autour d'un moteur.",
   "Le nôtre s'appelait la recherche de Son agrément.",
   "Celui qu'on nous a donné s'appelle l'accumulation."]),
])
block("F bis · Axe 1, le Riḍā",
 "AVANT ta slide du verset 6:162 « Dis : en vérité, ma prière… » — tu l'as déjà, je ne la redonne pas", [
 ("titre", ["NOUS, LE BUT, C'EST LE RIḌĀ"]),
])
block("F ter · Axe 1, le Riḍā",
 "APRÈS ta slide du verset 6:162", [
 ("punch", ["Le commerce est un des chemins qui y mènent.",
   "L'argent est un moyen puissant d'y avancer.",
   "Ce n'est pas un renoncement. C'est un changement de rang."]),
])

block("G · Compétences transversales",
 "ENTRE ta slide « Ce qu'on jette, ce n'est pas l'efficacité. C'est le mensonge. » et ta slide « LA MÉTHODE, EN UNE PAGE ». "
 "Et remonte ta slide PARTIE 3 juste après ce bloc.", [
 ("titre", ["CE QUI TE MANQUE N'EST PAS CE QUE TU CROIS"]),
 ("punch", ["Tu penses qu'il te manque une compétence métier.", "Presque jamais."]),
 ("vs", ("L'expertise métier", ["Elle est propre à ton métier", "Le couscous, le béton, le code",
   "C'est souvent ce que tu maîtrises le mieux", "Elle ne suffit jamais à elle seule"],
   "Les compétences transversales", ["Elles servent quel que soit le métier",
   "Vendre, se faire connaître, décider", "C'est presque toujours ce qui bloque",
   "Elles ne dépendent d'aucun secteur"], "→")),
 ("punch", ["Le meilleur pâtissier du quartier", "peut fermer boutique.",
   "Ce n'est pas la pâtisserie qui l'a tué."]),
 ("liste", ["QUATRE COMPÉTENCES, QUEL QUE SOIT TON PROJET",
   "1. Le marketing digital — être trouvé", "2. La vente — être choisi",
   "3. Le dîn — connaître les règles du jeu", "4. L'IA — augmenter ta portée"]),
 ("punch", ["Et les quatre changent de nature", "selon le paradigme qui les tient."]),
 ("titre", ["1. LE MARKETING DIGITAL"]),
 ("punch", ["Le monde où tu vends", "est déjà numérique.", "Que ça te plaise ou non."]),
 ("liste", ["CE QUI SE PASSE QUAND TU NE PARLES PAS",
   "Ton client cherche ton métier, et il trouve quelqu'un d'autre",
   "Ton concurrent explique ce qu'est un bon produit — et c'est le sien",
   "Celui qui parle le plus fort devient la référence, même s'il est moins bon",
   "👉 Ne pas communiquer, c'est aussi communiquer."]),
 ("punch", ["« Je ne veux pas me mettre en avant. »", "Vérifie que c'est de l'humilité,",
   "et pas une peur qui a trouvé un joli nom."]),
 ("liste", ["ORIENTÉ PAR LE BON PARADIGME, ÇA DONNE",
   "La légitimité vient de l'expertise, pas de la capacité à convaincre",
   "Ne pas tout montrer pour se faire connaître — le principe du voile s'applique ici aussi",
   "Une promesse vraie ET adaptée au palier de celui qui l'écoute",
   "👉 On se rend trouvable. On ne se transforme pas en produit."]),
 ("titre", ["2. LA VENTE"]),
 ("punch", ["Il faut qu'on parle", "de ce mot qui te dérange."]),
 ("liste", ["CE QU'ON SE DIT TOUS, PLUS OU MOINS",
   "« Vendre, c'est forcer la main »", "« Si le produit est bon, il se vend tout seul »",
   "« Je ne veux pas être ce commercial-là »",
   "👉 Et pendant ce temps, personne n'achète."]),
 ("punch", ["La manipulation, c'est de faire faire à quelqu'un", "ce qui te sert à toi.",
   "Ce n'est pas la même chose que convaincre."]),
 ("punch", ["Si tu es convaincu que ton offre aide vraiment la personne en face,",
   "ne rien faire pour l'aider à franchir le pas,",
   "ce n'est pas de la délicatesse. C'est une trahison par timidité."]),
 ("liste", ["DEUX QUESTIONS, AVANT CHAQUE MÉCANIQUE",
   "1. Est-ce que c'est vrai ?", "2. Est-ce que ça sert vraiment cette personne-là ?",
   "👉 Deux oui : tu peux pousser fort. Un seul non : on jette."]),
 ("titre", ["3. LE DÎN"]),
 ("punch", ["Les règles du jeu.", "Pas un supplément d'âme :", "une compétence technique."]),
 ("liste", ["CE QU'UN ENTREPRENEUR DEVRAIT SAVOIR NOMMER",
   "Le gharar — l'aléa, ce que ton client ne peut pas évaluer",
   "Le tadlîs — dissimuler le défaut",
   "Le ghubn — le déséquilibre excessif, même consenti",
   "L'iqāla — défaire une vente à la demande de celui qui regrette"]),
 ("punch", ["Tu n'as pas besoin d'être savant.", "Tu as besoin de savoir à qui demander,",
   "et de savoir que la question existe."]),
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
 ("liste", ["CE QU'ELLE FAIT VRAIMENT BIEN",
   "Elle t'oblige à formuler — et formuler est le travail que la plupart évitent",
   "Elle produit du générique, donc elle rend ton point de vue plus précieux",
   "Elle exécute pendant que tu réfléchis, jamais l'inverse",
   "👉 Et elle fabrique aussi de la fausse preuve. La frontière avec le tadlîs est à un clic."]),
 ("punch", ["Six axes pour le cap.", "Quatre compétences pour avancer.",
   "Reste à savoir dans quel ordre."]),
])

for i, (label, k, d, note) in enumerate(P, 1):
    add(k, d, "[%02d / %s]  %s" % (i, label, note))
prs.save(OUT)

print(len(P), "slides ->", OUT, os.path.getsize(OUT), "octets\n")
cur = None
for i, (label, k, d, note) in enumerate(P, 1):
    if label != cur:
        cur = label
        print("\n%s" % label)
        print("   %s" % note.split("]  ")[1])
    first = d[0] if isinstance(d, list) else (d[0] if k != "vs" else d[0])
    print("   %02d  %-9s %s" % (i, k, (first if isinstance(first, str) else str(first))[:64]))
