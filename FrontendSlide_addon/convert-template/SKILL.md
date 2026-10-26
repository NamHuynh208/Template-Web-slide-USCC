---
name: convert-template
description: Use when converting a PowerPoint PPTX or POTX visual template into a frontend-slides bold-template-pack template, especially when the user mentions template assets, preview.md, design.md, selection-index.json, Slide Master, or reusable slide styles.
---

# Convert Template

## Overview

Convert a PowerPoint `.pptx` / `.potx` visual template into a reusable `frontend-slides` bold template pack entry. The goal is not an asset dump: extract the template’s visual grammar, preserve source assets, document implementation rules, and make the template discoverable by `frontend-slides`.

## Output Contract

Create or update exactly one bold template directory:

```text
frontend-slides/skills/frontend-slides/bold-template-pack/templates/<slug>/
  assets/        # extracted and renamed source assets
  preview.md     # lightweight title-preview guidance only
  design.md      # full design system recipe
```

Then update:

```text
frontend-slides/skills/frontend-slides/bold-template-pack/selection-index.json
```

Required index fields must mimic neighboring entries exactly: `slug`, `name`, `tagline`, `mood`, `tone`, `formality`, `density`, `scheme`, `best_for`, `avoid_for`, `preview_md`, `design_md`.

## Boundaries

- Modify one template directory and `selection-index.json` only; do not reformat unrelated index entries or edit other templates.
- If the slug or directory already exists, inspect it and ask whether to update it or create a new slug. Do not overwrite silently.
- Do not create `template.html` by default. The pack contract is `assets/`, `preview.md`, and `design.md`; add HTML only if the user explicitly requests a runnable reference.
- Template docs must not contain absolute local paths, `file://` URLs, temporary extraction paths, machine-specific paths, root-relative paths, URL-like asset paths, or `../` traversal. Template asset refs stay inside `assets/`.

## Workflow

1. **Inspect existing pack structure first**
   - Read `selection-index.json` and 1-2 existing templates’ `preview.md` / `design.md`.
   - Do not invent schema, paths, or metadata names.

2. **Treat PowerPoint as an OOXML archive**
   - Work from a copy of the source file.
   - Inspect `ppt/slideMasters/`, `ppt/slideLayouts/`, `ppt/theme/`, `ppt/slides/`, `ppt/media/`, and relationship files.
   - Include `.potx`; it is the same ZIP-family format but often stores reusable layout intent in masters/layouts.

   Use the helper script for mechanical OOXML inventory before interpreting the design:

   ```bash
   python scripts/inspect-template-pptx.py <input.pptx-or-potx> <work-dir>
   ```

   It writes `<work-dir>/template-inspection.json`, `<work-dir>/summary.json`, and copies raw media into `<work-dir>/media/`. Treat this JSON as evidence for coordinates, relationships, placeholders, theme colors/fonts, fills, lines, and media references. It does **not** decide asset roles, visual grammar, semantic names, safe areas, or final template rules; those still require rendered comparison and design judgment.

3. **Extract assets safely**
   - Extract only into a controlled work directory.
   - Preserve original media during analysis, then copy only used assets into the template `assets/` folder with semantic names.
   - **Do not assume a rendered-looking background image contains the whole slide.** For each representative title/section/content slide, inspect its `picture` elements and relationships separately from background plates. If a slide uses a full-slide or near-full-slide background plus smaller picture overlays such as logos, seals, sponsor marks, icons, badges, QR codes, or corner emblems, copy and name those overlays as separate assets too.
   - Rename semantically when the role is clear: `logo-title.png`, `logo-small.png`, `logo-vnu.png`, `corner-ribbon.png`, `wave-footer.png`, `campus-line.png`. If the role is unclear but required, use `decorative-<n>.<ext>` and document it.
   - Deduplicate repeated images. Keep original formats unless browser support requires conversion.
   - Add a source mapping in `design.md`, e.g. `ppt/media/image3.png -> assets/logo-title.png`.

