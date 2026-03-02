## 2024-05-24 - Required Form Fields Visual Indicator
**Learning:** Users often miss which fields are required when relying solely on HTML5 `required` attributes, which only trigger upon form submission. Visually indicating required fields upfront is a critical UX and accessibility pattern.
**Action:** Always append `.required-label` (which renders an asterisk via `::after`) to the `<label>` of any input that has the `required` attribute to provide immediate visual feedback.
