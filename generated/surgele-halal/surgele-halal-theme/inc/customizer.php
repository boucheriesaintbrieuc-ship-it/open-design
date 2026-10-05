<?php
/**
 * Customizer : logo (natif), couleurs, textes, zones, badges, pied de page.
 *
 * @package SurgeleHalal
 */

defined( 'ABSPATH' ) || exit;

/**
 * Déclare les sections et réglages.
 *
 * @param WP_Customize_Manager $wp_customize Gestionnaire.
 */
function sh_customize_register( $wp_customize ) {
	$d = sh_defaults();

	$wp_customize->add_panel(
		'sh_panel',
		array(
			'title'    => __( 'Surgelé Halal — Tasty Crousty', 'surgele-halal' ),
			'priority' => 30,
		)
	);

	$sections = array(
		'sh_colors' => __( 'Couleurs', 'surgele-halal' ),
		'sh_hero'   => __( 'Accueil — Hero & bandeau', 'surgele-halal' ),
		'sh_zones'  => __( 'Accueil — 3 zones (catégories)', 'surgele-halal' ),
		'sh_trust'  => __( 'Accueil — Best-sellers & réassurance', 'surgele-halal' ),
		'sh_shop'   => __( 'Boutique — badges & performance', 'surgele-halal' ),
		'sh_footer' => __( 'Pied de page & mentions légales', 'surgele-halal' ),
	);
	foreach ( $sections as $id => $title ) {
		$wp_customize->add_section( $id, array( 'title' => $title, 'panel' => 'sh_panel' ) );
	}

	// Couleurs.
	$colors = array(
		'color_night'  => __( 'Fond nuit', 'surgele-halal' ),
		'color_orange' => __( 'Orange sunset (boutons)', 'surgele-halal' ),
		'color_pink'   => __( 'Rose néon (accents)', 'surgele-halal' ),
		'color_yellow' => __( 'Jaune crousty (prix, liens)', 'surgele-halal' ),
		'color_cream'  => __( 'Crème (texte clair)', 'surgele-halal' ),
	);
	foreach ( $colors as $key => $label ) {
		$wp_customize->add_setting( 'sh_' . $key, array( 'default' => $d[ $key ], 'sanitize_callback' => 'sanitize_hex_color', 'transport' => 'refresh' ) );
		$wp_customize->add_control(
			new WP_Customize_Color_Control(
				$wp_customize,
				'sh_' . $key,
				array(
					'label'       => $label,
					'section'     => 'sh_colors',
					'description' => 'color_night' === $key ? __( 'Gardez un fond très sombre : le texte crème doit rester lisible (contraste AA 4,5:1).', 'surgele-halal' ) : '',
				)
			)
		);
	}

	// Textes.
	$texts = array(
		'ticker_text'     => array( 'sh_hero', __( 'Bandeau défilant (haut de page)', 'surgele-halal' ), 'text' ),
		'hero_badge'      => array( 'sh_hero', __( 'Badge « mission »', 'surgele-halal' ), 'text' ),
		'hero_title'      => array( 'sh_hero', __( 'Titre (début)', 'surgele-halal' ), 'text' ),
		'hero_highlight'  => array( 'sh_hero', __( 'Titre (mot en surbrillance)', 'surgele-halal' ), 'text' ),
		'hero_text'       => array( 'sh_hero', __( 'Sous-titre', 'surgele-halal' ), 'textarea' ),
		'hero_cta_label'  => array( 'sh_hero', __( 'Bouton principal (vers la zone Crousty)', 'surgele-halal' ), 'text' ),
		'hero_cta2_label' => array( 'sh_hero', __( 'Bouton secondaire', 'surgele-halal' ), 'text' ),
		'zone1_kicker'    => array( 'sh_zones', __( 'Zone 1 — sur-titre', 'surgele-halal' ), 'text' ),
		'zone1_text'      => array( 'sh_zones', __( 'Zone 1 — exemples', 'surgele-halal' ), 'text' ),
		'zone2_kicker'    => array( 'sh_zones', __( 'Zone 2 — sur-titre', 'surgele-halal' ), 'text' ),
		'zone2_text'      => array( 'sh_zones', __( 'Zone 2 — exemples', 'surgele-halal' ), 'text' ),
		'zone3_kicker'    => array( 'sh_zones', __( 'Zone 3 — sur-titre', 'surgele-halal' ), 'text' ),
		'zone3_text'      => array( 'sh_zones', __( 'Zone 3 — exemples', 'surgele-halal' ), 'text' ),
		'best_title'      => array( 'sh_trust', __( 'Titre best-sellers', 'surgele-halal' ), 'text' ),
		'trust_title_1'   => array( 'sh_trust', __( 'Bandeau garanties — titre 1', 'surgele-halal' ), 'text' ),
		'trust_title_2'   => array( 'sh_trust', __( 'Bandeau garanties — titre 2', 'surgele-halal' ), 'text' ),
		'trust_text'      => array( 'sh_trust', __( 'Bandeau garanties — texte', 'surgele-halal' ), 'textarea' ),
		'reas_1_title'    => array( 'sh_trust', __( 'Réassurance 1 — titre', 'surgele-halal' ), 'text' ),
		'reas_1_text'     => array( 'sh_trust', __( 'Réassurance 1 — texte', 'surgele-halal' ), 'text' ),
		'reas_2_title'    => array( 'sh_trust', __( 'Réassurance 2 — titre', 'surgele-halal' ), 'text' ),
		'reas_2_text'     => array( 'sh_trust', __( 'Réassurance 2 — texte', 'surgele-halal' ), 'text' ),
		'reas_3_title'    => array( 'sh_trust', __( 'Réassurance 3 — titre', 'surgele-halal' ), 'text' ),
		'reas_3_text'     => array( 'sh_trust', __( 'Réassurance 3 — texte', 'surgele-halal' ), 'text' ),
		'footer_about'    => array( 'sh_footer', __( 'Texte de présentation', 'surgele-halal' ), 'textarea' ),
		'brand_cats'      => array( 'sh_footer', __( 'Slugs des catégories « marques » (séparés par des virgules) — ajoutés comme « brand » dans les données structurées Product', 'surgele-halal' ), 'text' ),
	);
	foreach ( $texts as $key => $conf ) {
		$wp_customize->add_setting(
			'sh_' . $key,
			array(
				'default'           => $d[ $key ],
				'sanitize_callback' => 'textarea' === $conf[2] ? 'sanitize_textarea_field' : 'sanitize_text_field',
			)
		);
		$wp_customize->add_control( 'sh_' . $key, array( 'label' => $conf[1], 'section' => $conf[0], 'type' => $conf[2] ) );
	}

	$wp_customize->add_setting( 'sh_hero_cta2_url', array( 'default' => '', 'sanitize_callback' => 'esc_url_raw' ) );
	$wp_customize->add_control( 'sh_hero_cta2_url', array( 'label' => __( 'Lien du bouton secondaire (vide = boutique)', 'surgele-halal' ), 'section' => 'sh_hero', 'type' => 'url' ) );

	$wp_customize->add_setting( 'sh_hero_image', array( 'default' => 0, 'sanitize_callback' => 'absint' ) );
	$wp_customize->add_control(
		new WP_Customize_Media_Control(
			$wp_customize,
			'sh_hero_image',
			array(
				'label'       => __( 'Image du hero (optionnelle, détourée de préférence)', 'surgele-halal' ),
				'section'     => 'sh_hero',
				'mime_type'   => 'image',
				'description' => __( 'Sans image, le hero reste 100 % CSS (le plus rapide).', 'surgele-halal' ),
			)
		)
	);

	// Slugs des zones : liste déroulante des catégories produits existantes.
	$choices = array( '' => __( '— Aucune —', 'surgele-halal' ) );
	if ( taxonomy_exists( 'product_cat' ) ) {
		$terms = get_terms( array( 'taxonomy' => 'product_cat', 'hide_empty' => false ) );
		if ( ! is_wp_error( $terms ) ) {
			foreach ( $terms as $t ) {
				$choices[ $t->slug ] = $t->name;
			}
		}
	}
	for ( $i = 1; $i <= 3; $i++ ) {
		$key = "zone{$i}_slug";
		if ( $d[ $key ] && ! isset( $choices[ $d[ $key ] ] ) ) {
			/* translators: %s: slug de catégorie. */
			$choices[ $d[ $key ] ] = sprintf( __( '%s (à créer avec le script de rangement)', 'surgele-halal' ), $d[ $key ] );
		}
		$wp_customize->add_setting( 'sh_' . $key, array( 'default' => $d[ $key ], 'sanitize_callback' => 'sanitize_title' ) );
		$wp_customize->add_control(
			'sh_' . $key,
			array(
				/* translators: %d: numéro de zone. */
				'label'   => sprintf( __( 'Zone %d — catégorie WooCommerce', 'surgele-halal' ), $i ),
				'section' => 'sh_zones',
				'type'    => 'select',
				'choices' => $choices,
			)
		);
	}

	$wp_customize->add_setting( 'sh_best_count', array( 'default' => $d['best_count'], 'sanitize_callback' => 'absint' ) );
	$wp_customize->add_control( 'sh_best_count', array( 'label' => __( 'Nombre de best-sellers', 'surgele-halal' ), 'section' => 'sh_trust', 'type' => 'number', 'input_attrs' => array( 'min' => 2, 'max' => 16 ) ) );

	$bools = array(
		'badge_halal'  => array( 'sh_shop', __( 'Badge « Halal » sur chaque produit', 'surgele-halal' ) ),
		'badge_frozen' => array( 'sh_shop', __( 'Badge « Surgelé −18 °C » sur chaque produit', 'surgele-halal' ) ),
		'badge_weight' => array( 'sh_shop', __( 'Badge poids (poids WooCommerce, attribut « poids » ou titre)', 'surgele-halal' ) ),
		'light_mode'   => array( 'sh_shop', __( 'Mode léger : ajout au panier AJAX sans jQuery dans les listes (désactivez si un plugin dépend du panier jQuery de WooCommerce)', 'surgele-halal' ) ),
	);
	foreach ( $bools as $key => $conf ) {
		$wp_customize->add_setting( 'sh_' . $key, array( 'default' => $d[ $key ], 'sanitize_callback' => 'rest_sanitize_boolean' ) );
		$wp_customize->add_control( 'sh_' . $key, array( 'label' => $conf[1], 'section' => $conf[0], 'type' => 'checkbox' ) );
	}

	$wp_customize->add_setting( 'sh_legal_page', array( 'default' => 0, 'sanitize_callback' => 'absint' ) );
	$wp_customize->add_control( 'sh_legal_page', array( 'label' => __( 'Page « Mentions légales »', 'surgele-halal' ), 'section' => 'sh_footer', 'type' => 'dropdown-pages' ) );
}
add_action( 'customize_register', 'sh_customize_register' );

/**
 * Variables CSS issues du Customizer (ajoutées en ligne après style.css).
 *
 * @return string
 */
function sh_customizer_css() {
	$map = array(
		'--sh-night'  => 'color_night',
		'--sh-orange' => 'color_orange',
		'--sh-pink'   => 'color_pink',
		'--sh-yellow' => 'color_yellow',
		'--sh-cream'  => 'color_cream',
	);
	$css = '';
	foreach ( $map as $var => $key ) {
		$val = sanitize_hex_color( sh_mod( $key ) );
		if ( $val && strtolower( $val ) !== strtolower( sh_defaults()[ $key ] ) ) {
			$css .= $var . ':' . $val . ';';
		}
	}
	return $css ? ':root{' . $css . '}' : '';
}
