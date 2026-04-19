## 2025-03-01 - Form Accessibility in Contact Forms
**Learning:** The contact form elements were missing explicit label associations (`for` and `id` pairings), which breaks screen reader compatibility for visually impaired users.
**Action:** Ensure all new form inputs are paired explicitly with `id` and `for` attributes or `aria-label` when labels are hidden.
