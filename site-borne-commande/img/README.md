# Visuels à fournir

Le site fonctionne aujourd’hui sans aucune photo : le produit est dessiné en SVG,
directement dans les pages. C’est net à toutes les tailles, ça pèse deux kilo-octets
et ça ne fait aucune requête réseau. Mais un dessin ne remplace pas une photo pour
vendre du matériel à 499 €.

## Ce qu’il faut, par ordre d’importance

| Fichier | Format | Dimensions | Contenu |
|---|---|---|---|
| `borne-commande-restaurant-face.jpg` | WebP ou JPEG | 1400 × 1400 | La borne entière, de face, écran allumé, sur fond neutre |
| `borne-commande-restaurant-profil.jpg` | WebP ou JPEG | 1400 × 1400 | De profil, la platine et la colonne visibles |
| `borne-en-situation.jpg` | WebP ou JPEG | 1600 × 1200 | La borne posée dans un vrai restaurant, à hauteur d’œil |
| `borne-socle.jpg` | WebP ou JPEG | 1200 × 900 | Le socle et le passage de câble, de près |
| `og-borne-commande-restaurant.jpg` | JPEG | 1200 × 630 | Image de partage, référencée dans toutes les pages |

## Deux règles qui évitent les ennuis

Les photos du fournisseur lui appartiennent. Les publier sur un site marchand
français sans autorisation écrite expose à une action en contrefaçon, et le fait
que tout le monde le fasse n’y change rien. Le script `outils/telecharger-images.sh`
sert à les récupérer pour travailler, pas à les publier telles quelles.

La photo en situation vaut plus que les quatre autres réunies. Un packshot
identique à celui de trente autres revendeurs ne prouve rien. Une borne visible
dans une vraie salle, avec un vrai comptoir derrière, prouve que le produit existe
et que vous l’avez eu entre les mains.
