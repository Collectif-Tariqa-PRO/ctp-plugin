# Le gabarit du portrait — la mise en page, et comment sortir le fichier

Tu ouvres cette page **avant d'écrire le portrait**, en même temps que `restitution.md`.
Celle-là dit ce qu'on écrit ; celle-ci dit à quoi ça ressemble et comment ça sort du fil.

## Pourquoi un gabarit, et pourquoi on n'en invente jamais un autre

Le portrait est un document que la personne va garder et relire dans trois mois. Il doit se
reconnaître au premier coup d'oeil comme un document du Collectif, et deux portraits produits
à trois mois d'écart doivent se ressembler. **Aucune couleur, aucune police, aucune marge ne
se décide en séance.** Tu remplaces le texte dans les blocs ci-dessous, tu ne redessines rien.

Si un passage du portrait n'entre dans aucun bloc existant, tu le mets dans un simple
paragraphe. Tu n'inventes pas un bloc.

---

## ⛔ La mise en page ne résume JAMAIS

C'est la faute la plus probable à cette étape, et c'est la plus grave, alors elle est écrite
avant tout le reste.

Tu passes d'un texte à des blocs. Le geste naturel, à ce moment-là, c'est de « ranger » :
raccourcir un paragraphe pour qu'il tienne dans un cadre, garder la phrase-clé et jeter
l'explication, transformer un raisonnement en trois puces. **Tu ne fais rien de tout ça.**

**Chaque phrase du portrait entre dans le fichier, entière.** Les introductions de section,
les explications de mécanique, les citations de la personne, les « pourquoi celle-là » sous
chaque vidéo et chaque invocation : tout est reporté tel quel. Tu ne coupes pas, tu ne
condenses pas, tu ne remplaces pas un paragraphe par une liste.

**Le test avant de livrer.** Compare la longueur du portrait que tu as écrit et celle du
fichier. Si le fichier est plus court, tu as résumé : reprends. Un portrait complet fait
**une vingtaine de pages, souvent davantage**. Un document de cinq pages n'est pas un portrait
serré, c'est un portrait amputé.

**Pourquoi ça compte plus que la mise en page elle-même.** La personne vient de passer une
heure à répondre. Ce qu'elle doit sentir en ouvrant le document, c'est le travail : quelqu'un
a pris ce qu'elle a dit au sérieux, l'a expliqué, l'a relié, l'a argumenté. Un document qui
résume donne exactement l'impression inverse — celle d'un texte qu'elle aurait pu obtenir
toute seule en trois minutes. C'est ce que le Collectif ne fait pas.

**Et donc, dans les blocs :** un `.couche` contient plusieurs paragraphes, pas une phrase. Un
`.axe` contient bien une phrase, c'est le seul endroit où c'est voulu. Une fiche vidéo garde
son explication en entier. Une invocation garde son *pourquoi celle-là*. Le bloc `.final`
reprend les lignes du portrait sans les tailler.

---

## Comment tu produis le fichier

**Tu le produis toujours, sans qu'on te le demande, à la fin de la séance.** La personne n'a
rien à réclamer, rien à copier-coller.

Tu as deux manières de faire, et tu prends la première qui marche chez toi.

**1. Tu sais fabriquer un vrai PDF.** Tu composes la page HTML ci-dessous et tu la convertis
en PDF. C'est le rendu idéal : la personne reçoit le document fini.

⚠️ **Le piège, et il est réel.** L'atelier dans lequel tu fabriques le fichier n'a souvent
**pas d'accès à internet**, même quand toi tu en as un. Les images ne se téléchargeront donc
pas, et tu obtiendras un PDF avec des cadres vides. Avant de livrer un PDF, **vérifie que les
images sont bien dedans**. Si elles ne le sont pas, tu ne livres pas ce PDF : tu passes à la
seconde manière.

**2. Tu livres la page HTML.** Tu écris exactement le même document dans un fichier `.html`
et tu le remets. Les images se chargent depuis le web au moment où la personne l'ouvre, donc
le rendu est complet. Tu ajoutes alors cette phrase, telle quelle :

> *Ton portrait est dans ce fichier. Ouvre-le, il s'affiche comme un document. Pour en faire
> un PDF que tu gardes : Ctrl+P sur Windows, Cmd+P sur Mac, puis « Enregistrer au format
> PDF ». Coche « Graphiques d'arrière-plan » pour garder les couleurs.*

**Dans les deux cas tu nommes le fichier** `Le-Debug_portrait_<Prénom>.pdf` ou `.html`. Sans
prénom : `Le-Debug_portrait.html`.

---

## Les images — les adresses sont écrites en entier, c'est volontaire

