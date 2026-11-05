#!/usr/bin/env python3
"""
Assemble les pages du site à partir d'une charpente commune.

Pourquoi un générateur plutôt que onze fichiers écrits à la main : l'en-tête,
le pied de page, le sprite du produit et les balises SEO doivent rester
identiques partout. Écrits onze fois, ils divergent au premier changement.

Usage : python3 outils/construire.py
Les fichiers .html sont écrits à la racine du site.
"""
import json, pathlib, re, sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from articles import ARTICLES

RACINE = pathlib.Path(__file__).resolve().parent.parent
DOMAINE = "https://borne-restaurants.fr"
MARQUE = "Bornéa"
TEL_AFF = "02 96 00 00 00"
TEL = "+33296000000"
MAIL = "contact@bornea.fr"

# --------------------------------------------------------------------------
# Sprite du produit. Dessiné d'après les photos fournisseur : caisson noir mat,
# écran vertical, colonne fine, socle rond lesté. Les proportions suivent la
# photo de face ; la vue de profil suit la seconde photo (platine VESA visible).
# --------------------------------------------------------------------------
SPRITE = """
<svg style="position:absolute;width:0;height:0;overflow:hidden" aria-hidden="true" focusable="false">
  <defs>
    <linearGradient id="ecranVeille" x1="0" y1="0" x2=".9" y2="1">
      <stop offset="0" stop-color="#6B4FE0"/>
      <stop offset=".34" stop-color="#3AA6E8"/>
      <stop offset=".62" stop-color="#F6E3E8"/>
      <stop offset=".84" stop-color="#E86A9A"/>
      <stop offset="1" stop-color="#5B3FC4"/>
    </linearGradient>
  </defs>

  <symbol id="borne-veille" viewBox="0 0 200 660">
    <rect x="14" y="6" width="172" height="302" rx="8" fill="#101114"/>
    <rect x="22" y="14" width="156" height="286" rx="3" fill="url(#ecranVeille)"/>
    <rect x="92" y="304" width="16" height="322" rx="5" fill="#101114"/>
    <rect x="34" y="624" width="132" height="14" fill="#101114"/>
    <ellipse cx="100" cy="624" rx="66" ry="15" fill="#22242A"/>
    <ellipse cx="100" cy="638" rx="66" ry="15" fill="#101114"/>
  </symbol>

  <symbol id="borne-commande" viewBox="0 0 200 660">
    <rect x="14" y="6" width="172" height="302" rx="8" fill="#101114"/>
    <rect x="22" y="14" width="156" height="286" rx="3" fill="#1B1D23"/>
    <rect x="32" y="26" width="74" height="9" rx="4" fill="#6E727C"/>
    <rect x="32" y="46" width="136" height="58" rx="4" fill="#2A2D35"/>
    <rect x="40" y="56" width="38" height="38" rx="3" fill="#6B4FE0"/>
    <rect x="86" y="60" width="62" height="8" rx="4" fill="#9AA0AB"/>
    <rect x="86" y="76" width="34" height="8" rx="4" fill="#5D626D"/>
    <rect x="32" y="112" width="136" height="58" rx="4" fill="#2A2D35"/>
    <rect x="40" y="122" width="38" height="38" rx="3" fill="#3AA6E8"/>
    <rect x="86" y="126" width="52" height="8" rx="4" fill="#9AA0AB"/>
    <rect x="86" y="142" width="34" height="8" rx="4" fill="#5D626D"/>
    <rect x="32" y="178" width="136" height="58" rx="4" fill="#2A2D35"/>
    <rect x="40" y="188" width="38" height="38" rx="3" fill="#E86A9A"/>
    <rect x="86" y="192" width="58" height="8" rx="4" fill="#9AA0AB"/>
    <rect x="86" y="208" width="34" height="8" rx="4" fill="#5D626D"/>
    <rect x="32" y="252" width="136" height="34" rx="5" fill="#3B2BD9"/>
    <rect x="66" y="264" width="68" height="10" rx="5" fill="#FFFFFF"/>
    <rect x="92" y="304" width="16" height="322" rx="5" fill="#101114"/>
    <rect x="34" y="624" width="132" height="14" fill="#101114"/>
    <ellipse cx="100" cy="624" rx="66" ry="15" fill="#22242A"/>
    <ellipse cx="100" cy="638" rx="66" ry="15" fill="#101114"/>
  </symbol>

  <symbol id="borne-profil" viewBox="0 0 200 660">
    <rect x="86" y="6" width="20" height="302" rx="4" fill="#101114"/>
    <rect x="80" y="14" width="6" height="286" rx="2" fill="#2A2D35"/>
    <rect x="104" y="150" width="26" height="34" rx="3" fill="#1B1D23"/>
    <rect x="112" y="158" width="4" height="4" fill="#4A4E58"/>
    <rect x="120" y="158" width="4" height="4" fill="#4A4E58"/>
    <rect x="112" y="170" width="4" height="4" fill="#4A4E58"/>
    <rect x="120" y="170" width="4" height="4" fill="#4A4E58"/>
    <rect x="126" y="160" width="16" height="14" rx="3" fill="#101114"/>
    <rect x="128" y="170" width="16" height="456" rx="5" fill="#101114"/>
    <rect x="70" y="624" width="132" height="14" fill="#101114"/>
    <ellipse cx="136" cy="624" rx="66" ry="15" fill="#22242A"/>
    <ellipse cx="136" cy="638" rx="66" ry="15" fill="#101114"/>
  </symbol>

  <symbol id="i-check" viewBox="0 0 24 24">
    <path fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" d="M4 12.5l5 5L20 6.5"/>
  </symbol>
  <symbol id="i-son" viewBox="0 0 24 24">
    <path fill="currentColor" d="M4 9h3.2L12 4.8v14.4L7.2 15H4a1 1 0 0 1-1-1v-4a1 1 0 0 1 1-1z"/>
    <g class="ecoute__onde" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round">
      <path d="M15.6 9.2a4 4 0 0 1 0 5.6"/>
      <path d="M18.2 6.6a7.6 7.6 0 0 1 0 10.8"/>
    </g>
  </symbol>
  <symbol id="i-son-coupe" viewBox="0 0 24 24">
    <path fill="currentColor" d="M4 9h3.2L12 4.8v14.4L7.2 15H4a1 1 0 0 1-1-1v-4a1 1 0 0 1 1-1z"/>
    <g fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round">
      <path d="M16 9.5l5 5M21 9.5l-5 5"/>
    </g>
  </symbol>
  <symbol id="i-logo" viewBox="0 0 24 24">
    <rect x="6" y="2" width="12" height="15" rx="2" fill="currentColor"/>
    <rect x="11" y="17" width="2" height="4" fill="currentColor"/>
    <rect x="5" y="20" width="14" height="2.4" rx="1.2" fill="currentColor"/>
  </symbol>
</svg>
"""

def borne(symbole="borne-veille", classe="borne", label=None, attrs=""):
    role = f' role="img" aria-label="{label}"' if label else ' aria-hidden="true"'
    return (f'<svg class="{classe}" viewBox="0 0 200 660"{role}{attrs}>'
            f'<use href="#{symbole}"/></svg>')

# --------------------------------------------------------------------------
NAV = [
    ("index.html", "La borne", True),
    ("blog.html", "Blog", True),
    ("guide-borne-de-commande-restaurant.html", "Guide d’achat", False),
    ("livraison-et-retours.html", "Livraison", False),
    ("contact.html", "Contact", False),
]

def bandeau():
    """Le bandeau du haut ne porte que ce qui decide : le prix, l'absence
    d'abonnement, le port offert. Trois faits, pas un slogan."""
    return f"""<div class="bandeau">
  <div class="env bandeau__int">
    <span><em>Sans abonnement</em></span>
    <span><b>720 € TTC</b> la borne, payés une fois</span>
    <span><b>Livraison offerte</b> en France métropolitaine</span>
    <span><a href="commander.html">Construire ma borne</a></span>
  </div>
</div>"""


def entete():
    morceaux = []
    for u, t, principal in NAV:
        classe = "" if principal else ' class="nav__secondaire"'
        morceaux.append('<a href="%s"%s>%s</a>' % (u, classe, t))
    liens = "".join(morceaux)
    return f"""<header class="tete">
  <div class="env tete__int">
    <a class="marque" href="index.html"><svg aria-hidden="true"><use href="#i-logo"/></svg>{MARQUE}</a>
    <nav class="nav" aria-label="Navigation principale">
      {liens}
      <a class="btn btn--petit" href="commander.html">Commander</a>
    </nav>
  </div>
</header>"""

def pied():
    return f"""<footer class="pied">
  <div class="env cols">
    <div>
      <h2>{MARQUE}</h2>
      <p>Bornes de commande tactiles pour la restauration. Vente et assistance depuis Saint-Brieuc.</p>
    </div>
    <div>
      <h2>Le produit</h2>
      <ul role="list">
        <li><a href="index.html">La borne à 600 € HT</a></li>
        <li><a href="commander.html">Commander</a></li>
        <li><a href="guide-borne-de-commande-restaurant.html">Guide d’achat</a></li>
        <li><a href="blog.html">Blog</a></li>
      </ul>
    </div>
    <div>
      <h2>Commande</h2>
      <ul role="list">
        <li><a href="livraison-et-retours.html">Livraison et retours</a></li>
        <li><a href="cgv.html">Conditions générales de vente</a></li>
        <li><a href="contact.html">Nous écrire</a></li>
      </ul>
    </div>
    <div>
      <h2>Le site</h2>
      <ul role="list">
        <li><a href="mentions-legales.html">Mentions légales</a></li>
        <li><a href="confidentialite.html">Données personnelles</a></li>
        <li><a data-tel href="tel:{TEL}">{TEL_AFF}</a></li>
        <li><a data-mail href="mailto:{MAIL}">{MAIL}</a></li>
      </ul>
    </div>
  </div>
  <div class="env pied__bas">
    <p>© <span data-annee>2026</span> {MARQUE}. Prix hors taxes, destinés aux professionnels.</p>
    <p>Paiement par carte sécurisé par Stripe.</p>
  </div>
</footer>"""

def fil(items):
    """items : [(libellé, url ou None pour la page courante)]"""
    lis = []
    for t, u in items:
        lis.append(f'<li><a href="{u}">{t}</a></li>' if u else f'<li><span aria-current="page">{t}</span></li>')
    ld = {
        "@context": "https://schema.org", "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": t,
             **({"item": DOMAINE + "/" + ("" if u == "index.html" else u)} if u else {})}
            for i, (t, u) in enumerate(items)]
    }
    return (f'<nav class="env fil" aria-label="Fil d’Ariane"><ol>{"".join(lis)}</ol></nav>'
            f'<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>')

# --------------------------------------------------------------------------
# CSS et JavaScript sont recopiés dans chaque page au lieu d'être liés.
#
# Un fichier lié suppose que tout le dossier arrive intact sur le serveur.
# Dans les faits, un seul fichier envoyé par erreur suffit à afficher un site
# sans aucun style. Une page qui contient tout ce dont elle a besoin s'affiche
# correctement même envoyée seule.
#
# Contrepartie : modifier un prix ou un numéro de téléphone se fait dans
# assets/config.js, puis on relance ce script pour propager le changement.
# --------------------------------------------------------------------------
def _lire(chemin):
    return (RACINE / chemin).read_text(encoding="utf-8").strip()

CSS = _lire("assets/site.css")
JS_CONFIG = _lire("assets/config.js")
JS_SITE = _lire("assets/site.js")
JS_INTEGRE = JS_CONFIG + "\n\n/* ---------------------------------------------------------------- */\n\n" + JS_SITE

def page(slug, titre, description, corps, ld=None, robots=None, classe_body="", script_page=None, style_page=None):
    """script_page et style_page sont intégrés à cette page seulement.
       Le configurateur de borne pèse plusieurs centaines de lignes : les
       mettre dans le script commun alourdirait les vingt-neuf autres pages
       pour rien."""
    blocs = ""
    for bloc in (ld or []):
        blocs += f'\n<script type="application/ld+json">{json.dumps(bloc, ensure_ascii=False, indent=1)}</script>'
    meta_robots = f'\n<meta name="robots" content="{robots}">' if robots else ""
    canon = f"{DOMAINE}/{slug}" if slug != "index.html" else f"{DOMAINE}/"
    html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titre}</title>
<meta name="description" content="{description}">{meta_robots}
<link rel="canonical" href="{canon}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{MARQUE}">
<meta property="og:title" content="{titre}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{DOMAINE}/img/og-borne-commande-restaurant.jpg">
<meta property="og:locale" content="fr_FR">
<meta name="theme-color" content="#F6F7F9">
<script>document.documentElement.className+=" js"</script>
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'><rect width='24' height='24' fill='%230B0E14'/><rect x='7' y='4' width='10' height='12' rx='1.5' fill='%231B4DF5'/><rect x='11' y='16' width='2' height='3' fill='%23fff'/><rect x='6' y='19' width='12' height='2' rx='1' fill='%23fff'/></svg>">
<style>
{{CSS_ICI}}
{style_page or ""}
</style>{blocs}
</head>
<body{f' class="{classe_body}"' if classe_body else ''}>
<a class="saut" href="#contenu">Aller au contenu</a>
{SPRITE.strip()}
{bandeau()}
{entete()}
{corps}
{pied()}
<script>
{{JS_ICI}}
</script>
{f'<script>{script_page}</script>' if script_page else ""}
</body>
</html>
"""
    html = html.replace("{CSS_ICI}", CSS).replace("{JS_ICI}", JS_INTEGRE)
    (RACINE / slug).write_text(html, encoding="utf-8")
    return slug

# ==========================================================================
# 1. Accueil : la page de vente, celle qui doit ressortir sur la requête
#    « borne commande restaurant ».
# ==========================================================================
CORPS_INDEX = """
<main id="contenu">

