/* Reveal.js owns slide visibility, scaling, keyboard shortcuts and PDF layout. */
;(() => {
  const previous = document.getElementById("prev")
  const next = document.getElementById("next")
  const fullscreenButton = document.getElementById("fullscreen")
  const query = new URLSearchParams(window.location.search)
  const printMode = query.has("print-pdf")
  const checkMode = query.get("check") === "1"

  function updateNavigation() {
    const slides = Reveal.getSlides()
    const total = slides.length
    const format = (number) => String(number).padStart(2, "0")
    previous.disabled = Reveal.isFirstSlide()
    next.disabled = Reveal.isLastSlide()
    slides.forEach((slide, index) => {
      const page = slide.querySelector(".page-number")
      if (page) page.textContent = `${format(index + 1)} / ${format(total)}`
    })
  }

  async function toggleFullscreen() {
    try {
      if (document.fullscreenElement) await document.exitFullscreen()
      else await document.documentElement.requestFullscreen()
    } catch {
      console.warn("Toàn màn hình không khả dụng")
    }
  }

  async function runChecks() {
    const issues = []
    const slides = Reveal.getSlides()
    const images = Array.from(document.images)
    await Promise.all(images.map((image) => image.complete
      ? Promise.resolve()
      : new Promise((resolve) => {
          image.addEventListener("load", resolve, { once: true })
          image.addEventListener("error", resolve, { once: true })
        })))

    images.forEach((image) => {
      const decorative = image.getAttribute("aria-hidden") === "true" && image.alt === ""
      if (!image.complete || image.naturalWidth === 0) {
        issues.push(`Ảnh không tải được: ${image.getAttribute("src") || "(không có src)"}`)
      }
      if (!decorative && !image.hasAttribute("alt")) {
        issues.push("Ảnh nội dung thiếu thuộc tính alt")
      }
    })

    slides.forEach((slide, index) => {
      const frame = slide.querySelector(".content-frame")
      if (!frame) return
      if (frame.scrollHeight > frame.clientHeight + 2 || frame.scrollWidth > frame.clientWidth + 2) {
        issues.push(`Slide ${index + 1}: content-frame bị tràn nội dung`)
      }
      const frameRect = frame.getBoundingClientRect()
      frame.querySelectorAll("h1, h2, h3, p, li, figure, table, .columns, .split, .statement, .list, .timeline").forEach((element) => {
        const rect = element.getBoundingClientRect()
        const tolerance = 3
        if (rect.top < frameRect.top - tolerance || rect.bottom > frameRect.bottom + tolerance
          || rect.left < frameRect.left - tolerance || rect.right > frameRect.right + tolerance) {
          issues.push(`Slide ${index + 1}: ${element.tagName.toLowerCase()} vượt content-frame`)
        }
      })
    })

    if (issues.length) {
      console.group("USCC deck check: FAIL")
      issues.forEach((issue) => console.warn(issue))
      console.groupEnd()
    } else {
      console.info(`USCC deck check: PASS (${slides.length} slide(s))`)
    }
    return issues
  }

  const deck = Reveal.initialize({
    width: 1920,
    height: 1080,
    margin: 0,
    minScale: 0.1,
    maxScale: 1,
    center: false,
    hash: true,
    controls: false,
    progress: false,
    slideNumber: false,
    transition: "fade",
    backgroundTransition: "none",
    transitionSpeed: "fast",
    overview: true,
    touch: true,
    pdfMaxPagesPerSlide: 1,
    pdfSeparateFragments: false,
    plugins: [RevealNotes],
  })

  deck.then(async () => {
    updateNavigation()
    Reveal.on("slidechanged", updateNavigation)
    previous.addEventListener("click", () => Reveal.prev())
    next.addEventListener("click", () => Reveal.next())
    fullscreenButton.addEventListener("click", toggleFullscreen)
    if (document.fonts) {
      await document.fonts.ready
      Reveal.layout()
    }
    if (checkMode) await runChecks()
    if (printMode) document.querySelector(".deck-toolbar").hidden = true
  })
})()
