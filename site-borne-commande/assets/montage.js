/* =========================================================================
   Le montage du burger au défilement.

   Les cinq couches découpées dans la photo s'écartent quand la section
   entre dans le champ, et se posent quand elle est centrée. Rien ne bouge
   si le visiteur a demandé moins d'animations.

   Piloté en JavaScript plutôt qu'avec animation-timeline : la propriété
   n'est pas encore lue par Firefox, et une section qui reste figée chez un
   visiteur sur cinq n'est pas une animation, c'est un bug.
   ========================================================================= */
(function () {
  "use strict";

  var cadre = document.querySelector("[data-montage]");
  if (!cadre) return;
  if (matchMedia("(prefers-reduced-motion: reduce)").matches) return;

  var couches = [].slice.call(cadre.querySelectorAll(".monte__c"));
  if (!couches.length) return;

  var enVue = false, demande = null;

  function placer() {
    demande = null;
    var r = cadre.getBoundingClientRect();
    var h = innerHeight || 800;
    /* 0 quand la section arrive par le bas, 1 quand elle est centrée. */
    var t = 1 - Math.min(1, Math.max(0, (r.top - h * 0.18) / (h * 0.62)));
    var e = 1 - t;                                  /* coefficient d'écartement */
    for (var i = 0; i < couches.length; i++) {
      var c = couches[i];
      var d = +getComputedStyle(c).getPropertyValue("--d") || 0;
      c.style.transform = "translateY(" + (-d * e).toFixed(2) + "%) scale(" + (1 + e * 0.04).toFixed(3) + ")";
      c.style.opacity = (0.25 + 0.75 * t).toFixed(3);
    }
  }

  function demander() { if (enVue && demande === null) demande = requestAnimationFrame(placer); }

  if ("IntersectionObserver" in window) {
    new IntersectionObserver(function (es) {
      enVue = es[0].isIntersecting;
      if (enVue) demander();
    }, { rootMargin: "20% 0px" }).observe(cadre);
  } else {
    enVue = true;
  }

  addEventListener("scroll", demander, { passive: true });
  addEventListener("resize", demander, { passive: true });
  placer();
})();
