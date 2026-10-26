# USCC — Template slide độc lập (thiết kế Figma)

Bộ slide sinh hoạt Câu lạc bộ Cờ USCC chuyển từ bản thiết kế Figma (`uscc-slides`).
Deck HTML/CSS/JS thuần, **không cần cài đặt, không cần mạng, không dependency**.

## Dùng ngay

Nhấp đúp `index.html` để mở bằng Chrome/Edge.

| Phím | Chức năng |
| --- | --- |
| ← / →, Space, PageUp / PageDown | Chuyển slide |
| Nút ‹ › (góc phải dưới) | Chuyển slide, kèm bộ đếm |

## Cấu trúc

```text
revealjs/
  index.html          # 10 slide + điều hướng; số trang tự đếm
  uscc.css            # Toàn bộ theme: màu, chữ, lưới, bảng, in
  assets/
    uscc-logo.png     # Logo CLB (từ Figma)
    sweep-navy.svg    # Sóng navy lớn phủ khung (nền mọi slide)
    wave-gold.svg     # Dải sóng vàng sát đáy
```

## 10 slide mẫu

1. Bìa — logo trái trên, khối tên trường phải trên, tiêu đề gold
2. Lời chào — căn giữa (logo giữa, eyebrow, tiêu đề gold, lead)
3. Chương trình — lưới 2×2
4. Hai môn cờ — 2 cột
5. Cùng phát triển — 3 cột
6. Điểm hẹn — 3 cột
7. Hành trình — 4 bước (steps)
8. Chỉ số chính — 3 thẻ số liệu kèm thanh tiến độ
9. Trụ cột — 3 cột có nhãn số nhỏ
10. Tổng hợp — bảng hoạt động

## Sửa nội dung

- Chỉnh chữ: mở `index.html`, sửa trong từng `<section class="slide">`.
  Mỗi slide có `<span class="page">` — số trang được script tự điền, không cần sửa tay.
- Thêm slide: nhân bản một `<section>`; số trang và bộ đếm tự cập nhật.
- Đổi màu/font toàn deck: sửa biến ở đầu `uscc.css` (`--navy`, `--blue`, `--gold`...).
- Thay logo/sóng: thay file trong `assets/` giữ nguyên tên.

Thiết kế chuẩn: font Arimo (fallback Arial khi máy không có); nếu cần font chính xác,
tải Arimo về máy hoặc tự nhúng `@font-face` cục bộ — không dùng link font remote.

## Xuất PDF

Nhấn **Ctrl+P / Cmd+P** trong trang, chọn **Save as PDF**, bật in hình nền
và tắt header/footer. CSS in đã xếp các slide dọc thành trang 1280×720.

## Ghi chú

- Nội dung chữ và số liệu là dữ liệu minh họa.
- Bố cốc fluid 16:9: khung `min(100vw, 100vh·16/9)`, chữ theo `clamp()` —
  hiển thị đúng từ màn hình nhỏ tới trình chiếu full HD.
