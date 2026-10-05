<?php
/**
 * En-tête : bandeau défilant, header sticky, menu, recherche, mini-panier.
 *
 * @package SurgeleHalal
 */

defined( 'ABSPATH' ) || exit;
?><!doctype html>
<html <?php language_attributes(); ?>>
<head>
<meta charset="<?php bloginfo( 'charset' ); ?>">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#07070B">
<?php wp_head(); ?>
</head>
<body <?php body_class(); ?>>
<?php wp_body_open(); ?>
<a class="sh-skip" href="#main"><?php esc_html_e( 'Aller au contenu', 'surgele-halal' ); ?></a>

<?php $sh_ticker = sh_mod( 'ticker_text' ); ?>
<?php if ( $sh_ticker ) : ?>
<div class="sh-announce"><p><?php echo esc_html( $sh_ticker ); ?></p></div>
<?php endif; ?>

<header class="sh-header" id="sh-header">
	<div class="sh-header__inner">
		<?php sh_site_branding(); ?>

		<button class="sh-nav-toggle" type="button" aria-expanded="false" aria-controls="sh-nav" data-sh-nav-toggle>
			<?php echo sh_icon( 'menu' ); // phpcs:ignore WordPress.Security.EscapeOutput ?>
			<span><?php esc_html_e( 'Menu', 'surgele-halal' ); ?></span>
		</button>

		<nav class="sh-nav" id="sh-nav" aria-label="<?php esc_attr_e( 'Menu principal', 'surgele-halal' ); ?>">
			<?php
			wp_nav_menu(
				array(
					'theme_location' => 'primary',
					'container'      => false,
					'menu_class'     => 'sh-menu',
					'menu_id'        => 'sh-primary-menu',
					'depth'          => 2,
					'fallback_cb'    => 'sh_primary_menu_fallback',
				)
			);
			?>
		</nav>

		<?php sh_search_form( 'sh-search-header' ); ?>
		<?php sh_cart_button(); ?>
	</div>
</header>

<?php if ( class_exists( 'WooCommerce' ) ) : ?>
<div class="sh-drawer" id="sh-minicart" role="dialog" aria-modal="true" aria-labelledby="sh-minicart-title" hidden>
	<div class="sh-drawer__backdrop" data-sh-cart-close></div>
	<div class="sh-drawer__panel" tabindex="-1">
		<div class="sh-drawer__head">
			<h2 id="sh-minicart-title" class="sh-drawer__title"><?php esc_html_e( 'Mon panier', 'surgele-halal' ); ?></h2>
			<button type="button" class="sh-drawer__close" data-sh-cart-close aria-label="<?php esc_attr_e( 'Fermer le panier', 'surgele-halal' ); ?>"><?php echo sh_icon( 'close' ); // phpcs:ignore WordPress.Security.EscapeOutput ?></button>
		</div>
		<div class="sh-drawer__body" data-sh-cart-body aria-live="polite"></div>
		<div class="sh-drawer__foot">
			<p class="sh-drawer__total" data-sh-cart-total></p>
			<a class="sh-btn sh-btn--ghost" href="<?php echo esc_url( wc_get_cart_url() ); ?>"><?php esc_html_e( 'Voir le panier', 'surgele-halal' ); ?></a>
			<a class="sh-btn sh-btn--primary" href="<?php echo esc_url( wc_get_checkout_url() ); ?>"><?php esc_html_e( 'Commander', 'surgele-halal' ); ?></a>
		</div>
	</div>
</div>
<?php endif; ?>
<div class="sh-toast" role="status" aria-live="polite" data-sh-toast></div>
