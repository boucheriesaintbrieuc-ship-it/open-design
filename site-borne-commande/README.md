# Site « Borne de commande restaurant »

Site marchand mono-produit, trente pages dont un blog de dix-huit articles, tunnel
complet jusqu’au paiement Stripe.
Aucune dépendance externe : pas de CDN, pas de police tierce, pas de bibliothèque
JavaScript, aucune requête réseau au chargement.

**Chaque page contient son propre style et son propre script.** Elle s’affiche
correctement même envoyée seule sur un serveur, sans le reste du dossier. Une page
pèse entre 40 et 58 ko, ce qui reste largement sous le seuil où le poids se voit.

---

## Ce qui n’a pas pu être fait, à lire en premier

**Les photos sont maintenant les vraies.** Celles que vous avez envoyées ont été
converties en WebP et intégrées : entre 5 et 18 ko chacune, affichées en deux
tailles selon la largeur d’écran.

**La fiche technique du fabricant reste inaccessible.** Le site du fournisseur
bloque les accès automatisés et refuse la page pour notre région. Les valeurs
numériques portent donc encore la mention « à confirmer » : cherchez `avf` dans
les fichiers pour les retrouver toutes et les remplacer par vos mesures.

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

## Récitation du Coran sur la page de commande

`commander.html` porte un lecteur qui joue un fichier audio en boucle. Déposez
votre enregistrement dans `audio/coran.mp3` et il fonctionne. Le nom du fichier,
le volume et le titre affiché se règlent dans `assets/config.js`, sous `audio`.

### Pourquoi le son ne démarre pas au chargement

Chrome, Safari et Firefox refusent de lancer un son tant que le visiteur n'a pas
interagi avec la page. Aucun site ne peut passer outre, et les contournements qui
circulent, comme démarrer en muet puis monter le volume, sont bloqués eux aussi.

Le lecteur fait donc le maximum de ce qui est permis : il tente la lecture au
chargement, et si le navigateur refuse, il se relance au premier clic du
visiteur, où qu'il clique sur la page. En pratique le son part dès qu'il touche
quoi que ce soit.

### Le reste du comportement

Le bouton coupe et relance. Ce choix est mémorisé dans le navigateur : un
visiteur qui a coupé ne verra pas le son redémarrer à chaque page. Si le fichier
est absent ou dans un format refusé, le lecteur se retire de lui-même au lieu de
laisser un bouton inerte. Le bouton de coupure n'est pas décoratif : un son qui
dépasse trois secondes doit pouvoir être arrêté, c'est le critère WCAG 1.4.2.

### Deux réserves

Une récitation enregistrée appartient à son récitant et à son producteur.
La diffuser sur un site marchand demande une autorisation, sauf si
l'enregistrement est explicitement libre de droits.

Pour le reste, c'est votre site et votre clientèle : sachez simplement qu'un son
qui se déclenche sur une page de paiement fait partir une partie des visiteurs,
surtout ceux qui naviguent au bureau ou dans les transports. Le bouton de
coupure limite la casse. Si vous voulez mesurer l'effet, gardez le son sur
`commander.html` seulement, comme c'est le cas aujourd'hui, et regardez le taux
d'abandon avant et après dans Stripe.

## Le blog : dix-huit articles, dix-huit requêtes

Le blog vise les requêtes d'information autour de la borne de commande. La page
de vente garde seule la requête transactionnelle ; aucun article ne la vise,
pour que vos propres pages ne se fassent pas concurrence.

Les requêtes ont été choisies après lecture des SERP françaises, pas au jugé.
Deux constats ont guidé la sélection : les requêtes principales sont tenues par
des comparateurs et des éditeurs de logiciels, difficiles à déloger ; en
revanche plusieurs sujets n'ont aucune couverture sérieuse en français, au
premier rang desquels le paiement en titres-restaurant sur une borne, sur
lequel la recherche n'a rien remonté du tout.

