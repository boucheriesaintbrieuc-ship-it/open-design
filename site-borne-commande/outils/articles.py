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
<p>Celle que nous vendons coche les cinq points, pivote entre paysage et portrait, embarque sa batterie, et coûte <strong>600 € hors taxes, sans aucun abonnement</strong>.</p>
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
   "Le prix du matériel seul, une fois. Chez nous, 600 € hors taxes. Il vous reste à fournir le logiciel de prise de commande, soit par votre éditeur de caisse s’il en propose un, soit en le construisant vous-même."),
 ],
 "offre": """
<p>Notre réponse à ce calcul a été simple : nous fabriquons déjà du matériel en Chine, et nous avons un restaurant. Nous avons fait venir nos propres tablettes au lieu de signer un contrat à 185 € par mois.</p>
<p>Le même matériel, sans le reste, revient à <strong>600 € HT payés une fois</strong>. Sur trois ans, l’écart avec le devis ci-dessus dépasse 6 000 € par borne.</p>
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
<p>La tablette est vendue nue, à <strong>600 € HT</strong>, sans abonnement : vous y installez l’application de commande qui vous va, et vous gardez la main sur les sept étapes.</p>
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
<p>La tablette part à <strong>600 € HT, une fois, sans mensualité et sans engagement</strong>. Si vous arrêtez de nous parler demain, elle continue de fonctionner.</p>
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
<p>Les devis tournaient autour de 3 000 € par poste, plus un mensuel. Pour une salle qui a besoin de deux écrans, l’addition devenait difficile à justifier. Nous avons fait venir nos propres tablettes, et il est resté le logiciel.</p>

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
<p>Faire son application de borne est devenu accessible à quelqu’un de méthodique, à condition de ne pas toucher à l’encaissement. Le mensuel économisé compte, mais moins que ça : on peut changer un écran le mardi parce qu’on a vu le lundi que les clients hésitaient.</p>
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
<p>La tablette, écran pivotant et batterie intégrée, est à <strong>600 € HT sans abonnement</strong>. Elle est livrée nue, sous Android ouvert, prête à recevoir l’application que vous choisirez ou celle que vous construirez.</p>
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
<p>C’est celui que nous vendons : <strong>600 € HT, sans abonnement</strong>, avec un écran qui pivote en vertical pour tenir dans un couloir étroit.</p>
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
   "Une caisse conforme démarre autour de 30 à 80 € par mois selon l’éditeur, matériel compris ou non. Pour la borne, seul l’écran s’ajoute si votre caisse propose déjà une application, soit 600 € hors taxes chez nous, une fois."),
 ],
 "offre": """
<p>Nous vendons l’écran, pas la caisse, et c’est volontaire : votre caisse est déjà là et c’est elle qui doit rester le point de vérité de votre chiffre d’affaires.</p>
<p>La tablette sur pied est à <strong>600 € HT sans abonnement</strong>. Dites-nous quel logiciel de caisse vous utilisez : si rien ne s’y branche correctement, nous vous le dirons avant la vente plutôt qu’après.</p>
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
<p>Le modèle que nous importons depuis notre usine tient sur 40 cm de socle, embarque sa batterie pour se passer de rallonge, et pivote en vertical pour les couloirs étroits. <strong>600 € HT, sans abonnement, livré monté.</strong></p>
""",
 "voisins": ["borne-de-commande-kebab-pizzeria-snack", "tablette-tactile-pour-restaurant", "tablette-de-commande-restaurant-fonctionnement"],
},
# =========================================================================
{
 "slug": "titres-restaurant-borne-de-commande",
 "accroche": "Plafond journalier, paiement mixte, émetteurs acceptés. La question que personne ne traite, et qui bloque une vente sur cinq le midi.",
 "cle": "titres restaurant borne de commande",
 "titre": "Titres-restaurant sur borne de commande : ce qu’il faut savoir",
 "h1": "Payer en titres-restaurant sur une borne de commande : comment ça se passe",
 "description": "Plafond de 25 € par jour, paiement mixte avec la carte bancaire, émetteurs acceptés : ce que votre borne doit savoir faire pour encaisser un titre-restaurant.",
 "date": "2026-11-05", "maj": "2026-11-05", "lecture": 6,
 "resume": "Une part importante de votre clientèle du midi paie en titres-restaurant dématérialisés. Si la borne ne sait pas les traiter, ces clients retournent au comptoir, et votre borne perd son intérêt à l’heure où elle devait servir.",
 "corps": """
<p>C’est la question qu’on nous pose le plus souvent après la démonstration, et c’est aussi celle qu’aucun comparateur ne traite. Nous avons cherché avant d’écrire cette page : on trouve des dizaines d’articles sur le plafond des titres-restaurant, aucun sur leur usage à une borne.</p>
<p>Le sujet n’est pourtant pas anodin. Dans un quartier de bureaux, les titres représentent souvent un tiers à la moitié des règlements du midi.</p>

<h2>Le plafond, d’abord</h2>
<p>Le montant maximal utilisable en titres-restaurant est de 25 € par jour, relevé de 19 à 25 € au 1<sup>er</sup> octobre 2022 et toujours en vigueur en 2026 selon les émetteurs. Ce plafond est journalier, pas par achat : un client peut le consommer en une fois ou le répartir sur plusieurs passages dans la journée.</p>
<p>Conséquence pratique pour vous : le plafond n’est pas vérifiable de votre côté. C’est la carte du client et le serveur de l’émetteur qui savent ce qu’il a déjà dépensé ailleurs le matin.</p>

<h2>Le vrai sujet : le paiement mixte</h2>
<p>Un client qui commande pour 31 € avec 25 € de solde disponible doit payer 6 € autrement. Avec une carte dématérialisée, le basculement vers la carte bancaire associée est automatique chez la plupart des émetteurs.</p>
<p>Mais cela se passe sur le terminal de paiement, pas dans votre logiciel de commande. Une borne qui calcule un total et renvoie vers un terminal n’a rien de particulier à gérer : c’est le terminal qui découpe le règlement.</p>
<p>En revanche, une borne qui prétend encaisser elle-même doit savoir afficher ce que le client vient de payer en titres et ce qui reste dû. Faute de quoi le client reste planté devant l’écran, et c’est à ce moment qu’il abandonne.</p>

<h2>Les trois montages possibles</h2>
<p><strong>Le client paie au comptoir.</strong> Le plus simple, et celui que nous utilisons. La borne prend la commande et édite un numéro, le règlement se fait au terminal du comptoir qui accepte déjà vos titres. Aucun matériel supplémentaire, aucun contrat à signer.</p>
<p><strong>Un terminal dédié à la borne.</strong> Vous ajoutez un lecteur accepté par les émetteurs. C’est le montage le plus fluide pour le client, et le plus coûteux pour vous, parce qu’il ajoute un contrat monétique et un loyer de terminal.</p>
<p><strong>Le paiement en ligne depuis le téléphone.</strong> Le client scanne un code affiché par la borne et paie sur son téléphone. Les cartes titres-restaurant fonctionnent en ligne chez les principaux émetteurs, mais vérifiez-le pour chacun avant d’annoncer quoi que ce soit à vos clients.</p>

<h2>Ce qu’il faut vérifier auprès de votre émetteur</h2>
<p>Vous êtes déjà affilié chez un ou plusieurs émetteurs, Edenred, Pluxee, Swile ou un autre. Votre affiliation porte sur votre établissement, pas sur un appareil : ajouter une borne ne demande en principe aucune démarche supplémentaire.</p>
<p>Deux points méritent quand même un appel : l’acceptation sur un nouveau terminal si vous en ajoutez un, et le traitement en ligne si vous passez par le téléphone du client.</p>

