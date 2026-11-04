/* =========================================================================
   Configurateur de borne.

   Chargé uniquement par commander.html. Il fait trois choses :
   1. recueillir l'enseigne, la carte, les suppléments et le choix de site ;
   2. produire un fichier HTML autonome qui tourne sur la tablette, hors ligne,
      images comprises (elles sont redimensionnées puis intégrées au fichier) ;
   3. transmettre cette configuration avec la commande.

   Rien ne part sur un serveur tant que le client n'a pas validé : tout vit
   dans son navigateur, et la configuration est conservée en local pour
   survivre à l'aller-retour vers la page de paiement.
   ========================================================================= */
(() => {
  "use strict";

  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const CLE = "borne-config-v1";

  const euros = n => Number(n || 0).toLocaleString("fr-FR", { minimumFractionDigits: 2, maximumFractionDigits: 2 }) + " €";
  const esc = s => String(s == null ? "" : s)
    .replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;").replace(/'/g, "&#39;");
  const uid = () => Math.random().toString(36).slice(2, 9);

  /* ---- Carte de départ -------------------------------------------------
     Un configurateur vide décourage. Celle-ci est modifiable entièrement et
     sert surtout à montrer ce que la borne sait afficher. */
  const DEPART = {
    enseigne: { nom: "", type: "Restauration rapide", couleur: "#D4321C", logo: "" },
    tva: { place: 10, emporter: 5.5 },
    categories: [
      { id: uid(), nom: "Menus", produits: [
        { id: uid(), nom: "Menu burger", prix: 12.9, desc: "Burger, frites et boisson", image: "" },
        { id: uid(), nom: "Menu poulet", prix: 11.5, desc: "Poulet croustillant, frites et boisson", image: "" },
        { id: uid(), nom: "Menu enfant", prix: 7.5, desc: "Petit burger, frites et jus", image: "" },
      ]},
      { id: uid(), nom: "À la carte", produits: [
        { id: uid(), nom: "Burger simple", prix: 8.5, desc: "Steak, cheddar, salade, sauce maison", image: "" },
        { id: uid(), nom: "Frites", prix: 3.2, desc: "Portion généreuse", image: "" },
      ]},
      { id: uid(), nom: "Boissons", produits: [
        { id: uid(), nom: "Soda 33 cl", prix: 2.5, desc: "Au gobelet", image: "" },
        { id: uid(), nom: "Eau minérale 50 cl", prix: 1.8, desc: "Bouteille", image: "" },
        { id: uid(), nom: "Café", prix: 1.5, desc: "Expresso", image: "" },
      ]},
      { id: uid(), nom: "Desserts", produits: [
        { id: uid(), nom: "Brownie", prix: 3.5, desc: "Fait maison", image: "" },
      ]},
    ],
    supplements: [
      { id: uid(), nom: "Bacon", prix: 1.5 },
      { id: uid(), nom: "Cheddar", prix: 1 },
      { id: uid(), nom: "Frites XL", prix: 1.2 },
      { id: uid(), nom: "Sauce maison", prix: 0.6 },
    ],
    site: { solution: "nouveau", domaine: "", statut: "" },
  };

  let E = charger() || structuredClone(DEPART);

  function charger() {
    try { const v = localStorage.getItem(CLE); return v ? JSON.parse(v) : null; }
    catch (e) { return null; }
  }
  function sauver() {
    try { localStorage.setItem(CLE, JSON.stringify(E)); } catch (e) { /* mode privé */ }
  }

  /* ---- Images : redimensionnées dans le navigateur ---------------------
     Une photo de téléphone pèse 4 Mo. Intégrée telle quelle dans le fichier
     de la borne, elle le rendrait inutilisable. On la ramène à 420 px. */
  function redimensionner(fichier, max = 420) {
    return new Promise((ok, non) => {
      if (!fichier.type.startsWith("image/")) return non(new Error("ce fichier n’est pas une image"));
      const fr = new FileReader();
      fr.onerror = () => non(new Error("lecture impossible"));
      fr.onload = () => {
        const im = new Image();
        im.onerror = () => non(new Error("image illisible"));
        im.onload = () => {
          const c = Math.min(im.width, im.height);
          const cv = document.createElement("canvas");
          cv.width = cv.height = max;
          const x = cv.getContext("2d");
          x.drawImage(im, (im.width - c) / 2, (im.height - c) / 2, c, c, 0, 0, max, max);
          ok(cv.toDataURL("image/jpeg", 0.74));
        };
        im.src = fr.result;
      };
      fr.readAsDataURL(fichier);
    });
  }

  /* =====================================================================
     Rendu du configurateur
     ===================================================================== */
  function rendreEnseigne() {
    const z = $("#cfg-enseigne");
    if (!z) return;
    $("#ens-nom").value = E.enseigne.nom;
    $("#ens-type").value = E.enseigne.type;
    $("#ens-couleur").value = E.enseigne.couleur;
    const ap = $("#ens-logo-apercu");
    ap.innerHTML = E.enseigne.logo
      ? '<img src="' + E.enseigne.logo + '" alt="Logo de votre enseigne" width="72" height="72">'
      : '<span class="note">Aucun logo</span>';
  }

  function rendreCarte() {
    const z = $("#cfg-carte");
    if (!z) return;
    z.innerHTML = "";
    E.categories.forEach((cat, ic) => {
      const bloc = document.createElement("section");
      bloc.className = "cat";
      bloc.innerHTML =
        '<header class="cat__tete">' +
          '<input class="cat__nom" value="' + esc(cat.nom) + '" aria-label="Nom de la catégorie">' +
          '<button type="button" class="lien-sup" data-sup-cat="' + ic + '">Retirer la catégorie</button>' +
        '</header>' +
        '<div class="produits"></div>' +
        '<button type="button" class="btn btn--secondaire btn--petit" data-add-prod="' + ic + '">Ajouter un produit</button>';
      const liste = $(".produits", bloc);
      cat.produits.forEach((p, ip) => {
        const l = document.createElement("div");
        l.className = "prod";
        l.innerHTML =
          '<label class="prod__img">' +
            (p.image ? '<img src="' + p.image + '" alt="">' : '<span>photo</span>') +
            '<input type="file" accept="image/*" data-img="' + ic + ':' + ip + '" hidden>' +
          '</label>' +
          '<div class="prod__champs">' +
            '<input value="' + esc(p.nom) + '" data-ch="nom" data-i="' + ic + ':' + ip + '" placeholder="Nom du produit" aria-label="Nom du produit">' +
            '<input value="' + esc(p.desc) + '" data-ch="desc" data-i="' + ic + ':' + ip + '" placeholder="Description courte" aria-label="Description">' +
          '</div>' +
          '<div class="prod__prix">' +
            '<input type="number" step="0.10" min="0" value="' + Number(p.prix).toFixed(2) + '" data-ch="prix" data-i="' + ic + ':' + ip + '" aria-label="Prix en euros"> €' +
          '</div>' +
          '<button type="button" class="lien-sup" data-sup-prod="' + ic + ':' + ip + '" aria-label="Retirer ce produit">×</button>';
        liste.append(l);
      });
      z.append(bloc);
    });

    const sup = $("#cfg-supplements");
    sup.innerHTML = "";
    E.supplements.forEach((s, i) => {
      const l = document.createElement("div");
      l.className = "supp";
      l.innerHTML =
        '<input value="' + esc(s.nom) + '" data-sch="nom" data-si="' + i + '" placeholder="Nom" aria-label="Nom du supplément">' +
        '<input type="number" step="0.10" min="0" value="' + Number(s.prix).toFixed(2) + '" data-sch="prix" data-si="' + i + '" aria-label="Prix du supplément"> €' +
        '<button type="button" class="lien-sup" data-sup-supp="' + i + '" aria-label="Retirer">×</button>';
      sup.append(l);
    });

    const n = E.categories.reduce((t, c) => t + c.produits.length, 0);
    $("#cfg-compte").textContent = n + (n > 1 ? " produits" : " produit") + " dans " + E.categories.length + " catégories";
  }

  function rendreSite() {
    const z = $("#cfg-site");
    if (!z) return;
    $$("input[name=solution]").forEach(r => { r.checked = (r.value === E.site.solution); });
    $("#dom-nom").value = E.site.domaine;
    $("#bloc-domaine").hidden = (E.site.solution !== "nouveau");
  }

  /* =====================================================================
     Le fichier de borne produit
     ===================================================================== */
  function genererBorne() {
    const ens = E.enseigne;
    const nom = ens.nom.trim() || "Votre enseigne";
    const c = ens.couleur || "#D4321C";
    const data = {
      nom, couleur: c, logo: ens.logo,
      tva: E.tva,
      categories: E.categories.map(cat => ({
        nom: cat.nom,
        produits: cat.produits.filter(p => p.nom.trim()).map(p => ({
          nom: p.nom, prix: Number(p.prix) || 0, desc: p.desc, image: p.image
        }))
      })).filter(cat => cat.produits.length),
      supplements: E.supplements.filter(s => s.nom.trim()).map(s => ({ nom: s.nom, prix: Number(s.prix) || 0 })),
    };

    return `<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">
<meta name="robots" content="noindex, nofollow">
<title>${esc(nom)} — Commande</title>
<style>
*,*::before,*::after{box-sizing:border-box}
html,body{margin:0;height:100%;overflow:hidden;background:#0D0D0F;color:#fff;
 font-family:"Helvetica Neue","Segoe UI",system-ui,sans-serif;-webkit-font-smoothing:antialiased;
 -webkit-tap-highlight-color:transparent;user-select:none}
button{font:inherit;color:inherit;border:0;background:none;cursor:pointer}
#app{display:flex;flex-direction:column;height:100%}
header{display:flex;align-items:center;gap:14px;padding:14px 20px;background:#141417;border-bottom:1px solid #26262B}
header img{width:44px;height:44px;object-fit:contain;border-radius:8px}
header h1{font-size:20px;margin:0;letter-spacing:-.02em}
header .h{margin-left:auto;font-variant-numeric:tabular-nums;color:#8E8E96;font-size:15px}
nav{display:flex;gap:8px;padding:12px 20px;overflow-x:auto;background:#101013;border-bottom:1px solid #26262B}
nav button{padding:10px 18px;border-radius:999px;background:#1C1C21;color:#C9C9D1;white-space:nowrap;font-size:16px}
nav button[aria-selected=true]{background:${c};color:#fff;font-weight:600}
main{flex:1;display:flex;min-height:0}
#grille{flex:1;overflow-y:auto;padding:18px;display:grid;gap:14px;
 grid-template-columns:repeat(auto-fill,minmax(180px,1fr));align-content:start}
.carte{background:#17171B;border:1px solid #26262B;border-radius:14px;overflow:hidden;text-align:left;display:flex;flex-direction:column}
.carte:active{transform:scale(.98)}
.carte .ph{aspect-ratio:1;background:#1F1F25;display:grid;place-items:center;color:#4A4A55;font-size:13px}
.carte .ph img{width:100%;height:100%;object-fit:cover;display:block}
.carte .t{padding:12px}
.carte .n{font-weight:600;font-size:16px;line-height:1.25}
.carte .d{font-size:13px;color:#8E8E96;margin-top:4px;line-height:1.35}
.carte .p{margin-top:8px;font-weight:700;font-variant-numeric:tabular-nums;color:${c}}
aside{width:340px;background:#141417;border-left:1px solid #26262B;display:flex;flex-direction:column}
aside h2{font-size:15px;text-transform:uppercase;letter-spacing:.12em;color:#8E8E96;margin:0;padding:18px 18px 10px}
#panier{flex:1;overflow-y:auto;padding:0 18px}
#panier .vide{color:#6A6A74;font-size:15px;padding:20px 0}
.ligne{display:flex;gap:10px;align-items:flex-start;padding:12px 0;border-top:1px solid #26262B}
.ligne:first-child{border-top:0}
.ligne .q{background:${c};color:#fff;min-width:26px;height:26px;border-radius:7px;display:grid;place-items:center;font-weight:700;font-size:14px}
.ligne .i{flex:1;font-size:15px;line-height:1.3}
.ligne .i small{display:block;color:#8E8E96;font-size:13px;margin-top:2px}
.ligne .m{font-variant-numeric:tabular-nums;font-weight:600}
.ligne .x{color:#6A6A74;font-size:20px;line-height:1;padding:0 4px}
#bas{padding:18px;border-top:1px solid #26262B}
#total{display:flex;justify-content:space-between;align-items:baseline;font-size:26px;font-weight:700;font-variant-numeric:tabular-nums}
#total span:first-child{font-size:15px;color:#8E8E96;font-weight:400}
.gros{width:100%;margin-top:14px;padding:18px;border-radius:12px;background:${c};color:#fff;font-size:19px;font-weight:700}
.gros[disabled]{opacity:.35}
dialog{border:0;border-radius:18px;padding:0;background:#17171B;color:#fff;width:min(94vw,520px);max-height:88vh}
dialog::backdrop{background:rgba(0,0,0,.72)}
.dlg{padding:22px}
.dlg h3{margin:0 0 4px;font-size:24px}
.dlg .dd{color:#8E8E96;font-size:15px;margin:0 0 18px}
.opts{display:grid;gap:9px;max-height:38vh;overflow-y:auto;margin-bottom:18px}
.opt{display:flex;align-items:center;gap:12px;padding:13px 15px;border:1px solid #2E2E36;border-radius:11px;font-size:16px}
.opt[aria-pressed=true]{border-color:${c};background:rgba(255,255,255,.04)}
.opt .pp{margin-left:auto;font-variant-numeric:tabular-nums;color:#8E8E96}
.rangee{display:flex;gap:10px}
.rangee button{flex:1;padding:16px;border-radius:12px;font-size:17px;font-weight:600}
.sec{background:#24242B;color:#fff}
#fin{position:fixed;inset:0;background:#0D0D0F;display:none;place-items:center;text-align:center;padding:30px;z-index:9}
#fin.on{display:grid}
#fin .num{font-size:19vh;font-weight:800;line-height:1;color:${c};font-variant-numeric:tabular-nums}
#fin p{font-size:21px;color:#C9C9D1;margin:18px 0 0}
@media (max-width:860px){
 main{flex-direction:column}
 aside{width:auto;border-left:0;border-top:1px solid #26262B;max-height:46%}
 #grille{grid-template-columns:repeat(auto-fill,minmax(140px,1fr))}
}
</style>
</head>
<body>
<div id="app">
  <header>
    ${ens.logo ? '<img src="' + ens.logo + '" alt="">' : ""}
    <h1>${esc(nom)}</h1>
    <span class="h" id="heure"></span>
  </header>
  <nav id="cats" role="tablist"></nav>
  <main>
    <div id="grille"></div>
    <aside>
      <h2>Votre commande</h2>
      <div id="panier"></div>
      <div id="bas">
        <div id="total"><span>Total</span><span id="mt">0,00 €</span></div>
        <button class="gros" id="valider" disabled>Valider ma commande</button>
      </div>
    </aside>
  </main>
</div>

<dialog id="dlg"><div class="dlg">
  <h3 id="d-nom"></h3>
  <p class="dd" id="d-desc"></p>
  <div class="opts" id="d-opts"></div>
  <div class="rangee">
    <button class="sec" id="d-annuler">Annuler</button>
    <button class="gros" id="d-ok" style="margin:0">Ajouter</button>
  </div>
</div></dialog>

<dialog id="dlg2"><div class="dlg">
  <h3>Vous mangez…</h3>
  <p class="dd">Le taux de TVA appliqué en dépend.</p>
  <div class="rangee">
    <button class="gros" style="margin:0" data-ou="place">Sur place</button>
    <button class="gros" style="margin:0" data-ou="emporter">À emporter</button>
  </div>
  <div class="rangee" style="margin-top:10px"><button class="sec" id="d2-annuler">Retour</button></div>
</div></dialog>

<div id="fin"><div>
  <p style="font-size:19px;color:#8E8E96;margin:0">Commande envoyée en cuisine</p>
  <div class="num" id="f-num">—</div>
  <p id="f-txt"></p>
</div></div>

<script>
(function(){
"use strict";
var D = ${JSON.stringify(data)};
var panier = [], cat = 0, enCours = null, opts = [], numero = 1;
var eur = function(n){ return n.toLocaleString("fr-FR",{minimumFractionDigits:2,maximumFractionDigits:2}) + " \\u20AC"; };
var $ = function(s){ return document.querySelector(s); };

function heure(){
  var d = new Date();
  $("#heure").textContent = ("0"+d.getHours()).slice(-2)+":"+("0"+d.getMinutes()).slice(-2);
}
heure(); setInterval(heure, 10000);

function cats(){
  var n = $("#cats"); n.innerHTML = "";
  D.categories.forEach(function(c,i){
    var b = document.createElement("button");
    b.type = "button"; b.setAttribute("role","tab");
    b.setAttribute("aria-selected", i===cat ? "true" : "false");
    b.textContent = c.nom;
    b.onclick = function(){ cat = i; cats(); grille(); };
    n.append(b);
  });
}
function grille(){
  var g = $("#grille"); g.innerHTML = "";
  (D.categories[cat] ? D.categories[cat].produits : []).forEach(function(p){
    var b = document.createElement("button");
    b.type = "button"; b.className = "carte";
    b.innerHTML = '<div class="ph">' + (p.image ? '<img src="'+p.image+'" alt="">' : 'photo') + '</div>' +
      '<div class="t"><div class="n"></div><div class="d"></div><div class="p"></div></div>';
    b.querySelector(".n").textContent = p.nom;
    b.querySelector(".d").textContent = p.desc || "";
    b.querySelector(".p").textContent = eur(p.prix);
    b.onclick = function(){ ouvrir(p); };
    g.append(b);
  });
}
function ouvrir(p){
  enCours = p; opts = [];
  $("#d-nom").textContent = p.nom;
  $("#d-desc").textContent = p.desc || "";
  var z = $("#d-opts"); z.innerHTML = "";
  D.supplements.forEach(function(s){
    var b = document.createElement("button");
    b.type = "button"; b.className = "opt"; b.setAttribute("aria-pressed","false");
    b.innerHTML = '<span></span><span class="pp">+ ' + eur(s.prix) + '</span>';
    b.firstChild.textContent = s.nom;
    b.onclick = function(){
      var i = opts.indexOf(s);
      if (i < 0) { opts.push(s); b.setAttribute("aria-pressed","true"); }
      else { opts.splice(i,1); b.setAttribute("aria-pressed","false"); }
    };
    z.append(b);
  });
  if (!D.supplements.length) z.innerHTML = '<p class="dd" style="margin:0">Aucun supplément disponible.</p>';
  $("#dlg").showModal();
}
$("#d-annuler").onclick = function(){ $("#dlg").close(); };
$("#d-ok").onclick = function(){
  panier.push({ p: enCours, o: opts.slice() });
  $("#dlg").close(); rendre();
};
function total(){
  return panier.reduce(function(t,l){
    return t + l.p.prix + l.o.reduce(function(a,s){ return a + s.prix; },0);
  },0);
}
function rendre(){
  var z = $("#panier"); z.innerHTML = "";
  if (!panier.length) { z.innerHTML = '<p class="vide">Touchez un produit pour commencer.</p>'; }
  panier.forEach(function(l,i){
    var d = document.createElement("div"); d.className = "ligne";
    d.innerHTML = '<span class="q">1</span><span class="i"><b></b><small></small></span>' +
      '<span class="m"></span><button class="x" type="button" aria-label="Retirer">\\u00D7</button>';
    d.querySelector("b").textContent = l.p.nom;
    d.querySelector("small").textContent = l.o.map(function(s){ return "+ " + s.nom; }).join(", ");
    d.querySelector(".m").textContent = eur(l.p.prix + l.o.reduce(function(a,s){ return a+s.prix; },0));
    d.querySelector(".x").onclick = function(){ panier.splice(i,1); rendre(); };
    z.append(d);
  });
  $("#mt").textContent = eur(total());
  $("#valider").disabled = !panier.length;
}
$("#valider").onclick = function(){ $("#dlg2").showModal(); };
$("#d2-annuler").onclick = function(){ $("#dlg2").close(); };
Array.prototype.forEach.call(document.querySelectorAll("[data-ou]"), function(b){
  b.onclick = function(){
    var ou = b.getAttribute("data-ou");
    var taux = ou === "place" ? D.tva.place : D.tva.emporter;
    $("#dlg2").close();
    $("#f-num").textContent = numero;
    $("#f-txt").textContent = "Présentez ce numéro au comptoir. " + eur(total()) +
      " \\u00B7 " + (ou === "place" ? "Sur place" : "\\u00C0 emporter") + " \\u00B7 TVA " + String(taux).replace(".",",") + " %";
    $("#fin").classList.add("on");
    numero = numero >= 99 ? 1 : numero + 1;
    setTimeout(function(){
      $("#fin").classList.remove("on");
      panier = []; rendre();
    }, 7000);
  };
});
cats(); grille(); rendre();
})();
<\/script>
</body>
</html>`;
  }

  function telecharger(nomFichier, contenu) {
    const b = new Blob([contenu], { type: "text/html;charset=utf-8" });
    const u = URL.createObjectURL(b);
    const a = document.createElement("a");
    a.href = u; a.download = nomFichier;
    document.body.append(a); a.click(); a.remove();
    setTimeout(() => URL.revokeObjectURL(u), 4000);
  }

  /* =====================================================================
     Branchements
     ===================================================================== */
  function init() {
    if (!$("#cfg-carte")) return;

    /* Onglets */
    $$("[data-onglet]").forEach(b => b.addEventListener("click", () => {
      const cible = b.dataset.onglet;
      $$("[data-onglet]").forEach(x => x.setAttribute("aria-selected", String(x === b)));
      $$("[data-panneau]").forEach(p => { p.hidden = (p.dataset.panneau !== cible); });
    }));

    /* Enseigne */
    $("#ens-nom").addEventListener("input", e => { E.enseigne.nom = e.target.value; sauver(); majResume(); });
    $("#ens-type").addEventListener("change", e => { E.enseigne.type = e.target.value; sauver(); });
    $("#ens-couleur").addEventListener("input", e => { E.enseigne.couleur = e.target.value; sauver(); });
    $("#ens-logo").addEventListener("change", async e => {
      const f = e.target.files[0]; if (!f) return;
      try { E.enseigne.logo = await redimensionner(f, 180); sauver(); rendreEnseigne(); }
      catch (err) { alerte(err.message); }
    });
    $("#ens-logo-sup").addEventListener("click", () => { E.enseigne.logo = ""; sauver(); rendreEnseigne(); });

    /* Carte : délégation, le markup est reconstruit à chaque rendu */
    $("#cfg-carte").addEventListener("input", e => {
      const t = e.target;
      if (t.dataset.ch) {
        const [ic, ip] = t.dataset.i.split(":").map(Number);
        const p = E.categories[ic].produits[ip];
        p[t.dataset.ch] = t.dataset.ch === "prix" ? Number(t.value) : t.value;
        sauver(); majResume();
      } else if (t.classList.contains("cat__nom")) {
        const ic = [...$$(".cat")].indexOf(t.closest(".cat"));
        E.categories[ic].nom = t.value; sauver();
      }
    });
    $("#cfg-carte").addEventListener("change", async e => {
      const t = e.target;
      if (!t.dataset.img) return;
      const f = t.files[0]; if (!f) return;
      const [ic, ip] = t.dataset.img.split(":").map(Number);
      try {
        E.categories[ic].produits[ip].image = await redimensionner(f);
        sauver(); rendreCarte();
      } catch (err) { alerte(err.message); }
    });
    $("#cfg-carte").addEventListener("click", e => {
      const b = e.target.closest("button"); if (!b) return;
      if (b.dataset.addProd !== undefined) {
        E.categories[+b.dataset.addProd].produits.push({ id: uid(), nom: "", prix: 0, desc: "", image: "" });
      } else if (b.dataset.supProd) {
        const [ic, ip] = b.dataset.supProd.split(":").map(Number);
        E.categories[ic].produits.splice(ip, 1);
      } else if (b.dataset.supCat !== undefined) {
        E.categories.splice(+b.dataset.supCat, 1);
      } else return;
      sauver(); rendreCarte(); majResume();
    });
    $("#add-cat").addEventListener("click", () => {
      E.categories.push({ id: uid(), nom: "Nouvelle catégorie", produits: [] });
      sauver(); rendreCarte();
    });

    /* Suppléments */
    $("#cfg-supplements").addEventListener("input", e => {
      const t = e.target; if (!t.dataset.sch) return;
      const s = E.supplements[+t.dataset.si];
      s[t.dataset.sch] = t.dataset.sch === "prix" ? Number(t.value) : t.value;
      sauver();
    });
    $("#cfg-supplements").addEventListener("click", e => {
      const b = e.target.closest("[data-sup-supp]"); if (!b) return;
      E.supplements.splice(+b.dataset.supSupp, 1); sauver(); rendreCarte();
    });
    $("#add-supp").addEventListener("click", () => {
      E.supplements.push({ id: uid(), nom: "", prix: 0 }); sauver(); rendreCarte();
    });

    /* Site et domaine */
    $$("input[name=solution]").forEach(r => r.addEventListener("change", () => {
      E.site.solution = r.value; sauver(); rendreSite(); majResume();
    }));
    $("#dom-nom").addEventListener("input", e => {
      E.site.domaine = e.target.value.trim().toLowerCase();
      E.site.statut = ""; $("#dom-reponse").textContent = ""; sauver();
    });
    $("#dom-verifier").addEventListener("click", verifierDomaine);

    /* Génération */
    $("#generer").addEventListener("click", () => {
      const nom = (E.enseigne.nom.trim() || "ma-borne")
        .toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, "")
        .replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "");
      telecharger("borne-" + nom + ".html", genererBorne());
      $("#generer-ok").hidden = false;
    });
    $("#apercu").addEventListener("click", () => {
      const f = $("#apercu-cadre");
      f.hidden = false;
      f.srcdoc = genererBorne();
      f.scrollIntoView({ behavior: "smooth", block: "nearest" });
    });
    $("#reinit").addEventListener("click", () => {
      if (!confirm("Repartir de la carte de démonstration ? Vos saisies seront perdues.")) return;
      E = structuredClone(DEPART); sauver();
      rendreEnseigne(); rendreCarte(); rendreSite(); majResume();
    });

    rendreEnseigne(); rendreCarte(); rendreSite(); majResume();

    /* La configuration part avec la commande */
    window.CONFIG_BORNE = () => E;
  }

  function alerte(msg) {
    const z = $("#cfg-erreur");
    if (!z) return;
    z.hidden = false; z.textContent = msg;
    setTimeout(() => { z.hidden = true; }, 6000);
  }

  function majResume() {
    const n = E.categories.reduce((t, c) => t + c.produits.filter(p => p.nom.trim()).length, 0);
    const r = $("#resume-borne");
    if (!r) return;
    const parts = [];
    parts.push(E.enseigne.nom.trim() || "Enseigne à nommer");
    parts.push(n + (n > 1 ? " produits" : " produit"));
    parts.push(E.site.solution === "nouveau"
      ? (E.site.domaine ? "nouveau site : " + E.site.domaine : "nouveau site à créer")
      : "installation sur votre site");
    r.textContent = parts.join(" · ");
  }

  /* ---- Disponibilité du nom de domaine ---------------------------------
     Interrogation du registre via un petit script côté serveur. Si PHP n'est
     pas disponible, on le dit et la vérification se fait à la commande. */
  async function verifierDomaine() {
    const champ = $("#dom-nom");
    const rep = $("#dom-reponse");
    const d = champ.value.trim().toLowerCase();
    if (!/^[a-z0-9][a-z0-9-]{0,61}\.[a-z]{2,24}$/.test(d)) {
      rep.className = "dom-rep dom-rep--non";
      rep.textContent = "Écrivez le nom complet avec son extension, par exemple mon-restaurant.fr";
      return;
    }
    rep.className = "dom-rep";
    rep.textContent = "Vérification auprès du registre…";
    $("#dom-verifier").disabled = true;
    try {
      const r = await fetch("paiement/verifier-domaine.php?d=" + encodeURIComponent(d), { headers: { Accept: "application/json" } });
      const j = await r.json();
      if (j.statut === "libre") {
        rep.className = "dom-rep dom-rep--oui";
        rep.textContent = d + " est libre. Nous pouvons le réserver pour vous, 20 € par an.";
        E.site.statut = "libre";
      } else if (j.statut === "pris") {
        rep.className = "dom-rep dom-rep--non";
        rep.textContent = d + " est déjà enregistré. Essayez une autre orthographe ou une autre extension.";
        E.site.statut = "pris";
      } else {
        rep.className = "dom-rep";
        rep.textContent = "Le registre n’a pas répondu. Nous vérifierons ce nom à la commande.";
        E.site.statut = "inconnu";
      }
    } catch (e) {
      rep.className = "dom-rep";
      rep.textContent = "Vérification automatique indisponible. Nous contrôlerons ce nom à la commande et vous préviendrons s’il est pris.";
      E.site.statut = "inconnu";
    }
    $("#dom-verifier").disabled = false;
    sauver(); majResume();
  }

  document.readyState === "loading"
    ? document.addEventListener("DOMContentLoaded", init, { once: true })
    : init();
})();
