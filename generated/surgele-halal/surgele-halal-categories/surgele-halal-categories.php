<?php
/**
 * Plugin Name: Surgelé Halal — Rangement des catégories
 * Description: Crée les catégories Poissons, Poulet et Crousty si elles n'existent pas, puis y AJOUTE les produits existants selon des mots-clés du titre. Ne retire aucune catégorie, ne modifie aucun autre champ. Mode simulation, journal et annulation. WP-CLI : wp surgele ranger --dry-run
 * Version: 1.0.0
 * Requires at least: 6.4
 * Requires PHP: 7.4
 * Author: Surgelé Halal Saint-Brieuc
 * License: GPL-2.0-or-later
 * Text Domain: surgele-halal-categories
 *
 * @package SurgeleHalalCategories
 */

defined( 'ABSPATH' ) || exit;

/**
 * Logique de rangement (sans effet tant que run() n'est pas appelé avec $apply = true).
 */
final class SH_Category_Sorter {

	const LOG_OPTION = 'sh_category_sorter_log';

	/**
	 * Catégories cibles et règles. L'ordre compte : la première règle qui
	 * correspond l'emporte (« Tenders de poulet » → Crousty, pas Poulet).
	 * Les motifs sont appliqués sur le titre en minuscules et sans accents,
	 * avec limites de mots.
	 *
	 * Filtre : sh_category_sorter_rules.
	 *
	 * @return array<string, array{name:string, description:string, patterns:string[]}>
	 */
	public static function rules() {
		$rules = array(
			'crousty'  => array(
				'name'        => 'Crousty',
				'description' => 'Tenders, nuggets, cordons bleus, kebab, panés : le snacking qui croustille.',
				'patterns'    => array(
					'tenders?',
					'nuggets?',
					'cordons? bleus?',
					'kebabs?',
					'panes?',
					'panees?',
					'fingers?',
					'burgers?',
					'samoussas?',
					'crousty',
					'croustillants?',
					'strips?',
				),
			),
			'poissons' => array(
				'name'        => 'Poissons',
				'description' => 'Tilapia, dorade, maquereau et autres poissons surgelés.',
				'patterns'    => array(
					'tilapias?',
					'dorades?',
					'maquereaux?',
					'poissons?',
					'chinchards?',
					'sardines?',
					'merlus?',
					'colins?',
					'saumons?',
					'cabillauds?',
					'thons?',
					'crevettes?',
					'calamars?',
					'capitaines?',
					'soles?',
				),
			),
			'poulet'   => array(
				'name'        => 'Poulet',
				'description' => 'Cuisses, ailes, pilons, poulet entier.',
				'patterns'    => array(
					'cuisses?',
					'hauts? de cuisses?',
					'ailes?',
					'ailerons?',
					'wings',
					'pilons?',
					'manchons?',
					'poulets? entiers?',
					'poulets?',
					'poules?',
					'coquelets?',
				),
			),
		);
		return apply_filters( 'sh_category_sorter_rules', $rules );
	}

	/**
	 * Normalise un titre pour la recherche de mots-clés.
	 *
	 * @param string $title Titre.
	 * @return string
	 */
	public static function normalize( $title ) {
		$title = wp_specialchars_decode( wp_strip_all_tags( (string) $title ), ENT_QUOTES );
		$title = remove_accents( $title );
		return strtolower( $title );
	}

	/**
	 * Trouve la catégorie cible d'un titre.
	 *
	 * @param string $title Titre du produit.
	 * @return array{slug:string, keyword:string}|null
	 */
	public static function match( $title ) {
		$haystack = self::normalize( $title );
		foreach ( self::rules() as $slug => $rule ) {
			foreach ( $rule['patterns'] as $pattern ) {
				if ( preg_match( '/(?<![a-z0-9])(' . $pattern . ')(?![a-z0-9])/u', $haystack, $m ) ) {
					return array(
						'slug'    => $slug,
						'keyword' => $m[1],
					);
				}
			}
		}
		return null;
	}

