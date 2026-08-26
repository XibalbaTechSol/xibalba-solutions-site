## 2026-08-07 - Adding Required Indicators to Forms
**Learning:** Found that required input fields in the contact form were missing a visual indicator before submission, despite having the 'required' HTML attribute. This is an accessibility issue because users should not have to attempt form submission to find out which fields are required.
**Action:** Always append an explicit visual indicator (e.g., `<span aria-hidden="true">*</span>`) to labels of required fields, utilizing existing design system classes (like `text-error`).

## 2026-08-26 - Adding explicit disabled states to buttons
**Learning:** Found that buttons did not have explicit `:disabled` states or pointer restrictions in CSS, despite JavaScript manipulating their disabled property. This caused confusing UX where disabled form submission buttons continued to show active pointer cursors and apply transform/shadow hover effects.
**Action:** Always verify that interactive components have defined CSS for their disabled state (e.g. `opacity: 0.6; cursor: not-allowed;`) and that pseudo-classes like `:hover` are scoped with `:not(:disabled)` to prevent false interactivity feedback.
