# Template reveal.js tái sử dụng (không cần cài đặt, không cần gõ lệnh)

## 1. Dùng ngay

Giải nén, nhấp đúp file `slides.html`. Trình duyệt mở ra bài thuyết trình mẫu.

- Chuyển slide: phím mũi tên hoặc cách (Space)
- Xem tất cả slide: phím `O`
- Toàn màn hình: phím `F`
- Ghi chú diễn giả: phím `S`
- Xuất PDF: thêm `?print-pdf` vào cuối địa chỉ trên thanh trình duyệt (ví dụ `file:///.../slides.html?print-pdf`), nhấn Ctrl+P rồi chọn Lưu thành PDF (bật "Background graphics", lề "None")

Thư viện reveal.js đã nằm sẵn trong thư mục `lib/` nên **chạy được khi không có mạng**. Chỉ phần font chữ Be Vietnam Pro cần mạng; không có mạng thì trình duyệt tự dùng font hệ thống thay thế.

## 2. Làm bài mới bằng AI (quy trình lặp lại nhiều lần)

1. Viết nội dung vào một file docs (Word, Google Docs, Markdown...). Xem mẫu `CONTENT_EXAMPLE.md`.
2. Gửi cho AI **ba thứ**: file docs, file `AI_PROMPT.md`, file `slides.html` mẫu.
3. AI trả về nội dung file `slides.html` mới. Lưu thành file (ví dụ `bai-thang-10.html`) **trong cùng thư mục** với `theme.css`, `lib/`, `images/`.
4. Nhấp đúp file đó để xem. Cần sửa chữ thì mở bằng Notepad hoặc VS Code, sửa trong phần giữa thẻ `<textarea>`.

Mỗi bài mới chỉ là một file `.html` mới, dùng chung `theme.css`. Bạn không cần cài hay chạy lệnh nào.

Ảnh: bỏ vào thư mục `images/` rồi gọi bằng `![](images/ten-anh.png)`.

## 3. Cấu trúc thư mục

```
slides.html        bài thuyết trình (AI sinh ra file kiểu này)
theme.css          MÀU, FONT, BO GÓC và kiểu từng loại slide: sửa ở đây để đổi giao diện
images/            ảnh dùng trong bài
lib/               thư viện reveal.js (không cần đụng vào)
AI_PROMPT.md       hướng dẫn cho AI
CONTENT_EXAMPLE.md mẫu file docs nội dung
```

## 4. Chia sẻ bài thuyết trình

- **Gửi cho người khác:** nén cả thư mục thành file zip. Người nhận giải nén rồi nhấp đúp `slides.html`.
- **Gửi dạng link:** kéo thả cả thư mục lên Netlify (hoặc GitHub Pages, Cloudflare Pages). Bạn nhận một đường link ai cũng mở được.
- **Gửi dạng một file:** xuất PDF như mục 1.

## 5. Thiết kế giao diện dễ như Canva

Giao diện nằm trong `theme.css`. Từ dễ đến khó:

### Cách A: Đổi bảng màu và font (5 phút)
Mở `theme.css`, sửa các biến ở khối `:root` ở đầu file (`--c-primary`, `--c-accent`, `--c-dark`, `--f-heading`...). Toàn bộ slide đổi theo. Lấy mã màu từ Canva Color Palette Generator, Coolors hoặc Adobe Color.

### Cách B: Dùng Canva làm nền
1. Trong Canva tạo trang 1920x1080, thiết kế nền (hình khối, họa tiết, logo), **không đặt chữ**.
2. Tải về PNG, bỏ vào thư mục `images/`, ví dụ `images/nen-cover.png`.
3. Trong `theme.css`, thêm vào mục `.reveal section.cover` cho slide mở đầu:
   ```css
   .reveal section.cover { background: url('images/nen-cover.png') center/cover; }
   ```
   Nếu nền chưa hiện, mở `slides.html` và bỏ `cover` ra khỏi danh sách `bg` trong đoạn script cuối file để nó không bị phủ màu gradient.
4. Chữ vẫn do reveal.js hiển thị, nên AI vẫn sinh nội dung bình thường và chữ vẫn sửa được.

### Cách C: Thiết kế ở Figma hoặc Penpot rồi copy CSS
- **Penpot** (miễn phí, mã nguồn mở) và **Figma** có chế độ xem thuộc tính (Inspect / Dev Mode) cho ra CSS của từng khung: màu, bo góc, đổ bóng, khoảng cách, cỡ chữ.
- Vẽ khung 1280x720, copy CSS của phần tử bạn muốn, dán vào `theme.css` cho đúng class.

### Cách D: Nhờ AI làm cầu nối (nhanh nhất nếu không rành code)
1. Chụp ảnh slide mẫu bạn thích (Canva, Pinterest, PowerPoint...).
2. Gửi AI cùng file `theme.css` và ảnh chụp slide hiện tại, yêu cầu: "Sửa `theme.css` để slide giống ảnh mẫu này, giữ nguyên tên class và các biến ở `:root`".
3. Thay file `theme.css`, tải lại trang (F5), xem kết quả, chụp lại và yêu cầu chỉnh tiếp. Lặp 3-5 lần là đẹp.

### Cách E: Tinh chỉnh ngay trên trình duyệt
Mở slide, nhấn F12, chuột phải vào phần tử rồi chọn Inspect. Sửa CSS trực tiếp để thấy kết quả ngay, rồi chép giá trị ưng ý vào `theme.css`.

| Bạn là... | Nên dùng |
|---|---|
| Không biết code, chỉ muốn đổi màu | A |
| Quen Canva, muốn nền đẹp | B (cùng A) |
| Là designer, quen Figma | C |
| Muốn nhanh, chấp nhận thử sai | D |

## 6. Thêm kiểu slide mới

1. Trong `theme.css` thêm một khối `.reveal section.ten-kieu { ... }`, dùng biến màu (`var(--c-primary)`...) để đồng bộ.
2. Gọi trong slide bằng dòng `<!-- .slide: class="ten-kieu" -->`.
3. Nếu kiểu mới cần nền toàn màn hình, thêm vào danh sách `bg` trong đoạn script cuối `slides.html`.
4. **Cập nhật bảng kiểu slide trong `AI_PROMPT.md`** để AI biết kiểu mới.

## 7. Lưu ý

- Các khối đặc biệt (thẻ số liệu, timeline, callout) viết bằng HTML thuần. Không có component dạng Vue như Slidev, nhưng đổi lại không cần cài đặt gì.
- Trong nội dung Markdown, nhớ để **dòng trống** trước khối HTML hoặc ảnh đi sau danh sách gạch đầu dòng, nếu không khối đó bị dính vào dòng trên.
- Không thụt lề đầu dòng trong phần `<textarea>`.
- Mình đã chạy thử bằng trình duyệt không giao diện (Chromium) khi mở trực tiếp file từ ổ đĩa và 9 slide mẫu hiển thị đúng. Chưa thử trên Safari và Firefox.
