---
theme: none
title: Tên bài thuyết trình
info: Template Slidev tái sử dụng
aspectRatio: 16/9
canvasWidth: 1280
fonts:
  sans: Be Vietnam Pro
  mono: JetBrains Mono
transition: slide-left
mdc: true
---

---
layout: cover
subtitle: Phụ đề ngắn gọn mô tả bài thuyết trình
author: Tên diễn giả
date: 19/10/2026
---

# Tiêu đề chính của bài thuyết trình

---
layout: section
number: 1
---

# Phần 1: Tổng quan

Một câu mô tả ngắn cho phần này

---
layout: content
---

# Các điểm chính

- Điểm quan trọng thứ nhất
- Điểm quan trọng thứ hai
- Điểm quan trọng thứ ba

<Callout type="tip" title="Mẹo">
Dùng component Callout để nhấn mạnh một ý.
</Callout>

---
layout: content
---

# Số liệu nổi bật

<div class="grid grid-cols-3 gap-6 mt-10">
  <StatCard value="85%" label="Tỉ lệ hoàn thành" hint="So với kỳ trước" />
  <StatCard value="1.2K" label="Người tham gia" />
  <StatCard value="4.8/5" label="Mức hài lòng" />
</div>

---
layout: split
image: https://images.unsplash.com/photo-1519389950473-47ba0277781c?w=1200
side: right
---

# Nội dung kèm hình ảnh

- Chữ bên trái, ảnh bên phải
- Đổi `side: left` để đảo bên

---
layout: content
---

# Lộ trình thực hiện

<Timeline :items="[
  { title: 'Chuẩn bị', desc: 'Thu thập nội dung', time: 'Tuần 1' },
  { title: 'Triển khai', desc: 'Thực hiện kế hoạch', time: 'Tuần 2-3' },
  { title: 'Tổng kết', desc: 'Đánh giá kết quả', time: 'Tuần 4' }
]" />

---
layout: quote
author: Tên người nói
---

Một câu trích dẫn ngắn, đáng nhớ.

---
layout: end
contact: email@example.com
---

# Cảm ơn!

Xin mời đặt câu hỏi