<h2>Le détail qui fait partir les clients</h2>
<p>Affichez les moyens de paiement acceptés sur l’écran d’accueil de la borne, avant que le client compose sa commande. Un client qui découvre au moment de payer que ses titres ne passent pas abandonne un panier déjà rempli, et il ne revient pas forcément le lendemain.</p>
<p>C’est un détail d’interface, il coûte deux minutes de paramétrage, et c’est celui qui a le plus d’effet sur le taux d’abandon au midi.</p>
""",
 "faq": [
  ("Peut-on payer en titres-restaurant sur une borne de commande ?",
   "Oui, dès lors que le règlement passe par un terminal accepté par votre émetteur, que ce soit le terminal du comptoir ou un lecteur fixé à la borne. La borne elle-même ne fait que transmettre un montant : c’est le terminal qui gère le titre."),
  ("Quel est le plafond journalier des titres-restaurant ?",
   "Vingt-cinq euros par jour depuis le 1er octobre 2022, toujours applicable en 2026. Le plafond porte sur la journée et non sur chaque achat, et il tient compte de ce que le salarié a dépensé ailleurs dans la même journée."),
  ("Que se passe-t-il si la commande dépasse le plafond ?",
   "Avec une carte dématérialisée, le montant excédentaire bascule automatiquement sur la carte bancaire associée chez la plupart des émetteurs. Votre interface doit simplement afficher clairement le reste à payer, sinon le client abandonne devant l’écran."),
  ("Faut-il une affiliation différente pour encaisser à la borne ?",
   "Non. Votre affiliation porte sur l’établissement et non sur l’appareil. Un appel à votre émetteur reste utile si vous ajoutez un terminal de paiement dédié à la borne ou si vous encaissez en ligne depuis le téléphone du client."),
 ],
 "offre": """
<p>Dans notre salle, les titres passent au comptoir et la borne ne fait que prendre la commande. C’est le montage le plus simple, et il n’a jamais posé de problème à un client.</p>
<p>La borne que nous vendons suit cette logique : elle prend la commande, le reste se règle où vous encaissez déjà. <strong>600 € HT, sans abonnement, sans contrat monétique supplémentaire.</strong></p>
""",
 "voisins": ["tablette-de-commande-restaurant-fonctionnement", "borne-de-commande-ou-caisse-enregistreuse", "commission-plateformes-livraison-vs-borne"],
},

# =========================================================================
{
 "slug": "borne-de-commande-boulangerie",
 "accroche": "Deux pics au lieu d’un, un panier à 4 € et des ruptures toute la matinée. La boulangerie ne se règle pas comme un fast-food.",
 "cle": "borne de commande boulangerie",
 "titre": "Borne de commande en boulangerie : ce qui change",
 "h1": "Borne de commande en boulangerie : deux pics, petits paniers et ruptures permanentes",
 "description": "Deux pics par jour, un panier moyen bas et des ruptures toutes les heures : pourquoi une borne en boulangerie demande un réglage très différent d’un fast-food.",
 "date": "2026-11-05", "maj": "2026-11-05", "lecture": 6,
 "resume": "Les bornes se vendent en pensant au fast-food. Une boulangerie travaille autrement : deux pointes dans la journée, un panier de quelques euros, et des produits qui disparaissent au fil des heures.",
 "corps": """
<p>Nous avons cherché ce qui existait sur le sujet avant d’écrire cette page. On trouve une fiche chez un comparateur, qui donne une fourchette de 2 000 à 7 000 € sans expliquer à quoi elle correspond, et rien d’autre. Le métier mérite mieux.</p>

<h2>Deux pointes, pas une</h2>
<p>Un fast-food concentre son flux entre 12 h et 13 h 30. Une boulangerie en a deux : le matin, court et dense, et le midi, plus long. Les deux ne posent pas le même problème.</p>
<p>Le matin, les clients savent ce qu’ils veulent et paient en quelques secondes. Une borne les ralentirait. Le midi, en revanche, le client hésite entre six sandwichs et une formule, et c’est là qu’un écran libère la vendeuse.</p>
<p>Conséquence : la borne doit pouvoir être mise en veille le matin et activée à 11 h 30. Si elle reste allumée toute la journée sur un écran de sandwichs, elle encombre sans servir.</p>

<h2>Un panier moyen qui change tout</h2>
<p>Un fast-food travaille autour de 12 à 15 € par commande. Une boulangerie tourne entre 3 et 8 €, hors formules du midi. La hausse de panier que vous pouvez espérer se compte donc en centimes, pas en euros.</p>
<p>Cela ne rend pas la borne inutile, mais cela change ce qu’elle doit viser. Son intérêt n’est pas d’augmenter le ticket, il est de faire passer plus de clients à l’heure, et d’éviter que la file déborde sur le trottoir.</p>
<p>Le calcul de rentabilité se fait donc sur le nombre de clients servis en plus, pas sur une hausse de panier. Comptez les gens qui repartent quand la file dépasse votre vitrine : c’est votre vrai gisement.</p>

<h2>Les ruptures, le point le plus sous-estimé</h2>
<p>À 11 h, il n’y a plus de pains au chocolat. À 13 h 15, il reste deux sandwichs sur sept. Une carte figée qui propose des produits épuisés fait trois choses, toutes mauvaises : elle fait perdre du temps au client, elle crée une réclamation au comptoir, et elle donne l’impression que la maison ne suit pas.</p>
<p>Vérifiez une chose avant d’acheter quoi que ce soit : combien de gestes faut-il pour masquer un produit épuisé. Si la réponse dépasse trois appuis sur un téléphone, la fonction ne sera jamais utilisée en plein service.</p>

<h2>La vente à la pièce et au poids</h2>
<p>Une boulangerie vend des produits à l’unité, parfois au poids pour les pâtisseries ou les parts de quiche. Toutes les applications de borne ne gèrent pas la vente au poids, parce qu’elles ont été écrites pour des burgers.</p>
<p>Si une part de votre chiffre se fait à la balance, ce point élimine la moitié des solutions du marché. Posez la question avant le devis.</p>

<h2>Où la poser dans une boutique étroite</h2>
<p>Les boulangeries ont souvent une surface de vente réduite et une file qui longe la vitrine. Une borne sur pied prend de la place dans le passage, et c’est le premier motif de retour que nous entendons.</p>
<p>Un écran en orientation verticale réduit l’emprise. Comptez 40 cm de socle et 90 cm de dégagement, et placez-la du côté opposé à la file pour qu’elle crée un second flux au lieu de doubler le premier.</p>
""",
 "faq": [
  ("Une borne de commande est-elle utile en boulangerie ?",
   "Surtout au service du midi, quand les clients hésitent devant les sandwichs et les formules. Le matin, les achats sont rapides et décidés d’avance : une borne y ralentit plutôt le passage. Prévoyez de pouvoir l’activer et la mettre en veille selon l’heure."),
  ("La borne gère-t-elle la vente au poids ?",
   "Cela dépend entièrement de l’application que vous installez. Beaucoup sont écrites pour la restauration rapide et ne prévoient que la vente à l’unité. Si une part de votre chiffre se fait à la balance, posez la question avant tout devis."),
  ("Comment gérer les produits épuisés en cours de journée ?",
   "Exigez de pouvoir masquer un produit en moins de trois gestes depuis un téléphone. Une fonction plus longue que cela ne sera jamais utilisée en plein service, et la borne continuera de proposer des viennoiseries qui n’existent plus."),
  ("Quelle place prend une borne dans une petite boutique ?",
   "Environ 40 cm de socle au sol, plus 90 cm de dégagement devant pour le passage. En orientation verticale, l’emprise reste contenue. Placez-la à l’opposé de la file existante, pour créer un second flux plutôt que d’allonger le premier."),
 ],
 "offre": """
