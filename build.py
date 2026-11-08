#!/usr/bin/env python3
"""Génère le site de documentation de Steady : src/*.md (export Notion) -> pages HTML à la racine.

Lancement : python3 build.py   (aucune dépendance, Python 3.9+)
Sortie : index.html (accueil), <slug>.html (une page par fichier), search.json (index de recherche).
"""
import html
import json
import re
import unicodedata
from datetime import date
from pathlib import Path

ROOT = Path(__file__).parent
SRC = ROOT / 'src'
APP_URL = 'https://laurent-stp95.github.io/muscu-auto/'
MONTHS = ['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre']

meta = json.loads((SRC / '_pages.json').read_text())
PAGES = sorted(meta['pages'], key=lambda p: p['order'])
IDS = {k.replace('-', '').lower(): v for k, v in meta['ids'].items() if v}
GROUPS = list(dict.fromkeys(p['group'] for p in PAGES))
CUR_TRUE, CUR_PAGE = ' aria-current="true"', ' aria-current="page"'


def typo(markup):
    """Apostrophes typographiques dans le texte affiché, jamais dans les balises ni les attributs."""
    return ''.join(part if part.startswith('<') else re.sub(r"(?<=\w)(?:'|&#x27;)(?=\w)", '’', part) for part in re.split(r'(<[^>]+>)', markup))


def slugify(text):
    text = unicodedata.normalize('NFD', re.sub(r'<[^>]+>', '', text)).encode('ascii', 'ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+', '-', text).strip('-')[:60] or 'section'


def plain(fragment):
    return html.unescape(re.sub(r'<[^>]+>', '', fragment)).strip()


def page_of(url):
    """Lien Notion (mention ou lien direct) -> page du site, ou None."""
    m = re.search(r'([0-9a-f]{32})', url.replace('-', '').lower())
    return IDS.get(m.group(1)) if m else None


def inline(text):
    # Mentions entre pages : liens internes.
    def mention(m):
        slug = page_of(m.group(1))
        return f'<a href="{slug}.html">{m.group(2)}</a>' if slug else m.group(2)
    text = re.sub(r'<mention url="([^"]+)">(.*?)</mention>', mention, text)
    # Liens Markdown [texte](url) : internes si c'est une page Notion de la doc.
    def link(m):
        label, url = m.group(1), m.group(2)
        slug = page_of(url) if 'notion' in url else None
        if slug:
            return f'<a href="{slug}.html">{label}</a>'
        return f'<a href="{html.escape(url)}" rel="noopener">{label}</a>'
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', link, text)
    text = re.sub(r'&(?![a-zA-Z]+;|#\d+;)', '&amp;', text)
    return text.replace('<b>', '<strong>').replace('</b>', '</strong>')


