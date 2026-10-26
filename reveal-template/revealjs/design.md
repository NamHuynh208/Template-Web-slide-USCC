---
version: "1.0"
name: "USCC Reveal.js Slide Template"
status: "Current implementation"
description: "Template slide trống cho Câu lạc bộ Cờ USCC: nền trắng, logo USCC, bàn cờ mờ và wave orange. Reveal.js quản lý trình chiếu; có bản HTML độc lập dùng ngoại tuyến."
source:
  slides: "revealjs/index.html"
  theme: "revealjs/uscc.css"
  configuration: "revealjs/deck.js"
  standalone: "index.html"
  exporter: "scripts/export-revealjs.mjs"
  usage: "revealjs/README.md"
colors:
  logoNavy: "#031140"
  text: "#2D4C9A"
  paper: "#FFFFFF"
  workspace: "#EEF0F2"
  accent: "#D98323"
  border: "rgba(45, 76, 154, 0.18)"
typography:
  family: "Inter"
  weights: [400, 700]
  heading: { size: "36px", weight: 700, lineHeight: 1.25 }
  coverClosingTitle: { size: "96px", weight: 700, lineHeight: 1.12, letterSpacing: "-0.035em", align: "center" }
  coverClosingLead: { size: "32px", weight: 400, lineHeight: 1.45, align: "center" }
  body: { size: "27px", weight: 400, lineHeight: 1.45 }
  emphasis: { size: "27px", weight: 700, lineHeight: 1.35 }
  eyebrow: { size: "36px", weight: 700, lineHeight: 1.25, color: "#D98323", letterSpacing: "0.06em", transform: "uppercase" }
  pageNumber: { size: "19.2px", weight: 700, color: "#FFFFFF", letterSpacing: "0.1em" }
layout:
  canvas: { width: 1920, height: 1080, aspectRatio: "16:9" }
  scaling: { engine: "Reveal.js", margin: 0.08, minScale: 0.1, maxScale: 1, center: false }
  slideClasses: ["cover", "body-slide", "closing"]
  defaultSlideCount: 6
  defaultContent: "empty"
  currentPreview: "sparse-mock-content"
assets:
  directory: "revealjs/assets"
  clubLogo: "uscc-logo.png"
  wave: "wave-orange.png"
  footerWordmark: "club-footer.png"
  fonts: ["inter-400.ttf", "inter-700.ttf"]
  fontLicense: "Inter-OFL.txt"
reveal:
  npmVersion: "5.2.1"
  vendorDirectory: "revealjs/vendor"
  transition: "fade"
  transitionSpeed: "fast"
  backgroundTransition: "none"
  notesPlugin: true
  navigation: "horizontal-only"
  pdfMaxPagesPerSlide: 1
  pdfSeparateFragments: false
---

# USCC — Hệ thiết kế slide

## 1. Mục tiêu và phạm vi

Đây là hệ thiết kế của **Câu lạc bộ Cờ USCC — HCMUS Chess Club**, không phải
bộ nhận diện trình chiếu cấp trường. Logo USCC và ngôn ngữ cờ là chủ thể;
HCMUS xuất hiện trong tên thương hiệu của CLB, không phải một hệ logo trường riêng.

Tài liệu này mô tả template đang có trong `revealjs/` và thay thế các quy tắc
HCMUS cũ. Không tự khôi phục các thành phần đã bỏ chỉ vì chúng tồn tại trong
thư mục tham khảo.

**Hướng thị giác:** nền trắng thoáng, chữ xanh royal, nhãn mục cam, logo navy,
bàn cờ phối cảnh mờ ở vùng dưới bên phải, bốn quân cờ tướng nhỏ rải hai bên và vùng dưới
và sóng xanh–cam chạy hết chân slide.

Template mặc định có **6 slide trống**: 1 mở đầu, 4 nội dung và 1 kết thúc.
Không có tiêu đề minh họa, lời chào, nội dung mẫu hay lời cảm ơn được điền sẵn.
Tên loại slide trong `aria-label` chỉ phục vụ khả năng truy cập, không phải nội dung hiển thị.

**Bản xem hiện tại:** theo yêu cầu riêng của người dùng, 6 slide đang có nội dung
mẫu phong cách ít chữ để đánh giá bố cục: mỗi slide một thông điệp, tối đa ba ý
ngắn hoặc bốn mốc hành trình. Đây là dữ liệu minh họa, không phải thông tin hoạt
động chính thức. Khi trả về template trống, xóa nội dung trong `.content-frame`
và làm rỗng `.eyebrow` ở header; giữ nguyên nền, logo, footer và các phần tử định vị.