| Article | Requête principale |
|---|---|
| `accessibilite-borne-de-commande.html` | accessibilité borne de commande |
| `augmentation-ticket-moyen-borne-chiffres.html` | augmentation ticket moyen borne de commande |
| `borne-de-commande-boulangerie.html` | borne de commande boulangerie |
| `borne-de-commande-food-truck.html` | borne de commande food truck |
| `borne-de-commande-kebab-pizzeria-snack.html` | borne de commande kebab |
| `borne-de-commande-occasion.html` | borne de commande occasion |
| `borne-de-commande-ou-caisse-enregistreuse.html` | borne de commande ou caisse enregistreuse |
| `borne-de-commande-sans-abonnement.html` | borne de commande sans abonnement |
| `borne-tactile-commande-prix.html` | borne tactile commande prix |
| `commission-plateformes-livraison-vs-borne.html` | commission plateforme livraison restaurant |
| `installer-borne-de-commande-restaurant.html` | installer borne de commande restaurant |
| `logiciel-borne-de-commande-ia.html` | logiciel borne de commande |
| `mode-kiosque-android-restaurant.html` | mode kiosque android tablette |
| `tablette-de-commande-restaurant-fonctionnement.html` | tablette de commande restaurant |
| `tablette-tactile-pour-restaurant.html` | tablette tactile pour restaurant |
| `titres-restaurant-borne-de-commande.html` | titres restaurant borne de commande |
| `tva-restauration-borne-de-commande.html` | tva restauration rapide 10 ou 5,5 |
| `ecran-cuisine-restaurant.html` | écran de cuisine restaurant |

Chaque article se termine par un bloc qui renvoie vers la page de vente et vers
la commande, rédigé différemment à chaque fois. C'est le passage le plus exposé
au copier-coller, donc celui qui ferait tomber le site en contenu dupliqué.

### Les quatre articles qui portent le plus

- **Titres-restaurant sur borne** : aucune source française ne traite le sujet,
  alors que la demande existe et que la question bloque des ventes au midi.
- **Food truck** : le sujet n'est couvert par personne, et l'article conclut
  qu'une borne sur pied n'y convient pas, ce qui le rend crédible.
- **Hausse du ticket moyen** : il remonte la piste du chiffre de 15 à 30 %
  affiché partout et constate qu'aucune étude publique ne le soutient. Un
  contenu de ce genre se fait citer, y compris par les moteurs de réponse.
- **Commission des plateformes** : forte charge émotionnelle chez les
  restaurateurs, et il mène naturellement au seul argument qui compte ici,
  l'absence de pourcentage sur vos ventes.

### Contrôle de duplication

`python3 outils/doublons.py` compare le texte de toutes les pages par séquences
de huit mots et refuse tout recouvrement au-dessus de 15 %. Les grilles de
cartes et les blocs « à lire ensuite » sont exclus : ils répètent des titres par
construction, c'est de la navigation, pas du contenu.

Dernier passage sur les trente pages : **3,7 % au pire**, titres, descriptions
et H1 tous uniques.

### Ajouter un article

Tout se passe dans `outils/articles.py`. Copiez une entrée, remplissez `slug`,
`cle`, `titre`, `h1`, `description`, `accroche`, `resume`, `corps`, `faq`,
`offre` et `voisins`, puis relancez `python3 outils/construire.py`. Le menu, le
sitemap, l'index du blog, les données structurées et le maillage se mettent à
jour seuls.

---

## Un point de droit qui vous concerne comme vendeur

L'article sur l'accessibilité documente la directive européenne entrée en
application le 28 juin 2025, qui impose une évaluation de conformité et un
marquage CE à certains terminaux en libre-service.

La fiche publiée par la DGCCRF en juillet 2025 cite les terminaux de paiement,
les distributeurs de billets, de titres de transport et de tickets de file
d'attente. **Les bornes de commande en restauration n'y figurent pas
nommément**, parce que le texte vise les terminaux servant les services qu'il
couvre, et que la restauration n'en fait pas partie. En revanche, un lecteur de
carte intégré à une borne relève bien du texte.

