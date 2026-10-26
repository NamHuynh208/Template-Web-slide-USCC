# USCC — Template Slidev (thiết kế Figma)

Bản Slidev của bộ slide sinh hoạt USCC, cùng hệ thiết kế với bản độc lập trong
`reveal-template/revealjs/`: navy `#1a295e` · xanh `#5d78c4` · gold `#f1bf0c`,
font Arimo, nền gradient trắng + sóng navy + dải sóng vàng.

## Chạy thử

```bash
npm install        # lần đầu; cần Node.js 18+
npm run dev        # mở http://localhost:3030
npm run build      # xuất web tĩnh vào dist/
npm run export     # xuất PDF (cần playwright-chromium)
npm run export-pptx # xuất PPTX (dạng ảnh từng slide)
```

## Cấu trúc

```text
slides.md           # nội dung 11 slide (AI/thành viên chỉ sửa chủ yếu file này)
styles/tokens.css   # MÀU + FONT — sửa đây để đổi toàn bộ giao diện
styles/index.css    # kiểu chữ, thẻ article, bảng, số trang dùng chung
layouts/            # cover, section, content, split, quote, end
components/         # StatCard, Timeline, Callout
public/             # uscc-logo.png, sweep-navy.svg, wave-gold.svg
```

## Layouts

| Layout | Dùng khi | Thuộc tính frontmatter |
| --- | --- | --- |
| `cover` | Bìa | `eyebrow`, `note` |
| `section` | Slide chào/mở phần, căn giữa | `eyebrow` |
| `content` | Slide nội dung (mặc định) | `eyebrow` |
| `split` | Nội dung kèm hình | `image`, `side: left\|right`, `eyebrow` |
| `quote` | Câu trích dẫn, thông điệp | `author` |
| `end` | Slide kết, căn giữa | `eyebrow` |

Nhãn mục màu navy (vd `07 / Chương trình`) đặt qua thuộc tính `eyebrow` của layout.

## Components

```md
<StatCard value="120+" label="Thành viên đang sinh hoạt" :progress="76" color="gold" />
```
Thẻ số liệu: số lớn navy + mô tả xanh + thanh tiến độ màu (`gold|navy|blue`).

```md
<Timeline :items="[{ title: 'Làm quen' }, { title: 'Luyện tập' }]" />
```
Lộ trình tối đa 4 bước, số thứ tự lớn + đường vàng phía trên.

```md
<Callout title="Lưu ý">Nội dung nhấn mạnh</Callout>
```
Khối nhấn viền vàng, tối đa 1 mỗi slide.

## Quy tắc nội dung

- Mỗi slide một thông điệp; tối đa ~5 ý ngắn; dài quá thì tách slide.
- Lưới dùng class UnoCSS: `grid grid-cols-3 gap-x-11`; mỗi ô là một `<article>`
  (tự có đường vàng phía trên) — xem mẫu trong `slides.md`.
- Bảng dùng cú pháp Markdown bảng; style đã có sẵn trong `styles/index.css`.
- Chỉ dùng ảnh trong `public/`; không dùng URL ngoài.

## Ghi chú

- Font Arimo được tải từ Google Fonts lần đầu chạy dev/build (do Slidev quản lý);
  cần mạng ở lần đầu.
- Nội dung chữ và số liệu là dữ liệu minh họa.
