<?php
/**
 * Article de blog.
 *
 * @package SurgeleHalal
 */

defined( 'ABSPATH' ) || exit;

get_header();
?>
<main id="main" class="sh-main" tabindex="-1">
	<?php
	while ( have_posts() ) :
		the_post();
		?>
		<article id="post-<?php the_ID(); ?>" <?php post_class( 'sh-page' ); ?>>
			<header class="sh-archive-head sh-archive-head--compact">
				<div class="sh-container">
					<p class="sh-kicker"><time datetime="<?php echo esc_attr( get_the_date( 'c' ) ); ?>"><?php echo esc_html( get_the_date() ); ?></time></p>
					<h1 class="sh-archive-head__title"><?php the_title(); ?></h1>
				</div>
			</header>
			<div class="sh-container sh-section">
				<div class="sh-paper sh-content">
					<?php
					if ( has_post_thumbnail() ) {
						the_post_thumbnail( 'large' );
					}
					the_content();
					wp_link_pages();
					?>
				</div>
				<?php
				if ( comments_open() || get_comments_number() ) {
					comments_template();
				}
				?>
			</div>
		</article>
	<?php endwhile; ?>
</main>
<?php
get_footer();
