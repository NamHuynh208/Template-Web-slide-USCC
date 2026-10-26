# Cài addon HCMUS cho frontend-slides

## 1. Chép template HCMUS

Chép **nguyên thư mục `hcmus`** vào thư mục `templates` của frontend-slides:


...\bold-template-pack\templates\hcmus\
  assets\
  design.md
  preview.md
```

## 2. Đăng ký template trong selection-index.json

Mở file:

```text
...\skills\frontend-slides\bold-template-pack\selection-index.json
```

Thêm object HCMUS vào mảng `templates`:

```json
{
  "slug": "hcmus",
  "name": "HCMUS",
  "tagline": "Official HCMUS academic slide system with original VNUHCM University of Science assets, Inter typography, #2D4C9A text, 36px headers, and 27px body text.",
  "mood": [
    "academic",
    "institutional",
    "trustworthy",
    "Vietnamese university",
    "clean"
  ],
  "tone": [
    "formal",
    "instructional",
    "polished",
    "campus-branded",
    "lecture-ready"
  ],
  "formality": "high",
  "density": "medium",
  "scheme": "light",
  "best_for": "University lectures, course decks, seminar presentations, research briefings, student reports, graduation/institutional content, and any Vietnamese academic presentation that should preserve the HCMUS/ĐHQG-HCM template identity with strict official typography.",
  "avoid_for": "Decks that need a playful, luxury, startup, or non-institutional brand voice; designs where the HCMUS identity should not appear.",
  "preview_md": "bold-template-pack/templates/hcmus/preview.md",
  "design_md": "bold-template-pack/templates/hcmus/design.md"
}
```

## 3. Cài skill convert-template 

Chỉ cần làm bước này nếu muốn dùng lệnh `/custom-frontend-slides:convert-template` để chuyển PowerPoint thành template:

Chép **nguyên thư mục `convert-template`** vào thư mục skills của plugin `frontend-slides` tương ứng:

```text
<USER_HOME>\.claude\plugins\cache\frontend-slides\frontend-slides\<VERSION>\skills\convert-template
```

Sau khi chép xong, thư mục phải có dạng:

```text
...\skills\convert-template\
  SKILL.md
  scripts\
```

## Nội dung addon này

- `hcmus/`: template HCMUS dùng để tạo slide.
- `convert-template/`: skill chuyển file `.pptx`/`.potx` thành template frontend-slides; không cần cài nếu chỉ dùng HCMUS.

Sau khi copy xong, khởi động lại Claude Code rồi dùng frontend-slides như bình thường. Khi chọn template, dùng tên hoặc slug `HCMUS` / `hcmus`.
