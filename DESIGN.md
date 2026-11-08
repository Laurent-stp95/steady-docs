---
name: Steady Documentation
description: The user manual of Steady, in the app's own iOS grouped world.
colors:
  accent: "#c8441d"
  accent-ink: "#a83a17"
  accent-dark: "#ff8a5c"
  ground: "#f2f2f7"
  surface: "#ffffff"
  ink: "#1c1c1e"
  body: "#2c2c2e"
  muted: "#5e5e63"
  faint: "#6e6e73"
  line: "#e2e2e7"
  line-strong: "#d1d1d6"
  ground-dark: "#000000"
  surface-dark: "#111113"
  card-dark: "#1c1c1e"
  ink-dark: "#f5f5f7"
  body-dark: "#e5e5ea"
  muted-dark: "#a1a1a6"
  line-dark: "#2c2c2e"
  line-strong-dark: "#3a3a3c"
typography:
  display:
    fontFamily: "-apple-system, BlinkMacSystemFont, SF Pro Text, Segoe UI, system-ui, sans-serif"
    fontSize: "clamp(32px, 5vw, 48px)"
    fontWeight: 700
    lineHeight: 1.12
    letterSpacing: "-0.025em"
  headline:
    fontFamily: "-apple-system, BlinkMacSystemFont, SF Pro Text, Segoe UI, system-ui, sans-serif"
    fontSize: "clamp(30px, 4vw, 38px)"
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: "-0.022em"
  title:
    fontFamily: "-apple-system, BlinkMacSystemFont, SF Pro Text, Segoe UI, system-ui, sans-serif"
    fontSize: "24px"
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: "-0.015em"
  subtitle:
    fontFamily: "-apple-system, BlinkMacSystemFont, SF Pro Text, Segoe UI, system-ui, sans-serif"
    fontSize: "19px"
    fontWeight: 700
    lineHeight: 1.35
    letterSpacing: "-0.01em"
  lead:
    fontFamily: "-apple-system, BlinkMacSystemFont, SF Pro Text, Segoe UI, system-ui, sans-serif"
    fontSize: "18px"
    fontWeight: 400
    lineHeight: 1.55
  body:
    fontFamily: "-apple-system, BlinkMacSystemFont, SF Pro Text, Segoe UI, system-ui, sans-serif"
    fontSize: "16.5px"
    fontWeight: 400
    lineHeight: 1.7
  nav:
    fontFamily: "-apple-system, BlinkMacSystemFont, SF Pro Text, Segoe UI, system-ui, sans-serif"
    fontSize: "14.5px"
    fontWeight: 400
    lineHeight: 1.4
  label:
    fontFamily: "-apple-system, BlinkMacSystemFont, SF Pro Text, Segoe UI, system-ui, sans-serif"
    fontSize: "13px"
    fontWeight: 650
rounded:
  s: "8px"
  m: "12px"
  l: "16px"
  full: "999px"
spacing:
  top-bar: "60px"
  sidebar: "272px"
  rail: "232px"
  measure: "70ch"
  gutter: "20px"
components:
  button-app:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.surface}"
    rounded: "{rounded.full}"
    padding: "7px 14px"
  search-field-hero:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.l}"
    height: "60px"
    width: "680px"
  search-button:
    backgroundColor: "{colors.ground}"
    textColor: "{colors.faint}"
    rounded: "10px"
    height: "36px"
    width: "260px"
  part-card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.l}"
    padding: "20px 22px 18px"
  question-chip:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    padding: "9px 16px"
  sidebar-link:
    textColor: "{colors.muted}"
    typography: "{typography.nav}"
    rounded: "{rounded.s}"
    padding: "6px 10px"
  sidebar-link-current:
    backgroundColor: "rgb(200 68 29 / .09)"
    textColor: "{colors.accent-ink}"
    rounded: "{rounded.s}"
    padding: "6px 10px"
  pager-card:
    textColor: "{colors.ink}"
    rounded: "{rounded.m}"
    padding: "16px 18px"
---

# Design System: Steady Documentation

## Overview

**Creative North Star: "The App's Own Manual"**

The documentation lives in the same world as the Steady app: the iOS grouped look, the system font, white cards on a pale grey ground, and one orange that only ever marks where you are or where you can go. It should feel like a Réglages screen that grew into a manual: calm, dense with real answers, no decoration competing with the text.

