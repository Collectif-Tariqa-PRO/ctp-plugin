# Le débug sur quatre surfaces — ce qui passe, ce qui casse

Question posée : le débug doit vivre dans Claude Code, Claude, un GPT personnalisé et un site
web. Coach Zaki, avec toute sa doctrine, suit-il partout ?

**Réponse courte : non, pas tel quel.** Voici les chiffres, puis ce qu'il faut faire.

---

## Ce que pèse le débug aujourd'hui

| | Mots | ≈ tokens |
|---|---|---|
| `SKILL.md` — le moteur | 1 740 | 2 300 |
| Les 8 références du débug | 19 400 | 26 000 |
| **Coach Zaki embarqué** (doctrine 6 piliers, lexique, posture, leviers) | **45 660** | **61 000** |
| **Total** | **66 830** | **≈ 89 000** |

**Coach Zaki pèse plus du double du débug lui-même.** C'est normal — c'est la doctrine, et
c'est le différenciateur. Mais c'est aussi ce qui rend le portage non trivial.

---

## Surface par surface

### Claude Code — fonctionne aujourd'hui
Chargement progressif : seul `SKILL.md` entre en contexte (2 300 tokens), les références sont
lues à la demande. Les 89 000 tokens ne sont jamais tous chargés. **Rien à faire.**

### Claude (application et web) — même mécanisme
Les compétences y fonctionnent pareil. **Portage direct.**

### GPT personnalisé — ça casse ici
Deux limites dures. Les **instructions sont plafonnées à 8 000 caractères**, soit environ
2 000 tokens : notre `SKILL.md` fait déjà ~10 000 caractères, il **ne rentre pas**. Et la
**connaissance est limitée à 20 fichiers**, servis par recherche automatique, pas par
chargement contrôlé.

**Le vrai risque n'est pas la place, c'est le hasard de la récupération.** Sur un GPT, rien ne
garantit que `lignes-rouges.md` soit retrouvé au moment précis où quelqu'un pose une question
piégeuse. Un fichier de sécurité qui n'est chargé qu'« en général » ne protège pas.

### Site web — ça casse autrement
Il faut un backend. Mettre 89 000 tokens dans le prompt système à chaque tour est lent et
coûteux, et la qualité se dégrade sur des contextes aussi longs. Il faut la même séparation
que partout : un noyau permanent, une bibliothèque à la demande.

---

## Ce qu'il faut faire : séparer le noyau de la bibliothèque

### Le noyau — toujours chargé, partout, sans exception
Environ **6 000 à 8 000 tokens**. Il contient ce qui ne doit jamais dépendre d'une recherche :

- la **posture** et le dosage de la franchise ;
- les **onze questions** et ce qu'on écoute pour chacune ;
- les **huit règles dures** ;
- le **déroulé** et la règle « le process ne se saute pas » ;
- **les lignes rouges en entier.**

**Les lignes rouges ne sont jamais en récupération.** C'est le seul point non négociable de
tout ce document : un garde-fou qu'on va chercher quand on y pense n'est pas un garde-fou.

### La bibliothèque — à la demande
Le référentiel des douleurs, les sources vérifiées, le crible, les objections, et la doctrine
de Coach Zaki. On ne la charge que lorsque le sujet apparaît.

### Et deux fichiers doivent cesser d'être de la prose
Le **référentiel vidéo** et les **sources vérifiées** sont des tables, pas des textes. En
faire des données structurées apporte trois choses : elles deviennent identiques sur les
quatre surfaces, elles se mettent à jour sans toucher au prompt, et une nouvelle vidéo se
publie sans redéployer quoi que ce soit.

---

## L'architecture que je recommande : un moteur, plusieurs portes

**Un seul backend** porte le noyau, la bibliothèque et les données. Le site l'appelle
directement. Le GPT personnalisé l'appelle par une action. Claude Code garde sa copie locale
**pour construire et tester**, pas pour servir.

**Pourquoi c'est la seule option viable.** Quatre copies divergent — c'est déjà arrivé dans le
Collectif entre `~/.claude` et le plugin, au point qu'il a fallu décider que le plugin fait
foi. À quatre surfaces, ce n'est plus une divergence, c'est quatre produits différents portant
le même nom. Et la première chose qui divergera, ce sont les lignes rouges.

**Et il y a un argument qui tranche.** Il y a de toute façon une **page de capture** avant
l'outil : coordonnées, puis accès. Donc le site est la porte principale, pas un canal
secondaire. Autant y mettre le moteur.

---

## L'ordre que je propose

1. **Découper le noyau** (6-8k tokens) et vérifier qu'il tient seul, sans les références. Se
   teste dans Claude Code aujourd'hui.
2. **Convertir en données** le référentiel vidéo et les sources.
3. **Monter le backend** avec la page de capture — c'est là que les leads arrivent, et ça
   répare au passage la fuite du formulaire actuel.
4. **Brancher le GPT personnalisé** dessus en client léger.

**Ce qu'on ne fait pas** : un GPT personnalisé autonome avec 20 fichiers de connaissance. Ça
donnerait un débug qui a l'air de marcher, qui perd ses garde-fous une fois sur cinq, et
qu'on ne pourrait pas corriger d'un seul endroit.

---

## Sur la qualité de l'expérience

Le point de vigilance n'est pas technique, il est de contenu : **ce qui fait la qualité du
débug, c'est la doctrine.** Un débug sans les 61 000 tokens de Coach Zaki pose les mêmes
questions et rend un portrait générique.

Donc le critère d'acceptation d'une surface est simple, et il vaut la peine d'être testé
littéralement : **le même cas, joué sur les quatre surfaces, doit produire le même
diagnostic.** Si le site et le GPT ne trouvent pas le même blocage que Claude Code sur le même
profil, la surface n'est pas prête.
