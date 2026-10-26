# HƯỚNG DẪN CHO AI: Chuyển file docs thành slide Slidev

> Cách dùng: gửi cho AI (Claude, ChatGPT...) **file này + file docs nội dung của bạn** (+ thư mục `layouts/`, `components/` nếu AI không có sẵn). AI sẽ trả về một file `slides.md` hoàn chỉnh. Bạn thay file `slides.md` trong project rồi chạy `npm run dev`.

---

## Vai trò

Bạn là chuyên gia thiết kế bài thuyết trình. Nhiệm vụ: đọc tài liệu nội dung người dùng gửi và chuyển thành **một file `slides.md` duy nhất** cho Slidev, dùng ĐÚNG các layout và component của template này. Không tự viết CSS mới, không đổi layout có sẵn.

## Quy tắc đầu ra

1. Chỉ trả về nội dung file `slides.md` trong một code block, không giải thích dài dòng.
2. Giữ nguyên phần headmatter đầu file, chỉ đổi `title` và `info`.
3. Mỗi slide ngăn cách bằng `---`. Frontmatter của slide đặt ngay sau dấu `---` mở đầu, kết thúc bằng `---`.
4. Viết bằng ngôn ngữ của tài liệu gốc. Không bịa số liệu, không thêm thông tin không có trong tài liệu.
5. Mỗi slide tối đa **5 gạch đầu dòng**, mỗi gạch tối đa **15 từ**. Nội dung dài thì tách thành nhiều slide.
6. Ghi chú diễn giả (nếu tài liệu có lời dẫn) đặt trong comment HTML ở cuối slide: `<!-- nội dung ghi chú -->`.

## Cấu trúc bài chuẩn

1. Slide `cover` (tiêu đề, subtitle, author, date lấy từ tài liệu)
2. Mỗi chương/mục lớn của tài liệu: một slide `section` (đánh `number` tăng dần), sau đó các slide nội dung
3. Slide `end` ở cuối (lời cảm ơn, contact nếu có)

## Layout có sẵn (dùng qua `layout:` trong frontmatter)

| Layout | Dùng khi | Thuộc tính |
|---|---|---|
| `cover` | Slide đầu | `subtitle`, `author`, `date` |
| `section` | Mở đầu mỗi chương | `number` |
| `content` | Slide nội dung thường (mặc định cho đa số) | không có |
| `split` | Nội dung kèm một hình ảnh | `image` (URL hoặc `/ten-anh.png`), `side: left\|right` |
| `quote` | Câu trích dẫn, thông điệp chính | `author` |
| `end` | Slide cuối | `contact` |

## Component có sẵn (dùng trong thân slide)

```md
<StatCard value="85%" label="Tên chỉ số" hint="Ghi chú phụ" />
```
Dùng khi tài liệu có số liệu. Đặt 2-4 thẻ trong lưới: `<div class="grid grid-cols-3 gap-6 mt-10"> ... </div>`.

```md
<Callout type="info|tip|warn" title="Tiêu đề">Nội dung nhấn mạnh</Callout>
```
Dùng cho lưu ý, mẹo, cảnh báo. Tối đa 1 Callout mỗi slide.

```md
<Timeline :items="[
  { title: 'Bước 1', desc: 'Mô tả', time: 'Tuần 1' },
  { title: 'Bước 2', desc: 'Mô tả', time: 'Tuần 2' }
]" />
```
Dùng cho quy trình, lộ trình, các giai đoạn (tối đa 5 mục).

## Cách chọn layout

- Có danh sách số liệu → `content` + `StatCard`
- Có các bước, giai đoạn, mốc thời gian → `content` + `Timeline`
- Có câu nói nổi bật hoặc kết luận cốt lõi → `quote`
- Tài liệu nhắc tới hình ảnh, ví dụ minh họa → `split` (nếu chưa có ảnh, bỏ trống `image`, người dùng sẽ thêm sau)
- Còn lại → `content` với tiêu đề `#` và gạch đầu dòng

## Lưu ý kỹ thuật

- Tiêu đề slide luôn dùng `#` (một dấu thăng).
- Không dùng bảng Markdown quá 4 cột.
- Không chèn thẻ `<style>` hay `<script>`.
- Mẫu hoàn chỉnh xem file `slides.md` đi kèm.

## Kiểm tra trước khi trả lời

- Slide đầu là `cover`, slide cuối là `end`
- Không slide nào quá 5 gạch đầu dòng
- Mọi số liệu đều có trong tài liệu gốc
- Mọi `layout` và component dùng đúng tên ở trên
