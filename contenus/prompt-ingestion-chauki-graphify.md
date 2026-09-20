# Prompt — ingérer le corpus Chauki Lazhar dans Graphify

> À coller dans une session Claude Code **tournant sur le Mac de Zaki** (les chemins
> `~/CTP-master-graph`, `~/CTP-vimeo`, `~/CTP-taqwa-impact` n'existent que là).
> Rédigé le 20 septembre 2026 depuis la session « Paradigme entrepreneurial musulman ».

---

Tu travailles sur la base de connaissances du Collectif Tariqa PRO — le graphe Graphify.

**Objectif : ajouter le corpus Dr Chauki Lazhar comme neuvième corpus du graphe maître, puis
régénérer l'export d'équipe.**

## Contexte

Le graphe maître vit dans `~/CTP-master-graph`. Il fusionne aujourd'hui huit corpus :
`vimeo`, `taqwa`, `youtube`, `crm`, `vidiq`, `fiches`, `parcours`, `loom`, `doctrine`.
Son export partageable est publié dans le dépôt privé
`Collectif-Tariqa-PRO/ctp-base-connaissances`, sous `graphify-out/graph.json`
(état actuel : 4 699 nœuds, 7 471 liens).

Dr Chauki Lazhar est professeur à l'Université du Qatar, directeur adjoint fondateur du CILE,
spécialiste des usul al-fiqh. Sa chaîne `@chaukilazhar` a été scannée intégralement en
septembre 2026 : 98 vidéos inventoriées, ~45 transcripts tirés, ~38 lus. **Il apporte au
Collectif le niveau paradigme** — la méthode pour évaluer un objet importé. Il n'est
actuellement pas dans le graphe : zéro nœud.

## Étape 0 — Lire la spécification

Elle est déjà écrite. Dans le dépôt `ctp-plugin`, sur la branche
`claude/personal-development-video-script-xn7xum` (non mergée dans `main`) :

```
git fetch origin claude/personal-development-video-script-xn7xum
git show FETCH_HEAD:docs/contenus/source-chauki-lazhar.md
```

Lis-le en entier. La section **②.5 « Protocole d'ingestion (graphify) »** est la
spécification de ce travail. Lis aussi `docs/contenus/notes-brutes-chauki-lazhar.md`
sur la même branche.

## Étape 1 — Retrouver les transcripts, ne pas les re-tirer

Environ 45 transcripts ont déjà été tirés et sont sur le disque. **Localise-les avant toute
chose** (cherche du côté de `~/CTP-chauki`, `~/CTP-master-graph`, ou les dossiers de travail
de la session du 7-9 septembre). Chaque appel de transcription coûte des crédits vidIQ :
**ne re-tire jamais un transcript déjà présent.** Ne complète que ce qui manque réellement.

**Périmètre à ingérer** (~60 vidéos) : la série *Istikhlāf — La Vision Islamique du Monde*
(17 ép.), les *Finalités supérieures / maqāsid* (émission Orix Islam, 17), *Méthodologie &
modernité* (5), *Un jour un verset* (13), *Théologie / anthropologie* (8).

**À exclure :** le fiqh social grand public (16 vidéos) — hors périmètre CTP, exclusion déjà
confirmée. **À écarter :** *Les Noms Sublimes d'Allah* (22) — aucun sous-titre disponible,
non transcriptibles ; leur contenu est de toute façon couvert par *Istikhlāf 7*.

## Étape 2 — La passe de normalisation (obligatoire)

C'est le point de vigilance numéro un. Les sous-titres automatiques massacrent l'arabe
translittéré. **Sans cette passe, le graphe se remplira de nœuds fantômes** et les ponts
avec le corpus `taqwa` ne se formeront pas.

Écris un dictionnaire de remplacement et applique-le à tous les transcripts avant ingestion.
Cas déjà relevés, à compléter en lisant les fichiers :

| Ce que produisent les sous-titres | Forme normalisée |
|---|---|
| hilafa · ilf · f | khilāfa |
| fêtra · fit | fiṭra |
| Ashour · our | Ibn ʿĀshūr |
| rum | ghumma |
| carb | karb |

Passe le dictionnaire en revue avec Zaki avant de lancer l'ingestion : une substitution trop
agressive (« f », « our ») peut casser du texte légitime. **Ancre-les sur le mot entier et
vérifie chaque remplacement sur un échantillon avant de traiter le lot.**

## Étape 3 — Ingérer

Ingère comme **un neuvième corpus, nommé `chauki`**, au même rang que `taqwa`. Respecte le
schéma de nœud existant : `label`, `file_type`, `source_file`, `source_location`,
`source_url`, `captured_at`, `author`, `contributor`, `corpus`, `norm`, `id`, `community`,
`norm_label`. Renseigne `source_url` avec l'URL YouTube de la vidéo — c'est ce qui rendra
chaque nœud vérifiable.

**Le gain attendu n'est pas le volume, ce sont les ponts.** Le corpus `taqwa`
(Taqwa Impact / Management prophétique, Médine Académie, modules MR1 à MR4) et celui de
Chauki Lazhar traitent les mêmes objets — l'âme, la modernité, la laïcité, les finalités,
le travail — par deux entrées différentes : la formation d'un côté, la recherche de l'autre.
Ce sont les liens entre les deux qui feront ressortir ce qu'on ne pensait pas à chercher.

## Étape 4 — Régénérer l'export d'équipe

```
cd ~/CTP-master-graph && python3 exporter_equipe.py           # rapport, n'écrit rien
cd ~/CTP-master-graph && python3 exporter_equipe.py --ecrire  # écrit
```

Le script exige `~/CTP-vimeo/members_roster.json` et **refuse de produire l'export si le
dépôt passe en public**. Les corpus `fiches` et `loom` sont écartés en bloc, et tout nœud
portant l'identité d'un membre est retiré en s'appuyant sur le registre Circle.
**Ajoute `chauki` à `CORPUS_GARDES` dans `exporter_equipe.py`** — sinon le nouveau corpus
sera filtré à l'export.

Puis publie dans `Collectif-Tariqa-PRO/ctp-base-connaissances`. Ce dépôt **reste privé** :
il contient les noms des membres, leurs blocages et des montants.

## Étape 5 — Vérifier avant de déclarer que c'est fait

1. Le nombre de nœuds `chauki` créés, et un échantillon de 20 libellés lus à l'œil :
   aucun ne doit être un fragment d'arabe mal transcrit.
2. Le nombre de **liens entre `chauki` et `taqwa`**. S'il est proche de zéro, la passe de
   normalisation a échoué — ne publie pas, reprends l'étape 2.
3. Trois requêtes de contrôle qui doivent retourner quelque chose de sensé :
   ```
   graphify query "on a inversé les idéaux et les moyens"
   graphify query "qu'est-ce qui détermine le cap d'un projet ?"
   graphify query "changer la forme d'un modèle sans changer sa direction"
   ```
4. Le total de nœuds et de liens avant / après, annoncé explicitement.

## Ensuite, si le temps le permet (second lot, facultatif)

Trois autres sources ont été analysées dans la même session et ne sont pas non plus dans le
graphe : **Sofiane Meziani** (Académie l'Olivier), **Nouman Ali Khan** (les émotions humaines
dans le Coran), et **Théo Le Lion** (source adverse, développement personnel mainstream).
Leurs comptes rendus sont sur la même branche : `source-sofiane-meziani.md`,
`notes-brutes-sofiane-meziani.md`, `inventaire-academie-olivier.md`,
`video-developpement-personnel.md`.

Propose à Zaki de les ingérer comme un corpus distinct — par exemple `paradigme` — pour
garder séparés la matière brute (`chauki`) et la couche déjà distillée. **Ne le fais pas
sans son accord.**

## Règles de la maison

- Ne publie rien de ce graphe à l'extérieur de l'équipe. Il contient de vraies identités.
- L'équipe `membres` de l'organisation ne doit jamais avoir accès à `ctp-base-connaissances`.
- Sur les références religieuses : l'attribution est obligatoire (Coran, le Prophète ﷺ,
  un compagnon, la sira), **le degré ne se mentionne jamais**.
- Les verbatims de Chauki Lazhar viennent de sous-titres automatiques : fiables sur le fond,
  approximatifs sur la lettre. Marque-les comme tels dans le graphe.
