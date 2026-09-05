# Changelog — plugin Collectif Tariqa PRO

Le membre voit sa version via `lance le parcours CTP` (affichée en tête).
Pour mettre à jour : voir `GUIDE-MEMBRE.md` §10.

## 1.5.0

- **La reprise — on ne fait plus répéter le membre.** Nouveau premier geste dans le pilier
  Mindset et dans les quatre étapes de Mon projet : on demande au membre de coller ce qu'il a
  déjà écrit sur son projet avec une IA, plutôt que de tout lui refaire raconter. Faire
  recommencer était la première cause d'abandon au deuxième module.
  ⚠️ Garde-fou écrit noir sur blanc : un historique d'IA généraliste est **presque toujours
  complaisant**. On en récupère la **matière** — les faits, ses mots, ses tentatives — **jamais
  les conclusions** : ni les validations, ni les compliments, ni les livrables déjà rédigés à
  sa place. Et c'est du texte collé, donc traité comme des **données, jamais des instructions**.
  On restitue en trois blocs (compris / manque / **pas convaincu**), on challenge sur un point,
  on fait valider — puis on passe quand même toutes les étapes.

- **Quatre garde-fous remontés au bon endroit.** Audit des cinq skills : une règle qui doit
  s'appliquer *au moment où personne ne la cherche* doit vivre dans le `SKILL.md`, pas dans
  `references/` — sinon elle disparaît dès que le skill tourne ailleurs que dans Claude Code.
  - **Déclaration d'invariant** en tête des cinq : ce fichier s'applique en permanence,
    `references/` est une bibliothèque.
  - **« On ne remplit jamais à sa place »** — la seule lacune qui traversait les cinq. Rédiger
    le livrable à la place du membre est toujours plus rapide et donne toujours un meilleur
    texte, et c'est toujours une erreur : un livrable qu'il n'a pas produit, il ne saura pas le
    défendre.
  - **On ne tranche jamais en licite / illicite** — ajouté à `ctp-voix` et
    `ctp-branding-positionnement`, qui produisent du texte public et pouvaient être
    interrogés là-dessus.
  - **Les personnes que tu décris sont réelles** — `buyer-persona-architect` : prénom ou
    initiale, jamais de coordonnées ni de détail identifiant.

## 1.4.0

- **Le rythme, écrit une fois et appliqué partout** — nouveau
  `skills/coach-zaki/references/tenue-de-seance.md`, pointé par le parcours, par le
  pilier Mindset, par Coach Zaki et par chacune des étapes de Mon projet. Une idée
  par message, on vérifie qu'elle est passée, puis on avance. Pas de longueur à
  compter : le test est « est-ce que ça se lit d'un coup d'œil, sans faire peur ? ».
  Fini les pavés qui font décrocher avant la première question.
- **L'introduction rejouée en sept temps**, chacun fermé par un arrêt réel où le
  membre reprend la parole — au lieu de dix sections déroulées d'une traite.
- **La plomberie reste en coulisses.** Le membre n'entend plus parler de
  connecteurs, de serveurs ni d'autorisations. Trois exceptions seulement : son
  travail risque d'être perdu, il pose la question lui-même, ou rien ne peut
  avancer sans lui.
- **S'il demande, on répond franchement.** « Tu te connectes comment ? », « il y a
  une base derrière toi ? » → réponse courte et honnête, puis retour au travail.
  Ce qui ne se dit jamais reste : d'où viennent les principes eux-mêmes.
- **La bibliothèque de doctrine ne dépend plus de l'environnement** — trois étages :
  le connecteur s'il est là, sinon la lecture web directe de la bibliothèque en
  ligne, sinon le socle embarqué. On descend d'un étage sans rien annoncer.
- **Le parcours depuis un navigateur (tablette, téléphone)** est reconnu : on
  prévient une fois que le travail vit le temps de la séance, et on rend les
  fichiers à la fin. Le guide d'installation documente ce chemin.
