# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with this repository.

## Repository overview

This repository contains independent presentation templates rather than one application:

- `slidev-template/slidev-template/` is the component-based Slidev template. `slides.md` is the deck content; reusable Vue layouts live in `layouts/`, reusable content components live in `components/`, and shared design tokens/global styles live in `styles/`.
- `reveal-template/reveal-template/` is the older standalone Reveal.js template. `slides.html` contains Markdown inside a Reveal Markdown `<textarea>`; `theme.css` owns the tokens, slide variants, and HTML components; `lib/` is the vendored Reveal.js runtime and plugins. It is intentionally usable offline (apart from the optional Google font).
- `reveal-template/revealjs/` is a second, USCC-branded standalone Reveal.js deck. `index.html` contains six explicit sections, `uscc.css` contains the theme/layout, `deck.js` initializes Reveal and wires the toolbar/counter/fullscreen/PDF behavior, and `vendor/` plus `assets/` are local runtime dependencies.
- `FrontendSlide_addon/hcmus/` is a frontend-slides template-pack entry: brand assets plus `design.md`/`preview.md` describing the fixed 1920×1080 HCMUS visual system. `FrontendSlide_addon/convert-template/` documents and implements the PowerPoint/POTX-to-template conversion workflow; its helper script performs OOXML inventory while the final design/asset decisions are made in the docs.

Treat the three presentation directories as separate products. A change to one template does not automatically belong in the others; preserve each template's documented editing workflow.

## Common commands

### Slidev template

Run commands from `slidev-template/slidev-template/`:

```bash
npm install
npm run dev          # development server, normally http://localhost:3030
npm run build        # build the static site into dist/
npm run export       # export PDF; requires Playwright Chromium
npm run export-pptx  # export PPTX as slide images
```

The available scripts and dependencies are defined in that directory's `package.json`. Node.js 18+ is required. There is no test or lint script configured in this repository; do not assume `npm test` or `npm run lint` exists.

### Standalone Reveal.js templates

The classic template under `reveal-template/reveal-template/` remains package-free:
open `slides.html` directly or serve it with a static HTTP server.

The USCC template under `reveal-template/revealjs/` is also package-free at runtime,
but now includes Node standard-library checks/export:

```bash
cd reveal-template/revealjs
node scripts/check-revealjs.mjs
node scripts/export-revealjs.mjs
python -m http.server 8000
```

Open `http://localhost:8000`; use `?check=1` for browser layout diagnostics. The
multi-file source deck is `index.html` plus its `assets/` and `vendor/` directories;
the exporter writes `dist/uscc-reveal.html`. Keep adjacent CSS, images, fonts and
vendor files together when moving or sharing it. PDF output is performed from
Reveal's `?print-pdf` view with the browser's print command. There is no npm install,
runtime dependency, lint suite, or automated browser test runner.

### Template conversion helper

From `FrontendSlide_addon/convert-template/`, the documented inspection command is:

```bash
python scripts/inspect-template-pptx.py <input.pptx-or-potx> <work-dir>
```

The script writes an OOXML inventory and copies raw media into the supplied work directory. Follow the adjacent `SKILL.md` contract: inspect before editing, keep extraction isolated, and update only the target template directory plus the selection index when integrating into a frontend-slides installation.

## Editing conventions by template

- Slidev content changes normally belong in `slides.md`; keep `layouts/`, `components/`, and `styles/` reusable. New layouts need a `<slot />` and should be added to the layout guidance in `AI_PROMPT.md`; new components should follow the existing Vue `<script setup>` plus scoped-style pattern.
- The classic Reveal template keeps the editable deck content inside the marked `<textarea>` in `slides.html`. Avoid changing the surrounding runtime scaffold unless the task is a framework/theme change. Add visual variants in `theme.css` and update `AI_PROMPT.md` when adding a new slide type.
- The USCC Reveal deck uses ordinary HTML sections rather than Markdown. Keep the direct-child structure under `.reveal > .slides`, and update page-number behavior through `deck.js` rather than hard-coding counts when changing the number of sections. Preserve local asset paths and the fixed 1920×1080 canvas.
- HCMUS design documentation uses fixed-stage coordinates and relative asset references. Preserve source brand assets and document layout, layering, motion, scaling, and any approximation in `design.md`; do not replace official artwork with guessed CSS when the source asset is available.

## Documentation and repository rules

- The relevant README is local to each template: read `slidev-template/slidev-template/README.md`, `reveal-template/reveal-template/README.md`, or `reveal-template/revealjs/README.md` before changing that product.
- No `.cursor/rules/`, `.cursorrules`, `.github/copilot-instructions.md`, or repository-wide README was present when this file was created.
- Keep generated output such as Slidev's `dist/` out of source edits unless the task explicitly requests generated artifacts. Do not edit vendored Reveal.js files under `lib/` or `vendor/` for ordinary theme/content changes.

## Project Memory Guidelines

- Trước khi bắt đầu nhiệm vụ: Đọc `memory/activeContext.md` và `memory/progress.md`.
- Sau khi hoàn thành hoặc đổi hướng triển khai: Cập nhật lại `memory/activeContext.md` và `memory/progress.md`.
- Khi cấu trúc dự án, stack hoặc quy ước code thay đổi: Cập nhật `memory/architecture.md`.
