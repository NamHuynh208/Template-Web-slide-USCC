# Template Slidev tái sử dụng

## 1. Chạy thử

```bash
npm install
npm run dev          # mở http://localhost:3030
npm run build        # xuất web tĩnh (thư mục dist)
npm run export       # xuất PDF (cần playwright-chromium)
npm run export-pptx  # xuất PowerPoint (dạng ảnh)
```

Cần Node.js 18 trở lên.

## 2. Quy trình dùng lại nhiều lần

1. Viết nội dung vào một file docs (Word, Google Docs, Markdown...). Xem mẫu `CONTENT_EXAMPLE.md`.
2. Gửi cho AI: file docs + file `AI_PROMPT.md` (nếu AI không đọc được thư mục thì gửi thêm `slides.md` mẫu).
3. AI trả về nội dung `slides.md`. Dán đè vào file `slides.md` trong project.
4. `npm run dev` để xem, sửa nhanh bằng tay nếu cần, rồi `npm run export`.

Mẹo: giữ nguyên thư mục `layouts/`, `components/`, `styles/`. Mỗi bài mới chỉ thay `slides.md` (và thư mục `public/` chứa ảnh).

## 3. Cấu trúc project

```
slides.md                nội dung bài (AI sinh ra file này)
styles/tokens.css        MÀU, FONT, BO GÓC: sửa ở đây để đổi toàn bộ giao diện
styles/index.css         style chung (chữ, gạch đầu dòng, link)
layouts/*.vue            cover, section, content, split, quote, end
components/*.vue         StatCard, Callout, Timeline
public/                  ảnh, logo (tự tạo thư mục khi cần)
AI_PROMPT.md             hướng dẫn cho AI
```

## 4. Thiết kế giao diện dễ như Canva

Slidev là code (Vue + CSS) nên không có giao diện kéo thả sẵn. Cách thực tế nhất là **thiết kế trực quan ở công cụ khác, rồi lấy giá trị đưa vào template**. Từ dễ đến khó:

### Cách A: Chỉ đổi `tokens.css` (dễ nhất, 5 phút)
Mở `styles/tokens.css`, đổi mã màu và font. Toàn bộ layout đổi theo. Chọn bảng màu bằng Canva Color Palette Generator, Coolors hoặc Adobe Color rồi dán mã hex vào.

### Cách B: Thiết kế nền ở Canva, dùng làm hình nền layout
1. Trong Canva tạo trang 1920x1080, thiết kế nền (hình khối, họa tiết, logo), **không đặt chữ**.
2. Tải về PNG hoặc SVG, bỏ vào `public/bg/cover.png`.
3. Trong `layouts/cover.vue` thêm vào `.cover`:
   ```css
   background: url('/bg/cover.png') center/cover;
   ```
4. Chữ vẫn do Slidev render, nên AI sinh nội dung được và chữ vẫn sửa được.

Đây là cách gần Canva nhất mà vẫn giữ được khả năng tự động hóa.

### Cách C: Thiết kế layout ở Figma hoặc Penpot, copy CSS
- **Penpot** (miễn phí, mã nguồn mở) và **Figma** đều có chế độ xem thuộc tính (Inspect / Dev Mode) cho ra CSS của từng khung: màu, bo góc, đổ bóng, khoảng cách, cỡ chữ.
- Cách làm: vẽ khung 1280x720, copy CSS của từng phần tử, dán vào khối `<style scoped>` của file layout `.vue`.
- Hoặc chụp ảnh thiết kế rồi gửi AI kèm file layout hiện tại, yêu cầu: "Viết lại `layouts/cover.vue` giống thiết kế này, dùng biến trong `tokens.css`".

### Cách D: Nhờ AI làm cầu nối (nhanh nhất cho người không rành code)
1. Chụp ảnh slide mẫu bạn thích (Canva, Pinterest, PowerPoint...).
2. Gửi AI cùng file layout `.vue` cần sửa và ảnh chụp màn hình slide hiện tại.
3. Yêu cầu: "Chỉnh layout này giống ảnh mẫu, giữ nguyên props và `<slot />`, dùng biến CSS trong tokens.css".
4. Mở `npm run dev`, xem kết quả, chụp lại, yêu cầu chỉnh tiếp. Lặp 3-5 lần là đẹp.

### Cách E: Tinh chỉnh trực tiếp ngay trên trình duyệt
- Khi `npm run dev` đang chạy, nhấn F12, chuột phải vào phần tử, **Inspect**, sửa CSS trực tiếp để thấy kết quả ngay, rồi copy giá trị ưng ý vào file `.vue`.
- Slidev có sẵn **Tailwind-like utility (UnoCSS)**: viết trực tiếp trong slide như `class="grid grid-cols-3 gap-6 text-center"` mà không cần file CSS.
- Cài tiện ích **Vue.js devtools** trên trình duyệt để xem cấu trúc component.

### Gợi ý chọn cách nào?

| Bạn là... | Nên dùng |
|---|---|
| Không biết code, chỉ muốn đổi màu | A |
| Quen Canva, muốn nền đẹp | B (+ A) |
| Là designer, quen Figma | C |
| Muốn nhanh, chấp nhận thử sai | D |

## 5. Thêm layout mới

1. Tạo `layouts/ten-layout.vue`, có `<slot />` để nhận nội dung và `defineProps` cho các thuộc tính frontmatter.
2. Dùng màu, bo góc qua `var(--c-primary)`, `var(--radius)`... để đồng bộ.
3. Gọi trong slide: `layout: ten-layout`.
4. **Cập nhật bảng layout trong `AI_PROMPT.md`** để AI biết layout mới.

## 6. Lưu ý

- Font Be Vietnam Pro được tải từ Google Fonts khi chạy `dev` hoặc `build`, cần có mạng lần đầu.
- Export PPTX của Slidev chỉ ra dạng ảnh từng slide, không sửa chữ được trong PowerPoint. Cần file sửa được thì xuất PDF hoặc dùng bản web.
- Bản mẫu chưa được chạy thử trên máy bạn, nếu gặp lỗi hãy gửi nội dung lỗi để mình chỉnh.