L'article dit exactement cela, sans trancher à votre place. Si vous ajoutez un
jour un terminal de paiement à la borne, faites vérifier ce point par un
juriste : vous seriez alors l'importateur d'un produit couvert.

---

## Google Shopping

`flux-google.xml` est un flux Merchant Center prêt à déclarer. Pour l'activer :
compte sur merchants.google.com, revendication du site, puis Produits, Sources
de produits, Ajouter, fichier récupéré depuis
`https://borne-restaurants.fr/flux-google.xml`, récupération quotidienne, et
activation des fiches gratuites.

Le flux est régénéré par `construire.py` ; si vous changez le prix, changez-le
dans `assets/config.js` et relancez, sinon Merchant Center rejettera la fiche
pour écart entre le flux et la page.

---

## Deux points à trancher de votre côté

**« La moins chère du marché ».** Vous me l'avez demandé et je ne l'ai pas écrit
tel quel sur le site. Un superlatif de prix doit pouvoir être prouvé à la
DGCCRF le jour où un concurrent se plaint. À la place, les pages donnent le prix
et la comparaison chiffrée, ce qui dit la même chose et se défend. Si vous voulez
la formule, gardez un relevé daté des prix de cinq concurrents, refait tous les
trimestres, et dites-le moi : je l'ajoute.

**motion-lab.agency.** Vous avez donné ce lien dans la phrase sur votre logiciel.
C'est une agence de motion design pour SaaS et startups, pas un éditeur de
logiciel de caisse. Je n'ai donc écrit aucun lien entre elle et votre outil sur
le site, pour ne pas affirmer quelque chose de faux. Dites-moi ce que vous
vouliez : une mention de partenaire, un lien en pied de page, ou simplement une
référence visuelle pour le motion, et je l'ajoute correctement.

---

## Obligations liées à la vente sous votre marque

Vendre ce matériel sous votre nom fait de vous le fabricant au sens du règlement
européen sur la sécurité générale des produits. Cela ajoute aux points déjà
listés plus haut :

- nom, raison sociale et adresse postale **et électronique** du fabricant visibles
  sur la fiche produit ;
- un identifiant du produit, type ou référence de lot ;
- les avertissements et consignes de sécurité en français ;
- la déclaration UE de conformité, à réclamer au fabricant avant la première
  commande et à conserver dix ans.

Ces informations ne figurent pas encore sur le site parce que je ne les ai pas.
Elles doivent y être avant la première vente.

---

## Le paiement : Stripe, en autorisation seule

C'est le mode actif. `modePaiement: "php"` dans `assets/config.js`, et
`capture_manuelle => true` dans `paiement/config.php`.

La carte du client est **autorisée** et non débitée : sa banque bloque le
montant et ne le verse pas. C'est vous qui déclenchez le prélèvement, à la
main, depuis le tableau de bord Stripe.

### Les quatre choses à faire avant la première vente

**1. Copier la configuration.** Sur le serveur, dupliquez
`paiement/config.exemple.php` en `paiement/config.php`.

**2. Coller votre clé secrète.** Tableau de bord Stripe, Développeurs, Clés
API. Commencez par la clé `sk_test_` pour un essai, passez à `sk_live_`
ensuite. Cette clé vaut votre compte marchand : elle ne doit jamais sortir de
ce fichier. Un `.htaccess` interdit déjà de le servir, et un `.gitignore`
empêche de le versionner.

**3. Vérifier que le dossier exécute PHP.** Ouvrez
`https://borne-restaurants.fr/paiement/verifier-domaine.php?d=google.com`
dans un navigateur. Vous devez lire `{"domaine":"google.com","statut":"pris"}`.
Si vous voyez du code PHP, l'hébergement ne l'exécute pas et le paiement ne
marchera pas.