<p>Notre écran pivote, ce qui règle précisément le problème de la boutique étroite : en vertical, il tient là où un écran large ne passe pas.</p>
<p>Il est vendu <strong>600 € HT, une fois, sans abonnement</strong>, et vous y installez l’application qui gère votre façon de vendre, y compris au poids si vous en avez besoin.</p>
""",
 "voisins": ["borne-de-commande-kebab-pizzeria-snack", "installer-borne-de-commande-restaurant", "tablette-tactile-pour-restaurant"],
},

# =========================================================================
{
 "slug": "borne-de-commande-food-truck",
 "accroche": "Pas de prise, pas de réseau, de la pluie et un comptoir qui bouge. Pourquoi une borne sur pied n’y a pas sa place, et ce qui marche.",
 "cle": "borne de commande food truck",
 "titre": "Borne de commande pour food truck : ce qui marche vraiment",
 "h1": "Food truck : pourquoi une borne sur pied n’est pas la bonne réponse",
 "description": "Alimentation, réseau mobile, pluie, rangement du soir : les quatre contraintes d’un camion qui éliminent la borne classique, et le montage qui fonctionne à la place.",
 "date": "2026-11-05", "maj": "2026-11-05", "lecture": 6,
 "resume": "Nous vendons des bornes, et nous allons vous expliquer pourquoi vous ne devriez probablement pas en poser une devant votre camion. Puis ce qui marche à la place.",
 "corps": """
<p>La demande revient régulièrement, et la réponse honnête commence par un refus. Une borne sur pied est pensée pour une salle : un sol plat, une prise, un réseau, et personne pour la faire tomber la nuit. Un camion ne coche aucune de ces cases.</p>

<h2>Les quatre contraintes d’un camion</h2>

<h3>Le sol</h3>
<p>Un socle lesté tient sur du carrelage. Sur un parking en pente, un sol gravillonné ou une place de marché, il bascule. Le premier coup de vent sur un écran plat de 50 cm de large suffit.</p>

<h3>L’alimentation</h3>
<p>Votre groupe ou votre raccordement sert déjà la plancha, la friteuse et la vitrine réfrigérée. Ajouter un poste permanent sur un circuit déjà chargé n’est pas une bonne idée, et tirer une rallonge au sol dans une zone de passage public l’est encore moins.</p>

<h3>Le réseau</h3>
<p>Pas de box, donc pas de Wi-Fi local. Vous dépendez de la 4G, qui s’effondre exactement là où vous travaillez le mieux : festivals, marchés, sorties d’usine à midi. Une installation qui a besoin du réseau pour prendre une commande vous lâchera au pire moment.</p>

<h3>Le rangement</h3>
<p>Tout ce qui sort doit rentrer en fin de service, en quelques minutes, souvent sous la pluie. Un écran sur pied de 20 kg, démonté et remonté deux fois par jour, ne tient pas une saison.</p>

<h2>Ce qui marche à la place</h2>
<p>Un écran tactile posé sur le comptoir du camion, côté client, relié à rien d’autre qu’à lui-même. Le client compose, l’écran affiche un numéro, vous préparez. Pas de pied, pas de prise obligatoire si l’appareil a sa batterie, pas de dépendance au réseau si l’application garde la carte en local.</p>
<p>C’est moins impressionnant qu’une borne, et c’est ce qui fonctionne. Le gain reste le même : la personne qui prenait les commandes retourne à la production.</p>

<h2>Les trois caractéristiques à exiger</h2>
<ul>
<li><strong>Une batterie.</strong> Elle vous dispense d’un circuit dédié et vous permet de servir pendant une coupure de groupe.</li>
<li><strong>Une carte stockée en local.</strong> L’appareil doit prendre les commandes sans réseau, et synchroniser plus tard. Posez la question explicitement : beaucoup d’applications affichent une page blanche hors ligne.</li>
<li><strong>Un écran lisible dehors.</strong> C’est le critère le plus dur à satisfaire. En plein soleil, un écran à 300 cd/m² est inutilisable, et l’auvent du camion ne suffit pas toujours. Testez l’appareil dehors avant de l’acheter, pas en boutique.</li>
</ul>

<h2>Le cas où une borne sur pied se justifie</h2>
<p>Un seul : un emplacement fixe, couvert, avec électricité, où vous revenez tous les jours. Une halle, un marché couvert permanent, une zone de food trucks aménagée. Là, la borne reprend tout son intérêt et vous rentrez dans le cas d’une salle.</p>
<p>Partout ailleurs, gardez l’écran sur le comptoir.</p>
""",
 "faq": [
  ("Peut-on installer une borne de commande devant un food truck ?",
   "Techniquement oui, mais le sol, l’alimentation, le réseau mobile et le rangement du soir s’y opposent dans la plupart des cas. Un écran posé sur le comptoir côté client rend le même service sans aucune de ces contraintes."),
  ("La commande fonctionne-t-elle sans réseau sur un marché ?",
   "Seulement si l’application garde votre carte en mémoire sur l’appareil. Beaucoup affichent une page blanche dès que la 4G faiblit. Demandez une démonstration en mode avion avant de choisir : c’est le test le plus parlant."),
  ("Quelle autonomie prévoir pour un service en extérieur ?",
   "De quoi tenir le service complet, en comptant que la luminosité maximale, nécessaire dehors, consomme nettement plus qu’en intérieur. Prévoyez aussi une batterie externe ou un point de recharge pour les journées de festival."),
  ("Un écran d’intérieur tient-il dehors ?",
   "Rarement. Sous 350 cd/m², il devient illisible en plein jour, et l’humidité abîme la connectique si l’appareil n’est pas protégé. Si votre service se fait au soleil, testez l’écran dehors avant l’achat, jamais en boutique."),
 ],
 "offre": """
<p>Nous préférons vous dire non sur le pied plutôt que de vous vendre un matériel qui finira rangé au fond du camion.</p>
<p>Cela dit, notre écran se démonte de sa colonne et embarque sa batterie : posé sur un comptoir, il rend exactement le service décrit ici, pour <strong>600 € HT sans abonnement</strong>. Appelez-nous avant de commander, on regardera votre configuration ensemble.</p>
""",
 "voisins": ["borne-de-commande-kebab-pizzeria-snack", "tablette-tactile-pour-restaurant", "borne-de-commande-boulangerie"],
},

# =========================================================================
{
 "slug": "augmentation-ticket-moyen-borne-chiffres",
 "accroche": "15 %, 25 %, 30 % : trois chiffres, aucune étude publique. D’où ils viennent et ce qu’on peut raisonnablement en retenir.",
 "cle": "augmentation ticket moyen borne de commande",
 "titre": "+15 à 30 % de ticket moyen : d’où sort ce chiffre ?",
 "h1": "La borne augmente le ticket moyen de 15 à 30 % : nous avons cherché la source",
 "description": "Tous les vendeurs de bornes annoncent 15 à 30 % de hausse du panier. Nous avons remonté la piste de ces chiffres, et voici ce qu’on peut honnêtement en conclure.",
 "date": "2026-11-05", "maj": "2026-11-05", "lecture": 7,
 "resume": "Le chiffre est partout et sa source nulle part. Voici ce que nous avons trouvé en remontant la piste, et la méthode pour estimer le gain chez vous sans croire personne sur parole.",
 "corps": """
<p>Lisez trois pages de vendeurs de bornes et vous verrez le même argument : la borne augmente le panier moyen de 15 à 30 %. Certains annoncent 25 %. Un comparateur attribue 15 % à un cabinet de conseil.</p>
<p>Nous vendons des bornes, et nous avons quand même cherché d’où venait ce chiffre, parce que c’est sur lui que des restaurateurs signent des contrats à 185 € par mois.</p>

<h2>Ce que nous avons trouvé</h2>
<p>Trois fourchettes circulent, publiées en novembre 2026 encore : 15 à 30 % chez un éditeur de logiciel de caisse, 25 % dans le guide d’un fournisseur de solutions de paiement, environ 15 % attribués à un cabinet d’audit par un troisième.</p>
<p>Aucune de ces pages ne renvoie vers une étude consultable. Pas de méthodologie, pas de périmètre, pas de taille d’échantillon, pas de date. Le chiffre attribué au cabinet d’audit ne pointe vers aucun document publié.</p>
<p>Cela ne veut pas dire que le chiffre est faux. Cela veut dire qu’il n’est pas vérifiable, et qu’il provient dans tous les cas d’acteurs qui vendent la solution.</p>

