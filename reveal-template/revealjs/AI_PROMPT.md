# USCC Reveal.js content prompt

Use this prompt together with `CONTENT_TEMPLATE.md`, the source document text, and
`index.html` when generating a deck for the USCC Chess Club.

## Role

You are editing an existing static Reveal.js presentation. Return a complete,
ready-to-open `index.html`; do not create a new framework, Markdown runtime, CSS
system, or build tool.

## Source-of-truth workflow

1. Read the supplied DOCX/PDF text or extracted outline. Preserve its language,
   names, numbers, dates, quotations, and uncertainty.
2. Use `CONTENT_TEMPLATE.md` as the normalized slide brief.
3. Generate only the slide content and metadata that the source supports. Never
   invent facts, statistics, citations, or image descriptions.
4. Put source-page references, caveats, and useful speaking context in
   `<aside class="notes">`, not in visible slide copy unless the brief requests it.
5. Return the entire HTML file so the existing runtime scaffold is not lost.

## Immutable scaffold

Keep these parts unchanged unless the task explicitly asks for a runtime change:

- The local `vendor/` and `assets/` paths.
- The `.reveal > .slides` structure.
- The three toolbar buttons (`prev`, `next`, `fullscreen`) and script tags at the end of the file.
- The Reveal configuration in `deck.js`.
- The decorative `.chessboard`, `.wave-orange`, `.uscc-logo`, `.footer-logo`,
  `.page-number`, and notes elements on every slide.
- The fixed 1920×1080 design and local Inter font usage.

Every slide must be a direct child of `.slides`. Use one horizontal slide stream;
do not nest `<section>` elements.

## Slide structure

- The first section must have `class="slide cover"`.
- The last section must have `class="slide closing"`.
- All intermediate sections must have `class="slide body-slide"`.
- Every section needs an accurate Vietnamese `aria-label`, one `.content-frame`,
  one `<aside class="notes">`, and one `.page-number`.
- Body slides keep the `.eyebrow` in the header, even when it is empty.
- Change the document `<title>` to the actual deck title.
- Keep `lang="vi"` unless the source deck is explicitly in another language.
- The number of slides may change by duplicating or removing a complete section;
  never paste a partial section or create nested sections.

## Supported content patterns

Use only patterns already supported by `uscc.css`:

- `.lead` for one short introductory paragraph.
- `.meta` with `<span>` elements for date, speaker, audience, or context.
- `.columns` containing up to three `.column` elements.
- `.split` for two balanced content regions.
- `.statement` for one short, high-confidence takeaway.
- `.list` for a small ordered set of labeled points.
- `.timeline` containing up to four `.phase` elements.
- `.content-image` for a local figure inside a content region.

A slide should communicate one main idea. Split a slide instead of shrinking text.
Use approximately five bullets or fewer, short bullets, and no more than four
steps in a timeline. Do not reduce the template's 27px body text to fit more copy.

## Images

Only use images supplied locally in `assets/` or `assets/content/`. Do not use
remote URLs, data copied from an unverified source, or invented image paths.
Content images must use this shape:

```html
<figure class="content-image">
  <img src="assets/content/example.png" alt="Mô tả ngắn, chính xác của hình" />
  <figcaption>Nguồn: tài liệu gốc, trang 3</figcaption>
</figure>
```

Keep the `alt` text factual and concise. Include a credit or source page when the
brief provides one. Do not apply inline width/height values that distort the image.

## Content safety

- Do not place important text in the footer wave or chessboard area.
- Do not allow content to cover the header, logo, or footer.
- Do not add HCMUS/VNUHCM institutional marks, new logos, purple palettes,
  gradients, glassmorphism, or decorative animation.
- Do not copy internal workflow labels such as `preview`, `template`, or file paths
  into visible slide content.
- Keep HTML escaped and valid. Use semantic headings in order where practical.
- Keep speaker notes useful but concise; include source page numbers when available.

## Required final checks

Before returning the HTML:

1. Confirm the first/last/intermediate slide classes.
2. Confirm all sections are direct children of `.slides`.
3. Confirm all local image paths exist and every non-decorative image has `alt`.
4. Confirm each slide has `.content-frame`, notes, and page number.
5. Confirm there are no remote asset URLs or nested sections.
6. Confirm content fits the fixed safe area; split dense material into another slide.
7. Run `node scripts/check-revealjs.mjs` after saving the file.
8. Open the deck through `python -m http.server 8000` and inspect it at both a
   1920×1080 viewport and a smaller laptop viewport.
