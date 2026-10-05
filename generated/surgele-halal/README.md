# Surgelé Halal — thème « Tasty Crousty » + rangement des catégories

Livrables :

| Fichier | Rôle |
|---|---|
| `dist/surgele-halal-theme.zip` | Le thème, à téléverser dans **Apparence › Thèmes › Ajouter › Téléverser** |
| `dist/surgele-halal-categories.zip` | Le plugin de rangement des catégories (WP-CLI **et** page Outils), à utiliser une fois |
| `surgele-halal-theme/` | Sources du thème (style.css, functions.php, gabarits, assets) |
| `surgele-halal-categories/` | Source du plugin |

---

## 1. Ce que fait (et ne fait pas) le thème

- **N'écrit rien en base.** Activer le thème ne crée, ne modifie et ne supprime aucun produit, catégorie, page, menu ou commande. Seuls ses réglages du Customizer sont enregistrés (dans les `theme_mods` du thème).
- Affiche le catalogue existant via les gabarits WooCommerce standards. Le thème surcharge seulement `archive-product.php`, `single-product.php` et `content-product.php`, avec les mêmes hooks que l'original pour que vos extensions continuent de fonctionner. Panier, commande et Mon compte gardent les gabarits et blocs WooCommerce d'origine, posés sur un « écran de mission » clair.
- Galerie produit WooCommerce : zoom, lightbox, slider.
- **Votre page d'accueil actuelle est la boutique.** Le thème le gère : sur la page 1 de l'accueil-boutique, il affiche le hero, les 3 zones, les best-sellers, les bandeaux garanties et réassurance, **puis** le catalogue complet. L'adresse, la pagination (`/page/2/`) et le nombre de produits par page (réglé dans Personnaliser › WooCommerce › Catalogue) ne changent pas. Si vous définissez plus tard une page statique comme accueil, `front-page.php` affiche les mêmes sections.
- Permaliens produits (`/saintbrieuc/…`) et catégories (`/categorie-produit/…`) : inchangés, le thème n'y touche pas.
- Polices libres (Anton, Archivo, Bungee, licence OFL) **hébergées dans le thème** : aucun appel à Google, ce qui est plus rapide et évite le transfert d'IP vers Google (RGPD).
- JavaScript : un seul fichier natif (~9 Ko), sans jQuery. Les scripts jQuery « ajout au panier » et « fragments » de WooCommerce sont retirés des pages de liste. Panier, commande et fiches produits variables gardent ceux dont WooCommerce a besoin.
- Aucun élément Rockstar/GTA : pas de logo, police, personnage ni visuel propriétaire. Tout le graphisme est en CSS original.

## 2. Avant tout : la sauvegarde (obligatoire)