Tu ne reconstruis jamais une adresse à partir d'un dossier et d'un nom : tu copies celle qui
correspond à la vidéo que tu cites. Une vidéo dont la miniature n'est pas dans cette liste se
cite **sans image**, avec le bloc `.vid` privé de son `<div class="th">`.

- Pourquoi tu n'arrives pas à changer : https://hub.tariqa.pro/le-debug/kb/img/z4O-y-9aieE.jpg
- Maîtriser son temps : https://hub.tariqa.pro/le-debug/kb/img/RbsZMkrTgTk.jpg
- La vérité crue, avec Fethallah Otmani : https://hub.tariqa.pro/le-debug/kb/img/d_JgDTmVfV8.jpg
- Collectif contre individualisme : https://hub.tariqa.pro/le-debug/kb/img/wfbIrwEsMVY.jpg
- Change ton entourage : https://hub.tariqa.pro/le-debug/kb/img/mgSYqycZHWc.jpg
- Entreprendre en islam, ta foi comme force : https://hub.tariqa.pro/le-debug/kb/img/ovzn-YJSZU8.jpg
- Consultant, expert, juriste : https://hub.tariqa.pro/le-debug/kb/img/H31Q5_s0X-Y.jpg
- Ce n'est pas une formation de plus : https://hub.tariqa.pro/le-debug/kb/img/Wqr0sohEAdg.jpg
- Un week-end à Paris : https://hub.tariqa.pro/le-debug/kb/img/J8x5YwVMy2g.jpg
- Qui je suis, et pourquoi j'ai lancé le Collectif : https://hub.tariqa.pro/le-debug/kb/img/i6D3foCljjs.jpg
- https://hub.tariqa.pro/le-debug/kb/img/pst_VceGdQ8.jpg
- https://hub.tariqa.pro/le-debug/kb/img/mxCJJ4GOgaA.jpg
- https://hub.tariqa.pro/le-debug/kb/img/oWy8zo-2W5E.jpg
- https://hub.tariqa.pro/le-debug/kb/img/qoVJfBCmHXU.jpg

---

## Le squelette — tu le copies tel quel et tu remplaces le texte

Les polices sont celles de la machine de la personne, il n'y a rien à télécharger. Les
coupures de page sont calculées par le navigateur : tu ne comptes pas les pages et tu ne
coupes rien à la main.

