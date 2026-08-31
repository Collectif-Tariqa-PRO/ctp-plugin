#!/usr/bin/env python3
"""
Rapport quotidien de l'activite DM Instagram (travail de setting).

Lit les conversations Instagram via la Graph API et produit :
  - les statistiques de la journee (prises de contact, relances, reponses, delais)
  - les exemples concrets de relances
  - les prospects laisses sans reponse
  - un topo pret a copier dans WhatsApp

Usage :
    export IG_TOKEN="EAA..."
    python3 report.py                 # aujourd'hui
    python3 report.py --date 2026-08-30
    python3 report.py --json          # sortie machine (pour automatisation)

Aucune dependance externe : stdlib uniquement.
"""

import argparse
import json
import os
import statistics
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, date, timedelta
from zoneinfo import ZoneInfo

GRAPH = "https://graph.instagram.com/v23.0"
TZ = ZoneInfo("Europe/Paris")

# Au-dela de cette duree sans reponse, un prospect est considere comme "qui refroidit".
SEUIL_FROID_H = 24


# --------------------------------------------------------------------------- #
# Appels API
# --------------------------------------------------------------------------- #

def _get(path, token, **params):
    params["access_token"] = token
    url = f"{GRAPH}/{path}?{urllib.parse.urlencode(params)}"
    try:
        with urllib.request.urlopen(url, timeout=30) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        detail = e.read().decode("utf-8", "replace")
        raise SystemExit(
            f"\nErreur API Instagram ({e.code}) sur /{path}\n{detail}\n\n"
            "Causes frequentes :\n"
            "  - le token a expire (ils durent 60 jours) -> en regenerer un\n"
            "  - la permission instagram_business_manage_messages n'est pas cochee\n"
            "  - le compte n'est pas un compte professionnel\n"
        )


def _paginate(path, token, limit=50, max_pages=20, **params):
    """Suit les curseurs `after` et renvoie toutes les lignes."""
    out, page = [], 0
    params["limit"] = limit
    while path and page < max_pages:
        data = _get(path, token, **params)
        out.extend(data.get("data", []))
        after = data.get("paging", {}).get("cursors", {}).get("after")
        if not after or not data.get("data"):
            break
        params["after"] = after
        page += 1
    return out


def charger_conversations(token, jour):
    """Recupere les conversations touchees le jour demande, avec leurs messages."""
    convs = _paginate(
        "me/conversations", token,
        platform="instagram",
        fields="id,updated_time,participants",
    )

    # On ne descend dans les messages que des fils actifs ce jour-la : l'API
    # facture un appel par conversation, autant ne pas les parcourir tous.
    debut = datetime.combine(jour, datetime.min.time(), tzinfo=TZ)
    retenues = []
    for c in convs:
        maj = _parse_ts(c.get("updated_time"))
        if maj and maj >= debut:
            retenues.append(c)

    for c in retenues:
        c["msgs"] = _paginate(
            f"{c['id']}/messages", token,
            fields="id,created_time,from,to,message",
        )
    return retenues


def _parse_ts(ts):
    if not ts:
        return None
    try:
        return datetime.fromisoformat(ts.replace("+0000", "+00:00")).astimezone(TZ)
    except ValueError:
        return None


# --------------------------------------------------------------------------- #
# Analyse
# --------------------------------------------------------------------------- #

