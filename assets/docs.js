// Steady Documentation : recherche (⌘K, /), thème clair/sombre, tiroir de navigation sur téléphone, sommaire qui suit la lecture.
(() => {
  const $ = (s, r = document) => r.querySelector(s);
  const store = { get: (k) => { try { return localStorage.getItem(k); } catch { return null; } }, set: (k, v) => { try { localStorage.setItem(k, v); } catch { /* navigation privée */ } } };

  // --- Thème : suit l'iPhone ; le bouton force l'inverse de ce qui est affiché, et s'en souvient.
  $('[data-theme-toggle]')?.addEventListener('click', () => {
    const dark = document.documentElement.dataset.theme ? document.documentElement.dataset.theme === 'dark' : matchMedia('(prefers-color-scheme: dark)').matches;
    document.documentElement.dataset.theme = dark ? 'light' : 'dark';
    store.set('theme', document.documentElement.dataset.theme);
  });

  // --- Tiroir de navigation (téléphone)
  const menu = $('[data-menu]');
  const setMenu = (open) => { document.body.classList.toggle('menu-open', open); menu?.setAttribute('aria-expanded', String(open)); };
  menu?.addEventListener('click', () => setMenu(!document.body.classList.contains('menu-open')));
  $('[data-scrim]')?.addEventListener('click', () => setMenu(false));
  $('.side [aria-current]')?.scrollIntoView({ block: 'center' });

  // --- Sommaire de la page : le titre lu est mis en avant.
  const tocLinks = [...document.querySelectorAll('.toc a')];
  if (tocLinks.length && 'IntersectionObserver' in window) {
    const heads = tocLinks.map((a) => document.getElementById(decodeURIComponent(a.hash.slice(1)))).filter(Boolean);
    const mark = (id) => tocLinks.forEach((a) => a.classList.toggle('on', a.hash === `#${id}`));
    const seen = new Map();
    const io = new IntersectionObserver((entries) => {
      entries.forEach((e) => seen.set(e.target.id, e.isIntersecting));
      const current = heads.find((h) => seen.get(h.id)) || heads.filter((h) => h.getBoundingClientRect().top < 120).pop();
      if (current) mark(current.id);
    }, { rootMargin: '-64px 0px -65% 0px' });
    heads.forEach((h) => io.observe(h));
  }

  // --- FAQ : une question visée par l'adresse s'ouvre.
  const openTarget = () => { const t = location.hash && document.getElementById(decodeURIComponent(location.hash.slice(1))); if (t?.tagName === 'DETAILS') t.open = true; };
  openTarget();
  addEventListener('hashchange', openTarget);

  // --- Recherche
  const dialog = $('dialog.search');
  if (!dialog) return;
  const input = $('input', dialog), list = $('.results', dialog);
  let index = null, items = [], sel = 0;
  const norm = (s) => s.toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/['’]/g, ' ');
  const esc = (s) => s.replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' })[c]);
  const load = () => index || (index = fetch('search.json').then((r) => r.json()).then((d) => d.map((e) => ({ ...e, n: norm(`${e.t} ${e.h} ${e.x}`), nh: norm(`${e.t} ${e.h}`) }))));

  // Surligne les mots cherchés sans toucher aux accents du texte affiché.
  function highlight(text, words) {
    const n = norm(text);
    const marks = [];
    words.forEach((w) => { let i = n.indexOf(w); while (i >= 0) { marks.push([i, i + w.length]); i = n.indexOf(w, i + w.length); } });
    if (!marks.length) return esc(text);
    marks.sort((a, b) => a[0] - b[0]);
    let out = '', at = 0;
    marks.forEach(([s, e]) => { if (s < at) return; out += esc(text.slice(at, s)) + '<mark>' + esc(text.slice(s, e)) + '</mark>'; at = e; });
    return out + esc(text.slice(at));
  }
  function snippet(text, words) {
    const n = norm(text), i = Math.min(...words.map((w) => n.indexOf(w)).filter((x) => x >= 0));
    if (!isFinite(i) || i < 60) return text.slice(0, 160);
    return '…' + text.slice(i - 40, i + 120);
  }

  async function run() {
    const q = norm(input.value.trim());
    const words = q.split(/\s+/).filter((w) => w.length > 1);
    if (!words.length) { items = []; list.innerHTML = '<li class="r-empty">Tape un mot : micro, disques, sauvegarde, repos…</li>'; return; }
    const data = await load();
    items = data
      .filter((e) => words.every((w) => e.n.includes(w)))
      .map((e) => ({ e, score: words.reduce((s, w) => s + (e.nh.includes(w) ? 10 : 0) + (norm(e.h).startsWith(w) ? 5 : 0), 0) - (e.h ? 0 : 3) }))
      .sort((a, b) => b.score - a.score)
      .slice(0, 30)
      .map((r) => r.e);
    sel = 0;
    input.removeAttribute('aria-activedescendant');
    if (!items.length) { list.innerHTML = `<li class="r-empty">Aucun résultat pour « ${esc(input.value.trim())} ».</li>`; return; }
    list.innerHTML = items.map((e, i) => `<li role="option" id="r${i}" aria-selected="${i === 0}"><a href="${e.u}">
      <span class="r-path">${esc(e.g)} › ${esc(e.t)}</span><span class="r-title">${highlight(e.h || e.t, words)}</span>
      <span class="r-text">${highlight(snippet(e.x, words), words)}</span></a></li>`).join('');
    input.setAttribute('aria-activedescendant', 'r0');
  }
  const move = (d) => {
    if (!items.length) return;
    sel = (sel + d + items.length) % items.length;
    list.querySelectorAll('li').forEach((li, i) => li.setAttribute('aria-selected', String(i === sel)));
    list.children[sel].scrollIntoView({ block: 'nearest' });
    input.setAttribute('aria-activedescendant', `r${sel}`);
  };
  function open(text = '') {
    if (!dialog.open) dialog.showModal();
    input.value = text;
    input.focus();
    run();
    load();
  }
  input.addEventListener('input', run);
  input.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowDown') { e.preventDefault(); move(1); }
    if (e.key === 'ArrowUp') { e.preventDefault(); move(-1); }
    if (e.key === 'Enter' && items[sel]) { e.preventDefault(); location.href = items[sel].u; dialog.close(); }
  });
  dialog.addEventListener('click', (e) => { if (e.target === dialog || e.target.closest('[data-close]')) dialog.close(); });
  list.addEventListener('click', (e) => { if (e.target.closest('a')) dialog.close(); });
  document.querySelectorAll('[data-search]').forEach((b) => b.addEventListener('click', () => open()));
  const home = $('[data-home-search]');
  home?.addEventListener('input', () => { open(home.value); home.value = ''; });
  home?.addEventListener('focus', () => load());
  addEventListener('keydown', (e) => {
    const typing = /INPUT|TEXTAREA/.test(document.activeElement?.tagName);
    if ((e.key === 'k' && (e.metaKey || e.ctrlKey)) || (e.key === '/' && !typing)) { e.preventDefault(); open(home?.value || ''); }
    if (e.key === 'Escape') setMenu(false);
  });
})();
