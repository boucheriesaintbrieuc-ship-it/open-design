"""Contrôle de contenu dupliqué entre les pages du site.

Compare le texte visible de chaque page par séquences de 8 mots.
Seuil retenu : plus de 15 % de recouvrement entre deux pages = à réécrire.
Les en-têtes, pieds de page et navigations sont retirés avant comparaison,
sinon elles se recouvrent toutes à 100 % par construction.
"""
import pathlib, re, sys, itertools

BASE = pathlib.Path('/home/user/open-design/site-borne-commande')


def texte_visible(html):
    m = re.search(r'<main\b.*?</main>', html, re.S)
    corps = m.group(0) if m else html
    corps = re.sub(r'<script\b.*?</script>', ' ', corps, flags=re.S)
    corps = re.sub(r'<style\b.*?</style>', ' ', corps, flags=re.S)
    corps = re.sub(r'<svg\b.*?</svg>', ' ', corps, flags=re.S)
    # Les grilles de cartes et les blocs « à lire ensuite » répètent par
    # construction le titre et l'accroche d'autres pages : c'est de la
    # navigation interne, pas du contenu rédactionnel. On les retire.
    corps = re.sub(r'<div class="blog-grille".*?</div>\s*(?=<p|</main|</section|</div)', ' ', corps, flags=re.S)
    corps = re.sub(r'<nav class="art-voisins".*?</nav>', ' ', corps, flags=re.S)
    corps = re.sub(r'<[^>]+>', ' ', corps)
    corps = re.sub(r'&[a-z]+;|&#\d+;', ' ', corps)
    return re.sub(r'\s+', ' ', corps).strip().lower()


def sequences(txt, n=8):
    mots = re.findall(r"[a-zà-ÿ0-9']+", txt)
    return {tuple(mots[i:i + n]) for i in range(max(0, len(mots) - n + 1))}


pages = sorted(p for p in BASE.glob('*.html'))
textes = {}
for p in pages:
    t = texte_visible(p.read_text(encoding='utf-8'))
    if len(t.split()) >= 120:          # on ignore les pages trop courtes (merci, 404)
        textes[p.name] = t

seqs = {n: sequences(t) for n, t in textes.items()}
alertes = []
print('pages comparées :', len(seqs))
for a, b in itertools.combinations(sorted(seqs), 2):
    sa, sb = seqs[a], seqs[b]
    if not sa or not sb:
        continue
    commun = len(sa & sb)
    pct = commun / min(len(sa), len(sb)) * 100
    if pct > 15:
        alertes.append((pct, a, b, commun))

if alertes:
    print('\nRECOUVREMENT AU-DESSUS DE 15 % :')
    for pct, a, b, c in sorted(alertes, reverse=True):
        print(f'  {pct:5.1f} %  {a}  <->  {b}   ({c} séquences communes)')
else:
    print('aucun recouvrement au-dessus de 15 %')

pires = sorted(
    ((len(seqs[a] & seqs[b]) / min(len(seqs[a]), len(seqs[b])) * 100, a, b)
     for a, b in itertools.combinations(sorted(seqs), 2)), reverse=True)[:5]
print('\nles 5 paires les plus proches :')
for pct, a, b in pires:
    print(f'  {pct:5.1f} %  {a[:42].ljust(44)} {b[:42]}')

# Unicité des titres, descriptions et H1
import collections
for champ, motif in (('title', r'<title>(.*?)</title>'),
                     ('description', r'name="description" content="(.*?)"'),
                     ('h1', r'<h1[^>]*>(.*?)</h1>')):
    vals = []
    for p in pages:
        m = re.search(motif, p.read_text(encoding='utf-8'), re.S)
        if m:
            vals.append(re.sub(r'<[^>]+>', '', m.group(1)).strip())
    dbl = [v for v, n in collections.Counter(vals).items() if n > 1]
    print(f'{champ} : {len(vals)} valeurs, doublons = {dbl or "aucun"}')

sys.exit(1 if alertes else 0)
