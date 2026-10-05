<?php
/**
 * Fragments de gabarits réutilisés.
 *
 * @package SurgeleHalal
 */

defined( 'ABSPATH' ) || exit;

/**
 * Logo (Customizer) ou logotype typographique.
 */
function sh_site_branding() {
	if ( has_custom_logo() ) {
		the_custom_logo();
		return;
	}
	// Logo O'Surgelé fourni avec le thème (SVG vectoriel, version pour fond sombre).
	printf(
		'<p class="sh-brand"><a href="%1$s" rel="home"><img src="%2$s" alt="%3$s" width="220" height="34"></a></p>',
		esc_url( home_url( '/' ) ),
		esc_url( SH_URI . '/assets/img/brand/osurgele-logo-light.svg' ),
		esc_attr( get_bloginfo( 'name' ) )
	);
}

/**
 * Menu principal par défaut tant qu'aucun menu n'est assigné :
 * les 3 zones + la boutique.
 */
function sh_primary_menu_fallback() {
	echo '<ul id="sh-primary-menu" class="sh-menu">';
	foreach ( sh_zones() as $zone ) {
		$current = $zone['term'] && is_tax( 'product_cat', $zone['term']->term_id );
		printf(
			'<li class="menu-item sh-menu__zone sh-menu__zone--%1$d%2$s"><a href="%3$s"%4$s>%5$s</a></li>',
			(int) $zone['index'],
			$current ? ' current-menu-item' : '',
			esc_url( $zone['url'] ),
			$current ? ' aria-current="page"' : '',
			esc_html( $zone['label'] )
		);
	}
	if ( function_exists( 'wc_get_page_permalink' ) ) {
		$is_shop = function_exists( 'is_shop' ) && is_shop();
		printf(
			'<li class="menu-item%1$s"><a href="%2$s"%3$s>%4$s</a></li>',
			$is_shop ? ' current-menu-item' : '',
			esc_url( wc_get_page_permalink( 'shop' ) ),
			$is_shop ? ' aria-current="page"' : '',
			esc_html__( 'Toute la boutique', 'surgele-halal' )
		);
	}
	echo '</ul>';
}

/**
 * Bouton du mini-panier (header).
 */
function sh_cart_button() {
	if ( ! class_exists( 'WooCommerce' ) ) {
		return;
	}
	$count = sh_cart_count();
	printf(
		'<a class="sh-cart-btn" href="%1$s" data-sh-cart-toggle aria-controls="sh-minicart" aria-label="%2$s">%3$s<span class="sh-cart-count" data-sh-cart-count>%4$d</span></a>',
		esc_url( wc_get_cart_url() ),
		/* translators: %d: nombre d'articles. */
		esc_attr( sprintf( __( 'Mon panier, %d article(s)', 'surgele-halal' ), $count ) ),
		sh_icon( 'cart' ), // phpcs:ignore WordPress.Security.EscapeOutput -- SVG statique.
		(int) $count
	);
}

/**
 * Formulaire de recherche produits (ou articles si WooCommerce est absent).
 *
 * @param string $id Identifiant unique du champ.
 */
function sh_search_form( $id = 'sh-search' ) {
	?>
	<form role="search" method="get" class="sh-search" action="<?php echo esc_url( home_url( '/' ) ); ?>">
		<label class="screen-reader-text" for="<?php echo esc_attr( $id ); ?>"><?php esc_html_e( 'Rechercher un produit', 'surgele-halal' ); ?></label>
		<input type="search" id="<?php echo esc_attr( $id ); ?>" name="s" value="<?php echo esc_attr( get_search_query() ); ?>" placeholder="<?php esc_attr_e( 'Tenders, dorade, wings…', 'surgele-halal' ); ?>" autocomplete="off">
		<?php if ( class_exists( 'WooCommerce' ) ) : ?>
			<input type="hidden" name="post_type" value="product">
		<?php endif; ?>
		<button type="submit" aria-label="<?php esc_attr_e( 'Lancer la recherche', 'surgele-halal' ); ?>"><?php echo sh_icon( 'search' ); // phpcs:ignore WordPress.Security.EscapeOutput ?></button>
	</form>
	<?php
}

/**
 * Lien vers la page de mentions légales choisie dans le Customizer.
 *
 * @return string URL ou chaîne vide.
 */
function sh_legal_url() {
	$id = (int) sh_mod( 'legal_page' );
	if ( $id && 'publish' === get_post_status( $id ) ) {
		return get_permalink( $id );
	}
	return '';
}