<h2>Pourquoi l’effet existe quand même</h2>
<p>Le mécanisme, lui, est solide et ne demande aucune étude pour être compris. Trois choses se produisent devant un écran, et elles jouent toutes dans le même sens.</p>
<p>Le client n’est pressé par personne, donc il lit la carte en entier. L’écran propose le supplément à chaque commande, là où une équipe en rush cesse de le faire vers 12 h 40. Et le client qui veut ajouter un dessert n’a plus à relancer quelqu’un qui est déjà passé à autre chose.</p>
<p>Ce qui est discutable, ce n’est pas l’existence de l’effet. C’est son ampleur, qui dépend entièrement de votre carte, de votre clientèle et de la part de commandes qui passe réellement à l’écran.</p>

<h2>Les trois raisons pour lesquelles le chiffre ne s’applique pas chez vous</h2>
<p><strong>Il porte sur les commandes de la borne, pas sur votre chiffre d’affaires.</strong> Si 30 % de vos commandes passent à l’écran et que leur panier monte de 20 %, votre chiffre global progresse de 6 %, pas de 20 %.</p>
<p><strong>Il dépend de ce que vous avez à vendre en plus.</strong> Un établissement avec six suppléments et trois desserts a de la matière. Une carte sans options n’a rien à proposer, et la borne ne crée pas de produits.</p>
<p><strong>Il suppose une carte bien paramétrée.</strong> Un parcours où le supplément arrive après le paiement ne vend rien. La moitié de l’écart entre deux établissements équipés du même matériel vient de là.</p>

<h2>Comment estimer le gain chez vous</h2>
<p>Prenez vos quatre derniers mois. Comptez le nombre de commandes au pic. Estimez la part qui passerait à l’écran, en restant pessimiste, disons un tiers au démarrage. Appliquez une hausse de panier que vous jugez plausible au vu de votre carte, pas celle d’une page de vente.</p>
<p>Multipliez, comparez au coût total sur trois ans, abonnement compris. Si le compte n’y est qu’avec 25 % de hausse, c’est que le projet ne tient pas.</p>
<p>Dans notre salle, nous observons un effet réel et nettement plus modeste que les chiffres affichés par la profession. Nous ne publions pas notre pourcentage, pour une raison simple : il vaut pour notre carte et il ne vous dirait rien d’utile.</p>
""",
 "faq": [
  ("La borne augmente-t-elle vraiment le ticket moyen ?",
   "Le mécanisme est réel : plus de temps pour lire la carte et un supplément proposé à chaque commande. L’ampleur, en revanche, dépend de votre carte et de la part de commandes passées à l’écran. Les fourchettes publiées par les vendeurs ne sont pas vérifiables."),
  ("D’où vient le chiffre de 15 à 30 % ?",
   "De pages commerciales d’éditeurs de logiciels et de fournisseurs de paiement, consultées en novembre 2026. Aucune ne renvoie à une étude publiée avec sa méthodologie et son échantillon, y compris celles qui citent un cabinet d’audit."),
  ("Comment calculer le gain réel pour mon établissement ?",
   "Multipliez votre nombre de commandes au pic par la part qui passerait à l’écran, puis par une hausse de panier que vous jugez plausible au vu de votre carte. Comparez au coût total sur trois ans, abonnement compris."),
  ("Une carte sans suppléments profite-t-elle d’une borne ?",
   "Beaucoup moins, parce que la borne ne crée pas de produits à vendre. Son intérêt se déplace alors vers le débit : servir plus de clients à l’heure de pointe, ce qui se mesure en nombre de commandes et non en panier moyen."),
 ],
 "offre": """
<p>Nous avons écrit cette page en sachant qu’elle dessert notre propre argumentaire. C’est volontaire : un restaurateur qui achète sur un chiffre gonflé revend son matériel six mois plus tard et le dit autour de lui.</p>
<p>Notre réponse à ce problème est ailleurs. À <strong>600 € HT sans abonnement</strong>, la borne est amortie avec une hausse de panier bien plus faible que celle que la profession annonce. Vous n’avez pas besoin de croire un chiffre pour que le calcul tienne.</p>
""",
 "voisins": ["borne-tactile-commande-prix", "borne-de-commande-sans-abonnement", "tablette-de-commande-restaurant-fonctionnement"],
},
# =========================================================================
{
 "slug": "tva-restauration-borne-de-commande",
 "accroche": "10 %, 5,5 % ou 20 % selon le produit et son contenant. La règle complète, et ce que l’écran doit demander au client.",
 "cle": "tva restauration rapide 10 ou 5,5",
 "titre": "TVA en restauration : 10 %, 5,5 % ou 20 % ? La règle",
 "h1": "TVA 10 %, 5,5 % ou 20 % : ce que votre borne doit demander avant le paiement",
 "description": "La règle complète des taux de TVA en restauration selon le produit, le mode de consommation et le contenant, et la question que l’écran doit poser au client.",
 "date": "2026-11-05", "maj": "2026-11-05", "lecture": 7,
 "resume": "Le taux ne dépend pas du canal de vente mais du produit et de son contenant. Une borne mal paramétrée ne crée pas d’erreur visible : elle la rend systématique, ligne après ligne, jusqu’au bilan.",
 "corps": """
<p>C’est le sujet sur lequel nous avons fait relire notre paramétrage par un comptable avant d’ouvrir, et c’est le seul endroit où nous déconseillons formellement de se fier à son intuition.</p>
<p>Une erreur de taux ne se voit pas. L’écran affiche un total juste, le client paie, la journée se passe bien. Elle apparaît en fin d’exercice, multipliée par le nombre de commandes.</p>

<h2>Les trois taux, et ce qui les déclenche</h2>
<p><strong>10 %</strong> : les ventes à consommer sur place, et les ventes à emporter de produits destinés à une consommation immédiate. Un sandwich, un plat chaud, une part de pizza emportée pour être mangée tout de suite.</p>
<p><strong>5,5 %</strong> : les produits à emporter conditionnés de façon à permettre leur conservation. Une boîte de conserve, un plat sous vide, un paquet de biscuits, une bouteille d’eau refermable.</p>
<p><strong>20 %</strong> : toutes les boissons alcoolisées, quel que soit le mode de consommation. Sur place ou à emporter ne change rien.</p>

<h2>Le piège du contenant</h2>
<p>C’est la partie qui surprend le plus. Pour une boisson non alcoolisée, le taux dépend du contenant.</p>
<p>Servie dans un gobelet, donc dans un contenant non refermable, elle est destinée à une consommation immédiate : 10 %. Vendue en bouteille refermable à emporter, elle relève de 5,5 %.</p>
<p>La même boisson, le même client, le même jour, deux taux différents selon que vous la servez au verre ou que vous lui tendez la bouteille. Une borne doit donc distinguer vos références au niveau du produit, pas au niveau de la commande.</p>

<h2>Ce que l’écran doit poser comme question</h2>
<p>Une seule, avant le paiement : sur place ou à emporter. Elle est indispensable pour trancher entre consommation immédiate et conservation, et elle doit être obligatoire, pas facultative.</p>
<p>Le reste se règle au paramétrage. Chaque produit porte son propre taux par défaut, et seuls ceux dont le taux change selon le mode de consommation doivent être liés à la réponse du client.</p>
<p>La ventilation doit ensuite remonter ligne par ligne à votre caisse, pas sous forme d’un total global. Un total global vous oblige à reconstituer la ventilation à la main, ce qui est exactement le travail que la borne était censée vous éviter.</p>

<h2>L’erreur de paramétrage la plus fréquente</h2>
<p>Appliquer un taux unique à toute une famille de produits. On range toutes les boissons à 10 % parce que la majorité part au gobelet, et les bouteilles vendues à emporter passent au mauvais taux toute l’année.</p>
<p>Prenez votre carte, et pour chaque ligne posez deux questions : contient-elle de l’alcool, et le client peut-il la refermer. Les deux réponses donnent le taux.</p>