class Doc:
    """Convertit le Markdown de Notion (sous-ensemble utilisé par la doc) en HTML, et relève titres et sections."""

    def __init__(self, slug):
        self.slug, self.toc, self.sections, self.ids = slug, [], [], set()

    def anchor(self, text):
        base = slugify(text)
        a, n = base, 2
        while a in self.ids:
            a, n = f'{base}-{n}', n + 1
        self.ids.add(a)
        return a

    def section(self, level, title, anchor):
        self.sections.append({'h': plain(title), 'a': anchor, 'level': level, 'x': []})

    def text(self, s):
        if self.sections:
            self.sections[-1]['x'].append(plain(s))
        else:
            self.sections.append({'h': '', 'a': '', 'level': 1, 'x': [plain(s)]})

    def render(self, md):
        lines = md.split('\n')
        out, i = [], 0
        while i < len(lines):
            line = lines[i]
            s = line.strip()
            if not s or s == '<table-of-contents />':
                i += 1
            elif s.startswith('<toggle'):
                j = i + 1
                while not lines[j].strip().startswith('</toggle>'):
                    j += 1
                body = [l for l in lines[i + 1:j]]
                q = next(l for l in body if l.strip())
                rest = body[body.index(q) + 1:]
                a = self.anchor(q)
                self.section(3, q, a)
                out.append(f'<details class="qa" id="{a}"><summary><h3>{inline(q.strip())}</h3></summary><div class="answer">{self.render_block(rest)}</div></details>')
                i = j + 1
            elif s.startswith('#'):
                level = len(s) - len(s.lstrip('#'))
                title = s[level:].strip()
                a = self.anchor(title)
                tag = min(max(level, 2), 4)
                self.section(tag, title, a)
                if tag in (2, 3):
                    self.toc.append((tag, plain(title), a))
                out.append(f'<h{tag} id="{a}"><a class="hash" href="#{a}" aria-label="Lien vers cette section">#</a>{inline(title)}</h{tag}>')
                i += 1
            else:
                j = i
                while j < len(lines) and lines[j].strip() and not lines[j].strip().startswith(('#', '<toggle', '<table-of-contents')):
                    j += 1
                out.append(self.render_block(lines[i:j]))
                i = j
        return '\n'.join(out)

    def render_block(self, block):
        """Paragraphes, listes (un niveau d'imbrication) et tableaux, séparés par des lignes vides."""
        out, chunk = [], []
        for line in block + ['']:
            if line.strip():
                chunk.append(line)
                continue
            if not chunk:
                continue
            first = chunk[0].strip()
            if first.startswith('|'):
                out.append(self.table(chunk))
            elif re.match(r'^(- |\d+\. )', first):
                out.append(self.list(chunk))
            else:
                txt = ' '.join(l.strip() for l in chunk)
                self.text(txt)
                out.append(f'<p>{inline(txt)}</p>')
            chunk = []
        return '\n'.join(out)

    def list(self, chunk):
        ordered = bool(re.match(r'^\d+\. ', chunk[0].strip()))
        tag = 'ol' if ordered else 'ul'
        items, sub = [], None
        for line in chunk:
            nested = line.startswith((' ', '\t'))
            m = re.match(r'^\s*(?:- |\d+\. )(.*)$', line)
            content = m.group(1) if m else line.strip()
            self.text(content)
            if nested and items:
                items[-1][1].append(content)
            elif m:
                items.append([content, []])
            elif items:
                items[-1][0] += ' ' + line.strip()
        html_items = []
        for text, children in items:
            kids = ''
            if children:
                kids = '<ul>' + ''.join(f'<li>{inline(c)}</li>' for c in children) + '</ul>'
            html_items.append(f'<li>{inline(text)}{kids}</li>')
        return f'<{tag}>' + ''.join(html_items) + f'</{tag}>'

    def table(self, chunk):
        rows = [[c.strip() for c in l.strip().strip('|').split('|')] for l in chunk if not re.match(r'^\|\s*:?-', l.strip())]
        head, body = rows[0], rows[1:]
        for r in rows:
            self.text(' · '.join(r))
        th = ''.join(f'<th scope="col">{inline(c)}</th>' for c in head)
        trs = ''.join('<tr>' + ''.join(f'<td>{inline(c)}</td>' for c in r) + '</tr>' for r in body)
        return f'<div class="table"><table><thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table></div>'


def front(text):
    m = re.match(r'^---\n(.*?)\n---\n', text, re.S)
    fm = {}
    for line in m.group(1).split('\n'):
        k, v = line.split(':', 1)
        fm[k.strip()] = v.strip().strip('"')
    return fm, text[m.end():]


ICON = {
    'search': '<path d="M10.5 18a7.5 7.5 0 1 1 0-15 7.5 7.5 0 0 1 0 15ZM21 21l-4.6-4.6"/>',
    'menu': '<path d="M4 7h16M4 12h16M4 17h16"/>',
    'sun': '<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/>',
    'moon': '<path d="M20 14.5A8.5 8.5 0 0 1 9.5 4a8.5 8.5 0 1 0 10.5 10.5Z"/>',
    'arrow': '<path d="M5 12h14M13 6l6 6-6 6"/>',
    'back': '<path d="M19 12H5M11 6l-6 6 6 6"/>',
    'ext': '<path d="M14 4h6v6M20 4l-9 9M18 14v5a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V7a1 1 0 0 1 1-1h5"/>',
    'close': '<path d="M6 6l12 12M18 6 6 18"/>',
}


def icon(name, cls='icon'):
    return f'<svg class="{cls}" viewBox="0 0 24 24" aria-hidden="true">{ICON[name]}</svg>'


def header(current_group=None, home=False):
    parts = [('Démarrer', 'Démarrer'), ("S'entraîner", "S'entraîner"), ('Progrès', 'Suivre tes progrès'), ('Aide', 'Aide')]
    first = {g: next(p['slug'] for p in PAGES if p['group'] == g) for g in GROUPS}
    links = ''.join(f'<a href="{first[g]}.html"{CUR_TRUE if g == current_group else ""}>{label}</a>' for label, g in parts if g in first)
    search = '' if home else f'<button class="search-btn" type="button" data-search>{icon("search")}<span>Rechercher</span><kbd>⌘ K</kbd></button>'
    menu = '' if home else f'<button class="icon-btn menu-btn" type="button" data-menu aria-label="Ouvrir le sommaire" aria-expanded="false">{icon("menu")}</button>'
    return f'''<header class="top">
  {menu}<a class="brand" href="index.html"><img src="icon.png" alt="" width="28" height="28"><span>Steady</span><span class="brand-sub">Documentation</span></a>
  <nav class="top-links" aria-label="Parties">{links}</nav>
  <div class="top-tools">{search}<button class="icon-btn" type="button" data-theme-toggle aria-label="Changer de thème">{icon("moon", "icon only-light")}{icon("sun", "icon only-dark")}</button>
  <a class="app-link" href="{APP_URL}"><span class="long">Ouvrir l'appli</span><span class="short">Appli</span>{icon("ext")}</a></div>
</header>'''


