---
version: alpha
name: HCMUS
description: Official HCMUS / VNUHCM University of Science academic presentation system using original extracted PowerPoint template assets. Typography is Inter across the entire deck, with #2D4C9A as the global text color, 36px headers, and 27px body text. Background assets are placed as original images with strict bottom/full-width layering rules.

colors:
  bg: "#ffffff"
  primary: "#2D4C9A"
  text: "#2D4C9A"
  sky: "#2992D0"
  pale: "#C5D7DB"
  orange: "#D98323"
  border: "rgba(45, 76, 154, 0.18)"
  card-bg: "rgba(255, 255, 255, 0.94)"

typography:
  global:
    fontFamily: "'Inter', sans-serif"
    color: "#2D4C9A"
    rule: "Use Inter for every text element in the deck: titles, headers, body, labels, tables, captions, footer, slide numbers, and chart text."
  header:
    fontFamily: "'Inter', sans-serif"
    fontWeight: 700
    fontSize: "36px at 1920px stage"
    lineHeight: 1.25
    color: "#2D4C9A"
    usage: "All section headers, slide titles, card titles, and major labels. Do not scale these into oversized hero typography unless the user explicitly asks."
  body:
    fontFamily: "'Inter', sans-serif"
    fontWeight: 400
    fontSize: "27px at 1920px stage"
    lineHeight: 1.45
    color: "#2D4C9A"
    usage: "Normal paragraph text, bullet text, captions, notes, and explanatory copy."
  emphasis:
    fontFamily: "'Inter', sans-serif"
    fontWeight: 700
    fontSize: "27px at 1920px stage"
    lineHeight: 1.35
    color: "#2D4C9A"
    usage: "Short emphasis inside body copy or data labels."

assets:
  directory: "bold-template-pack/templates/hcmus/assets"
  titleLogo: "assets/logo-title.png"
  smallLogo: "assets/logo-small.png"
  waveOrange: "assets/wave-orange.png"
  waveBlue: "assets/wave-blue.png"
  cornerTall: "assets/corner-tall.png"
  buildingLine: "assets/building-line.png"
  skylineDeep: "assets/skyline-deep.png"
  skylineLight: "assets/skyline-light.png"

layout:
  model: "fixed-stage"
  canvas: "1920x1080"
  slidePadding: "96px 128px 178px"
  contentPaddingWithLogo: "118px 270px 178px 128px"
  titleLogoPlacement:
    left: "50%"
    top: 115px
    width: 780px
    transform: "translateX(-50%)"
    note: "First/title slide logo is centered and placed high near the top title area."
  smallLogoPlacement:
    right: 98px
    top: 54px
    width: 112px
  finalSmallLogoPlacement:
    left: "50%"
    top: 120px
    width: 150px
    transform: "translateX(-50%)"
    note: "Final/thank-you slide uses the small logo, centered high near the top."
  rightRibbonPlacement:
    asset: "assets/corner-tall.png"
    right: 0
    top: 0
    note: "image1/cornerTall is the only layout background that does not have to sit at the bottom. It stays at the right side/top-right as in the PowerPoint template."
  bottomFullWidthPlacement:
    left: 0
    bottom: 0
    width: 1920px
    note: "All background/layout elements except cornerTall/image1 are placed at the bottom and stretched/positioned to full slide width."
  deepBuildingLayer:
    zIndex: 0
    rule: "buildingLine, skylineDeep, and skylineLight are the deepest decorative layers. They are independent: a slide may use at most one of these three building/skyline styles."
  footerWaveLayer:
    zIndex: 1
    rule: "waveOrange or waveBlue sits above the deep building/skyline layer, also bottom full-width."
  logoLayer:
    zIndex: 4
  contentLayer:
    zIndex: 3

components:
  contentCard:
    background: "rgba(255,255,255,0.94)"
    border: "2px solid rgba(45,76,154,0.18)"
    borderRadius: "18-28px"
    shadow: "0 12px 32px rgba(45,76,154,0.06)"
    padding: "24-36px"
    color: "#2D4C9A"
    usage: "Definition blocks, stat cards, comparison cells, concept cards. Card titles are 36px Inter; card text is 27px Inter."
  blueNumberBox:
    background: "#2D4C9A"
    color: "#ffffff"
    borderRadius: "12-16px"
    size: "48-60px"
    usage: "Step numbers and labeled concepts."
  orangeBadge:
    background: "#D98323"
    color: "#ffffff"
    borderRadius: "12-15px"
    usage: "Small emphasis markers only; do not use orange as body text."
  footerNote:
    color: "#ffffff"
    fontFamily: "'Inter', sans-serif"
    fontSize: "27px"
    fontWeight: 700
    position: "bottom-right inside wave footer"
  slideNumber:
    color: "#ffffff"
    fontFamily: "'Inter', sans-serif"
    fontSize: "27px"
    fontWeight: 700
    position: "bottom-right after footer note"