<section class="env vitrine">
  <div class="vitrine__objet">
    <figure class="photo">
      <img src="img/borne-de-commande-restaurant-ecran-paysage-1000.webp"
           srcset="img/borne-de-commande-restaurant-ecran-paysage-600.webp 600w, img/borne-de-commande-restaurant-ecran-paysage-1000.webp 1000w"
           sizes="(max-width: 62rem) 100vw, 27rem"
           width="1000" height="1000" fetchpriority="high" decoding="async"
           alt="Borne de commande pour restaurant : écran tactile blanc en position paysage sur son pied, affichant l’accueil Android">
    </figure>
    <div class="achat carte">
      <p class="surtitre">Borne de commande sur pied</p>
      <p class="achat__prix">
        <span class="montant prix">720 €</span>
        <span class="ttc">TTC, TVA 20 % comprise</span>
      </p>
      <p class="note" style="margin-top:.2rem">600 € HT · <strong style="color:var(--valide)">livraison offerte</strong> · payé une fois, aucun abonnement</p>
      <a class="btn btn--large" href="commander.html">Commander une borne</a>
      <ul class="garanties mt-1" role="list">
        <li><svg aria-hidden="true"><use href="#i-check"/></svg><span>0 € par mois, à vie</span></li>
        <li><svg aria-hidden="true"><use href="#i-check"/></svg><span>Garantie 2 ans, pièces et main-d’œuvre</span></li>
        <li><svg aria-hidden="true"><use href="#i-check"/></svg><span>Paiement par carte sécurisé par Stripe</span></li>
        <li><svg aria-hidden="true"><use href="#i-check"/></svg><span>Assistance par téléphone au <a data-tel href="tel:+33296000000">02 96 00 00 00</a></span></li>
      </ul>
    </div>
  </div>

  <div class="argument">
    <p class="surtitre">Restauration rapide · brasserie · kebab · boulangerie</p>
    <h1>Borne de commande pour restaurant</h1>
    <p class="chapo">Un écran tactile sur pied, posé à l’entrée de votre salle, sur lequel vos clients composent leur commande pendant que votre équipe reste en cuisine. Vendu une fois, sans abonnement.</p>

    <div class="actions mt-2">
      <a class="btn" href="commander.html">Construire ma borne</a>
      <a class="btn btn--secondaire" href="#video">Voir la borne en service</a>
    </div>
    <p class="note mt-1">Le configurateur est gratuit et sans compte à créer. Vous repartez avec le fichier de votre borne, que vous payiez ou non.</p>

    <dl class="chiffres-cle mt-2">
      <div><dt>Prix</dt><dd class="chiffres">720 €<span>TTC, payés une fois</span></dd></div>
      <div><dt>Abonnement</dt><dd class="chiffres">0 €<span>par mois, à vie</span></dd></div>
      <div><dt>Installation</dt><dd class="chiffres">0 €<span>nous montons votre page</span></dd></div>
      <div><dt>Mise en service</dt><dd class="chiffres">15 min<span>vous branchez, elle commande</span></dd></div>
    </dl>

    <div class="encadre-cle mt-2" data-reveal>
      <h2>L’essentiel en dix secondes</h2>
      <dl>
        <div><dt>Prix</dt><dd>600 € HT, payés une fois</dd></div>
        <div><dt>Abonnement</dt><dd>aucun, jamais</dd></div>
        <div><dt>Ce que c’est</dt><dd>un écran tactile sur pied, sous Android ouvert</dd></div>
        <div><dt>Particularité</dt><dd>l’écran pivote en paysage ou en portrait</dd></div>
        <div><dt>Alimentation</dt><dd>batterie intégrée, donc sans rallonge au sol</dd></div>
        <div><dt>Ce qui n’est pas fourni</dt><dd>le logiciel de caisse, l’imprimante, le lecteur de carte</dd></div>
        <div><dt>Livraison</dt><dd>offerte, 4 à 7 jours ouvrés</dd></div>
        <div><dt>Garantie</dt><dd>2 ans</dd></div>
      </dl>
    </div>

    <div class="mt-2 prose" data-reveal>
      <p>La borne ne remplace pas votre caisse et ne prétend pas la remplacer. Elle règle un problème plus étroit : à midi, la prise de commande devient le point le plus lent du service, et une file de six personnes fait repartir la septième.</p>
      <p>Vos clients composent leur commande sur l’écran, puis règlent au comptoir ou en ligne si votre application le permet. Pendant ce temps, la personne qui tenait la caisse peut servir, débarrasser ou aider en cuisine.</p>
    </div>

    <h2 class="mt-2" style="font-size:var(--t-xl)">Ce que ça change à midi</h2>
    <div class="points mt-1">
      <div data-reveal>
        <h3>Le client prend son temps</h3>
        <p>Devant un écran, personne ne souffle derrière lui. Il lit toute la carte au lieu de commander ce qu’il connaît déjà, et il ajoute plus volontiers un dessert ou une boisson.</p>
      </div>
      <div data-reveal>
        <h3>Le supplément est proposé à chaque fois</h3>
        <p>À 12 h 40, une équipe en rush arrête de proposer la sauce et la boisson : il faut faire avancer la file. Un écran pose la question à la commande n° 1 comme à la commande n° 180.</p>
      </div>
      <div data-reveal>
        <h3>Les commandes gênantes deviennent faciles</h3>
        <p>Une allergie, un plat mal prononcé, un français hésitant, un groupe qui change trois fois d’avis. Tout cela passe mieux sur un écran que devant six personnes qui attendent.</p>
      </div>
    </div>
  </div>
</section>

<section class="sec sec--alt" id="video">
  <div class="env">
    <p class="surtitre">En une minute</p>
    <h2 style="font-size:var(--t-xl)">À quoi sert une borne de commande</h2>
    <p class="prose mt-1">Si vous hésitez encore sur le principe, regardez. C’est plus rapide que de lire la page.</p>
    <figure class="video mt-2" data-reveal>
      <video id="film" controls preload="none" playsinline
             poster="video/borne-de-commande-restaurant-poster.webp"
             width="1280" height="720">
        <source src="video/borne-de-commande-restaurant.mp4" type="video/mp4">
        <p>Votre navigateur ne lit pas cette vidéo. <a href="video/borne-de-commande-restaurant.mp4">Téléchargez-la</a> pour la regarder.</p>
      </video>
      <button type="button" class="video__play" id="film-play" aria-label="Lire la vidéo de présentation">
        <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5.5v13l11-6.5z" fill="currentColor"/></svg>
        <span>Lire la présentation · 1 min 13</span>
      </button>
      <figcaption>La vidéo ne se télécharge qu’au moment où vous appuyez sur lecture.</figcaption>
    </figure>
  </div>
</section>

<section class="recit">
  <div class="env">
    <p class="surtitre" style="color:#9BA0A8">Pourquoi nous vendons ça</p>
    <h2 style="font-size:var(--t-xl)">Nous avons une usine. Et un restaurant.</h2>
    <div class="prose mt-2" data-reveal>
      <p>Les deux n’ont longtemps rien eu à voir. D’un côté une usine en Chine qui fabrique des écrans, de l’autre une salle à faire tourner, avec un service de midi qui bouchonnait au comptoir.</p>
      <p>Quand nous avons demandé des devis pour équiper cette salle, les montants allaient de 2 400 à 4 100 € par borne, plus 59 à 149 € par mois. Pour deux écrans, l’addition dépassait 13 000 € sur trois ans. Le matériel, lui, nous le connaissions : nous en fabriquons.</p>
      <p>Nous avons donc fait venir nos propres tablettes, et il est resté la vraie question, celle du logiciel. Nous avons écrit le nôtre nous-mêmes, en nous faisant assister par l’IA, et il tourne depuis dans notre salle : il prend les commandes, applique le bon taux de TVA et les envoie en cuisine. Ce n’est pas un produit, c’est un outil taillé pour notre carte, et il ne nous coûte aucune licence.</p>
      <p>Une fois les deux bornes installées et rentables, la suite s’est imposée toute seule : vendre le même matériel, au prix du matériel, à des restaurateurs qui se posaient les mêmes questions que nous.</p>
    </div>
    <div class="chiffres" data-reveal>
      <div><b>600 €</b><span>le prix du matériel, sans la couche de services qu’on vous facture ailleurs</span></div>
      <div><b>0 €</b><span>par mois, parce que nous ne vendons pas de logiciel</span></div>
      <div><b>2</b><span>bornes en service dans notre propre salle, tous les jours</span></div>
    </div>
    <p class="mt-2"><a href="logiciel-borne-de-commande-ia.html" style="color:#fff">Comment nous avons fabriqué notre logiciel avec l’IA</a></p>
  </div>
</section>

<section class="sec" id="comment">
  <div class="env">
    <p class="surtitre">Comment ça se passe</p>
    <h2 style="font-size:var(--t-xl)">De votre paiement à la borne en service</h2>
    <p class="prose mt-1">Tout se fait depuis la page de commande, sans rendez-vous, sans devis à signer et sans commercial au téléphone.</p>
    <ol class="deroule-v mt-2" role="list">
      <li data-reveal><b>Vous construisez votre borne en ligne</b><span>Votre carte, vos prix, vos photos, vos suppléments. C’est gratuit, sans compte à créer, et vous pouvez télécharger le résultat pour l’essayer avant de payer.</span></li>
      <li data-reveal><b>Vous payez 720 € TTC par carte</b><span>600 € hors taxes plus 20 % de TVA. Livraison comprise, aucun frais d’installation, aucun abonnement, aucun engagement.</span></li>
      <li data-reveal><b>Nous lançons la fabrication</b><span>La tablette part de notre atelier vers votre adresse. Vous recevez le numéro de suivi au départ du colis.</span></li>
      <li data-reveal><b>Pendant le transport, nous montons votre page</b><span>Nous reprenons votre configuration et nous la mettons en ligne, soit sur votre site, soit sur un nouveau site que nous créons pour vous.</span></li>
      <li data-reveal><b>Vous branchez, elle ouvre sur votre carte</b><span>Vous verrouillez l’écran sur cette adresse et la borne prend ses premières commandes. Comptez un quart d’heure.</span></li>
    </ol>
    <div class="avantages mt-2">
      <div data-reveal><b>720 € TTC</b><span>TVA de 20 % comprise, rien à ajouter au moment de payer</span></div>
      <div data-reveal><b>Livraison offerte</b><span>France métropolitaine, transport compris dans le prix</span></div>
      <div data-reveal><b>0 € d’installation</b><span>Nous montons votre page de borne sans frais supplémentaires</span></div>
      <div data-reveal><b>0 € par mois</b><span>Aucun abonnement, aucune commission sur vos ventes</span></div>
    </div>
    <p class="note mt-2">Seul l’hébergement de votre page reste à votre charge, parce qu’il est facturé par votre hébergeur et non par nous. Si vous n’avez pas de site, nous réservons votre nom de domaine pour 20 € par an et nous nous occupons de tout.</p>
    <p class="mt-2"><a class="btn" href="commander.html">Construire ma borne</a></p>
  </div>
</section>

<section class="sec">
  <div class="env duo">
    <div>
      <p class="surtitre">Le détail qui sert tous les jours</p>
      <h2 style="font-size:var(--t-xl)">L’écran pivote</h2>
      <p class="prose mt-1">En portrait, la borne tient dans un couloir étroit et affiche une liste de produits plus longue. En paysage, elle met en valeur des photos larges et fait un bon écran de cuisine.</p>
      <p class="prose mt-1">Vous ne saurez laquelle des deux vous convient qu’après deux semaines de service réel. Le pivot vous évite de trancher au moment de la commande, et de le regretter.</p>
      <p class="mt-1"><a href="installer-borne-de-commande-restaurant.html">Où poser la borne et comment la brancher</a></p>
    </div>
    <figure class="photo" data-reveal>
      <img src="img/borne-de-commande-restaurant-rotation-1000.webp"
           srcset="img/borne-de-commande-restaurant-rotation-600.webp 600w, img/borne-de-commande-restaurant-rotation-1000.webp 1000w"
           sizes="(max-width: 48rem) 100vw, 30rem"
           width="1000" height="1000" loading="lazy" decoding="async"
           alt="L’écran de la borne pivotant entre la position paysage et la position portrait sur son support">
      <figcaption>Le pivot se manœuvre à la main, sans outil, pendant le service.</figcaption>
    </figure>
  </div>
</section>

