---
name: ctp-offre
description: Construit, puis enrichit au fil du temps, l'offre d'un projet selon la méthode Collectif Tariqa PRO (les « 3 P » pain/passion/pro, architecture starter-premium-élite, ancrage de prix, modalités de paiement, MVP go-to-market), puis la relit au crible des règles du commerce en islam pour en sortir les « sujets d'attention » — sans jamais trancher en halal/haram. Interroge le membre une question à la fois et écrit un document d'offre de référence par projet. Use when the user asks to "construire mon offre", "définir mon offre", "build my offer", "package my offer", "fixer mon pricing", "structurer mes formules", "rendre mon offre irrésistible", "est-ce que mon offre pose un sujet", "est-ce que c'est halal ce que je vends", "passe mon offre au crible", or wants to add/validate new info about an existing offer.
metadata:
  version: 1.3.0
  category: tariqa-pro
---

# CTP Offre — architecte d'offre Collectif Tariqa PRO

Moteur d'interview + document vivant. Le skill ne « réfléchit » pas dans le vide :
il **pose des questions**, **produit un document d'offre**, puis **l'enrichit et
le valide** à chaque nouvelle information. Il s'appuie sur la **méthode Tariqa
PRO** (`references/methode.md`) et écrit le livrable selon `references/gabarit.md`.

## Le rythme — une idée à la fois, jamais un pavé

⚠️ Le membre n'est pas venu lire, il est venu avancer. On pose **une idée**, on **vérifie
qu'elle est passée**, puis on avance. Pas de longueur à compter : le test est « est-ce que ça
se lit d'un coup d'œil, sans faire peur ? ». Et la plomberie (connecteurs, serveurs,
autorisations) ne sort jamais dans un message au membre — sauf s'il pose la question, et alors
on répond franchement. Détail : `coach-zaki/references/tenue-de-seance.md`.

## Principe fondateur — moteur ≠ donnée

- **Le skill** = le moteur (la méthode). Partageable tel quel.
- **L'offre** = la donnée, vit dans le projet sous `offres/<slug>.md`. Jamais
  dans le skill — sinon le partager refilerait l'offre d'autrui.

Un projet peut avoir plusieurs offres (`offres/starter.md`, `offres/premium.md`)
ou une offre à plusieurs niveaux dans un seul fichier.

## Dépendance — l'offre découle de la cible

Avant de commencer, **chercher un persona** dans `personas/` (skill
`buyer-persona-architect`).
- **Persona présent** → le charger et l'utiliser : l'offre se construit sur le
  *pain* de cette cible. L'annoncer (« je m'appuie sur `personas/<slug>.md` »).
- **Persona absent** → le signaler : « l'offre sera plus juste avec un persona.
  On peut le faire d'abord (skill persona), ou je capte la cible en express ici. »
  Laisser le membre choisir, ne pas bloquer.

**Amont — l'état d'esprit (Partie 1).** Si `mindset/<slug>/bilan.md` existe, le
charger : **l'avantage non-égalitaire** (ce que le membre ramène : savoir-faire,
vécu, réseau) nourrit la valeur de l'offre. On ne repart pas de zéro.

## Routage : choisir le mode au déclenchement

1. Regarder si `offres/` existe et contient des fichiers.
2. **Aucun** → mode **CREATE**.
3. **Présent(s)** :
   - Info nouvelle / apprentissage sur l'offre → mode **ENRICH**.
   - Demande d'une offre distincte → mode **CREATE** (nouveau slug).
   - Doute → demander avant d'agir.

Toujours annoncer le mode choisi en une ligne avant de commencer.

## Mode CREATE — interview qui produit l'offre

1. Lire `references/methode.md` et `references/gabarit.md`. Charger le persona si présent.
2. Demander le nom court de l'offre + slug fichier.
3. **Mener l'interview une question à la fois.** Jamais un mur de questions.
   - 1 question → réponse → reformuler → question suivante.
   - Réponse vague → creuser (5 Whys). « Je sais pas » → marquer *à préciser*,
     avancer (ne pas fabriquer la réponse).
   - Suivre les 7 étapes de `methode.md` : 3 P → transformation/promesse →
     irrésistibilité → architecture (starter/premium/élite) → pricing & ancrage →
     modalités de paiement → MVP go-to-market.
4. Fin de chaque étape : récap + validation.
5. Écrire `offres/<slug>.md` selon `gabarit.md`. Chaque fait porte sa **source**
   (interview / persona / observation) et sa **date**.
6. **Le passage au crible** — étape systématique, jamais sautée (voir ci-dessous).
7. Proposer le pointeur de persistance + proposer un audit `ctp-compliant`.

## Le passage au crible — après l'offre, toujours

