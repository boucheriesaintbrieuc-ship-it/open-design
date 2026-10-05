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
		'color_night'      => '#07070B',
		'color_orange'     => '#FF7A1A',
		'color_pink'       => '#FF2D3A',
		'color_yellow'     => '#FFB238',
		'color_cream'      => '#F5F5F7',

		// Bandeau d'annonce.
		'ticker_text'      => '100 % halal certifié · Chaîne du froid −18 °C · Click & Collect à Saint-Brieuc · Paiement en caisse',

		// Hero « showroom 3D ».
		'hero_badge'       => 'Nouveau · Collection crousty',
		'hero_title'       => 'Le surgelé halal,',
		'hero_highlight'   => 'version premium.',
		'hero_text'        => 'Tenders, nuggets, cordons bleus, kebab, wings, poissons : sélectionne un produit et remplis ton congélo en Click & Collect.',
		'hero_cta_label'   => 'Voir les produits',
		'hero_cta2_label'  => 'Tout le catalogue',
		'hero_cta2_url'    => '',
		'hero_image'       => 0,

		// Zones (catégories mises en avant).
		'zone1_slug'       => 'poissons',
		'zone1_kicker'     => '01 · Poissons',
		'zone1_text'       => 'Tilapia, dorade, maquereau, chinchard',
		'zone2_slug'       => 'poulet',
		'zone2_kicker'     => '02 · Poulet',
		'zone2_text'       => 'Cuisses, wings, pilons, poule fumée',
		'zone3_slug'       => 'crousty',
		'zone3_kicker'     => '03 · Crousty',
		'zone3_text'       => 'Tenders, nuggets, cordons bleus, kebab',

		// Best-sellers.
		'best_title'       => 'Les plus commandés',
		'best_count'       => 8,

		// Bandeau garanties + réassurance.
		'trust_title_1'    => '100 % halal',
		'trust_title_2'    => 'Froid garanti −18 °C',
		'trust_text'       => 'Produits certifiés halal, conservés à −18 °C du fournisseur jusqu’à votre retrait.',
		'reas_1_title'     => 'Click & Collect',
		'reas_1_text'      => 'Commandez en ligne, récupérez sur place à Saint-Brieuc.',
		'reas_2_title'     => 'Paiement en caisse',
		'reas_2_text'      => 'Vous réglez au moment du retrait.',
		'reas_3_title'     => 'Chaîne du froid',
		'reas_3_text'      => 'Pensez à votre sac isotherme pour le trajet retour.',

		// Badges produits.
		'badge_halal'      => true,
		'badge_frozen'     => true,
		'badge_weight'     => true,

		// Pied de page.
		'footer_about'     => 'O’Surgelé — surgelés halal à Saint-Brieuc depuis 2015.',
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
	$renders = array(
		1 => 'dorade',
		2 => 'wings',
		3 => 'tenders',
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
			'render' => sh_render_url( $renders[ $i ] ),
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
		'prev'   => '<path d="M15 6l-6 6 6 6"/>',
		'next'   => '<path d="M9 6l6 6-6 6"/>',
		'check'  => '<path d="M5 12l5 5L20 7"/>',
	);
	if ( ! isset( $paths[ $name ] ) ) {
		return '';
	}
	return '<svg class="sh-icon" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">' . $paths[ $name ] . '</svg>';
}

/**
 * URL d'un rendu 3D livré avec le thème (assets/img/3d/<nom>.webp).
 *
 * @param string $name Nom du rendu.
 * @return string
 */
function sh_render_url( $name ) {
	return SH_URI . '/assets/img/3d/' . sanitize_file_name( $name ) . '.webp';
}

/**
 * Produits vedettes du showroom 3D de l'accueil. Chaque entrée renvoie vers
 * une recherche produits (aucune donnée en base n'est requise).
 * Filtre : sh_showroom_items.
 *
 * @return array<int, array{name:string, tag:string, render:string, url:string}>
 */
function sh_showroom_items() {
	$items = array(
		array( 'name' => 'Tenders', 'tag' => 'Crousty', 'render' => 'tenders', 'q' => 'tenders' ),
		array( 'name' => 'Nuggets', 'tag' => 'Crousty', 'render' => 'nuggets', 'q' => 'nuggets' ),
		array( 'name' => 'Cordon bleu', 'tag' => 'Crousty', 'render' => 'cordon-bleu', 'q' => 'cordon bleu' ),
		array( 'name' => 'Kebab', 'tag' => 'Crousty', 'render' => 'kebab', 'q' => 'kebab' ),
		array( 'name' => 'Wings', 'tag' => 'Poulet', 'render' => 'wings', 'q' => 'wings' ),
		array( 'name' => 'Cuisses', 'tag' => 'Poulet', 'render' => 'cuisses', 'q' => 'poulet' ),
		array( 'name' => 'Dorade', 'tag' => 'Poissons', 'render' => 'dorade', 'q' => 'dorade' ),
	);
	$out = array();
	foreach ( $items as $item ) {
		$args = array( 's' => $item['q'] );
		if ( class_exists( 'WooCommerce' ) ) {
			$args['post_type'] = 'product';
		}
		$out[] = array(
			'name'   => $item['name'],
			'tag'    => $item['tag'],
			'render' => sh_render_url( $item['render'] ),
			'url'    => add_query_arg( $args, home_url( '/' ) ),
		);
	}
	return apply_filters( 'sh_showroom_items', $out );
}
