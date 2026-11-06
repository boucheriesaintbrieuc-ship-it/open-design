/* =========================================================================
   LA BORNE EN 360° — construction et manipulation

   Le modèle est assemblé ici plutôt qu'écrit dans le HTML : une colonne de
   quatorze facettes et un socle de vingt-deux, c'est trente-six éléments
   qu'il serait absurde de taper à la main et impossible de relire.

   Manipulation : le doigt entraîne l'objet au ratio 1:1, la vitesse de
   relâchement est reprise telle quelle par l'inertie, et l'inclinaison
   résiste de plus en plus près de ses bornes au lieu de buter net. On peut
   rattraper l'objet en plein vol, ce qui est tout l'intérêt : une
   animation qu'on ne peut pas interrompre n'est pas une manipulation.
   ========================================================================= */
(function () {
  "use strict";

  var hote = document.querySelector("[data-v360]");
  if (!hote) return;

  var menage = matchMedia("(prefers-reduced-motion: reduce)");

  /* ---- Géométrie du modèle, en pixels de maquette ---------------------
     Montage relevé sur les photos du produit : la colonne passe DERRIÈRE
     l'écran et monte jusqu'à son centre, où une rotule le tient. C'est ce
     qui permet au basculement portrait / paysage de se faire sans que
     l'écran quitte son support : il tourne autour de son propre centre,
     pas autour d'un point situé sous lui. */
  var SOCLE_R = 76, SOCLE_H = 12;
  var MAT_R = 7.5, MAT_H = 200;
  var ROTULE_R = 16;
  var EC_L = 196, EC_H = 280, EC_E = 13;     /* écran : largeur, hauteur, épaisseur */
  var N_MAT = 14, N_SOCLE = 22;
  var MAT_Z = -(EC_E / 2 + 9);               /* la colonne, derrière le plan de l'écran */

  var objet = hote.querySelector(".v360__objet");
  if (!objet) return;

  var H = SOCLE_H + MAT_H + EC_H / 2;
  var C = H / 2;

  /* Chaque facette garde son angle de naissance : l'éclairage en a besoin
     à chaque trame pour savoir où elle regarde une fois l'objet tourné. */
  var facettes = [];

  function cylindre(parent, rayon, hauteur, n, y, teinte, z) {
    var pas = 360 / n;
    var larg = 2 * Math.PI * rayon / n * 1.06;     /* léger recouvrement */
    var dz = z || 0;
    for (var i = 0; i < n; i++) {
      var a = i * pas;
      var f = document.createElement("span");
      f.className = "f";
      f.style.width = larg.toFixed(2) + "px";
      f.style.height = hauteur + "px";
      f.style.marginLeft = (-larg / 2).toFixed(2) + "px";
      f.style.marginTop = (C - y - hauteur).toFixed(1) + "px";
      f.style.transform = "translateZ(" + dz + "px) rotateY(" + a + "deg) translateZ(" + rayon.toFixed(2) + "px)";
      parent.appendChild(f);
      facettes.push({ el: f, a: a, teinte: teinte });
    }
    /* Le disque du dessus ferme le volume : sans lui on voit l'intérieur.
       Il ne reçoit QUE la rotation : un translateY posé avant le rotateX
       déplacerait le disque le long d'un axe déjà tourné. */
    var d = document.createElement("span");
    d.className = "f";
    d.style.width = (rayon * 2) + "px";
    d.style.height = (rayon * 2) + "px";
    d.style.marginLeft = -rayon + "px";
    d.style.marginTop = (C - y - hauteur - rayon).toFixed(1) + "px";
    d.style.borderRadius = "50%";
    d.style.background = teinte.haut;
    d.style.transform = "translateZ(" + dz + "px) rotateX(90deg)";
    parent.appendChild(d);
  }

  var BLANC = { base: [233, 229, 238], haut: "#EFECF4" };
  var METAL = { base: [196, 190, 205], haut: "#D8D3E0" };

  cylindre(objet, SOCLE_R, SOCLE_H, N_SOCLE, 0, BLANC, 0);
  cylindre(objet, MAT_R, MAT_H, N_MAT, SOCLE_H, METAL, MAT_Z);

  /* ---- L'écran, tenu par sa rotule ------------------------------------ */
  var tete = document.createElement("span");
  tete.className = "p";
  tete.style.marginTop = (C - (SOCLE_H + MAT_H)).toFixed(1) + "px";
  objet.appendChild(tete);

  var pivot = document.createElement("span");
  pivot.className = "p";
  tete.appendChild(pivot);

  function face(parent, l, h, transform, fond, classe) {
    var f = document.createElement("span");
    f.className = "f" + (classe ? " " + classe : "");
    f.style.width = l + "px";
    f.style.height = h + "px";
    f.style.marginLeft = (-l / 2) + "px";
    f.style.marginTop = (-h / 2) + "px";
    f.style.transform = transform;
    if (fond) f.style.background = fond;
    parent.appendChild(f);
    return f;
  }

  /* L'avant : la dalle. L'arrière et les tranches : la coque blanche. */
  var avant = face(pivot, EC_L, EC_H, "translateZ(" + (EC_E / 2) + "px)", "", "v360__dalle");
  avant.style.borderRadius = "10px";
  avant.innerHTML =
    '<span class="v360__objectif"></span>' +
    "<b>SMASH<i>Avenue</i></b>" +
    "<span>Commandez ici</span>";

  var arriere = face(pivot, EC_L, EC_H, "rotateY(180deg) translateZ(" + (EC_E / 2) + "px)", "#E9E5EE");
  arriere.style.borderRadius = "10px";
  facettes.push({ el: arriere, a: 180, teinte: BLANC });

  var tr = [
    [EC_E, EC_H, "rotateY(90deg)  translateZ(" + (EC_L / 2) + "px)", 90],
    [EC_E, EC_H, "rotateY(-90deg) translateZ(" + (EC_L / 2) + "px)", 270],
    [EC_L, EC_E, "rotateX(90deg)  translateZ(" + (EC_H / 2) + "px)", 0],
    [EC_L, EC_E, "rotateX(-90deg) translateZ(" + (EC_H / 2) + "px)", 0]
  ];
  for (var t = 0; t < tr.length; t++) {
    var e = face(pivot, tr[t][0], tr[t][1], tr[t][2], "#DCD7E3");
    if (t < 2) facettes.push({ el: e, a: tr[t][3], teinte: BLANC });
  }

  /* La rotule : un disque plaqué au dos de l'écran, à l'aplomb de la
     colonne. Elle ne tourne PAS avec le pivot, puisque c'est la pièce
     fixe sur laquelle l'écran pivote : elle reste donc sur « tete ». */
  var rotule = face(tete, ROTULE_R * 2, ROTULE_R * 2,
                    "rotateY(180deg) translateZ(" + (EC_E / 2 + 2) + "px)", "#C9C3D2");
  rotule.style.borderRadius = "50%";
  rotule.style.boxShadow = "inset 0 0 0 3px #AFA7BC, 0 0 10px rgb(0 0 0 / .5)";

  /* L'ombre est posée au sol, sous la base. */
  var ombre = hote.querySelector(".v360__ombre");
  if (ombre) ombre.style.marginTop = (C - 22).toFixed(1) + "px";

  /* ---- Éclairage ------------------------------------------------------
     Une seule source, placée en haut à gauche de la scène. Chaque facette
     lit son angle dans le monde et en déduit sa clarté. */
  var LUMIERE = -35;
  function eclairer(tour) {
    for (var i = 0; i < facettes.length; i++) {
      var f = facettes[i];
      var a = (f.a + tour - LUMIERE) * Math.PI / 180;
      var k = 0.42 + 0.58 * Math.max(0, Math.cos(a));
      var c = f.teinte.base;
      f.el.style.background = "rgb(" +
        Math.round(c[0] * k) + "," + Math.round(c[1] * k) + "," + Math.round(c[2] * k) + ")";
    }
  }

  /* ---- État et rendu --------------------------------------------------- */
  var tour = -22, pente = -8, pivotZ = 0, ciblePivot = 0;
  var vTour = 0, vPente = 0, vPivot = 0;
  var PENTE_MIN = -26, PENTE_MAX = 18;
  var auto = !menage.matches, touche = false, boucle = null, vu = true, dernier = 0;

  function caoutchouc(depassement, course) {
    var k = 0.55;
    return (depassement * course * k) / (course + k * Math.abs(depassement));
  }

  function borner(p) {
    if (p < PENTE_MIN) return PENTE_MIN + caoutchouc(p - PENTE_MIN, 90);
    if (p > PENTE_MAX) return PENTE_MAX + caoutchouc(p - PENTE_MAX, 90);
    return p;
  }

  var echelle = 1;
  function rendre() {
    objet.style.transform =
      "scale(" + echelle.toFixed(3) + ") rotateX(" + pente.toFixed(2) + "deg)" +
      " rotateY(" + tour.toFixed(2) + "deg)";
    pivot.style.transform = "rotateZ(" + pivotZ.toFixed(2) + "deg)";
    eclairer(tour);
  }

  /* Le modèle est dessiné en pixels de maquette ; on l'ajuste au cadre
     plutôt que de recalculer toute la géométrie. */
  function ajuster() {
    /* On mesure la hauteur UTILE, dégagement de la barre déduit : calculée
       sur la boîte entière, l'échelle faisait dépasser le socle sous les
       boutons en écran étroit. */
    var cadre = hote.querySelector(".v360__cadre");
    var util = cadre.clientHeight - parseFloat(getComputedStyle(cadre).paddingBottom || 0);
    echelle = Math.min(1, (util * 0.94) / H);
    rendre();
  }

  /* ---- Ressort du pivot écran (portrait / paysage) ---------------------
     Amortissement critique, réponse 0,4 s : la bascule ne doit pas rebondir,
     c'est une pièce mécanique, pas un objet lancé. */
  var W = 2 * Math.PI / 0.4;

  function trame(t) {
    var dt = Math.min(0.033, (t - dernier) / 1000) || 0.016;
    dernier = t;
    var bouge = false;

    if (auto && !touche) { tour += 14 * dt; bouge = true; }

    if (!touche) {
      /* Inertie du tour : décroissance exponentielle, comme une roue libre. */
      if (Math.abs(vTour) > 0.4) {
        tour += vTour * dt;
        vTour *= Math.pow(0.12, dt);
        bouge = true;
      } else { vTour = 0; }

      /* La pente revient dans ses bornes au ressort. */
      var cible = Math.max(PENTE_MIN, Math.min(PENTE_MAX, pente));
      if (Math.abs(pente - cible) > 0.01 || Math.abs(vPente) > 0.01) {
        vPente += (-2 * W * vPente - W * W * (pente - cible)) * dt;
        pente += vPente * dt;
        bouge = true;
      } else { pente = cible; vPente = 0; }
    }

    if (Math.abs(pivotZ - ciblePivot) > 0.01 || Math.abs(vPivot) > 0.01) {
      vPivot += (-2 * W * vPivot - W * W * (pivotZ - ciblePivot)) * dt;
      pivotZ += vPivot * dt;
      bouge = true;
    } else { pivotZ = ciblePivot; vPivot = 0; }

    rendre();
    if (bouge && vu) { boucle = requestAnimationFrame(trame); }
    else { boucle = null; }
  }

  function reveiller() {
    if (boucle === null && vu) { dernier = performance.now(); boucle = requestAnimationFrame(trame); }
  }

  /* ---- Manipulation ----------------------------------------------------
     Suivi au pointeur, capture comprise : sans setPointerCapture, le suivi
     s'arrête dès que le doigt sort du cadre, et l'objet reste planté. */
  var dernierX = 0, dernierY = 0, histoire = [];

  hote.addEventListener("pointerdown", function (e) {
    if (e.button !== undefined && e.button !== 0) return;
    if (e.target.closest(".v360__b")) return;
    hote.setPointerCapture(e.pointerId);
    touche = true; auto = false;
    hote.setAttribute("data-touche", "");
    vTour = 0; vPente = 0;
    dernierX = e.clientX; dernierY = e.clientY;
    histoire = [{ x: e.clientX, y: e.clientY, t: performance.now() }];
    majAuto();
  });

  hote.addEventListener("pointermove", function (e) {
    if (!touche) return;
    var dx = e.clientX - dernierX, dy = e.clientY - dernierY;
    dernierX = e.clientX; dernierY = e.clientY;
    tour += dx * 0.42;
    pente = borner(pente - dy * 0.3);
    histoire.push({ x: e.clientX, y: e.clientY, t: performance.now() });
    if (histoire.length > 6) histoire.shift();
    rendre();
  });

  function lacher(e) {
    if (!touche) return;
    touche = false;
    try { hote.releasePointerCapture(e.pointerId); } catch (x) {}
    /* La vitesse vient des dernières positions, pas du dernier delta : un
       seul échantillon donne une valeur bruitée et l'objet part de travers. */
    var n = histoire.length;
    if (n >= 2) {
      var a = histoire[0], b = histoire[n - 1];
      var dts = (b.t - a.t) / 1000;
      if (dts > 0.004) {
        vTour = (b.x - a.x) * 0.42 / dts;
        vTour = Math.max(-1600, Math.min(1600, vTour));
      }
    }
    reveiller();
  }
  hote.addEventListener("pointerup", lacher);
  hote.addEventListener("pointercancel", lacher);

  /* ---- Clavier ---------------------------------------------------------
     Un objet qu'on ne peut tourner qu'à la souris est inutilisable sans
     souris. Les flèches font le même travail. */
  hote.addEventListener("keydown", function (e) {
    var k = e.key, pas = e.shiftKey ? 22 : 9;
    if (k === "ArrowLeft")       { tour -= pas; auto = false; }
    else if (k === "ArrowRight") { tour += pas; auto = false; }
    else if (k === "ArrowUp")    { pente = Math.max(PENTE_MIN, pente - 5); }
    else if (k === "ArrowDown")  { pente = Math.min(PENTE_MAX, pente + 5); }
    else return;
    e.preventDefault();
    hote.setAttribute("data-touche", "");
    majAuto(); rendre();
  });

  /* ---- Commandes -------------------------------------------------------- */
  var bAuto = hote.querySelector("[data-v360-auto]");
  var bPivot = hote.querySelector("[data-v360-pivot]");
  var bFace = hote.querySelector("[data-v360-face]");

  function majAuto() {
    if (bAuto) bAuto.setAttribute("aria-pressed", auto ? "true" : "false");
  }

  if (bAuto) bAuto.addEventListener("click", function () {
    auto = !auto; majAuto(); reveiller();
  });

  if (bPivot) bPivot.addEventListener("click", function () {
    ciblePivot = ciblePivot === 0 ? -90 : 0;
    bPivot.setAttribute("aria-pressed", ciblePivot !== 0 ? "true" : "false");
    bPivot.querySelector("span").textContent = ciblePivot === 0 ? "Paysage" : "Portrait";
    reveiller();
  });

  if (bFace) bFace.addEventListener("click", function () {
    /* On vise le demi-tour le plus proche dans le sens courant, pour que le
       bouton ne fasse jamais repartir l'objet en arrière de trois tours. */
    var cible = Math.round((tour + 180) / 360) * 360 + 180;
    vTour = (cible - tour) * 2.4;
    auto = false; majAuto(); reveiller();
  });

  if ("IntersectionObserver" in window) {
    new IntersectionObserver(function (es) {
      vu = es[0].isIntersecting;
      if (vu) reveiller();
      else if (boucle !== null) { cancelAnimationFrame(boucle); boucle = null; }
    }, { rootMargin: "20% 0px" }).observe(hote);
  }

  addEventListener("resize", ajuster, { passive: true });
  if (menage.addEventListener) menage.addEventListener("change", function () {
    auto = !menage.matches; majAuto();
  });

  majAuto();
  ajuster();
  reveiller();
})();
