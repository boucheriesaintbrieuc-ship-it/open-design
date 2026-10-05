<?php
/**
 * The Template for displaying all single products
 *
 * Surcharge du thème Surgelé Halal : structure WooCommerce d'origine
 * (galerie zoom/lightbox/slider, onglets, produits apparentés), habillée
 * par le thème. Les badges halal / surgelé / poids sont ajoutés via
 * le hook woocommerce_single_product_summary (inc/woocommerce.php).
 *
 * @see         https://woocommerce.com/document/template-structure/
 * @package     WooCommerce\Templates
 * @version     1.6.4
 */

defined( 'ABSPATH' ) || exit;

get_header( 'shop' );

/**
 * Hook: woocommerce_before_main_content.
 *
 * @hooked sh main wrapper - 5
 * @hooked sh_breadcrumb - 20
 */
do_action( 'woocommerce_before_main_content' );
?>
<div class="sh-container sh-single">
	<?php
	while ( have_posts() ) :
		the_post();
		wc_get_template_part( 'content', 'single-product' );
	endwhile;
	?>
</div>
<?php
/**
 * Hook: woocommerce_after_main_content.
 */
do_action( 'woocommerce_after_main_content' );

/**
 * Hook: woocommerce_sidebar (retiré par le thème : pleine largeur).
 */
do_action( 'woocommerce_sidebar' );

get_footer( 'shop' );