4. **Recover the visual grammar**
   - Identify theme colors, fonts, slide backgrounds, repeated artwork, header/body sizes, safe areas, footer/ribbon behavior, cards, borders, icon treatment, and layout families.
   - **Recover picture-overlay grammar explicitly.** For title and divider slides, list every non-background `picture` element from the source XML: source media path, semantic asset name, 1920×1080 coordinates, intended z-index, and whether it is required or optional. This is mandatory for logos and institutional marks even when the background already looks visually complete.
   - Source truth order: rendered slide/master screenshot > slide layout XML > theme XML > guessed CSS.
   - To render visually, prefer PowerPoint export if available; otherwise try LibreOffice/PowerPoint-compatible rendering; if neither works, continue from XML and label fidelity as approximate.
   - Cover at least title, section/divider, content, two-column or grid, image/media, and closing layouts when present. If a source has many variants, document representative families and list omitted variants.
   - Fidelity overrides generic design preferences: if the source template uses Inter, Arial-like institutional sans, or restrained academic colors, preserve that and document why.
   - For editable PowerPoint shapes, prefer exported SVG/PNG assets for official brand geometry; use CSS/SVG reconstruction only when asset export is impossible and document the approximation.
   - Recover **motion grammar** separately from static design. Default converted templates to static assets and one-time entrance reveals only. Document looping motion only when the source template clearly uses it as an intentional motif; otherwise mark decorative bobbing, shaking, jitter, wobble, pulse, and infinite movement as disallowed.
   - Recover **layer safety** as explicit coordinates: text-safe rectangles, decorative-only zones, reserved footer/header bands, maximum asset bounding boxes, and z-index order. Foreground assets may frame text but must not cover or sit above readable text unless the source intentionally uses a translucent background behind that text.
   - Recover **asset scaling rules** for every reusable bitmap/SVG prop. Never specify one-axis scaling that distorts artwork (for example stretching a footer image to full slide width while keeping a fixed height). Preserve each asset's intrinsic aspect ratio with `object-fit: contain`/`cover`, cropping, repetition/tiling, multiple placed copies, or CSS reconstruction of simple bands; document which method to use.
   - Document approximations explicitly; never claim pixel-perfect fidelity without rendered comparison.

5. **Write `preview.md` for selection**
   - Purpose: help `frontend-slides` generate one authentic title-slide preview.
   - Include selection metadata, visual snapshot, preview ingredients, and preview rules.
   - Do not include long implementation details better suited to `design.md`.

6. **Write `design.md` for generation**
   - Include frontmatter-style metadata, colors, typography, assets, source mapping, layout coordinates at the fixed 1920×1080 stage, components, slide layouts, rules, anti-patterns, and approximations.
   - Reference assets relative to the template directory, e.g. `assets/logo-title.png`.
   - Translate PowerPoint proportions into fixed-stage coordinates; do not keep viewport-reflow rules.
   - For each reusable slide pattern, state both the background plate and any required foreground/overlay pictures. Title slide recipes must explicitly say which logo/mark assets to place above the background, with coordinates and z-index. Do not rely on the generator to infer missing logos from source PowerPoint later.
   - Include a **Layering** section with: background layer, content/card layer, decorative asset layer, foreground/mascot/logo layer, and explicit z-index or stacking order. State which asset zones are decorative-only and which text-safe areas must remain clear.
   - Include a **Motion** section. The default is no continuous decorative animation. Allowed motion is one-time slide/content entrance and user-triggered interaction. If preserving source looping motion, constrain it to non-text background/prop layers, small amplitude, no jitter/shake, and `prefers-reduced-motion` fallback.
   - Include an **Asset scaling** section. For every repeated/footer/ribbon/prop image, state its intended aspect-ratio behavior: contain, cover-and-crop, repeat/tile, multiple copies, or CSS reconstruction. Explicitly forbid `width`/`height` pairs that change the intrinsic ratio unless the source rendering proves intentional distortion.
   - Use predictable sections: Visual thesis, Typography, Assets, Asset scaling, Layering, Motion, Layout recipe, Slide patterns, Rules, Anti-patterns, Source mapping, Verification notes.

7. **Update `selection-index.json`**
   - If adding a new slug, increment `template_count` if present; if updating an existing slug, keep `template_count` unchanged.
   - Insert the entry in the same object shape as existing templates.
   - Paths must be `bold-template-pack/templates/<slug>/preview.md` and `bold-template-pack/templates/<slug>/design.md`.

8. **Verify before reporting**
   - Required files exist.
   - Required assets referenced by `preview.md` / `design.md` exist.
   - **Title-slide overlay audit:** compare the first/title slide's source `picture` elements against the final `preview.md`/`design.md` asset recipes. Every visible logo/mark overlay in the source title slide must be either (a) copied into `assets/` and documented with placement, or (b) explicitly documented as omitted with a reason. A full-slide background plate does not satisfy this check if the logo was a separate `p:pic` in the source.
   - `selection-index.json` parses as JSON.
   - The changed entry has all required fields and matches neighboring field types.
   - New slug appears exactly once in the index.
   - No absolute paths, `../`, root-relative paths, or URL-like asset paths appear in `preview.md`, `design.md`, or the new index entry.
   - No unrelated template directories or unrelated index entries changed.
   - Generate a small preview slide and visually compare it with the source template when any renderer/export path is available; if not, state the exact missing tool/blocker.
   - Render at least the title, one content layout, and one densest/card-grid layout. Check that foreground/decorative assets do not overlap or cover readable text, equations, captions, or controls.
   - Inspect generated CSS/recipe text for continuous decorative animation (`infinite`, jitter/shake/wobble/bob/pulse) and remove it unless the source template intentionally requires it and the Motion section constrains it.

