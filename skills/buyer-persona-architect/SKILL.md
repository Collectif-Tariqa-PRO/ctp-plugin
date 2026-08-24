---
name: buyer-persona-architect
description: Étape 1 du parcours Collectif Tariqa PRO — interroge le membre pour construire, puis enrichir au fil du temps, un document persona / ICP de référence par projet. Use when the user asks to "create a persona", "build an ICP", "define target audience", "analyze customer motivations", "construire un persona", "définir ma cible", "l'étape persona du parcours CTP", or wants to add/validate new information about an existing persona.
metadata:
  version: 1.3.0
  category: tariqa-pro
---

# Buyer Persona Architect

Moteur d'interview + document vivant. Le skill ne « réfléchit » pas dans le vide :
il **pose des questions**, **produit un fichier persona**, puis **l'enrichit et le
valide** à chaque nouvelle information.

Méthodologie : `references/methode.md` (questions précises + 5 Rings of Buying
Insights de Revella). Structure du livrable : `references/gabarit.md`.

## Le rythme — une idée à la fois, jamais un pavé

⚠️ Le membre n'est pas venu lire, il est venu avancer. On pose **une idée**, on **vérifie
qu'elle est passée**, puis on avance. Pas de longueur à compter : le test est « est-ce que ça
se lit d'un coup d'œil, sans faire peur ? ». Et la plomberie (connecteurs, serveurs,
autorisations) ne sort jamais dans un message au membre — sauf s'il pose la question, et alors
on répond franchement. Détail : `coach-zaki/references/tenue-de-seance.md`.

## Principe fondateur — moteur ≠ donnée

- **Le skill** = le moteur (cette méthode). Partageable tel quel.
- **Le persona** = la donnée, vit dans le projet sous `personas/<slug>.md`.
  Jamais stocké dans le skill — sinon le partager refilerait le persona d'autrui.

Chaque projet a son ou ses fichiers persona. Un projet peut en avoir plusieurs
(`personas/acheteur-b2b.md`, `personas/dirigeant-pme.md`).

## Routage : choisir le mode au déclenchement

1. Regarder si `personas/` existe dans le projet courant et contient des fichiers.
2. **Aucun fichier** → mode **CREATE**.
3. **Fichier(s) présent(s)** :
   - L'utilisateur apporte une info nouvelle / un apprentissage → mode **ENRICH**.
   - L'utilisateur demande un nouveau persona distinct → mode **CREATE** (nouveau slug).
   - Doute sur lequel viser → demander quel persona avant d'agir.

Toujours annoncer le mode choisi en une ligne avant de commencer.

## Mode CREATE — interview qui produit le document

1. Lire `references/methode.md` et `references/gabarit.md`. **Si
   `mindset/<slug>/bilan.md` existe**, le charger : pour un membre qui cherchait
   encore quoi faire, les **directions** qui en sont sorties (croisement
   savoir-faire × ce qui l'anime × un problème réel) sont le point de départ du
   persona — on part de là, on ne redemande pas.
2. Demander d'abord : nom court du persona + slug fichier (ex. `dirigeant-pme`).
3. **Mener l'interview une question à la fois.** Jamais de bloc de 10 questions.
   - Poser 1 question → attendre la réponse → reformuler ce qu'on a compris →
     question suivante.
   - Si une réponse est vague, creuser avec « 5 Whys » avant d'avancer.
   - Suivre l'ordre des sections de `methode.md`.
4. À la fin de chaque grande section, montrer un récap et faire valider.
5. Écrire `personas/<slug>.md` selon `gabarit.md`. Chaque fait porte sa **source**
   (interview / observation / donnée / hypothèse) et sa **date**.
6. Proposer d'ajouter le pointeur de référence (voir « Persistance » plus bas).
7. Optionnel : export HTML lisible pour présenter à un humain — mais la **source
   vivante reste le markdown**.

## Mode ENRICH — ajouter sans casser

1. Charger le fichier persona ciblé en entier.
2. Pour chaque information nouvelle, **passer par VALIDATE** (ci-dessous).
3. N'écrire qu'après accord. Ajouter dans la bonne section, daté + source.
4. Mettre à jour la ligne « Dernière mise à jour » en tête de document.
5. Montrer le diff de ce qui a changé.

## Mode VALIDATE — règle de cohérence (toujours avant écriture)

Pour toute info entrante, classer et annoncer :

- **Nouvelle** — absente du doc → proposer où l'ajouter.
- **Confirmation** — déjà présente, renforcée → noter comme corroborée.
- **Contradiction** — entre en conflit avec un fait existant → **ne pas écraser
  en silence**. Montrer les deux versions, demander laquelle garder, archiver
  l'ancienne en note datée.
- **Hors-cible** — ne concerne pas ce persona → le signaler, ne pas l'ajouter.

Ne jamais écrire dans le fichier sans avoir montré à l'utilisateur quoi et où,
et obtenu un « ok ».

## Persistance — pour que le persona revienne à chaque session

Le rappel automatique ne vient PAS de ce skill ni de la mémoire globale. Il vient
d'une ligne dans le `CLAUDE.md` du projet, du type :

```
## Persona de référence
Cible décrite dans `personas/<slug>.md` — toujours la respecter pour tout
contenu, copie, design et décision marketing de ce projet.
```

En mode CREATE, après avoir écrit le persona, proposer d'ajouter cette ligne si
elle n'existe pas.

## Voix

Si le projet est CTP (Collectif Tariqa PRO), produire le persona en français,
voix CTP (tutoiement, phrases courtes), et respecter les mots interdits du
CLAUDE.md global. Pas de chiffres d'argent (CA, montants) mis en avant.

## Garde-fous

- Une question à la fois. Pas de mur de questions.
- Jamais écrire sans validation.
- Persona trop large → forcer ≥3 traits spécifiques + le segment où l'offre est
  nettement meilleure que l'alternative.
- Distinguer fait observé vs hypothèse. Une hypothèse non validée est étiquetée
  comme telle.