Two surfaces, two grounds. The home is a help centre: grouped grey ground (#f2f2f7, black in dark) with white part cards and question chips around one large search field. Content pages are for long reading, so they sit on a plain reading surface (white, #111113 in dark) with a sticky sidebar, a 70ch column and a « Sur cette page » rail. Light and dark follow the iPhone; a header toggle forces either.

The part a page belongs to is shown by the header pill and the sidebar group, never by a label stacked above the title.

**Key Characteristics:**
- iOS grouped world: grey ground, white 16px cards, hairline separators.
- System font stack only; no web fonts.
- One orange, used as a pointer (numerals, current page, links, focus, caret), never as decoration.
- Home on grouped ground, content pages on a plain reading surface.
- Flat by default; the only shadows belong to the hero search, the search dialog and the mobile drawer.

## Colors

A near-neutral iOS greyscale carrying a single orange pointer, mirrored for dark mode.

### Primary
- **Steady Orange** (accent): filled "Ouvrir l'appli" button, part numerals, focus ring, active TOC rule, caret, pager hover border, accent-colour for native controls.
- **Deep Orange Ink** (accent-ink): orange as text on light grounds (links, current sidebar page, ordered-list numerals, hovered part names), darker than the accent so small text holds AA.
- **Ember Ink** (accent-dark): the dark-mode orange, both fill and ink; the filled app button flips its label to ink (#1c1c1e) on it.
- Tints derived from the accent: soft wash at 9% (12% dark) behind the current sidebar page, the selected search result and the hero search focus halo; mark at 16% (22% dark) for text selection and search highlights.

### Neutral
- **Grouped Ground** (ground / ground-dark): the home background and table header rows.
- **Card White** (surface / surface-dark): the header (at 86% with blur), the sidebar, and the whole background of content pages.
- **Raised Card** (surface in light, card-dark in dark): part cards, question chips, hero search, search dialog.
- **Ink** (ink / ink-dark): titles, strong text, first table column.
- **Body** (body / body-dark): prose and part page lists.
- **Muted** (muted / muted-dark): leads, sidebar and TOC links, secondary lines.
- **Faint** (faint; muted-dark in dark): placeholders, list bullets, footer, kbd, heading anchors.
- **Hairline** (line / line-dark) and **Strong Hairline** (line-strong / line-strong-dark): separators, h2 rules, table and pager borders; the strong one for field borders and scrollbars.
- iOS fills for hover (rgb(118 118 128 / .08), .16 dark) and pressed/current pills (rgb(118 118 128 / .12), .24 dark).

### Named Rules
**The Pointer Rule.** Orange only marks a part numeral, the current page, a link, focus or the caret, plus the single filled "Ouvrir l'appli" button. No orange backgrounds, borders, icons or rules for decoration.

**The Two Grounds Rule.** The help-centre home sits on the grouped ground with raised cards; content pages sit on the plain reading surface. Do not put a long-reading page on grey, and do not put the home cards on white.

## Typography

**Display Font:** system stack (-apple-system, SF Pro Text, Segoe UI, system-ui)
**Body Font:** the same stack

**Character:** one family, iOS-native; hierarchy comes from size, weight (400 / 600 / 650 / 700) and slight negative tracking on headings, not from a second face.

### Hierarchy
- **Display** (700, 32 to 48px, 1.12, -0.025em): the home title only, balanced.
- **Headline** (700, 30 to 38px, 1.15, -0.022em): page titles.
- **Title** (700, 24px, 1.3): h2, preceded by a hairline rule and 52px of air.
- **Subtitle** (700, 19px, 1.35): h3; FAQ questions use 600 at 17px.
- **Lead** (400, 18px, 1.55, muted, 64ch): the opening paragraph of each page; 19px on the home.
- **Body** (400, 16.5px, 1.7, 70ch; 16px on phone): prose. Bold is 600 in ink, used for exact app labels.
- **Nav** (400, 14.5px, 1.4): sidebar links, part page lists (14px), TOC (14px).
- **Label** (650, 13px): sidebar group names and the « Sur cette page » heading. Sentence case, no tracking.

### Named Rules
**The No Kicker Rule.** No eyebrow or kicker label above a title. The part is already named by the header pill and the sidebar group.

**The System Face Rule.** System font stack only; no web font is loaded (fast and offline-tolerant on a phone). Numerals that align (part numbers, ordered lists) use tabular figures.

## Layout

Home: a centred column (max 1120px, 20px gutters) with the hero (title, lead, 680px search), a 3-column grid of six part cards (14px gap; 2 columns 861 to 1080px; 1 column on phone), then question chips.

Pages: a three-column shell (max 1440px): 272px sticky sidebar, a reading column capped at 70ch with fluid padding (24 to 72px), and a 232px « Sur cette page » rail sticky under the 60px header. At 1200px and below the rail disappears and the table of contents becomes a collapsible block under the lead; the header part links hide. At 860px and below the header shrinks to 56px, the sidebar becomes a left drawer (max 320px, 86vw) over a 30% black scrim, the search button collapses to an icon, and "Ouvrir l'appli" shortens to "Appli".

Rhythm: paragraphs and blocks 16px apart, 10px under a heading, h2 52px above, h3 36px, list items 6px. Previous/next pager sits 56px under the content, footer 40px under that.

## Elevation & Depth

Flat by default: depth comes from the grouped ground against white cards and from hairlines. Shadows are reserved for things that float above the page.

### Shadow Vocabulary
- **Float** (`0 1px 2px rgb(0 0 0 / .04), 0 8px 28px rgb(0 0 0 / .06)`; dark `.4` / `.5`): the hero search field and the open mobile drawer.
- **Dialog** (`0 24px 80px rgb(0 0 0 / .28)`): the search dialog, over a 32% black backdrop with 2px blur.
- **Glass header**: surface at 86% with `saturate(180%) blur(16px)`, a hairline below.

### Named Rules
**The Flat Card Rule.** Part cards and chips carry no shadow and no border; the ground does the separating.

## Shapes

Continuous iOS rounding: 8px for list rows and sidebar links, 10px for header controls, 12px for tables, pager cards, TOC block and search results, 16px for part cards, hero search and dialog, full pills for header links, chips and the app button. Lines are always 1px hairlines. Disclosure chevrons are drawn as two rotated 2px borders, not glyphs; icons are inline 24px-grid stroke SVGs at 1.8px.

## Components

### Buttons
- **App button:** filled orange pill (button-app), white 14px/600 label with an external-link icon; dark mode puts ink on Ember. Hover brightens by 6%. It is the only filled button.
- **Icon buttons:** 36px, 10px radius, muted icon, iOS hover fill.

### Search
- **Hero field:** 60px (54px phone), 16px radius, strong hairline, raised card with Float shadow; on focus the border turns orange with a 4px soft-orange halo. ⌘K hint in a kbd.
- **Header button:** 260px grey-ground pill-rectangle with "Rechercher" and ⌘K; icon only on phone.
- **Dialog:** 640px, results as 12px-radius rows; the selected row takes the soft orange wash; matches highlighted with the mark tint.

### Cards / Containers
- **Part card:** raised white, 16px radius, no border or shadow; orange tabular numeral then part name (20px/650), a muted one-liner, and the part's pages as inline links.
- **Question chip:** raised pill, 15px ink text, orange-ink on hover.
- **Pager card:** 1px hairline, 12px radius, muted "Précédent / Suivant" over the ink title; border turns orange on hover.
- **Table:** 1px hairline frame at 12px radius, grey-ground header row, hairline row separators, 15px text.

### Navigation
- **Header pills:** muted 15px links; current part gets the iOS fill in ink.
- **Sidebar:** 13px/650 group names, 14.5px muted links on 8px rows; the current page gets the soft orange wash, orange ink, weight 600.
- **Sur cette page:** a 1px left rule per link; the active section turns the rule orange and the text orange ink; h3 entries indented.
- **FAQ disclosure:** questions as rows with a hairline below and a rotating chevron; question text turns orange ink on hover.

## Do's and Don'ts

### Do:
- **Do** keep the home on the grouped ground (#f2f2f7 / #000) and content pages on the plain reading surface (#fff / #111113).
- **Do** limit orange to part numerals, the current page, links, focus, caret and the one app button.
- **Do** use the system font stack and tabular figures for numbering.
- **Do** cap reading text at 70ch and separate h2 sections with a hairline.
- **Do** keep cards flat; give shadows only to the hero search, the dialog and the drawer.

### Don't:
- **Don't** put a kicker or eyebrow label above a title.
- **Don't** use orange as decoration (backgrounds, dividers, icon tint, badges).
- **Don't** load web fonts.
- **Don't** add borders or shadows to part cards or chips.
- **Don't** use emoji or glyph characters as icons; icons are inline stroke SVGs.