**4. Faire un achat d'essai** avec la clé `sk_test_` et la carte
`4242 4242 4242 4242`, date future, CVC au hasard. Vous devez retrouver dans
Stripe un paiement **à capturer**, pas un paiement réussi.

### Comment vous capturez

Tableau de bord Stripe, Paiements. Les commandes apparaissent avec la mention
**Non capturé** (*Uncaptured*). Vous ouvrez la ligne et vous cliquez sur
**Capturer**. Vous pouvez capturer un montant **inférieur** à l'autorisation,
ce qui est pratique pour une remise de dernière minute, mais jamais supérieur.

Pour renoncer à une commande, cliquez sur **Annuler** : le blocage est levé et
le client ne paie rien. C'est plus propre qu'un remboursement, qui lui laisse
une ligne au débit puis au crédit sur son relevé.

### Le piège, et il est sérieux

**Une autorisation non capturée est annulée par Stripe au bout de sept
jours.** L'argent retourne chez le client et il faut tout redemander.

Vos bornes partent de Chine. Si vous attendez l'expédition pour capturer,
vous perdrez le paiement à chaque commande. **Capturez à la confirmation de
commande**, dans les deux ou trois jours, pas au départ du colis. Les
conditions de vente et la page de paiement annoncent exactement cela au
client, donc vous êtes couvert : elles disent « à la confirmation de votre
commande, sous sept jours au plus tard ».

Si vous voulez vraiment ne débiter qu'à l'expédition, il faut une autre
mécanique que la capture différée : enregistrer le moyen de paiement à la
commande et créer le paiement au départ du colis. C'est faisable, ça demande
un webhook et un peu de code en plus, et le client doit l'accepter
explicitement. Dites-le si vous voulez partir là-dessus.

### Ce qui change pour le client

| | Avant | Maintenant |
|---|---|---|
| Bouton | Payer par carte | **Autoriser le paiement** |
| Libellé du total | Total à payer | **Montant autorisé** |
| Au-dessus du bouton | — | « Rien n'est débité aujourd'hui… » |
| Sur la page Stripe | — | le même message, via `custom_text` |
| Page de remerciement | « Le paiement est passé » | « Votre carte est autorisée » |
| Moyens de paiement | tous | **carte seule** |

Ce dernier point n'est pas un choix : Link, le prélèvement SEPA et les
paiements en plusieurs fois ne gèrent pas la capture différée. Les proposer
ferait refuser la session par Stripe.

Les trois mentions de l'écran, celle de la page Stripe, les CGV et la page de
confidentialité disent tous la même chose. Si vous repassez un jour en débit
immédiat (`capture_manuelle => false`), **repassez aussi `captureManuelle` à
`false` dans `assets/config.js`** et régénérez les pages, sinon vous
promettez à l'écran l'inverse de ce que fait la banque.

### Les paliers et les options sont revenus

Contrairement au mode boutique, le serveur calcule ici le total exact. Les
570 € et 540 € des paliers fonctionnent, et les deux options aussi.

Vérifié au navigateur contre un faux Stripe local, sur les pages construites :

```
1 borne                        720,00 € TTC   →  72 000 centimes
3 bornes + les deux options   2 407,20 € TTC  → 240 720 centimes
```

L'affichage client et le calcul serveur tombent au centime. La charge envoyée
porte bien `payment_intent_data[capture_method]=manual` et
`payment_method_types[0]=card`.

### Les prix sont recalculés côté serveur

`paiement/creer-session.php` ne fait **aucune** confiance aux montants envoyés
par le navigateur : il ne lit que la quantité et les deux cases d'options, puis
recalcule tout à partir de ses propres constantes. Sans cela, n'importe qui
achèterait la borne à un centime en modifiant la requête avec les outils de
développement.

