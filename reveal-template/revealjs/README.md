# USCC — Reveal.js template

Bộ template 6 slide 16:9 cho Câu lạc bộ Cờ USCC, dùng **Reveal.js 5.2.1**.
Giữ logo USCC, wave orange, nền bàn cờ và footer nhỏ của thiết kế hiện tại.
Bản xem hiện tại có nội dung mẫu ít chữ theo yêu cầu: mỗi slide một thông điệp
và vài từ khóa. Đây không phải thông tin hoạt động chính thức. Để trở về slide
trống, xóa nội dung trong `.content-frame` và làm rỗng `.eyebrow` ở header.

## Các file

```text
revealjs/
  index.html          # Soạn nội dung trực tiếp trong từng <section>
  uscc.css            # Theme USCC, bố cục, màu và kiểu chữ
  deck.js             # Cấu hình Reveal.js và thanh điều khiển
  assets/
    uscc-logo.png
    wave-orange.png
    club-footer.png
    inter-400.ttf
    inter-700.ttf
    Inter-OFL.txt
  vendor/
    reveal.js         # Thư viện chính, lưu cục bộ
    reveal.css
    notes.js          # Plugin ghi chú người thuyết trình
    REVEAL-LICENSE.txt
```

## Mở và chỉnh sửa

- Mở `revealjs/index.html` bằng Chrome/Edge. Giữ nguyên các thư mục đi kèm.
- Mở `index.html` **ở thư mục gốc** nếu cần bản một file độc lập, hoạt động ngoại tuyến.
- Không cần cài npm để trình chiếu. Thư viện, ảnh và font đều lưu cục bộ.
- Không sửa `vendor/`; đây là bản phân phối Reveal.js (MIT), đã kiểm tra SHA-512 từ npm.

Các slide là con trực tiếp của `.reveal > .slides`.
Slide đầu có class `cover`, slide cuối có class `closing`, các slide giữa có class `body-slide`.
Logo đầu/cuối ở giữa phía trên; logo của slide nội dung ở góc phải.

Thêm nội dung vào `.content-frame`:

```html
<div class="content-frame">
  <h2><!-- Tiêu đề --></h2>
  <p class="lead"><!-- Đoạn giới thiệu --></p>
  <div class="columns">
    <article class="column">
      <h3><!-- Tiêu đề cột --></h3>
      <p><!-- Nội dung --></p>
    </article>
  </div>
</div>
```

Điền tiêu đề mục vào `<p class="eyebrow">` trong header của slide nội dung.
Ghi chú riêng đặt trong `<aside class="notes">`; ghi chú không hiển thị trên slide.
Nhân bản hoặc xóa một `<section class="slide ...">` để đổi số slide.
Số trang được cập nhật tự động khi mở deck. Không tạo section lồng nhau: template
này dùng một luồng slide ngang để giữ số trang chính xác.

## Phím tắt

| Phím | Chức năng |
| --- | --- |
| ← / →, Space | Chuyển slide |
| Esc / O | Xem tổng quan các slide |
| F | Toàn màn hình |
| B / . | Tạm ẩn trình chiếu |

**Ghi chú người thuyết trình:** cần cho phép popup. Để cửa sổ người thuyết trình
hoạt động ổn định, phục vụ thư mục qua HTTP/localhost; chế độ `file://` có thể bị
trình duyệt chặn giao tiếp giữa các cửa sổ. Trong Figma Make, dùng server sẵn có,
không khởi chạy thêm server phát triển.

## Xuất PDF

1. Nhấn nút **PDF** hoặc phím **P** để mở tab `?print-pdf`.
2. Chờ ảnh và font tải xong, nhấn **Ctrl+P** (macOS: **Cmd+P**).
3. Chọn **Save as PDF**, bật in hình nền và tắt header/footer của trình duyệt.
4. Bản in bao gồm toàn bộ slide, không chỉ slide đang xem.

## Tạo lại bản HTML độc lập

Từ thư mục gốc của dự án, sau khi sửa file trong `revealjs/`:

```sh
pnpm export:reveal
```

Lệnh này ghi lại `index.html` ở thư mục gốc, nhúng toàn bộ thư viện, CSS, JS, ảnh,
font và giấy phép. **Không sửa trực tiếp bản root nếu muốn giữ thay đổi qua lần
export tiếp theo.** Cần Node.js để chạy lệnh export; không cần mạng.

Kiểm tra build của ứng dụng:

```sh
pnpm build
```

## Thiết kế

- Canvas Reveal.js: 1920×1080, tự co theo màn hình.
- Font Inter: tiêu đề 36px, nội dung 27px.
- Chữ xanh `#2D4C9A`; tiêu đề mục cam `#D98323`.
- Theo `design.md`, nhưng giữ các điều chỉnh riêng cho USCC đã thống nhất:
  không thêm logo trường, hình cơ sở hay ribbon góc phải.
- Có sẵn `.columns`, `.split`, `.list`, `.timeline` cho các bố cục nội dung.
- Ảnh và font lấy từ tài sản đã nhúng trong template hiện tại.

Reveal.js: MIT, giấy phép tại `vendor/REVEAL-LICENSE.txt`.
Inter: SIL Open Font License, tại `assets/Inter-OFL.txt`.
