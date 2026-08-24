---
name: ctp-export
description: Compile TOUT le pilier 1 (Mindset) — les deux moitiés : l'état d'esprit (bilan, ancrage, intention, posture, environnement, agenda, commencement + le carnet des remèdes personnalisé) ET Mon projet (persona, offre, marque, voix, page de vente, compliance) — en un livrable vérifiable avec scorecard, GÉNÈRE un pitch puissant (méthode SIRA, < 3 min), et maintient un document de référence vivant. Use when the user asks "exporter mon travail CTP", "générer le livrable", "compiler mes docs", "export CTP", "export complet du parcours", "préparer pour envoi", "rapport de mon projet", "génère mon pitch", "crée mon pitch", "mon elevator pitch", "mon carnet de remèdes", or wants a single shareable deliverable of all CTP work.
metadata:
  version: 1.3.0
  category: tariqa-pro
---

# CTP Export — livrable unique vérifiable

Compile les documents de référence CTP d'un projet en **un seul texte** que le
membre peut envoyer (WhatsApp, email, Drive) et que l'animateur peut **vérifier**
d'un coup d'œil : qui a vraiment fait le travail, et où ça reste à compléter.

## Le rythme — une idée à la fois, jamais un pavé

⚠️ Le membre n'est pas venu lire, il est venu avancer. On pose **une idée**, on **vérifie
qu'elle est passée**, puis on avance. Pas de longueur à compter : le test est « est-ce que ça
se lit d'un coup d'œil, sans faire peur ? ». Et la plomberie (connecteurs, serveurs,
autorisations) ne sort jamais dans un message au membre — sauf s'il pose la question, et alors
on répond franchement. Détail : `coach-zaki/references/tenue-de-seance.md`.

## Sources compilées — TOUT le pilier 1, les deux moitiés

L'export imbrique **l'état d'esprit ET Mon projet**, dans l'ordre du parcours.

**Partie 1 — L'état d'esprit** (skill `ctp-mindset`)
| Module | Fichier |
|---|---|
| Le bilan | `mindset/<slug>/bilan.md` |
| L'ancrage | `mindset/<slug>/ancrage.md` |
| Toi ↔ Dieu (intention) | `mindset/<slug>/intention.md` |
| Toi ↔ toi-même (posture) | `mindset/<slug>/posture.md` |
| Toi ↔ ton environnement | `mindset/<slug>/environnement.md` |
| Le rituel & l'agenda | `mindset/<slug>/agenda.md` |
| Le commencement | `mindset/<slug>/commencement.md` |
| **Le carnet des remèdes** (personnalisé sur les blocages du membre) | `mindset/<slug>/carnet-remedes.html` |

**Partie 2 — Mon projet**
| Étape | Fichier |
|---|---|
| Persona | `personas/<slug>.md` |
| Offre | `offres/<slug>.md` |
| Marque (branding + positionnement + différenciateur) | `positionnement/<slug>.md` |
| Voix | `voix/<slug>.md` |
| Page de vente | `landing/` + URL |
| Compliance | `ctp/tariqa-compliance.md` |

Le **carnet des remèdes** se génère depuis `ctp-mindset/references/remedes-spirituels.md`
(la pharmacopée, rangée par blocage) et le gabarit
`ctp-mindset/references/carte-remedes-modele.html`, **filtré sur les blocages
diagnostiqués du membre** (lus dans `posture.md`, `ancrage.md`, `ETAT.md`) —
rangé par problème, trois versions par remède (arabe / phonétique / français).

## Deux entrées

