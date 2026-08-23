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
  telephone: "+33296000000",
  telAffiche:"02 96 00 00 00",
  email:     "contact@bornea.fr",
  ville:     "Saint-Brieuc",

  /* ---- Tarifs, en euros hors taxes ----------------------------------- */
  tva: 0.20,
  paliers: [                                   /* à partir de N unités, prix unitaire HT */
    { aPartirDe: 1, prixHT: 499 },
    { aPartirDe: 2, prixHT: 469 },
    { aPartirDe: 3, prixHT: 449 }
  ],
  options: {
    miseEnService: { libelle: "Mise en service à distance",  prixHT: 149, parUnite: false },
    garantie:      { libelle: "Extension de garantie 3 ans", prixHT: 79,  parUnite: true  }
  },
  livraisonHT: 0,                              /* 0 = offerte en France métropolitaine */

  /* ---- Paiement ------------------------------------------------------
     Deux modes possibles, au choix.

     "lien"  : Stripe Payment Links. Aucun serveur, aucune clé. Vous créez
               trois liens dans le tableau de bord Stripe (un par palier de
               quantité) et vous collez les URL ci-dessous. Les options sont
               ajoutées par le client sur la page Stripe, en articles
               facultatifs. C'est le mode par défaut, il marche partout.

     "php"   : le fichier paiement/creer-session.php crée une session Stripe
               Checkout avec le total exact calculé par le configurateur.
               Demande un hébergement qui exécute PHP (o2switch le fait) et
               une clé secrète placée dans paiement/config.php, jamais ici.
     ------------------------------------------------------------------- */
  modePaiement: "lien",

  liensStripe: {
    "1": "https://buy.stripe.com/REMPLACER_LIEN_1_BORNE",
    "2": "https://buy.stripe.com/REMPLACER_LIEN_2_BORNES",
    "3": "https://buy.stripe.com/REMPLACER_LIEN_3_BORNES_ET_PLUS"
  },

  cheminPhp: "paiement/creer-session.php",

  /* ---- Délais annoncés ----------------------------------------------- */
  delaiExpedition: "4 à 7 jours ouvrés",
  garantieMois: 24
};
