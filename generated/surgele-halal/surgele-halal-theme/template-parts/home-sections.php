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
$sh_crousty   = $sh_zones[2]['url'];
?>
<section class="sh-hero" aria-labelledby="sh-hero-title">
	<div class="sh-hero__sky" aria-hidden="true">
		<span></span><span></span><span></span><span></span><span></span><span></span><span></span>
	</div>
	<div class="sh-hero__sun" aria-hidden="true"></div>
	<div class="sh-hero__crumbs" aria-hidden="true"><i></i><i></i><i></i><i></i><i></i><i></i></div>

	<div class="sh-container sh-hero__inner">
		<div class="sh-hero__copy">
			<p class="sh-mission"><span class="sh-mission__dot" aria-hidden="true"></span><?php echo esc_html( sh_mod( 'hero_badge' ) ); ?></p>
			<h1 class="sh-hero__title" id="sh-hero-title">
				<span class="sh-hero__line"><?php echo esc_html( sh_mod( 'hero_title' ) ); ?></span>
				<span class="sh-hero__line sh-hero__hl"><?php echo esc_html( sh_mod( 'hero_highlight' ) ); ?></span>
			</h1>
			<p class="sh-hero__text"><?php echo esc_html( sh_mod( 'hero_text' ) ); ?></p>
			<div class="sh-hero__ctas">
				<a class="sh-btn sh-btn--primary sh-btn--xl" href="<?php echo esc_url( $sh_crousty ); ?>"><?php echo esc_html( sh_mod( 'hero_cta_label' ) ); ?></a>
				<a class="sh-btn sh-btn--outline sh-btn--xl" href="<?php echo esc_url( $sh_cta2_url ); ?>"><?php echo esc_html( sh_mod( 'hero_cta2_label' ) ); ?></a>
			</div>
		</div>

		<div class="sh-hero__side">
			<?php if ( $sh_hero_img ) : ?>
				<?php
				echo wp_get_attachment_image(
					$sh_hero_img,
					'large',
					false,
					array(
						'class'         => 'sh-hero__img',
						'loading'       => 'eager',
						'fetchpriority' => 'high',
						'sizes'         => '(max-width: 900px) 90vw, 520px',
					)
				);
				?>
			<?php endif; ?>
			<div class="sh-hud">
				<p class="sh-hud__title"><?php esc_html_e( 'Objectifs', 'surgele-halal' ); ?></p>
				<ul>
					<li><?php esc_html_e( 'Certifié halal', 'surgele-halal' ); ?> <?php echo sh_icon( 'check' ); // phpcs:ignore WordPress.Security.EscapeOutput ?></li>
					<li><?php esc_html_e( 'Stocké à −18 °C', 'surgele-halal' ); ?> <?php echo sh_icon( 'check' ); // phpcs:ignore WordPress.Security.EscapeOutput ?></li>
					<li><?php esc_html_e( 'Retrait sur place', 'surgele-halal' ); ?> <?php echo sh_icon( 'check' ); // phpcs:ignore WordPress.Security.EscapeOutput ?></li>
				</ul>
				<div class="sh-hud__bar" aria-hidden="true"><span></span></div>
			</div>
		</div>
	</div>
</section>

<section class="sh-section sh-container" aria-labelledby="sh-zones-title">
	<p class="sh-kicker sh-kicker--pink"><?php esc_html_e( 'Carte de la ville', 'surgele-halal' ); ?></p>
	<h2 class="sh-h2" id="sh-zones-title"><?php esc_html_e( 'Choisis ta zone', 'surgele-halal' ); ?></h2>
	<ul class="sh-zones">
		<?php foreach ( $sh_zones as $sh_zone ) : ?>
			<li>
				<a class="sh-zone sh-zone--<?php echo (int) $sh_zone['index']; ?>" href="<?php echo esc_url( $sh_zone['url'] ); ?>">
					<span class="sh-zone__kicker"><?php echo esc_html( $sh_zone['kicker'] ); ?></span>
					<span class="sh-zone__body">
						<span class="sh-zone__name"><?php echo esc_html( $sh_zone['label'] ); ?></span>
						<span class="sh-zone__text"><?php echo esc_html( $sh_zone['text'] ); ?></span>
						<span class="sh-zone__go">
							<?php
							if ( null !== $sh_zone['count'] ) {
								/* translators: %d: nombre de produits. */
								echo esc_html( sprintf( _n( 'Entrer · %d produit', 'Entrer · %d produits', $sh_zone['count'], 'surgele-halal' ), $sh_zone['count'] ) );
							} else {
								esc_html_e( 'Entrer', 'surgele-halal' );
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
				<p class="sh-kicker"><?php esc_html_e( 'Inventaire · top butin', 'surgele-halal' ); ?></p>
				<h2 class="sh-h2" id="sh-best-title"><?php echo esc_html( sh_mod( 'best_title' ) ); ?></h2>
			</div>
			<a class="sh-link-arrow" href="<?php echo esc_url( $sh_shop_url ); ?>"><?php esc_html_e( 'Tout l’inventaire', 'surgele-halal' ); ?> <?php echo sh_icon( 'arrow' ); // phpcs:ignore WordPress.Security.EscapeOutput ?></a>
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
	<h2 class="sh-h2 sh-h2--sm" id="sh-reas-title"><?php esc_html_e( 'Bonus débloqués', 'surgele-halal' ); ?></h2>
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
