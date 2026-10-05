<?php
/**
 * Bandeau d'en-tête des archives produits (boutique, catégorie, étiquette, recherche).
 *
 * @package SurgeleHalal
 */

defined( 'ABSPATH' ) || exit;

$sh_is_home_shop = ! empty( $args['is_home_shop'] );
$sh_zone_index   = 0;
$sh_kicker       = __( 'Catalogue complet', 'surgele-halal' );
$sh_render       = '';

if ( is_product_category() ) {
	$sh_term = get_queried_object();
	foreach ( sh_zones() as $sh_zone ) {
		if ( $sh_zone['term'] && (int) $sh_zone['term']->term_id === (int) $sh_term->term_id ) {
			$sh_zone_index = (int) $sh_zone['index'];
			$sh_kicker     = $sh_zone['kicker'];
			$sh_render     = $sh_zone['render'];
		}
	}
	if ( ! $sh_zone_index ) {
		$sh_kicker = __( 'Rayon', 'surgele-halal' );
	}
} elseif ( is_search() ) {
	$sh_kicker = __( 'Recherche', 'surgele-halal' );
}

// Sur l'accueil-boutique, le h1 est celui du hero : ici un h2.
$sh_heading_tag = $sh_is_home_shop ? 'h2' : 'h1';
?>
<header class="sh-archive-head<?php echo $sh_zone_index ? ' sh-archive-head--zone' . (int) $sh_zone_index : ''; ?>">
	<?php if ( $sh_render ) : ?>
		<img class="sh-archive-head__render" src="<?php echo esc_url( $sh_render ); ?>" alt="" width="640" height="640" fetchpriority="high">
	<?php endif; ?>
	<div class="sh-container">
		<p class="sh-kicker"><?php echo esc_html( $sh_kicker ); ?></p>
		<<?php echo tag_escape( $sh_heading_tag ); ?> class="sh-archive-head__title">
			<?php
			if ( $sh_is_home_shop ) {
				esc_html_e( 'Tout le catalogue', 'surgele-halal' );
			} else {
				woocommerce_page_title();
			}
			?>
		</<?php echo tag_escape( $sh_heading_tag ); ?>>
		<?php if ( is_product_taxonomy() && 0 === absint( get_query_var( 'paged' ) ) ) : ?>
			<div class="sh-archive-head__desc"><?php echo wp_kses_post( wpautop( term_description() ) ); ?></div>
		<?php endif; ?>
	</div>
</header>
