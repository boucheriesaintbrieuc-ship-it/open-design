# Landing « borne de commande restaurant » — 3 directions artistiques

Trois pages complètes, **même produit, même argumentaire, même prix**, pour que la
comparaison porte uniquement sur la direction artistique et la mécanique de conversion.
Chacune est un `index.html` autonome : aucun CDN, aucune police tierce, aucune requête
réseau sortante. Prêt à déposer en FTP.

| | Direction | Signature | À qui la donner |
|---|---|---|---|
| **A** | `option-a-comptoir/` — *Le comptoir* | Une **borne réellement fonctionnelle** dans le hero : menu → suppléments → sur place / à emporter → ticket imprimé | Fast-food, kebab, burger. Le patron doit *toucher* le produit avant de comprendre. |
| **B** | `option-b-fiche-technique/` — *Le dossier technique* | Un **schéma coté SVG** (vue de face + profil, cotes en mm) et un comparatif borne / QR code / caisse / plateforme | Multi-sites, gérant qui compare trois devis, franchise. Décision rationnelle, documentée. |
| **C** | `option-c-service-du-soir/` — *Le calculateur* | Un **calculateur à 4 curseurs** en haut de page qui pilote toute la page, hypothèses affichées, résultat négatif assumé | Patron qui raisonne en ROI et se méfie des commerciaux. Le plus fort en conversion à froid. |

---

## Les tokens de chaque direction

### A — Le comptoir
```
Palette   kraft #EDE7DC (papier ticket) · encre #16150F · inox #C9C7C0
          vert #0F6B3A = validation, paiement, CTA — nulle part ailleurs
          orange #A32E06 = la file d'attente — uniquement dans la section « problème »
Typo      display condensé (Haettenschweiler / Arial Narrow / Impact) = le panneau
          de menu au-dessus du comptoir ; mono pour tous les prix
Grille    bandes horizontales pleine largeur, comme les panneaux d'un menu board
Densité   compacte en haut, aérée dans la preuve
Motion    le total qui s'incrémente, le survol franc sur les items. Rien d'autre.
Signature la borne jouable dans le hero, et le ticket qui s'imprime à la fin
```
La page va **de l'orange au vert** : le problème est orange, tout ce qui suit est vert.
C'est la règle d'usage de la couleur, pas une décoration.

### B — Le dossier technique
```
Palette   papier #FFF · fond de plan #EDF1F5 · encre #0B0F14
          bleu de plan #1B4F9C = légendes et structure
          orange #BE3806 = cotes et valeurs qui tranchent — nulle part ailleurs
Typo      grotesque neutre + mono sur toutes les données, surtitres « §1 » en mono
Grille    dossier : colonne de légende en marge gauche, corps à droite, figures numérotées
Densité   haute, tableaux partout — le lecteur est un acheteur qui compare
Motion    aucune, sauf accordéon et focus. Un document ne bouge pas.
Signature Fig. 01 : la borne cotée en mm, vue de face et de profil, repères 1-5
```

### C — Le service du soir
```
Palette   nuit #0C0C0A · texte #F5F2E9
          ambre #FFB020 = les chiffres qui montent (l'écran de cuisine allumé)
          braise #FF4A1C = les chiffres qu'on perd
Typo      mono pour tous les chiffres et surtitres, chiffres géants comme matériau graphique
Grille    colonne de lecture étroite (40 rem) interrompue par des blocs pleine largeur
Densité   très aérée, écarts de corps énormes
Motion    les jauges de ticket moyen qui se déplacent. Rien d'autre.
Signature le calculateur : 4 curseurs qui recalculent la page, hypothèses exposées
```

---

## Contrôle avant livraison — résultats réels

| Test | A | B | C |
|---|---|---|---|
| Requêtes réseau externes | 0 | 0 | 0 |
| Débordement horizontal à 375 / 768 / 1440 px | aucun | aucun | aucun |
| Contraste texte/fond ≥ 4.5:1 (3:1 gros texte) | 0 défaut | 0 défaut | 0 défaut |
| Erreurs JS console | aucune | aucune | aucune |
| JSON-LD (parsing) | valide | valide | valide |
| `prefers-reduced-motion` | oui | oui | oui |
| `:focus-visible` stylé | oui | oui | oui |
| Cible tactile ≥ 44 px | oui | oui | oui |
| Liens `#` orphelins | aucun | aucun | aucun |
| Poids du fichier | 44 ko | 48 ko | 36 ko |

