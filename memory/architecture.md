# Kiến trúc dự án

> Cập nhật: 2026-10-26

## Tổng quan
Repo tập hợp nhiều template thuyết trình độc lập (không phải một ứng dụng duy nhất), chủ đề thương hiệu USCC.

## Cấu trúc
- `slidev-template/slidev-template/` — template Slidev dạng component: `slides.md` (nội dung), `layouts/`, `components/`, `styles/`, `public/`.
- `slidev-template 2nd ver/slidev-template/` — bản sao/rút gọn của template Slidev.
- `reveal-template/reveal-template/` — template Reveal.js cổ điển, không cần build; nội dung Markdown nằm trong `<textarea>` của `slides.html`, style ở `theme.css`, runtime vendored ở `lib/`.
- `reveal-template/revealjs/` — deck Reveal.js thương hiệu USCC: `index.html` (6 section HTML), `uscc.css`, `deck.js`, `vendor/`, `assets/`, `dist/uscc-reveal.html` (bản export), script kiểm tra/export trong `scripts/`.
- `reveal-template 2nd ver/revealjs/` — bản sao rút gọn của deck Reveal.js USCC.
- `FrontendSlide_addon/hcmus/` — bộ brand asset + `design.md`/`preview.md` cho hệ hình ảnh HCMUS 1920×1080.
- `FrontendSlide_addon/convert-template/` — quy trình chuyển PPTX/POTX sang template, script Python trong `scripts/`.
- `assets/`, `Figma/`, `Figma.zip` — tư liệu thiết kế nguồn.

## Stack & lệnh
- Slidev: Node.js 18+, `npm install`, `npm run dev|build|export|export-pptx`.
- Reveal.js: chạy tĩnh (`python -m http.server 8000`); kiểm tra `node scripts/check-revealjs.mjs`, export `node scripts/export-revealjs.mjs`.
- Python 3 cho `scripts/inspect-template-pptx.py`.
- Không có test/lint tự động.

## Quy ước
- Mỗi thư mục template là một sản phẩm riêng; thay đổi không tự động áp dụng chéo.
- Slidev: nội dung trong `slides.md`, giữ `layouts/`/`components/` tái sử dụng.
- Reveal cổ điển: chỉ sửa trong `<textarea>` của `slides.html` trừ khi đổi framework/theme.
- Reveal USCC: giữ cấu trúc direct-child dưới `.reveal > .slides`, số trang xử lý trong `deck.js`.
- Không commit `node_modules/`, `__pycache__/` (đã có `.gitignore`).
