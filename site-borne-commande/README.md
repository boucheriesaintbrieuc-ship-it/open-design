# Site « Borne de commande restaurant »

Site marchand mono-produit, onze pages, tunnel complet jusqu’au paiement Stripe.
Aucune dépendance externe : pas de CDN, pas de police tierce, pas de bibliothèque
JavaScript, aucune requête réseau au chargement.

**Chaque page contient son propre style et son propre script.** Elle s’affiche
correctement même envoyée seule sur un serveur, sans le reste du dossier. Une page
pèse entre 40 et 58 ko, ce qui reste largement sous le seuil où le poids se voit.

---

## Ce qui n’a pas pu être fait, à lire en premier

**Les images du fournisseur n’ont pas pu être récupérées.** AliExpress bloque les
accès automatisés : la page renvoie une erreur 503 et une boucle de redirection
anti-robot. Ni la fiche technique ni les photos n’ont donc pu être lues.

Deux conséquences :

1. Le produit est dessiné en SVG dans les pages, d’après les deux photos que vous
   avez envoyées. C’est net à toutes les tailles, ça pèse deux kilo-octets, mais
   ça ne remplace pas une photo pour vendre du matériel à 499 €. Voyez `img/README.md`
   pour la liste des visuels à produire, et `outils/telecharger-images.sh` pour
   récupérer ceux du fournisseur depuis votre navigateur.
2. Les caractéristiques techniques portent la mention **« à confirmer »**, visible
   sur la page. Cherchez `avf` dans les fichiers pour les retrouver toutes.
   Mesurez-les sur l’exemplaire que vous recevrez, puis retirez la classe.

**Attention sur les photos fournisseur.** Elles appartiennent au vendeur. Les publier
sur un site marchand français sans autorisation écrite expose à une action en
contrefaçon. Vos propres photos convertissent mieux de toute façon : un packshot
identique à celui de trente revendeurs ne prouve rien, une borne visible dans une
vraie salle prouve que vous l’avez eue entre les mains.

---

## Les fichiers

```
index.html                                page de vente, cible « borne commande restaurant »
guide-borne-de-commande-restaurant.html   guide d’achat, environ 2 000 mots
commander.html                            configurateur, dernier écran avant Stripe
merci.html                                retour de paiement réussi
paiement-annule.html                      retour de paiement abandonné
contact.html
livraison-et-retours.html
cgv.html
mentions-legales.html
confidentialite.html
404.html
robots.txt · sitemap.xml

assets/config.js        LE SEUL FICHIER À REMPLIR : identité, prix, liens Stripe
assets/site.css         feuille de style unique
assets/site.js          configurateur, calculs, départ vers Stripe

paiement/creer-session.php     mode avancé : total exact calculé côté serveur
paiement/config.exemple.php    à copier en config.php, contient la clé secrète
paiement/.htaccess             empêche de servir la configuration

img/README.md                  visuels à produire, avec dimensions
outils/construire.py           régénère les onze pages depuis la charpente commune
outils/telecharger-images.sh   récupère les photos fournisseur et les convertit
```

Les pages partagent un en-tête, un pied de page et un jeu de balises identiques
parce qu’elles sont assemblées par `outils/construire.py`. Modifiez le texte dans
ce script puis relancez `python3 outils/construire.py`, plutôt que d’éditer onze
fichiers à la main et de les voir diverger au premier changement.

---

## Brancher Stripe

Deux modes. Commencez par le premier.

### Mode « lien » (par défaut, aucun serveur nécessaire)

1. Dans Stripe, créez un produit **Borne de commande** avec trois prix : 499 €, 469 €
   et 449 €, tous en hors taxes.
2. Créez trois **Payment Links**, un par prix. Sur chacun :
   activez l’ajustement de quantité pour le lien à 449 €, laissez-le fixe sur les deux autres ;
   ajoutez la mise en service (149 €) et l’extension de garantie (79 €) en **articles facultatifs**,
   que le client coche sur la page de paiement ;
   activez la collecte de l’adresse de livraison pour la France ;
   réglez la page de confirmation sur `https://votre-domaine.fr/merci.html`.
3. Collez les trois URL dans `assets/config.js`, dans `liensStripe`.

Le configurateur choisit le bon lien selon la quantité, et transmet l’adresse e-mail
et le nom de l’établissement à Stripe en paramètres d’URL.

Limite assumée de ce mode : les options se cochent sur la page Stripe, pas sur la vôtre.
Le récapitulatif de `commander.html` affiche donc le total avec options, et Stripe
recalcule le sien. Si cet écart vous gêne, passez au mode suivant.

### Mode « php » (total exact, demande un hébergement PHP)

o2switch exécute PHP, donc ce mode y fonctionne tel quel.

1. `cp paiement/config.exemple.php paiement/config.php`, puis renseignez votre clé
   secrète Stripe et votre domaine.
