<?php
/**
 * Accueil quand une page statique est définie comme page d'accueil
 * (Réglages › Lecture). Si la page d'accueil est la boutique WooCommerce,
 * c'est archive-product.php qui affiche ces mêmes sections.
 *
 * @package SurgeleHalal
 */

defined( 'ABSPATH' ) || exit;

get_header();
?>
<main id="main" class="sh-main sh-home" tabindex="-1">
	<?php get_template_part( 'template-parts/home-sections' ); ?>

	<?php
	// Contenu éventuel de la page d'accueil (éditeur de blocs), affiché après les sections.
	while ( 'page' === get_option( 'show_on_front' ) && have_posts() ) :
		the_post();
		if ( get_the_content() ) :
			?>
			<section class="sh-section sh-container sh-content">
				<?php the_content(); ?>
			</section>
			<?php
		endif;
	endwhile;
	?>
</main>
<?php
get_footer();
