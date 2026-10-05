<?php
/**
 * Intégration WooCommerce : enveloppes, badges, filtres, mini-panier,
 * données structurées. Aucune requête d'écriture en base.
 *
 * @package SurgeleHalal
 */

defined( 'ABSPATH' ) || exit;

/*
 * Enveloppes de contenu : on remplace celles de WooCommerce par les nôtres.
 */
remove_action( 'woocommerce_before_main_content', 'woocommerce_output_content_wrapper', 10 );
remove_action( 'woocommerce_after_main_content', 'woocommerce_output_content_wrapper_end', 10 );
remove_action( 'woocommerce_sidebar', 'woocommerce_get_sidebar', 10 );

add_action(
	'woocommerce_before_main_content',
	function () {
		echo '<main id="main" class="sh-main sh-shop-main" tabindex="-1">';
	},
	5
);
add_action(
	'woocommerce_after_main_content',
	function () {
		echo '</main>';
	},
	50
);

/*
 * Fil d'Ariane : celui de Yoast s'il est actif (cohérent avec son schema
 * BreadcrumbList), sinon celui de WooCommerce.
 */
remove_action( 'woocommerce_before_main_content', 'woocommerce_breadcrumb', 20 );
add_action( 'woocommerce_before_main_content', 'sh_breadcrumb', 20 );

/**
 * Affiche le fil d'Ariane (pas sur l'accueil).
 */
function sh_breadcrumb() {
	if ( is_front_page() ) {
		return;
	}
	echo '<div class="sh-container sh-crumbs-wrap">';
	if ( function_exists( 'yoast_breadcrumb' ) && class_exists( 'WPSEO_Options' ) && WPSEO_Options::get( 'breadcrumbs-enable', false ) ) {
		yoast_breadcrumb( '<nav class="sh-crumbs" aria-label="' . esc_attr__( 'Fil d’Ariane', 'surgele-halal' ) . '">', '</nav>' );
	} else {
		woocommerce_breadcrumb(
			array(
				'wrap_before' => '<nav class="sh-crumbs woocommerce-breadcrumb" aria-label="' . esc_attr__( 'Fil d’Ariane', 'surgele-halal' ) . '">',
				'wrap_after'  => '</nav>',
				'delimiter'   => '<span aria-hidden="true"> / </span>',
			)
		);
	}
	echo '</div>';
}

/*
 * En-tête des archives : notre bandeau « zone » remplace le titre standard.
 */
remove_action( 'woocommerce_shop_loop_header', 'woocommerce_product_taxonomy_archive_header', 10 );
add_filter( 'woocommerce_show_page_title', '__return_false' );

/*
 * Titre des cartes produit : h2 dans les archives (sous le h1 de la page),
 * h3 dans les sections de l'accueil (sous les h2 de section).
 */
remove_action( 'woocommerce_shop_loop_item_title', 'woocommerce_template_loop_product_title', 10 );
add_action( 'woocommerce_shop_loop_item_title', 'sh_loop_product_title', 10 );

/**
 * Titre de carte produit.
 */
function sh_loop_product_title() {
	$tag = ( is_shop() || is_product_taxonomy() || is_search() ) && ! wc_get_loop_prop( 'is_shortcode' ) ? 'h2' : 'h3';
	printf(
		'<%1$s class="%2$s">%3$s</%1$s>',
		tag_escape( $tag ),
		esc_attr( apply_filters( 'woocommerce_product_loop_title_classes', 'woocommerce-loop-product__title sh-card__title' ) ),
		esc_html( get_the_title() )
	);
}

/*
 * Badges sur les cartes (sur l'image) et sur la fiche produit.
 */
add_action( 'woocommerce_before_shop_loop_item_title', 'sh_loop_badges', 11 );
add_action( 'woocommerce_single_product_summary', 'sh_single_badges', 4 );

/**
 * Poids lisible d'un produit : poids WooCommerce, attribut « poids »,
 * ou motif dans le titre (ex. « 2kg », « 360g »). Lecture seule.
 *
 * @param WC_Product $product Produit.
 * @return string
 */
function sh_product_weight_label( $product ) {
	if ( ! $product instanceof WC_Product ) {
		return '';
	}
	if ( $product->is_type( 'variable' ) && count( $product->get_children() ) > 1 ) {
		return __( 'Plusieurs formats', 'surgele-halal' );
	}
	$weight = $product->get_weight();
	if ( '' !== $weight && null !== $weight ) {
		return wc_format_weight( $weight );
	}
	foreach ( array( 'pa_poids', 'poids', 'pa_weight' ) as $attr ) {
		$val = $product->get_attribute( $attr );
		if ( $val ) {
			return $val;
		}
	}
	if ( preg_match( '/(\d+(?:[.,]\d+)?)\s?(kg|g)\b/i', $product->get_name(), $m ) ) {
		return str_replace( '.', ',', $m[1] ) . ' ' . strtolower( $m[2] );
	}
	return '';
}

/**
 * Liste de badges pour un produit.
 *
 * @param WC_Product $product Produit.
 * @return array<int, array{class:string,label:string}>
 */
function sh_product_badges( $product ) {
	$badges = array();
	if ( sh_mod( 'badge_halal' ) ) {
		$badges[] = array( 'class' => 'halal', 'label' => __( 'Halal', 'surgele-halal' ) );
	}
	if ( sh_mod( 'badge_frozen' ) ) {
		$badges[] = array( 'class' => 'frozen', 'label' => __( 'Surgelé −18 °C', 'surgele-halal' ) );
	}
	if ( sh_mod( 'badge_weight' ) ) {
		$weight = sh_product_weight_label( $product );
		if ( $weight ) {
			$badges[] = array( 'class' => 'weight', 'label' => $weight );
		}
	}
	return apply_filters( 'sh_product_badges', $badges, $product );
}