## 2. File nguồn và nguyên tắc chỉnh sửa

| File | Vai trò |
| --- | --- |
| `revealjs/index.html` | Nguồn soạn slide; mỗi slide là một `<section>` |
| `revealjs/uscc.css` | Màu, kiểu chữ, bố cục, nền và footer |
| `revealjs/deck.js` | Cấu hình Reveal.js, điều khiển, đếm trang và liên kết PDF |
| `revealjs/assets/` | Logo, wave và font cục bộ |
| `revealjs/vendor/` | Reveal.js, CSS lõi, plugin notes và giấy phép MIT |
| `scripts/export-revealjs.mjs` | Nhúng các tài nguyên để tạo bản một file |
| `index.html` ở thư mục gốc | Bản HTML độc lập được sinh từ bộ file nguồn |

Chỉnh sửa trong `revealjs/`, không sửa trực tiếp bản HTML gốc đã sinh nếu muốn
thay đổi được giữ lại qua lần export sau. Không chỉnh các file trong `vendor/`.

## 3. Màu sắc

| Token CSS | Giá trị | Sử dụng |
| --- | --- | --- |
| `--navy` | `#031140` | Tông nhận diện navy, họa tiết bàn cờ và lớp tạm ẩn trình chiếu |
| `--ink` | `#2D4C9A` | Tiêu đề, đoạn văn, danh sách, số thứ tự trong nội dung |
| `--paper` | `#FFFFFF` | Nền slide; màu chữ/số trang trên wave |
| `--workspace` | `#EEF0F2` | Vùng ngoài slide trên màn hình; không phải màu nền slide |
| `--accent` | `#D98323` | Nhãn mục `.eyebrow`, đường nhấn và nút mốc timeline |
| `--line` | `rgba(45, 76, 154, 0.18)` | Đường phân cách, viền nhẹ |

- Phân biệt **navy của logo** và **xanh royal của nội dung**; không đổi toàn bộ chữ sang navy.
- Chữ nội dung chính dùng xanh royal, không dùng xám than/xám ấm của phương án thử trước.
- Nhãn mục màu cam là ngoại lệ có chủ đích. Không tô cam toàn bộ đoạn văn.
- Footer trên wave dùng trắng để có độ tương phản.
- Wave và logo dùng ảnh gốc; không áp một màu CSS mới lên toàn bộ các tài sản này.
  Ngoại lệ: wordmark chân trang dùng `brightness(0) invert(1)` để chuyển sang trắng.

## 4. Kiểu chữ

Mọi kích thước dưới đây tính trên **canvas 1920×1080**, sau đó Reveal.js thu phóng
đồng nhất cả slide. Không đổi sang cỡ chữ theo viewport của trình duyệt.

| Vai trò | Cỡ chữ | Độ đậm | Giãn dòng | Màu |
| --- | --- | --- | --- | --- |
| Tiêu đề slide nội dung, `h2`, `h3` | 36px | 700 | 1.25 | Xanh royal |
| Tiêu đề chính mở đầu/kết thúc | 96px | 700 | 1.12 | Xanh royal |
| Mô tả mở đầu/kết thúc | 32px | 400 | 1.45 | Xanh royal |
| Nội dung, đoạn giới thiệu, chú thích | 27px | 400 | 1.45 | Xanh royal |
| Nhấn mạnh và `.number` | 27px | 700 | 1.35 | Xanh royal |
| `.eyebrow` | 36px | 700 | 1.25 | Cam |
| `.page-number` | 19.2px | 700 | Kế thừa | Trắng |

- Chỉ dùng **Inter**; font thường và đậm nằm tại `assets/inter-400.ttf` và `assets/inter-700.ttf`.
- Nhãn `.eyebrow` viết hoa bằng CSS, giãn chữ `0.06em`.
- Số trang giãn chữ `0.1em`, nhỏ hơn chữ nội dung.
- Theo yêu cầu riêng, mở đầu/kết thúc dùng tiêu đề hero 96px, giãn chữ `-0.035em`,
  mô tả 32px. Nhãn phụ của mở đầu nhỏ hơn, 24px. Không áp các cỡ này cho slide nội dung.
- Dòng “HCMUS CHESS CLUB” ở chân slide là **wordmark dạng ảnh**, không phải text HTML;
  thay đổi kích thước bằng chiều rộng ảnh, không bằng `font-size`.
- Giữ font cục bộ để trình chiếu ngoại tuyến; không thêm Google Fonts CDN.