<h2>Ce qui relève de votre comptable, pas de nous</h2>
<p>Nous vendons un écran et nous décrivons la règle telle que nous l’avons appliquée. Les situations particulières existent : vente de produits mixtes, formules associant plusieurs taux, activité de traiteur, livraison.</p>
<p>Faites valider votre table de taux avant de mettre quoi que ce soit en service. C’est une heure de votre comptable, et elle vous évite une régularisation qui se compte en milliers d’euros.</p>
""",
 "faq": [
  ("Quel taux de TVA pour un sandwich à emporter ?",
   "Dix pour cent, parce qu’il s’agit d’un produit destiné à une consommation immédiate. Le taux réduit de 5,5 % vise les produits conditionnés de façon à permettre leur conservation, ce qui n’est pas le cas d’un sandwich préparé à la demande."),
  ("Une boisson change-t-elle de taux selon le contenant ?",
   "Oui, pour les boissons non alcoolisées. Servie en gobelet non refermable, elle relève de la consommation immédiate à 10 %. Vendue en bouteille refermable à emporter, elle relève de 5,5 %. L’alcool reste à 20 % dans tous les cas."),
  ("La borne applique-t-elle le bon taux automatiquement ?",
   "Seulement si vous l’avez paramétrée produit par produit et si la question sur place ou à emporter est obligatoire avant le paiement. Aucune borne ne devine le taux : elle applique ce que vous avez saisi, correct ou non."),
  ("Qui est responsable en cas d’erreur de taux ?",
   "Vous, en tant qu’exploitant. Ni le fabricant de l’écran ni l’éditeur de l’application ne portent cette responsabilité. C’est la raison pour laquelle une relecture de votre table de taux par un comptable, avant la mise en service, est un investissement et non une dépense."),
 ],
 "offre": """
<p>Nous ne vendons pas de logiciel, donc nous ne paramétrons pas vos taux. Nous vous disons simplement, parce que nous sommes passés par là, de faire relire cette table avant d’ouvrir.</p>
<p>Le matériel, lui, est à <strong>600 € HT sans abonnement</strong>, et il accepte l’application de commande qui gère correctement votre carte.</p>
""",
 "voisins": ["borne-de-commande-ou-caisse-enregistreuse", "tablette-de-commande-restaurant-fonctionnement", "logiciel-borne-de-commande-ia"],
},

# =========================================================================
{
 "slug": "accessibilite-borne-de-commande",
 "accroche": "Zone d’atteinte, comptoir qui reste ouvert, et la directive européenne entrée en application le 28 juin 2025. Ce qui vous concerne vraiment.",
 "cle": "accessibilité borne de commande",
 "titre": "Accessibilité d’une borne de commande : les règles réelles",
 "h1": "Borne de commande et accessibilité : ce que la loi impose à votre établissement",
 "description": "Zone d’atteinte, obligation de maintenir une alternative, et portée réelle de la directive européenne accessibilité pour une borne de commande en restaurant.",
 "date": "2026-11-05", "maj": "2026-11-05", "lecture": 7,
 "resume": "Deux régimes se superposent : les règles françaises d’accessibilité des établissements recevant du public, et une directive européenne entrée en application en juin 2025 dont la portée exacte pour un restaurant mérite d’être précisée.",
 "corps": """
<p>Le sujet est traité nulle part correctement, et il revient dès qu’un exploitant accueille du public. Voici ce que nous avons compris, avec ce qui est certain et ce qui ne l’est pas.</p>

<h2>Ce qui est certain : votre établissement reçoit du public</h2>
<p>Un restaurant est un établissement recevant du public. À ce titre, les équipements mis à disposition de la clientèle doivent pouvoir être utilisés par les personnes handicapées.</p>
<p>L’arrêté du 20 avril 2017 fixe la zone d’atteinte des commandes entre 0,90 m et 1,30 m du sol. Un écran dont les boutons sortent de cette plage est hors des clous, même s’il fonctionne parfaitement.</p>
<p>Il faut aussi un dégagement de 90 cm devant l’appareil pour permettre l’approche d’un fauteuil, et un sol qui ne présente pas d’obstacle sur ce passage. Une rallonge qui traverse ce dégagement suffit à le disqualifier.</p>

<h2>La règle que presque personne n’applique</h2>
<p>La borne ne doit jamais être le seul moyen de commander. Un client qui ne peut pas utiliser l’écran, pour une raison de vue, de motricité ou simplement parce qu’il ne veut pas, doit pouvoir commander autrement.</p>
<p>Un comptoir ouvert en permanence règle la question entièrement. C’est de toute façon ce que vous voulez pour d’autres raisons : une borne en panne un vendredi soir ne doit pas arrêter votre service.</p>

<h2>La directive européenne : ce qui est entré en application</h2>
<p>La directive européenne sur l’accessibilité des produits et services s’applique depuis le 28 juin 2025. Elle impose à certains terminaux en libre-service une évaluation de conformité et un marquage CE spécifique.</p>
<p>La fiche publiée par la DGCCRF en juillet 2025 cite les terminaux de paiement, les distributeurs automatiques de billets de banque, les distributeurs de titres de transport et les distributeurs de tickets de file d’attente. Les bornes de commande en restauration n’y figurent pas nommément.</p>
<p>La raison tient au mécanisme du texte : il vise les terminaux utilisés pour fournir les services qu’il couvre, parmi lesquels la restauration ne figure pas. En revanche, dès que votre borne intègre un terminal de paiement, ce composant-là entre bien dans le champ.</p>
<p>Pour les appareils déjà en service avant le 28 juin 2025, la DGCCRF retient une période transitoire allant jusqu’à la fin de leur durée de vie économique, sans excéder quinze ans à compter de leur mise en service.</p>

<h2>Ce que nous en tirons comme consigne</h2>
<p>Nous ne sommes pas juristes et nous vous le disons. Notre lecture est que la borne de commande d’un restaurant n’est pas visée nommément, que le lecteur de carte qu’on y ajoute l’est, et que la situation est assez incertaine pour qu’il soit plus simple de concevoir accessible d’emblée.</p>
<p>Concrètement : respectez la zone d’atteinte, gardez le comptoir ouvert, exigez du fabricant sa déclaration de conformité, et faites valider votre installation si vous équipez plusieurs établissements.</p>

<h2>Les réglages qui coûtent zéro euro</h2>
<ul>
<li>Texte d’au moins 16 px, contraste franc entre le texte et le fond, jamais de gris clair sur blanc.</li>
<li>Boutons d’au moins 44 px de côté, espacés, pour une main qui tremble.</li>
<li>Pas de parcours chronométré : un écran qui revient à l’accueil au bout de dix secondes exclut tous ceux qui lisent lentement.</li>
<li>Aucune information portée par la couleur seule, un symbole ou un mot en plus.</li>
</ul>
<p>Ces quatre points relèvent du paramétrage de votre application. Ils améliorent l’usage pour tout le monde, y compris pour le client pressé de midi.</p>
""",
 "faq": [
  ("Une borne de commande doit-elle être accessible aux personnes handicapées ?",
   "Les équipements mis à disposition de la clientèle d’un établissement recevant du public doivent pouvoir être utilisés par tous. L’arrêté du 20 avril 2017 fixe la zone d’atteinte des commandes entre 0,90 m et 1,30 m du sol, avec 90 cm de dégagement devant."),
  ("La directive européenne accessibilité s’applique-t-elle aux bornes de restaurant ?",
   "La fiche DGCCRF de juillet 2025 cite les terminaux de paiement, les distributeurs de billets, de titres de transport et de tickets de file d’attente, sans nommer les bornes de restauration. Un lecteur de carte intégré à la borne relève en revanche du texte."),
  ("Peut-on n’avoir que des bornes et plus de comptoir ?",
   "Non. Un client qui ne peut pas ou ne veut pas utiliser l’écran doit disposer d’une alternative. Un comptoir ouvert en permanence règle la question, et il vous protège aussi le jour où la borne tombe en panne."),
  ("Que faire des bornes installées avant juin 2025 ?",
   "La DGCCRF prévoit une période transitoire : les terminaux en service avant le 28 juin 2025 peuvent continuer d’être utilisés jusqu’à la fin de leur durée de vie économique, dans la limite de quinze ans après leur mise en service."),
 ],
 "offre": """