<section class="sec sec--alt">
  <div class="env duo">
    <div>
      <p class="surtitre">Le carton</p>
      <h2 style="font-size:var(--t-xl)">Ce que vous recevez</h2>
      <p class="prose mt-1">La borne arrive montée. Vous sortez le socle du carton, vous vissez la colonne, vous allumez. Comptez un quart d’heure, sans outil particulier.</p>
      <ul class="inclus mt-2" role="list">
        <li>La borne assemblée, écran monté sur sa colonne et son socle lesté</li>
        <li>Le bloc d’alimentation et le câble secteur en 220 V</li>
        <li>La visserie de fixation au sol, si vous préférez la sceller</li>
        <li>Un guide de branchement en français, sur papier</li>
      </ul>
      <p class="surtitre mt-2">Ce qui n’est pas dans le carton</p>
      <ul class="inclus exclus mt-1" role="list">
        <li>Le logiciel de prise de commande, que vous choisissez vous-même</li>
        <li>L’imprimante à tickets et le terminal de paiement</li>
        <li>Le câble réseau, si vous branchez en Ethernet plutôt qu’en Wi-Fi</li>
      </ul>
      <p class="note mt-1">Nous préférons l’écrire ici plutôt que vous le laisser découvrir à la livraison.</p>
    </div>
    <div>
      <figure class="photo" data-reveal>
        <img src="img/borne-de-commande-restaurant-ecran-portrait-1000.webp"
             srcset="img/borne-de-commande-restaurant-ecran-portrait-600.webp 600w, img/borne-de-commande-restaurant-ecran-portrait-1000.webp 1000w"
             sizes="(max-width: 48rem) 100vw, 30rem"
             width="1000" height="1000" loading="lazy" decoding="async"
             alt="La borne de commande en position portrait, écran vertical allumé sur l’accueil Android">
      </figure>
      <div class="cadre-defil mt-1">
        <table class="tbl">
          <caption>Fiche technique</caption>
          <tbody>
            <tr><th scope="row">Écran</th><td class="avf">tactile capacitif, verre trempé</td></tr>
            <tr><th scope="row">Diagonale</th><td class="avf">21,5″</td></tr>
            <tr><th scope="row">Définition</th><td class="avf">1920 × 1080</td></tr>
            <tr><th scope="row">Orientation</th><td class="txt">paysage ou portrait, pivot manuel</td></tr>
            <tr><th scope="row">Système</th><td class="txt">Android ouvert, verrouillable en mode kiosque</td></tr>
            <tr><th scope="row">Applications</th><td class="txt">Play Store accessible, navigateur inclus</td></tr>
            <tr><th scope="row">Batterie</th><td class="avf">intégrée</td></tr>
            <tr><th scope="row">Réseau</th><td class="avf">Wi-Fi, Ethernet par adaptateur</td></tr>
            <tr><th scope="row">Caméra</th><td class="txt">frontale, désactivable</td></tr>
            <tr><th scope="row">Hauteur totale</th><td class="avf">≈ 1 100 mm</td></tr>
            <tr><th scope="row">Socle</th><td class="avf">rond lesté, ≈ 400 mm</td></tr>
            <tr><th scope="row">Finition</th><td class="txt">blanc mat</td></tr>
            <tr><th scope="row">Alimentation</th><td>220 V, prise standard</td></tr>
          </tbody>
        </table>
      </div>
      <p class="note mt-1">Les valeurs marquées « à confirmer » viennent de la fiche fabricant et seront remplacées par nos mesures sur exemplaire.</p>
      <div class="prose mt-2">
        <h3 style="font-size:var(--t-md)">Ce que c’est, précisément</h3>
        <p>Un écran tactile de bureau monté sur une colonne et un socle rond lesté, le tout en blanc mat. L’écran se démonte de sa colonne et pivote à la main entre paysage et portrait, grâce à une rotule visible sur la photo.</p>
        <p>À l’intérieur, un appareil Android complet : Play Store accessible, navigateur, Wi-Fi, caméra frontale désactivable et batterie intégrée. Ce n’est donc pas un écran passif branché sur un ordinateur, c’est un appareil autonome qui démarre seul sur la page que vous lui désignez.</p>
        <p>Cette ouverture est le point important. Un écran verrouillé par son fabricant ne sert qu’avec le logiciel du fabricant, et s’éteint le jour où vous arrêtez de payer. Celui-ci accepte n’importe quelle application Android, y compris celle de votre éditeur de caisse, et la page que nous montons pour vous.</p>
        <h3 style="font-size:var(--t-md)">Ce qu’il sait faire au-delà de la prise de commande</h3>
        <p>Posé en paysage près de la cuisine, il affiche les commandes à préparer. En portrait dans une vitrine, il sert d’affichage de carte ou de promotion. Branché sur rien du tout, il reste une tablette de travail pour l’équipe.</p>
        <p>La batterie change la façon de l’installer : vous le déplacez en terrasse à midi, vous le rentrez le soir, et vous évitez la rallonge qui traverse un passage, qui est en pratique la première cause de chute dans un établissement recevant du public.</p>
      </div>
    </div>
  </div>
</section>

<section class="sec">
  <div class="env">
    <p class="surtitre">Le point qui fâche</p>
    <h2 style="font-size:var(--t-xl)">Le logiciel n’est pas fourni, et c’est voulu</h2>
    <div class="prose mt-1">
      <p>Un restaurateur qui achète une borne se retrouve souvent avec un abonnement dont il ne peut plus sortir, parce que le logiciel et le matériel sont vendus ensemble. Le jour où il arrête de payer, l’écran qu’il croyait avoir acheté s’éteint.</p>
      <p>Nous vendons l’écran seul. Il arrive sous Android ouvert : vous y installez l’application de commande que vous voulez, y compris celle de votre éditeur de caisse s’il en propose une, et vous la verrouillez en mode kiosque pour que le client ne puisse pas en sortir.</p>
      <h3>Et la conformité à la loi anti-fraude à la TVA ?</h3>
      <p>Elle dépend de votre logiciel d’encaissement, pas de l’écran sur lequel il tourne. L’attestation prévue à l’article 286-I-3° bis du code général des impôts vous est délivrée par l’éditeur de votre caisse. Un vendeur de matériel qui vous promet cette conformité avec un simple écran vous raconte une histoire.</p>
    </div>
    <p class="mt-2">
      <a href="borne-de-commande-ou-caisse-enregistreuse.html">Borne ou caisse : ce que chacune fait</a> ·
      <a href="guide-borne-de-commande-restaurant.html">Le guide d’achat complet</a>
    </p>
  </div>
</section>

<section class="sec sec--alt">
  <div class="env">
    <p class="surtitre">Comparaison</p>
    <h2 style="font-size:var(--t-xl)">Borne, tablette au comptoir ou QR code&nbsp;?</h2>
    <p class="prose mt-1">Trois manières de faire passer une commande sans mobiliser quelqu’un en caisse. Elles ne servent pas les mêmes situations.</p>
    <div class="cadre-defil mt-2">
      <table class="tbl compare">
        <caption>Ce que chaque solution sait faire</caption>
        <thead>
          <tr><th scope="col">&nbsp;</th><th scope="col">Borne sur pied</th><th scope="col">Tablette au comptoir</th><th scope="col">QR code à table</th></tr>
        </thead>
        <tbody>
          <tr><th scope="row">Visible depuis la rue</th><td class="oui">oui</td><td class="non">non</td><td class="non">non</td></tr>
          <tr><th scope="row">Marche sans smartphone du client</th><td class="oui">oui</td><td class="oui">oui</td><td class="non">non</td></tr>
          <tr><th scope="row">Absorbe la file de 12 h 30</th><td class="oui">oui</td><td class="txt">un peu</td><td class="non">non</td></tr>
          <tr><th scope="row">Sert la vente à emporter</th><td class="oui">oui</td><td class="oui">oui</td><td class="non">non</td></tr>
          <tr><th scope="row">Sert le service à table</th><td class="non">non</td><td class="non">non</td><td class="oui">oui</td></tr>
          <tr><th scope="row">Coût de départ</th><td>600 € HT</td><td class="txt">200 à 600 €</td><td class="txt">quasi nul</td></tr>
          <tr><th scope="row">Abonnement</th><td class="oui">aucun</td><td class="txt">celui de votre logiciel</td><td class="txt">souvent mensuel</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

<section class="sec" id="prix">
  <div class="env">
    <p class="surtitre">Tarifs</p>
    <h2 style="font-size:var(--t-xl)">Le prix baisse à partir de deux bornes</h2>
    <div class="cadre-defil mt-2">
      <table class="tbl">
        <caption>Prix unitaire selon la quantité</caption>
        <thead><tr><th scope="col">Quantité</th><th scope="col">Prix unitaire HT</th><th scope="col">Prix unitaire TTC</th><th scope="col">Total HT</th></tr></thead>
        <tbody>
          <tr><th scope="row">1 borne</th><td>600,00 €</td><td>720,00 €</td><td>600,00 €</td></tr>
          <tr><th scope="row">2 bornes</th><td>570,00 €</td><td>684,00 €</td><td>1 140,00 €</td></tr>
          <tr><th scope="row">3 bornes et plus</th><td>540,00 €</td><td>648,00 €</td><td>1 620,00 €</td></tr>
        </tbody>
      </table>
    </div>
    <p class="note mt-1">Deux options au moment de la commande : la mise en service à distance à 149 € HT, où nous installons et paramétrons votre application en visio, et l’extension de garantie à 3 ans à 79 € HT par borne.</p>
    <p class="mt-2"><a class="btn" href="commander.html">Configurer ma commande</a></p>
  </div>
</section>

<section class="sec sec--alt">
  <div class="env">
    <p class="surtitre">Le blog</p>
    <h2 style="font-size:var(--t-xl)">Ce qu’on a appris en équipant notre propre salle</h2>
    <p class="prose mt-1">Prix réels du marché, choix du matériel, logiciel, implantation. Écrit depuis un restaurant, pas depuis un service commercial.</p>
    <div class="blog-grille mt-2">{DERNIERS_ARTICLES}</div>
    <p class="mt-2"><a class="btn btn--secondaire" href="blog.html">Tous les articles</a></p>
  </div>
</section>

<section class="sec">
  <div class="env">
    <p class="surtitre">Questions</p>
    <h2 style="font-size:var(--t-xl)">Ce qu’on nous demande avant d’acheter</h2>
    <div class="mt-2" style="max-width:var(--mesure)">
      <details><summary>Le logiciel de commande est-il fourni avec la borne&nbsp;?</summary><p class="rep">Non. La borne est un écran tactile sous Android ouvert, verrouillable en mode kiosque. Vous y installez l’application de commande de votre choix, y compris celle de votre éditeur de caisse. Si vous préférez qu’on s’en occupe, la mise en service à distance coûte 149 € HT et se fait en visio.</p></details>
      <details><summary>Y a-t-il un abonnement&nbsp;?</summary><p class="rep">Aucun. Vous payez la borne une fois et elle vous appartient. Si votre logiciel de commande est facturé au mois, cet abonnement reste entre votre éditeur et vous. Le jour où vous cessez de nous parler, la borne continue de fonctionner.</p></details>
      <details><summary>Sous combien de temps suis-je livré&nbsp;?</summary><p class="rep">Quatre à sept jours ouvrés en France métropolitaine, transport compris dans le prix. Vous recevez le numéro de suivi dès le départ du colis. Pour la Corse et l’outre-mer, écrivez-nous avant de commander, le transport est chiffré au cas par cas.</p></details>
      <details><summary>Est-ce que ça marche avec ma caisse&nbsp;?</summary><p class="rep">La question porte sur votre logiciel, pas sur l’écran. Dites-nous lequel vous utilisez, nous vous dirons s’il existe une application Android compatible et ce qu’elle sait remonter. Nous préférons vous répondre non avant la vente plutôt qu’après.</p></details>
      <details><summary>La batterie tient-elle un service complet&nbsp;?</summary><p class="rep">Elle est prévue pour, mais l’autonomie dépend de la luminosité et de l’usage. En pratique, la plupart des établissements laissent la borne branchée en permanence et se servent de la batterie pour la déplacer sans couper le service, ou pour éviter une rallonge dans un passage.</p></details>
      <details><summary>Et si elle tombe en panne&nbsp;?</summary><p class="rep">La garantie couvre deux ans, pièces et main-d’œuvre. Vous appelez, on diagnostique par téléphone, et si le matériel doit revenir, l’étiquette de retour vous est envoyée. Comme votre caisse continue de fonctionner, une borne en panne ralentit le service sans l’arrêter.</p></details>
    </div>
  </div>
</section>

<section class="sec">
  <div class="env rappel carte">
    <figure class="photo">
      <img src="img/borne-de-commande-restaurant-ecran-portrait-600.webp" width="600" height="600" loading="lazy" decoding="async"
           alt="Borne de commande pour restaurant, vue d’ensemble">
    </figure>
    <div>
      <h2 style="font-size:var(--t-lg)">Borne de commande sur pied</h2>
      <p class="note mt-1">600 € HT, sans abonnement, livraison offerte, garantie 2 ans. Paiement par carte, virement possible sur demande.</p>
    </div>
    <a class="btn" href="commander.html">Commander</a>
  </div>
</section>

</main>

<div class="barre-mobile">
  <span class="prix">720,00 € TTC</span>
  <a class="btn btn--petit" href="commander.html">Commander</a>
