## 2026-08-07 - Adding Required Indicators to Forms
**Learning:** Found that required input fields in the contact form were missing a visual indicator before submission, despite having the 'required' HTML attribute. This is an accessibility issue because users should not have to attempt form submission to find out which fields are required.
**Action:** Always append an explicit visual indicator (e.g., `<span aria-hidden="true">*</span>`) to labels of required fields, utilizing existing design system classes (like `text-error`).

## 2026-09-01 - Disabled States on Interactive Elements
**Learning:** Found that while buttons were programmatically disabled (e.g. during form submission), they lacked a visual indicator, leaving users confused about why they couldn't click.
**Action:** Always include a visual indicator of disabled state. For this application's design system, the pattern is to set `opacity: 0.6`, `cursor: not-allowed`, and explicitly prevent hover states (e.g., using `:not(:disabled)`).