<p>Notre écran se règle en hauteur selon le montage choisi, et son interface dépend de l’application que vous y installez : les quatre réglages gratuits listés plus haut sont donc entre vos mains.</p>
<p>Le matériel reste à <strong>600 € HT sans abonnement</strong>. Si vous équipez plusieurs établissements, dites-le nous : la question de la conformité ne se pose pas pareil à cette échelle.</p>
""",
 "voisins": ["installer-borne-de-commande-restaurant", "borne-de-commande-ou-caisse-enregistreuse", "tva-restauration-borne-de-commande"],
},

# =========================================================================
{
 "slug": "commission-plateformes-livraison-vs-borne",
 "accroche": "Une commande à 20 € vous laisse environ 14 € sur une plateforme. Le calcul complet, et ce que la même commande rapporte en direct.",
 "cle": "commission plateforme livraison restaurant",
 "titre": "30 % de commission : ce que les plateformes vous prennent",
 "h1": "Commission des plateformes de livraison : le calcul que peu de restaurateurs font jusqu’au bout",
 "description": "Ce qu’il reste d’une commande à 20 € passée par une plateforme de livraison, poste par poste, et ce que la même commande rapporte en vente directe.",
 "date": "2026-11-05", "maj": "2026-11-05", "lecture": 7,
 "resume": "La commission n’est pas le seul prélèvement. Entre le pourcentage, la TVA sur la commission et le coût matière inchangé, une commande livrée rapporte beaucoup moins qu’elle n’en a l’air.",
 "corps": """
<p>Les plateformes apportent du volume, et ce volume a de la valeur, surtout le soir et en hiver. Personne de sérieux ne dira le contraire.</p>
<p>Ce qui pose problème, c’est que peu de restaurateurs refont le calcul jusqu’au bout, parce que le versement arrive net et mensuel. On voit un virement, pas une ponction.</p>

<h2>Le calcul sur une commande à 20 €</h2>
<p>Prenons une commande de 20 € TTC, avec une commission de 30 % et un coût matière de 30 %, qui sont des ordres de grandeur courants en restauration rapide.</p>
<ul>
<li>Encaissé : 20,00 € TTC, soit 18,18 € hors taxes à 10 %</li>
<li>Commission de la plateforme : 6,00 € TTC sur le montant TTC, soit 5,00 € hors taxes</li>
<li>Coût matière : environ 5,45 € hors taxes</li>
<li>Reste avant charges de production : <strong>environ 7,73 € hors taxes</strong></li>
</ul>
<p>La même commande passée chez vous, à la borne ou au comptoir, laisse environ 12,73 € hors taxes avant les mêmes charges. L’écart est de 5 € par commande, soit 65 % de marge en plus.</p>
<p>Sur quarante commandes par jour et vingt-six jours par mois, l’écart atteint 5 200 € par mois. C’est le chiffre qui décide.</p>

<h2>Les prélèvements qu’on oublie</h2>
<p><strong>La commission porte sur le TTC.</strong> Vous payez donc un pourcentage sur une somme dont une partie ne vous appartient pas : la TVA que vous reversez à l’État.</p>
<p><strong>Le coût matière ne baisse pas.</strong> Il est identique que la commande vienne d’une plateforme ou de votre comptoir. Toute la commission sort donc de votre marge, pas de votre chiffre d’affaires.</p>
<p><strong>L’emballage de livraison coûte plus cher</strong> qu’un emballage à emporter classique, et il est rarement refacturé.</p>
<p><strong>Vous ne récupérez pas le client.</strong> Son nom, son adresse et ses habitudes restent chez la plateforme. Vous louez un flux, vous ne construisez pas une clientèle.</p>

<h2>Ce que ça ne veut pas dire</h2>
<p>Pas de quitter les plateformes. Une commande à 7,73 € de marge reste meilleure qu’une commande qui n’existe pas, et le volume couvre des créneaux que vous ne rempliriez pas autrement.</p>
<p>Cela veut dire qu’une commande en direct vaut environ une commande et demie passée par plateforme. Tout euro investi pour faire basculer des clients vers le direct se compare à ce ratio, pas à zéro.</p>

<h2>Où se situe une borne dans ce calcul</h2>
<p>Une borne ne remplace pas la livraison : elle sert les gens qui sont déjà entrés chez vous. Son rôle est ailleurs, dans le débit au comptoir et dans le panier.</p>
<p>Mais elle partage une propriété avec la vente directe, et c’est celle qui compte ici : elle ne prend aucun pourcentage. Une commande passée à l’écran vous laisse exactement ce qu’une commande passée au comptoir vous laisse, quel que soit son montant et quel que soit le volume.</p>
<p>C’est la différence de fond entre un équipement qu’on achète et un canal qu’on loue.</p>
""",
 "faq": [
  ("Quelle commission prennent les plateformes de livraison ?",
   "Les taux pratiqués se situent couramment autour de 30 % du montant TTC pour la livraison, moins pour la commande à emporter. Le pourcentage s’applique au TTC, donc aussi sur la part de TVA que vous reversez ensuite à l’État."),
  ("Combien rapporte réellement une commande livrée ?",
   "Sur une commande à 20 € TTC avec 30 % de commission et 30 % de coût matière, il reste environ 7,73 € hors taxes avant charges de production, contre environ 12,73 € pour la même commande vendue en direct."),
  ("Faut-il quitter les plateformes de livraison ?",
   "Rarement. Une commande à faible marge reste préférable à une commande inexistante, et le volume remplit des créneaux creux. L’enjeu est plutôt de savoir qu’une commande directe en vaut environ une et demie, et d’investir en conséquence."),
  ("Une borne de commande réduit-elle la dépendance aux plateformes ?",
   "Indirectement. Elle sert les clients déjà présents dans votre salle et ne prélève aucun pourcentage, quel que soit le volume. Elle améliore la marge sur le flux direct sans rien changer au flux de livraison."),
 ],
 "offre": """
<p>C’est exactement le raisonnement qui nous a poussés à acheter du matériel plutôt qu’à louer un service. Un équipement payé une fois ne prend rien sur votre croissance.</p>
<p>Notre borne coûte <strong>600 € HT, zéro euro par mois et zéro pourcentage sur vos ventes</strong>. Le jour où votre volume double, elle coûte toujours 600 €.</p>
""",
 "voisins": ["borne-de-commande-sans-abonnement", "borne-tactile-commande-prix", "augmentation-ticket-moyen-borne-chiffres"],
},
# =========================================================================
{
 "slug": "mode-kiosque-android-restaurant",
 "accroche": "Verrouiller une tablette sur une seule application, sans abonnement de supervision. La méthode, et ce qu’elle ne protège pas.",
 "cle": "mode kiosque android tablette",
 "titre": "Mode kiosque Android : verrouiller une tablette sur une seule app",
 "h1": "Verrouiller une tablette Android en mode kiosque pour un usage client",
 "description": "Comment bloquer une tablette Android sur une seule application de commande, sans outil de supervision payant, et les trois limites de cette méthode.",
 "date": "2026-11-05", "maj": "2026-11-05", "lecture": 6,
 "resume": "Un écran que le client peut quitter n’est pas une borne, c’est une tablette. Voici comment la verrouiller sans payer d’abonnement de supervision, et ce que ce verrouillage ne couvre pas.",
 "corps": """
<p>C’est la première chose à faire après avoir branché l’écran, et c’est aussi celle dont personne ne parle, parce qu’elle ne se vend pas. Une tablette laissée telle quelle finira avec un client sur un navigateur, un autre dans les réglages Wi-Fi, et un troisième qui aura installé quelque chose.</p>

<h2>Ce que fait réellement le mode kiosque</h2>
<p>Il fixe une application unique à l’écran, retire les boutons de navigation, empêche l’accès aux notifications et au panneau de réglages, et relance l’application si elle se ferme. L’appareil redémarre directement dessus après une coupure de courant.</p>
<p>Android propose cette fonction nativement, sous le nom d’épinglage d’écran dans les réglages de sécurité. C’est le niveau le plus simple, suffisant pour beaucoup de situations, et il ne coûte rien.</p>