</div>
"""


_derniers = sorted(ARTICLES, key=lambda x: x["date"], reverse=True)[:3]
CORPS_INDEX = CORPS_INDEX.replace("{DERNIERS_ARTICLES}", "".join(
    f'''<article class="blog-carte" data-reveal>
      <h2><a href="{a["slug"]}.html">{a["h1"]}</a></h2>
      <p>{a["accroche"]}</p>
      <p class="meta">{a["lecture"]} min de lecture</p>
    </article>''' for a in _derniers))

# ==========================================================================
# 2. Commander : le configurateur, dernier écran avant Stripe.
# ==========================================================================
CORPS_COMMANDER = fil([("Accueil", "index.html"), ("Commander", None)]) + """
<main id="contenu" class="env sec" style="padding-top:var(--pas)">
  <p class="surtitre">Commande</p>
  <h1 style="font-size:var(--t-2xl)">Configurez votre borne, puis payez</h1>
  <p class="prose mt-1">Vous construisez votre écran de commande ici, gratuitement et sans créer de compte. Vous pouvez même le télécharger pour l’essayer avant de payer quoi que ce soit.</p>

  <div class="carte mt-2" data-reveal>
    <h2 style="font-size:var(--t-lg)">Comment se passe la vente</h2>
    <ol class="deroule" role="list">
      <li><div><b>Vous configurez votre borne sur cette page</b><span>Votre carte, vos prix, vos photos. Rien n’est envoyé nulle part tant que vous n’avez pas payé.</span></div></li>
      <li><div><b>Vous payez 720 € TTC par carte</b><span>600 € hors taxes plus 20 % de TVA. Livraison comprise, aucun frais d’installation, aucun abonnement.</span></div></li>
      <li><div><b>Nous lançons la commande à notre usine</b><span>La tablette part de notre atelier en Chine vers votre adresse. Vous recevez le numéro de suivi au départ.</span></div></li>
      <li><div><b>Pendant le transport, nous montons votre page de borne</b><span>Nous reprenons votre configuration, nous la mettons en ligne, et nous vous envoyons l’adresse à ouvrir sur la tablette.</span></div></li>
      <li><div><b>Vous branchez, elle ouvre sur votre carte</b><span>Vous verrouillez l’écran sur cette page et la borne est en service. Comptez un quart d’heure.</span></div></li>
    </ol>
  </div>

  <form class="config mt-2" id="configurateur" novalidate>
    <div>

      <!-- ============ 1. Matériel ============ -->
      <section class="etape">
        <div class="etape__tete"><span class="etape__num">1</span><h2>Votre matériel</h2></div>
        <fieldset class="carte mt-1">
          <legend class="surtitre" style="padding:0 0 .6rem">Quantité</legend>
          <div style="display:flex;align-items:center;gap:1rem;flex-wrap:wrap">
            <div class="compteur">
              <button type="button" data-qte="-1" aria-label="Retirer une borne">−</button>
              <output id="qte-valeur" aria-live="polite">1</output>
              <button type="button" data-qte="1" aria-label="Ajouter une borne">+</button>
            </div>
            <p class="note" style="max-width:26rem">600 € HT l’unité, 570 € à partir de deux bornes, 540 € à partir de trois. La remise s’applique toute seule.</p>
          </div>
        </fieldset>

        <fieldset class="mt-2">
          <legend class="surtitre" style="padding:0 0 .6rem">Options</legend>
          <div style="display:grid;gap:.7rem">
            <label class="option">
              <input type="checkbox" id="opt-mise-en-service">
              <span>
                <span class="titre-opt">Mise en service à distance</span>
                <span class="desc-opt">Une heure en visio : nous installons votre page de borne sur la tablette, nous la verrouillons en mode kiosque et nous formons la personne qui s’en occupera.</span>
              </span>
              <span class="prix">149 € HT</span>
            </label>
            <label class="option">
              <input type="checkbox" id="opt-garantie">
              <span>
                <span class="titre-opt">Extension de garantie à 3 ans</span>
                <span class="desc-opt">Un an de garantie contractuelle supplémentaire, sur les mêmes pièces et la même main-d’œuvre. Facturée par borne.</span>
              </span>
              <span class="prix">79 € HT</span>
            </label>
          </div>
        </fieldset>
      </section>

      <!-- ============ 2. La borne ============ -->
      <section class="etape">
        <div class="etape__tete"><span class="etape__num">2</span><h2>Votre borne</h2></div>
        <p class="note mt-1">Modifiez la carte de démonstration ou repartez de zéro. <span id="cfg-compte"></span></p>

        <div class="onglets" role="tablist">
          <button type="button" role="tab" data-onglet="enseigne" aria-selected="true">Enseigne</button>
          <button type="button" role="tab" data-onglet="carte" aria-selected="false">Carte et prix</button>
          <button type="button" role="tab" data-onglet="images" aria-selected="false">Photos</button>
          <button type="button" role="tab" data-onglet="apercu" aria-selected="false">Aperçu</button>
        </div>
        <p id="cfg-erreur" hidden></p>

        <div data-panneau="enseigne" id="cfg-enseigne">
          <div class="ens-grille">
            <label class="champ"><span>Nom affiché sur la borne</span>
              <input type="text" id="ens-nom" placeholder="Le Comptoir 22" autocomplete="organization">
            </label>
            <label class="champ"><span>Type d’établissement</span>
              <select id="ens-type">
                <option>Restauration rapide</option>
                <option>Kebab</option>
                <option>Pizzeria</option>
                <option>Burger</option>
                <option>Boulangerie</option>
                <option>Brasserie</option>
                <option>Snack</option>
                <option>Food truck</option>
                <option>Autre</option>
              </select>
            </label>
            <label class="champ"><span>Couleur principale</span>
              <input type="color" id="ens-couleur" value="#D4321C">
            </label>
            <div class="champ"><span>Logo</span>
              <div class="ens-logo">
                <div id="ens-logo-apercu"></div>
                <div>
                  <label class="btn btn--secondaire btn--petit" style="cursor:pointer">Choisir un fichier
                    <input type="file" id="ens-logo" accept="image/*" hidden>
                  </label>
                  <button type="button" class="lien-sup" id="ens-logo-sup">Retirer</button>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div data-panneau="carte" hidden>
          <div id="cfg-carte"></div>
          <button type="button" class="btn btn--secondaire btn--petit" id="add-cat">Ajouter une catégorie</button>

          <h3 class="mt-2" style="font-size:var(--t-md)">Suppléments proposés à chaque produit</h3>
          <p class="note">C’est ce qui fait monter le panier. L’écran les propose à chaque commande, sans jamais les oublier.</p>
          <div id="cfg-supplements" class="mt-1"></div>
          <button type="button" class="btn btn--secondaire btn--petit" id="add-supp">Ajouter un supplément</button>
        </div>

        <div data-panneau="images" hidden>
          <p class="prose">Les photos se chargent depuis l’onglet « Carte et prix » : touchez le carré gris à gauche de chaque produit. Elles sont redimensionnées dans votre navigateur et intégrées au fichier de la borne, donc elle fonctionne même sans connexion.</p>
          <ul class="inclus mt-1" role="list">
            <li>Format carré, recadrage automatique au centre</li>
            <li>Une photo par produit, aucune limite de nombre</li>
            <li>Vos fichiers ne quittent pas votre ordinateur tant que vous n’avez pas payé</li>
            <li>Pas de photo sous la main ? La borne affiche le nom et le prix, et vous les ajouterez plus tard</li>
          </ul>
          <p class="note mt-1">Nous reprenons ces mêmes photos pour monter votre page en ligne. Si vous préférez nous envoyer les originaux en haute définition, écrivez-nous après la commande.</p>
        </div>

        <div data-panneau="apercu" hidden>
          <p class="prose">Essayez votre borne comme le fera votre client, puis téléchargez le fichier. Il fonctionne seul, sur n’importe quelle tablette, sans internet.</p>
          <div class="generer-ligne">
            <button type="button" class="btn btn--secondaire" id="apercu">Voir l’aperçu</button>
            <button type="button" class="btn" id="generer">Télécharger ma borne</button>
            <button type="button" class="lien-sup" id="reinit">Repartir de la démonstration</button>
          </div>
          <p id="generer-ok" hidden>Fichier téléchargé. Ouvrez-le dans un navigateur pour le tester.</p>
          <iframe id="apercu-cadre" title="Aperçu de votre borne de commande" hidden></iframe>
        </div>
      </section>

      <!-- ============ 3. Site ============ -->
      <section class="etape" id="cfg-site">
        <div class="etape__tete"><span class="etape__num">3</span><h2>Où votre borne sera hébergée</h2></div>
        <p class="prose mt-1">Votre page de borne doit vivre à une adresse que la tablette ouvre au démarrage. Deux solutions, au choix.</p>

        <div class="solutions mt-1">
          <label class="solution">
            <input type="radio" name="solution" value="existant">
            <span>
              <b>Je l’installe sur mon site</b>
              <span class="d">Vous avez déjà un site. Nous vous livrons le fichier et l’adresse à créer, vous le déposez chez votre hébergeur. Aucun frais supplémentaire.</span>
            </span>
          </label>
          <label class="solution">
            <input type="radio" name="solution" value="nouveau" checked>
            <span>
              <b>Je n’ai pas de site, créez-le-moi</b>
              <span class="d">Nous montons la page et la mettons en ligne. Vous ne payez que l’hébergement et le nom de domaine, directement au prestataire ou par nous.</span>
            </span>
          </label>
        </div>

        <div id="bloc-domaine" class="carte mt-2">
          <h3 style="font-size:var(--t-md)">Votre nom de domaine</h3>
          <p class="note mt-1">Nous le réservons et nous nous occupons de tout pour <strong>20 € par an</strong>. Vérifiez d’abord qu’il est libre.</p>
          <div class="dom-ligne mt-1">
            <label class="champ"><span>Nom souhaité, avec son extension</span>
              <input type="text" id="dom-nom" placeholder="mon-restaurant.fr" autocomplete="off" spellcheck="false">
            </label>
            <button type="button" class="btn btn--secondaire" id="dom-verifier">Vérifier</button>
          </div>
          <p class="dom-rep" id="dom-reponse"></p>
          <p class="note">La réponse vient du registre du domaine, pas d’une estimation. Si le registre ne répond pas, nous vérifions à la main au moment de la commande et nous vous prévenons.</p>
        </div>
      </section>

      <!-- ============ 4. Coordonnées ============ -->
      <section class="etape">
        <div class="etape__tete"><span class="etape__num">4</span><h2>Vos coordonnées</h2></div>
        <div style="display:grid;gap:.9rem;max-width:30rem" class="mt-1">
          <label class="champ"><span>Nom de l’établissement</span>
            <input type="text" id="client-etablissement" name="etablissement" autocomplete="organization" placeholder="Le Comptoir 22, Saint-Brieuc">
          </label>
          <label class="champ"><span>Adresse e-mail</span>
            <input type="email" id="client-email" name="email" autocomplete="email" placeholder="vous@votre-restaurant.fr">
          </label>
          <p class="note">Ces deux champs pré-remplissent la page de paiement et nous permettent de rattacher votre configuration de borne à votre commande. L’adresse de livraison, la raison sociale et l’éventuel numéro de TVA se saisissent à l’étape suivante, sur la page sécurisée de Stripe.</p>
        </div>
      </section>
    </div>

    <aside class="config__recap">
      <div class="carte">
        <figure class="photo" style="margin-bottom:var(--pas)">
          <img src="img/borne-de-commande-restaurant-ecran-portrait-600.webp" width="600" height="600" loading="lazy" decoding="async"
               alt="La borne de commande sur son pied, écran vertical">
        </figure>

        <h2 style="font-size:var(--t-lg)">Récapitulatif</h2>
        <p id="resume-borne" class="mt-1"></p>
        <div class="recap__lignes" id="recap-lignes"></div>
        <div class="recap__total">
          <span>Montant autorisé</span>
          <span class="prix" id="recap-total-ttc">720,00 €</span>
        </div>
        <p class="note" style="text-align:right;margin-top:.3rem"><span id="recap-total-ht">600,00 €</span> HT · TVA 20 % · livraison offerte</p>

        <label class="option mt-1" style="grid-template-columns:auto 1fr">
          <input type="checkbox" id="accepte-cgv">
          <span class="desc-opt">J’ai lu et j’accepte les <a href="cgv.html">conditions générales de vente</a>, y compris les modalités de livraison et de retour.</span>
        </label>

        <p class="note mt-1" id="note-paiement"><strong>Rien n’est débité aujourd’hui.</strong> Votre carte est autorisée : votre banque bloque le montant, et nous le prélevons à la confirmation de votre commande. Si nous ne confirmons pas, le blocage est levé et vous ne payez rien.</p>

        <button class="btn btn--large mt-1" id="aller-au-paiement" type="button" disabled>Autoriser le paiement</button>
        <p class="erreur mt-1" id="erreur-paiement" hidden></p>

        <ul class="garanties mt-1" role="list">
          <li><svg aria-hidden="true"><use href="#i-check"/></svg><span><strong>Livraison offerte</strong>, aucun frais d’installation</span></li>
          <li><svg aria-hidden="true"><use href="#i-check"/></svg><span><strong>0 € par mois</strong>, aucun engagement</span></li>
          <li><svg aria-hidden="true"><use href="#i-check"/></svg><span>TVA 20 % comprise dans le prix affiché</span></li>
          <li><svg aria-hidden="true"><use href="#i-check"/></svg><span><strong>Carte autorisée, pas débitée</strong> : le prélèvement vient à la confirmation</span></li>
          <li><svg aria-hidden="true"><use href="#i-check"/></svg><span>Paiement traité par Stripe, aucune donnée bancaire sur ce site</span></li>
          <li><svg aria-hidden="true"><use href="#i-check"/></svg><span>Facture envoyée par e-mail après le prélèvement</span></li>
        </ul>

        <p class="note mt-1">Vous préférez payer par virement, ou vous avez besoin d’un devis pour votre comptable&nbsp;? Écrivez à <a data-mail href="mailto:contact@bornea.fr">contact@bornea.fr</a> ou appelez le <a data-tel href="tel:+33296000000">02 96 00 00 00</a>.</p>
      </div>
    </aside>
  </form>

  <!-- Récitation. Masquée tant que le script n'a pas vérifié que le fichier
       existe, pour ne pas afficher un bouton qui ne joue rien. -->
  <div class="ecoute" id="ecoute" hidden>
    <audio id="ecoute-audio" preload="auto" loop playsinline></audio>
    <span class="ecoute__titre">Récitation du Coran</span>
    <button type="button" class="ecoute__btn" id="ecoute-btn" aria-pressed="false" aria-label="Écouter la récitation">
      <svg aria-hidden="true"><use id="ecoute-icone" href="#i-son-coupe"/></svg>
    </button>
  </div>
