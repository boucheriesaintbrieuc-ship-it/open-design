/* =========================================================================
   LE SEUL FICHIER À MODIFIER POUR METTRE LE SITE EN PRODUCTION.
   Tout le reste du site lit ces valeurs. Ne mettez jamais de clé secrète
   Stripe ici : ce fichier est téléchargé par le navigateur du visiteur.
   Une clé secrète commence par sk_ ou rk_. Si vous en voyez une, retirez-la.
   ========================================================================= */

window.CONFIG = {

  /* ---- Identité ------------------------------------------------------ */
  marque:    "Bornéa",
  domaine:   "https://borne-restaurants.fr",         /* sans barre oblique finale */
  telephone: "+33756939700",
  telAffiche:"07 56 93 97 00",
  email:     "infos@borne-restaurants.fr",
  ville:     "Saint-Brieuc",

  /* ---- Tarifs, en euros hors taxes ----------------------------------- */
  tva: 0.20,
  paliers: [                                   /* à partir de N unités, prix unitaire HT */
    { aPartirDe: 1, prixHT: 600 },
    { aPartirDe: 2, prixHT: 570 },
    { aPartirDe: 3, prixHT: 540 }
  ],
  options: {
    miseEnService: { libelle: "Mise en service à distance",  prixHT: 149, parUnite: false },
    garantie:      { libelle: "Extension de garantie 3 ans", prixHT: 79,  parUnite: true  }
  },
  livraisonHT: 0,                              /* 0 = offerte en France métropolitaine */

  /* ---- Paiement ------------------------------------------------------
     Trois modes possibles. Le mode actif est celui de modePaiement.

     "woocommerce" : la commande part sur une boutique WooCommerce que vous
               possédez déjà, et c'est elle qui encaisse. Rien à créer chez
               Stripe, aucune clé à manipuler, aucun PHP à installer ici :
               la passerelle bancaire, le certificat, les e-mails de
               confirmation et les factures existent déjà là-bas et ont
               tourné sur des dizaines de milliers de commandes. Mode
               fonctionnel, gardé en secours.

               En contrepartie, le panier de la boutique ne connaît qu'un
               seul article à un seul prix. Les paliers dégressifs et les
               deux options sont donc retirés du formulaire dans ce mode,
               et traités par devis. C'est volontaire : il vaut mieux une
               ligne de panier exacte qu'une remise promise à l'écran et
               absente au moment de débiter.

     "lien"  : Stripe Payment Links. Aucun serveur, aucune clé. Vous créez
               trois liens dans le tableau de bord Stripe (un par palier de
               quantité) et vous collez les URL ci-dessous.

     "php"   : le fichier paiement/creer-session.php crée une session Stripe
               Checkout avec le total exact calculé par le configurateur.
               Demande un hébergement qui exécute PHP (o2switch le fait) et
               une clé secrète placée dans paiement/config.php, jamais ici.
               C'EST LE MODE ACTIF, et il est réglé en autorisation seule :
               la carte du client est bloquée, et c'est vous qui déclenchez
               le débit depuis le tableau de bord Stripe. Voyez
               capture_manuelle dans paiement/config.php.
     ------------------------------------------------------------------- */
  modePaiement: "php",

  /* ---- La boutique qui encaisse (mode "woocommerce") ------------------
     idProduit est l'identifiant WooCommerce de la fiche borne. Il ne change
     jamais, même si vous renommez le produit ou son adresse : c'est pour ça
     qu'on s'appuie dessus plutôt que sur l'URL de la fiche.

     nomAffiche et hote servent à prévenir le client de la redirection, sur
     la page de commande et dans les conditions de vente. Ne les retirez
     pas : un acheteur qui atterrit sans prévenir sur un autre nom de
     domaine au moment de sortir sa carte referme l'onglet.
     ------------------------------------------------------------------- */
  boutique: {
    base:         "https://epicerie-saintbrieuc.fr",
    pageCommande: "/commander/",
    idProduit:    7910,
    nomAffiche:   "Épicerie Saint-Brieuc",
    hote:         "epicerie-saintbrieuc.fr"
  },

  liensStripe: {
    "1": "https://buy.stripe.com/REMPLACER_LIEN_1_BORNE",
    "2": "https://buy.stripe.com/REMPLACER_LIEN_2_BORNES",
    "3": "https://buy.stripe.com/REMPLACER_LIEN_3_BORNES_ET_PLUS"
  },

  cheminPhp: "paiement/creer-session.php",

  /* true : le site annonce au client que sa carte est seulement autorisée et
     qu'elle sera débitée à la confirmation de commande. Doit rester aligné
     sur capture_manuelle dans paiement/config.php : si les deux divergent,
     vous promettez à l'écran l'inverse de ce que fait la banque. */
  captureManuelle: true,

  /* ---- Récitation du Coran sur la page de commande --------------------
     Déposez votre fichier dans audio/ et indiquez son nom ci-dessous.
     Format : MP3 ou M4A. Visez moins de 8 Mo, sinon la page met trop
     longtemps à se charger sur un téléphone en 4G.

     Le son ne peut pas démarrer tout seul : Chrome, Safari et Firefox
     l'interdisent tant que le visiteur n'a pas cliqué sur la page. La
     lecture démarre donc au premier clic, quel qu'il soit.

     Mettez fichier à "" pour retirer complètement le lecteur.
     ------------------------------------------------------------------- */
  audio: {
    fichier: "audio/coran.mp3",
    titre:   "Récitation du Coran",
    volume:  0.35,          /* entre 0 et 1 */
    demarrerSeul: true      /* false : le visiteur doit cliquer sur le bouton */
  },

  /* ---- Délais annoncés ----------------------------------------------- */
  delaiExpedition: "4 à 7 jours ouvrés",
  garantieMois: 24
};