- **Export complet** (« export CTP », « génère le livrable ») → toute la procédure ci-dessous.
- **Pitch seul** (« génère mon pitch », « crée mon pitch », « mon elevator pitch ») → **ne pas
  forcer l'export complet**. Lire ce qui existe déjà (`ctp/REFERENCE-<slug>.md` en priorité, sinon
  les docs présents), générer le pitch via `references/pitch.md` à partir de ce qu'on a, et
  **signaler les briques manquantes** (« pitch partiel : offre pas encore définie → la résolution
  reste floue ; on fait l'offre pour un pitch complet ? »). Sortir le pitch dans un bloc de code.
  Ne pas écrire de fichier d'export, ne pas recalculer tout le scorecard.

## Procédure (export complet)

1. **Identifier le projet** : si plusieurs slugs, demander lequel exporter.
2. **Récupérer la date du jour** (`date +%F`) et lister les fichiers présents.
3. **Calculer le scorecard de complétion** pour chaque doc :
   - **absent** ⬜ · **commencé** 🟡 (contient des `⏳`/sections vides) ·
     **complet** ✅.
   - compter les marqueurs `⏳ à préciser` / champs `<…>` non remplis.
4. **Assembler le fichier** `ctp/EXPORT-<slug>-<AAAA-MM-JJ>.md` selon le gabarit
   ci-dessous : en-tête + scorecard + liste des points ⏳ ouverts + contenu intégral
   de chaque doc.
5. **Produire aussi un bloc copier-coller court** (résumé + scorecard) à coller
   directement dans un message — dans un bloc de code.
6. **Générer le PITCH (méthode SIRA)** à partir de persona/offre/positionnement/voix —
   suivre `references/pitch.md`. L'inclure dans l'export ET dans le doc de référence.
   Si une brique manque (ex. offre non définie), faire un pitch partiel + le signaler.
6bis. **Générer le carnet des remèdes** — filtrer
   `ctp-mindset/references/remedes-spirituels.md` (la pharmacopée, par blocage) sur
   les **blocages diagnostiqués du membre** (`posture.md`, `ancrage.md`, `ETAT.md`),
   et produire `mindset/<slug>/carnet-remedes.html` depuis le gabarit
   `ctp-mindset/references/carte-remedes-modele.html` — **rangé par problème**, trois
   versions par remède. Ne garder que les problèmes du membre, pas toute la pharmacopée.
7. **Mettre à jour le document de référence vivant** `ctp/REFERENCE-<slug>.md`
   (voir section dédiée) — c'est le doc consolidé à consulter pour toute la suite.
8. Proposer un **export HTML** lisible si demandé (un seul fichier autonome), et un
   **PDF** si le membre veut l'envoyer/imprimer (générer via l'outil PDF, ou « Imprimer
   → Enregistrer en PDF » depuis le HTML).
9. **Inviter à publier dans le Collectif Tariqa PRO** (voir section dédiée).
10. **Garde-fous CTP avant export** : vérifier qu'aucun chiffre d'argent ni mot
   interdit ne traîne dans les docs ; si oui, le signaler (ne pas bloquer l'export,
   mais avertir). Recommander un dernier `ctp-compliant` si pas fait.

## Gabarit du fichier d'export

```markdown
# Livrable Pilier 1 (Mindset) — <Nom du projet>
> Membre : <nom> · Date : <AAAA-MM-JJ> · Généré par skill `ctp-export`

## Scorecard de complétion — le pilier complet
**Partie 1 — L'état d'esprit**
| Module | Statut | Points ouverts |
|---|---|---|
| 0. Bilan | ✅ / 🟡 / ⬜ | <n ⏳> |
| 1. Ancrage | … | … |
| 2. Toi ↔ Dieu | … | … |
| 3. Toi ↔ toi-même | … | … |
| 4. Environnement | … | … |
| 5. Agenda | … | … |
| 6. Commencement | … | … |

**Partie 2 — Mon projet**
| Étape | Statut | Points ouverts |
|---|---|---|
| 1. Persona | ✅ / 🟡 / ⬜ | <n ⏳> |
| 2. Offre | … | … |
| 3. Marque | … | … |
| 4. Voix | … | … |
| 5. Page de vente | <URL ou ⬜> | … |
| ✓ Compliance | … | dernier verdict : <✅/⚠️/❌ + date> |

**Avancement global : <X>/8 modules d'état d'esprit · <Y>/4 étapes Mon projet.**

## Points encore à préciser (⏳)
- [module/étape] <…>

---
# PARTIE 1 — L'état d'esprit

## 0. Le bilan
<contenu intégral de mindset/<slug>/bilan.md>
## 1. L'ancrage
<contenu intégral de mindset/<slug>/ancrage.md>
## 2. Toi ↔ Dieu — l'intention
<contenu intégral de mindset/<slug>/intention.md>
## 3. Toi ↔ toi-même — la posture
<contenu intégral de mindset/<slug>/posture.md>
## 4. Toi ↔ ton environnement
<contenu intégral de mindset/<slug>/environnement.md>
## 5. Le rituel & l'agenda
<contenu intégral de mindset/<slug>/agenda.md>
## 6. Le commencement
<contenu intégral de mindset/<slug>/commencement.md>

## ✦ Le carnet des remèdes
<le carnet personnalisé — rangé par les blocages diagnostiqués du membre ;
chaque remède en 3 versions (arabe / phonétique / français) ; lien vers le HTML imprimable>

---
# PARTIE 2 — Mon projet

## 1. Persona
<contenu intégral de personas/<slug>.md>
## 2. Offre
<contenu intégral de offres/<slug>.md>
## 3. Marque (branding + positionnement)
<contenu intégral de positionnement/<slug>.md>
## 4. Voix
<contenu intégral de voix/<slug>.md>
## ✓ Compliance
<contenu intégral de ctp/tariqa-compliance.md>

---
## ★ Pitch (méthode SIRA)
<pitch court ~30 s> · <pitch complet < 3 min : hook + Situation + Impact + Résolution + Appel à l'action>
<3-5 punchlines marketing réutilisables> — généré selon references/pitch.md, dans la voix du membre.
```