</main>
"""

# ==========================================================================
# 3. Retour de Stripe
# ==========================================================================
CORPS_MERCI = """
<main id="contenu" class="env-etroite confirme">
  <p class="pastille"><svg aria-hidden="true"><use href="#i-check"/></svg></p>
  <h1>Commande enregistrée</h1>
  <p>Votre carte est autorisée : le montant est bloqué par votre banque, il n’est pas encore prélevé. Vous recevez la confirmation par e-mail dans les minutes qui viennent.</p>
  <p>Nous contrôlons votre commande, puis nous déclenchons le prélèvement et nous vous envoyons la facture. Si nous ne pouvions pas honorer la commande, le blocage serait levé et vous n’auriez rien payé.</p>
  <p id="ref-commande" hidden class="note">Référence de paiement : <code class="prix" id="ref-valeur"></code></p>

  <div class="carte mt-2" style="text-align:left">
    <h2 style="font-size:var(--t-lg)">La suite, dans l’ordre</h2>
    <ol class="prose" style="padding-left:1.2rem;margin-top:.8rem">
      <li>Nous préparons la borne et vous envoyons le numéro de suivi au départ du colis, sous 4 à 7 jours ouvrés.</li>
      <li>À la livraison, vérifiez le carton devant le transporteur. Si l’emballage est enfoncé, écrivez la réserve sur le bordereau : sans cette mention, un recours transport devient difficile.</li>
      <li>Vous vissez la colonne sur le socle, vous branchez, l’écran démarre.</li>
      <li>Si vous avez pris la mise en service à distance, nous vous appelons pour caler le rendez-vous en visio.</li>
    </ol>
  </div>

  <p class="mt-2">Une question sur la commande&nbsp;? Appelez le <a data-tel href="tel:+33296000000">02 96 00 00 00</a> ou écrivez à <a data-mail href="mailto:contact@bornea.fr">contact@bornea.fr</a>.</p>
  <p class="mt-1"><a class="btn btn--secondaire" href="index.html">Revenir à l’accueil</a></p>
</main>
"""

CORPS_ANNULE = """
<main id="contenu" class="env-etroite confirme">
  <h1>Paiement interrompu</h1>
  <p>Rien n’a été débité et votre configuration n’a pas été perdue. Vous pouvez reprendre là où vous en étiez.</p>
  <p class="mt-2">
    <a class="btn" href="commander.html">Reprendre la commande</a>
  </p>
  <div class="carte mt-2" style="text-align:left">
    <h2 style="font-size:var(--t-lg)">Si quelque chose a coincé</h2>
    <p class="note mt-1">Une carte refusée vient le plus souvent du plafond de paiement de la carte professionnelle. Votre banque peut le relever pour la journée. Nous acceptons aussi le virement : demandez la facture proforma à <a data-mail href="mailto:contact@bornea.fr">contact@bornea.fr</a> et la borne part dès réception des fonds.</p>
  </div>
</main>
"""

# ==========================================================================
# 4. Guide d'achat : la page de fond, écrite pour la requête d'information
#    et pour être citable telle quelle par un moteur de réponse.
# ==========================================================================
CORPS_GUIDE = fil([("Accueil", "index.html"), ("Guide d’achat", None)]) + """
<main id="contenu" class="env sec" style="padding-top:var(--pas)">
  <div style="max-width:46rem">
    <p class="surtitre">Guide d’achat, mis à jour en 2026</p>
    <h1 style="font-size:var(--t-2xl)">Bien choisir une borne de commande pour son restaurant</h1>
    <p class="chapo prose" style="max-width:38ch;font-size:clamp(1.125rem,1rem+.6vw,1.4375rem);line-height:1.5;margin-top:1rem">Ce qu’il faut regarder avant d’acheter, ce que les vendeurs passent sous silence, et le calcul qui dit si ça vaut le coup chez vous.</p>

    <div class="encadre-cle mt-2">
      <h2>Les réponses courtes</h2>
      <dl>
        <div><dt>Prix d’une borne</dt><dd>400 à 3 500 € selon le format</dd></div>
        <div><dt>Ce qui coûte cher</dt><dd>le logiciel, souvent au mois</dd></div>
        <div><dt>Format le plus courant</dt><dd>écran vertical sur pied, 1,3 à 1,5 m</dd></div>
        <div><dt>Nombre de bornes</dt><dd>une par tranche de 60 à 80 commandes au pic</dd></div>
        <div><dt>Conformité fiscale</dt><dd>elle dépend du logiciel, pas de l’écran</dd></div>
      </dl>
    </div>

    <div class="prose mt-2">
      <p>Une borne de commande, dans un restaurant, ne sert pas à faire moderne. Elle sert à retirer du travail au comptoir pendant les cinquante minutes où tout le monde arrive en même temps. Si votre service ne connaît pas ce pic, vous n’en avez probablement pas besoin, et aucun vendeur ne vous le dira.</p>

      <h2>Ce qu’une borne fait, et ce qu’elle ne fait pas</h2>
      <p>Elle fait trois choses concrètes. Elle prend une commande sans mobiliser quelqu’un. Elle propose systématiquement les suppléments, ce qu’une équipe débordée cesse de faire vers 12 h 40. Elle donne au client le temps de lire la carte en entier, ce qui augmente mécaniquement le panier chez la plupart des enseignes qui publient leurs chiffres.</p>
      <p>Elle ne fait pas le reste. Elle ne remplace pas votre caisse, qui reste le point de vérité de votre chiffre d’affaires. Elle ne prend pas le service à table. Elle ne règle pas un problème de cuisine : si vos temps de production sont le goulot, une borne ne fera qu’accumuler des commandes plus vite devant une plancha déjà saturée. Dans ce cas précis, elle dégrade même l’expérience, parce que le client qui a commandé en trente secondes attend ensuite douze minutes et le vit mal.</p>
      <p>Le test simple : allez regarder votre salle à 12 h 25. Si la file dépasse quatre personnes pendant que la cuisine sort les plats sans retard, la borne va vous servir. Si les plats sortent en retard alors que la file est courte, achetez autre chose.</p>

      <h2>Les quatre formats, et lequel prendre</h2>
      <h3>La borne sur pied</h3>
      <p>Un écran vertical monté sur une colonne, avec un socle lesté, entre 1,30 m et 1,50 m de haut. C’est le format le plus vendu parce qu’il se voit depuis la rue et qu’il crée un point d’attente distinct du comptoir. Il demande environ 0,4 m² au sol, plus un dégagement devant. Comptez 400 à 1 500 € pour le matériel seul.</p>
      <h3>La borne murale</h3>
      <p>Le même écran, fixé au mur. Elle libère le sol, ce qui compte dans une salle étroite, mais elle impose une hauteur unique, donc un compromis entre un adulte debout et une personne en fauteuil. Prévoyez l’axe de l’écran autour de 1,10 m et une commande accessible entre 0,90 m et 1,30 m.</p>
      <h3>La borne de comptoir</h3>
      <p>Un écran sur une platine posée ou vissée sur le comptoir. Bon marché, discrète, mais elle recrée la file au même endroit et n’apporte donc pas grand-chose sur le débit. Elle a du sens en boulangerie, où le comptoir est long et le passage rapide.</p>
      <h3>La borne extérieure</h3>
      <p>Écran renforcé, luminosité élevée, étanchéité. Utile pour un drive ou une terrasse fermée. Le prix change d’échelle, autour de 2 500 à 3 500 €, et l’installation demande une alimentation protégée. À réserver aux cas où le passage extérieur est réel.</p>

      <h2>Ce qu’il faut regarder sur l’écran</h2>
      <p>La diagonale intéresse moins que trois autres points. La luminosité d’abord : sous 300 cd/m², un écran placé face à une vitrine devient illisible entre mai et septembre. Visez 350 cd/m² si la lumière du jour tombe dessus.</p>
      <p>Le verre ensuite. Une dalle protégée par un verre trempé de 4 mm encaisse un coup de plateau, une dalle nue non. C’est le premier poste de casse en restauration rapide, avant même la panne électronique.</p>
      <p>Le comportement du tactile enfin. Vos clients toucheront l’écran avec des doigts gras. Un tactile capacitif correct ne s’en soucie pas, un tactile bas de gamme commence à rater des appuis au bout de six mois. Si vous pouvez essayer une borne avant d’acheter, appuyez avec le pouce mouillé : c’est un test plus utile qu’une fiche technique.</p>

      <h2>Le logiciel, c’est là que se joue la facture</h2>
      <p>Beaucoup de restaurateurs comparent le prix des écrans et découvrent l’abonnement après. Une borne vendue 1 200 € avec un logiciel à 89 € par mois coûte 4 400 € sur trois ans. Une borne à 600 € avec une application déjà comprise dans votre logiciel de caisse coûte 600 €. La différence ne se voit pas sur la page produit.</p>
      <p>Trois configurations existent. Soit votre éditeur de caisse propose déjà une application de borne, et vous n’avez besoin que du matériel. Soit vous prenez un logiciel de borne indépendant, qui se branche sur votre caisse par une interface, avec un abonnement à la clé. Soit le fabricant vous vend un ensemble fermé, où le matériel ne sert à rien sans son logiciel : c’est le cas le plus confortable au départ et le plus difficile à quitter ensuite.</p>
      <p>Avant de signer, posez une question précise à votre éditeur de caisse : « avez-vous une application de prise de commande qui tourne sur une tablette Android, et à quelles conditions ? » La réponse détermine tout le reste.</p>

      <h2>Caisse, TVA et obligations légales</h2>
      <p>Une confusion revient souvent, entretenue par certains vendeurs. La conformité à la loi anti-fraude à la TVA, celle qui impose un logiciel d’encaissement inaltérable et une attestation au titre de l’article 286-I-3° bis du code général des impôts, porte sur le logiciel qui enregistre les règlements. Elle ne porte pas sur l’écran. Un fabricant de matériel ne peut pas vous délivrer cette attestation, et s’il vous la promet, demandez-lui de l’écrire sur le devis.</p>
      <p>Deuxième point : le taux de TVA. En restauration, la vente à consommer sur place relève de 10 % et la vente à emporter de produits destinés à une consommation immédiate relève elle aussi de 10 %, tandis que les produits à emporter conditionnés pour être conservés relèvent de 5,5 %. C’est votre logiciel qui doit poser la question et appliquer le bon taux ligne à ligne. Si vous vendez les deux, vérifiez que l’application de la borne sait le faire avant de l’installer, sinon vous récupérerez le problème au moment du bilan.</p>
      <p>Troisième point : les allergènes. Le règlement européen 1169/2011 impose de porter à la connaissance du client la présence des quatorze allergènes réglementaires. Une borne est un bon endroit pour le faire, à condition que le logiciel prévoie le champ. Beaucoup ne le prévoient pas.</p>

      <h2>Combien ça coûte vraiment</h2>
      <p>Le prix affiché ne suffit pas. Voici les postes à additionner sur trois ans, hors logiciel, pour une borne intérieure sur pied.</p>
    </div>

    <div class="cadre-defil mt-2">
      <table class="tbl">
        <caption>Coût d’une borne sur trois ans, hors logiciel</caption>
        <thead><tr><th scope="col">Poste</th><th scope="col">Fourchette</th><th scope="col">Remarque</th></tr></thead>
        <tbody>
          <tr><th scope="row">Matériel</th><td>400 à 1 500 €</td><td class="txt">achat unique</td></tr>
          <tr><th scope="row">Livraison</th><td>0 à 120 €</td><td class="txt">un colis de 20 kg et plus part en messagerie</td></tr>
          <tr><th scope="row">Mise en service</th><td>0 à 400 €</td><td class="txt">gratuite si vous le faites vous-même</td></tr>
          <tr><th scope="row">Électricité</th><td>25 à 50 € par an</td><td class="txt">environ 45 W, 12 h par jour</td></tr>
          <tr><th scope="row">Casse et consommables</th><td>0 à 300 €</td><td class="txt">dépend surtout du verre de protection</td></tr>
          <tr><th scope="row">Logiciel</th><td>0 à 3 200 €</td><td class="txt">le poste qui fait tout basculer</td></tr>
        </tbody>
      </table>
    </div>

    <div class="prose mt-2">
      <p>Pour savoir si l’investissement tient, prenez le chemin le plus court. Comptez le nombre de commandes que vous passez au pic, multipliez par la part que la borne prendra en charge, disons un tiers au démarrage, puis par la hausse de panier que vous jugez plausible. Sur 120 commandes par jour, 40 passées à la borne, un panier moyen de 14 € et une hausse de 10 %, cela fait 56 € par jour de chiffre d’affaires supplémentaire, soit environ 1 450 € par mois sur 26 jours. Une borne à 600 € est amortie en une semaine et demie dans ce scénario, un ensemble à 4 400 € sur trois ans reste rentable mais vous engage beaucoup plus longtemps.</p>
      <p>Faites le calcul avec vos vrais chiffres plutôt qu’avec les miens. Si la hausse de panier que vous jugez plausible est de 0 %, ne l’achetez pas.</p>

      <h2>Où la poser</h2>
      <p>La borne doit être visible avant la file, pas après. Posée derrière les gens qui attendent, elle ne sert à rien : personne ne double une file pour aller vers un écran. Le bon emplacement se trouve dans les deux mètres qui suivent la porte, sur le côté, avec un dégagement d’au moins 90 cm devant pour laisser passer un fauteuil roulant.</p>
      <p>Prévoyez une prise à moins de trois mètres et faites passer le câble dans la colonne plutôt que sur le sol. Un câble qui traverse un passage finit arraché, et vous êtes responsable de la chute.</p>

      <h2>Les erreurs qu’on voit le plus souvent</h2>
      <p>Acheter deux bornes d’un coup. Commencez par une, regardez ce qui se passe pendant trois semaines, puis décidez. Le taux d’usage réel surprend souvent, dans un sens comme dans l’autre.</p>
      <p>Charger toute la carte. Une carte de soixante références sur un écran vertical devient une liste que personne ne lit. Les enseignes qui réussissent leurs bornes affichent une sélection, pas un catalogue.</p>
      <p>Laisser l’écran s’éteindre. Une borne noire ressemble à une borne en panne, et les clients ne la touchent pas. Réglez la mise en veille sur une animation ou une image, jamais sur un écran éteint.</p>
      <p>Ne rien changer au comptoir. Si la personne en caisse continue de héler les clients qui approchent de la borne, personne ne l’utilisera. Le changement d’habitude de l’équipe compte autant que le matériel.</p>
    </div>

    <h2 class="mt-2" style="font-size:var(--t-xl)">Questions fréquentes</h2>
    <div class="mt-1">
      <details><summary>Quelle taille d’écran choisir&nbsp;?</summary><p class="rep">Entre 21 et 27 pouces en orientation verticale pour un usage intérieur. En dessous de 21 pouces, les photos de produits deviennent trop petites pour donner envie. Au-dessus de 27, vous payez surtout de l’encombrement.</p></details>
      <details><summary>Une ou deux bornes&nbsp;?</summary><p class="rep">Une borne absorbe confortablement 60 à 80 commandes sur une heure de pic. Au-delà, une deuxième évite de recréer la file devant l’écran. Commencez par une et mesurez avant d’en ajouter.</p></details>
      <details><summary>Une borne permet-elle de réduire l’effectif&nbsp;?</summary><p class="rep">Dans les faits, rarement. Elle déplace la personne qui tenait la caisse vers la salle ou la production. Un projet de borne justifié uniquement par une économie de salaire déçoit presque toujours, parce que le pic reste le pic et qu’il faut toujours quelqu’un pour les cas particuliers.</p></details>
      <details><summary>Quel taux de TVA s’applique à une commande passée sur borne&nbsp;?</summary><p class="rep">Le même que pour la même commande passée au comptoir : le taux dépend de la nature du produit et du mode de consommation, pas du canal de vente. La borne doit demander « sur place ou à emporter » et transmettre l’information à votre caisse.</p></details>
      <details><summary>Faut-il une attestation de conformité fiscale pour la borne&nbsp;?</summary><p class="rep">Pour le matériel, non. Pour le logiciel qui enregistre les règlements, oui, et c’est son éditeur qui la fournit. Réclamez-la à votre éditeur de caisse, pas à votre fournisseur d’écran.</p></details>
      <details><summary>Combien de temps pour amortir une borne&nbsp;?</summary><p class="rep">Cela dépend du prix payé et de la hausse de panier constatée. Avec un matériel autour de 500 € et 40 commandes par jour passées à la borne, l’amortissement se compte en semaines. Avec un ensemble matériel et logiciel à 100 € par mois, il se compte en mois et dure tant que l’abonnement dure.</p></details>
    </div>

    <div class="carte mt-2">
      <h2 style="font-size:var(--t-lg)">Ce que nous vendons, pour être clair</h2>
      <p class="note mt-1">Une borne sur pied à 600 € HT, sans logiciel et sans abonnement, livrée montée. Nous avons écrit ce guide en sachant qu’il vous conduira parfois à ne pas acheter chez nous. C’est un risque assumé : un restaurateur qui installe une borne dont il n’avait pas besoin la revend au bout de six mois et le dit autour de lui.</p>
      <p class="mt-1"><a class="btn" href="index.html">Voir la borne</a> <a class="btn btn--secondaire" href="commander.html" style="margin-left:.5rem">Commander</a></p>
    </div>
  </div>