2. Dans `assets/config.js`, passez `modePaiement` à `"php"`.
3. Dans Stripe, créez un taux de TVA à 20 % (Produits, puis Taux de taxe) et collez
   son identifiant `txr_…` dans `paiement/config.php`. Sans lui, les montants partent
   en TTC sans ligne de TVA distincte, ce qui complique la facture de votre client.

Le fichier PHP recalcule les prix à partir de la seule quantité envoyée par le
navigateur. Les montants ne viennent jamais du client : sans cette précaution,
n’importe qui achèterait la borne à un centime en modifiant la requête.

**La clé secrète (`sk_live_…`) ne doit jamais figurer dans `assets/config.js`**, qui est
téléchargé par le navigateur de chaque visiteur. Elle vit dans `paiement/config.php`,
et nulle part ailleurs.

### Ce qui manque encore côté Stripe

Il n’y a pas de webhook. Une commande payée déclenche le reçu Stripe et la page de
confirmation, mais rien ne prévient votre système. Tant que le volume reste faible,
le tableau de bord Stripe suffit pour suivre les commandes. Au-delà d’une dizaine par
semaine, ajoutez un webhook `checkout.session.completed` qui vous envoie un e-mail ou
alimente votre suivi.

---

## Ce qui doit être fait avant la mise en ligne

### Bloquant, sous peine d’infraction ou de site qui ment

1. **Identité.** « Bornéa », `bornea.fr`, `contact@bornea.fr` et le `02 96 00 00 00`
   sont des valeurs de remplacement. Tout se change dans `assets/config.js`, sauf le
   domaine des balises canoniques et du sitemap qui se change dans `outils/construire.py`,
   ligne `DOMAINE`.
2. **Mentions légales.** `mentions-legales.html` contient des mentions en majuscules à
   compléter : raison sociale, forme juridique, capital, siège, SIREN, TVA
   intracommunautaire, directeur de la publication. Un site professionnel sans ces
   informations est en infraction avec l’article 6-III de la LCEN.
3. **CGV.** Même chose pour la ville du tribunal de commerce compétent.
4. **Marquage CE et responsabilité d’importateur.** En important vous-même un
   équipement électrique depuis la Chine pour le revendre en France, vous devenez
   l’importateur au sens du règlement UE 2019/1020. Vous endossez alors les obligations
   du fabricant : vérifier que la déclaration UE de conformité existe, la conserver dix
   ans, apposer vos coordonnées sur le produit ou son emballage. Réclamez la déclaration
   au fournisseur avant la première commande. Sans elle, vous ne pouvez pas vendre.
5. **Filière des déchets électriques.** La revente d’équipements électriques impose de
   s’enregistrer auprès de l’ADEME et d’adhérer à un éco-organisme. L’identifiant unique
   doit figurer dans les mentions légales, l’éco-participation sur la facture.
6. **Prix des paliers.** 499, 469 et 449 € hors taxes sont ceux que vous avez indiqués
   pour le premier, extrapolés pour les deux autres. Vérifiez que la marge tient sur
   les quantités avant de publier.

### Important mais pas bloquant

7. **Photos.** Voir `img/README.md`. L’image de partage `og-borne-commande-restaurant.jpg`
   en 1200 × 630 est référencée par les onze pages et n’existe pas encore.
8. **Formulaire de contact.** Il ouvre la messagerie du visiteur, sans serveur. Pour un
   envoi direct, branchez un traitement côté serveur, et nommez alors le prestataire
   dans la page « Données personnelles ».
9. **Adresse postale** dans `contact.html`.

---

## Référencement

### Ce qui est fait

Une page par intention : la page de vente vise la requête transactionnelle
« borne commande restaurant », le guide vise la requête d’information. Aucune phrase
n’est reprise d’une page à l’autre, et les deux blocs de questions fréquentes ne se
recoupent pas : c’est ce qui évite la cannibalisation entre vos propres pages.

Sur chaque page : un seul `h1`, un titre entre 16 et 65 caractères, une description
entre 101 et 155 caractères, une balise canonique, un fil d’Ariane balisé, la langue
déclarée. Données structurées `Organization`, `Product` avec l’offre, les frais de port
et la politique de retour, `FAQPage`, `Article` et `BreadcrumbList`, toutes validées par
analyse syntaxique. `robots.txt` et `sitemap.xml` générés, les pages de retour de
paiement exclues de l’indexation.

Pour la recherche par IA, chaque page longue s’ouvre sur un encadré de faits courts et
autonomes (prix, délai, garantie, ce qui est inclus et ce qui ne l’est pas). Un moteur
de réponse cite ce qu’il peut extraire sans interpréter, et une phrase comme « le
logiciel n’est pas fourni » se cite mieux qu’un paragraphe promotionnel.

### Ce que ça ne fait pas

