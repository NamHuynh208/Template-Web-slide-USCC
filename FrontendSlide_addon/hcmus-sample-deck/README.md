# Bộ slide mẫu HCMUS (11 trang)

Bộ trang mẫu được sinh theo đúng hợp đồng của addon `FrontendSlide_addon/hcmus/`
(`design.md` + `preview.md` + `assets/`), phục vụ việc xem trước và đánh giá
template HCMUS trước khi cài vào frontend-slides.

## Cách xem

Mở `index.html` bằng trình duyệt (Chrome/Edge). Không cần server — ảnh nằm sẵn
trong `assets/` cạnh file. Font Inter tải từ Google Fonts khi có mạng; nếu
ngoại tuyến, trình duyệt dùng font sans thay thế.

Trang là một gallery dọc: mỗi slide 1920×1080 tự co theo chiều rộng cửa sổ,
có chú thích mẫu bố cục bên dưới từng trang.

## 11 trang mẫu

| # | Kiểu trang | Điểm nhấn bố cục |
| --- | --- | --- |
| 01 | Bìa (title) | logo-title 780px giữa cao, badge cam, skyline-light + wave-orange + corner-tall |
| 02 | Slide phần 01 | numbox 01, skyline-deep |
| 03 | Nội dung danh sách | h0 "01 / Nền tảng" tại x≈158 y≈78, ba ý phân cách đường xanh |
| 04 | Nội dung 3 thẻ | contentCard trắng viền xanh, một nền skyline-light |
| 05 | Trang số liệu | wave-blue (quy tắc slide dữ liệu), 4 thẻ số liệu |
| 06 | Slide phần 02 | numbox 02, skyline-deep |
| 07 | So sánh hai cột | hai contentCard cân bằng |
| 08 | Timeline | 4 giai đoạn, blueNumberBox + orangeBadge mốc thời gian |
| 09 | Lưới 2×2 | bố cục dày nhất — kiểm tra khoảng thở |
| 10 | Thông điệp | một câu chốt căn giữa, thanh cam nhấn |
| 11 | Kết thúc (closing) | logo-small 150px giữa cao, lời cảm ơn căn giữa |

## Quy tắc đã tuân theo (trích design.md)

- Khung cố định 1920×1080, co toàn khung theo viewport.
- Inter toàn deck; chữ #2D4C9A; tiêu đề 36px/700, nội dung 27px/400.
- Thứ tự lớp: skyline (z0) → wave (z1) → corner ribbon (z2) → nội dung (z3) → logo (z4).
- Mỗi slide dùng tối đa một trong các nền skyline; mọi nền ảnh (trừ ribbon) nằm sát đáy,
  full khung, giữ tỉ lệ gốc `width: 1920px; height: auto`.
- Không vẽ lại logo/wave/ribbon bằng CSS; chỉ dùng ảnh gốc trong `assets/`.
- Nội dung bắt đầu x=128px; nhãn mục h0 tại x≈158px, y≈78px; không đặt nội dung
  quan trọng dưới y≈850; chừa phải ~360px cho ribbon/logo ở slide nội dung.
- Chân trang: ghi chú trắng 27px/700 + số trang, góc phải bên dưới, nằm trong vùng
  sóng đặc (có text-shadow nhẹ vì wave-blue là lớp xanh mờ).

## Ghi chú

- Nội dung chữ (chuyên đề "Khoa học dữ liệu và Ứng dụng", tên diễn giả, số liệu)
  là dữ liệu minh họa, không phải thông tin chính thức.
- Assets được sao chép từ `../hcmus/assets/` theo quy tắc deploy trong design.md
  ("copy the HCMUS image assets next to the generated HTML").
- Thư mục này chỉ là bản xem trước mẫu, không thuộc hợp đồng template-pack
  (`assets/` + `preview.md` + `design.md`) của thư mục `hcmus/`.