</main>
"""

# ==========================================================================
# 5. Pages de service et pages légales
# ==========================================================================
CORPS_CONTACT = fil([("Accueil", "index.html"), ("Contact", None)]) + """
<main id="contenu" class="env sec" style="padding-top:var(--pas)">
  <div class="duo">
    <div>
      <p class="surtitre">Contact</p>
      <h1 style="font-size:var(--t-2xl)">Écrivez-nous</h1>
      <p class="prose mt-1">La question la plus utile avant d’acheter reste « est-ce que ça marche avec ma caisse ». Dites-nous quel logiciel vous utilisez, on vous répond franchement, quitte à vous dire non.</p>
      <form class="mt-2" data-mailto="Question sur la borne de commande" style="display:grid;gap:.9rem;max-width:30rem">
        <label class="champ"><span>Établissement et ville</span><input type="text" name="Établissement" required placeholder="Le Comptoir 22, Saint-Brieuc"></label>
        <label class="champ"><span>Téléphone ou e-mail</span><input type="text" name="Contact" required placeholder="06 00 00 00 00"></label>
        <label class="champ"><span>Logiciel de caisse utilisé</span><input type="text" name="Caisse" placeholder="Zelty, Tiller, aucun…"></label>
        <label class="champ"><span>Votre question</span><textarea name="Message" required placeholder="Ce que vous voulez savoir"></textarea></label>
        <button class="btn" type="submit">Envoyer</button>
        <p class="note">Ce formulaire ouvre votre messagerie avec le message déjà écrit. Les informations servent uniquement à vous répondre, sont conservées douze mois et ne sont ni revendues ni utilisées pour de la prospection. Accès et effacement : <a data-mail href="mailto:contact@bornea.fr">contact@bornea.fr</a>.</p>
        <p class="note secours" hidden></p>
      </form>
    </div>
    <div>
      <div class="carte">
        <h2 style="font-size:var(--t-lg)">Par téléphone</h2>
        <p class="prix mt-1" style="font-size:1.5rem;font-weight:700"><a data-tel href="tel:+33296000000">02 96 00 00 00</a></p>
        <p class="note mt-1">Du lundi au vendredi, 9 h à 18 h. En dehors de ces horaires, laissez un message, on rappelle le jour ouvré suivant.</p>
        <h2 style="font-size:var(--t-lg)" class="mt-2">Par e-mail</h2>
        <p class="mt-1"><a data-mail href="mailto:contact@bornea.fr">contact@bornea.fr</a></p>
        <h2 style="font-size:var(--t-lg)" class="mt-2">Adresse</h2>
        <p class="note mt-1">ADRESSE POSTALE À COMPLÉTER<br>22000 Saint-Brieuc</p>
        <p class="note mt-1">Les visites se font sur rendez-vous. Nous n’avons pas de magasin ouvert au public.</p>
      </div>
    </div>
  </div>
</main>
"""

CORPS_LIVRAISON = fil([("Accueil", "index.html"), ("Livraison et retours", None)]) + """
<main id="contenu" class="env sec" style="padding-top:var(--pas)">
  <div style="max-width:44rem">
    <p class="surtitre">Livraison et retours</p>
    <h1 style="font-size:var(--t-2xl)">Comment la borne arrive chez vous</h1>
    <div class="prose mt-2">
      <h2>Délais et transport</h2>
      <p>La borne part sous 4 à 7 jours ouvrés après le paiement, en messagerie, sur palette ou en colis renforcé selon la quantité. Le transport est compris dans le prix pour la France métropolitaine. Vous recevez le numéro de suivi le jour du départ.</p>
      <p>Pour la Corse, Monaco et l’outre-mer, le transport est chiffré au cas par cas. Écrivez-nous avant de commander, nous vous envoyons un devis avec le montant exact.</p>
      <p>La livraison se fait au pied du camion, pas dans votre salle. Prévoyez une personne disponible : un colis de plus de 20 kg ne se réceptionne pas d’une main pendant le coup de feu.</p>

      <h2>À faire à la réception, dans l’ordre</h2>
      <ol>
        <li>Ouvrez le carton devant le chauffeur. Le transporteur doit vous en laisser le temps.</li>
        <li>Si l’emballage est enfoncé, percé ou mouillé, écrivez la réserve précise sur le bordereau. « Carton enfoncé angle supérieur droit, écran non vérifié » vaut quelque chose. « Sous réserve de déballage » ne vaut rien.</li>
        <li>Confirmez-nous la réserve par e-mail sous trois jours ouvrés, en joignant une photo. C’est ce délai qui rend un recours possible.</li>
      </ol>

      <h2>Garantie</h2>
      <p>La borne est garantie deux ans, pièces et main-d’œuvre, à compter de la livraison. L’extension à trois ans peut être ajoutée à la commande pour 79 € HT par borne. La garantie couvre les défauts de fabrication et les pannes en usage normal. Elle ne couvre pas le verre cassé par un choc, les dégâts liés à un branchement hors norme, ni une borne installée en extérieur alors qu’elle ne le prévoit pas.</p>
      <p>En cas de panne, appelez-nous. On diagnostique par téléphone, ce qui règle une partie des cas sans rien renvoyer. Si le matériel doit revenir, l’étiquette de retour vous est envoyée et le transport est à notre charge.</p>

      <h2>Retour et rétractation</h2>
      <p>La vente s’adresse à des professionnels dans le cadre de leur activité. Le droit de rétractation de quatorze jours prévu pour les consommateurs par l’article L221-18 du code de la consommation ne s’applique donc pas à cette commande.</p>
      <p>Nous appliquons quand même une reprise commerciale de quatorze jours, à compter de la livraison, si la borne est renvoyée complète, dans son emballage d’origine et en état de revente. Le retour est à votre charge, le remboursement se fait sous quatorze jours après réception et contrôle. C’est un engagement contractuel de notre part, pas un droit légal : il figure aussi dans nos <a href="cgv.html">conditions générales de vente</a>.</p>

      <h2>Déchets d’équipements électriques</h2>
      <p>La borne est un équipement électrique et électronique. En fin de vie, elle ne se jette pas avec les ordures. Nous reprenons gratuitement l’ancien matériel équivalent lors d’une nouvelle livraison, et l’éco-participation applicable est indiquée sur la facture.</p>
    </div>
    <p class="mt-2"><a class="btn" href="commander.html">Commander</a></p>
  </div>
</main>
"""

CORPS_CGV = fil([("Accueil", "index.html"), ("Conditions générales de vente", None)]) + """
<main id="contenu" class="env sec" style="padding-top:var(--pas)">
  <div style="max-width:44rem">
    <h1 style="font-size:var(--t-xl)">Conditions générales de vente</h1>
    <p class="note mt-1">Version du <span data-annee>2026</span>. Les mentions en majuscules doivent être complétées avant la mise en ligne.</p>
    <div class="prose mt-2">
      <h2>1. Objet et champ d’application</h2>
      <p>Les présentes conditions régissent les ventes conclues sur ce site par RAISON SOCIALE À COMPLÉTER auprès d’acheteurs agissant à des fins professionnelles. Toute commande vaut acceptation sans réserve des présentes conditions, dans leur version en vigueur au jour de la commande.</p>
      <p>À la validation de la commande, la carte de l’acheteur fait l’objet d’une autorisation bancaire et non d’un débit : l’établissement émetteur bloque le montant sans le verser. Le vendeur déclenche le prélèvement effectif lors de la confirmation de la commande, et au plus tard dans les sept jours suivant l’autorisation. À défaut de prélèvement dans ce délai, l’autorisation devient caduque et le montant est restitué à l’acheteur sans que la vente soit formée. L’acheteur en est informé sur la page de commande et sur la page de paiement.</p>

      <h2>2. Produits</h2>
      <p>Les caractéristiques essentielles des produits figurent sur les pages produits. Les photographies et illustrations n’ont pas de valeur contractuelle. Le produit vendu est un écran tactile sur pied. Il ne comprend ni logiciel de prise de commande, ni logiciel d’encaissement, ni imprimante, ni terminal de paiement.</p>

      <h2>3. Prix</h2>
      <p>Les prix sont indiqués en euros hors taxes, la TVA au taux en vigueur étant ajoutée lors du paiement. Ils comprennent le transport en France métropolitaine. L’éco-participation au titre de la filière des déchets d’équipements électriques et électroniques est mentionnée sur la facture. Le vendeur se réserve le droit de modifier ses prix à tout moment, le prix applicable étant celui affiché au moment de la commande.</p>

      <h2>4. Commande et paiement</h2>
      <p>La commande est ferme après validation du paiement. Le paiement par carte bancaire est traité par Stripe Payments Europe Limited. Aucune donnée bancaire n’est collectée ni conservée par le vendeur. Le paiement par virement est possible sur demande : la commande est alors préparée à réception des fonds.</p>
      <p>Le vendeur peut refuser une commande en cas de litige antérieur, de commande anormale au regard des quantités habituelles, ou de suspicion de fraude.</p>

      <h2>5. Livraison</h2>
      <p>Les produits sont expédiés sous 4 à 7 jours ouvrés à l’adresse indiquée lors du paiement. Le transfert des risques s’opère à la remise du produit à l’acheteur. Les réserves relatives à l’état du colis doivent être portées sur le bordereau de transport à la réception et confirmées au vendeur dans les trois jours ouvrés.</p>
      <p>Un retard de livraison n’ouvre pas droit à indemnité, sauf faute du vendeur. En cas de retard supérieur à trente jours, l’acheteur peut annuler la commande et obtenir le remboursement intégral.</p>

      <h2>6. Rétractation</h2>
      <p>La vente s’adressant à des professionnels agissant dans le cadre de leur activité, le droit de rétractation prévu aux articles L221-18 et suivants du code de la consommation ne s’applique pas.</p>
      <p>Le vendeur accorde néanmoins, à titre contractuel, un droit de reprise de quatorze jours à compter de la livraison. Le produit doit être renvoyé complet, dans son emballage d’origine et en état de revente. Les frais de retour restent à la charge de l’acheteur. Le remboursement intervient dans les quatorze jours suivant la réception et le contrôle du produit.</p>

      <h2>7. Garanties</h2>
      <p>Le vendeur accorde une garantie contractuelle de vingt-quatre mois à compter de la livraison, portant sur les pièces et la main-d’œuvre, extensible à trente-six mois en option. Cette garantie couvre les défauts de fabrication et les pannes survenant en usage normal. Elle exclut la casse, les dommages résultant d’un branchement non conforme, d’une installation en extérieur, d’une modification du matériel ou d’un usage anormal.</p>
      <p>L’acheteur bénéficie par ailleurs de la garantie légale contre les vices cachés dans les conditions des articles 1641 et suivants du code civil.</p>

      <h2>8. Réserve de propriété</h2>
      <p>Le vendeur conserve la propriété des produits jusqu’au paiement intégral du prix. L’acheteur en supporte les risques dès la livraison.</p>

      <h2>9. Retard de paiement</h2>
      <p>Toute somme non payée à l’échéance porte intérêt au taux d’intérêt appliqué par la Banque centrale européenne à son opération de refinancement la plus récente, majoré de dix points de pourcentage, et donne lieu à une indemnité forfaitaire pour frais de recouvrement de quarante euros, conformément aux articles L441-10 et D441-5 du code de commerce.</p>

      <h2>10. Données personnelles</h2>
      <p>Le traitement des données est décrit dans la <a href="confidentialite.html">politique de confidentialité</a>.</p>

      <h2>11. Droit applicable et litiges</h2>
      <p>Les présentes conditions sont soumises au droit français. À défaut d’accord amiable, tout litige relève de la compétence exclusive du tribunal de commerce de VILLE DU RESSORT À COMPLÉTER, y compris en cas de pluralité de défendeurs ou d’appel en garantie.</p>
    </div>
  </div>