def analyser(convs, ig_user_id, jour):
    """
    Classe chaque message et deduit les indicateurs de setting.

    Definitions retenues :
      - prise de contact : 1er message sortant d'un fil, sans entrant avant
      - relance          : message sortant dont le precedent du fil est aussi
                           sortant (donc aucune reponse recue entre les deux)
      - reponse          : message sortant precede d'un message entrant
    """
    stats = {
        "date": jour.isoformat(),
        "conversations_actives": 0,
        "nouvelles_conversations": 0,
        "messages_envoyes": 0,
        "messages_recus": 0,
        "prises_de_contact": 0,
        "relances": 0,
        "reponses": 0,
    }
    delais = []            # minutes entre un message recu et sa reponse
    ex_relances = []       # exemples concrets a montrer
    en_attente = []        # prospects dont le dernier message reste sans reponse
    maintenant = datetime.now(TZ)

    for c in convs:
        msgs = sorted(
            (m for m in c.get("msgs", []) if _parse_ts(m.get("created_time"))),
            key=lambda m: _parse_ts(m["created_time"]),
        )
        if not msgs:
            continue

        interlocuteur = _interlocuteur(c, ig_user_id)
        actif_ce_jour = False
        premier_du_jour = True

        for i, m in enumerate(msgs):
            quand = _parse_ts(m["created_time"])
            sortant = str(m.get("from", {}).get("id")) == str(ig_user_id)
            du_jour = quand.date() == jour

            if du_jour:
                actif_ce_jour = True
                stats["messages_envoyes" if sortant else "messages_recus"] += 1

            if not sortant or not du_jour:
                premier_du_jour = False if du_jour else premier_du_jour
                continue

            precedents = msgs[:i]
            entrants_avant = [
                p for p in precedents
                if str(p.get("from", {}).get("id")) != str(ig_user_id)
            ]

            if not entrants_avant and not precedents:
                stats["prises_de_contact"] += 1
            elif precedents and str(precedents[-1].get("from", {}).get("id")) == str(ig_user_id):
                stats["relances"] += 1
                if len(ex_relances) < 5:
                    ex_relances.append({
                        "prospect": interlocuteur,
                        "heure": quand.strftime("%H:%M"),
                        "message": (m.get("message") or "").strip(),
                        "precedent": (precedents[-1].get("message") or "").strip(),
                        "silence_h": round(
                            (quand - _parse_ts(precedents[-1]["created_time"])).total_seconds() / 3600, 1
                        ),
                    })
            elif entrants_avant:
                stats["reponses"] += 1
                dernier_entrant = entrants_avant[-1]
                ecart = (quand - _parse_ts(dernier_entrant["created_time"])).total_seconds() / 60
                if 0 <= ecart <= 60 * 48:
                    delais.append(ecart)

            premier_du_jour = False

        if actif_ce_jour:
            stats["conversations_actives"] += 1
            if _parse_ts(msgs[0]["created_time"]).date() == jour:
                stats["nouvelles_conversations"] += 1

        dernier = msgs[-1]
        if str(dernier.get("from", {}).get("id")) != str(ig_user_id):
            age_h = (maintenant - _parse_ts(dernier["created_time"])).total_seconds() / 3600
            en_attente.append({
                "prospect": interlocuteur,
                "depuis_h": round(age_h, 1),
                "message": (dernier.get("message") or "").strip(),
            })

    stats["delai_median_min"] = round(statistics.median(delais)) if delais else None
    stats["taux_reponse"] = (
        round(100 * stats["reponses"] / (stats["reponses"] + len(en_attente)))
        if (stats["reponses"] + len(en_attente)) else None
    )
    en_attente.sort(key=lambda p: -p["depuis_h"])
    return stats, ex_relances, en_attente


def _interlocuteur(conv, ig_user_id):
    for p in conv.get("participants", {}).get("data", []):
        if str(p.get("id")) != str(ig_user_id):
            return p.get("username") or p.get("name") or "inconnu"
    return "inconnu"


# --------------------------------------------------------------------------- #
# Restitution
# --------------------------------------------------------------------------- #

def _p(n, singulier, pluriel=None):
    """Accorde un nom avec son nombre : _p(2, "relance") -> "2 relances"."""
    mot = singulier if abs(n) < 2 else (pluriel or singulier + "s")
    return f"{n} {mot}"


def _tronque(txt, n=110):
    txt = " ".join((txt or "").split())
    return txt if len(txt) <= n else txt[: n - 1] + "…"


def rapport_interne(s, relances, en_attente):
    """Le detail, pour toi."""
    L = [f"RAPPORT SETTING — {s['date']}", "=" * 46, "", "VOLUME"]
    L += [
        f"  Conversations actives   : {s['conversations_actives']}",
        f"  Nouvelles conversations : {s['nouvelles_conversations']}",
        f"  Messages envoyes        : {s['messages_envoyes']}",
        f"  Messages recus          : {s['messages_recus']}",
        "",
        "NATURE DU TRAVAIL",
        f"  Prises de contact : {s['prises_de_contact']}",
        f"  Relances          : {s['relances']}",
        f"  Reponses          : {s['reponses']}",
        "",
        "REACTIVITE",
        f"  Delai median de reponse : "
        + (f"{s['delai_median_min']} min" if s["delai_median_min"] is not None else "n/d"),
        f"  Taux de reponse         : "
        + (f"{s['taux_reponse']} %" if s["taux_reponse"] is not None else "n/d"),
        "",
    ]

    L.append("RELANCES — " + _p(len(relances), "exemple"))
    if relances:
        for r in relances:
            L += [
                f"  @{r['prospect']} — {r['heure']} (apres {r['silence_h']} h de silence)",
                f"     avant   : \"{_tronque(r['precedent'])}\"",
                f"     relance : \"{_tronque(r['message'])}\"",
                "",
            ]
    else:
        L += ["  Aucune relance envoyee aujourd'hui.", ""]

    froids = [p for p in en_attente if p["depuis_h"] >= SEUIL_FROID_H]
    L.append("SANS REPONSE — " + _p(len(en_attente), "prospect")
             + f", dont {len(froids)} > {SEUIL_FROID_H} h")
    for p in en_attente[:10]:
        alerte = "  <-- a traiter" if p["depuis_h"] >= SEUIL_FROID_H else ""
        L.append(f"  @{p['prospect']} — {p['depuis_h']} h{alerte}")
        L.append(f"     \"{_tronque(p['message'], 90)}\"")
    return "\n".join(L)


