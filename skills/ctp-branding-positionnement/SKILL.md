---
name: ctp-branding-positionnement
description: Construit, puis enrichit, la MARQUE d'un projet selon la méthode Collectif Tariqa PRO — branding (identité, associations, histoire de marque) ET positionnement + différenciateur, en un seul parcours. Vise un MVB (Minimum Valuable Brand) : une marque suffisante pour démarrer, pas une réflexion infinie. Interroge le membre une question à la fois et écrit un document de marque de référence par projet. Use when the user asks "définir ma marque", "mon branding", "construire mon image de marque", "mon positionnement", "mon différenciateur", "qu'est-ce qui me rend unique", "à quoi je veux qu'on m'associe", "mon histoire de marque", "me démarquer", "trouver mon angle", or wants to add/validate info about an existing brand/positioning.
metadata:
  version: 1.3.0
  category: tariqa-pro
---

# CTP Branding & Positionnement — architecte de marque (MVB)

Moteur d'interview + document vivant. Pose des questions **une à la fois**, produit
**un document de marque** (branding + positionnement + différenciateur), puis
l'enrichit et le valide. Trois corpus de méthode :
- `references/branding.md` — l'identité de marque (destination, associations, histoire).
- `references/methode.md` + `references/cadres.md` — le positionnement et le différenciateur.
- `references/gabarit.md` — le livrable.

Le **différenciateur n'est pas un skill à part** : c'est le cœur du volet
positionnement (« quel est mon différenciateur ? » se traite ici).

## Le rythme — une idée à la fois, jamais un pavé

⚠️ Le membre n'est pas venu lire, il est venu avancer. On pose **une idée**, on **vérifie
qu'elle est passée**, puis on avance. Pas de longueur à compter : le test est « est-ce que ça
se lit d'un coup d'œil, sans faire peur ? ». Et la plomberie (connecteurs, serveurs,
autorisations) ne sort jamais dans un message au membre — sauf s'il pose la question, et alors
on répond franchement. Détail : `coach-zaki/references/tenue-de-seance.md`.

## ⛔ Principe directeur — le MVB (Minimum Valuable Brand)

On s'adresse à des membres qui **démarrent**. Le piège mortel = tourner en rond des
semaines sur sa marque sans jamais rien publier. **Ce skill produit une marque V1
"suffisante pour démarrer" en UNE session, puis s'arrête.**

- **Assez bon → on avance.** À chaque bloc, dès qu'on a une réponse exploitable, on
  passe à la suivante. On ne cherche pas la formulation parfaite.
- **Une décision, pas dix options.** Si le membre hésite, on tranche avec lui sur la
  meilleure réponse du moment et on note ⏳ pour affiner plus tard.
- **STOP forcé en fin de parcours** : « Voilà ta marque V1. Elle est suffisante pour
  commencer à créer. On l'affinera quand tu auras de **vrais retours** — pas avant.
  La clarté viendra de l'usage, pas de la réflexion infinie. »
- Ta marque existe déjà dans la tête des gens, que tu le veuilles ou non. Le but n'est
  pas de la rendre parfaite, mais de **décider intentionnellement** ce qu'elle dit.

## Principe fondateur — moteur ≠ donnée

- **Le skill** = le moteur. Partageable tel quel.
- **La marque** = la donnée, vit dans le projet sous `positionnement/<slug>.md`
  (le doc de marque). Jamais dans le skill.

## Dépendances — la marque découle de la cible et de l'offre

Avant de commencer, charger ce qui existe :
- **Persona** (`personas/<slug>.md`) → ce que la cible veut, son langage.
- **Offre** (`offres/<slug>.md`) → ce que tu proposes, ta valeur.
- **Le bilan de l'état d'esprit** (`mindset/<slug>/bilan.md`) → **l'avantage
  non-égalitaire** : c'est le cœur du « pourquoi moi ». On le reprend tel quel,
  on ne le redemande pas.
Annoncer ce qu'on a chargé. Si l'un manque, le signaler et capter l'essentiel en
express, sans bloquer.

## Routage : choisir le mode au déclenchement

1. Regarder si `positionnement/` existe et contient des fichiers.
2. **Aucun** → mode **CREATE**.
3. **Présent** :
   - Info / apprentissage nouveau → mode **ENRICH**.
   - Nouvelle marque distincte (autre marché/offre) → CREATE (nouveau slug).
   - Doute → demander.

Toujours annoncer le mode choisi en une ligne avant de commencer.

## Mode CREATE — l'interview MVB (branding d'abord, positionnement ensuite)

1. Lire `references/branding.md`, `references/methode.md`, `references/cadres.md`,
   `references/gabarit.md`. Charger persona + offre si présents.
2. **Poser le cadre MVB** en une phrase (« on pose une marque suffisante pour
   démarrer, pas parfaite — on boucle vite, on affine avec l'usage »). Demander nom
   court + slug.
3. **Volet BRANDING** (suivre `references/branding.md`, une question à la fois) :
   - **Destination** : (a) dans ~1 an, à quoi ça ressemble ? (b) connu pour QUOI —
     **la « une seule chose »** ?
   - **Associations** : (c) 3 idées/mots qu'on doit associer à toi ; (d) 1-2 choses
     dont tu te démarques / refuses d'être associé (**anti-association**).
   - **Histoire de marque** (courte, 1-2 phrases chacune) : (e) **Catalyseur** —
     pourquoi ça existe / le déclic ; (f) **Vérité-cœur** — ce que tu crois que
     d'autres ne croient pas ; (g) **Preuve** — comment tu le montres (1-2 exemples
     concrets, même petits).
