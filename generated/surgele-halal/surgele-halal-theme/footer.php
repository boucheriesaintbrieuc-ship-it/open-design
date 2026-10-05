<?php
/**
 * Pied de page : présentation, zones, liens, mentions légales.
 *
 * @package SurgeleHalal
 */

defined( 'ABSPATH' ) || exit;
?>
<footer class="sh-footer">
	<div class="sh-container sh-footer__grid">
		<div class="sh-footer__about">
			<p class="sh-footer__name"><?php echo esc_html( get_bloginfo( 'name' ) ); ?></p>
			<p><?php echo esc_html( sh_mod( 'footer_about' ) ); ?></p>
		</div>

		<nav aria-labelledby="sh-foot-zones">
			<h2 class="sh-footer__title" id="sh-foot-zones"><?php esc_html_e( 'Zones', 'surgele-halal' ); ?></h2>
			<ul>
				<?php foreach ( sh_zones() as $sh_zone ) : ?>
					<li><a href="<?php echo esc_url( $sh_zone['url'] ); ?>"><?php echo esc_html( $sh_zone['label'] ); ?></a></li>
				<?php endforeach; ?>
			</ul>
		</nav>

		<?php if ( has_nav_menu( 'footer' ) ) : ?>
			<nav aria-labelledby="sh-foot-links">
				<h2 class="sh-footer__title" id="sh-foot-links"><?php esc_html_e( 'Infos', 'surgele-halal' ); ?></h2>
				<?php wp_nav_menu( array( 'theme_location' => 'footer', 'container' => false, 'depth' => 1 ) ); ?>
			</nav>
		<?php endif; ?>

		<nav aria-labelledby="sh-foot-legal">
			<h2 class="sh-footer__title" id="sh-foot-legal"><?php esc_html_e( 'Légal', 'surgele-halal' ); ?></h2>
			<?php if ( has_nav_menu( 'legal' ) ) : ?>
				<?php wp_nav_menu( array( 'theme_location' => 'legal', 'container' => false, 'depth' => 1 ) ); ?>
			<?php else : ?>
				<ul>
					<?php
					$sh_links = array();
					if ( sh_legal_url() ) {
						$sh_links[] = array( sh_legal_url(), __( 'Mentions légales', 'surgele-halal' ) );
					}
					if ( function_exists( 'wc_terms_and_conditions_page_id' ) && wc_terms_and_conditions_page_id() ) {
						$sh_links[] = array( get_permalink( wc_terms_and_conditions_page_id() ), __( 'Conditions générales de vente', 'surgele-halal' ) );
					}
					if ( get_privacy_policy_url() ) {
						$sh_links[] = array( get_privacy_policy_url(), __( 'Politique de confidentialité', 'surgele-halal' ) );
					}
					foreach ( $sh_links as $sh_link ) {
						printf( '<li><a href="%s">%s</a></li>', esc_url( $sh_link[0] ), esc_html( $sh_link[1] ) );
					}
					if ( ! $sh_links && current_user_can( 'customize' ) ) {
						echo '<li>' . esc_html__( 'Choisissez la page « Mentions légales » dans Apparence › Personnaliser › Pied de page.', 'surgele-halal' ) . '</li>';
					}
					?>
				</ul>
			<?php endif; ?>
		</nav>
	</div>
	<div class="sh-container sh-footer__bottom">
		<p>&copy; <?php echo esc_html( wp_date( 'Y' ) ); ?> <?php echo esc_html( get_bloginfo( 'name' ) ); ?> · <?php esc_html_e( 'Produits certifiés halal · Chaîne du froid respectée', 'surgele-halal' ); ?></p>
	</div>
</footer>
<?php wp_footer(); ?>
</body>
</html>
