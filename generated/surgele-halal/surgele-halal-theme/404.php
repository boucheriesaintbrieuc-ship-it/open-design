<?php
/**
 * Page introuvable.
 *
 * @package SurgeleHalal
 */

defined( 'ABSPATH' ) || exit;

get_header();
?>
<main id="main" class="sh-main" tabindex="-1">
	<section class="sh-container sh-section sh-404">
		<p class="sh-mission"><span class="sh-mission__dot" aria-hidden="true"></span><?php esc_html_e( 'Mission échouée', 'surgele-halal' ); ?></p>
		<h1 class="sh-h1"><?php esc_html_e( 'Page introuvable', 'surgele-halal' ); ?></h1>
		<p><?php esc_html_e( 'Cette page n’existe pas ou a été déplacée. Reprends la partie :', 'surgele-halal' ); ?></p>
		<?php sh_search_form( 'sh-search-404' ); ?>
		<ul class="sh-filters__list sh-404__zones">
			<?php foreach ( sh_zones() as $sh_zone ) : ?>
				<li><a class="sh-chip sh-chip--zone<?php echo (int) $sh_zone['index']; ?>" href="<?php echo esc_url( $sh_zone['url'] ); ?>"><?php echo esc_html( $sh_zone['label'] ); ?></a></li>
			<?php endforeach; ?>
		</ul>
	</section>
</main>
<?php
get_footer();
