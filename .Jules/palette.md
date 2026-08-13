## 2026-08-07 - Adding Required Indicators to Forms
**Learning:** Found that required input fields in the contact form were missing a visual indicator before submission, despite having the 'required' HTML attribute. This is an accessibility issue because users should not have to attempt form submission to find out which fields are required.
**Action:** Always append an explicit visual indicator (e.g., `<span aria-hidden="true">*</span>`) to labels of required fields, utilizing existing design system classes (like `text-error`).

## 2026-08-13 - Global Focus Visible Styles
**Learning:** Interactive elements such as links and buttons lacked `:focus-visible` styles, making keyboard navigation difficult to track for users relying on tab navigation.
**Action:** Added global `:focus-visible` styles for `a`, `button`, and `[tabindex="0"]` to ensure a consistent, brand-aligned focus indicator (using `var(--color-brand-primary)`) appears across the site during keyboard navigation.
