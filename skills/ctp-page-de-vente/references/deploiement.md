# Déploiement — mettre la page EN LIGNE (Netlify)

But : une **URL publique** (ex. `nom-du-membre.netlify.app`) que le membre pointe depuis
ses réseaux. La page est statique (`landing/`), donc le déploiement est simple.

⚠️ **Prérequis membre** : un **compte Netlify** (gratuit, netlify.com). C'est l'équivalent
de l'abonnement / du compte GitHub : le plugin ne peut pas le fournir. Le dire dès le départ.

> **Pourquoi Netlify et plus Vercel ?** Jusqu'en version 1.6.0, on déployait sur l'offre
> gratuite de Vercel. Or ses conditions réservent cette offre à un usage personnel et non
> commercial, et elles citent noir sur blanc le fait de présenter un produit ou un service
> à vendre. Ta page de vente, c'est exactement ça. L'offre gratuite de Netlify, elle,
> n'interdit pas l'usage commercial. On préfère te le dire franchement plutôt que de te
> laisser sur un hébergement qui ne t'est pas destiné.

## Ce que l'offre gratuite de Netlify te donne (vérifié le 29/10/2026)

- **Gratuit, sans carte bancaire.** Un quota de **300 crédits par mois**, sans recharge possible.
- **Chaque mise en ligne en production coûte 15 crédits.** Le trafic consomme aussi des
  crédits (20 par Go transféré, 2 pour 10 000 requêtes). Une page légère et
  bien compressée tient très largement dans le quota.
- **Si le quota est épuisé, tes sites sont mis en pause** jusqu'au mois suivant : les
  visiteurs voient « Site not available ». D'où deux règles simples : compresser les
  images, et **regrouper tes corrections** avant de remettre en ligne, au lieu de
  redéployer pour chaque virgule.
- Nom de domaine perso et HTTPS inclus quand tu en voudras un.

Sources à revérifier si tu as un doute : `netlify.com/pricing` et
`docs.netlify.com` (page « How credits work »).

## Chemin recommandé — CLI Netlify (Claude pilote si dispo)

1. Vérifier la CLI : `netlify --version`. Absente → l'installer : `npm i -g netlify-cli`
   (nécessite Node ; sinon guider via l'install Node, ou passer au chemin B).
2. Connexion : `netlify login` (le membre confirme dans son navigateur — action manuelle).
3. Depuis le dossier `landing/`, faire d'abord un **brouillon** : `netlify deploy --dir .`
   - Au 1er run, Netlify demande s'il faut relier un projet existant ou en créer un
     nouveau : choisir **créer**, puis donner un nom simple (il devient `nom.netlify.app`).
   - Ouvrir l'URL de brouillon affichée, vérifier la page (y compris sur mobile).
4. Si tout est bon, mettre en production : `netlify deploy --dir . --prod`.
5. Récupérer l'**URL de production** affichée en fin de commande. C'est elle qu'on donne au membre.

## Chemin B — sans CLI / non-tech (Netlify Drop)

1. Le membre crée un compte sur netlify.com (connexion Google, GitHub ou email).
2. Il ouvre `app.netlify.com/drop` et **glisse-dépose le dossier `landing/`** entier.
3. Netlify met la page en ligne et donne l'URL `*.netlify.app`. Il peut renommer le site
   dans les réglages du projet pour obtenir une adresse propre.
4. Pour une mise à jour : dans le projet, onglet des déploiements, re-glisser le dossier
   `landing/` corrigé. L'URL reste la même.

Sans compte, une page déposée sur Drop ne reste pas en ligne : il faut un compte pour la garder.

## Repli — Cloudflare Pages (gratuit aussi)

Si Netlify bloque (compte refusé, quota épuisé à un moment critique), Cloudflare Pages
héberge aussi gratuitement une page statique, sans interdire l'usage commercial.

- **Avec la CLI** : `npx wrangler login`, puis depuis `landing/` :
  `npx wrangler pages deploy . --project-name nom-du-membre`. L'URL est `nom-du-membre.pages.dev`.
- **Sans CLI** : dans le tableau de bord Cloudflare, section Workers & Pages, créer un
  projet Pages par **téléversement direct** et déposer le dossier `landing/`.

## Après la mise en ligne

- Donner l'**URL** au membre, vérifier qu'elle s'ouvre (et sur **mobile**).
- L'inviter à la mettre dans ses bios réseaux (Instagram, TikTok, LinkedIn, WhatsApp).
- Mises à jour : ré-éditer `landing/`, regrouper les corrections, puis re-déployer
  (`netlify deploy --dir . --prod`) — l'URL reste la même.
- Nom de domaine perso (ex. `prenom.com`) = étape ultérieure facultative, pas pour la v1.

## Garde-fous

- Ne pas committer de secrets dans `landing/` (c'est public).
- Compresser les images avant déploiement : page rapide, et moins de crédits consommés.
- MVB : une URL `*.netlify.app` propre suffit pour la v1. On ne bloque pas sur le domaine custom.
- Ne jamais renvoyer un membre vers l'offre gratuite de Vercel pour sa page de vente :
  elle est réservée à un usage non commercial.
