/* =========================================================================
   Moteur de la scène 3D de la page d'accueil.

   Une seule boucle anime tout : la borne, les objets en orbite, et la
   réaction au pointeur et au défilement. Plusieurs boucles concurrentes,
   ou une animation CSS par objet, finissent par se marcher dessus dès
   qu'on veut composer deux mouvements sur le même élément.

   Rien ne tourne quand ce n'est pas utile : la boucle s'arrête dès que la
   scène sort du champ, et ne démarre pas du tout si le visiteur a demandé
   moins d'animations.
   ========================================================================= */
(function () {
  "use strict";

  var stage = document.getElementById("stage");
  if (!stage) return;

  var reduit = matchMedia("(prefers-reduced-motion: reduce)").matches;
  var pivot  = stage.querySelector("[data-pivot]");
  var borne  = stage.querySelector("[data-borne]");
  var objets = [].slice.call(stage.querySelectorAll("[data-objet]"));
  var video  = document.getElementById("film-borne");
  var btnSon = document.getElementById("stage-son");

  /* ---- La vidéo -------------------------------------------------------
     Un navigateur n'autorise la lecture automatique QUE si la vidéo est
     muette : c'est une règle de Chrome, Safari et Firefox, pas un réglage.
     Elle démarre donc sans son, et le bouton rend le son au premier clic,
     qui est le geste que les navigateurs attendent.

     Elle ne démarre pas non plus si le visiteur a demandé moins
     d'animations, ni en mode économie de données, ni sur une connexion
     lente : 2,6 Mo imposés à quelqu'un en 3G, c'est une page qu'il quitte
     avant de l'avoir vue. */
  function connexionMenagee() {
    var c = navigator.connection || navigator.mozConnection || navigator.webkitConnection;
    if (!c) return false;
    if (c.saveData) return true;
    return /^(slow-2g|2g|3g)$/.test(c.effectiveType || "");
  }

  if (video) {
    var autoriser = !reduit && !connexionMenagee();
    if (autoriser) {
      video.muted = true;               /* obligatoire avant play() */
      video.setAttribute("muted", "");
      var essai = video.play();
      if (essai && typeof essai.catch === "function") {
        essai.catch(function () {
          /* Refus malgré tout : on laisse l'affiche et le bouton prend le
             relais. On ne réessaie pas en boucle, ce serait du bruit. */
          if (btnSon) btnSon.dataset.etat = "arret";
        });
      }
    } else {
      video.removeAttribute("autoplay");
      video.preload = "none";
      if (btnSon) btnSon.dataset.etat = "arret";
    }
  }

  if (btnSon && video) {
    var libelle = btnSon.querySelector("[data-libelle]");
    var icone   = btnSon.querySelector("use");
    btnSon.addEventListener("click", function () {
      if (video.paused) { video.play(); }
      if (video.muted) {
        video.muted = false;
        btnSon.setAttribute("aria-pressed", "true");
        if (libelle) libelle.textContent = "Couper le son";
        if (icone) icone.setAttribute("href", "#i-son");
      } else {
        video.muted = true;
        btnSon.setAttribute("aria-pressed", "false");
        if (libelle) libelle.textContent = "Activer le son";
        if (icone) icone.setAttribute("href", "#i-son-coupe");
      }
    });
  }

  if (reduit) return;

  /* ---- État de chaque objet en orbite --------------------------------
     Chacun garde sa position de départ, sa phase et sa vitesse propres.
     Des phases tirées au hasard à chaque chargement donneraient une scène
     différente à chaque visite : on les dérive de l'index, ce qui reste
     irrégulier à l'œil mais reproductible. */
  var etats = objets.map(function (el, i) {
    return {
      el: el,
      x: +el.dataset.x || 0,
      y: +el.dataset.y || 0,
      z: +el.dataset.z || 0,
      phase: (i * 1.7) % 6.28,
      ampl: 14 + (i % 4) * 7,
      vit: 0.00022 + (i % 5) * 0.00006,
      rot: (i % 2 ? 1 : -1) * (5 + (i % 3) * 3)
    };
  });

  /* ---- Pointeur et défilement ----------------------------------------- */
  var cibleX = 0, cibleY = 0, curX = 0, curY = 0, defil = 0;

  stage.addEventListener("pointermove", function (e) {
    if (e.pointerType === "touch") return;     /* le doigt sert à défiler */
    var r = stage.getBoundingClientRect();
    cibleY = ((e.clientX - r.left) / r.width - 0.5) * 13;    /* rotation Y */
    cibleX = (0.5 - (e.clientY - r.top) / r.height) * 9;     /* rotation X */
  });
  stage.addEventListener("pointerleave", function () { cibleX = 0; cibleY = 0; });

  /* ---- La boucle ------------------------------------------------------- */
  var actif = true, marche = null;

  function image(t) {
    marche = null;
    if (!actif) return;

    /* Lissage : la scène suit le pointeur avec un retard, ce qui évite le
       mouvement nerveux d'un suivi au pixel. */
    curX += (cibleX - curX) * 0.06;
    curY += (cibleY - curY) * 0.06;

    if (pivot) {
      pivot.style.setProperty("--mx", (curX + defil * 5).toFixed(2) + "deg");
      pivot.style.setProperty("--my", curY.toFixed(2) + "deg");
    }
    if (borne) {
      borne.style.setProperty("--ry", (-16 + curY * 0.55 + Math.sin(t * 0.00019) * 4).toFixed(2) + "deg");
      borne.style.setProperty("--rx", (3 + curX * 0.3 + Math.sin(t * 0.00026) * 1.6).toFixed(2) + "deg");
      borne.style.setProperty("--tz", (defil * -140).toFixed(1) + "px");
    }

    for (var i = 0; i < etats.length; i++) {
      var o = etats[i];
      var a = t * o.vit + o.phase;
      /* Les objets s'écartent à mesure qu'on défile : la scène s'ouvre au
         lieu de simplement disparaître vers le haut. */
      var ecart = 1 + defil * 0.5;
      o.el.style.setProperty("--x", (o.x * ecart).toFixed(1));
      o.el.style.setProperty("--y", (o.y * ecart + Math.sin(a) * o.ampl).toFixed(1));
      o.el.style.setProperty("--z", (o.z + Math.cos(a * 0.8) * 26).toFixed(1));
      o.el.style.setProperty("--oy", (Math.sin(a * 0.7) * o.rot - 14).toFixed(2) + "deg");
      o.el.style.setProperty("--ox", (Math.cos(a * 0.6) * (o.rot * 0.5)).toFixed(2) + "deg");
      o.el.style.setProperty("--oz", (Math.sin(a * 0.45) * (o.rot * 0.35)).toFixed(2) + "deg");
    }

    marche = requestAnimationFrame(image);
  }

  function relancer() { if (actif && marche === null) marche = requestAnimationFrame(image); }

  /* La scène ne tourne que tant qu'elle est à l'écran. Une boucle qui
     continue dix écrans plus bas vide la batterie sans rien montrer. */
  if ("IntersectionObserver" in window) {
    new IntersectionObserver(function (es) {
      actif = es[0].isIntersecting;
      if (actif) relancer();
      else if (marche !== null) { cancelAnimationFrame(marche); marche = null; }
      if (video) { if (actif) { if (video.autoplay && video.paused) video.play().catch(function () {}); } else video.pause(); }
    }, { threshold: 0.02 }).observe(stage);
  }

  addEventListener("scroll", function () {
    var r = stage.getBoundingClientRect();
    defil = Math.min(1, Math.max(0, -r.top / Math.max(1, r.height)));
  }, { passive: true });

  relancer();
})();