Si vous changez un prix, changez-le **aux deux endroits** : les constantes
`PALIERS`, `PRIX_MISE_EN_SERVICE` et `PRIX_GARANTIE` dans
`paiement/creer-session.php`, et les `paliers` et `options` dans
`assets/config.js`. Le serveur a le dernier mot, donc un oubli côté config.js
se verra comme un total affiché qui ne correspond pas à la page Stripe.

### La boutique WooCommerce reste en secours

Le mode `"woocommerce"` et la fiche produit 7910 sur epicerie-saintbrieuc.fr
sont toujours en place. Si Stripe pose un problème le jour du lancement,
repassez `modePaiement` à `"woocommerce"` et régénérez : vous encaissez par la
boutique en attendant. Attention, dans ce mode le débit est immédiat et les
textes d'autorisation deviennent faux.

---

## Le paiement passe par votre boutique WooCommerce

**Ce mode n'est plus le mode actif** : le paiement se fait désormais par
Stripe en autorisation seule, décrit juste au-dessus. Cette section reste
parce que le mode fonctionne et sert de secours. Dans ce mode, la commande
rejoint le panier d'une boutique WooCommerce que vous possédez déjà.

### Pourquoi

La boutique `epicerie-saintbrieuc.fr` tourne sous WooCommerce avec l'extension
Stripe active, et elle a encaissé plus de quarante mille commandes. Sa
passerelle, son certificat, ses e-mails de confirmation et ses factures sont
rodés. Monter un deuxième tunnel de paiement à côté, c'est se créer une
deuxième surface à surveiller pour vendre le même produit.

Aucune clé secrète n'est donc nécessaire sur `borne-restaurants.fr`, et aucun
PHP n'a besoin d'y tourner pour le paiement.

### Ce qui a été fait sur la boutique

Une fiche produit a été créée, identifiant **7910**, intitulée « Borne de
commande tactile pour restaurant - écran Android sur pied ».

