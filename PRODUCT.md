# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Stack

Static HTML/CSS/JS, no framework, no runtime dependency. A small Python build script (`build.py`) turns the Markdown pages in `src/` (exported from Notion) into HTML in the repository root. Published with GitHub Pages at laurent-stp95.github.io/steady-docs.

## Users

Anyone discovering or using Steady (public audience, confirmed 2026-11-08): people who train at home with their own equipment and want to know how the app works before or while using it. First real reader is Laurent, the author, and people he shares the app with. Readers come on an iPhone (often from the app's Réglages) as much as on a desktop.

## Product Purpose

The user documentation of Steady: explain every screen, rule and message of the app in plain French so a reader can install it, set it up, run a session and understand why the app proposes what it proposes. Success: a reader finds the answer to a question in seconds (navigation, search, « Sur cette page »), and the docs read like a well-made product manual, at the level of the best developer documentation sites.

## Positioning

Steady is a free personal web app (PWA installed on iPhone) for home strength training: it builds the weekly programme from the user's own equipment (Smith machine, dumbbells, bands, kettlebell…), picks the load for every set, counts reps with the phone camera, takes voice commands, and can project the session on a TV with the iPhone as a remote. All data stays on the device.

## Operating Context

- Content source: 18 Notion pages in French (« Application » and its sub-pages), grouped in parts (Démarrer, S'entraîner, Suivre tes progrès, Comprendre, Compte et données, Aide), including a FAQ (55 questions) and a Lexique (48 terms). Notion stays the editing place; the site is regenerated from an export.
- The app lives at laurent-stp95.github.io/muscu-auto ; a separate showcase landing exists at laurent-stp95.github.io/steady. The app's Réglages will link to the docs.

## Capabilities and Constraints

- French only, tutoiement, as in the app.
- Must work offline-tolerant and fast on a phone: static pages, no web fonts required, no tracking.
- Readable in light and dark (follows the system).
- Pages reference app labels exactly (bold), spoken phrases between « », rules phrased « Action : résultat ».

## Brand Commitments

- Name: Steady. App accent orange #c8441d (dark-mode ink #ff8a5c), iOS-sober visual language (system font, grouped cards), app icon `icon-180.png` in the app repo.
- Writing rules from the author: no emoji, no em dash (cadratin), plain language for everyone, exact UI labels in bold, « Action : résultat ».
- Quality bar named by the author: the Anthropic documentation site (structure and finish), without copying Anthropic's brand.

## Evidence on Hand

- The 18 exported pages in `src/` (verbatim Notion content).
- App screens can be captured from the running app (localhost or the published app) if illustrations are needed.
- No testimonials, user counts or press: none may be invented.

## Product Principles

1. Find the answer fast: every page is reachable in two taps and searchable.
2. Say exactly what the app says: labels, messages and phrases match the app word for word.
3. Plain before complete: a beginner understands the first paragraph of each page; detail comes after.
4. Same voice as the app: tutoiement, calm, precise, no hype.

## Accessibility & Inclusion

WCAG AA contrast in both themes, keyboard navigation for sidebar, search and table of contents, respects text size settings and reduced motion.
