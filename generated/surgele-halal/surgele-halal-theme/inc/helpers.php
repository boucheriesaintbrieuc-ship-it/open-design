<?php
/**
 * Réglages par défaut et petites fonctions utilitaires.
 *
 * @package SurgeleHalal
 */

defined( 'ABSPATH' ) || exit;

/**
 * Valeurs par défaut de tous les réglages du Customizer.
 *
 * @return array<string, mixed>
 */
function sh_defaults() {
	return array(
		// Couleurs.
		'color_night'      => '#140A26',
		'color_orange'     => '#FF6B1A',
		'color_pink'       => '#FF2E88',
		'color_yellow'     => '#FFC93C',
		'color_cream'      => '#FFF4E6',

		// Bandeau défilant.
		'ticker_text'      => '100 % HALAL CERTIFIÉ · CHAÎNE DU FROID RESPECTÉE · CLICK & COLLECT À SAINT-BRIEUC · PAIEMENT EN CAISSE',

		// Hero.
		'hero_badge'       => 'Nouvelle mission — remplis ton congélo',
		'hero_title'       => 'La street food halal qui',
		'hero_highlight'   => 'croustille.',
		'hero_text'        => 'Tenders, wings, dorade, cordons bleus : tout le surgelé halal de Saint-Brieuc, en Click & Collect.',
		'hero_cta_label'   => 'Lancer la mission',
		'hero_cta2_label'  => 'Voir tout le catalogue',
		'hero_cta2_url'    => '',
		'hero_image'       => 0,

		// Zones (catégories mises en avant).
		'zone1_slug'       => 'poissons',
		'zone1_kicker'     => 'Zone 01 · Le port',
		'zone1_text'       => 'Tilapia, dorade, maquereau, chinchard',
		'zone2_slug'       => 'poulet',
		'zone2_kicker'     => 'Zone 02 · La ferme',
		'zone2_text'       => 'Cuisses, wings, pilons, poule fumée',
		'zone3_slug'       => 'crousty',
		'zone3_kicker'     => 'Zone 03 · Downtown',
		'zone3_text'       => 'Tenders, nuggets, cordons bleus, kebab',

		// Best-sellers.
		'best_title'       => 'Best-sellers',
		'best_count'       => 8,

		// Bandeau garanties + réassurance.
		'trust_title_1'    => '100 % halal',
		'trust_title_2'    => 'Chaîne du froid respectée',
		'trust_text'       => 'Produits certifiés halal, conservés à −18 °C du fournisseur jusqu’à votre retrait.',
		'reas_1_title'     => 'Click & Collect',
		'reas_1_text'      => 'Commandez en ligne, récupérez sur place à Saint-Brieuc.',
		'reas_2_title'     => 'Paiement en caisse',
		'reas_2_text'      => 'Vous réglez au moment du retrait.',
		'reas_3_title'     => 'Froid garanti',
		'reas_3_text'      => 'Pensez à votre sac isotherme pour le trajet retour.',

		// Badges produits.
		'badge_halal'      => true,
		'badge_frozen'     => true,
		'badge_weight'     => true,

		// Pied de page.
		'footer_about'     => 'Surgelés halal à Saint-Brieuc depuis 2015.',
		'legal_page'       => 0,
		'brand_cats'       => 'almondy,avs,chef-zaki,isla-delice',

		// Performance.
		'light_mode'       => true,
	);
}

/**
 * Lit un réglage du thème avec sa valeur par défaut.
 *
 * @param string $key Clé du réglage.
 * @return mixed
 */
function sh_mod( $key ) {
	$defaults = sh_defaults();
	$default  = isset( $defaults[ $key ] ) ? $defaults[ $key ] : '';
	return get_theme_mod( 'sh_' . $key, $default );
}

/**
 * Les trois zones (catégories) mises en avant, résolues en termes WooCommerce.
 * Si une catégorie n'existe pas encore, la tuile pointe vers la boutique.
 *
 * @return array<int, array<string, mixed>>
 */
function sh_zones() {
	$labels = array(
		1 => 'Poissons',
		2 => 'Poulet',
		3 => 'Crousty',
	);
	$zones  = array();

	foreach ( $labels as $i => $fallback_label ) {
		$slug = sanitize_title( sh_mod( "zone{$i}_slug" ) );
		$term = ( $slug && taxonomy_exists( 'product_cat' ) ) ? get_term_by( 'slug', $slug, 'product_cat' ) : false;
		$url  = $term ? get_term_link( $term ) : '';

		if ( ! $url || is_wp_error( $url ) ) {
			$url = function_exists( 'wc_get_page_permalink' ) ? wc_get_page_permalink( 'shop' ) : home_url( '/' );
		}

		$zones[] = array(
			'index'  => $i,
			'slug'   => $slug,
			'term'   => $term,
			'label'  => $term ? $term->name : $fallback_label,
			'count'  => $term ? (int) $term->count : null,
			'url'    => $url,
			'kicker' => sh_mod( "zone{$i}_kicker" ),
			'text'   => sh_mod( "zone{$i}_text" ),
		);
	}

	return $zones;
}

/**
 * Icônes SVG inline (trait), sans dépendance.
 *
 * @param string $name Nom de l'icône.
 * @return string
 */
function sh_icon( $name ) {
	$paths = array(
		'search' => '<circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/>',
		'cart'   => '<path d="M3 4h2l2.4 11h11l2-8H6.2"/><circle cx="9" cy="20" r="1.5"/><circle cx="18" cy="20" r="1.5"/>',
		'menu'   => '<path d="M4 7h16M4 12h16M4 17h16"/>',
		'close'  => '<path d="M6 6l12 12M18 6L6 18"/>',
		'store'  => '<path d="M4 10v10h16V10M3 4h18l-1 6H4zM9 20v-6h6v6"/>',
		'card'   => '<rect x="3" y="6" width="18" height="12" rx="2"/><path d="M3 10h18"/>',
		'snow'   => '<path d="M12 2v20M4 6l16 12M20 6L4 18"/>',
		'arrow'  => '<path d="M5 12h14M13 6l6 6-6 6"/>',
		'check'  => '<path d="M5 12l5 5L20 7"/>',
	);
	if ( ! isset( $paths[ $name ] ) ) {
		return '';
	}
	return '<svg class="sh-icon" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">' . $paths[ $name ] . '</svg>';
}
