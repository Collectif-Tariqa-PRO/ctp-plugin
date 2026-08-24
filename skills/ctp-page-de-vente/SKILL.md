---
name: ctp-page-de-vente
description: Étape finale du parcours Collectif Tariqa PRO (entrepreneurs hors e-commerce) — transforme tout le travail du parcours (persona, offre, marque/positionnement, voix, pitch) en une LANDING PAGE v1 mise EN LIGNE, pointable depuis les réseaux sociaux. Capte un CTA qualifié (calendrier / formulaire), les vraies images du membre (anti AI-slop), garde du grain à moudre pour le call de closing, et déploie la page sur Vercel. Use when the user asks "créer ma landing page", "ma page de vente", "mettre ma page en ligne", "déployer mon site", "ma page d'accueil", "une page pour mes réseaux", or wants to publish a one-page site from their CTP work.
metadata:
  version: 1.3.0
  category: tariqa-pro
---

# CTP Page de vente — la landing page v1, en ligne

Aboutissement du parcours. Le membre a travaillé sa cible, son offre, sa marque, sa
voix, son pitch — tout est dans ses docs. **Ici on en fait une vraie page, EN LIGNE**,
qu'il peut pointer depuis Instagram, TikTok, WhatsApp, LinkedIn. Objectif : une **v1
qui convertit l'inconnu en rendez-vous**, pas un chef-d'œuvre.

## Le rythme — une idée à la fois, jamais un pavé

⚠️ Le membre n'est pas venu lire, il est venu avancer. On pose **une idée**, on **vérifie
qu'elle est passée**, puis on avance. Pas de longueur à compter : le test est « est-ce que ça
se lit d'un coup d'œil, sans faire peur ? ». Et la plomberie (connecteurs, serveurs,
autorisations) ne sort jamais dans un message au membre — sauf s'il pose la question, et alors
on répond franchement. Détail : `coach-zaki/references/tenue-de-seance.md`.

## ⛔ GATE — cette étape n'est PAS pour l'e-commerce

**Avant tout, vérifier le modèle.** Lire `offres/<slug>.md` / `ctp/tariqa-compliance.md`,
sinon demander : « Tu vends un service / un accompagnement / une expertise (parcours
entrepreneur), ou tu fais du e-commerce (vente de produits physiques en boutique) ? »

- **E-commerce → STOP cette étape.** Expliquer franchement : « Cette page-là est faite
  pour les entrepreneurs qui vendent un service ou une expertise et qui veulent décrocher
  des rendez-vous. Pour de l'e-commerce, c'est une autre logique : fiche produit, boutique,
  tunnel d'achat. Tout le reste du parcours (cible, offre, marque, voix) t'a déjà servi —
  mais on ne fait pas cette landing-là ensemble. » Ne pas forcer.
- **Service / expertise / accompagnement → on continue.** C'est LE distinctif : cette
  étape s'adresse au parcours entrepreneur Tariqa PRO.

## ⚠️ Dépendances — à savoir

- **Skill de design `ctp-taste`** : inclus dans le plugin (aucune install). C'est lui qui
  garantit le rendu **anti AI-slop**. On l'utilise pour la direction visuelle.
- **Prérequis côté membre (NON fournis par le plugin)** — les annoncer dès le départ :
  1. Un **compte d'hébergement Vercel** (gratuit) → pour la mise en ligne. Guide : `references/deploiement.md`.
  2. Un **outil de CTA** : calendrier (Calendly / cal.com) et/ou formulaire (**Tally**, gratuit). Guide : `references/cta.md`.
  3. Ses **vraies images** (logo, portrait, photos de réalisations). **Jamais d'images AI génériques** (= slop).

## Principe MVB ici aussi

Une **v1 en ligne** suffit. On ne peaufine pas à l'infini : page propre, claire, en
ligne, pointable. On affine avec les vrais retours (visiteurs, calls). On avance.

## Procédure

