#!/usr/bin/env bash
# Télécharge les photos du fournisseur et les range dans img/.
#
# Pourquoi un script plutôt qu'un lien direct : AliExpress bloque les accès
# automatisés depuis un serveur, et surtout, pointer une balise <img> vers
# leur CDN est une mauvaise idée. Le lien casse le jour où ils changent de
# référence, et chaque visiteur de votre site envoie son adresse IP à
# Alibaba, ce qui vous oblige à un bandeau de consentement.
# Les images doivent donc vivre sur votre hébergement.
#
# Mode d'emploi
#   1. Ouvrez la fiche du fournisseur dans votre navigateur.
#   2. Clic droit sur chaque photo utile > « Copier l'adresse de l'image ».
#   3. Collez les adresses dans le tableau URLS ci-dessous, une par ligne.
#   4. bash outils/telecharger-images.sh
#
# Le script convertit en WebP si cwebp est installé, sinon il garde le JPEG.

set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p img

URLS=(
  # "https://ae01.alicdn.com/kf/EXEMPLE1.jpg"
  # "https://ae01.alicdn.com/kf/EXEMPLE2.jpg"
)

NOMS=(
  "borne-commande-restaurant-face"
  "borne-commande-restaurant-profil"
  "borne-commande-restaurant-socle"
  "borne-commande-restaurant-ecran"
)

if [ ${#URLS[@]} -eq 0 ]; then
  echo "Aucune adresse dans le tableau URLS. Ouvrez ce fichier et collez-les d'abord." >&2
  exit 1
fi

UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"

for i in "${!URLS[@]}"; do
  url="${URLS[$i]}"
  nom="${NOMS[$i]:-image-$i}"
  echo "→ $nom"
  if ! curl -fsSL -A "$UA" -e "https://fr.aliexpress.com/" "$url" -o "img/$nom.jpg"; then
    echo "   échec du téléchargement, enregistrez l'image à la main dans img/$nom.jpg" >&2
    continue
  fi
  if command -v cwebp >/dev/null 2>&1; then
    cwebp -quiet -q 82 -resize 1400 0 "img/$nom.jpg" -o "img/$nom.webp"
    echo "   img/$nom.webp ($(du -h "img/$nom.webp" | cut -f1))"
  else
    echo "   img/$nom.jpg ($(du -h "img/$nom.jpg" | cut -f1)) — installez cwebp pour diviser le poids par trois"
  fi
done

cat <<'FIN'

Fait. Deux points avant de publier ces images :

1. Une photo de catalogue fournisseur appartient au fournisseur. La reprendre
   telle quelle sur un site marchand français est un risque de contrefaçon,
   même quand tout le monde le fait. Demandez l'autorisation écrite au vendeur,
   ou photographiez l'exemplaire que vous recevez. Vos propres photos convertissent
   mieux de toute façon : un fond reconnaissable rassure plus qu'un packshot vu
   sur trente autres sites.

2. Remplacez ensuite les dessins SVG des pages par vos images, avec un attribut
   alt décrivant le produit, width et height déclarés, et loading="lazy" sur
   tout ce qui n'est pas visible au premier écran.
FIN
