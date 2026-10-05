<?php
/**
 * Pages (mentions légales, CGV, panier, commande, mon compte…).
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
					<h1 class="sh-archive-head__title"><?php the_title(); ?></h1>
				</div>
			</header>
			<div class="sh-container sh-section">
				<div class="sh-paper sh-content">
					<?php
					the_content();
					wp_link_pages();
					?>
				</div>
			</div>
		</article>
	<?php endwhile; ?>
</main>
<?php
get_footer();
