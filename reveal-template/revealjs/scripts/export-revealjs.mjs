import fs from 'node:fs'
import path from 'node:path'
import { fileURLToPath } from 'node:url'
import { spawnSync } from 'node:child_process'

const ROOT = path.resolve(fileURLToPath(new URL('..', import.meta.url)))
const INDEX = path.join(ROOT, 'index.html')
const OUTPUT_DIR = path.join(ROOT, 'dist')
const OUTPUT = path.join(OUTPUT_DIR, 'uscc-reveal.html')
const checker = path.join(ROOT, 'scripts', 'check-revealjs.mjs')

const check = spawnSync(process.execPath, [checker], { cwd: ROOT, encoding: 'utf8' })
if (check.stdout) process.stdout.write(check.stdout)
if (check.stderr) process.stderr.write(check.stderr)
if (check.status !== 0) process.exit(check.status || 1)

const source = fs.readFileSync(INDEX, 'utf8')

function mime(file) {
  const extension = path.extname(file).toLowerCase()
  return {
    '.css': 'text/css',
    '.js': 'text/javascript',
    '.png': 'image/png',
    '.jpg': 'image/jpeg',
    '.jpeg': 'image/jpeg',
    '.gif': 'image/gif',
    '.svg': 'image/svg+xml',
    '.webp': 'image/webp',
    '.ttf': 'font/ttf',
    '.woff': 'font/woff',
    '.woff2': 'font/woff2',
  }[extension] || 'application/octet-stream'
}

function dataUri(file) {
  return `data:${mime(file)};base64,${fs.readFileSync(file).toString('base64')}`
}

function resolveLocal(reference, fromFile) {
  const clean = reference.split('#')[0].split('?')[0]
  if (!clean || clean.startsWith('data:') || clean.startsWith('#')) return null
  if (/^(?:[a-z][a-z\d+.-]*:)?\/\//i.test(clean) || /^[a-z][a-z\d+.-]*:/i.test(clean)) {
    throw new Error(`Remote resource is not allowed: ${reference}`)
  }
  if (clean.startsWith('/')) throw new Error(`Root-relative resource is not allowed: ${reference}`)
  const file = path.resolve(path.dirname(fromFile), clean)
  const rootWithSep = `${ROOT}${path.sep}`
  if (file !== ROOT && !file.startsWith(rootWithSep)) {
    throw new Error(`Resource escapes template directory: ${reference}`)
  }
  if (!fs.existsSync(file) || !fs.statSync(file).isFile()) {
    throw new Error(`Missing resource: ${reference}`)
  }
  return file
}

function inlineCss(css, cssFile) {
  return css.replace(/url\(\s*(["']?)([^"')]+)\1\s*\)/gi, (match, quote, reference) => {
    if (reference.startsWith('data:')) return match
    const file = resolveLocal(reference, cssFile)
    return `url("${dataUri(file)}")`
  })
}

let output = source

output = output.replace(/<link\b([^>]*?)href\s*=\s*(["'])([^"']+)\2([^>]*)>/gi, (match, before, quote, reference, after) => {
  if (!/rel\s*=\s*["']stylesheet["']/i.test(`${before}${after}`)) return match
  const file = resolveLocal(reference, INDEX)
  const css = inlineCss(fs.readFileSync(file, 'utf8'), file)
  return `<style data-inlined-from="${reference}">\n${css}\n</style>`
})

output = output.replace(/(<img\b[^>]*?\bsrc\s*=\s*)(["'])([^"']+)\2/gi, (match, prefix, quote, reference) => {
  const file = resolveLocal(reference, INDEX)
  return `${prefix}${quote}${dataUri(file)}${quote}`
})

output = output.replace(/<script\b([^>]*?)src\s*=\s*(["'])([^"']+)\2([^>]*)><\/script>/gi, (match, before, quote, reference, after) => {
  const file = resolveLocal(reference, INDEX)
  const javascript = fs.readFileSync(file, 'utf8')
  return `<script data-inlined-from="${reference}">\n${javascript}\n<\/script>`
})

const licenses = [
  fs.readFileSync(path.join(ROOT, 'vendor', 'REVEAL-LICENSE.txt'), 'utf8'),
  fs.readFileSync(path.join(ROOT, 'assets', 'Inter-OFL.txt'), 'utf8'),
]
  .join('\n\n')
  .replaceAll('-->', '-- >')

output = `<!-- Inlined USCC Reveal.js deck. Source licenses follow.\n${licenses}\n-->\n${output}`

fs.mkdirSync(OUTPUT_DIR, { recursive: true })
fs.writeFileSync(OUTPUT, output)
console.log(`Standalone HTML written to ${path.relative(ROOT, OUTPUT).replaceAll(path.sep, '/')}`)
