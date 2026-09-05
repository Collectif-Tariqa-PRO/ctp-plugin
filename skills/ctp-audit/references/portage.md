# Faire vivre l'audit ailleurs — Claude, ChatGPT, le site

L'audit n'a de valeur que s'il est **le même partout**. Un diagnostic qui change de conclusion
selon l'outil n'est pas un diagnostic.

## La règle de la source unique

> **Ce dossier est la source. Tout le reste est un export.**

On ne modifie jamais les questions, la grille ou les renvois « juste pour la version site ».
On modifie ici, puis on ré-exporte. Chaque export porte la **version du skill** (`metadata.version`
dans `SKILL.md`) pour qu'on sache, en regardant une conversation, sur quelle version elle tournait.

### Les invariants — identiques sur toutes les surfaces

Ce qui change fait de l'audit un autre produit. Ce qui suit ne change jamais :

1. **Les dix questions**, dans l'ordre, ouvertes, une par message.
2. **Les quatre états** de pilier, et l'interdiction d'un état sans preuve citée.
3. **Un seul frein n°1**, et les piliers hors stade marqués « pas encore ton sujet ».
4. **Aucun score chiffré**, jamais.
5. **Les trois portes et leurs conditions** — en particulier : rien sur le rendez-vous avant
   que le portrait et l'ordonnance soient rendus.
6. **Le livrable est rendu, entier, gratuitement**, même si la personne ne donne rien en
   retour.

### Ce qui a le droit de différer

| | Fichiers écrits | Durée d'une session | Capture de coordonnées |
|---|---|---|---|
| **Claude Code / Cowork** | oui (`audit/`) | longue, reprise possible | aucune |
| **Claude.ai (Projet)** | non (blocs à copier + artefact) | longue | aucune |
| **ChatGPT (GPT perso)** | non (canvas + copier-coller) | moyenne, mémoire fragile | aucune |
| **Site web (le hub)** | côté serveur | courte, reprise par lien | oui, au temps 2 |

---

## Surface 1 — Claude Code et Cowork *(la référence)*

C'est le cas natif : le plugin est installé, `ctp-audit` se déclenche, les fichiers s'écrivent
dans `audit/`. Rien à faire de plus.

**Point d'attention navigateur / tablette :** le dossier de travail est temporaire. On prévient
**une fois** au temps 0, et on rend les fichiers à la fin. C'est une promesse, pas une formalité.

---

## Surface 2 — Claude.ai, en Projet

Le chemin le plus court pour ouvrir l'audit à quelqu'un qui n'installe rien.

1. Créer un **Projet** nommé « Audit de l'entrepreneur musulman ».
2. Dans les **instructions du projet** : coller le noyau compilé (§ *La compilation*).
3. Dans la **base de connaissances** du projet : déposer `questions.md`, `cartographie.md`,
   `renvois-youtube.md`, `passerelle.md`, `gabarit-rapport.md`.
4. Adapter deux points dans le noyau : pas d'écriture de fichiers → le livrable devient
   **un bloc à copier-coller** plus, si possible, la carte en **artefact HTML** à partir de
   `carte-audit-modele.html`.

**Limite connue :** pas de reprise fiable d'une conversation à l'autre. Si l'audit est coupé,
la personne doit recoller son bloc de notes au redémarrage. Le prévoir dans le noyau : à
chaque fin de temps, proposer le bloc de reprise.

---

## Surface 3 — ChatGPT, en GPT personnalisé

Faisable, avec deux contraintes structurelles à connaître avant de commencer.