def topo_whatsapp(s, relances, en_attente):
    """Le message court, a copier tel quel."""
    j = datetime.fromisoformat(s["date"]).strftime("%d/%m")
    froids = [p for p in en_attente if p["depuis_h"] >= SEUIL_FROID_H]

    L = [f"Topo setting — {j}", ""]
    L.append(
        _p(s["conversations_actives"], "conversation active", "conversations actives")
        + ", " + _p(s["nouvelles_conversations"], "nouvelle") + "."
    )
    L.append(
        _p(s["prises_de_contact"], "prise de contact", "prises de contact")
        + ", " + _p(s["relances"], "relance")
        + ", " + _p(s["reponses"], "reponse") + "."
    )
    if s["delai_median_min"] is not None:
        L.append(f"Delai median de reponse : {s['delai_median_min']} min.")
    if s["taux_reponse"] is not None:
        L.append(f"Taux de reponse : {s['taux_reponse']} %.")
    L.append("")

    if s["relances"] == 0:
        L.append("Aucune relance aujourd'hui. C'est le point a corriger en priorite : "
                 "la majorite des rdv se prennent a la 2e ou 3e prise de contact.")
    else:
        r = relances[0]
        L.append(f"Exemple de relance bien menee — @{r['prospect']}, "
                 f"apres {r['silence_h']} h de silence :")
        L.append(f"\"{_tronque(r['message'], 140)}\"")
    L.append("")

    if froids:
        L.append(_p(len(froids), "prospect") + " "
                 + ("attend" if len(froids) < 2 else "attendent")
                 + f" une reponse depuis plus de {SEUIL_FROID_H} h : "
                 + ", ".join("@" + p["prospect"] for p in froids[:5]))
        L.append("A traiter en premier demain matin.")
    else:
        L.append("Aucun prospect en attente de plus de 24 h. Boite propre.")
    return "\n".join(L)


# --------------------------------------------------------------------------- #

def main():
    ap = argparse.ArgumentParser(description="Rapport quotidien du setting Instagram")
    ap.add_argument("--date", help="jour analyse (AAAA-MM-JJ), defaut aujourd'hui")
    ap.add_argument("--hier", action="store_true", help="raccourci pour la veille")
    ap.add_argument("--json", action="store_true", help="sortie JSON brute")
    a = ap.parse_args()

    token = os.environ.get("IG_TOKEN")
    if not token:
        raise SystemExit(
            "IG_TOKEN absent.\n\n"
            "  export IG_TOKEN=\"EAA...\"\n\n"
            "Voir README.md pour obtenir un token (20 min, gratuit)."
        )
    ig_user_id = os.environ.get("IG_USER_ID", "17841408507941653")

    if a.hier:
        jour = (datetime.now(TZ) - timedelta(days=1)).date()
    elif a.date:
        jour = date.fromisoformat(a.date)
    else:
        jour = datetime.now(TZ).date()

    convs = charger_conversations(token, jour)
    stats, relances, en_attente = analyser(convs, ig_user_id, jour)

    if a.json:
        print(json.dumps(
            {"stats": stats, "relances": relances, "en_attente": en_attente},
            ensure_ascii=False, indent=2,
        ))
        return

    print(rapport_interne(stats, relances, en_attente))
    print("\n" + "=" * 46)
    print("A COPIER DANS WHATSAPP")
    print("=" * 46 + "\n")
    print(topo_whatsapp(stats, relances, en_attente))


if __name__ == "__main__":
    main()