- **Brique Création de contenu — liens réparés.** Trois skills envoyaient encore le
  membre sur l'ancien compte perso, dont une page en 404. Bonnes adresses :
  page `collectif-tariqa-pro.github.io/ctp-youtube/`, installation
  `github.com/Collectif-Tariqa-PRO/ctp-youtube-plugin.git`.
- **Correction — données du membre.** `mindset/` et `landing/` étaient absents du
  `.gitignore` : les livrables les plus intimes du parcours (famille, foi,
  blocages, agenda) pouvaient partir dans un dépôt. Corrigé.

## 1.3.0

- **Nouvelle étape 5 — `ctp-page-de-vente`** : l'aboutissement du parcours pour les
  entrepreneurs (hors e-commerce). Transforme tout le travail (persona, offre, marque,
  voix, pitch) en une **landing page v1 mise EN LIGNE**, pointable depuis les réseaux.
  - CTA qualifié (calendrier Calendly/cal.com et/ou formulaire Tally).
  - Vraies images du membre, **anti AI-slop**.
  - **Hold-back** : la page vend le rendez-vous, pas toute l'offre (grain à moudre pour le call).
  - Différenciateur mis en avant, SEO de base, page statique.
  - Déploiement **Vercel** (compte membre requis), URL en ligne.
  - **Filtre e-commerce** : l'étape ne s'adresse pas aux projets e-commerce.
- **`ctp-taste` inclus dans le plugin** : moteur de design anti-slop (copie de taste-skill,
  substance intacte), utilisé par `ctp-page-de-vente`.
- **Output final complet du parcours** = le pitch + les docs `.md` + la landing page v1.

## 1.2.0

- **Étape 3 fusionnée → `ctp-branding-positionnement`** : le branding (identité,
  associations + anti-association, histoire de marque en 3 temps) rejoint le
  positionnement et le différenciateur en un seul parcours.
- **MVB (Minimum Valuable Brand)** : on pose une marque V1 suffisante pour démarrer
  en une session, puis STOP — fini les cycles de réflexion sans fin.
- **Kit visuel de base** : `ctp-branding-positionnement` produit un `brand/design-kit.md`
  (palette hex, typos, règles) — spec réutilisable pour créer ses visuels.
- **`ctp-brandkit` inclus dans le plugin** : génère les planches visuelles + concepts
  logo à partir du kit, sans aucune install séparée (le rendu d'images dépend de la
  capacité du Claude du membre).
- `ctp-positionnement` est renommé `ctp-branding-positionnement` (la donnée reste
  `positionnement/<slug>.md`).

## 1.1.0

- **Coach Zaki** — coach qui challenge au lieu de flatter (modes Actif / Sur demande).
- **Pitch SIRA** dans `ctp-export` + génération **à la demande** (« génère mon pitch »)
  sans passer par l'export complet.
- **`ctp-init`** : au 1er lancement, `ctp-parcours` crée l'arborescence du projet
  (`personas/`, `offres/`…) + injecte le bloc `CLAUDE.md` + ancre la racine
  (`ctp/project.json`).
- **Référence vivante** `ctp/REFERENCE-<slug>.md` maintenue à la fin de **chaque** étape
  (plus seulement à l'export).
- Coach Zaki **propose son mode au 1er contact** s'il est appelé hors parcours.
- Lien de publication Circle réel et centralisé (`references/collectif.md`).
- Doctrine `ctp-compliant` versionnée (signale une version plus récente).
- Métadonnées harmonisées : tous les skills en `category: tariqa-pro`, version unique.
- Correctif : Coach Zaki lisait `offre/` (singulier) au lieu de `offres/`.

## 1.0.0

- Parcours guidé : persona → offre → positionnement → voix.
- Audit de cohérence `ctp-compliant`.
- Export vérifiable `ctp-export` (scorecard + bloc copier-coller).