```html
<!doctype html><html lang="fr"><head><meta charset="utf-8">
<title>Le Débug — ton portrait</title>
<style>
@page { size:A4; margin:17mm 16mm 15mm; }
@page cover { margin:0; }
:root{ --noir:#0d0d0d; --encre:#141414; --or:#FFC000; --beige:#f5f0e8;
  --ligne:#e2dad0; --gris:#6b6b6b; --blanc:#ffffff; }
*{box-sizing:border-box;}
body{margin:0;font-family:"Avenir Next",Avenir,"Segoe UI","Helvetica Neue",sans-serif;
  color:var(--encre);font-size:10.6pt;line-height:1.68;
  -webkit-print-color-adjust:exact;print-color-adjust:exact;background:var(--blanc);}
h1,h2,h3{font-family:Georgia,"Times New Roman",serif;font-weight:700;}
h2,h3{page-break-after:avoid;}

/* couverture — seule page à fond perdu */
.cover{page:cover;break-after:page;background:var(--noir);color:var(--blanc);
  min-height:297mm;display:flex;flex-direction:column;justify-content:center;padding:34mm 24mm;}
.marque{font-family:Georgia,serif;font-size:12pt;letter-spacing:.18em;text-transform:uppercase;
  margin-bottom:auto;color:var(--blanc);}
.marque span{color:var(--or);}
.cover h1{font-size:40pt;line-height:1.08;margin:0 0 3mm;color:var(--blanc);}
.cover .rule{width:26mm;height:3px;background:var(--or);margin:0 0 6mm;}
.cover .sub{font-size:12pt;color:#ddd6c9;max-width:132mm;line-height:1.6;}
.cover .foot{margin-top:auto;font-size:9pt;color:var(--or);letter-spacing:.08em;}

/* une section = un chapitre numéroté, il commence en haut d'une page */
.sec{break-before:page;}
h2{font-size:18pt;color:var(--noir);margin:0 0 5mm;padding-bottom:2.5mm;
  border-bottom:2px solid var(--or);}
h2 .num{color:var(--or);}
h3{font-size:11.5pt;color:var(--noir);margin:7mm 0 2mm;}
h3::before{content:"";display:inline-block;width:2.6mm;height:2.6mm;background:var(--or);
  margin-right:2.4mm;vertical-align:middle;}
p{margin:0 0 3.4mm;} b{color:var(--noir);}
.lede{font-size:10.8pt;color:var(--gris);font-style:italic;margin-bottom:6mm;}
ul{margin:0 0 3.4mm;padding-left:5mm;} li{margin-bottom:1.8mm;}
.som{columns:2;column-gap:9mm;font-size:9.8pt;line-height:1.9;}
.som b{color:var(--noir);}

/* les cinq axes */
.axe{margin:0 0 4mm;padding-left:4.5mm;border-left:2px solid var(--ligne);
  break-inside:avoid;}

/* les trois niveaux — nafs, aql, chemin */
.niv{border:1px solid var(--ligne);border-left:3px solid var(--ligne);padding:4mm 5mm;
  margin-bottom:2.5mm;break-inside:avoid;}
.niv .t{font-family:Georgia,serif;font-weight:700;font-size:12pt;color:var(--noir);margin-bottom:1mm;}
.niv .d{font-size:9.6pt;color:var(--gris);}
.niv.ici{background:var(--noir);border-color:var(--or);border-left:4px solid var(--or);}
.niv.ici .t{color:var(--blanc);} .niv.ici .d{color:#c9c2b4;}
.niv .flag{float:right;background:var(--or);color:var(--noir);font-size:7.8pt;
  letter-spacing:.1em;text-transform:uppercase;padding:.8mm 2.2mm;
  font-family:"Avenir Next",sans-serif;}

/* les couches du blocage — la dernière est en noir */
.couche{background:var(--beige);border-left:3px solid var(--or);padding:4.5mm 5.5mm;
  margin:0 0 4.5mm;break-inside:avoid;}
.couche.fond{background:var(--noir);color:#efe9dd;border-left:4px solid var(--or);}
.couche.fond h3,.couche.fond b{color:var(--blanc);}
.couche.fond h3::before{background:var(--or);}
.couche h3{margin-top:0;}

/* invocations */
blockquote.dua{border:1px solid var(--ligne);border-top:3px solid var(--or);
  background:var(--blanc);padding:4mm;margin:0 0 3.5mm;break-inside:avoid;}
blockquote.dua .ar{margin-top:0;font-size:13.5pt;line-height:1.7;text-align:right;
  direction:rtl;color:var(--noir);margin-bottom:3mm;font-family:"Geeza Pro","Al Bayan",serif;}
blockquote.dua .ph{font-style:italic;font-size:9.4pt;color:var(--gris);margin-bottom:1.5mm;}
blockquote.dua .tr{font-weight:600;font-size:9.9pt;margin-bottom:1.2mm;color:var(--noir);}
blockquote.dua .ref{font-size:8.8pt;color:var(--gris);letter-spacing:.06em;
  text-transform:uppercase;margin-bottom:3mm;}
blockquote.dua .why{font-size:9pt;line-height:1.55;border-top:1px solid var(--ligne);
  padding-top:2.5mm;}

/* la carte des six piliers */
.map{background:var(--noir);color:var(--blanc);padding:5mm 6mm;margin:0 0 5mm;
  font-family:Georgia,serif;font-size:11.5pt;text-align:center;letter-spacing:.03em;
  break-inside:avoid;}
.map .ici{display:block;margin-top:2.5mm;color:var(--or);font-size:13.5pt;font-weight:700;}

/* fiches vidéo */
.vid{display:flex;gap:5mm;margin:0 0 5mm;break-inside:avoid;align-items:flex-start;}
.vid .th{position:relative;flex:0 0 48mm;}
.vid .th img{width:48mm;display:block;border:1px solid var(--ligne);}
.vid .play{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);
  width:11mm;height:8mm;background:var(--or);border-radius:1.6mm;}
.vid .play::after{content:"";position:absolute;left:4.2mm;top:2mm;
  border-left:3.4mm solid var(--noir);border-top:2mm solid transparent;
  border-bottom:2mm solid transparent;}
.vid .txt{flex:1;}
.vid .tag{display:inline-block;font-size:7.6pt;letter-spacing:.12em;text-transform:uppercase;
  background:var(--noir);color:var(--or);padding:.7mm 2mm;margin-bottom:1.6mm;}
.vid .ti{display:block;font-weight:700;color:var(--noir);font-size:10.6pt;margin-bottom:1.4mm;}
.vid .why{font-size:9.7pt;margin-bottom:1.4mm;}
.vid .url{font-size:8.4pt;color:var(--gris);word-break:break-all;}

/* la seule chose de la semaine, et le bloc de fin */
.cta{background:var(--beige);border-left:3px solid var(--or);padding:5mm 5.5mm;
  margin:5mm 0 0;break-inside:avoid;}
.contact{display:flex;gap:5mm;margin:4mm 0;}
.contact .c{flex:1;border:1px solid var(--ligne);border-top:3px solid var(--or);
  padding:4mm;text-align:center;}
.contact .c .lab{font-size:8pt;letter-spacing:.12em;text-transform:uppercase;
  color:var(--gris);margin-bottom:1.5mm;}
.contact .c .val{font-size:11.5pt;font-weight:700;color:var(--noir);}
.final{border:2px solid var(--noir);padding:6mm;margin:4mm 0 0;break-inside:avoid;}
.final .lig{border-bottom:1px solid var(--ligne);padding:3mm 0;}
.final .lig:last-child{border-bottom:none;}
.final .k{font-size:8pt;letter-spacing:.12em;text-transform:uppercase;color:var(--blanc);
  background:var(--noir);display:inline-block;padding:.8mm 2.2mm;margin-bottom:1.6mm;}
.final .v{font-size:10.6pt;}
</style></head><body>

<div class="cover">
  <div class="marque">Collectif <span>Tariqa PRO</span></div>
  <h1>Le Débug</h1>
  <div class="rule"></div>
  <div class="sub">Le portrait de <b style="color:#FFC000;">PRÉNOM</b> — un regard honnête sur
    ta situation, à un instant T.<br>Pas un verdict, et rien sur ta valeur.</div>
  <div class="foot">tariqa.pro</div>
</div>

<div class="sec">
  <h2>À qui tu viens de parler</h2>
  <p>…</p>
  <h3>Ce que tu vas trouver</h3>
  <div class="som"><b>1.</b> …<br><b>2.</b> …</div>
</div>

</body></html>
```

