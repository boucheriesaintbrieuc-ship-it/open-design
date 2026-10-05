<?php
/**
 * Sections de l'accueil : hero animé, 3 zones, best-sellers, garanties,
 * réassurance. Utilisé par front-page.php (page statique) et par
 * archive-product.php quand la boutique est la page d'accueil.
 *
 * @package SurgeleHalal
 */

defined( 'ABSPATH' ) || exit;

$sh_zones     = sh_zones();
$sh_shop_url  = function_exists( 'wc_get_page_permalink' ) ? wc_get_page_permalink( 'shop' ) : home_url( '/' );
$sh_shop_home = function_exists( 'wc_get_page_id' ) && 'page' === get_option( 'show_on_front' ) && (int) get_option( 'page_on_front' ) === wc_get_page_id( 'shop' );
$sh_cta2_url  = sh_mod( 'hero_cta2_url' ) ? sh_mod( 'hero_cta2_url' ) : ( $sh_shop_home ? '#sh-catalogue' : $sh_shop_url );
$sh_hero_img  = (int) sh_mod( 'hero_image' );
?>
<?php $sh_items = sh_showroom_items(); ?>
<section class="sh-hero" aria-labelledby="sh-hero-title">
	<div class="sh-stage" aria-hidden="true">
		<?php if ( $sh_hero_img ) : ?>
			<?php echo wp_get_attachment_image( $sh_hero_img, 'large', false, array( 'class' => 'sh-stage__bg', 'alt' => '', 'loading' => 'eager' ) ); ?>
		<?php endif; ?>
		<span class="sh-stage__pillar"></span><span class="sh-stage__pillar"></span><span class="sh-stage__pillar"></span>
		<span class="sh-stage__glow"></span>
		<span class="sh-stage__floor"></span>
	</div>

	<div class="sh-container sh-hero__inner">
		<div class="sh-hero__copy">
			<p class="sh-pill"><span class="sh-pill__dot" aria-hidden="true"></span><?php echo esc_html( sh_mod( 'hero_badge' ) ); ?></p>
			<h1 class="sh-hero__title" id="sh-hero-title">
				<span class="sh-hero__line"><?php echo esc_html( sh_mod( 'hero_title' ) ); ?></span>
				<span class="sh-hero__line sh-gradient-text"><?php echo esc_html( sh_mod( 'hero_highlight' ) ); ?></span>
			</h1>
			<p class="sh-hero__text"><?php echo esc_html( sh_mod( 'hero_text' ) ); ?></p>
			<ul class="sh-hero__stats" aria-label="<?php esc_attr_e( 'Garanties', 'surgele-halal' ); ?>">
				<li><strong>100 %</strong> <?php esc_html_e( 'halal', 'surgele-halal' ); ?></li>
				<li><strong>−18 °C</strong> <?php esc_html_e( 'chaîne du froid', 'surgele-halal' ); ?></li>
				<li><strong>Click &amp; Collect</strong> <?php esc_html_e( 'Saint-Brieuc', 'surgele-halal' ); ?></li>
			</ul>
		</div>

		<div class="sh-showroom" data-sh-showroom>
			<p class="screen-reader-text" id="sh-showroom-help"><?php esc_html_e( 'Utilisez les boutons précédent et suivant, ou les flèches du clavier, pour choisir un produit.', 'surgele-halal' ); ?></p>
			<ul class="sh-showroom__track" aria-describedby="sh-showroom-help">
				<?php foreach ( $sh_items as $sh_i => $sh_item ) : ?>
					<li class="sh-showroom__item<?php echo 0 === $sh_i ? ' is-active' : ''; ?>" data-index="<?php echo (int) $sh_i; ?>" data-url="<?php echo esc_url( $sh_item['url'] ); ?>" data-name="<?php echo esc_attr( $sh_item['name'] ); ?>" data-tag="<?php echo esc_attr( $sh_item['tag'] ); ?>"<?php echo 0 === $sh_i ? '' : ' aria-hidden="true"'; ?>>
						<img src="<?php echo esc_url( $sh_item['render'] ); ?>" alt="<?php echo esc_attr( sprintf( /* translators: %s: produit. */ __( '%s surgelés en 3D', 'surgele-halal' ), $sh_item['name'] ) ); ?>" width="640" height="640" <?php echo 0 === $sh_i ? 'fetchpriority="high"' : 'loading="lazy"'; ?> decoding="async">
					</li>
				<?php endforeach; ?>
			</ul>
			<div class="sh-showroom__hud">
				<button type="button" class="sh-round-btn" data-sh-prev aria-label="<?php esc_attr_e( 'Produit précédent', 'surgele-halal' ); ?>"><?php echo sh_icon( 'prev' ); // phpcs:ignore WordPress.Security.EscapeOutput ?></button>
				<div class="sh-showroom__label" aria-live="polite">
					<span class="sh-showroom__tag" data-sh-tag><?php echo esc_html( $sh_items[0]['tag'] ); ?></span>
					<span class="sh-showroom__name" data-sh-name><?php echo esc_html( $sh_items[0]['name'] ); ?></span>
				</div>
				<button type="button" class="sh-round-btn" data-sh-next aria-label="<?php esc_attr_e( 'Produit suivant', 'surgele-halal' ); ?>"><?php echo sh_icon( 'next' ); // phpcs:ignore WordPress.Security.EscapeOutput ?></button>
			</div>
			<div class="sh-hero__ctas">
				<a class="sh-btn sh-btn--primary sh-btn--xl" data-sh-cta href="<?php echo esc_url( $sh_items[0]['url'] ); ?>"><?php echo esc_html( sh_mod( 'hero_cta_label' ) ); ?> <span class="screen-reader-text" data-sh-cta-name><?php echo esc_html( $sh_items[0]['name'] ); ?></span></a>
				<a class="sh-btn sh-btn--ghost sh-btn--xl" href="<?php echo esc_url( $sh_cta2_url ); ?>"><?php echo esc_html( sh_mod( 'hero_cta2_label' ) ); ?></a>
			</div>
		</div>
	</div>
	<div class="sh-ticker" aria-hidden="true"><p class="sh-ticker__track"><?php foreach ( array_merge( $sh_items, $sh_items ) as $sh_item ) : ?><span><?php echo esc_html( $sh_item['name'] ); ?></span><?php endforeach; ?></p></div>