1. **Sauvegarde complète** (fichiers + base) depuis votre hébergeur (cPanel › Sauvegardes, ou l'outil de votre hébergeur) **ou** avec une extension (UpdraftPlus, BackWPup…). Téléchargez l'archive sur votre ordinateur.
2. En complément, exportez les produits : **Produits › Tous les produits › Exporter** → gardez le CSV.
3. Notez la référence de départ (elle servira à vérifier qu'aucun produit n'a disparu) :
   - nombre de produits publiés affiché dans **Produits › Tous les produits** (« Publiés (N) ») ;
   - ou en WP-CLI : `wp post list --post_type=product --post_status=publish --format=count`
   - notez aussi le thème actif actuel (Apparence › Thèmes) pour pouvoir y revenir.
4. Idéalement, faites tout d'abord sur un **site de préproduction** (staging) si votre hébergeur en propose un.

## 3. Installation du thème, pas à pas

1. **Apparence › Thèmes › Ajouter › Téléverser un thème** → choisissez `surgele-halal-theme.zip` → **Installer maintenant**.
2. **Ne l'activez pas tout de suite** : cliquez sur **Prévisualisation en direct**. Vous voyez le site avec le nouveau thème, sans que les visiteurs le voient.
3. Dans la prévisualisation (Customizer), réglez :
   - **Identité du site** : votre logo (sinon un logotype typographique s'affiche).
   - **Surgelé Halal — Tasty Crousty** :
     - *Couleurs* : 5 couleurs modifiables. Gardez un fond très sombre pour que le texte reste lisible (contraste AA).
     - *Accueil — Hero & bandeau* : textes du bandeau défilant, badge « mission », titre, sous-titre, boutons, image optionnelle.
     - *Accueil — 3 zones* : la catégorie WooCommerce de chaque tuile (par défaut `poissons`, `poulet`, `crousty`) et leurs textes.
     - *Best-sellers & réassurance* : nombre de best-sellers et textes.
     - *Boutique — badges & performance* : badges Halal / Surgelé / Poids, et le « mode léger » (voir § 7).
     - *Pied de page & mentions légales* : choisissez votre page **Mentions légales**.
   - **Menus** : assignez votre menu existant à l'emplacement **Menu principal**, ou laissez-le vide : le thème affiche alors automatiquement *Poissons · Poulet · Crousty · Toute la boutique*. Emplacements optionnels : *Pied de page — liens* et *Pied de page — légal*.
4. Cliquez sur **Activer et publier**.
5. Videz les caches : extension de cache, cache serveur (o2switch / LiteSpeed…) et, si vous en avez un, le CDN.

Retour arrière : **Apparence › Thèmes** → réactivez l'ancien thème. Rien n'a été modifié en base, donc tout revient à l'identique.

## 4. Ranger les produits dans Poissons / Poulet / Crousty

Le plugin **ajoute** une de ces 3 catégories aux produits selon des mots-clés de leur titre. Il **ne retire jamais** de catégorie (vos catégories marques Almondy, AVS, Chef Zaki, Isla Délice… restent), et ne touche ni aux prix, ni aux stocks, ni aux descriptions, ni aux images.

Règles (titre comparé en minuscules, sans accents, mot entier). La première règle qui correspond l'emporte :

1. **Crousty** : tender(s), nugget(s), cordon(s) bleu(s), kebab, pané(e)(s), finger(s), burger, samoussa(s), crousty, croustillant, strips
2. **Poissons** : tilapia, dorade, maquereau(x), poisson(s), chinchard, sardine, merlu, colin, saumon, cabillaud, thon, crevette, calamar, capitaine, sole
3. **Poulet** : cuisse(s), haut de cuisse, aile(s), aileron, wings, pilon(s), manchon, poulet entier, poulet(s), poule(s), coquelet

L'ordre est voulu : « Tenders **de poulet** » va dans Crousty, pas dans Poulet. Les mots-clés se modifient avec le filtre PHP `sh_category_sorter_rules`.

### Installation

**Extensions › Ajouter › Téléverser une extension** → `surgele-halal-categories.zip` → **Activer**.

### A. Avec WP-CLI (SSH)

```bash
# 1. Simulation : liste les affectations, n'écrit RIEN
wp surgele ranger --dry-run

# (option) l'exporter pour la relire dans un tableur
wp surgele ranger --dry-run --format=csv > simulation.csv

# 2. Application (demande confirmation ; --yes pour l'éviter)
wp surgele ranger

# 3. En cas de besoin : annule la dernière exécution
#    (retire uniquement les liaisons ajoutées par l'outil)
wp surgele annuler
```

### B. Sans WP-CLI

**Outils › Ranger les catégories** → **1. Simuler** (tableau des affectations, aucune écriture) → vérifiez → **2. Appliquer ce rangement**. Un bouton **Annuler la dernière exécution** apparaît ensuite.

### Résultat attendu sur votre catalogue actuel (35 produits relevés le 05/10/2026)

Simulation exécutée sur une copie du catalogue (mêmes titres, WordPress 7.1.2, WooCommerce 11.1.2) :

- **Crousty (17)** : Burger Pané, Cordon Bleu Surgelé Halal, Nuggets, Kebab Poivrons, Tenders Piquant, Tenders, Kebab, Tenders Piquant ACHAHADA 2kg, Cordons Bleus Fromage Raclette, Tenders Nature ACHAHADA 2kg, Cordon Bleu 2kg, Fingers Dinde, Kebab 400g, Cordons Bleus Dinde, Tenders de poulet 360g, Tenders Hot Spicy, 5 Samoussas Dinde
- **Poissons (4)** : Chinchard, Maquereau, Dorade, Tilapia
- **Poulet (3)** : Wings Poulet Halal, Poule Fumée Halal Surgelée, Wings de poulet
- **Inchangés (11, aucun mot-clé)** : Schofrulade, Franui, Fraise Dubaï, Pot de glace Nutella, Allumette Frite, Kefta Bœuf, Gâteaux Milka / Daim / Toblerone, Lasagnes, Hachis Parmentier. Ils restent visibles dans la boutique et dans leurs catégories actuelles ; rangez-les à la main si vous voulez un rayon « Desserts » ou « Plats cuisinés ».

Vérifié sur cette copie : après application, titres, statuts, prix, stocks et SKU sont identiques (empreinte de base inchangée), seules 24 liaisons produit→catégorie ont été ajoutées ; un 2ᵉ passage n'ajoute rien ; `wp surgele annuler` restaure exactement l'état d'origine.

Une fois le rangement fait, vous pouvez désactiver puis supprimer le plugin : les catégories restent. Gardez-le si vous voulez pouvoir annuler.

## 5. Vérifier que tous les produits sont toujours visibles

1. **Comptage** : *Produits › Tous les produits* → « Publiés (N) » doit être identique à la référence notée au § 2. En WP-CLI : `wp post list --post_type=product --post_status=publish --format=count`.
2. **Boutique** : ouvrez l'accueil, descendez à « Tout le catalogue ». Le texte « Affichage de 1–X sur **N** résultats » doit afficher le même N. Parcourez les pages 1, 2… jusqu'à la dernière.
3. **Catégories** : *Produits › Catégories* : les compteurs des marques (Almondy, AVS, Chef Zaki, Isla Délice) sont inchangés ; Poissons / Poulet / Crousty affichent 4 / 3 / 17.
4. **Fiches** : ouvrez 3 ou 4 anciennes adresses produit (ex. `/saintbrieuc/tilapia/`, `/saintbrieuc/wings-poulet-halal/`) : elles s'ouvrent, avec la galerie (zoom au survol, loupe → lightbox).
5. **Tunnel de commande** : ajoutez un produit simple depuis une liste (le mini-panier s'ouvre), un produit variable depuis sa fiche, puis allez jusqu'à la page Commande. Passez une commande test si vous avez un moyen de paiement test.
6. **Gabarits** : *WooCommerce › État › Modèles* : les 3 surcharges du thème y figurent. Si WooCommerce en signale une « obsolète » après une mise à jour majeure, le site continue de fonctionner (mêmes hooks), mais signalez-le pour mise à jour.
7. **Search Console** (sous 1–2 semaines) : pas de hausse des erreurs 404 ni de pages exclues.

## 6. SEO et données structurées

- Balises sémantiques (`header`, `nav`, `main`, `footer`), un seul `h1` par page (le hero sur l'accueil, le nom de la catégorie ou du produit ailleurs), fil d'Ariane.
- **Schema Product** : le thème n'en émet **pas** de second. Il garde celui de WooCommerce, que Yoast SEO / Yoast WooCommerce SEO reprennent ou remplacent selon votre configuration, ce qui évite les doublons. Il ajoute seulement `brand` quand il manque, à partir des catégories marques listées dans le Customizer (*Pied de page › slugs des catégories marques* : `almondy,avs,chef-zaki,isla-delice` par défaut).
- Fil d'Ariane : celui de Yoast s'il est activé dans Yoast (cohérent avec son BreadcrumbList), sinon celui de WooCommerce.
- Après activation, testez une fiche avec le [test des résultats enrichis](https://search.google.com/test/rich-results) de Google.

## 7. Performance

- 1 CSS (49 Ko non minifié, ~10 Ko en gzip), 1 JS natif en `defer`, 3 polices WOFF2 (67 Ko au total, sous-ensemble latin), préchargement de la police des titres.
- Hero 100 % CSS (aucune image à charger), animations coupées si le visiteur a activé « réduire les animations ».
- Lazy-load natif des images WordPress / WooCommerce.
- **Mode léger** (activé par défaut) : l'ajout au panier depuis les listes passe par l'API Store de WooCommerce sans jQuery. Si une extension dépend du panier jQuery de WooCommerce (quick-view, upsell en pop-up…), décochez-le dans *Personnaliser › Boutique — badges & performance*. Sans JavaScript, les boutons restent de simples liens « ajouter au panier » qui fonctionnent.

## 8. Accessibilité (audit)

Audit axe-core (règles WCAG 2.0/2.1 A et AA) sur l'accueil, une catégorie, un produit variable et un produit simple, en 1440 px et en 390 px : **0 violation** après corrections. Les problèmes trouvés venaient du CSS par défaut de WooCommerce et ont été corrigés : prix barré à 50 % d'opacité (3:1), fil d'Ariane gris #767676 (4,2:1), onglets #515151 (2,4:1).

Également en place : lien « Aller au contenu », focus visible jaune, cibles tactiles ≥ 44 px, menu mobile au clavier (Échap ferme), mini-panier en `dialog` modal avec focus piégé, Échap et retour du focus, compteur du panier annoncé, `prefers-reduced-motion`, mode contraste forcé, `lang` du site.

Limites de l'audit automatique : il ne couvre ni la pertinence des textes alternatifs de vos images produit (à remplir dans la médiathèque), ni un test avec lecteur d'écran réel. Faites un passage NVDA ou VoiceOver sur le tunnel de commande. Si vous changez les couleurs dans le Customizer, revérifiez le contraste (par ex. avec WebAIM Contrast Checker).

## 9. Points relevés sur le site actuel

- La fiche **Maquereau** utilise l'image de la dorade (`dorade-surgele.png`) : à corriger dans le produit.
- Des produits sans catégorie (Fraise Dubaï, Pot de glace Nutella, Allumette Frite…) apparaissent sous « Non classé » ; le plugin n'y touche pas.
- Le thème n'importe pas les réglages ni les widgets de l'ancien thème (en-tête, pied de page, constructeur de pages). Contrôlez la page Mentions légales et les pages construites avec un page builder après activation.
