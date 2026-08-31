# Rapport quotidien du setting Instagram

Analyse les conversations DM Instagram et produit chaque soir :

- **le volume** : conversations actives, nouvelles conversations, messages envoyés / reçus
- **la nature du travail** : prises de contact, **relances**, réponses
- **la réactivité** : délai médian de réponse, taux de réponse
- **les relances en clair** : qui, à quelle heure, après combien d'heures de silence, avec le texte exact
- **les prospects laissés sans réponse**, triés par ancienneté
- **un topo prêt à copier dans WhatsApp**

## Pourquoi ce script existe

Le connecteur Instagram de Windsor.ai ne donne accès qu'aux insights, posts,
stories et commentaires. **Il n'expose aucune donnée de messagerie.** Les DM ne
sont accessibles que par la Graph API de Meta, d'où cet outil.

## Mise en route — 20 minutes, 0 €

L'API Instagram est gratuite. Aucun abonnement, aucun outil tiers.

> **Le point important :** tant que l'app reste en mode développement, tu accèdes
> à tes propres DM avec un simple *Standard Access*, réservé aux comptes ayant un
> rôle sur l'app. **Aucune App Review n'est nécessaire.** La validation Meta
> (2 à 3 semaines) ne devient obligatoire que pour lire les DM de comptes tiers,
> ce qui n'est pas notre cas.

1. **Compte développeur** — [developers.facebook.com](https://developers.facebook.com) → *Get Started*. Gratuit.
2. **Créer une app** — *Create App* → type **Business**.
3. **Ajouter le produit** *Instagram* → *API setup with Instagram login*.
4. **Lier le compte** `zaki_chairi` (compte professionnel obligatoire).
5. **Générer un token** avec les deux permissions :
   - `instagram_business_basic`
   - `instagram_business_manage_messages`
6. **Échanger contre un token longue durée** (60 jours) :

   ```bash
   curl -s "https://graph.instagram.com/access_token\
   ?grant_type=ig_exchange_token\
   &client_secret=TON_APP_SECRET\
   &access_token=TON_TOKEN_COURT"
   ```

Puis :

```bash
export IG_TOKEN="EAA..."
python3 report.py
```

## Utilisation

```bash
python3 report.py                  # aujourd'hui
python3 report.py --hier           # la veille (pour un envoi le matin)
python3 report.py --date 2026-08-30
python3 report.py --json           # sortie machine, pour l'automatisation
```

Aucune dépendance : Python 3.9+ et la bibliothèque standard.

## Automatiser l'envoi quotidien

Rapport chaque soir à 20 h :

```cron
0 20 * * * cd /chemin/vers/ig-setter-report && IG_TOKEN="EAA..." python3 report.py >> ~/setting.log 2>&1
```

Pour un envoi WhatsApp automatique, brancher la sortie `--json` sur l'API
WhatsApp Business, ou plus simplement laisser le rapport dans un fichier et le
copier — c'est un geste de 5 secondes par jour.

## Deux limites à connaître

**L'historique est perdu.** À la première connexion, Meta ne renvoie que les
**20 derniers messages** de chaque conversation existante. Tout ce qui a été
échangé avant est définitivement inaccessible. En revanche, à partir du jour du
branchement, **tout est conservé et mesurable**. Plus tôt c'est branché, plus tôt
l'historique commence.

**Le compte doit être le bon.** Le script ne voit que les DM du compte
professionnel connecté. Si la setteuse travaille depuis son compte personnel,
rien ne remonte — il faut qu'elle passe par un accès délégué au compte pro.

## Sécurité

Le token donne accès à la messagerie du compte. **Ne jamais le committer.**
Le passer par une variable d'environnement, ou un fichier `.env` non versionné.
Il expire au bout de 60 jours et doit être régénéré (étape 6).

## Définitions retenues

| Indicateur | Définition appliquée |
|---|---|
| Prise de contact | 1er message sortant d'un fil, sans message entrant avant |
| **Relance** | message sortant dont le précédent du fil est **aussi sortant** — donc aucune réponse reçue entre les deux |
| Réponse | message sortant précédé d'un message entrant |
| Délai de réponse | minutes entre un message reçu et la réponse (médiane, plafonnée à 48 h) |
| Taux de réponse | réponses ÷ (réponses + prospects encore sans réponse) |
| Prospect qui refroidit | dernier message entrant, sans réponse depuis plus de 24 h |
