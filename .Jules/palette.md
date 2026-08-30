## 2026-08-07 - Adding Required Indicators to Forms
**Learning:** Found that required input fields in the contact form were missing a visual indicator before submission, despite having the 'required' HTML attribute. This is an accessibility issue because users should not have to attempt form submission to find out which fields are required.
**Action:** Always append an explicit visual indicator (e.g., `<span aria-hidden="true">*</span>`) to labels of required fields, utilizing existing design system classes (like `text-error`).

## 2026-08-30 - Disabled Button States
**Learning:** The design system's `.btn` and `.btn-outline` components lacked explicit `:disabled` styling, causing them to maintain hover effects (glow and transform) and pointer cursors even when disabled during async form submissions.
**Action:** Always implement `:disabled` states for interactive elements by setting `opacity: 0.6`, `cursor: not-allowed`, and using `:not(:disabled)` on hover pseudo-classes to prevent interactive feedback on inactive elements.