slideLayouts:
  title:
    requiredAssets:
      - "assets/logo-title.png"
      - "assets/wave-orange.png"
      - "assets/corner-tall.png"
    optionalDeepBackgroundOneOf:
      - "assets/building-line.png"
      - "assets/skyline-deep.png"
      - "assets/skyline-light.png"
    composition: "White slide, official horizontal logo centered high near the top/title area, right-corner ribbon, bottom full-width wave footer, and at most one bottom full-width building/skyline layer behind the wave. Main text uses Inter, #2D4C9A, 36px header and 27px normal text."
  content:
    requiredAssets:
      - "assets/logo-small.png"
      - "assets/wave-orange.png"
      - "assets/corner-tall.png"
    optionalDeepBackgroundOneOf:
      - "assets/building-line.png"
      - "assets/skyline-deep.png"
      - "assets/skyline-light.png"
    composition: "Small logo at upper-right. Content stays clear of right ribbon and footer. Use at most one deep building/skyline layer. Headers 36px Inter, body 27px Inter, all text #2D4C9A."
  data:
    requiredAssets:
      - "assets/logo-small.png"
      - "assets/wave-blue.png"
      - "assets/corner-tall.png"
    optionalDeepBackgroundOneOf:
      - "assets/building-line.png"
      - "assets/skyline-deep.png"
      - "assets/skyline-light.png"
    composition: "Use blue wave footer for data/metrics slides. Metrics, chart labels, and body text all use Inter and #2D4C9A."
  closing:
    requiredAssets:
      - "assets/logo-small.png"
      - "assets/wave-orange.png"
      - "assets/corner-tall.png"
    optionalDeepBackgroundOneOf:
      - "assets/building-line.png"
      - "assets/skyline-deep.png"
      - "assets/skyline-light.png"
    composition: "Final/thank-you slide uses the small logo centered high near the top and the thank-you text centered at the same title-area rhythm. It can use one skyline/building layer behind the footer. Do not introduce new color systems."

rules:
  - "Use actual assets from the template directory; do not redraw HCMUS logos, wave footers, corner ribbons, or building line art with CSS."
  - "Inter is the only font for the entire deck. Do not use serif display fonts or alternative body fonts."
  - "The global text color is #2D4C9A. Only footer text over blue/orange waves may be white for contrast."
  - "Header text size is 36px at the 1920px stage. Normal text size is 27px at the 1920px stage."
  - "All background/layout images except cornerTall/image1 must be placed at the bottom and span the full slide width."
  - "buildingLine, skylineDeep, and skylineLight are deepest-layer backgrounds and are mutually exclusive per slide: use at most one."
  - "Layer order: deepest building/skyline at z-index 0; footer wave at z-index 1; corner ribbon at z-index 1 or 2; content above backgrounds; logos above content/backgrounds."
  - "Keep all slide content within a fixed 1920x1080 stage and scale the stage to viewport."
  - "Content must not overlap the right-corner ribbon, small logo, or footer wave."
  - "Avoid generic dark gradients, purple palettes, glassmorphism, fake logos, or CSS-recreated brand elements."
  - "When exporting/deploying, copy the HCMUS image assets next to the generated HTML or inline them as data URIs."

implementationNotes:
  fontLinks: "https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap"
  baseTypographyCss: |
    body, .slide, h1, h2, h3, h4, p, li, span, div, table, text {
      font-family: 'Inter', sans-serif;
      color: #2D4C9A;
    }
    h1, h2, h3, .header { font-size: 36px; line-height: 1.25; font-weight: 700; }
    p, li, .body-text, .caption { font-size: 27px; line-height: 1.45; font-weight: 400; }
  cssAssetClasses: |
    .tpl { position:absolute; pointer-events:none; user-select:none; }
    .tpl-building, .tpl-skyline-deep, .tpl-skyline-light {
      left:0; bottom:0; width:1920px; height:auto; z-index:0;
    }
    .tpl-wave-orange, .tpl-wave-blue {
      left:0; bottom:0; width:1920px; height:auto; z-index:1;
    }
    .tpl-corner { right:0; top:0; width:365px; height:auto; z-index:2; }
    .logo-title { position:absolute; left:50%; top:115px; width:780px; height:auto; transform:translateX(-50%); z-index:4; }
    .logo-small { position:absolute; right:98px; top:54px; width:112px; height:auto; z-index:4; }
    .logo-small-centered { position:absolute; left:50%; top:120px; width:150px; height:auto; transform:translateX(-50%); z-index:4; }