</main>
"""

CORPS_MENTIONS = fil([("Accueil", "index.html"), ("Mentions légales", None)]) + """
<main id="contenu" class="env sec" style="padding-top:var(--pas)">
  <div style="max-width:44rem">
    <h1 style="font-size:var(--t-xl)">Mentions légales</h1>
    <p class="note mt-1">Informations exigées par l’article 6-III de la loi pour la confiance dans l’économie numérique. Les valeurs en majuscules doivent être complétées avant la mise en ligne : un site professionnel sans ces mentions est en infraction.</p>
    <div class="prose mt-2">
      <h2>Éditeur du site</h2>
      <p>RAISON SOCIALE À COMPLÉTER, FORME JURIDIQUE au capital de MONTANT euros.<br>
      Siège social : ADRESSE COMPLÈTE À COMPLÉTER.<br>
      Immatriculée au registre du commerce et des sociétés de VILLE sous le numéro SIREN À COMPLÉTER.<br>
      Numéro de TVA intracommunautaire : FR À COMPLÉTER.<br>
      Téléphone : <a data-tel href="tel:+33296000000">02 96 00 00 00</a>. Courriel : <a data-mail href="mailto:contact@bornea.fr">contact@bornea.fr</a>.</p>

      <h2>Directeur de la publication</h2>
      <p>NOM ET PRÉNOM À COMPLÉTER, en qualité de représentant légal.</p>

      <h2>Hébergeur</h2>
      <p>SAS o2switch, 222-224 boulevard Gustave Flaubert, 63000 Clermont-Ferrand, France. Téléphone : 04 44 44 60 40.</p>
      <p class="note">À remplacer si le site est hébergé ailleurs. L’identité de l’hébergeur est obligatoire, pas optionnelle.</p>

      <h2>Propriété intellectuelle</h2>
      <p>Les textes, la structure et les illustrations de ce site sont la propriété de l’éditeur. Toute reproduction sans autorisation écrite préalable est interdite.</p>

      <h2>Filière des déchets électriques</h2>
      <p>L’éditeur déclare les équipements électriques et électroniques qu’il met sur le marché au titre de la responsabilité élargie du producteur. Identifiant unique : NUMÉRO ADEME À COMPLÉTER.</p>

      <h2>Signalement</h2>
      <p>Pour signaler un contenu illicite ou une erreur sur ce site, écrivez à <a data-mail href="mailto:contact@bornea.fr">contact@bornea.fr</a>.</p>
    </div>
  </div>
</main>
"""

CORPS_CONFID = fil([("Accueil", "index.html"), ("Données personnelles", None)]) + """
<main id="contenu" class="env sec" style="padding-top:var(--pas)">
  <div style="max-width:44rem">
    <h1 style="font-size:var(--t-xl)">Données personnelles</h1>
    <div class="prose mt-2">
      <h2>Ce que ce site ne fait pas</h2>
      <p>Ce site ne dépose aucun cookie de mesure d’audience, n’utilise ni Google Analytics ni pixel publicitaire, et ne charge aucune police ni script hébergé par un tiers. C’est la raison pour laquelle vous ne voyez pas de bandeau de consentement : il n’y a rien à consentir.</p>

      <h2>Les données que nous recevons</h2>
      <p>Quand vous utilisez le formulaire de contact, votre messagerie nous envoie ce que vous avez saisi : le nom de votre établissement, vos coordonnées et votre question. Ces informations servent à vous répondre. Elles sont conservées douze mois, puis effacées.</p>
      <p>Quand vous passez commande, le nom de l’établissement et l’adresse e-mail que vous indiquez sont transmis à Stripe pour pré-remplir la page de paiement. La commande elle-même, l’adresse de livraison, la facturation et le règlement sont traités par Stripe Payments Europe Limited, dont la politique de confidentialité est consultable sur stripe.com. Aucun numéro de carte ne passe par nos serveurs.</p>
      <p>Votre carte étant autorisée avant d’être débitée, Stripe conserve l’autorisation jusqu’au prélèvement ou jusqu’à sa caducité. Nous recevons de Stripe le détail de la commande et l’identité de l’acheteur, que nous conservons dix ans au titre des obligations comptables.</p>

      <h2>Vos droits</h2>
      <p>Vous pouvez demander l’accès à vos données, leur rectification, leur effacement ou la limitation de leur traitement en écrivant à <a data-mail href="mailto:contact@bornea.fr">contact@bornea.fr</a>. Une réponse vous est adressée dans un délai d’un mois. En cas de désaccord, vous pouvez saisir la Commission nationale de l’informatique et des libertés, 3 place de Fontenoy, 75007 Paris.</p>

      <h2>Si vous ajoutez un outil de mesure</h2>
      <p class="note">Cette page décrit le site tel qu’il est livré. L’ajout d’un outil de statistiques, d’un pixel publicitaire ou d’une police hébergée chez un tiers change la situation et impose de mettre cette page à jour, et le plus souvent d’ajouter un bandeau de consentement conforme, où refuser est aussi simple qu’accepter.</p>
    </div>
  </div>
</main>
"""

CORPS_404 = """
<main id="contenu" class="env-etroite confirme">
  <h1>Cette page n’existe pas</h1>
  <p>Le lien est peut-être ancien, ou l’adresse comporte une faute de frappe.</p>
  <p class="mt-2">
    <a class="btn" href="index.html">Voir la borne</a>
    <a class="btn btn--secondaire" href="guide-borne-de-commande-restaurant.html" style="margin-left:.5rem">Lire le guide d’achat</a>
  </p>
</main>
"""

# ==========================================================================
# 6. Données structurées
# ==========================================================================
ORG = {
    "@context": "https://schema.org", "@type": "Organization",
    "@id": f"{DOMAINE}/#organisation",
    "name": MARQUE, "url": DOMAINE + "/",
    "email": MAIL, "telephone": TEL,
    "description": "Vente de bornes de commande tactiles pour la restauration, sans abonnement.",
    "address": {"@type": "PostalAddress", "streetAddress": "ADRESSE À COMPLÉTER",
                "addressLocality": "Saint-Brieuc", "postalCode": "22000", "addressCountry": "FR"},
    "areaServed": {"@type": "Country", "name": "France"}
}

PRODUIT = {
    "@context": "https://schema.org", "@type": "Product",
    "@id": f"{DOMAINE}/#borne",
    "name": "Borne de commande tactile sur pied pour restaurant",
    "description": ("Écran tactile sur pied pour la prise de commande en restauration. L'écran pivote "
                    "entre paysage et portrait, la batterie est intégrée et Android reste ouvert, "
                    "verrouillable en mode kiosque. Livrée montée, sans logiciel imposé et sans abonnement."),
    "category": "Borne de commande restaurant",
    "brand": {"@type": "Brand", "name": MARQUE},
    "image": [f"{DOMAINE}/img/borne-de-commande-restaurant-ecran-paysage-1000.webp",
              f"{DOMAINE}/img/borne-de-commande-restaurant-ecran-portrait-1000.webp",
              f"{DOMAINE}/img/borne-de-commande-restaurant-rotation-1000.webp"],
    "offers": {
        "@type": "Offer",
        "price": "600.00", "priceCurrency": "EUR",
        "valueAddedTaxIncluded": False,
        "availability": "https://schema.org/InStock",
        "itemCondition": "https://schema.org/NewCondition",
        "url": f"{DOMAINE}/commander.html",
        "priceValidUntil": "2027-12-31",
        "seller": {"@id": f"{DOMAINE}/#organisation"},
        "shippingDetails": {
            "@type": "OfferShippingDetails",
            "shippingRate": {"@type": "MonetaryAmount", "value": "0", "currency": "EUR"},
            "shippingDestination": {"@type": "DefinedRegion", "addressCountry": "FR"},
            "deliveryTime": {
                "@type": "ShippingDeliveryTime",
                "handlingTime": {"@type": "QuantitativeValue", "minValue": 1, "maxValue": 2, "unitCode": "DAY"},
                "transitTime": {"@type": "QuantitativeValue", "minValue": 3, "maxValue": 5, "unitCode": "DAY"}
            }
        },
        "hasMerchantReturnPolicy": {
            "@type": "MerchantReturnPolicy",
            "applicableCountry": "FR",
            "returnPolicyCategory": "https://schema.org/MerchantReturnFiniteReturnWindow",
            "merchantReturnDays": 14,
            "returnMethod": "https://schema.org/ReturnByMail",
            "returnFees": "https://schema.org/ReturnShippingFees"
        }
    }
}

def faq(paires):
    return {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q,
                            "acceptedAnswer": {"@type": "Answer", "text": r}} for q, r in paires]}

FAQ_INDEX = faq([
 ("Le logiciel de commande est-il fourni avec la borne ?",
  "Non. La borne est un écran tactile sous Android verrouillé en mode kiosque. Vous y installez l'application de commande de votre choix, y compris celle de votre éditeur de caisse. Une mise en service à distance est proposée en option à 149 euros hors taxes."),
 ("Faut-il un abonnement pour utiliser cette borne de commande ?",
  "Non. La borne est vendue 600 euros hors taxes, payés une fois. Si votre logiciel de commande est facturé au mois, cet abonnement reste entre votre éditeur et vous."),
 ("Sous combien de temps la borne est-elle livrée ?",
  "Quatre à sept jours ouvrés en France métropolitaine, transport compris dans le prix. Le numéro de suivi est envoyé au départ du colis."),
 ("La borne fonctionne-t-elle avec ma caisse enregistreuse ?",
  "Cela dépend de votre logiciel de caisse, pas de l'écran. Indiquez-nous lequel vous utilisez et nous vous dirons s'il existe une application Android compatible."),
 ("Peut-on poser la borne sur un comptoir plutôt que sur son pied ?",
  "L'écran est monté sur une platine standard et se démonte de sa colonne. Un support de comptoir compatible se trouve facilement, mais il n'est pas fourni."),
 ("Que se passe-t-il si la borne tombe en panne ?",
  "La garantie couvre deux ans, pièces et main-d'œuvre. Le diagnostic se fait par téléphone et l'étiquette de retour est fournie si le matériel doit revenir. La caisse continuant de fonctionner, une borne en panne ralentit le service sans l'arrêter.")
])

FAQ_GUIDE = faq([
 ("Quelle taille d'écran choisir pour une borne de commande ?",
  "Entre 21 et 27 pouces en orientation verticale pour un usage intérieur. En dessous de 21 pouces les photos de produits deviennent trop petites, au-dessus de 27 pouces on paie surtout de l'encombrement."),
 ("Faut-il installer une ou deux bornes de commande ?",
  "Une borne absorbe confortablement 60 à 80 commandes sur une heure de pic. Au-delà, une deuxième évite de recréer une file devant l'écran."),
 ("Une borne de commande permet-elle de réduire l'effectif ?",
  "Rarement dans les faits. Elle déplace la personne qui tenait la caisse vers la salle ou la production. Un projet justifié uniquement par une économie de salaire déçoit presque toujours."),
 ("Quel taux de TVA s'applique à une commande passée sur borne ?",
  "Le même que pour la même commande passée au comptoir. Le taux dépend de la nature du produit et du mode de consommation, pas du canal de vente. La borne doit demander sur place ou à emporter et transmettre l'information à la caisse."),
 ("Faut-il une attestation de conformité fiscale pour une borne de commande ?",
  "Pour le matériel, non. L'attestation prévue à l'article 286-I-3° bis du code général des impôts porte sur le logiciel qui enregistre les règlements et c'est son éditeur qui la délivre."),
 ("Combien de temps faut-il pour amortir une borne de commande ?",
  "Cela dépend du prix payé et de la hausse de panier constatée. Avec un matériel autour de 500 euros et 40 commandes par jour passées à la borne, l'amortissement se compte en semaines.")
])

ARTICLE = {
    "@context": "https://schema.org", "@type": "Article",
    "headline": "Bien choisir une borne de commande pour son restaurant",
    "description": "Formats, écran, logiciel, TVA, coût réel sur trois ans et erreurs fréquentes.",
    "inLanguage": "fr-FR",
    "author": {"@id": f"{DOMAINE}/#organisation"},
    "publisher": {"@id": f"{DOMAINE}/#organisation"},
    "mainEntityOfPage": f"{DOMAINE}/guide-borne-de-commande-restaurant.html",
    "datePublished": "2026-08-01", "dateModified": "2026-08-23"
}

# ==========================================================================
# 7. Écriture
# ==========================================================================
FICHIERS = []

FICHIERS.append(page(
    "index.html",
    "Borne de commande restaurant à 600 € HT, sans abonnement | " + MARQUE,
    "Borne de commande tactile pour restaurant : écran vertical sur pied, 600 € HT, sans abonnement ni logiciel imposé. Livraison offerte, garantie 2 ans.",
    CORPS_INDEX, ld=[ORG, PRODUIT, FAQ_INDEX]))

FICHIERS.append(page(
    "guide-borne-de-commande-restaurant.html",
    "Borne de commande restaurant : le guide d’achat 2026 | " + MARQUE,
    "Quel format de borne choisir, ce que coûte vraiment le logiciel, ce que dit la loi sur la TVA et la caisse, et le calcul de rentabilité pour un restaurant.",
    CORPS_GUIDE, ld=[ARTICLE, FAQ_GUIDE]))

FICHIERS.append(page(
    "commander.html",
    "Commander votre borne de commande restaurant | " + MARQUE,
    "Construisez votre borne en ligne, essayez-la, puis commandez : 720 € TTC livraison comprise, sans abonnement ni frais d’installation.",
    CORPS_COMMANDER,
    style_page=_lire("assets/borne-builder.css"),
    script_page=_lire("assets/borne-builder.js")))

FICHIERS.append(page(
    "merci.html", "Commande enregistrée | " + MARQUE,
    "Votre paiement est confirmé. Voici la suite des opérations, le délai d’expédition et les réserves à porter au bordereau de transport à la livraison.",
    CORPS_MERCI, robots="noindex, follow"))

FICHIERS.append(page(
    "paiement-annule.html", "Paiement interrompu | " + MARQUE,
    "Le paiement n’a pas abouti et rien n’a été débité. Reprenez la commande là où vous en étiez, ou demandez une facture proforma pour régler par virement.",
    CORPS_ANNULE, robots="noindex, follow"))

FICHIERS.append(page(
    "contact.html", "Contact | " + MARQUE,
    "Une question sur la compatibilité avec votre caisse, la livraison ou la facturation. Réponse sous un jour ouvré.",
    CORPS_CONTACT))

FICHIERS.append(page(
    "livraison-et-retours.html", "Livraison, garantie et retours | " + MARQUE,
    "Délais d’expédition, réserves à porter au bordereau de transport, garantie de deux ans et conditions de reprise commerciale.",
    CORPS_LIVRAISON))

FICHIERS.append(page(
    "cgv.html", "Conditions générales de vente | " + MARQUE,
    "Conditions de vente aux professionnels : prix, commande, livraison, garanties, réserve de propriété et règlement des litiges.",
    CORPS_CGV))

FICHIERS.append(page(
    "mentions-legales.html", "Mentions légales | " + MARQUE,
    "Éditeur, directeur de la publication, hébergeur et identifiant de la filière des déchets électriques.",
    CORPS_MENTIONS))

FICHIERS.append(page(
    "confidentialite.html", "Données personnelles | " + MARQUE,
    "Ce site ne dépose aucun cookie de mesure d’audience. Voici les données que nous recevons, leur durée de conservation et vos droits.",
    CORPS_CONFID))

FICHIERS.append(page(
    "404.html", "Page introuvable | " + MARQUE,
    "Cette adresse ne correspond à aucune page du site. Retrouvez la borne de commande, le guide d’achat ou les informations de livraison depuis cette page.",
    CORPS_404, robots="noindex, nofollow"))

# ==========================================================================
# 8. Le blog
# ==========================================================================
PAR_SLUG = {a["slug"]: a for a in ARTICLES}

def _date_fr(iso):
    mois = ["janvier","février","mars","avril","mai","juin","juillet",
            "août","septembre","octobre","novembre","décembre"]
    a, m, j = iso.split("-")
    return f"{int(j)} {mois[int(m)-1]} {a}"

def corps_article(a):
    """Met en page un article : en-tête, corps, FAQ, offre, articles voisins."""
    faq_html = "".join(
        f'<details><summary>{q}</summary><p class="rep">{r}</p></details>'
        for q, r in a["faq"])

    voisins = ""
    for sl in a.get("voisins", []):
        v = PAR_SLUG.get(sl)
        if not v:
            continue
        voisins += (f'<li><a href="{v["slug"]}.html">{v["h1"]}'
                    f'<span>{v["accroche"]}</span></a></li>')

    return (fil([("Accueil", "index.html"), ("Blog", "blog.html"), (a["titre"], None)]) + f"""