**Contrainte 1 — le champ *Instructions* est court** (de l'ordre de 8 000 caractères). Le
`SKILL.md` seul en fait le double. Donc : **le noyau va dans les Instructions, le reste va
dans les fichiers de connaissance.**

**Contrainte 2 — la lecture des fichiers de connaissance n'est pas garantie** à chaque tour.
Tout ce qui est **non négociable** doit donc vivre **dans les Instructions**, pas dans un
fichier : les dix questions en une ligne chacune, les quatre états, la règle du frein unique,
les interdits, et les trois portes avec leurs conditions. Les fichiers portent le détail —
relances, preuves, table de renvois — pas les garde-fous.

**Le montage :**

1. **Instructions** ← le noyau compilé (§ ci-dessous).
2. **Knowledge** ← `questions.md`, `cartographie.md`, `renvois-youtube.md`, `passerelle.md`,
   `carte-audit-modele.html`.
3. **Capacités** : navigation web **désactivée** — l'audit ne doit rien chercher dehors, et
   surtout pas d'autres vidéos que les nôtres. Génération d'images inutile.
4. **Actions** : aucune. Pas d'appel vers un CRM depuis le GPT.
5. **Conversation starters** : « Fais-moi l'audit », « Je tourne en rond, aide-moi à
   comprendre pourquoi », « Je sais pas par où commencer », « J'ai une expertise mais je
   n'ose pas me lancer ».
6. **Visibilité** : lien seulement, au début. Une publication dans le magasin de GPT expose le
   contenu à la copie — c'est un arbitrage à faire en connaissance de cause.

⚠️ **Ce qui se perd sur ChatGPT :** l'écriture de fichiers, et une partie de la tenue de
séance (le modèle a tendance à dérouler des blocs longs). Renforcer la règle du rythme dans
les Instructions : *une question par message, on attend la réponse, jamais deux questions à la
fois*.

---

## Surface 4 — Le site : capter un lead sans trahir l'audit

C'est la surface la plus délicate, parce que c'est la seule où on **demande quelque chose** à
la personne. Trois architectures possibles, et une recommandation.

| | Ce que c'est | Verdict |
|---|---|---|
| **A. Le formulaire** | 10 questions en champs libres, un rapport généré à la fin | ❌ On perd les relances, donc le diagnostic. C'est un questionnaire, pas un audit. |
| **B. Le lien vers le GPT** | Une page qui renvoie vers ChatGPT ou Claude | ⚠️ Zéro friction à construire, mais **aucun lead capté** et aucune trace. Bon comme v0, pas comme destination. |
| **C. Le chat intégré** | Une conversation sur le site, servie par une API de modèle, avec le même noyau | ✅ **La recommandation.** Seule option qui garde les relances *et* permet la capture. |

### L'architecture C — le déroulé

```
   Page d'entrée
   « Deux heures pour savoir sur quoi tu dois vraiment travailler. »
   → un bouton. Pas de formulaire ici.
        │
   Temps 0-1   le chat pose les dix questions   ← AUCUNE capture
        │
   Temps 2     restitution de mi-parcours + une vidéo
        │
        ├─► LA CAPTURE, ici et nulle part ailleurs
        │   « Je te garde ta carte — donne-moi ton prénom et ton mail
        │     pour la retrouver si tu fermes la page. »
        │   → prénom + email → le hub
        │   → et un lien de reprise, qui marche même sans email
        │
   Temps 3-4   portrait + ordonnance + renvois  ← rendus EN ENTIER,
        │                                          email donné ou non
   Temps 5     la carte HTML : à l'écran, téléchargeable, envoyée si mail
        │
        └─► Porte 3 (WhatsApp) — seulement aux conditions de passerelle.md
```

**Les quatre règles de la version site** — ce sont elles qui font la différence entre un
audit et un aspirateur à emails :

1. **Aucune capture avant le temps 2.** Une personne qui n'a rien reçu ne doit rien donner.
2. **Le résultat n'est jamais l'appât.** Si elle refuse de donner son mail, elle reçoit
   **exactement le même portrait**, à l'écran, téléchargeable. Le mail sert à *retrouver* sa
   carte, pas à *l'obtenir*.
3. **Le lien de reprise fonctionne sans email.** Une URL avec un identifiant opaque, valable
   quelques semaines. Beaucoup couperont en cours de route ; ils doivent pouvoir revenir.
4. **Pas de relance automatique déguisée en conseil.** Une relance honnête rappelle
   l'action de 48 h — elle ne fabrique pas une urgence.

### Ce qu'on stocke, et ce qu'on n'envoie nulle part

Le contenu d'un audit est intime : la foi, le couple, la santé, l'argent, les peurs.

- **Dans le hub, on pousse le minimum utile à un suivi humain :** prénom, email, source
  d'arrivée, **stade**, **frein n°1** (une phrase), **date**. Rien d'autre.
- **Le transcript complet reste côté audit**, et n'entre pas dans l'outil marketing.
- **Jamais de verbatim brut dans un CRM**, jamais dans une automatisation d'emails, jamais
  dans un tableau partagé.
- Consentement explicite au moment de la capture, dans une phrase que quelqu'un comprend :
  ce qu'on garde, pourquoi, et comment on l'efface.
- Le numéro WhatsApp est **affiché**, pas pré-rempli avec ses données. C'est elle qui écrit.

### Ce qu'on mesure — et le piège

Utile : nombre d'audits démarrés, taux d'arrivée au temps 2, taux d'arrivée au portrait,
répartition des stades, répartition des freins n°1, part qui ouvre la porte 3.

⚠️ **Le piège :** dès qu'on optimise le taux de passage à WhatsApp, on est tenté de l'ouvrir
plus tôt et plus souvent — et l'audit devient un tunnel de vente. Le bon indicateur de santé
n'est pas le taux de rendez-vous : c'est **la part de gens qui vont au bout du portrait**.
Si celle-là monte, le reste suit. Si elle baisse, on a cassé quelque chose.

**La répartition des freins n°1 est le vrai trésor de ce dispositif** : c'est la carte de ce
qui bloque réellement les entrepreneurs musulmans francophones, mise à jour en continu. Elle
alimente les sujets YouTube, les cours, et les trous de contenu de `renvois-youtube.md`.

---

## La compilation — produire le noyau exporté

Le « noyau » est la version condensée qui tient dans un champ d'instructions. Il se fabrique
à partir de ce dossier, dans cet ordre, sans rien inventer :

1. **Le cadre** — qui parle (Coach Zaki), pour qui, la durée, le contrat d'honnêteté.
2. **Le rythme** — une idée par message, on attend la réponse, 80/20 de parole. *(à répéter :
   c'est la règle que les modèles lâchent en premier)*
3. **Les cinq temps**, en cinq lignes.
4. **Les dix questions**, une ligne chacune, dans l'ordre, telles quelles.
5. **Les quatre états + les cinq stades + les trois moteurs**, en une table compacte.
6. **La règle du frein unique**, en entier.
7. **Les interdits**, en entier — c'est la partie qu'on ne coupe jamais.
8. **Les trois portes et leurs conditions**, en entier.
9. **Le format du livrable** — le bloc à copier-coller.
10. **La consigne de repli** : « pour le détail des relances, de la grille et des renvois,
    consulter les fichiers joints ; en leur absence, appliquer strictement ce qui précède. »

**Ce qui ne descend jamais dans un noyau exporté :** aucune donnée de membre, aucun lien
interne (Circle, dépôts, outils du Collectif), aucune mention de la provenance des principes.

**À chaque évolution du skill :** incrémenter `metadata.version`, ré-exporter les noyaux, et
noter la version dans le `CHANGELOG.md`. Un GPT qui tourne sur une version d'il y a six mois
donnera un autre diagnostic que le parcours — et c'est exactement ce qu'on veut éviter.
