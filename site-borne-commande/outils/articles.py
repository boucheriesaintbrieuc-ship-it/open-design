# -*- coding: utf-8 -*-
"""
Les articles du blog.

Un article = un dict. Le générateur les met en page, construit les données
structurées, le fil d'Ariane, la FAQ et le maillage interne.

Règles tenues sur l'ensemble du jeu, et vérifiées par outils/doublons.py :
- une requête principale par article, jamais la même que celle d'une autre page ;
- aucune phrase reprise d'un article à l'autre, bloc de conclusion compris ;
- le bloc de fin diffère à chaque fois : c'est le passage le plus exposé
  au copier-coller, donc celui qui ferait tomber le site en contenu dupliqué.
"""

ARTICLES = [

# =========================================================================
{
 "slug": "tablette-tactile-pour-restaurant",
 "accroche": "Luminosité, verre, doigts gras, autonomie, rotation. Les seuils chiffrés, et pourquoi le processeur ne compte presque pas.",
 "cle": "tablette tactile pour restaurant",
 "titre": "Tablette tactile pour restaurant : les 5 critères qui comptent",
 "h1": "Tablette tactile pour restaurant : ce qu’il faut regarder avant d’acheter",
 "description": "Luminosité, verre, tactile gras, autonomie, rotation : les cinq points qui font qu’une tablette tient en salle ou meurt en six mois. Avec les valeurs chiffrées.",
 "date": "2026-10-06", "maj": "2026-11-04", "lecture": 7,
 "resume": "Une tablette grand public posée sur un comptoir de restaurant tient rarement une saison. Voici les cinq caractéristiques qui font la différence, avec les seuils chiffrés que nous appliquons.",
 "corps": """
<p>Beaucoup de restaurateurs commencent par poser une tablette familiale sur un support de bureau. Ça marche trois semaines. Puis l’écran devient illisible au soleil de mai, le tactile rate un appui sur quatre à cause des doigts gras, et la batterie lâche parce qu’elle reste branchée douze heures par jour.</p>
<p>Le matériel destiné à la salle n’est pas plus cher par principe. Il est juste calculé pour un usage que personne n’impose à une tablette de salon.</p>

<h2>1. La luminosité, avant la taille de l’écran</h2>
<p>C’est le premier critère, et presque personne n’en parle. Une tablette grand public plafonne entre 200 et 300 cd/m². Placée face à une vitrine entre mai et septembre, elle devient un miroir.</p>
<p>Le seuil utilisable commence à 350 cd/m² pour un intérieur lumineux. En vitrine directe, il faut monter au-delà. Avant d’acheter, allez vous mettre à l’emplacement prévu à 13 h un jour de soleil et regardez votre téléphone à pleine luminosité : si vous peinez déjà, une tablette moins lumineuse ne passera pas.</p>
<p>La diagonale vient après. Entre 21 et 27 pouces, vous affichez des photos de produits assez grandes pour donner envie. En dessous, votre carte ressemble à une liste de courses.</p>

<h2>2. Le verre, parce que le premier accident est mécanique</h2>
<p>En restauration, la première panne n’est pas électronique. C’est un plateau, un coin de caisse, un sac de courses. Une dalle protégée par un verre trempé encaisse ; une dalle nue se fend.</p>
<p>Demandez l’épaisseur du verre, pas seulement le mot « trempé ». Quatre millimètres changent la vie d’un écran posé à hauteur de hanche dans un couloir de passage.</p>

<h2>3. Le tactile avec des doigts gras</h2>
<p>Vos clients sortiront d’un kebab, d’un burger ou d’une boulangerie. Ils toucheront l’écran avec des doigts qui ne sont pas propres, et c’est normal.</p>
<p>Un tactile capacitif correct ne s’en soucie pas. Un tactile bas de gamme commence à rater des appuis au bout de quelques mois, parce que la couche de gras modifie la capacitance de surface. Le test, si vous pouvez essayer un modèle : mouillez votre pouce, posez un peu de matière grasse dessus, et appuyez vingt fois de suite dans un coin de l’écran. Deux ratés sur vingt suffisent à décider.</p>
<p>Le traitement antitrace compte aussi, mais pour une autre raison : un écran couvert d’empreintes donne l’impression que personne ne nettoie la salle.</p>

<h2>4. L’autonomie, qui n’est pas un gadget</h2>
<p>Une tablette avec batterie intégrée se déplace. Vous la mettez en terrasse à midi, vous la rentrez le soir, vous la posez près de la porte un jour de marché. Sans batterie, vous êtes marié à une prise.</p>
<p>Ça change aussi le plan de salle : plus besoin de faire courir une rallonge dans un passage, ce qui est en pratique la première cause de chute dans un établissement recevant du public.</p>

<h2>5. La rotation entre paysage et portrait</h2>
<p>Un écran vertical affiche plus de produits dans une liste et occupe moins de largeur au sol. Un écran horizontal convient mieux à une carte avec des photos larges ou à un écran de cuisine.</p>
<p>Les deux ont leur usage, et vous ne saurez lequel vous convient qu’après deux semaines de service réel. Un support qui pivote vous évite de trancher à l’aveugle au moment de la commande.</p>

<h2>Ce que ça donne en pratique</h2>
<p>Si vous ne deviez retenir que trois chiffres pour comparer deux modèles : 350 cd/m² de luminosité, un verre trempé d’au moins 4 mm, et une diagonale entre 21 et 27 pouces en orientation verticale.</p>
<p>Tout le reste, processeur compris, est secondaire. Une interface de prise de commande demande très peu de puissance ; ce qui la fait ramer, c’est presque toujours un Wi-Fi saturé, pas le processeur.</p>
""",
 "faq": [
  ("Une tablette grand public peut-elle servir de borne de commande ?",
   "Techniquement oui, pendant quelques mois. Elle n’est pas conçue pour rester allumée douze heures par jour, sa luminosité ne tient pas face à une vitrine et son verre casse au premier choc de plateau. C’est une solution d’essai, pas une solution d’exploitation."),
  ("Quelle taille d’écran pour une tablette de restaurant ?",
   "Entre 21 et 27 pouces pour un usage en salle. En dessous de 21, les photos de produits deviennent trop petites pour déclencher un achat. Au-dessus de 27, vous payez surtout de l’encombrement au sol sans gagner en lisibilité."),
  ("Faut-il une tablette Android ou iPad ?",
   "Android dans la quasi-totalité des cas. Le mode kiosque, qui verrouille l’appareil sur une seule application, y est plus simple à mettre en place et ne demande pas d’abonnement de gestion de parc. Un iPad verrouillé proprement passe par un outil de supervision payant."),
  ("Le processeur a-t-il de l’importance ?",
   "Très peu. Une interface de commande affiche des images et des boutons, ce qui ne demande presque rien. Quand une borne rame en service, la cause est pratiquement toujours un réseau Wi-Fi saturé par les téléphones des clients, pas la puissance de l’appareil."),
 ],
 "offre": """
<p>C’est en cherchant ces cinq critères pour notre propre restaurant que nous avons fini par importer nos tablettes nous-mêmes. Nous avons une usine en Chine, et un restaurant à faire tourner : relier les deux était la seule façon d’obtenir le bon matériel sans payer le prix d’une borne de marque.</p>
<p>Celle que nous vendons coche les cinq points, pivote entre paysage et portrait, embarque sa batterie, et coûte <strong>499 € hors taxes, sans aucun abonnement</strong>.</p>
""",
 "voisins": ["borne-tactile-commande-prix", "borne-de-commande-ou-caisse-enregistreuse", "installer-borne-de-commande-restaurant"],
},

# =========================================================================
{
 "slug": "borne-tactile-commande-prix",
 "accroche": "Décomposition d’un devis à 3 000 €, poste par poste, jusqu’au total réel sur trois ans. Le matériel y pèse moins d’un dixième.",
 "cle": "borne tactile commande prix",
 "titre": "Borne tactile de commande : le vrai prix sur trois ans",
 "h1": "Pourquoi une borne tactile de commande coûte 3 000 € (et ce que vous payez vraiment)",
 "description": "Décomposition du prix d’une borne de commande : le matériel coûte rarement plus de 600 €. Voici où part le reste, et le calcul complet sur trois ans.",
 "date": "2026-10-13", "maj": "2026-11-04", "lecture": 8,
 "resume": "Un devis de borne tourne autour de 3 000 € plus un abonnement mensuel. Le matériel, lui, dépasse rarement 600 €. Voici la décomposition poste par poste et le coût réel sur trois ans.",
 "corps": """
<p>Quand nous avons demandé des devis pour équiper notre propre salle, les montants allaient de 2 400 à 4 100 € par borne, plus 59 à 149 € par mois. Personne n’expliquait à quoi correspondait l’écart.</p>
<p>Après avoir monté notre propre matériel, nous savons où part l’argent. Voici le détail, sans chercher à accabler qui que ce soit : certains de ces postes sont parfaitement justifiés.</p>

<h2>Le matériel : 400 à 700 €</h2>
<p>Un écran tactile de 21 à 27 pouces, un support sur pied, une carte Android et une alimentation. C’est tout. À ce prix, vous avez déjà un verre trempé et une luminosité correcte.</p>
<p>L’imprimante à tickets, quand elle est intégrée, ajoute 80 à 150 €. Le lecteur de carte bancaire certifié, 150 à 300 €, et il est souvent facturé séparément parce qu’il dépend de votre banque.</p>

<h2>Le logiciel : le poste qui ne s’arrête jamais</h2>
<p>C’est lui qui fait l’essentiel de la facture. Un abonnement à 89 € par mois représente 3 204 € sur trois ans, soit plus que le matériel. Et il continue l’année suivante.</p>
<p>Ce montant finance du développement réel : la mise à jour de la carte, l’interface avec votre caisse, l’hébergement, le support. Le problème n’est pas qu’il existe, c’est qu’il est présenté comme accessoire alors qu’il représente la majorité du coût.</p>

<h2>L’installation et la formation : 300 à 800 €</h2>
<p>Un technicien se déplace, visse le socle, paramètre le réseau, saisit votre carte et forme votre équipe. Une demi-journée facturée au tarif d’intervention.</p>
<p>Ce poste est souvent négociable, et parfois évitable : si vous savez brancher un écran et saisir une carte, vous le faites vous-même en deux heures.</p>

<h2>Le financement, qui gonfle le tout</h2>
<p>Beaucoup de contrats passent par une location financière sur 36 ou 60 mois. Le loyer paraît indolore, mais il porte un taux. Sur cinq ans, une borne affichée 3 000 € peut vous coûter 4 600 €, et le contrat est souvent ferme sur toute la durée.</p>
<p>Lisez toujours deux lignes du contrat : la durée d’engagement ferme, et ce qui se passe à l’échéance. Une reconduction tacite de 36 mois existe encore chez certains loueurs.</p>

<h2>Le calcul sur trois ans</h2>
<p>Pour une borne, avec un abonnement moyen à 89 € par mois et une installation à 450 € :</p>
<ul>
<li>Matériel et mise en service : 3 450 €</li>
<li>Abonnement sur 36 mois : 3 204 €</li>
<li>Total : <strong>6 654 €</strong>, soit 185 € par mois pendant trois ans</li>
</ul>
<p>Comparez ce chiffre à ce qu’une borne doit vous rapporter. Avec 40 commandes par jour passées à l’écran, un ticket moyen de 14 € et une hausse de panier de 10 %, vous dégagez environ 1 450 € de chiffre d’affaires supplémentaire par mois. La borne reste rentable, mais elle absorbe 185 € par mois là où elle pourrait en absorber quinze.</p>

<h2>Ce qui est vraiment incompressible</h2>
<p>L’écran et le pied, oui. Le lecteur de carte si vous encaissez à la borne, oui. Le reste dépend de choix que vous pouvez reprendre en main, et le logiciel est le premier d’entre eux.</p>
""",
 "faq": [
  ("Pourquoi les bornes de commande sont-elles si chères ?",
   "Parce que le prix affiché mélange le matériel, qui coûte 400 à 700 €, et un logiciel vendu au mois qui représente la majorité du coût sur la durée du contrat. L’installation et le financement ajoutent encore plusieurs centaines d’euros."),
  ("Peut-on négocier le prix d’une borne de commande ?",
   "L’installation et la formation, souvent. Le loyer mensuel, rarement, car il est porté par un organisme de financement tiers et non par le vendeur. Demandez systématiquement le prix d’achat comptant à côté du loyer : l’écart est parlant."),
  ("Une borne de commande est-elle amortissable comptablement ?",
   "Une borne achetée est une immobilisation, amortissable sur sa durée d’usage, généralement trois à cinq ans. Une borne louée passe en charge d’exploitation. Votre comptable tranchera selon votre situation ; les deux se défendent."),
  ("Combien coûte une borne sans abonnement ?",
   "Le prix du matériel seul, une fois. Chez nous, 499 € hors taxes. Il vous reste à fournir le logiciel de prise de commande, soit par votre éditeur de caisse s’il en propose un, soit en le construisant vous-même."),
 ],
 "offre": """
<p>Notre réponse à ce calcul a été simple : nous fabriquons déjà du matériel en Chine, et nous avons un restaurant. Nous avons fait venir nos propres tablettes au lieu de signer un contrat à 185 € par mois.</p>
<p>Le même matériel, sans le reste, revient à <strong>499 € HT payés une fois</strong>. Sur trois ans, l’écart avec le devis ci-dessus dépasse 6 000 € par borne.</p>
""",
 "voisins": ["borne-de-commande-sans-abonnement", "tablette-tactile-pour-restaurant", "logiciel-borne-de-commande-ia"],
},

# =========================================================================
{
 "slug": "tablette-de-commande-restaurant-fonctionnement",
 "accroche": "Le trajet complet d’une commande, de l’écran au ticket cuisine. Et les trois maillons qui lâchent en service.",
 "cle": "tablette de commande restaurant",
 "titre": "Tablette de commande restaurant : comment ça marche vraiment",
 "h1": "Du doigt du client au ticket en cuisine : ce qui se passe dans une tablette de commande",
 "description": "Les sept étapes d’une commande passée sur tablette dans un restaurant, et les trois endroits où ça casse en pratique. Explication sans jargon.",
 "date": "2026-10-20", "maj": "2026-11-04", "lecture": 7,
 "resume": "Une commande passée à l’écran traverse sept étapes avant d’arriver en cuisine. Trois d’entre elles cassent régulièrement, et aucune n’est celle à laquelle on pense.",
 "corps": """
<p>La question revient à chaque démonstration : « et concrètement, ça arrive comment en cuisine ? » Voici le trajet complet, étape par étape, tel qu’il se déroule dans notre salle une centaine de fois par jour.</p>

<h2>Étape 1 : le client touche l’écran</h2>
<p>L’application tourne en mode kiosque. L’appareil démarre dessus, le client ne peut pas en sortir, et aucun bouton ne ramène à Android. C’est un réglage du système, pas une option payante.</p>

<h2>Étape 2 : il compose sa commande</h2>
<p>Produit, options, suppléments. C’est ici que le panier moyen se joue : l’écran propose le supplément à chaque commande, sans se lasser, là où une équipe en plein rush arrête de le faire vers 12 h 40.</p>

<h2>Étape 3 : sur place ou à emporter</h2>
<p>Question obligatoire avant le paiement, parce qu’elle détermine le taux de TVA appliqué à chaque ligne. Une application qui ne la pose pas vous laisse un problème à démêler au moment du bilan.</p>

<h2>Étape 4 : le paiement</h2>
<p>Trois configurations existent. Le client paie au comptoir avec un numéro de commande, ce qui ne demande aucun matériel supplémentaire. Il paie sur un lecteur de carte fixé à la borne. Ou il paie en ligne depuis son téléphone après avoir scanné un code affiché à l’écran.</p>
<p>La troisième option est la moins connue et la moins chère : elle ne demande ni lecteur certifié ni contrat monétique supplémentaire.</p>

<h2>Étape 5 : la commande part sur le réseau</h2>
<p>C’est le maillon faible. La tablette envoie la commande à votre caisse, à une imprimante de cuisine ou à un écran en cuisine, par le réseau local. Si le Wi-Fi est saturé par les téléphones de vos clients, cette étape ralentit ou échoue.</p>
<p>La parade tient en un câble : une liaison Ethernet entre la borne et votre routeur règle à elle seule la grande majorité des incidents de service.</p>

<h2>Étape 6 : impression ou affichage en cuisine</h2>
<p>Le ticket sort tel que le client l’a saisi. Le « sans oignon » ne se perd plus entre le comptoir et la plancha, et les plats refaits gratuitement disparaissent du service.</p>

<h2>Étape 7 : le numéro d’appel</h2>
<p>Le client reçoit un numéro, affiché sur un écran ou annoncé. Détail qui compte : un numéro visible libère la zone de retrait, là où une attente sans repère crée un attroupement devant le comptoir.</p>

<h2>Les trois endroits où ça casse</h2>
<p><strong>Le réseau</strong>, de loin le premier. Avant d’accuser la borne, regardez combien d’appareils partagent votre box.</p>
<p><strong>La carte mal saisie.</strong> Un supplément oublié dans le paramétrage, et le ticket cuisine est incomplet toute la journée. Faites relire votre carte par quelqu’un qui travaille en cuisine, pas seulement par vous.</p>
<p><strong>L’imprimante.</strong> Rouleau fini, capot mal refermé, papier thermique de mauvaise qualité qui laisse un ticket illisible après deux heures près d’une friteuse. Gardez deux rouleaux d’avance et n’achetez pas le papier le moins cher.</p>
""",
 "faq": [
  ("La tablette fonctionne-t-elle si internet tombe ?",
   "La prise de commande et l’impression en cuisine continuent, parce qu’elles passent par le réseau local et non par internet. Le paiement par carte, lui, a besoin de la liaison bancaire : il bascule au comptoir le temps de la coupure."),
  ("Faut-il obligatoirement une imprimante en cuisine ?",
   "Non. Un écran de cuisine affiche les commandes et évite le papier, le rouleau à changer et le ticket illisible. Beaucoup d’établissements gardent quand même l’impression en secours, parce qu’un écran éteint arrête le service."),
  ("Combien de temps un client met-il à passer commande sur tablette ?",
   "Entre 60 et 110 secondes pour une première commande, 40 à 60 secondes dès la deuxième visite. C’est plus long qu’au comptoir pour un habitué, mais la borne sert plusieurs clients en parallèle alors qu’une caisse en sert un seul."),
  ("Peut-on brancher la tablette sur n’importe quelle caisse ?",
   "Cela dépend de votre logiciel de caisse, pas de la tablette. Certains éditeurs proposent leur propre application de borne, d’autres ouvrent une interface, d’autres rien du tout. C’est la première question à poser à votre éditeur avant d’acheter du matériel."),
 ],
 "offre": """
<p>Les sept étapes ci-dessus, nous les faisons tourner tous les jours dans notre établissement, sur le matériel que nous importons nous-mêmes depuis notre usine.</p>
<p>La tablette est vendue nue, à <strong>499 € HT</strong>, sans abonnement : vous y installez l’application de commande qui vous va, et vous gardez la main sur les sept étapes.</p>
""",
 "voisins": ["installer-borne-de-commande-restaurant", "logiciel-borne-de-commande-ia", "borne-de-commande-kebab-pizzeria-snack"],
},
# =========================================================================
{
 "slug": "borne-de-commande-sans-abonnement",
 "accroche": "Le mensuel paie trois choses précises. Deux se reprennent facilement, la troisième demande un vrai arbitrage.",
 "cle": "borne de commande sans abonnement",
 "titre": "Borne de commande sans abonnement : pourquoi c’est si rare",
 "h1": "Borne de commande sans abonnement : ce que le mensuel paie réellement",
 "description": "Presque toutes les bornes se louent au mois. Voici les trois choses que cet abonnement finance, et comment chacune se remplace quand on accepte de s’en occuper.",
 "date": "2026-10-27", "maj": "2026-11-04", "lecture": 7,
 "resume": "Le mensuel d’une borne paie trois choses précises. Deux d’entre elles se remplacent sans difficulté, la troisième demande un vrai choix de votre part.",
 "corps": """
<p>Cherchez « borne de commande » et comparez les offres : la quasi-totalité se paie au mois. Entre 49 et 149 €, parfois en plus d’un achat de matériel. Ce n’est pas un hasard de marché, c’est un modèle économique délibéré, et il se défend.</p>
<p>Mais il n’est pas obligatoire. Pour savoir si vous pouvez vous en passer, il faut d’abord savoir ce qu’il contient.</p>

<h2>Ce que le mensuel finance, poste par poste</h2>

<h3>1. L’hébergement de votre carte</h3>
<p>Vos produits, vos prix et vos photos vivent sur un serveur. Quelqu’un paie ce serveur, le sauvegarde, le met à jour. Pour un restaurant, le coût réel se compte en quelques euros par mois.</p>
<p>C’est le poste le plus facile à reprendre : une application qui stocke la carte localement sur la tablette n’a besoin d’aucun serveur, et une carte de cinquante produits tient dans un fichier de quelques kilo-octets.</p>

<h3>2. Le développement continu</h3>
<p>Le logiciel évolue : nouvelles fonctions, corrections, adaptation aux versions d’Android. C’est un travail réel et récurrent, et c’est l’essentiel de ce que vous payez.</p>
<p>C’est aussi le poste qui a le plus changé ces deux dernières années, pour une raison qu’aucun vendeur n’a envie de mettre en avant : écrire une interface de prise de commande est devenu nettement moins coûteux.</p>

<h3>3. Le support</h3>
<p>Quelqu’un répond au téléphone un vendredi soir. Ça vaut de l’argent, et quand la borne encaisse vos clients, ça en vaut beaucoup.</p>
<p>C’est le seul poste des trois que vous ne pouvez pas remplacer par de la technique. Soit vous payez quelqu’un, soit vous acceptez de vous débrouiller, soit vous montez une installation assez simple pour qu’une panne ne vous arrête pas.</p>

<h2>Pourquoi le modèle au mois s’est imposé</h2>
<p>Du côté du vendeur, un client qui paie 89 € par mois pendant cinq ans rapporte 5 340 €. Le même client qui achète une borne 3 000 € rapporte 3 000 €, une fois. À matériel identique, le premier modèle vaut près du double.</p>
<p>Il permet aussi d’afficher un prix d’entrée bas, ce qui fait signer plus vite. Rien d’illégitime là-dedans : c’est le même raisonnement que celui d’un opérateur téléphonique. Il faut simplement savoir qu’on le subit.</p>

<h2>Ce que vous perdez vraiment en vous en passant</h2>
<p>Soyons clairs, parce qu’une page de vente honnête doit l’être. Sans abonnement :</p>
<ul>
<li>Personne ne met votre logiciel à jour à votre place.</li>
<li>Personne ne décroche à 21 h un samedi.</li>
<li>Si votre application vient d’un éditeur tiers, c’est à vous de suivre son évolution.</li>
</ul>
<p>En échange, vous ne payez rien tous les mois, vous n’êtes engagé nulle part, et vous pouvez changer de logiciel sans changer de matériel.</p>

<h2>Pour qui ce choix tient debout</h2>
<p>Il tient pour un indépendant ou un petit groupe qui a quelqu’un d’un minimum à l’aise avec un ordinateur, et dont le comptoir reste ouvert en permanence. La borne devient alors un canal de plus, pas une dépendance.</p>
<p>Il tient moins bien pour une structure où personne ne veut toucher à la technique et où la borne devient le seul point d’encaissement. Dans ce cas, payer quelqu’un pour qu’il réponde au téléphone est un investissement, pas une perte.</p>
""",
 "faq": [
  ("Une borne sans abonnement est-elle moins fiable ?",
   "Le matériel est le même. Ce qui change, c’est qui s’occupe du logiciel et qui répond en cas de panne. Une installation simple, où le comptoir reste ouvert, encaisse très bien une borne hors service le temps d’une réparation."),
  ("Que se passe-t-il si j’arrête de payer un abonnement de borne ?",
   "Dans la plupart des contrats, l’application cesse de fonctionner et la borne devient un écran inerte, même si vous l’avez achetée. Vérifiez ce point précis avant de signer : il détermine si vous possédez vraiment votre matériel."),
  ("Puis-je changer de logiciel sans changer de borne ?",
   "Oui, si la borne est une tablette Android ouverte et non un ensemble verrouillé par son éditeur. C’est la différence pratique entre acheter du matériel et louer un service qui se trouve avoir un écran."),
  ("Existe-t-il des applications de commande gratuites ?",
   "Certaines caisses incluent une application de borne dans leur offre existante, ce qui ne coûte rien de plus. Pour le reste, le gratuit durable est rare : une application maintenue par quelqu’un finit toujours par être payée par quelqu’un."),
 ],
 "offre": """
<p>Nous avons pris ce chemin pour notre propre salle avant de le proposer à d’autres. L’usine que nous avons en Chine fabrique déjà des écrans ; il ne restait qu’à les faire venir et à nous occuper du logiciel nous-mêmes.</p>
<p>La tablette part à <strong>499 € HT, une fois, sans mensualité et sans engagement</strong>. Si vous arrêtez de nous parler demain, elle continue de fonctionner.</p>
""",
 "voisins": ["borne-tactile-commande-prix", "logiciel-borne-de-commande-ia", "borne-de-commande-ou-caisse-enregistreuse"],
},

# =========================================================================
{
 "slug": "logiciel-borne-de-commande-ia",
 "accroche": "Une semaine pour la première version, six de plus pour qu’elle tienne un service. Et l’endroit où il ne faut surtout pas improviser.",
 "cle": "logiciel borne de commande",
 "titre": "Logiciel de borne de commande fait avec l’IA : notre retour",
 "h1": "Nous avons fabriqué le logiciel de notre borne avec l’IA : ce que ça donne au bout d’un an",
 "description": "Fabriquer son application de borne avec l’IA : le temps que ça prend, ce que ça couvre vraiment, et les trois limites rencontrées dans notre restaurant.",
 "date": "2026-11-03", "maj": "2026-11-04", "lecture": 9,
 "resume": "Nous avons construit l’application de notre borne nous-mêmes, avec de l’IA, pour notre restaurant. Voici le temps que ça a pris, ce que ça couvre, et les trois limites que nous avons rencontrées.",
 "corps": """
<p>Nous avons deux activités qui n’ont a priori rien à voir : une usine en Chine, et un restaurant. Le jour où il a fallu équiper la salle en bornes, les deux se sont rejointes.</p>
<p>Les devis tournaient autour de 3 000 € par poste, plus un mensuel. Pour une salle qui a besoin de deux écrans, l’addition devenait difficile à justifier. Nous avons fait venir nos propres tablettes, et il est resté la vraie question : le logiciel.</p>

<h2>Ce que fait réellement une application de borne</h2>
<p>Commencez par là, parce que la réponse est moins impressionnante qu’on ne le croit. Une borne affiche des produits, enregistre des choix, calcule un total, applique un taux de TVA, et envoie une commande à une imprimante.</p>
<p>Il n’y a ni intelligence, ni algorithme compliqué. C’est une liste, un panier et une sortie d’impression. Le travail d’un éditeur n’est pas dans la complexité, il est dans les cas particuliers et dans la fiabilité.</p>

<h2>Combien de temps ça a pris</h2>
<p>La première version utilisable a demandé environ une semaine de travail, en dictant à l’IA ce que nous voulions écran par écran. Pas une semaine à plein temps : des soirées et deux dimanches.</p>
<p>La version qui a tenu un service complet sans intervention est arrivée six semaines plus tard. L’écart entre les deux, ce sont exactement les cas particuliers : le client qui revient en arrière, la commande abandonnée à mi-chemin, le supplément indisponible, le rouleau d’imprimante qui se termine.</p>

<h2>Ce que l’IA fait bien</h2>
<p>Elle écrit vite une interface qui marche, et elle ne se trompe pas sur les choses répétitives : une grille de produits, un panier, un calcul de total, la mise en page sur un écran vertical.</p>
<p>Elle est aussi très utile sur ce que nous ne savions pas faire : verrouiller Android en mode kiosque, parler à une imprimante thermique, gérer une perte de réseau sans perdre la commande en cours.</p>

<h2>Les trois limites que nous avons rencontrées</h2>

<h3>1. Elle ne connaît pas votre salle</h3>
<p>Elle a proposé un parcours en cinq écrans, très propre, très logique. Nos clients du midi ont abandonné au troisième. Il a fallu descendre à deux écrans en acceptant une interface moins élégante. Ce réglage-là ne s’obtient qu’en regardant de vraies personnes commander.</p>

<h3>2. La TVA ne se devine pas</h3>
<p>Le taux appliqué dépend du produit et du mode de consommation, pas du canal de vente. C’est le genre de règle où une erreur ne se voit pas tout de suite et se paie au bilan. Nous l’avons fait vérifier par notre comptable avant de mettre quoi que ce soit en service, et c’est le seul endroit où nous recommandons de ne pas faire confiance à une sortie d’IA sans contrôle.</p>

<h3>3. La conformité de l’encaissement ne s’improvise pas</h3>
<p>Dès que le logiciel enregistre des règlements, il entre dans le champ de la loi anti-fraude à la TVA, qui impose un logiciel d’encaissement inaltérable et une attestation. Cela ne se code pas en un dimanche, et cela ne s’achète pas non plus avec un écran.</p>
<p>Notre réponse a été de séparer les deux : la borne prend la commande et l’envoie à la caisse, c’est la caisse certifiée qui enregistre le règlement. L’architecture est plus simple et le problème disparaît.</p>

<h2>Ce que nous en retenons</h2>
<p>Faire son application de borne est devenu accessible à quelqu’un de méthodique, à condition de ne pas toucher à l’encaissement. Le gain n’est pas seulement le mensuel économisé : c’est de pouvoir changer un écran le mardi parce qu’on a vu le lundi que les clients hésitaient.</p>
<p>Ce n’est pas pour tout le monde. Si personne chez vous n’a envie d’ouvrir un ordinateur, achetez une solution complète et dormez tranquille. Si quelqu’un a cette envie, le matériel ne doit pas être ce qui vous bloque.</p>
""",
 "faq": [
  ("Faut-il savoir programmer pour faire son application de borne ?",
   "Pas au sens classique, mais il faut être méthodique et accepter de tester longuement. Savoir décrire précisément ce que doit faire chaque écran compte plus que connaître un langage. Comptez plusieurs semaines avant une version qui tient un service réel."),
  ("Une application faite avec l’IA est-elle légale pour un restaurant ?",
   "Pour prendre des commandes, oui, sans restriction particulière. Pour enregistrer des règlements, elle entre dans le champ de la loi anti-fraude à la TVA et doit être certifiée, ce qui n’est pas réaliste en autoproduction. La solution est de laisser l’encaissement à votre caisse."),
  ("Combien coûte un logiciel de borne fait soi-même ?",
   "Le temps que vous y passez, plus un abonnement à un outil d’IA, de l’ordre de quelques dizaines d’euros par mois pendant la phase de construction. Après, l’application tourne sur la tablette sans rien coûter."),
  ("Peut-on reprendre une application existante plutôt que la refaire ?",
   "Souvent la meilleure option. Demandez d’abord à votre éditeur de caisse s’il propose une application de borne : si oui, vous n’avez besoin que du matériel, et vous évitez entièrement ce chantier."),
 ],
 "offre": """
<p>Nous ne vendons pas ce logiciel : il est taillé pour notre carte et il ne vous servirait pas tel quel. Nous vendons le matériel sur lequel il tourne, et nous expliquons volontiers comment nous l’avons fait.</p>
<p>La tablette, écran pivotant et batterie intégrée, est à <strong>499 € HT sans abonnement</strong>. Elle est livrée nue, sous Android ouvert, prête à recevoir l’application que vous choisirez ou celle que vous construirez.</p>
""",
 "voisins": ["borne-de-commande-sans-abonnement", "tablette-de-commande-restaurant-fonctionnement", "borne-tactile-commande-prix"],
},

# =========================================================================
{
 "slug": "borne-de-commande-kebab-pizzeria-snack",
 "accroche": "Carte qui bouge, options partout, pas de contrat de maintenance. Le réglage d’un indépendant n’est pas celui d’une chaîne.",
 "cle": "borne de commande kebab",
 "titre": "Borne de commande pour kebab, pizzeria et snack",
 "h1": "Borne de commande en kebab, pizzeria ou snack : ce qui change vraiment",
 "description": "Les bornes sont pensées pour les chaînes. En kebab, pizzeria ou snack indépendant, quatre choses diffèrent et changent le réglage de la carte à l’écran.",
 "date": "2026-11-04", "maj": "2026-11-04", "lecture": 6,
 "resume": "Les bornes du marché sont conçues pour des chaînes à carte figée. Un indépendant travaille autrement, et quatre différences changent complètement le paramétrage.",
 "corps": """
<p>Les bornes que vous voyez dans les grandes enseignes ont été pensées pour une carte stable, validée au siège, identique dans trois cents établissements. Un kebab de quartier ne fonctionne pas comme ça, et appliquer le même réglage donne un résultat médiocre.</p>

<h2>1. Votre carte bouge, la leur non</h2>
<p>Chez une chaîne, un changement de carte passe par un service marketing et se déploie une fois par trimestre. Chez vous, la pizza du jour change le jeudi et le fournisseur de salade vous lâche un mardi.</p>
<p>Conséquence pratique : exigez de pouvoir modifier un prix ou mettre un produit en rupture depuis votre téléphone, en moins d’une minute. Une solution qui demande un ticket au support pour masquer un produit épuisé vous fera perdre des clients avant midi.</p>

<h2>2. Vous vendez des options, pas des produits</h2>
<p>Un menu de chaîne, c’est trois choix. Un kebab, c’est le pain, la viande, les crudités, cinq sauces, la cuisson des frites et le supplément fromage. La combinatoire est énorme.</p>
<p>C’est une bonne nouvelle pour une borne : elle gère ces enchaînements sans se tromper, là où l’oral en perd toujours une partie. Mais cela impose un parcours bien construit. La règle que nous appliquons : jamais plus de huit choix sur un même écran, et les options les plus prises en premier.</p>

<h2>3. Votre clientèle n’est pas celle d’un centre commercial</h2>
<p>Vous avez des habitués qui commandent la même chose depuis trois ans, des ouvriers pressés à 12 h 10, des familles le vendredi soir. Les habitués iront au comptoir, et c’est très bien : ils vous font gagner du temps en parlant.</p>
<p>La borne sert surtout le flux du midi et les clients qui hésitent. Prévoyez qu’une partie de votre salle ne l’utilisera jamais, et ne dimensionnez pas votre projet en supposant l’inverse.</p>

<h2>4. Personne ne va venir vous dépanner en vingt minutes</h2>
<p>Une chaîne a un contrat de maintenance et un stock de pièces. Vous, non. Ce qui veut dire que votre installation doit continuer de tourner sans la borne, sans réflexion et sans bidouille.</p>
<p>Gardez le comptoir opérationnel en permanence. Une borne est un canal supplémentaire ; le jour où elle devient le seul moyen de commander chez vous, la moindre panne devient une journée perdue.</p>

<h2>Le réglage qui marche chez un indépendant</h2>
<ul>
<li>Une seule borne pour commencer, posée dans les deux mètres après la porte, sur le côté.</li>
<li>Une sélection, pas le catalogue : vos quinze à vingt produits les plus vendus, pas les soixante de l’ardoise.</li>
<li>Le parcours le plus court possible, quitte à être moins joli.</li>
<li>Le comptoir qui reste ouvert, toujours.</li>
</ul>
<p>Trois semaines de service suffisent à savoir si une deuxième borne se justifie. La mesure est simple : comptez la part des commandes passées à l’écran au pic de midi.</p>
""",
 "faq": [
  ("Une borne a-t-elle un intérêt dans un petit snack ?",
   "Oui si vous connaissez un pic où la file dépasse quatre personnes pendant que la cuisine suit. Non si vos plats sortent déjà en retard : la borne accumulerait alors des commandes plus vite que vous ne pouvez les produire, et dégraderait l’attente."),
  ("Combien de produits afficher sur la borne d’un kebab ?",
   "Quinze à vingt références au maximum sur l’écran d’accueil. Une carte complète de soixante lignes devient une liste que personne ne lit. Les habitués qui veulent un produit rare commanderont au comptoir, comme ils le font déjà."),
  ("La borne gère-t-elle les suppléments et les sauces ?",
   "C’est précisément ce qu’elle fait le mieux. Elle propose chaque option à chaque commande sans en oublier, là où une équipe en plein rush cesse de les proposer. C’est aussi la raison pour laquelle le panier moyen monte."),
  ("Faut-il une borne en extérieur pour la vente à emporter ?",
   "Seulement si le passage extérieur est réel et que vous pouvez sécuriser l’alimentation. Un écran prévu pour l’intérieur placé derrière une vitrine devient illisible l’été et s’abîme à l’humidité. Commencez à l’intérieur."),
 ],
 "offre": """
<p>Nous tenons un restaurant, pas un service commercial. Les quatre points de cette page viennent de notre propre salle, et le matériel dont nous nous servons sort de notre usine en Chine.</p>
<p>C’est celui que nous vendons : <strong>499 € HT, sans abonnement</strong>, avec un écran qui pivote en vertical pour tenir dans un couloir étroit.</p>
""",
 "voisins": ["tablette-de-commande-restaurant-fonctionnement", "installer-borne-de-commande-restaurant", "tablette-tactile-pour-restaurant"],
},
# =========================================================================
{
 "slug": "borne-de-commande-ou-caisse-enregistreuse",
 "accroche": "L’une enregistre les règlements et porte l’obligation légale, l’autre prend la commande. Confondre les deux coûte cher.",
 "cle": "borne de commande ou caisse enregistreuse",
 "titre": "Borne de commande ou caisse enregistreuse : lequel d’abord ?",
 "h1": "Borne de commande et caisse enregistreuse ne font pas le même travail",
 "description": "La borne prend la commande, la caisse enregistre le règlement. Comprendre cette séparation évite d’acheter deux fois la même chose, ou d’en oublier une.",
 "date": "2026-10-30", "maj": "2026-11-04", "lecture": 6,
 "resume": "Beaucoup de restaurateurs croient devoir choisir. Les deux appareils ne remplissent pas la même fonction, et seule la caisse a une obligation légale derrière elle.",
 "corps": """
<p>La confusion est fréquente, et elle coûte cher dans les deux sens : certains achètent une borne en pensant remplacer leur caisse, d’autres refusent la borne parce qu’ils ont déjà une caisse. Les deux se trompent de question.</p>

<h2>Deux fonctions distinctes</h2>
<p>La caisse enregistre les règlements. C’est elle qui tient votre chiffre d’affaires, édite le Z, ventile la TVA et vous sert en cas de contrôle. Elle est soumise à une obligation précise : l’article 286-I-3° bis du code général des impôts impose un logiciel d’encaissement inaltérable, avec une attestation délivrée par son éditeur.</p>
<p>La borne prend la commande. Elle affiche la carte, enregistre les choix du client et transmet. Elle n’a aucune obligation légale propre, parce qu’elle n’enregistre pas de règlement.</p>
<p>Une borne qui encaisserait vraiment, c’est-à-dire qui enregistrerait le paiement dans ses propres registres, deviendrait un logiciel de caisse et tomberait sous la même obligation. C’est pour cette raison que les bornes sérieuses renvoient toujours vers une caisse certifiée.</p>

<h2>Ce que vous devez avoir, dans l’ordre</h2>
<p>Une caisse conforme d’abord. Elle n’est pas optionnelle dès que vous encaissez des particuliers. Une borne ensuite, si et seulement si vous avez un problème de débit à régler.</p>
<p>Prendre les deux dans le mauvais ordre revient à acheter un deuxième four avant d’avoir une hotte.</p>

<h2>Le point qui décide : est-ce que les deux se parlent ?</h2>
<p>C’est la seule question technique qui compte avant d’acheter du matériel. Trois cas se présentent.</p>
<p><strong>Votre éditeur de caisse propose une application de borne.</strong> Le meilleur cas. Vous n’avez besoin que de l’écran, les commandes remontent toutes seules, votre Z est juste sans rien faire.</p>
<p><strong>Votre caisse ouvre une interface.</strong> Une application tierce peut lui envoyer les commandes. Cela marche, mais il faut vérifier ce qui remonte exactement : le détail des lignes, ou seulement un total.</p>
<p><strong>Votre caisse est fermée.</strong> La borne imprime alors en cuisine mais n’alimente pas votre chiffre d’affaires, et quelqu’un doit ressaisir. C’est une vraie limite, et elle doit être connue avant l’achat, pas découverte après.</p>

<h2>Et si je n’ai pas encore de caisse ?</h2>
<p>Commencez par là, en choisissant un éditeur qui propose déjà une application de borne. Vous réglez les deux sujets d’un coup et vous évitez de vous retrouver avec un écran orphelin.</p>
<p>Demandez l’attestation de conformité avant de signer, pas après. Un éditeur sérieux la fournit sans discuter ; les autres se font prier, ce qui est déjà une réponse.</p>

<h2>Le piège du « tout-en-un »</h2>
<p>Des offres proposent la caisse, la borne, le logiciel et le terminal de paiement dans un seul contrat mensuel. C’est confortable et parfois pertinent, surtout si vous partez de zéro.</p>
<p>Regardez simplement deux lignes avant de signer : ce qui se passe si vous arrêtez l’abonnement, et si le matériel vous reste. Dans beaucoup de contrats, tout s’éteint le même jour, y compris ce que vous pensiez avoir acheté.</p>
""",
 "faq": [
  ("Une borne de commande remplace-t-elle une caisse enregistreuse ?",
   "Non. La caisse enregistre les règlements et porte l’obligation de conformité fiscale ; la borne prend la commande et la transmet. Une borne qui enregistrerait elle-même les paiements deviendrait un logiciel de caisse soumis aux mêmes règles."),
  ("Faut-il une attestation de conformité pour une borne ?",
   "Pour le matériel, non. L’attestation prévue à l’article 286-I-3° bis du code général des impôts porte sur le logiciel qui enregistre les règlements, et c’est son éditeur qui la délivre. Réclamez-la à votre éditeur de caisse."),
  ("Peut-on installer une borne sans caisse du tout ?",
   "Techniquement oui, la borne imprimera en cuisine. Mais vous resterez tenu d’enregistrer vos encaissements avec un système conforme, donc le problème est seulement déplacé. Ce montage ne tient que pour un établissement qui n’encaisse pas de particuliers."),
  ("Quel budget prévoir pour les deux ?",
   "Une caisse conforme démarre autour de 30 à 80 € par mois selon l’éditeur, matériel compris ou non. Pour la borne, seul l’écran s’ajoute si votre caisse propose déjà une application, soit 499 € hors taxes chez nous, une fois."),
 ],
 "offre": """
<p>Nous vendons l’écran, pas la caisse, et c’est volontaire : votre caisse est déjà là et c’est elle qui doit rester le point de vérité de votre chiffre d’affaires.</p>
<p>La tablette sur pied est à <strong>499 € HT sans abonnement</strong>. Dites-nous quel logiciel de caisse vous utilisez : si rien ne s’y branche correctement, nous vous le dirons avant la vente plutôt qu’après.</p>
""",
 "voisins": ["tablette-de-commande-restaurant-fonctionnement", "borne-de-commande-sans-abonnement", "borne-tactile-commande-prix"],
},

# =========================================================================
{
 "slug": "installer-borne-de-commande-restaurant",
 "accroche": "Avant la file, jamais après. Les cotes à respecter, le câble à passer, et les quatre erreurs qui reviennent le plus.",
 "cle": "installer borne de commande restaurant",
 "titre": "Installer une borne de commande : emplacement et branchement",
 "h1": "Où poser une borne de commande dans un restaurant, et comment la brancher",
 "description": "Emplacement, dégagement, prise, réseau, accessibilité : le guide d’implantation d’une borne de commande, avec les cotes et les erreurs qui coûtent le plus cher.",
 "date": "2026-11-02", "maj": "2026-11-04", "lecture": 7,
 "resume": "Une borne mal placée ne sert à personne, même quand elle fonctionne parfaitement. Voici les cotes, le branchement et les quatre erreurs qui reviennent le plus souvent.",
 "corps": """
<p>Le matériel compte moins que l’endroit où vous le posez. Nous avons déplacé notre première borne trois fois avant de trouver la bonne place, et le taux d’utilisation a doublé entre le pire et le meilleur emplacement, sans rien changer d’autre.</p>

<h2>L’emplacement : avant la file, jamais après</h2>
<p>C’est la règle qui explique la plupart des échecs. Une borne placée derrière les gens qui attendent ne sert à rien : personne ne double une file pour aller vers un écran.</p>
<p>Le bon emplacement se trouve dans les deux premiers mètres après la porte, sur le côté, visible dès l’entrée. Le client doit la voir avant de décider de se mettre dans la file.</p>
<p>Deuxième critère : elle doit se voir depuis la rue si vous avez une vitrine. Un écran allumé visible de l’extérieur fait entrer des gens, surtout le soir.</p>

<h2>Les cotes à respecter</h2>
<ul>
<li><strong>Dégagement devant l’écran : 90 cm minimum.</strong> C’est la largeur nécessaire au passage d’un fauteuil roulant, et c’est aussi ce qui évite l’embouteillage quand deux clients se croisent.</li>
<li><strong>Hauteur de l’axe de l’écran : autour de 1,10 m.</strong> Un compromis entre un adulte debout et une personne assise. Un écran plus haut devient inatteignable, plus bas il oblige à se courber.</li>
<li><strong>Emprise au sol : comptez 40 cm de diamètre</strong> pour un socle rond, plus le dégagement.</li>
<li><strong>Deux bornes côte à côte : 1,40 m de large</strong>, sinon les clients se gênent et l’une des deux reste inutilisée.</li>
</ul>

<h2>L’électricité</h2>
<p>Une prise à moins de trois mètres, et le câble qui passe dans la colonne plutôt qu’au sol. Un câble qui traverse un passage finit arraché, et vous êtes responsable de la chute qui va avec.</p>
<p>Si vous ne pouvez pas rapprocher une prise, une borne avec batterie intégrée règle le problème : vous la rechargez la nuit et elle tient le service. C’est aussi ce qui permet de la sortir en terrasse à midi et de la rentrer le soir.</p>

<h2>Le réseau : le point qu’on néglige toujours</h2>
<p>Passez un câble Ethernet si vous le pouvez. Le Wi-Fi d’un restaurant est partagé avec les téléphones de vos clients, et il sature exactement au moment où vous en avez le plus besoin.</p>
<p>Un câble plat de quelques euros, glissé le long d’une plinthe, supprime à lui seul la majorité des incidents de service qu’on attribue à tort au matériel.</p>

<h2>Accessibilité : ce que dit la réglementation</h2>
<p>Un restaurant est un établissement recevant du public. Les équipements mis à disposition de la clientèle doivent être utilisables par les personnes handicapées, et l’arrêté du 20 avril 2017 fixe une zone d’atteinte entre 0,90 m et 1,30 m du sol pour les commandes.</p>
<p>Point important et souvent oublié : la borne ne doit pas être le seul moyen de commander. Un comptoir ouvert en permanence règle la question, et c’est de toute façon ce que vous voulez pour d’autres raisons.</p>

<h2>Les quatre erreurs qu’on voit le plus</h2>
<p><strong>La borne dans un coin.</strong> Elle est hors du flux, personne ne la voit, elle ne sert à rien.</p>
<p><strong>L’écran en veille noire.</strong> Un écran éteint ressemble à un écran en panne et les clients ne le touchent pas. Réglez la veille sur une image ou une animation, jamais sur du noir.</p>
<p><strong>Le câble au sol.</strong> Danger réel et aspect négligé. Passez-le dans la colonne ou prenez une borne sur batterie.</p>
<p><strong>L’équipe qui hèle les clients avant la borne.</strong> Si la personne au comptoir interpelle chaque client qui approche, personne n’utilisera l’écran. Le changement d’habitude de l’équipe compte autant que le matériel.</p>

<h2>Les trois premières semaines</h2>
<p>Comptez la part des commandes passées à l’écran au pic de midi, chaque jour. Si elle plafonne sous 15 % au bout de trois semaines, le problème est presque toujours l’emplacement, rarement la machine.</p>
""",
 "faq": [
  ("À quelle hauteur installer une borne de commande ?",
   "L’axe de l’écran autour de 1,10 m du sol, avec les commandes tactiles accessibles entre 0,90 m et 1,30 m, zone fixée par l’arrêté du 20 avril 2017 pour les établissements recevant du public. Au-delà, l’écran devient inatteignable pour une personne assise."),
  ("Faut-il fixer la borne au sol ?",
   "Pas obligatoirement si le socle est suffisamment lesté. La fixation devient utile dans un passage étroit, près d’une porte battante ou si des enfants circulent. Quatre chevilles suffisent et se retirent sans dégât."),
  ("Wi-Fi ou câble Ethernet pour une borne ?",
   "Câble dès que c’est possible. Le Wi-Fi d’un restaurant est partagé avec les téléphones des clients et sature au moment du pic. Un câble plat le long d’une plinthe coûte quelques euros et supprime la plupart des incidents de service."),
  ("Combien de temps prend l’installation d’une borne ?",
   "Environ un quart d’heure pour le montage et le branchement, sans outil particulier. Ce qui prend du temps, c’est la saisie de la carte et des options : comptez une à trois heures selon le nombre de produits et de suppléments."),
 ],
 "offre": """
<p>Les cotes de cette page sont celles que nous avons appliquées dans notre propre salle, après avoir déplacé la borne trois fois.</p>
<p>Le modèle que nous importons depuis notre usine tient sur 40 cm de socle, embarque sa batterie pour se passer de rallonge, et pivote en vertical pour les couloirs étroits. <strong>499 € HT, sans abonnement, livré monté.</strong></p>
""",
 "voisins": ["borne-de-commande-kebab-pizzeria-snack", "tablette-tactile-pour-restaurant", "tablette-de-commande-restaurant-fonctionnement"],
},

]
