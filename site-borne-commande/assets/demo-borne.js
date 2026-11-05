/* =========================================================================
   BORNE DE DÉMONSTRATION — Smash Avenue

   Borne de commande complète et jouable : veille, mode de consommation,
   carte, fiche produit avec options, panier, paiement simulé, ticket,
   retour à la veille. C'est la démonstration qu'on montre au restaurateur,
   donc elle tourne sur une vraie carte et de vrais prix, relevés sur les
   planches menu du client.

   LA TVA EST CALCULÉE POUR DE VRAI, parce que c'est précisément le point
   que les restaurateurs vérifient : 10 % sur place, 5,5 % à emporter. Une
   borne qui affiche le même total dans les deux cas se fait repérer en
   trente secondes.

   Aucun paiement réel n'a lieu : l'écran de paiement est une simulation,
   et il le dit.
   ========================================================================= */
(function () {
  "use strict";

  var racine = document.getElementById("borne-demo");
  if (!racine) return;

  /* ====================================================================
     LA CARTE
     Relevée sur les planches menu fournies par le client. Les libellés
     d'ingrédients sont repris tels quels ; là où la planche était
     illisible, le texte est volontairement court plutôt qu'inventé.
     ==================================================================== */
  var E = "img/menu/";

  function formule(sup) {           /* la formule menu des burgers */
    return { id: "f", nom: "Formule", type: "unique", requis: true, choix: [
      { id: "seul", nom: "Le burger seul", prix: 0 },
      { id: "menu", nom: "Menu : frite + boisson 33 cl", prix: 3.00 },
      { id: "menupd", nom: "Menu : frites patate douce + boisson", prix: 4.00 }
    ] };
  }
  var FRITE_CHOIX = { id: "fr", nom: "Votre frite", type: "unique", requis: true, choix: [
    { id: "crinkle", nom: "Frites crinkle", prix: 0 },
    { id: "douce", nom: "Frites patate douce", prix: 1.00 }
  ] };
  var SIDE_ASIA = { id: "sa", nom: "Votre side asiatique", type: "unique", requis: true, choix: [
    { id: "cd", nom: "Chicken dynamite", prix: 0 },
    { id: "crd", nom: "Crevette dynamite", prix: 0 },
    { id: "nem", nom: "Nems poulet", prix: 0 },
    { id: "yp", nom: "Yakitori poulet", prix: 0 },
    { id: "yb", nom: "Yakitori bœuf", prix: 0 },
    { id: "ct", nom: "Crevette tempura", prix: 0 }
  ] };

  var CARTE = [
    { id: "burgers", nom: "Smash burger", ic: "bacon-bomb", produits: [
      { id: "original-smash", nom: "Original Smash", prix: 6.90, ing: "1 steak smash, cheddar, salade, tomates, oignons, sauce smash", opts: [formule()] },
      { id: "double-smash", nom: "Double Smash", prix: 8.50, ing: "2 steaks smash, cheddar, salade, tomates, oignons rouges, sauce smash", opts: [formule()] },
      { id: "bacon-bomb", nom: "Bacon Bomb", prix: 8.90, ing: "2 steaks smash, cheddar, salade, tomates, oignons rouges, bacon, sauce creamy BBQ", opts: [formule()] },
      { id: "nash-smash", nom: "Nash’n Smash", prix: 8.50, ing: "2 steaks smash, cheddar, oignons rouges, salade, jalapeños, sauce Nashville", opts: [formule()] },
      { id: "chevre-miel", nom: "Chèvre Miel", prix: 8.90, ing: "2 steaks smash, chèvre, miel, oignons frits, noix, sauce maison", opts: [formule()] },
      { id: "smash-truffle", nom: "Smash Truffle", prix: 8.90, ing: "2 steaks smash, emmental, champignons, salade, oignon rouge, sauce creamy truffe", opts: [formule()] },
      { id: "melty-smash", nom: "Melty Smash", prix: 8.90, ing: "2 steaks smash, salade, lardons, oignons, sauce moutarde et poivre", opts: [formule()] },
      { id: "smash-mountain", nom: "Smash Mountain", prix: 9.90, ing: "2 steaks smash, raclette, rösti, bacon, oignons confits, sauce creamy pepper", opts: [formule()] },
      { id: "green-chicken", nom: "Green Chicken", prix: 9.00, ing: "Poulet frit, cheddar, salade, oignons rouges, guacamole, sauce verte", opts: [formule()] },
      { id: "nash-chicken", nom: "Nash’n Chicken", prix: 8.90, ing: "Poulet frit, cheddar, salade, oignons rouges, jalapeños, sauce Nashville", opts: [formule()] },
      { id: "smoky-chicken", nom: "Smoky Chicken", prix: 8.50, ing: "Poulet frit, cheddar, oignons rouges, bacon, sauce Nashville", opts: [formule()] },
      { id: "chicken-smash", nom: "Chicken Smash", prix: 7.90, ing: "Poulet frit, cheddar, salade, cornichons, sauce smash", opts: [formule()] }
    ] },

    { id: "box", nom: "Les box", ic: "good-deal", produits: [
      { id: "good-deal", nom: "Good Deal", prix: 16.90, ing: "1 Bacon Bomb, 1 Double Smash, 1 frite au choix, 1 boisson 33 cl", opts: [FRITE_CHOIX] },
      { id: "family", nom: "Family", prix: 29.90, ing: "3 smashs au choix, 3 frites au choix, 1 bouteille au choix", opts: [FRITE_CHOIX] },
      { id: "combo-fusion", nom: "Combo Fusion", prix: 14.90, ing: "1 smash au choix, 1 side asiatique au choix, 1 frite au choix, 1 boisson 33 cl", opts: [SIDE_ASIA, FRITE_CHOIX] },
      { id: "full-up", nom: "Full Up", prix: 14.90, ing: "1 smash au choix, 3 tenders, 1 frite, 1 boisson au choix", opts: [FRITE_CHOIX] },
      { id: "asian-box", nom: "Asian Box", prix: 15.90, ing: "1 bao au choix, 1 side asiatique au choix, 1 frite au choix, 1 boisson 33 cl", opts: [SIDE_ASIA, FRITE_CHOIX] }
    ] },

    { id: "salades", nom: "Salades", ic: "salade-cesar", produits: [
      { id: "salade-cesar", nom: "Salade César", prix: 8.90, ing: "Mélange patty (katsu), mélange de salade, tomates cerises, grana padano, croûtons ail, sauce césar", opts: [
        { id: "f", nom: "Formule", type: "unique", requis: true, choix: [
          { id: "seule", nom: "La salade seule", prix: 0 },
          { id: "menu", nom: "Menu : boisson 33 cl", prix: 1.00 } ] } ] },
      { id: "salade-fromagere", nom: "Salade Fromagère", prix: 8.00, ing: "Mélange patty (katsu), bacon, mélange de salade, tomates cerises, cornichons, emmental, féta, noix, croûtons ail, sauce fines herbes", opts: [
        { id: "f", nom: "Formule", type: "unique", requis: true, choix: [
          { id: "seule", nom: "La salade seule", prix: 0 },
          { id: "menu", nom: "Menu : boisson 33 cl", prix: 1.00 } ] } ] },
      { id: "salade-new-york", nom: "Salade New York", prix: 8.50, ing: "Mélange patty (katsu), bacon, mélange de salade, tomates cerises, cornichons, grana padano, croûtons ail, emmental, cheddar, oignons frits, sauce miel moutarde", opts: [
        { id: "f", nom: "Formule", type: "unique", requis: true, choix: [
          { id: "seule", nom: "La salade seule", prix: 0 },
          { id: "menu", nom: "Menu : boisson 33 cl", prix: 1.00 } ] } ] }
    ] },

    { id: "frites", nom: "Frites", ic: "frites-cheddar", produits: [
      { id: "frites-natures", nom: "Frites natures", prix: 3.00, ing: "Crinkle", opts: [
        { id: "s", nom: "Suppléments", type: "multi", choix: [
          { id: "jal", nom: "Jalapeño", prix: 1.00 }, { id: "oig", nom: "Oignon frit", prix: 1.00 } ] } ] },
      { id: "frites-patates-douces", nom: "Frites patates douces", prix: 3.50, ing: "", opts: [
        { id: "s", nom: "Suppléments", type: "multi", choix: [
          { id: "jal", nom: "Jalapeño", prix: 1.00 }, { id: "oig", nom: "Oignon frit", prix: 1.00 } ] } ] },
      { id: "frites-cheddar", nom: "Frites cheddar", prix: 4.00, ing: "Crinkle, sauce cheddar", opts: [
        { id: "s", nom: "Suppléments", type: "multi", choix: [
          { id: "jal", nom: "Jalapeño", prix: 1.00 }, { id: "oig", nom: "Oignon frit", prix: 1.00 } ] } ] },
      { id: "frites-cheddar-bacon", nom: "Frites cheddar bacon", prix: 5.50, ing: "Crinkle, sauce cheddar, bacon", opts: [
        { id: "s", nom: "Suppléments", type: "multi", choix: [
          { id: "jal", nom: "Jalapeño", prix: 1.00 }, { id: "oig", nom: "Oignon frit", prix: 1.00 } ] } ] }
    ] },

    { id: "sides", nom: "À côté", ic: "tenders", produits: [
      { id: "tenders", nom: "Tenders", prix: 5.90, ing: "", opts: [
        { id: "t", nom: "Quantité", type: "taille", requis: true, choix: [
          { id: "x3", nom: "× 3", prix: 5.90 }, { id: "x6", nom: "× 6", prix: 9.90 } ] } ] },
      { id: "wings", nom: "Wings", prix: 3.90, ing: "", opts: [
        { id: "t", nom: "Quantité", type: "taille", requis: true, choix: [
          { id: "x3", nom: "× 3", prix: 3.90 }, { id: "x6", nom: "× 6", prix: 6.90 } ] } ] },
      { id: "nuggets", nom: "Nuggets", prix: 3.90, ing: "", opts: [
        { id: "t", nom: "Quantité", type: "taille", requis: true, choix: [
          { id: "x5", nom: "× 5", prix: 3.90 }, { id: "x10", nom: "× 10", prix: 6.90 } ] } ] },
      { id: "mozza-stick", nom: "Mozza stick", prix: 3.90, ing: "", opts: [
        { id: "t", nom: "Quantité", type: "taille", requis: true, choix: [
          { id: "x3", nom: "× 3", prix: 3.90 }, { id: "x6", nom: "× 6", prix: 6.90 } ] } ] }
    ] },

    { id: "asiatique", nom: "Asiatique", ic: "chicken-dynamite", produits: [
      { id: "chicken-dynamite", nom: "Chicken Dynamite", prix: 5.90, ing: "", opts: [] },
      { id: "crevette-dynamite", nom: "Crevette Dynamite", prix: 5.90, ing: "", opts: [] },
      { id: "nem-poulet", nom: "Nems poulet", prix: 5.00, ing: "", opts: [
        { id: "t", nom: "Quantité", type: "taille", requis: true, choix: [
          { id: "x3", nom: "× 3", prix: 5.00 }, { id: "x6", nom: "× 6", prix: 9.00 } ] } ] },
      { id: "yakitori-poulet", nom: "Yakitori poulet", prix: 5.90, ing: "× 2", opts: [] },
      { id: "yakitori-boeuf", nom: "Yakitori bœuf", prix: 5.90, ing: "× 3", opts: [] },
      { id: "crevette-tempura", nom: "Crevette tempura", prix: 5.90, ing: "× 3", opts: [] }
    ] },

    { id: "menus", nom: "Menus", ic: "menu-enfant", produits: [
      { id: "menu-enfant", nom: "Menu Enfant", prix: 6.90, ing: "1 frite, boisson et cadeau compris", opts: [
        { id: "p", nom: "Le plat", type: "unique", requis: true, choix: [
          { id: "little", nom: "Little Smash", prix: 0 }, { id: "nug", nom: "5 nuggets", prix: 0 } ] },
        { id: "b", nom: "La boisson", type: "unique", requis: true, choix: [
          { id: "capri", nom: "Capri-Sun", prix: 0 }, { id: "eau", nom: "Eau", prix: 0 } ] } ] },
      { id: "menu-etudiant", nom: "Menu Étudiant", prix: 6.90, ing: "Original Smash, 1 frite, 1 boisson", opts: [FRITE_CHOIX] }
    ] },

    { id: "desserts", nom: "Desserts", ic: "milkshake", produits: [
      { id: "tiramisu", nom: "Tiramisu", prix: 3.90, ing: "", opts: [
        { id: "p", nom: "Le parfum", type: "unique", requis: true, choix: [
          { id: "pis", nom: "Pistache", prix: 0 }, { id: "oreo", nom: "Oréo", prix: 0 },
          { id: "man", nom: "Mangue", prix: 0 }, { id: "fra", nom: "Fraise", prix: 0 },
          { id: "nut", nom: "Nutella", prix: 0 }, { id: "car", nom: "Caramel", prix: 0 },
          { id: "pb", nom: "Paris-Brest", prix: 0 } ] } ] },
      { id: "bubble-waffle", nom: "Bubble Waffle", prix: 5.00, ing: "", opts: [
        { id: "b", nom: "La base", type: "unique", requis: true, choix: [
          { id: "nut", nom: "Nutella", prix: 0 }, { id: "cb", nom: "Chocolat blanc", prix: 0 },
          { id: "bue", nom: "Bueno", prix: 0 }, { id: "fr", nom: "Fruits rouges", prix: 0 },
          { id: "spe", nom: "Spéculos", prix: 0 } ] },
        { id: "t", nom: "Topping", type: "multi", choix: [
          { id: "kb", nom: "Kinder Bueno", prix: 1.00 }, { id: "kc", nom: "Kinder Country", prix: 1.00 },
          { id: "spe", nom: "Spéculos", prix: 1.00 }, { id: "oreo", nom: "Oréo", prix: 1.00 },
          { id: "sni", nom: "Snickers", prix: 1.00 }, { id: "ban", nom: "Banane", prix: 1.00 },
          { id: "fra", nom: "Fraise", prix: 1.00 } ] },
        { id: "g", nom: "Glace et coulis", type: "multi", choix: [
          { id: "gv", nom: "Glace vanille", prix: 0.50 }, { id: "gf", nom: "Glace fraise", prix: 0.50 },
          { id: "cc", nom: "Coulis caramel", prix: 0.50 }, { id: "cfr", nom: "Coulis fruits rouges", prix: 0.50 },
          { id: "cch", nom: "Coulis chocolat", prix: 0.50 }, { id: "cha", nom: "Chantilly", prix: 0.50 } ] } ] },
      { id: "milkshake", nom: "Milkshake", prix: 5.90, ing: "", opts: [
        { id: "p", nom: "Le parfum", type: "unique", requis: true, choix: [
          { id: "van", nom: "Vanille", prix: 0 }, { id: "fra", nom: "Fraise", prix: 0 },
          { id: "coco", nom: "Coco-ananas", prix: 0 }, { id: "oreo", nom: "Oréo", prix: 0 },
          { id: "kb", nom: "Kinder Bueno", prix: 0 }, { id: "fr", nom: "Fruits rouges", prix: 0 },
          { id: "cho", nom: "Chocolat", prix: 0 } ] } ] }
    ] }
  ];

  /* ==================================================================== */
  var $  = function (s, r) { return (r || racine).querySelector(s); };
  var $$ = function (s, r) { return [].slice.call((r || racine).querySelectorAll(s)); };
  var eur = function (n) { return n.toFixed(2).replace(".", ",") + " €"; };

  var etat = {
    mode: null,          /* "place" | "emporter" */
    panier: [],
    cat: "burgers",
    prod: null,
    choix: {},
    qte: 1,
    numero: 213
  };

  /* La TVA d'un ticket de restauration rapide : 10 % sur place, 5,5 % à
     emporter. C'est le premier calcul qu'un restaurateur vérifie. */
  function taux() { return etat.mode === "emporter" ? 0.055 : 0.10; }

  function ecran(nom) {
    $$(".ecran").forEach(function (e) { e.removeAttribute("data-actif"); });
    var c = $('[data-ecran="' + nom + '"]');
    if (c) c.setAttribute("data-actif", "");
    var def = $(".ecran[data-actif] [data-focus]");
    if (def) def.focus({ preventScroll: true });
    repousserVeille();
  }

  /* ---- Veille automatique ---------------------------------------------
     Une borne laissée sur un panier à moitié rempli bloque la suivante.
     Au bout de soixante secondes sans geste, tout repart à zéro. */
  var minuteur = null;
  function repousserVeille() {
    clearTimeout(minuteur);
    if ($('[data-ecran="veille"][data-actif]')) return;
    minuteur = setTimeout(reinitialiser, 60000);
  }
  racine.addEventListener("pointerdown", repousserVeille);

  function reinitialiser() {
    etat.mode = null; etat.panier = []; etat.cat = "burgers";
    etat.prod = null; etat.choix = {}; etat.qte = 1;
    majPastille();
    ecran("veille");
  }

  /* ---- Carte ----------------------------------------------------------- */
  function rendreRail() {
    $("#k-rail").innerHTML = CARTE.map(function (c) {
      return '<button type="button" role="tab" data-cat="' + c.id + '" aria-selected="' +
        (c.id === etat.cat) + '"><img src="' + E + c.ic + '.webp" alt="" loading="lazy" decoding="async">' +
        c.nom + "</button>";
    }).join("");
  }

  function rendreGrille() {
    var c = CARTE.filter(function (x) { return x.id === etat.cat; })[0];
    $("#k-titre").textContent = c.nom;
    $("#k-produits").innerHTML = c.produits.map(function (p, i) {
      return '<button type="button" class="pk" data-prod="' + p.id + '" style="animation-delay:' +
        (i * 28) + 'ms">' +
        '<img src="' + E + p.id + '.webp" alt="" loading="lazy" decoding="async">' +
        '<span class="pk__txt">' +
          '<span class="pk__nom">' + p.nom + "</span>" +
          (p.ing ? '<span class="pk__ing">' + p.ing + "</span>" : "") +
          '<span class="pk__prix">' + eur(p.prix) + "</span>" +
        "</span></button>";
    }).join("");
  }

  function trouver(id) {
    for (var i = 0; i < CARTE.length; i++) {
      var t = CARTE[i].produits.filter(function (p) { return p.id === id; });
      if (t.length) return t[0];
    }
    return null;
  }

  /* ---- Fiche produit ---------------------------------------------------- */
  function ouvrirFiche(id) {
    var p = trouver(id);
    if (!p) return;
    etat.prod = p; etat.qte = 1; etat.choix = {};
    /* Un groupe obligatoire part sur son premier choix : une borne qui
       exige une sélection sans en proposer une par défaut fait reculer. */
    p.opts.forEach(function (g) {
      if (g.requis && (g.type === "unique" || g.type === "taille")) etat.choix[g.id] = [g.choix[0].id];
      else etat.choix[g.id] = [];
    });

    $("#f-photo").src = E + p.id + ".webp";
    $("#f-photo").alt = p.nom;
    $("#f-photo").parentNode.style.backgroundImage = 'url("' + E + p.id + '.webp")';
    $("#f-nom").textContent = p.nom;
    $("#f-ing").textContent = p.ing || "";
    $("#f-ing").hidden = !p.ing;

    $("#f-groupes").innerHTML = p.opts.map(function (g) {
      return '<div class="groupe" data-groupe="' + g.id + '">' +
        '<div class="groupe__tete"><h4>' + g.nom + "</h4><span>" +
          (g.type === "multi" ? "Plusieurs possibles" : "Un seul choix") + "</span></div>" +
        '<div class="opts">' + g.choix.map(function (ch) {
          return '<button type="button" class="opt" data-type="' + g.type + '" data-g="' + g.id + '" data-c="' + ch.id + '" aria-pressed="false">' +
            '<span class="opt__coche"><svg viewBox="0 0 24 24" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round" d="M4 12.5l5 5L20 6.5"/></svg></span>' +
            '<span class="opt__nom">' + ch.nom + "</span>" +
            '<span class="opt__prix">' + (g.type === "taille" ? eur(ch.prix) : (ch.prix ? "+ " + eur(ch.prix) : "Inclus")) + "</span>" +
          "</button>";
        }).join("") + "</div></div>";
    }).join("");

    majFiche();
    ecran("fiche");
  }

  function prixUnite() {
    var p = etat.prod, base = p.prix, sup = 0;
    p.opts.forEach(function (g) {
      (etat.choix[g.id] || []).forEach(function (cid) {
        var ch = g.choix.filter(function (c) { return c.id === cid; })[0];
        if (!ch) return;
        if (g.type === "taille") base = ch.prix; else sup += ch.prix;
      });
    });
    return base + sup;
  }

  function majFiche() {
    $$(".opt").forEach(function (b) {
      var sel = (etat.choix[b.dataset.g] || []).indexOf(b.dataset.c) >= 0;
      b.setAttribute("aria-pressed", sel ? "true" : "false");
    });
    $("#f-prix").textContent = eur(prixUnite());
    $("#f-qte").textContent = etat.qte;
    $("#f-ajouter").textContent = "Ajouter · " + eur(prixUnite() * etat.qte);
  }

  function libelleChoix() {
    var out = [];
    etat.prod.opts.forEach(function (g) {
      (etat.choix[g.id] || []).forEach(function (cid) {
        var ch = g.choix.filter(function (c) { return c.id === cid; })[0];
        if (ch && !(g.type === "unique" && ch.prix === 0 && /seul/.test(ch.id))) out.push(ch.nom);
      });
    });
    return out.join(" · ");
  }

  /* ---- Panier ------------------------------------------------------------ */
  function ajouter() {
    etat.panier.push({
      id: etat.prod.id, nom: etat.prod.nom, det: libelleChoix(),
      pu: prixUnite(), qte: etat.qte
    });
    majPastille(true);
    ecran("carte");
  }

  function majPastille(anime) {
    var n = etat.panier.reduce(function (s, l) { return s + l.qte; }, 0);
    var tot = etat.panier.reduce(function (s, l) { return s + l.pu * l.qte; }, 0);
    $("#k-nb").textContent = n;
    $("#k-total").textContent = eur(tot);
    $("#k-voir").disabled = n === 0;
    if (anime) {
      var b = $("#k-nb");
      b.classList.remove("saute"); void b.offsetWidth; b.classList.add("saute");
    }
  }

  function rendrePanier() {
    var tot = etat.panier.reduce(function (s, l) { return s + l.pu * l.qte; }, 0);
    $("#p-lignes").innerHTML = etat.panier.map(function (l, i) {
      return '<div class="lk">' +
        '<img src="' + E + l.id + '.webp" alt="" loading="lazy">' +
        "<div><div class=\"lk__nom\">" + l.nom + "</div>" +
        (l.det ? '<div class="lk__det">' + l.det + "</div>" : "") +
        '<div class="qte" style="margin-top:.4em">' +
          '<button type="button" data-ligne="' + i + '" data-d="-1" aria-label="Retirer un">−</button>' +
          "<output>" + l.qte + "</output>" +
          '<button type="button" data-ligne="' + i + '" data-d="1" aria-label="Ajouter un">+</button>' +
        "</div></div>" +
        '<div class="lk__prix">' + eur(l.pu * l.qte) + "</div></div>";
    }).join("");

    var ht = tot / (1 + taux());
    $("#p-ht").textContent = eur(ht);
    $("#p-tva").textContent = eur(tot - ht);
    $("#p-tauxl").textContent = "TVA " + (taux() * 100).toFixed(1).replace(".0", "").replace(".", ",") + " %" +
      (etat.mode === "emporter" ? " (à emporter)" : " (sur place)");
    $("#p-total").textContent = eur(tot);
    $("#p-payer").disabled = etat.panier.length === 0;
  }

  /* ---- Paiement et ticket ------------------------------------------------ */
  function payer() {
    var tot = etat.panier.reduce(function (s, l) { return s + l.pu * l.qte; }, 0);
    $("#paie-montant").textContent = eur(tot);
    ecran("paiement");
    var barre = $("#paie-barre");
    barre.classList.remove("court"); void barre.offsetWidth; barre.classList.add("court");
    setTimeout(terminer, 2800);
  }

  function terminer() {
    if (!$('[data-ecran="paiement"][data-actif]')) return;   /* annulé entre-temps */
    var tot = etat.panier.reduce(function (s, l) { return s + l.pu * l.qte; }, 0);
    var ht = tot / (1 + taux());
    etat.numero += 1;
    $("#t-num").textContent = "B-" + etat.numero;
    $("#t-mode").textContent = etat.mode === "emporter" ? "À emporter" : "Sur place";
    $("#t-lignes").innerHTML = etat.panier.map(function (l) {
      return '<div class="recu-k__l"><span>' + l.qte + " × " + l.nom + "</span><span>" + eur(l.pu * l.qte) + "</span></div>";
    }).join("") +
      '<div class="recu-k__l"><span>dont TVA ' + (taux() * 100).toFixed(1).replace(".0", "").replace(".", ",") +
      " %</span><span>" + eur(tot - ht) + "</span></div>";
    $("#t-total").textContent = eur(tot);
    ecran("ticket");

    var reste = 9;
    $("#t-compte").textContent = "Nouvelle commande dans " + reste + " s";
    var tic = setInterval(function () {
      reste -= 1;
      if (!$('[data-ecran="ticket"][data-actif]')) { clearInterval(tic); return; }
      if (reste <= 0) { clearInterval(tic); reinitialiser(); return; }
      $("#t-compte").textContent = "Nouvelle commande dans " + reste + " s";
    }, 1000);
  }

  /* ---- Branchements ------------------------------------------------------ */
  racine.addEventListener("click", function (ev) {
    var t = ev.target.closest("button, [data-aller]");
    if (!t || !racine.contains(t)) return;

    if (t.dataset.aller) {
      if (t.dataset.aller === "carte" && !etat.mode) { ecran("mode"); return; }
      if (t.dataset.aller === "panier") rendrePanier();
      ecran(t.dataset.aller);
      return;
    }
    if (t.dataset.mode) {
      etat.mode = t.dataset.mode;
      $("#k-mode").textContent = etat.mode === "emporter" ? "À emporter" : "Sur place";
      $("#k-mode2").textContent = $("#k-mode").textContent;
      rendreRail(); rendreGrille(); majPastille();
      ecran("carte");
      return;
    }
    if (t.dataset.cat) { etat.cat = t.dataset.cat; rendreRail(); rendreGrille(); return; }
    if (t.dataset.prod) { ouvrirFiche(t.dataset.prod); return; }

    if (t.dataset.g) {
      var g = etat.prod.opts.filter(function (x) { return x.id === t.dataset.g; })[0];
      var sel = etat.choix[g.id] || [];
      if (g.type === "multi") {
        var i = sel.indexOf(t.dataset.c);
        if (i >= 0) sel.splice(i, 1); else sel.push(t.dataset.c);
      } else {
        etat.choix[g.id] = [t.dataset.c];
      }
      majFiche();
      return;
    }
    if (t.dataset.q) { etat.qte = Math.min(20, Math.max(1, etat.qte + (+t.dataset.q))); majFiche(); return; }
    if (t.id === "f-ajouter") { ajouter(); return; }

    if (t.dataset.ligne !== undefined) {
      var l = etat.panier[+t.dataset.ligne];
      l.qte += (+t.dataset.d);
      if (l.qte <= 0) etat.panier.splice(+t.dataset.ligne, 1);
      majPastille(); rendrePanier();
      return;
    }
    if (t.id === "p-payer") { payer(); return; }
    if (t.id === "t-fin") { reinitialiser(); return; }
    if (t.id === "k-plein") {
      if (document.fullscreenElement) document.exitFullscreen();
      else if (racine.requestFullscreen) racine.requestFullscreen();
      return;
    }
  });

  /* Images de veille : trois produits qui dérivent, décalés dans le temps. */
  var veilleFond = $("#veille-fond");
  if (veilleFond) {
    ["bacon-bomb", "frites-cheddar", "milkshake", "chicken-dynamite"].forEach(function (id, i) {
      var im = new Image();
      im.src = E + id + ".webp"; im.alt = ""; im.loading = "lazy";
      im.style.left = [4, 33, 60, 78][i] + "cqw";
      im.style.animationDelay = (i * 5.5) + "s";
      veilleFond.appendChild(im);
    });
  }

  rendreRail(); rendreGrille(); majPastille();
  ecran("veille");
})();
