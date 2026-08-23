<?php
/**
 * Crée une session Stripe Checkout et renvoie son URL.
 *
 * Le total est recalculé ici, à partir de la seule quantité et des options
 * envoyées par le navigateur. Les prix ne viennent jamais du client : sans
 * cela, n'importe qui pourrait acheter la borne à un centime en modifiant
 * la requête.
 *
 * Réponse : {"url": "https://checkout.stripe.com/..."} ou {"erreur": "..."}.
 */

declare(strict_types=1);

header('Content-Type: application/json; charset=utf-8');
header('X-Content-Type-Options: nosniff');

function repondre(int $code, array $donnees): never {
    http_response_code($code);
    echo json_encode($donnees, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES);
    exit;
}

if (($_SERVER['REQUEST_METHOD'] ?? '') !== 'POST') {
    repondre(405, ['erreur' => 'méthode non autorisée']);
}

$fichierConfig = __DIR__ . '/config.php';
if (!is_file($fichierConfig)) {
    repondre(500, ['erreur' => 'configuration absente : copiez config.exemple.php en config.php']);
}
$config = require $fichierConfig;
if (empty($config['cle_secrete']) || str_contains((string) $config['cle_secrete'], 'REMPLACER')) {
    repondre(500, ['erreur' => 'clé Stripe non renseignée']);
}

/* ---- Tarifs, en centimes hors taxes. Source de vérité unique. ---------- */
const PALIERS = [3 => 44900, 2 => 46900, 1 => 49900];   // à partir de N unités
const PRIX_MISE_EN_SERVICE = 14900;                      // forfait, une fois
const PRIX_GARANTIE        =  7900;                      // par borne

$brut = file_get_contents('php://input');
$entree = json_decode($brut ?: '[]', true);
if (!is_array($entree)) {
    repondre(400, ['erreur' => 'corps de requête illisible']);
}

$quantite = (int) ($entree['quantite'] ?? 0);
if ($quantite < 1 || $quantite > 20) {
    repondre(400, ['erreur' => 'quantité hors limites']);
}
$miseEnService = !empty($entree['miseEnService']);
$garantie      = !empty($entree['garantie']);
$email         = filter_var((string) ($entree['email'] ?? ''), FILTER_VALIDATE_EMAIL) ?: null;
$reference     = mb_substr(trim((string) ($entree['reference'] ?? '')), 0, 190);

$prixUnitaireHT = PALIERS[1];
foreach (PALIERS as $seuil => $prix) {
    if ($quantite >= $seuil) { $prixUnitaireHT = $prix; break; }
}

$tauxTva = (string) ($config['taux_tva_stripe'] ?? '');
$coefficient = $tauxTva === '' ? (1 + (float) ($config['tva'] ?? 0.20)) : 1.0;
$suffixe = $tauxTva === '' ? ' (TTC)' : '';
$montant = static fn (int $ht): int => (int) round($ht * $coefficient);

$articles = [[
    'nom'      => 'Borne de commande tactile sur pied' . $suffixe,
    'detail'   => 'Écran vertical sur pied, livré monté, garantie 2 ans.',
    'unitaire' => $montant($prixUnitaireHT),
    'quantite' => $quantite,
]];
if ($miseEnService) {
    $articles[] = [
        'nom'      => 'Mise en service à distance' . $suffixe,
        'detail'   => 'Une heure en visio : installation de l’application et verrouillage en mode kiosque.',
        'unitaire' => $montant(PRIX_MISE_EN_SERVICE),
        'quantite' => 1,
    ];
}
if ($garantie) {
    $articles[] = [
        'nom'      => 'Extension de garantie à 3 ans' . $suffixe,
        'detail'   => 'Un an de garantie contractuelle supplémentaire, par borne.',
        'unitaire' => $montant(PRIX_GARANTIE),
        'quantite' => $quantite,
    ];
}

$domaine = rtrim((string) ($config['domaine'] ?? ''), '/');

$parametres = [
    'mode'        => 'payment',
    'locale'      => 'fr',
    'success_url' => $domaine . '/merci.html?session_id={CHECKOUT_SESSION_ID}',
    'cancel_url'  => $domaine . '/paiement-annule.html',
    'billing_address_collection' => 'required',
    'phone_number_collection' => ['enabled' => 'true'],
    'shipping_address_collection' => ['allowed_countries' => ['FR', 'BE', 'LU', 'CH', 'MC']],
    'custom_fields' => [[
        'key'      => 'siret',
        'label'    => ['type' => 'custom', 'custom' => 'Numéro SIRET (facultatif)'],
        'type'     => 'text',
        'optional' => 'true',
    ]],
    'line_items' => [],
];

foreach ($articles as $i => $a) {
    $ligne = [
        'quantity'   => $a['quantite'],
        'price_data' => [
            'currency'      => 'eur',
            'unit_amount'   => $a['unitaire'],
            'product_data'  => ['name' => $a['nom'], 'description' => $a['detail']],
        ],
    ];
    if ($tauxTva !== '') {
        $ligne['price_data']['tax_behavior'] = 'exclusive';
        $ligne['tax_rates'] = [$tauxTva];
    }
    $parametres['line_items'][$i] = $ligne;
}
if ($email !== null)   { $parametres['customer_email'] = $email; }
if ($reference !== '') { $parametres['client_reference_id'] = preg_replace('/[^\w\-]+/u', '-', $reference); }

$curl = curl_init('https://api.stripe.com/v1/checkout/sessions');
curl_setopt_array($curl, [
    CURLOPT_POST           => true,
    CURLOPT_POSTFIELDS     => http_build_query($parametres, '', '&', PHP_QUERY_RFC3986),
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_TIMEOUT        => 20,
    CURLOPT_HTTPHEADER     => [
        'Authorization: Bearer ' . $config['cle_secrete'],
        'Content-Type: application/x-www-form-urlencoded',
        'Stripe-Version: 2024-06-20',
    ],
]);
$reponse = curl_exec($curl);
$statut  = (int) curl_getinfo($curl, CURLINFO_RESPONSE_CODE);
$erreurCurl = curl_error($curl);
curl_close($curl);

if ($reponse === false) {
    error_log('Stripe injoignable : ' . $erreurCurl);
    repondre(502, ['erreur' => 'la banque est injoignable, réessayez dans un instant']);
}

$data = json_decode((string) $reponse, true);
if ($statut >= 400 || empty($data['url'])) {
    error_log('Stripe a refusé la session : ' . substr((string) $reponse, 0, 500));
    repondre(502, ['erreur' => $data['error']['message'] ?? 'le paiement n’a pas pu être ouvert']);
}

repondre(200, ['url' => $data['url']]);