<main id="contenu" class="article">
  <p class="art-meta" data-reveal>Publié le {_date_fr(a["date"])} · mis à jour le {_date_fr(a["maj"])} · {a["lecture"]} min de lecture</p>
  <h1 data-reveal>{a["h1"]}</h1>
  <p class="art-resume" data-reveal>{a["resume"]}</p>

  <div class="art-corps">{a["corps"]}</div>

  <h2 style="font-size:var(--t-xl);margin-top:var(--section)">Questions fréquentes</h2>
  <div class="mt-1">{faq_html}</div>

  <aside class="art-offre" data-reveal>
    <h2>La borne dont nous nous servons</h2>
    {a["offre"]}
    <p class="liens">
      <a class="btn" href="index.html">Voir la borne à 600 € HT</a>
      <a class="btn btn--secondaire" href="commander.html">Commander</a>
    </p>
  </aside>

  <nav class="art-voisins" aria-label="Articles liés">
    <h2 style="font-size:var(--t-lg)">À lire ensuite</h2>
    <ul role="list">{voisins}</ul>
    <p class="mt-1"><a href="blog.html">Tous les articles</a></p>
  </nav>
</main>
""")

def corps_blog():
    cartes = ""
    for a in sorted(ARTICLES, key=lambda x: x["date"], reverse=True):
        cartes += f"""<article class="blog-carte" data-reveal>
          <h2><a href="{a["slug"]}.html">{a["h1"]}</a></h2>
          <p>{a["accroche"]}</p>
          <p class="meta">{_date_fr(a["date"])} · {a["lecture"]} min</p>
        </article>"""
    return fil([("Accueil", "index.html"), ("Blog", None)]) + f"""
<main id="contenu" class="env" style="padding-bottom:var(--section)">
  <div class="blog-tete">
    <p class="surtitre">Le blog</p>
    <h1 style="font-size:var(--t-2xl)">Tout ce qu’on aurait aimé lire avant d’équiper notre salle</h1>
    <p class="prose mt-1" style="max-width:40rem">Nous tenons un restaurant et nous fabriquons du matériel. Ces articles sortent de ce que nous avons appris en équipant notre propre comptoir, pas d’une documentation commerciale.</p>
  </div>
  <div class="blog-grille">{cartes}</div>
  <div class="prose mt-2" style="max-width:42rem">
    <h2 style="font-size:var(--t-lg)">Par où commencer</h2>
    <p>Si vous hésitez encore sur le principe, lisez d’abord ce que coûte réellement une borne sur trois ans : c’est le calcul qui nous a décidés, et il contient la seule donnée qui compte, le poids du logiciel dans la facture.</p>
    <p>Si vous êtes déjà décidé et que vous cherchez du matériel, allez voir les critères techniques. Les trois seuils chiffrés qui y figurent éliminent à eux seuls la moitié des modèles vendus en ligne.</p>
    <p>Et si vous avez déjà une borne qui ne sert à personne, le problème est presque toujours son emplacement. Trois semaines de comptage au pic de midi suffisent à le prouver.</p>
    <p>Une question qui n’est traitée nulle part ici ? Écrivez-nous, nous répondons et nous en faisons parfois un article.</p>
  </div>
</main>
"""

ARTICLE_LD = lambda a: {
    "@context": "https://schema.org", "@type": "Article",
    "headline": a["h1"][:110],
    "description": a["description"],
    "inLanguage": "fr-FR",
    "author": {"@id": f"{DOMAINE}/#organisation"},
    "publisher": {"@id": f"{DOMAINE}/#organisation"},
    "mainEntityOfPage": f"{DOMAINE}/{a['slug']}.html",
    "datePublished": a["date"], "dateModified": a["maj"],
    "about": {"@type": "Thing", "name": a["cle"]},
    "image": f"{DOMAINE}/img/og-borne-commande-restaurant.jpg",
}

for a in ARTICLES:
    FICHIERS.append(page(
        a["slug"] + ".html", a["titre"], a["description"],
        corps_article(a),
        ld=[ARTICLE_LD(a), faq(a["faq"])]))

FICHIERS.append(page(
    "blog.html", "Blog : bornes et tablettes de commande | " + MARQUE,
    "Prix réels, choix du matériel, logiciel et implantation en salle : nos articles sur les bornes et tablettes de commande, écrits depuis notre restaurant.",
    corps_blog(),
    ld=[{"@context": "https://schema.org", "@type": "Blog",
         "name": "Le blog de " + MARQUE,
         "url": f"{DOMAINE}/blog.html",
         "inLanguage": "fr-FR",
         "publisher": {"@id": f"{DOMAINE}/#organisation"},
         "blogPost": [{"@type": "BlogPosting", "headline": a["h1"][:110],
                       "url": f"{DOMAINE}/{a['slug']}.html",
                       "datePublished": a["date"]} for a in ARTICLES]}]))

# ==========================================================================
# 9. Flux produits Google Merchant Center (fiches gratuites)
# ==========================================================================
FLUX = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:g="http://base.google.com/ns/1.0"><channel>
<title>{MARQUE}</title><link>{DOMAINE}/</link><description>Bornes de commande pour la restauration</description>
<item>
<g:id>BORNE-K1</g:id>
<g:title>{MARQUE} borne de commande tactile sur pied pour restaurant, écran pivotant</g:title>
<g:description>Borne de commande tactile sur pied pour restaurant. Écran qui pivote entre paysage et portrait, batterie intégrée, Android ouvert en mode kiosque. Livrée montée, sans logiciel imposé et sans abonnement mensuel. Vous installez l application de prise de commande de votre choix, y compris celle de votre éditeur de caisse. Garantie 2 ans pièces et main d oeuvre, livraison offerte en France métropolitaine sous 4 à 7 jours ouvrés, assistance par téléphone en français.</g:description>
<g:link>{DOMAINE}/</g:link>
<g:image_link>{DOMAINE}/img/borne-de-commande-restaurant-ecran-paysage-1000.webp</g:image_link>
<g:additional_image_link>{DOMAINE}/img/borne-de-commande-restaurant-ecran-portrait-1000.webp</g:additional_image_link>
<g:additional_image_link>{DOMAINE}/img/borne-de-commande-restaurant-rotation-1000.webp</g:additional_image_link>
<g:availability>in_stock</g:availability>
<g:price>720.00 EUR</g:price>
<g:brand>{MARQUE}</g:brand>
<g:mpn>BORNE-K1</g:mpn><g:identifier_exists>no</g:identifier_exists>
<g:condition>new</g:condition>
<g:google_product_category>Entreprise et industrie &gt; Vente au détail &gt; Terminaux de point de vente</g:google_product_category>
<g:product_type>bornes de commande</g:product_type>
<g:shipping><g:country>FR</g:country><g:service>Standard</g:service><g:price>0.00 EUR</g:price></g:shipping>
</item>
</channel></rss>
"""
(RACINE / "flux-google.xml").write_text(FLUX, encoding="utf-8")

# --- robots.txt et sitemap ------------------------------------------------
(RACINE / "robots.txt").write_text(
    "User-agent: *\nAllow: /\nDisallow: /merci.html\nDisallow: /paiement-annule.html\n"
    "Disallow: /paiement/\nDisallow: /flux-google.xml\n\nSitemap: " + DOMAINE + "/sitemap.xml\n", encoding="utf-8")

PRIORITES = {"index.html": ("1.0", "weekly"),
             "guide-borne-de-commande-restaurant.html": ("0.9", "monthly"),
             "blog.html": ("0.8", "weekly"),
             "commander.html": ("0.8", "monthly")}
for _a in ARTICLES:
    PRIORITES[_a["slug"] + ".html"] = ("0.7", "monthly")
urls = []
for f in FICHIERS:
    if f in ("merci.html", "paiement-annule.html", "404.html"):
        continue
    prio, freq = PRIORITES.get(f, ("0.4", "yearly"))
    loc = DOMAINE + "/" + ("" if f == "index.html" else f)
    urls.append(f"  <url>\n    <loc>{loc}</loc>\n    <changefreq>{freq}</changefreq>\n    <priority>{prio}</priority>\n  </url>")
(RACINE / "sitemap.xml").write_text(
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    + "\n".join(urls) + "\n</urlset>\n", encoding="utf-8")

print(f"{len(FICHIERS)} pages écrites, plus robots.txt et sitemap.xml")
for f in FICHIERS:
    print("  ", f)