## 5. Canvas, lưới và vùng an toàn

Reveal.js dùng khung cố định `width: 1920`, `height: 1080`, `center: false`.
Nội dung được đặt theo tọa độ của slide; Reveal.js lo thu phóng và vị trí slide
trong màn hình, không tự căn giữa từng khối nội dung.

### Header

- `.header`: `top: 7%`, `left: 6.6%`, `right: 10%`.
- Trên canvas gốc, mép trái khoảng **127px**, mép trên khoảng **76px**.
- Bố cục header dùng flex, căn giữa theo chiều dọc.
- Logo `.uscc-logo` rộng **18% của header**, không phải 18% toàn slide; giữ `height: auto`.
- Ở slide mở đầu/kết thúc, header đổi `right: 6.6%` và `justify-content: center`
  để logo nằm đúng trục giữa slide.

### Vùng nội dung

| Loại slide | Trên | Trái | Phải | Dưới | Căn chữ |
| --- | --- | --- | --- | --- | --- |
| Mở đầu `.cover` | 22% | 6.6% | 6.6% | 33% | Giữa |
| Nội dung `.body-slide` | 22% | 6.6% | 14% | 30% | Trái |
| Kết thúc `.closing` | 22% | 6.6% | 6.6% | 33% | Giữa |

- Tiêu đề và đoạn văn nằm trong `.content-frame`.
- Tiêu đề mục của slide nội dung nằm **trong header**, phía trên tiêu đề chính.
- Giữ nội dung quan trọng trong vùng trên khoảng **70% chiều cao slide** (y≈756px).
  Không đặt chữ lên wave hoặc dồn nội dung xuống vùng bàn cờ.
- `.content-frame` là khung định vị, không tự kiểm soát tràn nội dung. Khi nội dung dài,
  tách slide hoặc giảm lượng chữ; không thu nhỏ tùy tiện dưới chuẩn 27px.

## 6. Ba loại slide

### Mở đầu — `.slide.cover`

- Logo USCC căn giữa phía trên.
- Không có cụm tên trường và tên CLB ở góc trên phải.
- Vùng nội dung trống; khi được yêu cầu, điền tiêu đề và mô tả bên dưới logo.
- Nội dung căn giữa cả ngang và dọc trong khung bằng flex; tiêu đề chính 96px,
  tối đa 1400px, mô tả 32px, nhãn phụ 24px. Ưu tiên một thông điệp ngắn, to rõ.
- Giữ nền bàn cờ, wave orange và hai thành phần footer.

### Nội dung — `.slide.body-slide`

- Logo USCC ở góc trên bên phải.
- Chừa một `.eyebrow` trống ở góc trên bên trái để điền tên mục màu cam.
  Giữ phần tử này ngay cả khi chưa có chữ để bảo toàn bố cục header.
- Không thêm cụm tên trường hoặc tên CLB cạnh logo.
- Tiêu đề chính và nội dung đặt bên dưới trong `.content-frame`.
- Có thể dùng bố cục cột, chia đôi, danh sách hoặc timeline khi có nội dung thật.

### Kết thúc — `.slide.closing`

- Logo USCC căn giữa phía trên, cùng nhịp với slide mở đầu.
- Vùng nội dung căn giữa cả ngang và dọc trong khung, tiêu đề chính 96px;
  mô tả 32px được căn giữa bằng margin tự động.
- Không điền sẵn “Cảm ơn”, hỏi đáp hay thông tin liên hệ trong template trống.
- Không có cụm tên trường và tên CLB ở góc trên phải.

## 7. Tài sản và các lớp nền

### Tài sản đang dùng

| File trong `revealjs/assets/` | Class | Vai trò |
| --- | --- | --- |
| `uscc-logo.png` | `.uscc-logo` | Logo chính của CLB |
| `wave-orange.png` | `.wave-orange` | Sóng xanh–cam ở chân mọi slide |
| `club-footer.png` | `.footer-logo` | Wordmark “HCMUS CHESS CLUB” |
| `inter-400.ttf`, `inter-700.ttf` | `@font-face` | Font Inter cục bộ |

Không dùng `wave-blue.png` trong phiên bản hiện tại. Không bắt buộc lấy tài nguyên
trong `uscc-slide-deck-download/`; bộ `revealjs/assets/` đã có đủ các file cần thiết.

### Bàn cờ mờ — `.chessboard`

Bàn cờ là **họa tiết CSS**, không phải logo hay ảnh nhận diện cần tái tạo.