---

# HCMUS Design System

HCMUS is a formal academic slide template built from the original `SlideHCMUS.potx` visual assets. It is best for Vietnamese university lectures, seminar decks, course reports, and institutional presentations that must preserve the University of Science / VNUHCM identity.

## Visual thesis

The slide should feel official and classroom-ready: white canvas, blue institutional framing, orange footer accent, and original campus/background artwork. The assets are the brand; do not reinterpret them as CSS drawings.

## Typography rules

- Use **Inter** for the entire deck.
- Use **#2D4C9A** for all text.
- Use **36px** for headers, including slide titles and card titles.
- Use **27px** for normal text, including paragraphs, bullet text, labels, and captions.
- Footer text may be white only when placed over the footer wave for contrast.

## Required asset behavior

1. Title slides use the horizontal logo (`logo-title.png`) near the upper-left.
2. Content slides use the small circular logo (`logo-small.png`) near the upper-right.
3. `corner-tall.png` is the right-corner ribbon and is the only background/layout asset that is not required to sit at the bottom.
4. `wave-orange.png`, `wave-blue.png`, `building-line.png`, `skyline-light.png`, and `skyline-deep.png` must be placed at the bottom and span the full slide width.
5. `building-line.png`, `skyline-light.png`, and `skyline-deep.png` are deepest-layer decorative backgrounds. They are independent: use at most one of these three on a slide.
6. Footer waves sit above the deepest building/skyline layer.

## Layer recipe

- z-index 0: one of `building-line.png`, `skyline-light.png`, or `skyline-deep.png`.
- z-index 1: `wave-orange.png` or `wave-blue.png`.
- z-index 2: `corner-tall.png`.
- z-index 3: content cards and main text.
- z-index 4: logos.


## Heading placement rules

- Content slide h0/eyebrow labels such as `01 / Nền tảng` use the same 36px Inter size as headers.
- Content slide h0/eyebrow labels should follow the original sample slide position: near the upper-left content area, around x=158px and y=78px on the 1920×1080 stage.
- Content slide main headings should sit below that h0 position, aligned to the same left edge, preserving the sample template rhythm.

## Layout recipe

- Canvas: fixed 1920×1080.
- Content starts at x=128px.
- Reserve the right 250–300px on content slides for the ribbon/logo zone.
- Reserve the bottom 170–190px for footer and background art.
- Avoid placing important content below y≈850.

## Common slide patterns

### Title slide

- Assets: `logo-title`, `wave-orange`, `corner-tall`, plus at most one building/skyline background.
- Horizontal logo centered high near the top/title area; text below it, centered.
- Header size 36px; normal text size 27px.

### Content slide

- Assets: `logo-small`, `wave-orange`, `corner-tall`, plus at most one building/skyline background.
- Use simple white content cards with blue borders.
- Header size 36px; normal text size 27px.

### Data slide

- Assets: `logo-small`, `wave-blue`, `corner-tall`, plus at most one building/skyline background.
- Charts and metric labels also use Inter, #2D4C9A.

### Closing slide

- Assets: centered `logo-small`, `wave-orange`, `corner-tall`, plus at most one building/skyline background.
- Place the small logo high near the top, centered.
- Place “Cảm ơn” / thank-you text centered in the title position rhythm.

## Anti-patterns

- Do not use `slide::before` / `slide::after` to recreate the footer/ribbon.
- Do not use generated text logos, fake brand marks, or approximated HCMUS logos.
- Do not stretch the small logo into the horizontal logo or vice versa.
- Do not use more than one of `building-line`, `skyline-light`, and `skyline-deep` on the same slide.
- Do not place non-corner background images anywhere except the bottom full-width layer.
- Do not introduce serif fonts, Be Vietnam Pro, IBM Plex Serif, or other font systems; Inter only.
