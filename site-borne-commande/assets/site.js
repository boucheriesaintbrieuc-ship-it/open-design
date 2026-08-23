/* =========================================================================
   Bornéa — comportements du site.
   Vanilla, sans dépendance. Chaque bloc se désactive tout seul si son
   markup est absent de la page, ce qui permet de charger ce fichier partout.
   ========================================================================= */
(() => {
  "use strict";
  const C = window.CONFIG || {};
  const $  = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];

  const euros = n => n.toLocaleString("fr-FR", { minimumFractionDigits: 2, maximumFractionDigits: 2 }) + " €";
  const ttc   = ht => ht * (1 + (C.tva ?? 0.2));

  /** Prix unitaire hors taxes applicable à une quantité, selon les paliers. */
  const prixUnitaire = (q) => {
    const p = (C.paliers || []).filter(p => q >= p.aPartirDe).pop();
    return p ? p.prixHT : 0;
  };

  const init = () => {

    /* ---- Valeurs de config injectées dans le HTML ---------------------
       Tout élément portant data-config="chemin.dans.CONFIG" reçoit la
       valeur correspondante. Évite d'avoir le téléphone en dur dans dix
       fichiers. */
    $$("[data-config]").forEach(el => {
      const v = el.dataset.config.split(".").reduce((o, k) => (o || {})[k], C);
      if (v === undefined || v === null) return;
      if (el.tagName === "A" && el.dataset.configHref) el.setAttribute("href", el.dataset.configHref.replace("{v}", v));
      else el.textContent = v;
    });
    $$("[data-tel]").forEach(a => { a.href = "tel:" + (C.telephone || ""); if (!a.textContent.trim()) a.textContent = C.telAffiche || ""; });
    $$("[data-mail]").forEach(a => { a.href = "mailto:" + (C.email || ""); if (!a.textContent.trim()) a.textContent = C.email || ""; });
    $$("[data-annee]").forEach(el => { el.textContent = new Date().getFullYear(); });

    /* ---- Prix affichés un peu partout --------------------------------- */
    $$("[data-prix-ht]").forEach(el => { el.textContent = euros(prixUnitaire(+el.dataset.prixHt || 1)) + " HT"; });
    $$("[data-prix-ttc]").forEach(el => { el.textContent = euros(ttc(prixUnitaire(+el.dataset.prixTtc || 1))) + " TTC"; });

    /* ---- Lien courant dans la navigation ------------------------------ */
    const ici = location.pathname.split("/").pop() || "index.html";
    $$(".nav a, .pied a").forEach(a => {
      const href = a.getAttribute("href");
      if (href && href.split("/").pop() === ici && !href.startsWith("#")) a.setAttribute("aria-current", "page");
    });

    /* ---- Configurateur ------------------------------------------------ */
    const form = $("#configurateur");
    if (form) {
      const sortieQte = $("#qte-valeur", form);
      const lignes    = $("#recap-lignes");
      const totalHT   = $("#recap-total-ht");
      const totalTTC  = $("#recap-total-ttc");
      const bouton    = $("#aller-au-paiement");
      const barrePrix = $("#barre-prix");
      const scene     = $("#scene-bornes");
      let quantite = 1;

      const etat = () => ({
        quantite,
        miseEnService: $("#opt-mise-en-service")?.checked || false,
        garantie:      $("#opt-garantie")?.checked || false
      });

      const detail = () => {
        const e = etat();
        const pu = prixUnitaire(e.quantite);
        const l = [{ libelle: `Borne tactile sur pied × ${e.quantite}`, montant: pu * e.quantite, detail: euros(pu) + " l’unité" }];
        if (e.miseEnService) l.push({ libelle: C.options.miseEnService.libelle, montant: C.options.miseEnService.prixHT });
        if (e.garantie)      l.push({ libelle: C.options.garantie.libelle + ` × ${e.quantite}`, montant: C.options.garantie.prixHT * e.quantite });
        l.push({ libelle: "Livraison en France métropolitaine", montant: C.livraisonHT || 0, gratuit: !C.livraisonHT });
        return l;
      };

      const dessinerScene = () => {
        if (!scene) return;
        const bornes = $$(".borne", scene);
        const visibles = Math.min(quantite, bornes.length);
        bornes.forEach((b, i) => {
          /* hidden est une propriété de HTMLElement, pas de SVGElement :
             sur un <svg> il faut passer par l'attribut, sinon on ne fait
             qu'ajouter une propriété inerte à l'objet. */
          const cache = b.hasAttribute("hidden");
          const doitVoir = i < visibles;
          if (doitVoir && cache) {
            b.removeAttribute("hidden");
            b.dataset.entrant = "1";
            setTimeout(() => delete b.dataset.entrant, 320);
          } else if (!doitVoir && !cache) {
            b.setAttribute("hidden", "");
          }
        });
        const surplus = $("#scene-surplus");
        if (surplus) {
          const reste = quantite - bornes.length;
          surplus.hidden = reste <= 0;
          if (reste > 0) surplus.textContent = "+ " + reste + " autre" + (reste > 1 ? "s" : "");
        }
      };

      const rendre = () => {
        const l = detail();
        const ht = l.reduce((s, x) => s + x.montant, 0);
        if (sortieQte) sortieQte.textContent = quantite;
        if (lignes) {
          lignes.innerHTML = "";
          l.forEach(x => {
            const d = document.createElement("div");
            const g = document.createElement("span");
            g.textContent = x.libelle;
            if (x.detail) { const s = document.createElement("span"); s.className = "note"; s.textContent = " " + x.detail; g.append(s); }
            const p = document.createElement("span");
            p.className = "prix";
            p.textContent = x.gratuit ? "Offerte" : euros(x.montant);
            d.append(g, p);
            lignes.append(d);
          });
        }
        const cgv = $("#accepte-cgv");
        if (bouton) bouton.disabled = cgv ? !cgv.checked : false;
        if (totalHT)  totalHT.textContent  = euros(ht);
        if (totalTTC) totalTTC.textContent = euros(ttc(ht)) + " TTC";
        if (barrePrix) barrePrix.textContent = euros(ttc(ht)) + " TTC";
        dessinerScene();
      };

      $$("[data-qte]", form).forEach(b => b.addEventListener("click", () => {
        quantite = Math.min(20, Math.max(1, quantite + (+b.dataset.qte)));
        rendre();
      }));
      $$("input[type=checkbox]", form).forEach(i => i.addEventListener("change", rendre));
      $("#accepte-cgv")?.addEventListener("change", rendre);

      /* ---- Départ vers Stripe ---------------------------------------- */
      if (bouton) bouton.addEventListener("click", async (ev) => {
        ev.preventDefault();
        const e = etat();
        const email = $("#client-email")?.value.trim() || "";
        const ref   = $("#client-etablissement")?.value.trim() || "";

        if (C.modePaiement === "php") {
          bouton.disabled = true;
          bouton.textContent = "Ouverture du paiement…";
          try {
            const r = await fetch(C.cheminPhp, {
              method: "POST",
              headers: { "Content-Type": "application/json" },
              body: JSON.stringify({ ...e, email, reference: ref })
            });
            const data = await r.json();
            if (!r.ok || !data.url) throw new Error(data.erreur || "réponse inattendue du serveur");
            location.href = data.url;
            return;
          } catch (err) {
            bouton.disabled = false;
            bouton.textContent = "Payer par carte";
            const zone = $("#erreur-paiement");
            if (zone) {
              zone.hidden = false;
              zone.textContent = "Le paiement n’a pas pu s’ouvrir (" + err.message + "). Appelez le " +
                (C.telAffiche || "") + " ou écrivez à " + (C.email || "") + ", la commande sera prise à la main.";
            }
            return;
          }
        }

        /* Mode Payment Links : un lien par palier de quantité. */
        const cle = e.quantite >= 3 ? "3" : String(e.quantite);
        const base = (C.liensStripe || {})[cle] || "";
        if (!base || base.includes("REMPLACER")) {
          const zone = $("#erreur-paiement");
          if (zone) {
            zone.hidden = false;
            zone.textContent = "Le lien de paiement n’est pas encore configuré. Renseignez liensStripe dans assets/config.js, ou passez commande au " + (C.telAffiche || "") + ".";
          }
          return;
        }
        const u = new URL(base);
        if (email) u.searchParams.set("prefilled_email", email);
        if (ref)   u.searchParams.set("client_reference_id", ref.replace(/[^\w\-]+/g, "-").slice(0, 190));
        location.href = u.toString();
      });

      rendre();
    }

    /* ---- Formulaires sans serveur : ouverture de la messagerie -------- */
    $$("form[data-mailto]").forEach(f => {
      f.addEventListener("submit", ev => {
        ev.preventDefault();
        const d = new FormData(f);
        const corps = [...d.entries()].map(([k, v]) => k + " : " + v).join("\n");
        location.href = "mailto:" + (C.email || "") +
          "?subject=" + encodeURIComponent(f.dataset.mailto) +
          "&body=" + encodeURIComponent(corps);
        const secours = $(".secours", f);
        if (secours) {
          secours.hidden = false;
          secours.innerHTML = "Si votre messagerie ne s’ouvre pas, appelez le <a href=\"tel:" + (C.telephone || "") +
            "\">" + (C.telAffiche || "") + "</a> ou écrivez à <a href=\"mailto:" + (C.email || "") + "\">" + (C.email || "") + "</a>.";
        }
      });
    });

    /* ---- Page de confirmation : rappel de la référence Stripe --------- */
    const ref = $("#ref-commande");
    if (ref) {
      const id = new URLSearchParams(location.search).get("session_id");
      if (id) { ref.hidden = false; $("#ref-valeur").textContent = id; }
    }
  };

  document.readyState === "loading"
    ? document.addEventListener("DOMContentLoaded", init, { once: true })
    : init();
})();
