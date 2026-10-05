<?php
/**
 * The Template for displaying product archives, including the main shop page which is a post type archive
 *
 * Surcharge du thème Surgelé Halal : mêmes hooks que le gabarit WooCommerce
 * d'origine (les extensions continuent de s'y accrocher), avec en plus :
 * - les sections d'accueil quand la boutique EST la page d'accueil (page 1) ;
 * - un bandeau « zone » en tête d'archive ;
 * - une colonne de filtres par catégorie.
 *
 * @see https://woocommerce.com/document/template-structure/
 * @package WooCommerce\Templates
 * @version 8.6.0
 */

defined( 'ABSPATH' ) || exit;

get_header( 'shop' );

do_action( 'woocommerce_before_main_content' );

$sh_is_home_shop = is_shop() && is_front_page() && ! is_paged() && ! is_search();

if ( $sh_is_home_shop ) {
	get_template_part( 'template-parts/home-sections' );
}

get_template_part( 'template-parts/shop-header', null, array( 'is_home_shop' => $sh_is_home_shop ) );

do_action( 'woocommerce_shop_loop_header' );
?>
<div class="sh-container sh-shop" id="sh-catalogue">
	<?php get_template_part( 'template-parts/shop-filters' ); ?>

	<div class="sh-shop__results">
		<?php
		if ( woocommerce_product_loop() ) {

			/**
			 * Hook: woocommerce_before_shop_loop.
			 *
			 * @hooked woocommerce_output_all_notices - 10
			 * @hooked woocommerce_result_count - 20
			 * @hooked woocommerce_catalog_ordering - 30
			 */
			echo '<div class="sh-shop__toolbar">';
			do_action( 'woocommerce_before_shop_loop' );
			echo '</div>';

			woocommerce_product_loop_start();

			if ( wc_get_loop_prop( 'total' ) ) {
				while ( have_posts() ) {
					the_post();

					/**
					 * Hook: woocommerce_shop_loop.
					 */
					do_action( 'woocommerce_shop_loop' );

					wc_get_template_part( 'content', 'product' );
				}
			}

			woocommerce_product_loop_end();

			/**
			 * Hook: woocommerce_after_shop_loop.
			 *
			 * @hooked woocommerce_pagination - 10
			 */
			do_action( 'woocommerce_after_shop_loop' );
		} else {
			/**
			 * Hook: woocommerce_no_products_found.
			 *
			 * @hooked wc_no_products_found - 10
			 */
			do_action( 'woocommerce_no_products_found' );
		}
		?>
	</div>
</div>
<?php
do_action( 'woocommerce_after_main_content' );

do_action( 'woocommerce_sidebar' );

get_footer( 'shop' );