def page_html(title, description, body, *, slug='index', group=None, home=False):
    canonical = 'index.html' if home else f'{slug}.html'
    return f'''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{html.escape(title)}{'' if home else ' · Steady Documentation'}</title>
<meta name="description" content="{html.escape(description)}">
<meta name="theme-color" content="#f2f2f7" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#000000" media="(prefers-color-scheme: dark)">
<link rel="icon" href="icon.png">
<link rel="apple-touch-icon" href="icon.png">
<link rel="stylesheet" href="assets/style.css">
<script>try{{var t=localStorage.getItem('theme');if(t)document.documentElement.dataset.theme=t}}catch(e){{}}</script>
</head>
<body class="{'home' if home else 'doc'}">
<a class="skip" href="#contenu">Aller au contenu</a>
{header(group, home)}
{body}
<dialog class="search" aria-label="Rechercher dans la documentation">
  <div class="search-box">{icon("search")}<input type="search" placeholder="Rechercher dans la documentation" autocomplete="off" spellcheck="false" aria-label="Rechercher" role="combobox" aria-expanded="true" aria-controls="resultats" aria-autocomplete="list"><button class="icon-btn" type="button" data-close aria-label="Fermer">{icon("close")}</button></div>
  <ul class="results" id="resultats" role="listbox" aria-label="Résultats"></ul>
  <p class="search-foot"><span><kbd>↑</kbd><kbd>↓</kbd> naviguer</span><span><kbd>↵</kbd> ouvrir</span><span><kbd>Échap</kbd> fermer</span></p>
</dialog>
<script src="assets/docs.js" defer></script>
</body>
</html>
'''


def sidebar(current):
    groups = []
    for g in GROUPS:
        items = ''.join(
            f'<li><a href="{p["slug"]}.html"{CUR_PAGE if p["slug"] == current else ""}>{html.escape(p["title"])}</a></li>'
            for p in PAGES if p['group'] == g)
        groups.append(f'<li><p class="side-group">{html.escape(g)}</p><ul>{items}</ul></li>')
    return f'<nav class="side" aria-label="Sommaire de la documentation"><ul>{"".join(groups)}</ul></nav>'


def updated():
    # Date du contenu (dernier export de Notion), pas de la génération : reconstruire ne la change pas.
    d = date.fromtimestamp(max(f.stat().st_mtime for f in SRC.glob('*.md')))
    return f'{d.day} {MONTHS[d.month - 1]} {d.year}'


def build():
    index, built = [], []
    for n, p in enumerate(PAGES):
        fm, md = front((SRC / f'{p["slug"]}.md').read_text())
        doc = Doc(p['slug'])
        content = doc.render(md)
        # Premier paragraphe = chapeau de la page : avant le sommaire replié, pour lire d'abord de quoi il s'agit.
        lead = ''
        m = re.match(r'\s*<p>(.*?)</p>\n?', content, re.S)
        if m:
            lead, content = f'<p class="lead">{m.group(1)}</p>', content[m.end():]
        prev_p, next_p = (PAGES[n - 1] if n else None), (PAGES[n + 1] if n + 1 < len(PAGES) else None)
        nav = '<nav class="pager" aria-label="Pages précédente et suivante">'
        nav += f'<a class="prev" href="{prev_p["slug"]}.html"><span>{icon("back")}Précédent</span><strong>{html.escape(prev_p["title"])}</strong></a>' if prev_p else '<span></span>'
        nav += f'<a class="next" href="{next_p["slug"]}.html"><span>Suivant{icon("arrow")}</span><strong>{html.escape(next_p["title"])}</strong></a>' if next_p else '<span></span>'
        nav += '</nav>'
        toc_items = ''.join(f'<li class="l{lvl}"><a href="#{a}">{html.escape(t)}</a></li>' for lvl, t, a in doc.toc)
        toc = f'<nav class="toc" aria-label="Sur cette page"><p>Sur cette page</p><ul>{toc_items}</ul></nav>' if doc.toc else ''
        toc_inline = f'<details class="toc-inline"><summary>Sur cette page</summary><ul>{toc_items}</ul></details>' if doc.toc else ''
        body = f'''<div class="shell">
{sidebar(p["slug"])}
<div class="scrim" data-scrim></div>
<main id="contenu" class="article">
  <h1>{html.escape(p["title"])}</h1>
  {lead}
  {toc_inline}
  <div class="prose{' faq' if p['slug'] == 'faq' else ''}">
{content}
  </div>
  {nav}
  <footer class="foot"><span>Mis à jour le {updated()}</span><a href="{APP_URL}">Ouvrir Steady</a></footer>
</main>
<aside class="rail">{toc}</aside>
</div>'''
        (ROOT / f'{p["slug"]}.html').write_text(typo(page_html(p['title'], p['description'], body, slug=p['slug'], group=p['group'])))
        built.append(p['slug'])
        index.append({'t': typo(p['title']), 'g': typo(p['group']), 'u': f'{p["slug"]}.html', 'h': '', 'x': typo(p['description'])})
        for s in doc.sections:
            if s['h'] or s['x']:
                index.append({'t': typo(p['title']), 'g': typo(p['group']), 'u': f'{p["slug"]}.html' + (f'#{s["a"]}' if s['a'] else ''), 'h': typo(s['h']), 'x': typo(' '.join(s['x'])[:600])})
        if p['slug'] == 'faq':
            faq = [s for s in doc.sections if s['level'] == 3]
    (ROOT / 'search.json').write_text(json.dumps(index, ensure_ascii=False, separators=(',', ':')))
    build_home(faq)
    print(f'{len(built)} pages, {len(index)} entrées de recherche')