- Nằm dưới cùng: `z-index: 0`, `right: 6%`, `bottom: -24%`.
- Rộng `44%` slide, tỉ lệ `1:1`, ô cờ tạo bằng `conic-gradient`.
- Phối cảnh: `perspective(960px) rotateX(56deg) rotateZ(-16deg)`.
- Màu navy, `opacity: 0.1`; viền mảnh 1px.
- Được cắt theo biên slide và che một phần bởi wave.
- Không có quân mã lớn, dải ô cờ nhỏ ở footer hay bàn cờ phụ ở góc phải trên.

### Quân cờ tướng mờ — `.xiangqi-piece`

- Ba quân **Xe (車), Sĩ (士), Tốt (卒)** dạng đĩa tròn, hai vòng viền mảnh, ký tự vẽ bằng path SVG.
- SVG nhúng trực tiếp trong từng slide; không cần font chữ Hán hay tài nguyên ngoài.
- Vị trí, kích thước và góc nghiêng khác nhau để tạo cảm giác rải rác, không xếp thành hàng:

| Quân / class | Top | Vị trí ngang | Width | Góc nghiêng | Opacity |
| --- | --- | --- | --- | --- | --- |
| Xe / `.xiangqi-piece--rook` | 55% | left: 5% | 8% | -12deg | 0.1 |
| Sĩ / `.xiangqi-piece--advisor` | 29% | right: 3%, left: auto | 5.4% | -24deg | 0.07 |
| Tốt / `.xiangqi-piece--pawn` | 76% | left: 20% | 6.8% | -22deg | 0.08 |

- Các quân dùng `translateY(-50%)` để định vị tâm theo giá trị top.
- Navy, `z-index: 0`, cùng sắc độ nhẹ với bàn cờ.
- Không nhận tương tác; dùng `aria-hidden="true"` và `focusable="false"`.
- Đây là các họa tiết nhỏ độc lập, không phải quân mã lớn đặt lên bàn cờ.

### Wave orange — `.wave-orange`

- Dùng ảnh gốc; không vẽ lại bằng CSS, SVG hay gradient tự tạo.
- `left: 0`, `right: 0`, `bottom: 0`, `width: 100%`, `height: auto`.
- Giữ nguyên tỉ lệ ảnh, không ép chiều cao 24% hay kéo méo wave.
- `z-index: 1`, ở trên bàn cờ nhưng dưới nội dung và logo.

### Thứ tự lớp

| Lớp | z-index |
| --- | --- |
| Bàn cờ mờ và quân cờ tướng nhỏ | 0 |
| Wave orange | 1 |
| Nội dung | 3 |
| Header/logo, wordmark footer, số trang | 4 |

Mỗi slide có `isolation: isolate` và `overflow: hidden`.
Nền trang trí không nhận tương tác; ảnh trang trí dùng `alt=""` và `aria-hidden="true"`.
Logo và wordmark giữ văn bản thay thế có nghĩa.

## 8. Footer

Cả hai thành phần đã được thu nhỏ theo thiết kế cuối cùng:

- **Số trang bên trái:** `left: 6.6%`, `bottom: 2.7%`, Inter đậm 19.2px, màu trắng.
- **Wordmark bên phải:** `right: 6.6%`, `bottom: 2.7%`, rộng **13.5% toàn slide**,
  cao tự động, chuyển sang trắng bằng CSS filter.
- Số trang theo dạng `01 / 06`; `deck.js` tự tính lại khi mở deck và chuyển slide.
- Không thêm đường viền, dải ô cờ nhỏ, tagline hay nội dung mẫu vào footer.

## 9. Các bố cục nội dung có sẵn

Những class này được chuẩn bị trong CSS nhưng **không hiển thị nội dung mẫu**:

| Class | Cấu trúc và khoảng cách chính |
| --- | --- |
| `.lead` | Đoạn giới thiệu, cách tiêu đề 25px, rộng tối đa 1190px; cover tối đa 922px |
| `.meta` | Thông tin phụ, cách phần trên 35px |
| `.columns` / `.column` | 3 cột bằng nhau, gap 48px, cách phần trên 42px, đường nhấn cam |
| `.split` / `.statement` | 2 cột bằng nhau, gap 77px; statement có đường cam bên trái |
| `.list` | Danh sách không bullet, phân cách bằng đường xanh nhạt |
| `.timeline` / `.phase` | 4 cột, gap 38px, nút mốc cam và đường nối nhẹ |

Ưu tiên khoảng trắng và đường phân cách hơn thẻ nổi. Không coi các card bo góc,
shadow hoặc number box của tài liệu HCMUS cũ là thành phần bắt buộc của template này.