Les seules URL restant dans les fichiers sont : `schema.org` (identifiants JSON-LD, jamais
téléchargés), `w3.org/2000/svg` (espace de noms XML), et le domaine du site lui-même.
**Aucune n'est une requête réseau.**

Tests non faits ici, à faire côté client : rendu sur iOS/Android réels, rendu sur Windows
(la police condensée de l'option A tombe sur Impact puis sur la grotesque système —
vérifié en rendu grotesque, la mise en page tient), lecteur d'écran.

---

## Ce qui reste à fournir avant mise en ligne

**Bloquant — la page ment tant que ce n'est pas fait :**
1. **Identité réelle** : « Ardoise », « ardoise-bornes.fr » et le `02 96 00 00 00` sont des
   valeurs de remplacement. À remplacer partout (y compris dans le JSON-LD et les `tel:`).
2. **Prix** : 1 690 € HT / 69 € HT par mois / 390 € HT d'installation / −15 % sur la 2ᵉ borne
   sont vraisemblables mais inventés. À confirmer ou corriger.
3. **Spécifications matérielles** : 21,5″, 350 cd/m², 24 kg, 1 400 × 420 × 380 mm, Android 13 —
   à recaler sur le matériel réellement revendu. Le schéma coté de l'option B doit suivre.
4. **Liste des caisses compatibles** : Zelty, L'Addition, Tiller, Popina, Lightspeed, Cashpad,
   JDC. Toute ligne non vérifiée doit être retirée, pas laissée « au cas où ».
5. **Mentions légales** (`/mentions-legales.html`) et **CGV** (`/cgv.html`) : les deux pages
   sont liées depuis les trois pieds de page mais **n'existent pas**. Obligatoires
   (art. 6-III LCEN). Prévoir : dénomination, forme juridique, capital, siège, RCS/SIREN,
   TVA intracommunautaire, directeur de publication, et l'hébergeur —
   *SAS o2switch, 222-224 boulevard Gustave Flaubert, 63000 Clermont-Ferrand*.

**Non bloquant mais visible :**
6. **Avis clients** : les emplacements sont volontairement laissés vides et visiblement
   provisoires. Un avis fabriqué est une pratique commerciale trompeuse (art. L121-2
   c. conso.). À remplir avec des références vérifiables, ou à supprimer.
7. **Photos** : aucune photo n'est utilisée (tout est SVG/CSS). Prévoir au minimum
   une borne installée en situation, 1 200 px de large, et l'image Open Graph
   `/img/og.jpg` en 1200 × 630.
8. **Formulaire** : sans serveur, il ouvre la messagerie du visiteur (`mailto:`) avec les
   champs pré-remplis, et affiche toujours téléphone + e-mail en secours. Pour un vrai
   envoi, brancher un traitement côté serveur ou un service de formulaire — dans ce cas,
   la mention RGPD doit nommer ce prestataire.
9. **Affirmation « hausse du ticket moyen »** : l'option C laisse le visiteur régler ce
   curseur lui-même, donc rien n'est affirmé. Si vous préférez annoncer un chiffre,
   il faut pouvoir le justifier auprès de la DGCCRF.

---

## Mise en ligne sur o2switch

```
1. Choisir un dossier, renommer son index.html si besoin, l'envoyer en FTP
   dans public_html/ (ou le sous-dossier du domaine additionnel).
2. Permissions : 644 sur le fichier, 755 sur les dossiers.
3. Purger le cache LiteSpeed depuis cPanel après chaque remplacement.
```
En cas d'erreur 403 après l'upload, vérifier le propriétaire du fichier côté FTP.

Si le site remplace un site existant : prévoir les redirections 301 des anciennes URL,
sinon le référencement acquis est perdu.
