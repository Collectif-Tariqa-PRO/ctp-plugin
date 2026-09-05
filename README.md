# Collectif Tariqa PRO — skills méthode

Plugin officiel pour les membres du **Collectif Tariqa PRO**. Il installe une
suite de skills qui te guident, dans le bon ordre, pour poser les fondations de
ton projet — puis vérifier qu'il est cohérent avec la méthode et les valeurs du
Collectif.

> *Entreprendre. Ensemble. Vers Dieu.*

## Ce que tu obtiens

| Skill | Ce qu'il fait |
|---|---|
| **ctp-audit** | 🩺 **L'audit de l'entrepreneur musulman** — le diagnostic, ouvert à tous. Dix questions ouvertes, un portrait, un frein n°1, et les vidéos publiques avec le passage exact. |
| **ctp-parcours** | 🧭 La porte d'entrée. Te dit où tu en es et lance la bonne étape. |
| **buyer-persona-architect** | 1. À qui tu t'adresses (persona / cible). |
| **ctp-offre** | 2. Ton offre (méthode des 3 P, architecture, pricing). |
| **ctp-branding-positionnement** | 3. Ta marque : branding (identité, associations, histoire) + positionnement + différenciateur. MVB : suffisant pour démarrer. |
| **ctp-brandkit** | 🎨 Génère tes planches visuelles + concepts logo à partir de ton kit de marque (inclus, aucune install séparée). |
| **ctp-voix** | 4. Ta voix de marque + rédaction (copywriting). |
| **ctp-page-de-vente** | 5. Ta landing page v1 **mise en ligne** (entrepreneurs hors e-commerce) : CTA qualifié, tes vraies images, déploiement Vercel. |
| **ctp-taste** | 🧩 Moteur de design anti-slop (inclus), utilisé par la page de vente. |
| **ctp-compliant** | ✓ Audit : « est-ce Tariqa PRO compliant ? » |
| **ctp-export** | 📤 Compile ton travail en un livrable vérifiable. |

Chaque skill **t'interroge** une question à la fois, écrit un **document de
référence** dans ton projet, et **s'enrichit** au fil du temps (il n'écrase jamais
un choix en silence).

## Installation

Dans Claude Code **ou** Cowork :

```
/plugin marketplace add tariqa-pro/ctp-plugin
/plugin install collectif-tariqa-pro@ctp
```

*(Remplace `tariqa-pro/ctp-plugin` par l'URL réelle du dépôt git du Collectif.)*

Mise à jour quand une nouvelle version sort :

```
/plugin marketplace update ctp
/plugin install collectif-tariqa-pro@ctp
```

## Par où commencer

**Tu ne sais pas encore ce qui te bloque ?** Commence par l'audit :

```
fais-moi l'audit
```

Deux heures, une dizaine de questions ouvertes, et tu ressors avec ta carte : où tu en es,
ton frein numéro un, tes trois chantiers dans l'ordre, et les passages précis de nos vidéos
publiques qui traitent ton sujet. L'audit est **ouvert à tous** — membre ou pas.

**Tu sais déjà, et tu veux construire ?** Tape simplement :

```
lance le parcours CTP
```

Le skill `ctp-parcours` scanne ton projet, t'affiche ta progression, et te lance
la bonne étape. Tu n'as rien à mémoriser.

## Ce que ça crée dans ton projet

```
personas/<projet>.md          ← ta cible
offres/<projet>.md            ← ton offre
positionnement/<projet>.md    ← ton positionnement + différenciateur
voix/<projet>.md              ← ta charte de voix
ctp/tariqa-compliance.md      ← ton profil d'alignement
audit/<prenom>-<date>.md      ← ta carte d'audit (si tu as fait l'audit)
ctp/EXPORT-<projet>-<date>.md ← le livrable à envoyer
```

Quand tu as fini, lance `export CTP` : tu obtiens un seul fichier texte (avec un
scorecard de complétion) à envoyer à ton accompagnateur.

## Règles de la maison

- Pas de chiffres d'argent mis en avant.
- Mots bannis : *hacks, hustle, revenu passif, growth hacking*.
- Toujours « Collectif Tariqa PRO » en entier.
- La voix captée est **la tienne** — le plugin ne t'impose pas un style.

---
© Collectif Tariqa PRO