	/**
	 * Calcule (et éventuellement applique) le rangement.
	 *
	 * @param bool $apply true pour écrire, false pour simuler.
	 * @return array{created:string[], rows:array<int, array<string, mixed>>, summary:array<string,int>}
	 */
	public static function run( $apply ) {
		if ( ! taxonomy_exists( 'product_cat' ) ) {
			return array( 'created' => array(), 'rows' => array(), 'summary' => array(), 'error' => 'WooCommerce n’est pas actif (taxonomie product_cat absente).' );
		}

		$rules   = self::rules();
		$terms   = array();
		$created = array();

		foreach ( $rules as $slug => $rule ) {
			$term = get_term_by( 'slug', $slug, 'product_cat' );
			if ( ! $term ) {
				// Une catégorie existante portant déjà ce nom (slug différent) est réutilisée.
				$existing = term_exists( $rule['name'], 'product_cat' );
				if ( $existing ) {
					$term = get_term( (int) $existing['term_id'], 'product_cat' );
				}
			}
			if ( $term && ! is_wp_error( $term ) ) {
				$terms[ $slug ] = (int) $term->term_id;
				continue;
			}
			$created[] = $rule['name'];
			if ( $apply ) {
				$res = wp_insert_term(
					$rule['name'],
					'product_cat',
					array(
						'slug'        => $slug,
						'description' => $rule['description'],
					)
				);
				if ( is_wp_error( $res ) ) {
					return array( 'created' => $created, 'rows' => array(), 'summary' => array(), 'error' => $res->get_error_message() );
				}
				$terms[ $slug ] = (int) $res['term_id'];
			} else {
				$terms[ $slug ] = 0; // Sera créée lors de l'exécution réelle.
			}
		}

		$ids = get_posts(
			array(
				'post_type'        => 'product',
				'post_status'      => array( 'publish', 'private', 'draft', 'pending', 'future' ),
				'posts_per_page'   => -1,
				'fields'           => 'ids',
				'orderby'          => 'ID',
				'order'            => 'ASC',
				'suppress_filters' => true,
			)
		);

		$rows    = array();
		$summary = array( 'total' => count( $ids ), 'to_add' => 0, 'already' => 0, 'no_match' => 0 );
		$log     = $apply ? get_option( self::LOG_OPTION, array() ) : array();
		$batch   = array();

		foreach ( $ids as $id ) {
			$title   = get_the_title( $id );
			$current = wp_get_object_terms( $id, 'product_cat', array( 'fields' => 'all' ) );
			$current = is_wp_error( $current ) ? array() : $current;
			$names   = wp_list_pluck( $current, 'name' );
			$cur_ids = array_map( 'intval', wp_list_pluck( $current, 'term_id' ) );
			$match   = self::match( $title );

			$row = array(
				'id'         => $id,
				'titre'      => html_entity_decode( $title, ENT_QUOTES, 'UTF-8' ),
				'statut'     => get_post_status( $id ),
				'actuelles'  => $names ? implode( ', ', $names ) : '—',
				'cible'      => $match ? $rules[ $match['slug'] ]['name'] : '—',
				'mot_cle'    => $match ? $match['keyword'] : '—',
				'action'     => 'aucune (pas de mot-clé)',
			);

			if ( ! $match ) {
				++$summary['no_match'];
			} elseif ( $terms[ $match['slug'] ] && in_array( $terms[ $match['slug'] ], $cur_ids, true ) ) {
				++$summary['already'];
				$row['action'] = 'déjà rangé';
			} else {
				++$summary['to_add'];
				$row['action'] = $apply ? 'ajoutée' : 'à ajouter';
				if ( $apply ) {
					// append = true : les catégories actuelles sont conservées.
					$res = wp_set_object_terms( $id, array( $terms[ $match['slug'] ] ), 'product_cat', true );
					if ( is_wp_error( $res ) ) {
						$row['action'] = 'ERREUR : ' . $res->get_error_message();
					} else {
						$batch[] = array( $id, $terms[ $match['slug'] ] );
						if ( function_exists( 'wc_delete_product_transients' ) ) {
							wc_delete_product_transients( $id );
						}
					}
				}
			}
			$rows[] = $row;
		}

		if ( $apply ) {
			$log[] = array(
				'date'    => current_time( 'mysql' ),
				'user'    => get_current_user_id(),
				'created' => $created,
				'added'   => $batch,
			);
			update_option( self::LOG_OPTION, $log, false );
			if ( function_exists( '_wc_term_recount' ) ) {
				$all = get_terms( array( 'taxonomy' => 'product_cat', 'hide_empty' => false ) );
				if ( ! is_wp_error( $all ) ) {
					_wc_term_recount( $all, get_taxonomy( 'product_cat' ), true, false );
				}
			}
			clean_taxonomy_cache( 'product_cat' );
		}

		return array( 'created' => $created, 'rows' => $rows, 'summary' => $summary );
	}

	/**
	 * Annule la dernière exécution : retire uniquement les liaisons produit →
	 * catégorie ajoutées par ce plugin. Les catégories créées sont conservées
	 * (vides) pour ne casser aucun lien ; supprimez-les à la main si besoin.
	 *
	 * @return int Nombre de liaisons retirées.
	 */
	public static function undo_last() {
		$log = get_option( self::LOG_OPTION, array() );
		if ( ! $log ) {
			return 0;
		}
		$last  = array_pop( $log );
		$count = 0;
		foreach ( $last['added'] as $pair ) {
			list( $product_id, $term_id ) = $pair;
			$res = wp_remove_object_terms( (int) $product_id, (int) $term_id, 'product_cat' );
			if ( true === $res ) {
				++$count;
			}
		}
		update_option( self::LOG_OPTION, $log, false );
		clean_taxonomy_cache( 'product_cat' );
		return $count;
	}
}

