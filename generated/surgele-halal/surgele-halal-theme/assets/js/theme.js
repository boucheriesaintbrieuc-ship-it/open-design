/**
 * Surgelé Halal — Tasty Crousty : JavaScript du thème.
 * Vanilla, sans dépendance, chargé en "defer".
 * - menu mobile ;
 * - mini-panier (tiroir) alimenté par l'API Store de WooCommerce ;
 * - ajout au panier AJAX depuis les listes (repli : lien classique).
 */
(function () {
	'use strict';

	var cfg = window.SH_CONFIG || {};
	var i18n = cfg.i18n || {};
	var nonce = cfg.nonce || '';

	function $(sel, ctx) { return (ctx || document).querySelector(sel); }
	function $$(sel, ctx) { return Array.prototype.slice.call((ctx || document).querySelectorAll(sel)); }
	function fmt(str, val) { return String(str || '').replace(/%[sd]/, val); }
	function decode(html) {
		var doc = new DOMParser().parseFromString(String(html || ''), 'text/html');
		return doc.documentElement.textContent || '';
	}

	/* ---------- Menu mobile ---------- */
	var navToggle = $('[data-sh-nav-toggle]');
	var nav = $('#sh-nav');
	if (navToggle && nav) {
		navToggle.addEventListener('click', function () {
			var open = navToggle.getAttribute('aria-expanded') === 'true';
			navToggle.setAttribute('aria-expanded', open ? 'false' : 'true');
			nav.classList.toggle('is-open', !open);
		});
		document.addEventListener('keydown', function (e) {
			if (e.key === 'Escape' && nav.classList.contains('is-open')) {
				navToggle.setAttribute('aria-expanded', 'false');
				nav.classList.remove('is-open');
				navToggle.focus();
			}
		});
	}

	/* Filtres repliés par défaut sur mobile. */
	var filters = $('.sh-filters__details');
	if (filters && window.matchMedia('(max-width: 899px)').matches) {
		filters.removeAttribute('open');
	}

	/* ---------- Showroom 3D (accueil) ---------- */
	var room = $('[data-sh-showroom]');
	if (room) {
		var items = $$('.sh-showroom__item', room);
		var nameEl = $('[data-sh-name]', room);
		var tagEl = $('[data-sh-tag]', room);
		var cta = $('[data-sh-cta]', room);
		var ctaName = $('[data-sh-cta-name]', room);
		var current = 0;
		var n = items.length;
		function show(i) {
			current = (i + n) % n;
			items.forEach(function (el, k) {
				var rel = (k - current + n) % n;
				el.style.transform = '';
				el.classList.toggle('is-active', rel === 0);
				el.classList.toggle('is-next', rel === 1);
				el.classList.toggle('is-prev', rel === n - 1);
				if (rel === 0) { el.removeAttribute('aria-hidden'); } else { el.setAttribute('aria-hidden', 'true'); }
				// Les images voisines se chargent dès qu'elles deviennent visibles.
				if (rel <= 1 || rel === n - 1) { var im = $('img', el); if (im && im.loading === 'lazy') { im.loading = 'eager'; } }
			});
			var a = items[current];
			if (nameEl) { nameEl.textContent = a.getAttribute('data-name'); }
			if (tagEl) { tagEl.textContent = a.getAttribute('data-tag'); }
			if (cta) { cta.href = a.getAttribute('data-url'); }
			if (ctaName) { ctaName.textContent = a.getAttribute('data-name'); }
		}
		show(0);
		var prev = $('[data-sh-prev]', room);
		var next = $('[data-sh-next]', room);
		if (prev) { prev.addEventListener('click', function () { show(current - 1); }); }
		if (next) { next.addEventListener('click', function () { show(current + 1); }); }
		room.addEventListener('keydown', function (e) {
			if (e.key === 'ArrowLeft') { e.preventDefault(); show(current - 1); }
			if (e.key === 'ArrowRight') { e.preventDefault(); show(current + 1); }
		});
		// Clic sur un produit voisin : il passe au centre.
		items.forEach(function (el, k) {
			el.addEventListener('click', function () { if (k !== current) { show(k); } });
		});
		// Glisser au doigt.
		var x0 = null;
		room.addEventListener('pointerdown', function (e) { x0 = e.clientX; });
		room.addEventListener('pointerup', function (e) {
			if (x0 === null) { return; }
			var dx = e.clientX - x0; x0 = null;
			if (Math.abs(dx) > 40) { show(current + (dx < 0 ? 1 : -1)); }
		});
		// Inclinaison 3D du produit actif selon la souris (désactivée si mouvement réduit).
		var still = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
		if (!still && window.matchMedia('(hover: hover)').matches) {
			var track = $('.sh-showroom__track', room);
			track.addEventListener('pointermove', function (e) {
				var r = track.getBoundingClientRect();
				var px = (e.clientX - r.left) / r.width - 0.5;
				var py = (e.clientY - r.top) / r.height - 0.5;
				var img = $('.is-active img', room);
				if (img) { img.parentNode.style.transform = 'translate(-50%, -50%) rotateY(' + (px * 18).toFixed(1) + 'deg) rotateX(' + (-py * 14).toFixed(1) + 'deg)'; }
			});
			track.addEventListener('pointerleave', function () {
				var act = $('.is-active', room);
				if (act) { act.style.transform = ''; }
			});
		}
	}

	/* ---------- Toast ---------- */
	var toast = $('[data-sh-toast]');
	var toastTimer;
	function say(msg) {
		if (!toast) { return; }
		toast.textContent = msg;
		toast.classList.add('is-visible');
		clearTimeout(toastTimer);
		toastTimer = setTimeout(function () { toast.classList.remove('is-visible'); }, 3500);
	}

	/* ---------- API Store ---------- */
	function api(path, method, body) {
		var headers = { 'Content-Type': 'application/json' };
		if (nonce) { headers.Nonce = nonce; }
		return fetch(cfg.storeApi + path, {
			method: method || 'GET',
			credentials: 'same-origin',
			headers: headers,
			body: body ? JSON.stringify(body) : undefined
		}).then(function (res) {
			var fresh = res.headers.get('Nonce');
			if (fresh) { nonce = fresh; }
			return res.json().then(function (data) {
				if (!res.ok) { var err = new Error(data && data.message ? data.message : 'HTTP ' + res.status); err.status = res.status; throw err; }
				return data;
			});
		});
	}

	function money(minor, cur) {
		var unit = cur && typeof cur.currency_minor_unit === 'number' ? cur.currency_minor_unit : 2;
		var n = parseInt(minor, 10) / Math.pow(10, unit);
		var parts = n.toFixed(unit).split('.');
		var thousand = cur && cur.currency_thousand_separator !== undefined ? cur.currency_thousand_separator : ' ';
		parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, thousand);
		var num = parts.join(cur && cur.currency_decimal_separator ? cur.currency_decimal_separator : ',');
		return (cur ? cur.currency_prefix || '' : '') + num + (cur ? cur.currency_suffix || '' : ' €');
	}

	/* ---------- Compteur ---------- */
	function setCount(count) {
		$$('[data-sh-cart-count]').forEach(function (el) { el.textContent = String(count); });
		$$('[data-sh-cart-toggle]').forEach(function (el) { el.setAttribute('aria-label', fmt(i18n.items, count)); });
	}

	/* ---------- Tiroir mini-panier ---------- */
	var drawer = $('#sh-minicart');
	var body = drawer ? $('[data-sh-cart-body]', drawer) : null;
	var totalEl = drawer ? $('[data-sh-cart-total]', drawer) : null;
	var lastFocus = null;

	function renderCart(cart) {
		if (!body) { return; }
		setCount(cart.items_count || 0);
		body.textContent = '';
		if (!cart.items || !cart.items.length) {
			var p = document.createElement('p');
			p.className = 'sh-drawer__empty';
			p.textContent = i18n.empty;
			body.appendChild(p);
			totalEl.textContent = '';
			return;
		}
		var ul = document.createElement('ul');
		ul.className = 'sh-drawer__items';
		cart.items.forEach(function (item) {
			var li = document.createElement('li');
			li.className = 'sh-drawer__item';
			if (item.images && item.images[0]) {
				var img = document.createElement('img');
				img.src = item.images[0].thumbnail;
				img.alt = '';
				img.width = 64;
				img.height = 64;
				img.loading = 'lazy';
				li.appendChild(img);
			} else {
				var ph = document.createElement('span');
				ph.className = 'sh-drawer__ph';
				ph.setAttribute('aria-hidden', 'true');
				li.appendChild(ph);
			}
			var info = document.createElement('div');
			var name = document.createElement('a');
			name.href = item.permalink;
			name.className = 'sh-drawer__name';
			name.textContent = decode(item.name);
			info.appendChild(name);
			if (item.variation && item.variation.length) {
				var v = document.createElement('p');
				v.className = 'sh-drawer__meta';
				v.textContent = item.variation.map(function (x) { return decode(x.value); }).join(' · ');
				info.appendChild(v);
			}
			var q = document.createElement('p');
			q.className = 'sh-drawer__meta';
			var line = parseInt(item.totals.line_total, 10) + parseInt(item.totals.line_total_tax || 0, 10);
			q.textContent = item.quantity + ' × ' + money(item.prices.price, item.prices) + ' = ' + money(line, item.totals);
			info.appendChild(q);
			li.appendChild(info);
			var rm = document.createElement('button');
			rm.type = 'button';
			rm.className = 'sh-drawer__remove';
			rm.setAttribute('aria-label', fmt(i18n.remove, decode(item.name)));
			rm.textContent = '×';
			rm.addEventListener('click', function () {
				rm.disabled = true;
				api('cart/remove-item', 'POST', { key: item.key }).then(renderCart).catch(function () {
					rm.disabled = false;
					say(i18n.error);
				});
			});
			li.appendChild(rm);
			ul.appendChild(li);
		});
		body.appendChild(ul);
		var t = cart.totals || {};
		var sub = parseInt(t.total_items || 0, 10) + parseInt(t.total_items_tax || 0, 10);
		totalEl.textContent = (i18n.subtotal || 'Sous-total') + ' : ' + money(sub, t);
	}

	function loadCart() {
		if (body) {
			body.textContent = i18n.loading || '';
		}
		return api('cart').then(renderCart);
	}

	function openDrawer() {
		if (!drawer) { return; }
		lastFocus = document.activeElement;
		drawer.hidden = false;
		document.documentElement.classList.add('sh-lock');
		requestAnimationFrame(function () { drawer.classList.add('is-open'); });
		$('.sh-drawer__panel', drawer).focus();
	}

	function closeDrawer() {
		if (!drawer || drawer.hidden) { return; }
		drawer.classList.remove('is-open');
		document.documentElement.classList.remove('sh-lock');
		drawer.hidden = true;
		if (lastFocus && lastFocus.focus) { lastFocus.focus(); }
	}

	if (drawer && cfg.storeApi) {
		$$('[data-sh-cart-toggle]').forEach(function (btn) {
			btn.setAttribute('role', 'button');
			btn.setAttribute('aria-haspopup', 'dialog');
			btn.addEventListener('click', function (e) {
				// Sur les pages panier / commande, le lien mène directement à la page.
				if (document.body.classList.contains('sh-paper-page')) { return; }
				e.preventDefault();
				openDrawer();
				loadCart().catch(function () { window.location.href = btn.href; });
			});
		});
		$$('[data-sh-cart-close]', drawer).forEach(function (el) { el.addEventListener('click', closeDrawer); });
		drawer.addEventListener('keydown', function (e) {
			if (e.key === 'Escape') { closeDrawer(); return; }
			if (e.key !== 'Tab') { return; }
			var focusables = $$('a[href], button:not([disabled]), input, [tabindex="0"]', drawer).filter(function (el) { return el.offsetParent !== null; });
			if (!focusables.length) { return; }
			var first = focusables[0];
			var last = focusables[focusables.length - 1];
			if (e.shiftKey && (document.activeElement === first || document.activeElement === $('.sh-drawer__panel', drawer))) { e.preventDefault(); last.focus(); }
			else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
		});
	}

	/* ---------- Ajout au panier depuis les listes ---------- */
	if (cfg.ajaxCart && cfg.storeApi) {
		document.addEventListener('click', function (e) {
			var btn = e.target.closest ? e.target.closest('a.ajax_add_to_cart[data-product_id]') : null;
			if (!btn) { return; }
			e.preventDefault();
			if (btn.classList.contains('loading')) { return; }
			btn.classList.add('loading');
			btn.setAttribute('aria-busy', 'true');
			api('cart/add-item', 'POST', {
				id: parseInt(btn.getAttribute('data-product_id'), 10),
				quantity: parseInt(btn.getAttribute('data-quantity') || '1', 10)
			}).then(function (cart) {
				btn.classList.remove('loading');
				btn.classList.add('added');
				btn.removeAttribute('aria-busy');
				var card = btn.closest('.product');
				var title = card ? $('.woocommerce-loop-product__title', card) : null;
				renderCart(cart);
				if (drawer) {
					openDrawer();
				} else {
					say(fmt(i18n.added, title ? title.textContent.trim() : ''));
				}
			}).catch(function () {
				// Repli : comportement WooCommerce standard (rechargement).
				window.location.href = btn.href;
			});
		});
	}
})();