**Sans prénom** : la couverture dit *« Ton portrait »* au lieu de *« Le portrait de X »*, et
le reste du document ne nomme personne.

---

## Les blocs, un par un

**Un axe du diagramme.** Cinq axes, une phrase chacun, **jamais de note ni de barre**.

```html
<div class="axe"><b>Clarté</b> — tu sais exactement ce que tu fais, pour qui, et pourquoi.</div>
```

**Un niveau.** Trois blocs `.niv`. Celui où la marque se voit porte `ici` et le drapeau.

```html
<div class="niv ici"><span class="flag">C'est ici</span>
  <div class="t">Ton nafs</div>
  <div class="d">Ce qui se passe en toi : ta raison d'y aller, tes peurs, le regard des autres.</div>
</div>
```

**Une couche du blocage.** La plus profonde, celle qui porte le diagnostic, prend `fond`.

```html
<div class="couche fond"><h3>Couche 4 — le pourquoi</h3><p>…</p></div>
```

**Une invocation.** Arabe, phonétique, traduction, source, puis le *pourquoi celle-là*.

```html
<blockquote class="dua">
  <div class="ar">اللَّهُمَّ لَا سَهْلَ إِلَّا مَا جَعَلْتَهُ سَهْلًا</div>
  <div class="ph">Allāhumma lā sahla illā mā jaʿaltahu sahlan</div>
  <div class="tr">Ô Allah, rien n'est facile sinon ce que Tu rends facile.</div>
  <div class="ref">Sahîh Ibn Hibbân 974</div>
  <div class="why">Pourquoi celle-là : …</div>
</blockquote>
```

**La carte des six piliers.**

```html
<div class="map">Mindset → Vente → Produit → Marketing → Opérations → Finances
  <span class="ici">Tu es ici : Mindset, à la porte de la Vente</span></div>
```

**Une fiche vidéo.**

```html
<div class="vid">
  <div class="th"><img src="https://hub.tariqa.pro/le-debug/kb/img/z4O-y-9aieE.jpg" alt=""><div class="play"></div></div>
  <div class="txt"><span class="tag">Le mécanisme</span>
    <span class="ti">Pourquoi tu n'arrives pas à changer</span>
    <div class="why">Pourquoi elle, pour toi : …</div>
    <div class="url">https://youtu.be/z4O-y-9aieE</div></div>
</div>
```

**Le bloc de fin.** Une ligne par idée à retenir.

```html
<div class="final">
  <div class="lig"><div class="k">Ce qui te bloque</div><div class="v">…</div></div>
  <div class="lig"><div class="k">À dire</div><div class="v">…</div></div>
</div>
```

---

## Ce qui n'entre jamais dans ce fichier

Aucune réponse du bloc pratique, et **jamais le verdict interne**. Le document doit pouvoir
être relu sans malaise et montré à son conjoint.

**Sur les montants, la règle se lit précisément**, parce qu'on l'a déjà lue trop large : ce
qui est interdit, ce sont **les montants qu'on énonce, nous** — promesse chiffrée, preuve par
le chiffre, prix du programme. **Les siens restent**, et ils portent souvent le diagnostic :
les deux mille euros qu'elle a mis dans une formation jamais appliquée sont son fait à elle,
et c'est parfois la phrase la plus parlante du portrait. Tu ne les retires pas.
