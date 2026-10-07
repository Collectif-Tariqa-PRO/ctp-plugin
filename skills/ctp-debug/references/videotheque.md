# La vidéothèque — quel sujet appelle quelle vidéo

**À quoi ça sert.** Sans arborescence, on sert la vidéo dont le titre ressemble le plus à ce
que la personne vient de dire. C'est ce qui a produit les deux défauts relevés en test : la
même vidéo servie trois fois avec trois horodatages différents, et une vidéo « expert »
donnée à quelqu'un qui n'est pas un expert.

---

## Les quatre règles

**Une vidéo n'apparaît qu'une seule fois dans un portrait.** Trois horodatages d'une même
masterclass, ce n'est pas trois ressources : c'est une ressource servie trois fois, et ça
donne l'impression qu'on n'en a qu'une.

**Pas d'horodatage par défaut — on donne la vidéo entière.** Le reste sert aussi. On ne
découpe que si un passage précis est le sujet **et** que la vidéo est longue.

**Que des vidéos longues.** Aucun Short : une minute fait réagir en scroll, elle ne fait pas
comprendre un mécanisme.

**On vérifie à QUI la vidéo parle, pas de quoi elle parle.** Le sujet peut coller alors que
le profil visé n'est pas le sien.

---

## L'arborescence

| Le sujet détecté | La vidéo à servir |
|---|---|
| **Changement, motivation, discipline, « j'attends d'être motivé »** | [Pourquoi tu n'arrives pas à changer en tant que musulman (les vraies lois du changement)](https://youtu.be/z4O-y-9aieE) |
| **Mindset de l'entrepreneur musulman, intention, tawakkul, rizq** | [Niyya, tawakkul, rizq — Comment penser en tant qu'entrepreneur musulman](https://www.youtube.com/watch?v=pst_VceGdQ8) |
| **Blocages, peur, ce qui retient, la foi comme force** | [Entreprendre en islam : et si ta foi était ta plus grande force ?](https://www.youtube.com/watch?v=ovzn-YJSZU8) |
| **La vente, le rapport à la vente** | [La vérité crue sur l'entrepreneuriat et la foi, avec Fethallah Otmani](https://www.youtube.com/watch?v=d_JgDTmVfV8) |
| **L'argent, le rapport à l'argent** | [La vérité sur l'argent que tout entrepreneur musulman doit entendre, avec Dr Fethallah Otmani](https://youtu.be/qoVJfBCmHXU) ⚠️ *à confirmer, voir plus bas* |
| **La solitude, l'entourage, « je ne veux pas le faire seul »** | [Tu veux réussir ? Change ton entourage avant de changer de stratégie](https://youtu.be/mgSYqycZHWc) — **c'est celle-ci en premier**, elle traite la mise en pratique et l'effet de l'entourage |
| **L'individualisme comme paradigme appris** | [Collectif vs Individualisme : le vrai défi des entrepreneurs musulmans](https://www.youtube.com/watch?v=wfbIrwEsMVY) |
| **Salarié qui hésite, transition vers l'entrepreneuriat** | [Salarié ou entrepreneur : comment savoir si c'est le bon moment pour un musulman de se lancer ?](https://www.youtube.com/watch?v=oWy8zo-2W5E) |
| **Le temps, l'organisation, « je n'ai pas le temps »** | [Maîtriser son temps — les principes qui changent tout pour un entrepreneur musulman](https://youtu.be/RbsZMkrTgTk) |
| **« La vente c'est sale », marketing contre closing** | [J'ai invité mon concurrent à débattre](https://youtu.be/mxCJJ4GOgaA) |
| **Expert-métier qui doit devenir entrepreneur** ⚠️ *ce profil uniquement* | [Consultant, expert, juriste : le switch stratégique à faire avant de te lancer](https://www.youtube.com/watch?v=H31Q5_s0X-Y) |

### Les trois vidéos de preuve — hors quota, servies au temps « et nous »

| | |
|---|---|
| **Pourquoi un accompagnement et pas une formation** | [Ce n'est pas une formation de plus qu'il te faut](https://youtu.be/Wqr0sohEAdg) |
| **Le collectif de l'intérieur** | [Un week-end avec des entrepreneurs musulmans à Paris](https://www.youtube.com/watch?v=J8x5YwVMy2g) |
| **Qui est Zaki** | [Qui je suis, et pourquoi j'ai lancé le Collectif Tariqa PRO](https://www.youtube.com/watch?v=i6D3foCljjs) |

---

## Une cartographie existe déjà, et elle est plus complète

`~/CTP-knowledge/CARTOGRAPHIE-RENVOIS.md` associe déjà des vidéos à des modules, à partir du
corpus des soixante transcriptions de la chaîne. **Cette vidéothèque-ci n'en est qu'un
extrait.** Le vrai catalogue reste à construire à partir de la chaîne entière — c'est la
proposition en attente.

## ⚠️ Les deux points en attente

**Le sujet « argent ».** Zaki a signalé que la vidéo servie n'était pas la bonne et qu'il en
existe une faite spécifiquement sur ce sujet avec Fethallah Otmani. Or les deux vidéos du
catalogue avec Fethallah Otmani sont *La vérité sur l'argent* (qoVJfBCmHXU) et *La vérité
crue sur l'entrepreneuriat et la foi* (d_JgDTmVfV8, rangée ici sous « vente »). **Il faut
trancher laquelle va sur « argent » et laquelle va sur « vente ».**

**« Tu as tout en toi ».** Vidéo annoncée par Zaki, lien pas encore fourni. **On ne la sert
pas tant qu'elle n'a pas d'URL ici** — on n'invente jamais un lien.

---

## La miniature

Chaque vidéo servie dans le portrait est accompagnée de sa miniature. Elle se récupère une
fois et se range dans `exports/thumbs/<videoId>.jpg` :

```bash
curl -sS -o "exports/thumbs/<ID>.jpg" "https://i.ytimg.com/vi/<ID>/maxresdefault.jpg"
```

Si le fichier fait moins de 5 ko, reprendre avec `hqdefault.jpg`.

**Et le titre ne s'invente jamais.** Il se récupère :

```bash
curl -sS "https://www.youtube.com/oembed?url=https%3A//www.youtube.com/watch%3Fv%3D<ID>&format=json"
```
