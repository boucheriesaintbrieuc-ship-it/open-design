<?php
/**
 * Copiez ce fichier en config.php et remplissez-le.
 * config.php ne doit jamais être versionné ni envoyé par e-mail :
 * la clé secrète Stripe vaut votre compte marchand.
 */
return [
    // Clé secrète Stripe. Commence par sk_test_ pour les essais,
    // sk_live_ une fois en production. Tableau de bord Stripe > Développeurs > Clés API.
    'cle_secrete' => 'sk_test_REMPLACER',

    // Adresse publique du site, sans barre oblique finale.
    'domaine' => 'https://borne-restaurants.fr',

    // true  : la carte est seulement AUTORISÉE à la commande. La banque bloque
    //         le montant, et c'est vous qui déclenchez le débit depuis le
    //         tableau de bord Stripe, quand vous décidez d'honorer la commande.
    //
    //         Attention : une autorisation non capturée est annulée par Stripe
    //         au bout de SEPT JOURS, et l'argent retourne chez le client.
    //         Capturez dans la semaine. Si vos colis mettent trois semaines à
    //         arriver, capturez à la confirmation de commande et pas à
    //         l'expédition, sinon vous perdrez le paiement.
    //
    //         Dans ce mode, seules les cartes sont proposées : Link, le
    //         prélèvement SEPA et le paiement en plusieurs fois ne gèrent pas
    //         la capture différée.
    //
    // false : le montant est débité immédiatement, comme dans une boutique
    //         classique.
    'capture_manuelle' => true,

    // Identifiant d'un taux de TVA créé dans Stripe (Produits > Taux de taxe),
    // par exemple 'txr_1234'. Laissez la chaîne vide pour facturer en TTC
    // sans ligne de TVA distincte.
    'taux_tva_stripe' => '',

    // Taux appliqué côté serveur quand taux_tva_stripe est vide.
    'tva' => 0.20,

    // Ne renseignez pas cette clé en production : elle sert à diriger les
    // appels vers un serveur d'essai local pour vérifier ce qui part chez
    // Stripe. Absente, le vrai https://api.stripe.com est utilisé.
    // 'api_base' => 'http://127.0.0.1:9911',
];
