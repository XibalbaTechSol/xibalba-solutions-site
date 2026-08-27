## 2026-08-07 - Adding Required Indicators to Forms
**Learning:** Found that required input fields in the contact form were missing a visual indicator before submission, despite having the 'required' HTML attribute. This is an accessibility issue because users should not have to attempt form submission to find out which fields are required.
**Action:** Always append an explicit visual indicator (e.g., `<span aria-hidden="true">*</span>`) to labels of required fields, utilizing existing design system classes (like `text-error`).

## 2026-08-27 - Adding Disabled States to Interactive Elements
**Learning:** Found that buttons like the form submission button were being disabled programmatically during async operations but lacked corresponding CSS styles (like opacity reduction or cursor change). This causes confusion as the element still appears interactive and retains hover states, which is a poor UX.
**Action:** Always define explicit `:disabled` states (e.g., `opacity: 0.6`, `cursor: not-allowed`) for buttons and interactive elements, and use `:not(:disabled)` pseudo-classes to prevent hover styling from activating on disabled elements.
