# HCMUS Preview Card

Use this small file for title-slide previews only. For final deck generation, read the full design doc listed below.

## Files

- Full design doc: `bold-template-pack/templates/hcmus/design.md`
- Preview card: `bold-template-pack/templates/hcmus/preview.md`
- Original assets: `bold-template-pack/templates/hcmus/assets/`

## Selection Metadata

- Slug: `hcmus`
- Tagline: Official HCMUS academic slide system with original VNUHCM University of Science logos, blue-orange wave footer, campus line art, right-corner ribbon, and strict Inter typography.
- Mood: academic, institutional, trustworthy, Vietnamese university, clean
- Tone: formal, instructional, polished, campus-branded, lecture-ready
- Formality: high
- Density: medium
- Scheme: light
- Best for: University lectures, course decks, seminar presentations, research briefings, student reports, graduation/institutional content, and any Vietnamese academic presentation that should preserve the HCMUS/ĐHQG-HCM template identity.
- Avoid for: Decks that need a playful, luxury, startup, or non-institutional brand voice; designs where the HCMUS identity should not appear.

## Visual Snapshot

A clean institutional university presentation system on a white canvas with original HCMUS template artwork. The visual identity is built from extracted POTX assets rather than recreated CSS shapes: a horizontal VNUHCM University of Science logo on the title slide, a small circular HCMUS logo on content slides, blue/orange footer waves, a tall blue right-corner ribbon, and bottom full-width campus/skyline artwork.

Typography is intentionally strict and template-like: Inter across the entire deck, #2D4C9A for all text, 36px headers, and 27px normal text. The deck should feel like an official classroom/seminar slide system rather than a redesigned brand interpretation.

## Preview Ingredients

- Palette: white canvas; global text/primary #2D4C9A; sky #2992D0; pale #C5D7DB; orange #D98323.
- Typography: Inter only, loaded from Google Fonts. Header text is 36px; body text is 27px.
- Signature move: Use actual image assets from `assets/`; do not redraw logos, waves, campus line art, skyline art, or corner ribbons with CSS.
- Signature move: Title slide uses `assets/logo-title.png` centered high near the top/title area.
- Signature move: Content slides use `assets/logo-small.png` at the upper-right, aligned with the existing right ribbon; final thank-you slides use the small logo centered high near the top.
- Signature move: `assets/corner-tall.png` is the right-corner ribbon and is the only layout background not required to sit at the bottom.
- Signature move: `assets/wave-orange.png`, `assets/wave-blue.png`, `assets/building-line.png`, `assets/skyline-light.png`, and `assets/skyline-deep.png` sit at the bottom and span the full slide width.
- Signature move: `assets/building-line.png`, `assets/skyline-light.png`, and `assets/skyline-deep.png` are deepest-layer backgrounds and are mutually exclusive per slide: use at most one.
- Signature move: Content surfaces are white or very pale blue, with thin blue borders and modest radius; avoid decorative glassmorphism.

- Signature move: Content slide h0/eyebrow labels such as `01 / Nền tảng` use 36px Inter and follow the original sample slide position near x=158px, y=78px.
- Signature move: Final/thank-you slide uses the small logo centered high near the top, with the thank-you text centered in the title-position rhythm.

## Preview Rules

- Build exactly one title slide at 1920x1080 inside the fixed-stage model.
- Preserve original HCMUS assets exactly; no CSS recreation of logo/background elements.
- Use Inter globally; visible title/header text should be 36px and normal text should be 27px.

- For title previews, center the official horizontal logo high near the top/title area rather than placing it upper-left.
- If previewing a thank-you/final slide, use the small logo centered high near the top and center the thank-you text.
- h0/eyebrow labels use 36px and should align to the original sample heading position.
- Use #2D4C9A for all visible text except white footer text where contrast requires it.
- Use only one deepest building/skyline background asset on the slide.
- Place all non-corner background/layout images at the bottom, full width.
- Use the user's real title/subtitle/context; do not copy demo slide content.
- The rendered preview must look like a real first slide, not a template-selection card.
- Never place internal workflow text on the slide: no `preview`, `generated from`, `preview.md`, `template`, `preset`, `style option`, `Option A/B/C`, file names, paths, or source-doc labels.
- Never place the template name or slug on the slide itself; mention it only in the chat message.
- Use only real deck content for visible chrome: deck title, real section title, date, author, company, page number, or genuine content phrases from the user material.
- Do not read `template.html` for preview generation.
- Do not read other templates' `design.md` files.
- After the user picks this template for the full deck, read the full design doc before generating final slides.