/*
 * ---------------------------------------------------------------
 * WP-CLI
 * ---------------------------------------------------------------
 */
if ( defined( 'WP_CLI' ) && WP_CLI ) {

	/**
	 * Range les produits WooCommerce dans Poissons / Poulet / Crousty.
	 */
	class SH_Category_CLI {

		/**
		 * Ajoute Poissons / Poulet / Crousty aux produits selon leur titre (sans retirer de catégorie).
		 *
		 * ## OPTIONS
		 *
		 * [--dry-run]
		 * : Simulation : affiche les affectations prévues sans rien écrire.
		 *
		 * [--yes]
		 * : Ne pas demander de confirmation avant l'écriture.
		 *
		 * [--only-changes]
		 * : N'afficher que les produits qui vont recevoir une catégorie.
		 *
		 * [--format=<format>]
		 * : Format de sortie.
		 * ---
		 * default: table
		 * options:
		 *   - table
		 *   - csv
		 *   - json
		 * ---
		 *
		 * ## EXAMPLES
		 *
		 *     wp surgele ranger --dry-run
		 *     wp surgele ranger --dry-run --format=csv > simulation.csv
		 *     wp surgele ranger
		 *
		 * @param array $args       Arguments.
		 * @param array $assoc_args Options.
		 */
		public function ranger( $args, $assoc_args ) {
			$dry    = (bool) \WP_CLI\Utils\get_flag_value( $assoc_args, 'dry-run', false );
			$format = \WP_CLI\Utils\get_flag_value( $assoc_args, 'format', 'table' );
			$only   = (bool) \WP_CLI\Utils\get_flag_value( $assoc_args, 'only-changes', false );

			if ( ! $dry ) {
				$preview = SH_Category_Sorter::run( false );
				if ( ! empty( $preview['error'] ) ) {
					WP_CLI::error( $preview['error'] );
				}
				WP_CLI::log( sprintf( '%d produit(s) vont recevoir une catégorie ; aucune catégorie existante ne sera retirée.', $preview['summary']['to_add'] ) );
				WP_CLI::confirm( 'Appliquer maintenant ?', $assoc_args );
			}

			$result = SH_Category_Sorter::run( ! $dry );
			if ( ! empty( $result['error'] ) ) {
				WP_CLI::error( $result['error'] );
			}

			$rows = $result['rows'];
			if ( $only ) {
				$rows = array_values(
					array_filter(
						$rows,
						function ( $r ) {
							return in_array( $r['action'], array( 'à ajouter', 'ajoutée' ), true );
						}
					)
				);
			}
			\WP_CLI\Utils\format_items( $format, $rows, array( 'id', 'titre', 'statut', 'actuelles', 'cible', 'mot_cle', 'action' ) );

			if ( 'table' === $format ) {
				if ( $result['created'] ) {
					WP_CLI::log( ( $dry ? 'Catégories à créer : ' : 'Catégories créées : ' ) . implode( ', ', $result['created'] ) );
				}
				$s = $result['summary'];
				WP_CLI::log( sprintf( 'Produits : %d · %s : %d · déjà rangés : %d · sans mot-clé (inchangés) : %d', $s['total'], $dry ? 'à ajouter' : 'ajoutés', $s['to_add'], $s['already'], $s['no_match'] ) );
				if ( $dry ) {
					WP_CLI::success( 'Simulation terminée : rien n’a été écrit.' );
				} else {
					WP_CLI::success( 'Rangement appliqué. Pour revenir en arrière : wp surgele annuler' );
				}
			}
		}

		/**
		 * Annule la dernière exécution réelle (retire seulement les liaisons ajoutées par l'outil).
		 *
		 * ## OPTIONS
		 *
		 * [--yes]
		 * : Ne pas demander de confirmation.
		 *
		 * @param array $args       Arguments.
		 * @param array $assoc_args Options.
		 */
		public function annuler( $args, $assoc_args ) {
			WP_CLI::confirm( 'Retirer les catégories ajoutées lors de la dernière exécution ?', $assoc_args );
			$n = SH_Category_Sorter::undo_last();
			WP_CLI::success( sprintf( '%d liaison(s) retirée(s).', $n ) );
		}
	}

	WP_CLI::add_command( 'surgele', 'SH_Category_CLI' );
}

/*
 * ---------------------------------------------------------------
 * Page d'outil (Outils › Ranger les catégories) pour qui n'a pas WP-CLI
 * ---------------------------------------------------------------
 */
