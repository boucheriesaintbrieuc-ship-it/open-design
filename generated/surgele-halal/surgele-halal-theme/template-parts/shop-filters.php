<?php
/**
 * Filtres par catégorie (liens : indexables, sans JS, compatibles cache).
 * Les 3 zones en premier, puis les autres catégories existantes
 * (marques, desserts…), toutes conservées.
 *
 * @package SurgeleHalal
 */

defined( 'ABSPATH' ) || exit;

$sh_current_id = is_product_category() ? (int) get_queried_object_id() : 0;
$sh_zone_ids   = array();
$sh_shop_url   = wc_get_page_permalink( 'shop' );
?>
<aside class="sh-filters" aria-labelledby="sh-filters-title">
	<details class="sh-filters__details" open>
		<summary class="sh-filters__summary"><h2 id="sh-filters-title" class="sh-filters__title"><?php esc_html_e( 'Filtrer par zone', 'surgele-halal' ); ?></h2></summary>
		<ul class="sh-filters__list sh-filters__list--zones">
			<?php foreach ( sh_zones() as $sh_zone ) : ?>
				<?php
				if ( ! $sh_zone['term'] ) {
					continue;
				}
				$sh_zone_ids[] = (int) $sh_zone['term']->term_id;
				$sh_is_current = $sh_current_id === (int) $sh_zone['term']->term_id;
				?>
				<li>
					<a class="sh-chip sh-chip--zone<?php echo (int) $sh_zone['index']; ?>" href="<?php echo esc_url( $sh_zone['url'] ); ?>"<?php echo $sh_is_current ? ' aria-current="page"' : ''; ?>>
						<?php echo esc_html( $sh_zone['label'] ); ?> <span class="sh-chip__count">(<?php echo (int) $sh_zone['count']; ?>)</span>
					</a>
				</li>
			<?php endforeach; ?>
			<li>
				<a class="sh-chip" href="<?php echo esc_url( $sh_shop_url ); ?>"<?php echo is_shop() && ! is_search() ? ' aria-current="page"' : ''; ?>><?php esc_html_e( 'Tout voir', 'surgele-halal' ); ?></a>
			</li>
		</ul>

		<?php
		$sh_others = get_terms(
			array(
				'taxonomy'   => 'product_cat',
				'hide_empty' => true,
				'parent'     => 0,
				'exclude'    => array_merge( $sh_zone_ids, array( (int) get_option( 'default_product_cat' ) ) ),
				'orderby'    => 'name',
			)
		);
		if ( $sh_others && ! is_wp_error( $sh_others ) ) :
			?>
			<h3 class="sh-filters__sub"><?php esc_html_e( 'Autres rayons', 'surgele-halal' ); ?></h3>
			<ul class="sh-filters__list">
				<?php foreach ( $sh_others as $sh_term ) : ?>
					<li>
						<a class="sh-chip sh-chip--small" href="<?php echo esc_url( get_term_link( $sh_term ) ); ?>"<?php echo $sh_current_id === (int) $sh_term->term_id ? ' aria-current="page"' : ''; ?>>
							<?php echo esc_html( $sh_term->name ); ?> <span class="sh-chip__count">(<?php echo (int) $sh_term->count; ?>)</span>
						</a>
					</li>
				<?php endforeach; ?>
			</ul>
		<?php endif; ?>
	</details>

	<?php if ( is_active_sidebar( 'shop-filters' ) ) : ?>
		<?php dynamic_sidebar( 'shop-filters' ); ?>
	<?php endif; ?>
</aside>