<h2>Les trois niveaux, du plus simple au plus solide</h2>

<h3>1. L’épinglage d’écran</h3>
<p>Réglages, Sécurité, Épinglage d’écran. Vous l’activez, vous ouvrez votre application, vous l’épinglez. Pour en sortir, il faut une combinaison de touches et le code de déverrouillage.</p>
<p>Avantage : gratuit, immédiat, aucune installation. Limite : un client qui connaît la manipulation peut tenter d’en sortir, et il reste coincé devant le code. Cela suffit dans une salle où quelqu’un est toujours présent.</p>

<h3>2. Une application de kiosque</h3>
<p>Des applications dédiées remplacent l’écran d’accueil et contrôlent ce qui est accessible. Beaucoup sont gratuites dans leur version de base.</p>
<p>Elles ajoutent ce qui manque à l’épinglage : redémarrage automatique sur l’application, blocage de la barre de statut, plage horaire d’extinction, et parfois le redémarrage programmé de nuit, qui règle à lui seul la majorité des ralentissements.</p>

<h3>3. Le propriétaire d’appareil</h3>
<p>Le niveau professionnel. L’appareil est enrôlé dès sa première mise en route et devient impossible à sortir de son cadre sans réinitialisation complète. C’est ce qu’utilisent les chaînes.</p>
<p>Il demande une configuration sur ordinateur et, selon l’outil, un abonnement de supervision. Il se justifie à partir de plusieurs dizaines d’appareils, rarement en dessous.</p>

<h2>Les réglages à ne pas oublier</h2>
<ul>
<li><strong>Désactiver la mise en veille.</strong> Un écran noir ressemble à un écran en panne et les clients ne le touchent pas.</li>
<li><strong>Désactiver les mises à jour automatiques du système.</strong> Une mise à jour lancée à 12 h 15 immobilise la borne pendant le service.</li>
<li><strong>Figer l’heure et la langue</strong>, et retirer le compte Google s’il n’est pas nécessaire.</li>
<li><strong>Programmer un redémarrage de nuit.</strong> C’est le réglage le plus rentable : il efface les petites fuites de mémoire qui font ramer l’appareil au bout de quelques jours.</li>
</ul>

<h2>Ce que le mode kiosque ne protège pas</h2>
<p>Il ne protège pas du vol de l’appareil, qui relève de la fixation mécanique. Il ne protège pas du réseau : une borne verrouillée reste sur votre Wi-Fi, et doit être sur un réseau séparé de votre caisse si vous tenez à cloisonner.</p>
<p>Il ne protège pas non plus de vous-même : notez le code de déverrouillage ailleurs que sur l’appareil. Nous avons passé une soirée à réinitialiser une tablette pour avoir oublié ce détail.</p>
""",
 "faq": [
  ("Comment verrouiller une tablette Android sur une seule application ?",
   "Par l’épinglage d’écran, dans Réglages puis Sécurité. Vous ouvrez votre application et vous l’épinglez : en sortir exige une combinaison de touches et le code de déverrouillage. C’est gratuit et suffisant quand du personnel est toujours présent."),
  ("Faut-il payer un abonnement pour le mode kiosque ?",
   "Non dans la plupart des cas. L’épinglage natif ne coûte rien et plusieurs applications de kiosque sont gratuites en version de base. Les outils de supervision payants ne se justifient qu’à partir de plusieurs dizaines d’appareils à gérer à distance."),
  ("La borne redémarre-t-elle seule après une coupure de courant ?",
   "Avec une application de kiosque configurée pour se lancer au démarrage, oui. L’épinglage natif seul ne le garantit pas toujours. Testez-le en débranchant l’appareil avant d’ouvrir, c’est le genre de détail qu’on découvre un samedi soir."),
  ("Peut-on empêcher les mises à jour pendant le service ?",
   "Oui, en désactivant les mises à jour automatiques du système et des applications dans les réglages. Une mise à jour déclenchée en plein coup de feu immobilise la borne plusieurs minutes, et c’est entièrement évitable."),
 ],
 "offre": """
<p>Notre écran arrive sous Android ouvert, donc les trois niveaux décrits ici sont à votre disposition. Rien n’est verrouillé par nous, et rien ne vous oblige à passer par un outil payant.</p>
<p>À <strong>600 € HT sans abonnement</strong>, vous achetez un appareil dont vous êtes réellement propriétaire, verrouillage compris.</p>
""",
 "voisins": ["logiciel-borne-de-commande-ia", "tablette-de-commande-restaurant-fonctionnement", "borne-de-commande-sans-abonnement"],
},

# =========================================================================
{
 "slug": "borne-de-commande-occasion",
 "accroche": "Le matériel se revend mal pour une raison précise : il est souvent inséparable du logiciel qui l’animait. Les six vérifications.",
 "cle": "borne de commande occasion",
 "titre": "Acheter une borne de commande d’occasion : les pièges",
 "h1": "Borne de commande d’occasion : six vérifications avant de payer",
 "description": "Le marché de l’occasion est plein de bornes qui ne fonctionneront jamais chez vous. Les six points à vérifier avant d’acheter, et le calcul qui tranche.",
 "date": "2026-11-05", "maj": "2026-11-05", "lecture": 6,
 "resume": "On trouve des bornes à 300 € en petites annonces. La plupart sont invendables pour une raison que le vendeur ignore parfois lui-même : elles ne fonctionnent qu’avec le logiciel qui les animait.",
 "corps": """
<p>Des bornes de seconde main circulent, souvent issues de fermetures d’établissements ou de fins de contrat. Les prix affichés sont tentants, entre 200 et 800 €. Le taux d’échec, lui, est élevé.</p>

<h2>Pourquoi tant de bornes d’occasion ne servent à rien</h2>
<p>La plupart ont été vendues dans un ensemble fermé : matériel plus logiciel plus abonnement. Le jour où l’abonnement s’arrête, l’application cesse de fonctionner et l’écran devient inerte.</p>
<p>Le vendeur, de bonne foi, vous dit qu’elle marchait très bien le mois dernier. C’est vrai. Elle marchait tant que quelqu’un payait.</p>
<p>Première question à poser, avant même le prix : sur quel système tourne-t-elle, et peut-on y installer une autre application. Si la réponse est floue, passez.</p>

<h2>Les six vérifications</h2>

<h3>1. Le système est-il ouvert</h3>
<p>Un Android standard sur lequel on peut installer ce qu’on veut, oui. Un système propriétaire verrouillé par l’éditeur, non. Demandez une photo de l’écran des réglages.</p>

<h3>2. L’appareil est-il encore enrôlé</h3>
<p>Un appareil enrôlé dans un outil de supervision reste sous le contrôle de son ancien propriétaire, et une réinitialisation ne suffit pas toujours à l’en sortir. Exigez qu’il soit désenrôlé avant la vente, et vérifiez-le à la réception.</p>

<h3>3. L’état du tactile</h3>
<p>C’est la pièce qui s’use. Faites glisser un doigt lentement sur toute la surface, y compris les bords et les coins, et cherchez les zones mortes. Une dalle tactile à remplacer coûte souvent plus cher que la borne.</p>

<h3>4. Les heures d’allumage</h3>
<p>Une borne de chaîne a tourné douze heures par jour pendant trois ans. Le rétroéclairage faiblit, et un écran terni devient illisible en salle lumineuse. Comparez sa luminosité à celle d’un écran neuf avant de conclure.</p>

<h3>5. L’alimentation et les câbles</h3>
<p>Les blocs d’alimentation spécifiques sont introuvables une fois le modèle sorti du catalogue. S’il manque le bloc d’origine, considérez que la borne est hors service.</p>

<h3>6. La garantie, qui n’existe plus</h3>
<p>Entre professionnels, un achat d’occasion de particulier à particulier ou de pro à pro ne vous laisse en pratique que la garantie des vices cachés, difficile à mobiliser. Vous achetez le risque avec l’appareil.</p>

