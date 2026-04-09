## 2026-04-09 - Accessible Form Controls Require Explicit IDs
**Learning:** For forms that rely on semantic HTML structure without framework abstractions, all `<label>` elements must explicitly reference their corresponding input controls via `for`/`id` pairs. Missing these implicitly breaks keyboard navigation spacing algorithms and screen reader functionality, reducing accessibility in custom-styled CSS components.
**Action:** When auditing legacy HTML, enforce explicit `for` and `id` bindings on all form elements even when visually adjacent.

## 2026-04-09 - Global Focus Indicators are Critical for Custom Styling
**Learning:** Adding complex custom CSS styling (like `var(--glass-bg)` or non-standard borders) routinely wipes out standard browser focus outlines. Relying solely on a color change for focus (e.g. `border-color`) is insufficient for a11y compliance.
**Action:** Implement a global `:focus-visible` CSS rule immediately when starting a project with custom styles to guarantee a visible focus ring for keyboard users, targeting interactive components universally (`a`, `button`, `input`, `select`, `textarea`).
