---
theme: none
title: USCC — Bộ slide sinh hoạt câu lạc bộ
info: Template USCC theo thiết kế Figma
aspectRatio: 16/9
canvasWidth: 1280
fonts:
  sans: Arimo
  mono: JetBrains Mono
transition: slide-left
mdc: true
---

---
layout: cover
eyebrow: SINH HOẠT CÂU LẠC BỘ · HỌC KỲ MỚI
note: USCC · HCMUS Chess Club — Nội dung minh họa
---

<h1><span>Cùng</span> đam mê.<br /><i>tiến một nước.</i></h1>

Chào mừng bạn đến với USCC — nơi kết nối những người yêu cờ, cùng học hỏi và trưởng thành qua từng ván đấu.

---
layout: section
eyebrow: USCC · GẶP GỠ ĐẦU NĂM
---

# Cùng đam mê.<br />Cùng tiến một nước.

<p class="lead">Chào mừng bạn đến với USCC.</p>

---
layout: content
eyebrow: 07 / Chương trình
---

## Chương trình hôm nay.

<div class="grid grid-cols-2 gap-x-11 gap-y-6">

<article>

### 01 · Chào mừng

Giới thiệu câu lạc bộ và các hoạt động

</article>

<article>

### 02 · Lịch sinh hoạt

Thời gian, địa điểm và nội quy

</article>

<article>

### 03 · Giải đấu nội bộ

Thể thức cờ vua và cờ tướng

</article>

<article>

### 04 · Giao lưu

Kết nối thành viên bên bàn cờ

</article>

</div>

---
layout: content
eyebrow: 01 / Chúng mình
---

## Hai môn cờ. Một cộng đồng.

<div class="grid grid-cols-2 gap-x-11">

<article>

### Cờ vua

Tư duy · Chiến thuật

</article>

<article>

### Cờ tướng

Bản lĩnh · Sáng tạo

</article>

</div>

---
layout: content
eyebrow: 02 / Cùng phát triển
---

## Mỗi ván cờ, một bước tiến.

<div class="grid grid-cols-3 gap-x-11">

<article>

### Học hỏi

Thêm một góc nhìn.

</article>

<article>

### Kết nối

Thêm một người bạn.

</article>

<article>

### Thử sức

Thêm một trải nghiệm.

</article>

</div>

---
layout: content
eyebrow: 03 / Điểm hẹn
---

## Hẹn nhau bên bàn cờ.

<div class="grid grid-cols-3 gap-x-11">

<article>

### Tập luyện

Rèn từng nước đi.

</article>

<article>

### Giao lưu

Gặp những đồng đội mới.

</article>

<article>

### Thi đấu

Chơi hết mình.

</article>

</div>

---
layout: content
eyebrow: 04 / Hành trình
---

## Từng bước, cùng nhau.

<Timeline :items="[
  { title: 'Làm quen' },
  { title: 'Luyện tập' },
  { title: 'Thử thách' },
  { title: 'Tiến bộ' }
]" />

---
layout: content
eyebrow: 08 / Chỉ số chính
---

## Con số nổi bật.

<div class="grid grid-cols-3 gap-x-11">

<StatCard value="120+" label="Thành viên đang sinh hoạt" :progress="76" color="gold" />

<StatCard value="02" label="Môn cờ: cờ vua và cờ tướng" :progress="62" color="navy" />

<StatCard value="12" label="Buổi sinh hoạt mỗi học kỳ" :progress="88" color="blue" />

</div>

---
layout: content
eyebrow: 09 / Trụ cột
---

## Ba trụ cột phát triển.

<div class="grid grid-cols-3 gap-x-11 pillars">

<article>

<b>01</b>

### Kết nối

Gắn kết thành viên qua các buổi giao lưu và sinh hoạt định kỳ.

</article>

<article>

<b>02</b>

### Rèn luyện

Nâng cao tư duy và chiến thuật qua luyện tập, thi đấu.

</article>

<article>

<b>03</b>

### Lan tỏa

Mở rộng cộng đồng cờ vua và cờ tướng trong trường.

</article>

</div>

<style>
.pillars b { display: block; font-size: 11px; font-weight: 700; letter-spacing: 0.15em; color: var(--c-blue); }
.pillars h3 { margin-top: 10px; }
</style>

---
layout: content
eyebrow: 10 / Tổng hợp
---

## Tổng hợp hoạt động.

| HOẠT ĐỘNG             | SỐ LƯỢNG | TRẠNG THÁI       |
| --------------------- | -------- | ---------------- |
| Sinh hoạt định kỳ     | 12 buổi  | Hoàn thành       |
| Giải đấu nội bộ       | 02 giải  | Đang triển khai  |
| Giao lưu liên câu lạc bộ | 04 buổi | Đang lên kế hoạch |

---
layout: end
eyebrow: USCC · HẸN GẶP BÀN CỜ
---

# Cảm ơn bạn.

<p class="lead">Hẹn gặp ở ván cờ tiếp theo.</p>