## Bloc copier-coller (pour envoi rapide)

À sortir dans un bloc de code, court :

```
LIVRABLE PILIER 1 (MINDSET) — <projet> — <date>
État d'esprit : <X>/8 modules · Mon projet : <Y>/4 étapes
Bilan ✅ · Ancrage ✅ · Toi↔Dieu ✅ · Toi↔toi 🟡 · Env ⬜ · Agenda ⬜ · Commencement ⬜
Persona ⬜ · Offre ⬜ · Marque ⬜ · Voix ⬜ · Compliance ⬜
Page de vente en ligne : <URL ou ⬜ pas encore>
Points ouverts : <n>
Fichier complet : ctp/EXPORT-<slug>-<date>.md
```

> Si une landing page existe (`landing/` + URL, étape 5), l'inclure ici : c'est une
> brique de l'output final (pitch + docs `.md` + page en ligne).

## Le document de référence vivant — `ctp/REFERENCE-<slug>.md`

En plus des exports datés (photos figées), maintenir **un seul** document vivant qui
représente l'**état courant consolidé** du projet : `ctp/REFERENCE-<slug>.md`.

- **Écrasé à chaque export** (≠ les `EXPORT-<slug>-<date>.md` qui s'accumulent comme
  historique). C'est la **source consolidée à jour**.
- **À consulter pour toute la suite du projet.** C'est le mémo central : avant de
  coacher, d'écrire un contenu, de prendre une décision, on relit cette référence pour
  rester cohérent avec la cible, l'offre, le positionnement et la voix déjà définis.
  Les autres skills (parcours, voix, coach-zaki…) doivent le lire en priorité s'il existe.
- Même structure que le gabarit d'export (en-tête + scorecard + contenu intégral), mais
  daté « dernière mise à jour : <AAAA-MM-JJ> ».

## Publier dans le Collectif Tariqa PRO (Circle)

L'export n'a de valeur que s'il est **partagé** : l'animateur (Zaki) le voit, le membre
s'engage devant le collectif, et chacun publie son avancement au fur et à mesure.

- Après l'export, **inviter le membre à le publier dans l'espace dédié** du Collectif
  Tariqa PRO sur Circle. Le lien est centralisé dans `references/collectif.md` (le lire) :
  **SIRAT — LE FAMEUX PARCOURS** → https://collectif-tariqa-pro.circle.so/c/sirat-le-fameux-parcours
- Format au choix du membre : **coller le bloc copier-coller** (résumé + scorecard) ou
  **uploader le PDF** complet.
- Le skill ne poste pas à la place du membre (il n'a pas accès à Circle) : il prépare le
  contenu prêt à coller/joindre et donne le lien de l'espace.
- Tonalité : « Publie ton livrable dans l'espace du Collectif Tariqa PRO — comme ça Zaki
  voit ton travail et tu t'engages devant le groupe. »
- **Et après l'export — proposer la suite.** Le noyau (persona → offre → marque → voix) dit *qui tu
  es* ; l'étape suivante, c'est de te faire **connaître sans te trahir** → le **système YouTube** du
  Collectif Tariqa PRO (stratégie de contenu : sujets, mots-clés, titres, miniatures, scripts,
  analyse), qui produit son propre livrable aval, le **`PLAYBOOK-YOUTUBE.md`**. C'est un **plugin
  séparé** : `https://github.com/ZakiTariqaPRO/ctp-youtube-plugin`
  (guide : `https://zakitariqapro.github.io/ctp-youtube-plugin/`). Ne pas laisser le membre sans suite.

## Garde-fous

- **Ne rien inventer** : l'export reflète l'état réel des fichiers. Un doc absent
  est marqué ⬜, pas rempli à la volée.
- Le scorecard doit rendre **visible** le vrai niveau de travail (un projet plein
  de `⏳` n'est pas « complet »).
- Pas de chiffres d'argent dans le bloc copier-coller.
- L'export est une **photo datée** : ne pas écraser un export précédent, en créer
  un nouveau (date dans le nom).