# Questions mises en avant sur l'accueil : celles qu'on se pose en séance ou au premier lancement,
# pas les « Que veut dire… » qui expliquent un message précis.
FEATURED = ['micro', 'charge', 'écran', 'sauvegard', 'caméra', 'matériel', 'repos', 'séance']
# Une ligne par partie, sur la carte de l'accueil.
PART_LINES = {
    'Démarrer': "Installer l'appli sur l'iPhone, régler ton matériel, tes jours et les notifications.",
    "S'entraîner": 'Ta semaine, la séance série par série, la voix, la caméra et la TV.',
    'Suivre tes progrès': 'Le bilan de la semaine, tes courbes, tes records et chaque exercice.',
    'Comprendre': 'Comment Steady construit ton programme et choisit tes charges.',
    'Compte et données': 'Ton journal reste sur ton iPhone : le sauvegarder, le restaurer, tes réglages.',
    'Aide': 'Les questions fréquentes, les messages de l’appli et le lexique.',
}


def build_home(faq):
    parts = []
    for n, g in enumerate(GROUPS, 1):
        pages = [p for p in PAGES if p['group'] == g]
        links = ''.join(f'<a href="{p["slug"]}.html">{html.escape(p["title"])}</a>' for p in pages)
        parts.append(f'''<section class="part">
  <a class="part-head" href="{pages[0]["slug"]}.html"><span class="part-num">{n}</span><span class="part-name">{html.escape(g)}</span></a>
  <p class="part-line">{html.escape(PART_LINES.get(g, ''))}</p>
  <p class="part-pages">{links}</p>
</section>''')
    chosen, seen = [], set()
    for word in FEATURED:
        q = next((s for s in faq if word in s['h'].lower() and s['a'] not in seen and not s['h'].startswith('Que veut dire')), None)
        if q:
            seen.add(q['a'])
            chosen.append(q)
    chips = ''.join(f'<li><a href="faq.html#{q["a"]}">{html.escape(q["h"])}</a></li>' for q in chosen[:6])
    body = f'''<main id="contenu" class="landing">
  <section class="hero">
    <h1>Comment <span class="nobr">pouvons-nous</span> t'aider ?</h1>
    <p class="lead">Tout sur Steady, l'appli de musculation à domicile : l'installer, suivre une séance, comprendre tes charges.</p>
    <label class="big-search">{icon("search")}<input type="search" placeholder="Rechercher : micro, disques…" autocomplete="off" aria-label="Rechercher dans la documentation" data-home-search><kbd>⌘ K</kbd></label>
  </section>
  <div class="parts">{''.join(parts)}</div>
  <section class="questions" aria-labelledby="faq-titre">
    <h2 id="faq-titre">Questions fréquentes</h2>
    <ul>{chips}</ul>
    <a class="more" href="faq.html">Toutes les questions{icon("arrow")}</a>
  </section>
  <footer class="foot"><span>Mis à jour le {updated()}</span><a href="{APP_URL}">Ouvrir Steady</a></footer>
</main>'''
    (ROOT / 'index.html').write_text(typo(page_html('Steady · Documentation', "Toute la documentation de Steady, l'appli de musculation à domicile : installer, s'entraîner, suivre tes progrès.", body, home=True)))


if __name__ == '__main__':
    build()