## 10. Reveal.js và tương tác

- Dùng các slide ngang là con trực tiếp của `.reveal > .slides`.
- Không lồng section thành slide dọc nếu chưa cập nhật lại cơ chế đếm trang.
- Reveal.js quản lý hiển thị slide, hash URL, keyboard, touch, tổng quan và bố cục PDF.
  Không khôi phục cơ chế `.active` và điều khiển slide tự viết trước đây.
- Cấu hình hiện tại: chuyển cảnh `fade`, tốc độ `fast`, nền không chuyển cảnh.
- Tắt controls, progress và số trang mặc định của Reveal.js; dùng toolbar và footer USCC.
- Toolbar `.deck-toolbar` chỉ gồm nút slide trước, slide sau và fullscreen;
  nằm ngoài canvas, ở giữa phía dưới màn hình và phải ẩn khi in.
- Khi fullscreen, toolbar được ẩn để slide phủ toàn bộ màn hình.
- Nút trước/sau bị vô hiệu hóa ở hai đầu; không tự lặp vòng slide.

| Phím | Tác dụng |
| --- | --- |
| ← / →, Space | Chuyển slide |
| Esc / O | Xem tổng quan |
| F | Toàn màn hình |
| B / . | Tạm ẩn trình chiếu |

Ghi chú vẫn được giữ trong `<aside class="notes">` cho khả năng mở rộng,
nhưng không hiển thị trong giao diện người xem.

## 11. Xuất bản và dùng ngoại tuyến

### Bản nhiều file

Lấy **toàn bộ thư mục `revealjs/`**, giữ nguyên `assets/`, `vendor/`, CSS và JS.
Mở `revealjs/index.html` để trình chiếu; không cần npm hay mạng để xem slide.

### Bản một file

Sau khi chỉnh nguồn, chạy ở thư mục gốc:

```sh
pnpm export:reveal
```

Exporter ghi lại **`index.html` ở thư mục gốc**, nhúng CSS, Reveal.js, plugin notes,
JS cấu hình, ảnh, font và giấy phép. Đây là file có thể mang đi riêng lẻ để trình chiếu
ngoại tuyến. Không đổi sang phụ thuộc CDN.

Giữ các thẻ liên kết CSS và script trong HTML nguồn theo cấu trúc hiện có, vì exporter
nhận diện chúng để nhúng tài nguyên. Khi thêm định dạng tài nguyên mới, cập nhật exporter.

### PDF

Nhấn **P** hoặc **PDF**, chờ tab `?print-pdf` tải xong, rồi dùng **Ctrl+P / Cmd+P**.
Chọn lưu PDF, bật in hình nền và tắt header/footer của trình duyệt.
`pdfMaxPagesPerSlide: 1`, `pdfSeparateFragments: false`; toolbar không xuất hiện trong bản in.

### Kiểm tra khi thay đổi template

- Kiểm tra cả ba bố cục: mở đầu, nội dung, kết thúc.
- Logo đúng vị trí; wave không méo; nội dung không đè lên header/footer.
- Ảnh và font tải được khi không có mạng.
- Chuyển slide, đếm trang, nút trước/sau và hash URL hoạt động.
- PDF đủ số trang, có hình nền và không có toolbar.
- Sau thay đổi mã nguồn cần kiểm tra build, dùng đúng lệnh của dự án:

```sh
pnpm build
```

Tài liệu thuần túy không yêu cầu chạy lại build hay khởi động server phát triển.
Server của Figma Make đã có sẵn.

## 12. Những điều không được tự ý đưa lại

- Logo trường HCMUS, logo VNUHCM, ảnh cơ sở, skyline hoặc building line art.
- Ribbon/họa tiết xanh dọc góc trên phải.
- Bàn cờ phụ góc trên phải, dải ô cờ nhỏ dưới chân hoặc quân mã lớn.
- Cụm tên trường và tên CLB cạnh logo của slide đầu/cuối.
- Nội dung mẫu, tiêu đề giả, lời chào/lời cảm ơn mặc định.
- Font khác Inter, tiêu đề hero trên slide nội dung, bảng màu tím, nền tối hay glassmorphism.
- Thay logo hoặc wave gốc bằng chữ giả, hình vẽ gần giống hoặc gradient tự dựng.

Chỉ thay đổi các quyết định này khi người dùng yêu cầu rõ ràng. Khi có thay đổi thiết kế
được chấp thuận, cập nhật **cả nguồn trong `revealjs/` và tài liệu này**, rồi export lại
bản HTML độc lập.