1. **Charger tout le parcours** : `personas/`, `offres/`, `positionnement/<slug>.md`
   (marque + positionnement + différenciateur), `voix/`, `brand/design-kit.md`,
   `ctp/REFERENCE-<slug>.md`, et le pitch si présent. Annoncer ce qu'on a.
2. **Gate e-commerce** (ci-dessus).
3. **Qualifier le CTA** (suivre `references/cta.md`) :
   - Type : prise de rendez-vous (calendrier), formulaire de contact, ou les deux.
   - Destination réelle : lien Calendly/cal.com et/ou formulaire Tally. **Valider** que
     le lien existe et que le CTA est **cohérent avec l'offre** (ex. offre premium →
     plutôt un call qu'un simple « achète maintenant »).
   - Un **CTA principal unique** par page (pas 5 boutons qui dispersent).
4. **Capter les images** (suivre `references/gabarit-page.md` § images) : demander les
   vraies photos. Si le membre n'en a pas encore → lister précisément ce qu'il doit
   fournir, et poser des **placeholders neutres** (aplats de couleurs du design-kit, pas
   de fausses photos AI). Ne pas bloquer la mise en ligne pour ça.
5. **Définir le hold-back** : décider ce qui va sur la page vs ce qu'on **garde pour le
   call de closing**. La page donne envie et qualifie ; elle ne déballe pas toute l'offre
   (prix détaillés, modalités, contenu exhaustif) — il faut laisser de quoi discuter en call.
6. **Construire la page** : structure dans `references/gabarit-page.md`. Direction visuelle
   via **`ctp-taste`** (anti-slop), couleurs/typos depuis `brand/design-kit.md`. Le
   **différenciateur doit être clair et visible**. SEO de base intégré (titre, meta
   description, balises Open Graph, HTML sémantique, page rapide). Footer discret
   « Collectif Tariqa PRO ».
7. **Écrire les fichiers** dans `landing/` du projet : `index.html`, `style.css`,
   `images/`. Page **statique, autonome** (pas de framework, pas de build).
8. **Mettre en ligne** (suivre `references/deploiement.md`) : déployer sur **Vercel**.
   Si la CLI Vercel est dispo, Claude pilote (`vercel`/`vercel deploy`) ; sinon, guider le
   membre pas-à-pas (compte → connexion → déploiement). Récupérer l'**URL en ligne**.
9. **Livrer** : donner l'URL, inviter à la pointer depuis ses réseaux (bio Insta/TikTok,
   LinkedIn, WhatsApp). Optionnel : proposer de publier l'annonce dans le Collectif.

## Règles de contenu — anti-slop & équilibre

- **Vraies images du membre uniquement.** Pas d'images AI génériques. Mieux vaut un aplat
  de couleur propre qu'une fausse photo.
- **Équilibre du texte** : lisible (corps ~16-18 px mini), pas de pavés, pas trop court non
  plus. **1 idée par section**, bénéfice avant caractéristique, hook en haut.
- **Hold-back** : la page vend le RENDEZ-VOUS, pas la totalité de l'offre.
- **Différenciateur clair** : il doit sauter aux yeux (section dédiée + repris dans le hero).
- **Voix du membre** : appliquer `voix/<slug>.md`. Respecter les mots interdits CTP et
  **pas de chiffres d'argent** mis en avant ; **pas de garantie de résultat**.

## Persistance

Ligne à ajouter au `CLAUDE.md` du projet :

```
## Landing page de référence
Page de vente v1 dans `landing/` (en ligne : <URL>). CTA : <calendrier/formulaire>.
Construite depuis la marque, l'offre et la voix (skill `ctp-page-de-vente`).
```

## Garde-fous

- **Gate e-commerce d'abord.** Ne jamais dérouler cette étape pour un projet e-commerce.
- **MVB** : viser une v1 en ligne, pas la perfection.
- Anti-slop non négociable : vraies images, design via `ctp-taste`, jamais de pavé illisible.
- **RGPD** : si formulaire, prévenir le membre (consentement, où vont les données) — voir `references/cta.md`.
- Footer « Collectif Tariqa PRO » discret sur la page.
