---
version: 1
slug: "index-html"
primary_target: "index.html"
related_targets: []
---

# Steady docs (index.html + every page)

Scope: the whole documentation site, Read mode. Audience: anyone discovering or using Steady, on iPhone as much as desktop. Job: find the answer to a question about the app in seconds. Source: 18 Notion pages in src/, 6 parts. Constraints: static, no framework, French, tutoiement, no emoji, no em dash, app labels in bold. User-pinned: sidebar navigation, « Sur cette page », search, light/dark, previous/next, quality bar of the Anthropic docs, Steady identity (orange #c8441d, iOS sober).

## Direction contract

THESIS: The help centre opens on the reader's question, not on a table of contents: one large search, the six parts, the questions people actually ask. It refuses the docs-site default of landing straight inside page one with a wall of sidebar.

OWN-WORLD: Steady's iOS grouped world: #f2f2f7 ground, white cards with 16px radius, system font, orange #c8441d only for part numerals, the current page, links and focus. Dark mirrors the app (#000 ground, #1c1c1e cards, #ff8a5c ink).

STORY: The reader types or picks a part, lands on a page with the part named above the title, reads a calm column, uses « Sur cette page » to jump, and leaves through previous/next or search.

FIRST VIEWPORT: Home: slim white header (icon, Steady Documentation, part links, Ouvrir l'appli), centred title « Comment pouvons-nous t'aider ? », lead, 680px search field with ⌘K, then a 3×2 grid of part cards (orange numeral and part name, page title, one line), then frequent-question chips. Pages: same header with search, left sidebar of parts and pages, 70ch column, right « Sur cette page ».

FORM: Help centre, search first; position 7 of 7 on my ordered list; seed:1b9ab007b687aa6f

FINISH: unreviewed and undocumented is unfinished; this build ends with the finish review, the verdict, DESIGN.md, and every shipping raster carrying its provenance