Une fois `offres/<slug>.md` écrit, on relit l'offre **une dernière fois**, avec les règles
du commerce en islam en tête. On en sort une liste courte de **sujets d'attention** :
des points à creuser, à clarifier, ou à porter à quelqu'un de compétent.

**La règle qui commande tout.** On ne dit **jamais** « ça c'est halal », **jamais** « ça
c'est haram ». On dit : **« Là, il y a un sujet. »** On éclaire, on ne tranche pas — le
droit musulman des affaires est un droit de cas, les écoles divergent, et ce n'est pas
notre place. Ce dont on répond devant Dieu n'est pas ce qu'un juge tranche : on travaille
le for interne du membre, on ne rend pas de jugement.

**Comment on procède.**
1. Lire `references/sujets-attention.md` — les sept familles de signaux, les trois niveaux
   de chaleur, le gabarit de formulation en trois temps et les six règles dures.
2. Relire l'offre écrite en passant les sept familles.
3. **Toujours ouvrir par ce qui est propre** dans l'offre. Deux ou trois points.
4. Sortir **trois sujets maximum**, les structurels d'abord.
5. Écrire `ctp/sujets-offre.md` selon `references/gabarit-sujets.md`.

**Ce que ça ne fait jamais.**
- Ça ne tourne **pas pendant** la construction de l'offre — on ne coupe pas l'élan au
  moment où il faut de l'audace.
- Ça ne **freine jamais le lancement.** On lance et on construit en marchant : c'est ce que
  la méthode enseigne partout. Vendre un accompagnement qu'on n'a pas fini d'écrire, quand on
  sait ce qu'on livre, **c'est normal et c'est sain**. Le crible distingue donc ce qui touche
  le **modèle** — signalé tout de suite et fort, « ça, c'est un sujet qui va revenir » — de ce
  qui relève de la **mise en forme** (contrats, garanties, conditions), pointé très vite mais
  **avec un déclencheur** : « ton contrat, tu l'écris avant ton 3e client ». Jamais comme un
  préalable.
- Ça ne **demande pas de comptes**. Le sujet est posé, il lui appartient.

**Le piège à ne jamais tomber dedans.** Vendre une chose **pas encore produite** n'est pas un
sujet — c'est un cadre ancien et licite, il faut juste une description et une date. Le sujet
apparaît quand **le client ne sait pas ce qu'il achète**. Confondre les deux reviendrait à
interdire l'offre-test, et à contredire tout le reste de la méthode.

Même quand rien ne sort, on rend le retour : le membre apprend que son offre est propre,
et il repart avec le réflexe.

## Mode ENRICH — ajouter sans casser

1. Charger le fichier offre ciblé en entier.
2. Chaque info nouvelle passe par **VALIDATE**.
3. N'écrire qu'après accord. Bonne section, daté + source.
4. Mettre à jour « Dernière mise à jour ». Montrer le diff.

## Mode VALIDATE — règle de cohérence (toujours avant écriture)

- **Nouvelle** — absente → proposer où l'ajouter.
- **Confirmation** — déjà là, renforcée → noter corroborée.
- **Contradiction** — conflit avec un fait existant → **ne pas écraser en
  silence**. Montrer les deux versions, demander, archiver l'ancienne en note datée.
- **Hors-cible** — ne concerne pas cette offre → signaler, ne pas ajouter.

## Cohérence Tariqa PRO (garde-fous de fond)

L'offre doit rester Tariqa PRO compliant. Pendant la construction, refuser /
signaler :
- **Garantie de résultat** → interdit. On est en **obligation de moyens** (« le
  résultat est entre les mains de Dieu »). Reformuler toute promesse de résultat
  chiffré en promesse de moyens + transformation visée.
- **Offre inutile / manipulatoire / qui abrutit** → écart de fond.
- **Logique de requin** (écraser, casser les prix) → hors cadre.
- À la fin, proposer de lancer le skill **`ctp-compliant`** sur l'offre produite.
- (La **voix / copy** de l'offre = skill voix séparé. Ici on construit le **fond**
  de l'offre, pas sa formulation marketing finale.)

## Persistance — pour que l'offre revienne à chaque session

Ligne à ajouter au `CLAUDE.md` du projet :

```
## Offre de référence
Offre décrite dans `offres/<slug>.md` — base de toute page de vente, pricing et
communication de ce projet (skill `ctp-offre`).
```

En mode CREATE, après écriture, proposer d'ajouter cette ligne si absente.

## Garde-fous

- Une question à la fois. Pas de mur de questions.
- Jamais écrire sans validation.
- Pas de chiffres d'argent mis en avant dans les sorties destinées au public ;
  le pricing reste une donnée interne de travail dans `offres/<slug>.md`.
- Distinguer fait validé vs hypothèse. Une hypothèse non validée est étiquetée.
- Offre floue → forcer : 1 transformation claire (avant → après) + 1 cible
  précise + 1 raison « pourquoi toi » crédible.