Le travail sur la page ne suffit pas à se positionner sur « borne commande restaurant ».
Cette requête est disputée par des acteurs installés depuis des années. Ce qui manque et
qui ne se code pas : des liens entrants depuis des sites du secteur, un historique de
domaine, et surtout des pages qui répondent à des requêtes plus précises et moins
disputées, du type « borne de commande pour kebab », « borne de commande sans abonnement »
ou « borne commande restaurant Bretagne ». Le guide est écrit pour servir de socle à ces
pages : ajoutez-en une par intention, pas une page unique bourrée de mots-clés.

Si le domaine `borne-commande-restaurant.fr` est libre, il vaut la peine : la
correspondance exacte du nom de domaine avec la requête reste un signal faible mais réel,
et le nom se retient.

---

## Mise en ligne sur o2switch

### La seule méthode qui marche du premier coup

Le gestionnaire de fichiers de cPanel envoie **des fichiers, pas des dossiers**.
C’est exactement ce qui s’est passé la première fois : `index.html` est bien arrivé
sur le serveur, mais `assets/site.css` non, et la page s’est affichée sans aucun
style. Passez par l’archive, elle règle le problème.

1. Récupérez `borne-restaurants-site.zip`.
2. cPanel, puis **Gestionnaire de fichiers**, puis ouvrez `public_html`.
3. Supprimez l’ancien `index.html` qui s’y trouve.
4. Cliquez sur **Téléverser** et envoyez le fichier `.zip` entier.
5. Revenez dans `public_html`, clic droit sur l’archive, puis **Extract**.
6. Supprimez l’archive une fois extraite.

Vérifiez ensuite ces trois adresses dans le navigateur :

```
https://borne-restaurants.fr/                 la page de vente, avec son style
https://borne-restaurants.fr/commander.html   le configurateur
https://borne-restaurants.fr/adresse-bidon    doit afficher la page 404 du site
```

Si la troisième renvoie l’erreur du serveur au lieu de votre page, le fichier
`.htaccess` n’a pas été extrait. Il commence par un point, donc le gestionnaire de
fichiers le masque par défaut : dans ses **Réglages**, cochez « Afficher les fichiers
cachés ».

### Réglages à faire une fois

Activez le certificat SSL dans cPanel s’il ne l’est pas déjà, puis purgez le cache
LiteSpeed. Déclarez enfin le site dans la Search Console et soumettez
`https://borne-restaurants.fr/sitemap.xml`.

### Pour modifier un texte ou un prix

Les pages contenant leur propre style, une modification globale se propage par le
générateur plutôt qu’à la main :

```bash
# 1. Prix, téléphone, adresse e-mail, liens Stripe
nano assets/config.js

# 2. Style
nano assets/site.css

# 3. Textes des pages
nano outils/construire.py

# 4. Régénérer les onze pages, puis refaire l'archive
python3 outils/construire.py
zip -r ../borne-restaurants-site.zip *.html robots.txt sitemap.xml .htaccess paiement img
```

Pour une correction ponctuelle sur une seule page, éditer directement le fichier
`.html` fonctionne aussi. Pensez alors à reporter la correction dans
`outils/construire.py`, sinon la prochaine régénération l’effacera.

## Contrôles passés

| Contrôle | Résultat |
|---|---|
| Requêtes réseau externes au chargement | 0, sur les 11 pages |
| Erreurs JavaScript et console | aucune |
| Débordement horizontal à 375, 768 et 1440 px | aucun |
| Contraste texte sur fond, seuil 4.5:1 (3:1 gros texte) | aucun défaut |
| Contour de focus au clavier | présent sur les 14 éléments testés |
| Cibles pointeur sous 24 px | une seule, un lien en ligne dans un paragraphe |
| Données structurées | 5 types, toutes analysées sans erreur |
| Liens internes morts | aucun |
| Un seul `h1` par page | oui |
| Calculs du configurateur | vérifiés de 1 à 5 bornes, avec et sans options |
| Blocage du paiement tant que les CGV ne sont pas acceptées | vérifié |
| URL transmise à Stripe | vérifiée, avec `prefilled_email` et `client_reference_id` |
| Syntaxe PHP | `php -l` sans erreur |
| Page envoyée **seule**, sans le dossier `assets/` | s’affiche complète : style, typographie, script |

Trois défauts ont été trouvés et corrigés, tous invisibles à la lecture du code. La
règle `.nav a` repeignait le bouton « Commander » en gris sur fond indigo par un effet
de spécificité. `element.hidden = false` n’a aucun effet sur un élément SVG, ce qui
empêchait les bornes 2 et 3 d’apparaître dans le configurateur. Et surtout, la première
version liait le style dans un fichier séparé, ce qui a suffi à afficher le site nu en
production : les pages embarquent désormais tout ce dont elles ont besoin.

Non testé ici, à faire de votre côté : rendu sur un iPhone et un Android réels, lecteur
d’écran, et un paiement de bout en bout avec une clé Stripe de test.