<h2>Le calcul qui tranche</h2>
<p>Une borne d’occasion à 450 €, avec un tactile incertain, sans garantie et sans bloc d’alimentation de rechange, se compare à un matériel neuf à 600 € garanti deux ans.</p>
<p>L’écart est de 150 €. Il faut vraiment que l’occasion soit exceptionnelle pour que ce calcul penche de son côté, et c’est la raison pour laquelle ce marché reste étroit.</p>
<p>Le seul cas où elle se défend : un modèle récent, sous Android ouvert, vendu avec son bloc et testé devant vous. Si les trois conditions sont réunies, foncez.</p>
""",
 "faq": [
  ("Peut-on réutiliser une borne de commande d’un autre fournisseur ?",
   "Seulement si son système est ouvert et qu’elle n’est plus enrôlée dans un outil de supervision. Beaucoup de bornes vendues en ensemble fermé cessent de fonctionner à l’arrêt de l’abonnement et ne peuvent pas recevoir une autre application."),
  ("Comment tester une borne d’occasion avant d’acheter ?",
   "Faites glisser un doigt lentement sur toute la dalle, bords et coins compris, pour repérer les zones mortes. Vérifiez la luminosité en pleine lumière, l’accès aux réglages du système, et la présence du bloc d’alimentation d’origine."),
  ("Une borne d’occasion est-elle garantie ?",
   "En pratique non. Entre professionnels, il vous reste la garantie des vices cachés, difficile à mobiliser et limitée dans le temps. Le risque de panne est intégralement pour vous à partir du jour de la livraison."),
  ("À partir de quel prix une borne d’occasion vaut-elle le coup ?",
   "Comparez au prix d’un matériel neuf garanti. Si l’écart se compte en dizaines d’euros, l’occasion ne compense pas l’absence de garantie et l’incertitude sur l’usure du tactile. Elle se défend en dessous de la moitié du prix du neuf, et à conditions réunies."),
 ],
 "offre": """
<p>Nous ne vendons pas d’occasion, et cette page vous conduira peut-être à en acheter une ailleurs. C’est assumé : une borne d’occasion saine est une bonne affaire.</p>
<p>Simplement, vérifiez les six points ci-dessus avant de payer. Si l’écart avec du neuf se réduit à quelques dizaines d’euros, notre matériel est à <strong>600 € HT, garanti deux ans, sans abonnement</strong>.</p>
""",
 "voisins": ["borne-tactile-commande-prix", "mode-kiosque-android-restaurant", "tablette-tactile-pour-restaurant"],
},

# =========================================================================
{
 "slug": "ecran-cuisine-restaurant",
 "accroche": "Plus de rouleau, plus de ticket illisible près de la friteuse. Ce qu’un écran de cuisine change, et pourquoi garder l’imprimante.",
 "cle": "écran de cuisine restaurant",
 "titre": "Écran de cuisine en restaurant : remplacer les tickets papier",
 "h1": "Écran de cuisine : ce qui change quand les commandes arrêtent de s’imprimer",
 "description": "Ce qu’un écran de cuisine apporte par rapport aux tickets papier, ce qu’il coûte réellement, et la raison de garder une imprimante en secours.",
 "date": "2026-11-05", "maj": "2026-11-05", "lecture": 6,
 "resume": "L’imprimante de cuisine tombe en panne au pire moment, le papier devient illisible près des sources de chaleur, et personne ne sait quelle commande est en cours. Un écran règle les trois, et en crée un nouveau.",
 "corps": """
<p>Le ticket papier en cuisine est une habitude, pas une nécessité. Il a trois défauts que tout le monde connaît et que personne ne compte vraiment.</p>

<h2>Les trois défauts du papier</h2>
<p><strong>Le rouleau se termine toujours à 12 h 30.</strong> Jamais à 15 h. Et il faut quelqu’un pour le changer pendant que les commandes s’accumulent.</p>
<p><strong>Le papier thermique vieillit mal près de la chaleur.</strong> Un ticket posé près d’une friteuse brunit en deux heures et devient illisible. On refait alors le plat de mémoire, ou on redemande.</p>
<p><strong>Personne ne sait où en est une commande.</strong> Un ticket est soit sur la barre, soit fait. Il n’existe pas d’état intermédiaire, donc aucune visibilité sur ce qui attend depuis huit minutes.</p>

<h2>Ce qu’un écran apporte</h2>
<p>Les commandes arrivent, s’affichent, et changent de couleur en vieillissant. Un coup d’œil suffit pour voir laquelle attend depuis trop longtemps, ce qui est exactement l’information qui manque sur une barre à tickets.</p>
<p>On marque un plat comme prêt d’un appui, la commande disparaît, et le client est appelé. En fin de service, vous savez combien de temps chaque plat a réellement pris : c’est la donnée qui permet de retravailler une carte, et elle n’existe pas sur papier.</p>
<p>Et plus de consommable. Sur trois ans, les rouleaux représentent une somme modeste mais réelle, et surtout du temps de manipulation en plein rush.</p>

<h2>Ce que ça coûte vraiment</h2>
<p>Un écran de cuisine est un écran tactile résistant, protégé de la vapeur et des projections, plus une application qui reçoit les commandes. Les deux postes sont souvent vendus séparément.</p>
<p>Le matériel ressemble beaucoup à celui d’une borne de commande : même type de dalle, même carte Android. La différence tient à l’emplacement et à la fixation, rarement à l’électronique.</p>
<p>Beaucoup d’applications de caisse incluent déjà un écran de cuisine dans leur offre. Avant d’acheter quoi que ce soit, posez la question à votre éditeur : la fonction est peut-être déjà payée.</p>

<h2>Le nouveau problème qu’il crée</h2>
<p>Un écran éteint arrête la cuisine, là où une imprimante en panne laisse au moins la possibilité de crier les commandes. C’est le seul vrai argument contre, et il est sérieux.</p>
<p>La parade tient en une phrase : gardez une imprimante branchée en secours, même si vous ne vous en servez jamais. Un rouleau tous les six mois est une assurance bon marché.</p>

<h2>Où le placer</h2>
<p>Hors de la zone de projection directe, à hauteur de regard depuis le poste de travail, et jamais face à une sortie de hotte. La vapeur chaude condense sur une dalle froide et finit par s’infiltrer.</p>
<p>Prévoyez aussi que quelqu’un le touchera avec des mains grasses toute la journée : la même exigence de tactile capacitif correct s’applique qu’en salle.</p>
""",
 "faq": [
  ("Un écran de cuisine remplace-t-il l’imprimante à tickets ?",
   "Fonctionnellement oui, mais gardez une imprimante branchée en secours. Un écran éteint arrête la production, là où une panne d’imprimante laisse la possibilité d’annoncer les commandes à la voix le temps de la réparation."),
  ("Quelle différence entre un écran de cuisine et une borne de commande ?",
   "L’électronique est très proche : même type de dalle tactile, même carte Android. Ce qui change est l’emplacement, la fixation et la protection contre la vapeur, ainsi que l’application qui tourne dessus."),
  ("Faut-il un écran résistant à l’eau en cuisine ?",
   "Au minimum protégé des projections et placé hors de la zone de vapeur directe. Une dalle froide face à une sortie de hotte accumule la condensation et finit par laisser passer l’humidité dans la connectique."),
  ("L’écran de cuisine est-il inclus dans les logiciels de caisse ?",
   "Souvent, dans les offres de restauration. Avant d’acheter une solution séparée, posez la question à votre éditeur : la fonction est peut-être déjà comprise dans ce que vous payez chaque mois."),
 ],
 "offre": """
<p>Notre écran pivote en paysage, ce qui en fait un affichage de cuisine utilisable, à condition de le placer à l’abri de la vapeur.</p>
<p>Même matériel, même prix : <strong>600 € HT sans abonnement</strong>. Certains clients en prennent deux, un en salle et un en cuisine, et profitent du tarif dégressif à partir du deuxième.</p>
""",
 "voisins": ["tablette-de-commande-restaurant-fonctionnement", "installer-borne-de-commande-restaurant", "tablette-tactile-pour-restaurant"],
},

]
