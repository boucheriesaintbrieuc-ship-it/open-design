<?php
/**
 * Dit si un nom de domaine est déjà enregistré.
 *
 * La réponse vient du registre lui-même, via le protocole RDAP qui a remplacé
 * whois. Ce n'est pas une estimation : un domaine absent du registre renvoie
 * 404, un domaine enregistré renvoie sa fiche. C'est la source qui fait foi.
 *
 * La requête part du serveur, jamais du navigateur du visiteur : son adresse
 * IP ne sort donc pas du site.
 *
 * Réponse : {"domaine":"x.fr","statut":"libre|pris|inconnu"}
 */

declare(strict_types=1);

header('Content-Type: application/json; charset=utf-8');
header('X-Content-Type-Options: nosniff');
header('Cache-Control: public, max-age=600');

function repondre(string $domaine, string $statut, ?string $detail = null): never {
    echo json_encode(
        array_filter(['domaine' => $domaine, 'statut' => $statut, 'detail' => $detail]),
        JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES
    );
    exit;
}

$d = strtolower(trim((string) ($_GET['d'] ?? '')));

// Forme attendue : un libellé, un point, une extension.
if (!preg_match('/^[a-z0-9][a-z0-9-]{0,61}\.[a-z]{2,24}$/', $d)) {
    http_response_code(400);
    repondre($d, 'inconnu', 'format invalide');
}

// rdap.org redirige vers le registre compétent pour l'extension demandée.
$curl = curl_init('https://rdap.org/domain/' . rawurlencode($d));
curl_setopt_array($curl, [
    CURLOPT_FOLLOWLOCATION => true,
    CURLOPT_MAXREDIRS      => 4,
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_NOBODY         => true,
    CURLOPT_TIMEOUT        => 8,
    CURLOPT_CONNECTTIMEOUT => 4,
    CURLOPT_HTTPHEADER     => ['Accept: application/rdap+json'],
    CURLOPT_USERAGENT      => 'verification-domaine/1.0',
]);
curl_exec($curl);
$statut = (int) curl_getinfo($curl, CURLINFO_RESPONSE_CODE);
$erreur = curl_error($curl);
curl_close($curl);

if ($erreur !== '') {
    error_log('RDAP injoignable pour ' . $d . ' : ' . $erreur);
    repondre($d, 'inconnu', 'registre injoignable');
}

// 200 : le registre connaît ce domaine. 404 : il ne le connaît pas.
// Tout le reste (429, 5xx, extension sans service RDAP) reste indéterminé.
repondre($d, match (true) {
    $statut === 200 => 'pris',
    $statut === 404 => 'libre',
    default         => 'inconnu',
});