add_action(
	'admin_menu',
	function () {
		add_management_page(
			'Ranger les catégories produits',
			'Ranger les catégories',
			'manage_woocommerce',
			'sh-category-sorter',
			'sh_category_sorter_page'
		);
	}
);

/**
 * Rendu de la page d'outil.
 */
function sh_category_sorter_page() {
	if ( ! current_user_can( 'manage_woocommerce' ) ) {
		wp_die( esc_html__( 'Accès refusé.', 'surgele-halal-categories' ) );
	}

	$mode   = '';
	$result = null;
	$undone = null;

	if ( isset( $_POST['sh_action'] ) ) {
		check_admin_referer( 'sh_category_sorter' );
		$mode = sanitize_key( wp_unslash( $_POST['sh_action'] ) );
		if ( 'simulate' === $mode ) {
			$result = SH_Category_Sorter::run( false );
		} elseif ( 'apply' === $mode ) {
			$result = SH_Category_Sorter::run( true );
		} elseif ( 'undo' === $mode ) {
			$undone = SH_Category_Sorter::undo_last();
		}
	}

	$log = get_option( SH_Category_Sorter::LOG_OPTION, array() );
	?>
	<div class="wrap">
		<h1>Ranger les catégories produits</h1>
		<p>Cet outil <strong>ajoute</strong> les catégories <em>Poissons</em>, <em>Poulet</em> et <em>Crousty</em> aux produits selon des mots-clés de leur titre. Il ne retire aucune catégorie, ne modifie ni prix, ni stock, ni description. Commencez toujours par la simulation.</p>

		<?php if ( null !== $undone ) : ?>
			<div class="notice notice-success"><p><?php echo esc_html( sprintf( '%d liaison(s) retirée(s). Les catégories créées restent en place (vides si plus aucun produit).', $undone ) ); ?></p></div>
		<?php endif; ?>

		<?php if ( $result && ! empty( $result['error'] ) ) : ?>
			<div class="notice notice-error"><p><?php echo esc_html( $result['error'] ); ?></p></div>
		<?php elseif ( $result ) : ?>
			<?php $s = $result['summary']; ?>
			<div class="notice <?php echo 'apply' === $mode ? 'notice-success' : 'notice-info'; ?>">
				<p><strong><?php echo 'apply' === $mode ? 'Rangement appliqué.' : 'Simulation : rien n’a été écrit.'; ?></strong>
				<?php echo esc_html( sprintf( 'Produits : %d · %s : %d · déjà rangés : %d · sans mot-clé (inchangés) : %d.', $s['total'], 'apply' === $mode ? 'ajoutés' : 'à ajouter', $s['to_add'], $s['already'], $s['no_match'] ) ); ?>
				<?php if ( $result['created'] ) : ?>
					<?php echo esc_html( ( 'apply' === $mode ? ' Catégories créées : ' : ' Catégories à créer : ' ) . implode( ', ', $result['created'] ) . '.' ); ?>
				<?php endif; ?>
				</p>
			</div>
			<table class="widefat striped">
				<thead><tr><th>ID</th><th>Produit</th><th>Statut</th><th>Catégories actuelles</th><th>Cible</th><th>Mot-clé</th><th>Action</th></tr></thead>
				<tbody>
				<?php foreach ( $result['rows'] as $r ) : ?>
					<tr>
						<td><?php echo (int) $r['id']; ?></td>
						<td><a href="<?php echo esc_url( get_edit_post_link( $r['id'] ) ); ?>"><?php echo esc_html( $r['titre'] ); ?></a></td>
						<td><?php echo esc_html( $r['statut'] ); ?></td>
						<td><?php echo esc_html( $r['actuelles'] ); ?></td>
						<td><strong><?php echo esc_html( $r['cible'] ); ?></strong></td>
						<td><code><?php echo esc_html( $r['mot_cle'] ); ?></code></td>
						<td><?php echo esc_html( $r['action'] ); ?></td>
					</tr>
				<?php endforeach; ?>
				</tbody>
			</table>
		<?php endif; ?>

		<form method="post" style="margin-top:20px;display:flex;gap:10px;flex-wrap:wrap">
			<?php wp_nonce_field( 'sh_category_sorter' ); ?>
			<button class="button button-secondary" name="sh_action" value="simulate">1. Simuler (aucune écriture)</button>
			<?php if ( 'simulate' === $mode && $result && empty( $result['error'] ) ) : ?>
				<button class="button button-primary" name="sh_action" value="apply" onclick="return confirm('Appliquer le rangement affiché ?');">2. Appliquer ce rangement</button>
			<?php endif; ?>
			<?php if ( $log ) : ?>
				<button class="button" name="sh_action" value="undo" onclick="return confirm('Retirer les catégories ajoutées lors de la dernière exécution ?');">Annuler la dernière exécution</button>
			<?php endif; ?>
		</form>
	</div>
	<?php
}