/**
 * Rendu HTML des badges.
 *
 * @param array  $badges Badges.
 * @param string $extra  Classe additionnelle.
 */
function sh_render_badges( $badges, $extra = '' ) {
	if ( ! $badges ) {
		return;
	}
	echo '<ul class="sh-badges ' . esc_attr( $extra ) . '" aria-label="' . esc_attr__( 'Caractéristiques', 'surgele-halal' ) . '">';
	foreach ( $badges as $b ) {
		echo '<li class="sh-badge sh-badge--' . esc_attr( $b['class'] ) . '">' . esc_html( $b['label'] ) . '</li>';
	}
	echo '</ul>';
}

/**
 * Badges des cartes : uniquement halal + poids, pour ne pas surcharger.
 */
function sh_loop_badges() {
	global $product;
	$badges = array_values(
		array_filter(
			sh_product_badges( $product ),
			function ( $b ) {
				return 'frozen' !== $b['class'];
			}
		)
	);
	sh_render_badges( $badges, 'sh-badges--card' );
}

/**
 * Badges de la fiche produit (tous).
 */
function sh_single_badges() {
	global $product;
	sh_render_badges( sh_product_badges( $product ), 'sh-badges--single' );
}

/*
 * Pastille « Promo » : texte court, style badge.
 */
add_filter(
	'woocommerce_sale_flash',
	function () {
		return '<span class="onsale sh-flash">' . esc_html__( 'Promo', 'surgele-halal' ) . '</span>';
	}
);

/*
 * Encart conservation sur la fiche produit (après le bouton panier).
 */
add_action(
	'woocommerce_single_product_summary',
	function () {
		echo '<div class="sh-storage"><strong>' . esc_html__( 'Conservation', 'surgele-halal' ) . '</strong> ';
		echo esc_html__( 'À conserver à −18 °C. Ne jamais recongeler un produit décongelé.', 'surgele-halal' ) . '</div>';
	},
	35
);

/*
 * Produits apparentés : 4 colonnes.
 */
add_filter(
	'woocommerce_output_related_products_args',
	function ( $args ) {
		$args['posts_per_page'] = 4;
		$args['columns']        = 4;
		return $args;
	}
);

/*
 * Données structurées Product : on garde celles de WooCommerce (reprises
 * ou remplacées par Yoast SEO / Yoast WooCommerce SEO s'ils sont actifs),
 * on n'en émet pas de seconde copie. On ajoute seulement « brand » quand
 * il manque et qu'une catégorie « marque » est attribuée au produit.
 */
add_filter( 'woocommerce_structured_data_product', 'sh_structured_data_brand', 10, 2 );

/**
 * Ajoute la marque au schema Product.
 *
 * @param array      $markup  Données.
 * @param WC_Product $product Produit.
 * @return array
 */
function sh_structured_data_brand( $markup, $product ) {
	if ( ! empty( $markup['brand'] ) || ! $product instanceof WC_Product ) {
		return $markup;
	}
	$brand_slugs = array_filter( array_map( 'sanitize_title', explode( ',', (string) sh_mod( 'brand_cats' ) ) ) );
	if ( ! $brand_slugs ) {
		return $markup;
	}
	$terms = get_the_terms( $product->get_id(), 'product_cat' );
	if ( $terms && ! is_wp_error( $terms ) ) {
		foreach ( $terms as $term ) {
			if ( in_array( $term->slug, $brand_slugs, true ) ) {
				$markup['brand'] = array(
					'@type' => 'Brand',
					'name'  => $term->name,
				);
				break;
			}
		}
	}
	return $markup;
}

/*
 * Mode léger : l'ajout au panier des listes passe par l'API Store de
 * WooCommerce en JavaScript natif (assets/js/theme.js). Les scripts jQuery
 * correspondants deviennent inutiles sur les pages de liste. Sans JS, les
 * boutons restent de simples liens « ?add-to-cart= » qui fonctionnent.
 */
add_action(
	'wp_enqueue_scripts',
	function () {
		if ( ! sh_mod( 'light_mode' ) ) {
			return;
		}
		wp_dequeue_script( 'wc-cart-fragments' );
		if ( ! is_product() && ! is_cart() && ! is_checkout() ) {
			wp_dequeue_script( 'wc-add-to-cart' );
		}
	},
	99
);

/**
 * Nombre d'articles du panier (0 hors contexte front).
 *
 * @return int
 */
function sh_cart_count() {
	if ( ! function_exists( 'WC' ) || ! WC()->cart ) {
		return 0;
	}
	return (int) WC()->cart->get_cart_contents_count();
}

/*
 * Fragments (si le mode léger est désactivé et que wc-cart-fragments tourne) :
 * le compteur du header reste synchronisé.
 */
add_filter(
	'woocommerce_add_to_cart_fragments',
	function ( $fragments ) {
		$fragments['span.sh-cart-count'] = '<span class="sh-cart-count" data-sh-cart-count>' . sh_cart_count() . '</span>';
		return $fragments;
	}
);

/*
 * Les pages panier, commande et compte sont rendues sur un « écran de
 * mission » clair : les formulaires et blocs WooCommerce y gardent leur
 * contraste prévu.
 */
add_filter(
	'body_class',
	function ( $classes ) {
		if ( is_cart() || is_checkout() || is_account_page() ) {
			$classes[] = 'sh-paper-page';
		}
		return $classes;
	}
);