| | |
|---|---|
| Prix | 720 € (c'est le montant débité, voir plus bas) |
| Référence | `BORNE-CMD-01` |
| Visibilité | **masquée du catalogue** : la fiche n'apparaît ni dans la boutique, ni dans la recherche interne. On y arrive seulement par le lien depuis ce site |
| Photos | les deux visuels produit, importés dans la médiathèque |
| État | **brouillon** |

La fiche est encore en brouillon : la mise en ligne a été refusée par la
protection d'écriture sur site externe. **C'est la seule action qui vous
reste** : ouvrez la fiche dans l'administration WooCommerce et cliquez sur
Publier. Tout le reste est câblé et testé.

### Pourquoi 720 et pas 600

Aucun taux de TVA n'est enregistré dans cette boutique : WooCommerce débite
donc exactement le prix saisi. Le prix de la fiche est pour cette raison le
montant TTC, 720 €, et pas le 600 € hors taxes. La ventilation 600 € + 20 %
reste affichée partout côté client, et c'est votre comptabilité qui la porte.

Si vous activez un jour la TVA dans cette boutique, **repassez le prix de la
fiche à 600** le même jour, sinon vous facturerez 864 €.

### Ce que le bouton fait exactement

Vérifié au navigateur sur la page construite :

```
1 borne  →  https://epicerie-saintbrieuc.fr/commander/?add-to-cart=7910&quantity=1
2 bornes →  https://epicerie-saintbrieuc.fr/commander/?add-to-cart=7910&quantity=2
```

L'identifiant du produit est utilisé plutôt que l'adresse de la fiche, parce
qu'il ne change pas si vous renommez le produit ou modifiez son permalien.

### Les paliers et les options sont retirés dans ce mode

Le panier WooCommerce ne connaît qu'un article à un prix. Il ne peut donc pas
appliquer les 570 € et 540 € des paliers, ni ajouter la mise en service et
l'extension de garantie.

Le formulaire les retire donc tout seul quand ce mode est actif : les deux
cases d'options sont masquées, et la mention de remise dégressive est
remplacée par une invitation à appeler. Deux bornes affichent 1 440 € TTC, et
c'est bien 1 440 € qui seront débités.

C'est délibéré. Une remise promise à l'écran et absente au moment de débiter
produit un litige ; une remise accordée au téléphone produit un client.

### Le client est prévenu de la redirection

Une mention apparaît au-dessus du bouton de paiement, remplie depuis
`config.js` : elle nomme la boutique et le nom de domaine sur lequel il va
atterrir. Les conditions de vente le disent aussi.

Ne retirez pas cette mention. Un acheteur professionnel qui sort sa carte et
voit soudain le nom d'une épicerie referme l'onglet, et vous ne saurez jamais
pourquoi la commande n'est pas arrivée.

### Le point à surveiller

Si le visiteur a déjà des articles de l'épicerie dans son panier, ils
partiront dans la même commande que la borne. C'est rare, puisqu'il arrive par
`borne-restaurants.fr`, mais c'est possible. Si cela vous gêne, la parade est
une boutique WooCommerce dédiée, ou un plugin qui vide le panier à l'arrivée.

### Pour revenir à Stripe

Repassez `modePaiement` à `"lien"` et renseignez les trois liens de
`liensStripe`, ou à `"php"` si vous installez `paiement/creer-session.php` et
sa clé secrète. Les deux modes sont restés en place et fonctionnels.

---

## Le configurateur de borne

`commander.html` porte un configurateur complet, placé avant le paiement. Le
client y construit sa borne, la teste, puis paie. Tout se passe dans son
navigateur : rien n'est envoyé nulle part tant qu'il n'a pas réglé.

### Ce qu'il fait

Quatre onglets. **Enseigne** : nom, type d'établissement, couleur principale,
logo. **Carte et prix** : catégories, produits, descriptions, prix, photos.
**Photos** : les images se chargent depuis la carte, sont recadrées en carré et
ramenées à 420 px dans le navigateur, puis intégrées au fichier produit.
**Aperçu** : la borne tourne pour de vrai dans un cadre, et se télécharge.

Le fichier téléchargé est un HTML autonome d'une dizaine de kilo-octets, photos
comprises. Il s'ouvre sur n'importe quelle tablette, sans connexion : grille de
produits par catégorie, suppléments, panier, question sur place ou à emporter
avec le taux de TVA correspondant, numéro d'appel, retour automatique à
l'accueil au bout de sept secondes.

Une carte de démonstration est préchargée. Un configurateur vide décourage, et
celle-ci montre immédiatement ce que la borne sait afficher.

### Le choix du site

Deux solutions proposées à l'étape 3 : installation sur le site existant du
client, ou création d'un nouveau site. Dans le second cas, un champ permet de
saisir le nom de domaine souhaité.

### La vérification du nom de domaine

`paiement/verifier-domaine.php` interroge le registre du domaine par RDAP, le
protocole qui a remplacé whois. Ce n'est pas une estimation : un domaine absent
du registre renvoie 404, un domaine enregistré renvoie sa fiche. C'est la source
qui fait foi, et elle est plus fiable qu'une réponse générée.

La requête part du serveur, donc l'adresse IP du visiteur ne sort pas du site.
Si PHP n'est pas disponible ou si le registre ne répond pas, l'interface le dit
et annonce une vérification manuelle à la commande.

Testé depuis ce serveur : `google.com` et `borne-restaurants.fr` ressortent
pris, un nom inventé ressort libre.

### Où va la configuration

Elle est conservée dans le navigateur du client pour survivre à l'aller-retour
vers Stripe, et jointe à la commande. Le client garde son fichier de borne
téléchargé. Vous recevez sa configuration pour monter sa page.

---

## La vidéo de présentation

Votre film de motion design est sur la page d'accueil, entre la fiche produit
et le récit. Il a été réencodé en 720p à 2,6 Mo, contre 11,5 Mo à l'origine, et
porte une affiche extraite de la vidéo elle-même.

Il est en `preload="none"` : **rien ne se télécharge tant que le visiteur n'a
pas appuyé sur lecture**. Vérifié au navigateur, zéro requête vers le MP4 avant
le clic. C'est ce qui permet de mettre une vidéo d'une minute treize en haut de
page sans ralentir personne.

---

## Prix et TVA

| | HT | TTC |
|---|---|---|
| 1 borne | 600,00 € | 720,00 € |
| 2 bornes | 570,00 € l'unité | 684,00 € l'unité |
| 3 et plus | 540,00 € l'unité | 648,00 € l'unité |

Le montant mis en avant partout est le TTC, puisque c'est celui qui sera
débité. La livraison est annoncée offerte en France métropolitaine, et elle
figure comme avantage sur la page d'accueil, dans le récapitulatif de commande
et dans le déroulé de la vente.

Un changement de prix se fait dans `assets/config.js` pour les paliers, puis
dans `outils/articles.py` et `outils/construire.py` pour les mentions
rédactionnelles. Les trente pages se régénèrent ensuite d'un coup.

---

## Point bloquant : l'expédition depuis la Chine

La page annonce désormais que la tablette part de votre atelier. Cela change
deux choses par rapport à un envoi depuis la France, et les deux doivent être
tranchées avant la première vente.

**Le délai.** Les pages annoncent encore 4 à 7 jours ouvrés, ce qui correspond à
un envoi depuis un stock européen. Un envoi direct depuis la Chine se compte en
semaines. Corrigez ce délai partout, ou expédiez depuis un stock européen.

**Les droits et la TVA à l'import.** Si le colis part de Chine vers votre client
français, quelqu'un paie les droits et la TVA à l'entrée dans l'Union. Si ce
n'est pas vous, votre client recevra un appel du transporteur et une facture
surprise, après avoir payé un prix annoncé TTC. C'est exactement le scénario qui
produit un litige et un avis négatif.

La parade est d'expédier en DDP, droits et taxes payés par l'expéditeur, et de
le confirmer par écrit à votre transitaire. Tant que ce point n'est pas réglé,
ne lancez pas la vente : vous vendez un prix tout compris que vous ne tenez pas.

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
2. cPanel, puis **Gestionnaire de fichiers**, puis ouvrez le dossier du domaine.
   Sur o2switch, un domaine supplémentaire a sa propre racine dans le dossier
   personnel, pas dans `public_html` : ici c’est `/home/moau1329/borne-restaurants.fr`.
   `public_html` sert le domaine principal du compte, qui est un autre site.
3. Supprimez l’ancien `index.html` qui s’y trouve.
4. Cliquez sur **Téléverser** et envoyez le fichier `.zip` entier.
5. Revenez dans le dossier, sélectionnez l’archive d’un clic, puis **Extraire**
   dans la barre d’outils. Le bouton reste grisé tant que rien n’est sélectionné.
6. **Supprimez l’archive une fois extraite.** Laissée en place, elle reste
   téléchargeable par n’importe qui à l’adresse du site.

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
| Lecteur audio | démarre au premier clic, boucle, coupe, choix mémorisé, se retire si le fichier manque |
| Page envoyée **seule**, sans le dossier `assets/` | s’affiche complète : style, typographie, script |

Trois défauts ont été trouvés et corrigés, tous invisibles à la lecture du code. La
règle `.nav a` repeignait le bouton « Commander » en gris sur fond indigo par un effet
de spécificité. `element.hidden = false` n’a aucun effet sur un élément SVG, ce qui
empêchait les bornes 2 et 3 d’apparaître dans le configurateur. Et surtout, la première
version liait le style dans un fichier séparé, ce qui a suffi à afficher le site nu en
production : les pages embarquent désormais tout ce dont elles ont besoin.

Non testé ici, à faire de votre côté : rendu sur un iPhone et un Android réels, lecteur
d’écran, et un paiement de bout en bout avec une clé Stripe de test.
