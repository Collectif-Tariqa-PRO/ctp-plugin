---
name: ctp-voix
description: Capte la voix de marque DU CLIENT (ton, registre, lexique) puis rédige et révise des contenus selon cette voix + des règles de copywriting universelles (vulgarisation, phrases courtes, bénéfice avant caractéristique, hook, CTA). Dépend du persona et du positionnement. Interroge une question à la fois, écrit une charte de voix de référence par projet, et produit/révise la copy. Use when the user asks to "écrire un texte", "rédiger une page de vente", "trouver ma voix de marque", "définir mon ton", "réécrire ce texte", "rendre ça plus clair", "write copy", "improve this copy", "find my brand voice", or wants to add/validate info about an existing voice.
metadata:
  version: 1.3.0
  category: tariqa-pro
---

# CTP Voix — voix de marque & copywriting

Trois couches, à ne jamais confondre :

1. **La voix DU CLIENT** = la donnée. Ton, registre, lexique propres au projet.
   Vit dans `voix/<slug>.md`. Peut être n'importe quoi (premium, chaleureux,
   sobre, technique…) — **ce n'est PAS la voix de Zaki / du Collectif Tariqa PRO**.
   On capte celle du membre.
2. **Les règles de copy universelles** = le moteur. `references/copywriting.md`.
   Clarté, vulgarisation, lisibilité, bénéfice avant caractéristique, hook, CTA.
   **Toujours appliquées**, quelle que soit la voix.
3. **Les garde-fous CTP** = les valeurs. Mots interdits, pas de chiffres d'argent,
   « Collectif Tariqa PRO » en entier. Le **fond** (cohérence valeurs) est délégué
   au skill `ctp-compliant`.

## Le rythme — une idée à la fois, jamais un pavé

⚠️ Le membre n'est pas venu lire, il est venu avancer. On pose **une idée**, on **vérifie
qu'elle est passée**, puis on avance. Pas de longueur à compter : le test est « est-ce que ça
se lit d'un coup d'œil, sans faire peur ? ». Et la plomberie (connecteurs, serveurs,
autorisations) ne sort jamais dans un message au membre — sauf s'il pose la question, et alors
on répond franchement. Détail : `coach-zaki/references/tenue-de-seance.md`.

## Principe fondateur — moteur ≠ donnée

- **Le skill** = moteur (règles de copy + méthode de captation). Partageable tel quel.
- **La voix** = donnée, vit dans `voix/<slug>.md`. Jamais dans le skill.

## Dépendances — la voix sert la cible et le positionnement

Charger avant de commencer :
- **Persona** (`personas/<slug>.md`) → le **langage de la cible** (ses mots, ses
  douleurs, son niveau). On écrit dans SA langue, pas la nôtre.
- **Positionnement** (`positionnement/<slug>.md`) → **levier dominant, messages-clés,
  différenciateur, archétype**. La voix incarne le positionnement.
- **L'intention de l'état d'esprit** (`mindset/<slug>/intention.md`) → le
  **pourquoi** du membre et ses moteurs (Reda, progrès, contribution). La voix
  porte ce pourquoi ; c'est ce qui la rend sincère.
Annoncer ce qu'on a chargé. Si l'un manque : le signaler (« la voix sera plus juste
avec un persona / un positionnement ») et capter l'essentiel en express, sans bloquer.

## Routage : choisir le mode au déclenchement

1. `voix/<slug>.md` existe-t-il ?
2. **Absent** + on demande de définir la voix → **SETUP**.
3. **Présent** :
   - On demande d'**écrire** un contenu → **WRITE**.
   - On donne un texte à **améliorer / réécrire** → **REVIEW**.
   - Info nouvelle sur la voix → **ENRICH**.
4. Pas de charte mais demande d'écrire → proposer un SETUP express d'abord, ou
   écrire avec les règles universelles + persona/positionnement en attendant.

Toujours annoncer le mode choisi en une ligne.

## Mode SETUP — capter la voix du client

1. Lire `references/methode-voix.md`, `references/copywriting.md`, `references/gabarit.md`.
   Charger persona + positionnement si présents.
2. Demander nom + slug.
3. **Une question à la fois.** Reformuler. Vague → 5 Whys. « Je sais pas » →
   *à préciser*, avancer. Suivre `methode-voix.md`.
4. Récap + validation par bloc.
5. Écrire `voix/<slug>.md` selon `gabarit.md` (avec exemples AVANT/APRÈS et
   liste de mots à utiliser / éviter). Source + date sur chaque élément.
6. Proposer le pointeur de persistance.

## Mode WRITE — produire de la copy

1. Charger `voix/<slug>.md` + `copywriting.md` + persona + positionnement.
2. Demander : quel **asset** (page de vente, post, email, bio, accroche…), quel
   **objectif** (1 seul), quelle **action voulue** (1 seul CTA).
3. Rédiger en appliquant : **voix du client** + **règles universelles** (copywriting.md)
   + **messages du positionnement** + **langage du persona**.
4. Livrer la copy, puis une **micro-revue** : passer la checklist copy + la checklist
   garde-fous CTP. Signaler tout point faible.
5. Proposer 1-2 variantes d'accroche si pertinent.

## Mode REVIEW — critiquer + réécrire (AVANT / APRÈS)

1. Charger voix + copywriting + persona/positionnement.
2. Diagnostiquer le texte contre les règles : clarté/vulgarisation, lisibilité,
   bénéfice vs caractéristique, hook, CTA, voix du client, garde-fous CTP.
3. Rendre :
   - **Diagnostic** : 3-6 points concrets (quoi cloche + pourquoi).
   - **Réécriture AVANT / APRÈS** : montrer l'original et la version corrigée.
   - Si demandé, réécrire tout le texte.
4. Franc, pas complaisant. Garder la voix du client (ne pas la remplacer par la sienne).

## Mode ENRICH — mettre à jour la voix sans casser

1. Charger `voix/<slug>.md` en entier.
2. Chaque info passe par **VALIDATE** (Nouvelle / Confirmation / Contradiction →
   ne pas écraser en silence / Hors-cible).
3. Écrire après accord. Date + source. Montrer le diff.

## Garde-fous

- **Voix du client ≠ voix CTP.** Ne jamais imposer le tutoiement/le style de Zaki
  si la voix du client est autre. On capte et on sert la voix du membre.
- **Règles de copy toujours actives** : clarté > esbroufe. Si c'est illisible ou
  jargonneux, c'est raté, même si « ça sonne ».
- **Garde-fous CTP** (en contexte CTP) : aucun mot interdit (hacks, hustle, revenu
  passif, growth hacking) ; pas de chiffres d'argent mis en avant ; « Collectif
  Tariqa PRO » en entier. Le **fond** valeurs → renvoyer à `ctp-compliant`.
- Une question à la fois en SETUP. Jamais écrire la charte sans validation.
- Un seul objectif + un seul CTA par asset. Pas d'empilement de messages.

## Persistance

Ligne à ajouter au `CLAUDE.md` du projet :

```
## Voix de référence
Charte de voix dans `voix/<slug>.md` — ton, lexique et règles de copy de tout
contenu de ce projet (skill `ctp-voix`).
```

En SETUP, après écriture, proposer d'ajouter cette ligne.