## Quick Reference

| Need | Do |
|---|---|
| Find brand colors | Run `python scripts/inspect-template-pptx.py <input> <work-dir>`, then inspect theme colors, fills, and rendered screenshots |
| Find reusable layouts | Use the script's slide master/layout inventory; inspect `ppt/slideMasters/` and `ppt/slideLayouts/`, not only sample slides |
| Preserve logos/backgrounds | Use the script's resolved media references, then copy/rename selected files from `<work-dir>/media/`; audit title-slide `picture` overlays separately from background plates; do not redraw official marks with CSS |
| Describe implementation | Put exact placement/layering rules from JSON coordinates plus visual judgment in `design.md` |
| Prevent covered text | Define text-safe rectangles, decorative-only zones, and z-index order |
| Control motion | Default to static props plus one-time entrance; document any source-required looping motion |
| Enable discovery | Add a schema-matching entry to `selection-index.json` |
| Handle uncertainty | State approximations and missing assets directly |

## Helper Script Boundary

`scripts/inspect-template-pptx.py` automates only the low-level extraction pass:

| Convert-template step | Script coverage |
|---|---|
| Open `.pptx` / `.potx` as ZIP | Automated |
| Enumerate slides, masters, layouts, themes, media | Automated |
| Parse `p:sp`, `p:pic`, `p:graphicFrame`, groups/connectors | Automated for common DrawingML objects |
| Resolve `rId` relationships to `ppt/media/*` | Automated |
| Extract geometry, placeholders, text, fills, lines, text runs | Automated where explicit in XML |
| Read theme colors/fonts | Automated |
| Copy raw media to a controlled folder | Automated |
| Decide asset roles and semantic filenames | Human/LLM judgment |
| Infer visual grammar, layout families, safe zones, layering, asset scaling rules | Human/LLM judgment, supported by JSON and screenshots |
| Write `preview.md`, `design.md`, and update `selection-index.json` | Human/LLM authorship |

## Minimal Example

For `SlideHCMUS.potx`, a good conversion creates:

- `templates/hcmus/assets/logo-title.png`, `logo-small.png`, `wave-orange.png`, `wave-blue.png`, `corner-tall.png`, skyline/campus art.
- `preview.md` saying title previews use the real logo, wave, corner ribbon, Inter, official blue/orange colors, and no internal template labels on the slide.
- `design.md` specifying fixed 1920×1080 placement: logo coordinates, right ribbon, bottom full-width waves, footer safe area, text sizes, and layer order.
- One `selection-index.json` entry with `slug: "hcmus"`, formal academic metadata, and correct preview/design paths.

## Common Mistakes

| Mistake | Fix |
|---|---|
| Dumping `ppt/media/image1.png` without understanding roles | Rename by visual purpose and document where each asset is used |
| Inspecting only normal slides | Inspect masters, layouts, themes, relationships, and sample slides |
| Recreating official logos/waves as CSS | Use actual extracted assets unless the source only contains editable shapes |
| Treating a background plate as the whole title slide | Audit title-slide `p:pic` overlays and place required logos/marks above the background with documented coordinates and z-index |
| Inventing index fields | Copy the shape of neighboring entries exactly |
| Overclaiming fidelity | Say what was verified; label approximations |
| Using absolute asset paths in template docs | Use paths relative to the template directory |
| Decorative assets cover text | Reserve text-safe rectangles and keep mascots/props in decorative-only zones or behind cards |
| Footer/ribbon image looks stretched or squashed | Preserve intrinsic aspect ratio; use repeated copies, cover-and-crop, contain, or CSS reconstruction instead of one-axis scaling |
| Jittery converted templates | Remove decorative infinite bob/shake/wobble/pulse unless source motion is intentional and constrained |
| Skipping visual checks | At minimum compare rendered title, content, and densest layouts against the source look and readability |

## Failure Handling

- Password-protected or corrupt file: stop and report the exact blocker.
- Missing fonts: document the original font and the chosen web-safe or Google/Fontshare substitute.
- Unsupported SmartArt/charts/shapes: approximate as CSS/SVG only after noting the source object type.
- Huge decks: sample representative masters/layouts first, then ask whether to cover every variant.