</section>

<section class="sh-section sh-container" aria-labelledby="sh-zones-title">
	<p class="sh-kicker"><?php esc_html_e( 'Rayons', 'surgele-halal' ); ?></p>
	<h2 class="sh-h2" id="sh-zones-title"><?php esc_html_e( 'Choisis ton univers', 'surgele-halal' ); ?></h2>
	<ul class="sh-zones">
		<?php foreach ( $sh_zones as $sh_zone ) : ?>
			<li>
				<a class="sh-zone sh-zone--<?php echo (int) $sh_zone['index']; ?>" href="<?php echo esc_url( $sh_zone['url'] ); ?>">
					<span class="sh-zone__kicker"><?php echo esc_html( $sh_zone['kicker'] ); ?></span>
					<img class="sh-zone__render" src="<?php echo esc_url( $sh_zone['render'] ); ?>" alt="" width="640" height="640" loading="lazy" decoding="async">
					<span class="sh-zone__body">
						<span class="sh-zone__name"><?php echo esc_html( $sh_zone['label'] ); ?></span>
						<span class="sh-zone__text"><?php echo esc_html( $sh_zone['text'] ); ?></span>
						<span class="sh-zone__go">
							<?php
							if ( null !== $sh_zone['count'] ) {
								/* translators: %d: nombre de produits. */
								echo esc_html( sprintf( _n( '%d produit', '%d produits', $sh_zone['count'], 'surgele-halal' ), $sh_zone['count'] ) );
							} else {
								esc_html_e( 'Découvrir', 'surgele-halal' );
							}
							echo sh_icon( 'arrow' ); // phpcs:ignore WordPress.Security.EscapeOutput
							?>
						</span>
					</span>
				</a>
			</li>
		<?php endforeach; ?>
	</ul>
</section>

<?php if ( class_exists( 'WooCommerce' ) ) : ?>
<section class="sh-band sh-band--inventory" aria-labelledby="sh-best-title">
	<div class="sh-container">
		<div class="sh-section-head">
			<div>
				<p class="sh-kicker"><?php esc_html_e( 'Best-sellers', 'surgele-halal' ); ?></p>
				<h2 class="sh-h2" id="sh-best-title"><?php echo esc_html( sh_mod( 'best_title' ) ); ?></h2>
			</div>
			<a class="sh-link-arrow" href="<?php echo esc_url( $sh_shop_url ); ?>"><?php esc_html_e( 'Tout le catalogue', 'surgele-halal' ); ?> <?php echo sh_icon( 'arrow' ); // phpcs:ignore WordPress.Security.EscapeOutput ?></a>
		</div>
		<?php
		$sh_count = max( 2, min( 16, (int) sh_mod( 'best_count' ) ) );
		echo do_shortcode( '[products limit="' . $sh_count . '" columns="4" best_selling="true" visibility="visible"]' );
		?>
	</div>
</section>
<?php endif; ?>

<section class="sh-trust" aria-label="<?php esc_attr_e( 'Garanties', 'surgele-halal' ); ?>">
	<div class="sh-container sh-trust__grid">
		<p class="sh-trust__big"><?php echo esc_html( sh_mod( 'trust_title_1' ) ); ?></p>
		<p class="sh-trust__big"><?php echo esc_html( sh_mod( 'trust_title_2' ) ); ?></p>
		<p class="sh-trust__text"><?php echo esc_html( sh_mod( 'trust_text' ) ); ?></p>
	</div>
</section>

<section class="sh-section sh-container" aria-labelledby="sh-reas-title">
	<h2 class="sh-h2 sh-h2--sm" id="sh-reas-title"><?php esc_html_e( 'Simple, rapide, au froid', 'surgele-halal' ); ?></h2>
	<ul class="sh-reas">
		<?php
		$sh_icons = array( 1 => 'store', 2 => 'card', 3 => 'snow' );
		foreach ( $sh_icons as $sh_i => $sh_icon ) :
			?>
			<li class="sh-reas__item">
				<?php echo sh_icon( $sh_icon ); // phpcs:ignore WordPress.Security.EscapeOutput ?>
				<h3><?php echo esc_html( sh_mod( "reas_{$sh_i}_title" ) ); ?></h3>
				<p><?php echo esc_html( sh_mod( "reas_{$sh_i}_text" ) ); ?></p>
			</li>
		<?php endforeach; ?>
	</ul>
</section>
