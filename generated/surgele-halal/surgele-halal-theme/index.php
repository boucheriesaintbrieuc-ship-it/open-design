<?php
/**
 * Gabarit de repli (articles, archives, résultats de recherche hors produits).
 *
 * @package SurgeleHalal
 */

defined( 'ABSPATH' ) || exit;

get_header();
?>
<main id="main" class="sh-main" tabindex="-1">
	<header class="sh-archive-head">
		<div class="sh-container">
			<h1 class="sh-archive-head__title">
				<?php
				if ( is_search() ) {
					/* translators: %s: terme recherché. */
					printf( esc_html__( 'Recherche : %s', 'surgele-halal' ), esc_html( get_search_query() ) );
				} elseif ( is_archive() ) {
					echo wp_kses_post( get_the_archive_title() );
				} elseif ( is_home() && get_option( 'page_for_posts' ) ) {
					echo esc_html( get_the_title( (int) get_option( 'page_for_posts' ) ) );
				} else {
					esc_html_e( 'Actualités', 'surgele-halal' );
				}
				?>
			</h1>
		</div>
	</header>

	<div class="sh-container sh-section">
		<?php if ( have_posts() ) : ?>
			<ul class="sh-posts">
				<?php
				while ( have_posts() ) :
					the_post();
					?>
					<li <?php post_class( 'sh-post-card' ); ?>>
						<?php if ( has_post_thumbnail() ) : ?>
							<?php the_post_thumbnail( 'medium_large', array( 'class' => 'sh-post-card__img' ) ); ?>
						<?php endif; ?>
						<h2 class="sh-post-card__title"><a href="<?php the_permalink(); ?>"><?php the_title(); ?></a></h2>
						<p class="sh-post-card__meta"><?php echo esc_html( get_the_date() ); ?></p>
						<?php the_excerpt(); ?>
					</li>
				<?php endwhile; ?>
			</ul>
			<?php the_posts_pagination( array( 'mid_size' => 1 ) ); ?>
		<?php else : ?>
			<p><?php esc_html_e( 'Aucun résultat. Essaie un autre mot-clé :', 'surgele-halal' ); ?></p>
			<?php sh_search_form( 'sh-search-empty' ); ?>
		<?php endif; ?>
	</div>
</main>
<?php
get_footer();
