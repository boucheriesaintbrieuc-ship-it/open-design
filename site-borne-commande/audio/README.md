# Fichier de récitation

Déposez ici le fichier audio, nommé `coran.mp3`. Le chemin attendu est
`audio/coran.mp3`, réglable dans `assets/config.js` sous `audio.fichier`.

## Ce qui marche

| Point | Valeur |
|---|---|
| Format | MP3 ou M4A (AAC). Pas de FLAC ni de WAV, trop lourds. |
| Poids | moins de 8 Mo. Au-delà, la page rame sur un téléphone en 4G. |
| Débit | 96 kbps en mono suffit pour une voix, et divise le poids par deux. |
| Durée | n'importe laquelle : la lecture reboucle toute seule. |

Pour alléger un fichier trop gros :

```bash
ffmpeg -i source.mp3 -ac 1 -b:a 96k audio/coran.mp3
```

## Le son ne démarrera pas tout seul au chargement

Chrome, Safari et Firefox bloquent la lecture automatique d'un son tant que le
visiteur n'a pas interagi avec la page. Ce n'est pas contournable, et les
contournements qui circulent (démarrer en muet puis monter le volume) sont
détectés et bloqués eux aussi.

Le site fait donc au plus près de ce qui est permis : il tente la lecture au
chargement, et si le navigateur refuse, il relance au premier clic du visiteur,
où qu'il clique. En pratique le son démarre dès qu'il touche la page.

## Deux points à régler avant de publier

Une récitation enregistrée appartient à son récitant et à son producteur. La
diffuser sur un site commercial demande une autorisation, sauf si
l'enregistrement est explicitement libre de droits. Vérifiez la licence de votre
fichier avant de le mettre en ligne.

Si vous pointez vers un fichier hébergé ailleurs plutôt que sur votre serveur,
l'adresse IP de chaque visiteur part chez cet hébergeur. Il faut alors le
mentionner dans `confidentialite.html`, qui affirme aujourd'hui qu'aucune
requête ne sort du site.