4. **Volet POSITIONNEMENT** (suivre `methode.md` + `cadres.md`, mais resté MVB) :
   recadrage → cadre de référence (alternatives, parité/différence) → **différenciateur
   (boîte à outils + test du concurrent + preuve)** → énoncé de positionnement (Moore)
   → ancrage CTP. Les frameworks avancés de `cadres.md` (archétypes, disciplines de
   valeur, création de catégorie) sont **optionnels** — ne les sortir que si le membre
   veut creuser, jamais comme passage obligé (anti-cycle).
5. Fin de chaque bloc : récap court + validation. Vague → 1 relance, puis ⏳ et on avance.
6. Écrire `positionnement/<slug>.md` selon `gabarit.md`. Chaque fait : **source** + **date**.
7. **Proposer le kit visuel** (voir section dédiée) puis le pointeur de persistance et
   un audit `ctp-compliant`. **Énoncer le STOP MVB.**

## Marque visuelle — deux livrables complémentaires

Une fois le concept de marque posé, proposer : « On pose ta **marque visuelle de
base** pour que tu puisses créer tes visuels (carrousels, vidéos, posts) ? »

Deux livrables, dans cet ordre :

### 1. Le kit texte — `brand/design-kit.md` (toujours)

La **spec réutilisable** que le membre rouvre pour Canva/Figma/CapCut. Produite
directement par ce skill, sans outil spécial. Déduire du concept déjà posé
(associations, « une seule chose », cible du persona) :

1. **Palette** : 3 à 5 couleurs avec **codes hex** — dominante, secondaire, accent,
   + neutres. Une ligne sur le lien avec les associations voulues.
2. **Typographies** : 1 titre + 1 corps (polices courantes/gratuites : Google Fonts,
   système). Tailles indicatives.
3. **Règles d'usage** : 3 « à faire » / 3 « à éviter ». Espacement, forme générale.
4. **Cohérence fond ↔ forme** : rappeler les 3 associations + l'anti-association.

Écrire dans **`brand/design-kit.md`** (créer le dossier `brand/`). Format : voir
`references/gabarit-design-kit.md`. MVB : on s'arrête au suffisant, on affine à l'usage.

### 2. Les planches visuelles — via le skill `ctp-brandkit` (bundlé)

Pour aller plus loin que le texte (planches de guidelines, **concepts de logo**,
mockups, univers visuel), **passer la main au skill `ctp-brandkit`** — il est
**inclus dans le plugin** (aucune install séparée). Lui fournir : les associations
de marque, la palette + typos du `design-kit.md`, la « une seule chose » et la cible.

- `ctp-brandkit` est **présent pour tout membre** du plugin. Le **rendu d'images**,
  lui, dépend de la capacité de génération d'images du Claude du membre (runtime) :
  si elle est dispo → planches rendues ; sinon → il fournit la direction artistique
  complète, prête à exécuter dans un outil de design.
- Ne jamais bloquer : le `design-kit.md` texte suffit déjà pour démarrer.

La marque visuelle **du membre est la sienne** — ne pas lui imposer la charte CTP
(beige/noir/or). Exception : si le projet EST le Collectif Tariqa PRO lui-même.

## Mode ENRICH — ajouter sans casser

1. Charger le fichier ciblé en entier.
2. Chaque info passe par **VALIDATE**.
3. Écrire après accord. Section + date + source. Montrer le diff.

## Mode VALIDATE — règle de cohérence (toujours avant écriture)

- **Nouvelle** → proposer où l'ajouter.
- **Confirmation** → noter corroborée.
- **Contradiction** → **ne pas écraser en silence** : montrer les deux, demander,
  archiver l'ancienne en note datée.
- **Hors-cible** → signaler, ne pas ajouter.

## Garde-fous spécifiques au différenciateur

- **Test du concurrent obligatoire** : si un concurrent pourrait dire la même phrase,
  ce **n'est pas** un différenciateur → recommencer.
- Un différenciateur **non prouvé** est une hypothèse, étiquetée comme telle.
- Ne pas confondre **parité** (table stakes) et **différenciateur** (ce que toi seul
  peux revendiquer crédiblement).

## Cohérence Tariqa PRO

- La marque vise à proposer une **alternative** crédible, utile, éthique — pas à
  écraser. L'anti-association / anti-positionnement assumé est un atout.
- Pas de garantie de résultat dans la promesse.
- À la fin, proposer `ctp-compliant` sur la marque.
- La **voix** (formulation) = skill `ctp-voix`. Ici on fixe le **fond** (identité, angle).
- Pas de chiffres d'argent mis en avant dans les sorties publiques.

## Persistance

Ligne à ajouter au `CLAUDE.md` du projet :

```
## Marque de référence
Branding, positionnement et différenciateur dans `positionnement/<slug>.md` ;
kit visuel dans `brand/design-kit.md`. Boussole de tout contenu, page et visuel
de ce projet (skill `ctp-branding-positionnement`).
```

En CREATE, après écriture, proposer d'ajouter cette ligne.

## Garde-fous

- **MVB d'abord** : viser une V1 suffisante en une session, puis STOP. Ne jamais
  entretenir un cycle de réflexion sans fin.
- Une question à la fois. Jamais écrire sans validation.
- Marque floue → forcer le minimum : 1 chose à être connu pour + 3 associations +
  1 différenciateur qui passe le test du concurrent + 1 preuve.
- Fait validé vs hypothèse : toujours distingués.
