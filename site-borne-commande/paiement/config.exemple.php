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
    'domaine' => 'https://www.bornea.fr',

    // Identifiant d'un taux de TVA créé dans Stripe (Produits > Taux de taxe),
    // par exemple 'txr_1234'. Laissez la chaîne vide pour facturer en TTC
    // sans ligne de TVA distincte.
    'taux_tva_stripe' => '',

    // Taux appliqué côté serveur quand taux_tva_stripe est vide.
    'tva' => 0.20,
];
