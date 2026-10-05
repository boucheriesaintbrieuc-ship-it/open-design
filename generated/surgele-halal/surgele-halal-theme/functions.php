<?php
/**
 * Surgelé Halal — GTA Tasty Crousty : fonctions du thème.
 *
 * Le thème est purement présentationnel : il n'écrit rien en base à
 * l'activation (aucun produit, catégorie, page ou menu n'est créé,
 * modifié ou supprimé). Les seules données qu'il stocke sont les réglages
 * du Customizer (theme_mods), propres au thème.
 *
 * @package SurgeleHalal
 */

defined( 'ABSPATH' ) || exit;

define( 'SH_VERSION', '1.0.0' );
define( 'SH_DIR', get_template_directory() );
define( 'SH_URI', get_template_directory_uri() );

require SH_DIR . '/inc/helpers.php';
require SH_DIR . '/inc/customizer.php';
require SH_DIR . '/inc/template-tags.php';

if ( class_exists( 'WooCommerce' ) ) {
	require SH_DIR . '/inc/woocommerce.php';
}

/**
 * Supports du thème.
 */
function sh_setup() {
	load_theme_textdomain( 'surgele-halal', SH_DIR . '/languages' );

	add_theme_support( 'title-tag' );
	add_theme_support( 'automatic-feed-links' );
	add_theme_support( 'post-thumbnails' );
	add_theme_support( 'responsive-embeds' );
	add_theme_support( 'html5', array( 'search-form', 'comment-form', 'comment-list', 'gallery', 'caption', 'style', 'script', 'navigation-widgets' ) );
	add_theme_support(
		'custom-logo',
		array(
			'height'      => 120,
			'width'       => 360,
			'flex-height' => true,
			'flex-width'  => true,
		)
	);

	// WooCommerce + galerie produit (zoom, lightbox, slider).
	add_theme_support(
		'woocommerce',
		array(
			'thumbnail_image_width' => 600,
			'single_image_width'    => 900,
			'product_grid'          => array(
				'default_rows'    => 4,
				'min_rows'        => 1,
				'default_columns' => 4,
				'min_columns'     => 2,
				'max_columns'     => 6,
			),
		)
	);
	add_theme_support( 'wc-product-gallery-zoom' );
	add_theme_support( 'wc-product-gallery-lightbox' );
	add_theme_support( 'wc-product-gallery-slider' );

	register_nav_menus(
		array(
			'primary' => __( 'Menu principal', 'surgele-halal' ),
			'footer'  => __( 'Pied de page — liens', 'surgele-halal' ),
			'legal'   => __( 'Pied de page — légal', 'surgele-halal' ),
		)
	);
}
add_action( 'after_setup_theme', 'sh_setup' );

/**
 * Largeur de contenu pour les médias intégrés.
 */
function sh_content_width() {
	$GLOBALS['content_width'] = 1240;
}
add_action( 'after_setup_theme', 'sh_content_width', 0 );

/**
 * Zone de widgets optionnelle (colonne filtres de la boutique).
 */
function sh_widgets_init() {
	register_sidebar(
		array(
			'name'          => __( 'Filtres boutique (sous la liste des zones)', 'surgele-halal' ),
			'id'            => 'shop-filters',
			'description'   => __( 'Widgets ajoutés sous les filtres de catégories dans la boutique.', 'surgele-halal' ),
			'before_widget' => '<section id="%1$s" class="sh-filter-block widget %2$s">',
			'after_widget'  => '</section>',
			'before_title'  => '<h2 class="sh-filter-block__title">',
			'after_title'   => '</h2>',
		)
	);
}
add_action( 'widgets_init', 'sh_widgets_init' );

/**
 * Styles et scripts : un seul CSS, un seul JS (vanilla, différé), polices
 * auto-hébergées (pas d'appel à Google : plus rapide et conforme RGPD).
 */
function sh_assets() {
	wp_enqueue_style( 'surgele-halal', get_stylesheet_uri(), array(), SH_VERSION );
	wp_add_inline_style( 'surgele-halal', sh_customizer_css() );

	wp_enqueue_script(
		'surgele-halal',
		SH_URI . '/assets/js/theme.js',
		array(),
		SH_VERSION,
		array(
			'in_footer' => true,
			'strategy'  => 'defer',
		)
	);

	$config = array(
		'storeApi' => esc_url_raw( rest_url( 'wc/store/v1/' ) ),
		'nonce'    => class_exists( 'WooCommerce' ) ? wp_create_nonce( 'wc_store_api' ) : '',
		'cartUrl'  => function_exists( 'wc_get_cart_url' ) ? wc_get_cart_url() : '',
		'checkout' => function_exists( 'wc_get_checkout_url' ) ? wc_get_checkout_url() : '',
		'ajaxCart' => class_exists( 'WooCommerce' ) && sh_mod( 'light_mode' ),
		'i18n'     => array(
			'added'    => __( '%s ajouté au panier.', 'surgele-halal' ),
			'empty'    => __( 'Ton panier est vide. Lance une mission !', 'surgele-halal' ),
			'error'    => __( 'Impossible de mettre à jour le panier. Réessaie.', 'surgele-halal' ),
			'remove'   => __( 'Retirer %s du panier', 'surgele-halal' ),
			'subtotal' => __( 'Sous-total', 'surgele-halal' ),
			'loading'  => __( 'Chargement du panier…', 'surgele-halal' ),
			'items'    => __( 'Mon panier, %d article(s)', 'surgele-halal' ),
		),
	);
	wp_add_inline_script( 'surgele-halal', 'window.SH_CONFIG = ' . wp_json_encode( $config ) . ';', 'before' );

	if ( is_singular() && comments_open() && get_option( 'thread_comments' ) ) {
		wp_enqueue_script( 'comment-reply' );
	}
}
add_action( 'wp_enqueue_scripts', 'sh_assets' );

/**
 * Précharge la police d'affichage (titres) : évite le saut de mise en page du hero.
 */
function sh_preload_fonts() {
	printf(
		'<link rel="preload" href="%s" as="font" type="font/woff2" crossorigin>' . "\n",
		esc_url( SH_URI . '/assets/fonts/unbounded-latin.woff2' )
	);
}
add_action( 'wp_head', 'sh_preload_fonts', 1 );

/**
 * Icône O'Surgelé par défaut tant qu'aucune icône de site n'est définie
 * (Personnaliser › Identité du site).
 */
function sh_default_favicon() {
	if ( has_site_icon() ) {
		return;
	}
	printf( '<link rel="icon" type="image/svg+xml" href="%s">' . "\n", esc_url( SH_URI . '/assets/img/brand/osurgele-icon.svg' ) );
}
add_action( 'wp_head', 'sh_default_favicon', 2 );

/**
 * Lien d'évitement + classe "js" posée avant le rendu (pas de flash).
 */
function sh_body_open() {
	echo '<script>document.documentElement.classList.add("js");</script>';
}
add_action( 'wp_body_open', 'sh_body_open', 1 );

/*
 * Script et styles d'emojis WordPress : inutiles ici, retirés pour alléger.
 * (Le lazy-load natif des images reste celui de WordPress.)
 */
remove_action( 'wp_head', 'print_emoji_detection_script', 7 );
remove_action( 'wp_print_styles', 'print_emoji_styles' );
