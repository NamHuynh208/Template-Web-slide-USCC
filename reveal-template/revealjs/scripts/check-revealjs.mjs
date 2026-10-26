import fs from 'node:fs'
import path from 'node:path'
import process from 'node:process'
import { fileURLToPath } from 'node:url'

const ROOT = path.resolve(fileURLToPath(new URL('..', import.meta.url)))
const INDEX = path.join(ROOT, 'index.html')
const errors = []

function fail(message) {
  errors.push(message)
}

function read(file) {
  try {
    return fs.readFileSync(file, 'utf8')
  } catch {
    fail(`Missing file: ${path.relative(ROOT, file)}`)
    return ''
  }
}

function relative(file) {
  return path.relative(ROOT, file).replaceAll(path.sep, '/')
}

function resolveLocal(reference, fromFile) {
  const clean = reference.split('#')[0].split('?')[0]
  if (!clean || clean.startsWith('data:') || clean.startsWith('#')) return null
  if (/^(?:[a-z][a-z\d+.-]*:)?\/\//i.test(clean) || /^[a-z][a-z\d+.-]*:/i.test(clean)) {
    fail(`Remote resource is not allowed: ${reference} (${relative(fromFile)})`)
    return null
  }
  if (clean.startsWith('/')) {
    fail(`Root-relative resource is not allowed: ${reference} (${relative(fromFile)})`)
    return null
  }
  const target = path.resolve(path.dirname(fromFile), clean)
  const rootWithSep = `${ROOT}${path.sep}`
  if (target !== ROOT && !target.startsWith(rootWithSep)) {
    fail(`Path escapes template directory: ${reference} (${relative(fromFile)})`)
    return null
  }
  if (!fs.existsSync(target) || !fs.statSync(target).isFile()) {
    fail(`Missing resource: ${reference} (${relative(fromFile)})`)
    return null
  }
  return target
}

function attributes(tag) {
  const result = {}
  for (const match of tag.matchAll(/([:\w-]+)\s*=\s*["']([^"']*)["']/g)) {
    result[match[1].toLowerCase()] = match[2]
  }
  return result
}

function classes(tag) {
  return new Set((attributes(tag).class || '').split(/\s+/).filter(Boolean))
}

function scanSections(html, slidesStart, slidesEnd) {
  const token = /<\/?section\b[^>]*>/gi
  const stack = []
  const sections = []
  let match
  while ((match = token.exec(html))) {
    if (match.index < slidesStart || match.index >= slidesEnd) continue
    const tag = match[0]
    if (/^<section\b/i.test(tag)) {
      stack.push({ tag, start: match.index, depth: stack.length + 1 })
    } else if (stack.length) {
      const open = stack.pop()
      sections.push({ ...open, end: token.lastIndex, depth: open.depth })
      if (open.depth > 1) fail(`Nested section detected near character ${open.start}`)
    } else {
      fail(`Closing section without opening section near character ${match.index}`)
    }
  }
  if (stack.length) fail(`${stack.length} section tag(s) are not closed`)
  return sections.filter((section) => section.depth === 1).sort((a, b) => a.start - b.start)
}

const html = read(INDEX)
if (!html) process.exit(1)

if (!/<html\b/i.test(html) || !/<div\s+class=["'][^"']*\breveal\b/i.test(html)) {
  fail('index.html is missing the HTML or Reveal scaffold')
}
if (!/<div\s+class=["'][^"']*\bslides\b/i.test(html)) {
  fail('index.html is missing .slides')
}
for (const id of ['prev', 'next', 'fullscreen']) {
  if (!new RegExp(`id=["']${id}["']`, 'i').test(html)) fail(`Missing toolbar element #${id}`)
}
for (const src of ['vendor/reveal.js', 'vendor/notes.js', 'deck.js']) {
  if (!new RegExp(`src=["']${src.replaceAll('.', '\\.') }["']`, 'i').test(html)) {
    fail(`Missing required script reference: ${src}`)
  }
}

const slidesMatch = /<div\s+class=["'][^"']*\bslides\b[^"']*["'][^>]*>/i.exec(html)

function findDivEnd(source, contentStart) {
  const token = /<\/?div\b[^>]*>/gi
  token.lastIndex = contentStart
  let depth = 1
  let match
  while ((match = token.exec(source))) {
    if (/^<div\b/i.test(match[0])) depth += 1
    else depth -= 1
    if (depth === 0) return match.index
  }
  return -1
}

if (!slidesMatch) fail('Could not locate the .slides container')

const slidesStart = slidesMatch ? slidesMatch.index + slidesMatch[0].length : 0
const slidesEnd = slidesMatch ? findDivEnd(html, slidesStart) : -1
if (slidesMatch && slidesEnd < 0) fail('The .slides container is not closed')
const sections = slidesMatch && slidesEnd >= 0 ? scanSections(html, slidesStart, slidesEnd) : []
if (!sections.length) fail('No slide sections found')

for (const [index, section] of sections.entries()) {
  const body = html.slice(section.start, section.end)
  const openTag = section.tag
  const sectionClasses = classes(openTag)
  const expected = index === 0 ? 'cover' : index === sections.length - 1 ? 'closing' : 'body-slide'
  if (!sectionClasses.has('slide') || !sectionClasses.has(expected)) {
    fail(`Slide ${index + 1} must have classes "slide ${expected}"`)
  }
  if (!/<div\s+class=["'][^"']*\bcontent-frame\b/i.test(body)) {
    fail(`Slide ${index + 1} is missing .content-frame`)
  }
  if (!/<aside\s+class=["'][^"']*\bnotes\b/i.test(body)) {
    fail(`Slide ${index + 1} is missing <aside class="notes">`)
  }
  if (!/<span\s+class=["'][^"']*\bpage-number\b/i.test(body)) {
    fail(`Slide ${index + 1} is missing .page-number`)
  }
  if (index > 0 && index < sections.length - 1 && !/<p\s+class=["'][^"']*\beyebrow\b/i.test(body)) {
    fail(`Body slide ${index + 1} is missing .eyebrow`)
  }

  for (const image of body.matchAll(/<img\b[^>]*>/gi)) {
    const attrs = attributes(image[0])
    const decorative = attrs['aria-hidden'] === 'true' && attrs.alt === ''
    if (!decorative && (!Object.hasOwn(attrs, 'alt') || !attrs.alt.trim())) {
      fail(`Slide ${index + 1} has an image without meaningful alt text`)
    }
  }
}

for (const match of html.matchAll(/<(?:link|script|img)\b[^>]*?(?:href|src)\s*=\s*["']([^"']+)["'][^>]*>/gi)) {
  resolveLocal(match[1], INDEX)
}

const cssFile = path.join(ROOT, 'uscc.css')
const css = read(cssFile)
for (const match of css.matchAll(/url\(\s*["']?([^"')]+)["']?\s*\)/gi)) {
  resolveLocal(match[1], cssFile)
}

if (errors.length) {
  console.error(`Reveal.js check failed with ${errors.length} error(s):`)
  for (const error of errors) console.error(`- ${error}`)
  process.exit(1)
}

console.log(`Reveal.js check passed: ${sections.length} slide(s), local references resolved.`)
