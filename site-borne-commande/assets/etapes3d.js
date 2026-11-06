/* =========================================================================
   LE PARCOURS EN TROIS DIMENSIONS — pilotage

   Une seule valeur gouverne une scène : la position dans le parcours, de 0
   au nombre d'étapes moins une. Le défilement fixe une cible, un ressort
   amorti critique tient la valeur courante, et chaque accessoire en déduit
   sa place en profondeur.

   Pourquoi un ressort plutôt que des images clés : parce qu'un lecteur qui
   remonte au milieu du mouvement ne doit rien attendre. Avec des keyframes
   il faudrait interrompre, relire la valeur affichée, puis relancer, et la
   coupure se voit. Ici la cible change, la vitesse est conservée, et le
   mouvement reste continu dans les deux sens.

   Paramètres repris du réglage d'Apple pour un déplacement : amortissement
   1,0, réponse 0,4 s. Amortissement critique, donc aucun dépassement : un
   rebond se justifie quand le geste portait de l'élan, ce qui n'est pas le
   cas d'un défilement lu.

   Le module sert toutes les sections « .parcours » de la page. Deux
   parcours cohabitent sur l'accueil, chacun avec son propre ressort.
   ========================================================================= */
(function () {
  "use strict";

  var REPONSE = 0.4, AMORT = 1.0;
  var W = 2 * Math.PI / REPONSE;
  var menage = matchMedia("(prefers-reduced-motion: reduce)");

  function monter(bloc) {
    var scene = bloc.querySelector(".parcours__scene");
    var liste = bloc.querySelector(".parcours__liste");
    if (!scene || !liste) return null;

    var accessoires = [].slice.call(scene.querySelectorAll(".ac"));
    var items = [].slice.call(liste.children);
    var jalons = [].slice.call(scene.querySelectorAll(".parcours__jalons i"));
    if (!accessoires.length || items.length !== accessoires.length) return null;

    var N = accessoires.length;
    var x = 0, v = 0, cible = 0, dernier = 0, boucle = null, vu = false;

    /* La cible est lue dans la géométrie de la liste. On n'utilise pas
       l'étape « visible » au sens d'un IntersectionObserver, qui ne donne
       qu'un entier et fait sauter la scène d'un cran à l'autre : on
       interpole entre deux étapes selon la position de la ligne de
       lecture, ce qui donne une valeur continue. */
    function lireCible() {
      var ligne = innerHeight * 0.45;
      var c = [], i, r;
      for (i = 0; i < N; i++) {
        r = items[i].getBoundingClientRect();
        c.push(r.top + r.height / 2);
      }
      if (ligne <= c[0]) return 0;
      if (ligne >= c[N - 1]) return N - 1;
      for (i = 0; i < N - 1; i++) {
        if (ligne >= c[i] && ligne < c[i + 1]) {
          var ecart = c[i + 1] - c[i];
          return i + (ecart > 0 ? (ligne - c[i]) / ecart : 0);
        }
      }
      return N - 1;
    }

    /* Deux propriétés seulement, transform et opacity : ce sont les seules
       que le compositeur traite sans refaire la mise en page. La variable
       --a transporte l'activité de l'accessoire jusqu'à ses pièces, qui
       animent leur propre détail en CSS. */
    function poser() {
      var i, d, e, a;
      for (i = 0; i < N; i++) {
        d = i - x;
        e = Math.abs(d);
        a = accessoires[i];
        a.style.opacity = Math.max(0, Math.min(1, 1 - e * 1.15)).toFixed(3);
        a.style.transform =
          "translate3d(0, calc(-50% + " + (d * 54).toFixed(1) + "px), " +
          (-260 * e).toFixed(1) + "px)" +
          " rotateX(" + (-9 * d).toFixed(2) + "deg)" +
          " rotateZ(" + (3 * d).toFixed(2) + "deg)" +
          " scale(" + (1 - 0.1 * e).toFixed(3) + ")";
        a.style.setProperty("--a", Math.max(0, Math.min(1, 1 - e)).toFixed(3));
      }
      for (i = 0; i < jalons.length; i++) {
        jalons[i].style.setProperty("--f", Math.max(0, Math.min(1, x - i + 1)).toFixed(3));
      }
      var vif = Math.round(x);
      for (i = 0; i < N; i++) {
        if (i === vif) items[i].setAttribute("data-vif", "");
        else items[i].removeAttribute("data-vif");
      }
    }

    function trame(t) {
      var dt = Math.min(0.033, (t - dernier) / 1000) || 0.016;
      dernier = t;
      v += (-2 * AMORT * W * v - W * W * (x - cible)) * dt;
      x += v * dt;
      poser();
      if (Math.abs(x - cible) < 0.0008 && Math.abs(v) < 0.0008) {
        x = cible; v = 0; poser();
        boucle = null;                     /* au repos : plus aucune trame */
        return;
      }
      boucle = requestAnimationFrame(trame);
    }

    function demander() {
      cible = lireCible();
      if (menage.matches) { x = cible; v = 0; poser(); return; }
      if (boucle === null && vu) { dernier = performance.now(); boucle = requestAnimationFrame(trame); }
    }

    /* Une scène hors du champ ne consomme aucune trame. */
    if ("IntersectionObserver" in window) {
      new IntersectionObserver(function (es) {
        vu = es[0].isIntersecting;
        if (vu) demander();
        else if (boucle !== null) { cancelAnimationFrame(boucle); boucle = null; }
      }, { rootMargin: "25% 0px" }).observe(bloc);
    } else {
      vu = true;
    }

    cible = lireCible(); x = cible; poser();
    return demander;
  }

  var mains = [];
  [].forEach.call(document.querySelectorAll(".parcours"), function (b) {
    var m = monter(b);
    if (m) mains.push(m);
  });
  if (!mains.length) return;

  function reveiller() { for (var i = 0; i < mains.length; i++) mains[i](); }
  addEventListener("scroll", reveiller, { passive: true });
  addEventListener("resize", reveiller, { passive: true });
  if (menage.addEventListener) menage.addEventListener("change", reveiller);
  reveiller();
})();
