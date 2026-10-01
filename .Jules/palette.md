## 2026-08-07 - Adding Required Indicators to Forms
**Learning:** Found that required input fields in the contact form were missing a visual indicator before submission, despite having the 'required' HTML attribute. This is an accessibility issue because users should not have to attempt form submission to find out which fields are required.
**Action:** Always append an explicit visual indicator (e.g., `<span aria-hidden="true">*</span>`) to labels of required fields, utilizing existing design system classes (like `text-error`).
## 2026-09-03 - [Disabled Button UX Pattern]
**Learning:** Forms in this application programmatically set buttons to `disabled` during submission (e.g., contact form), but previously lacked visual disabled states, allowing active hover animations (transform/box-shadow) to persist. This creates a confusing UX where elements appear interactive while fundamentally disabled.
**Action:** When implementing disabled states for interactive elements in this design system, explicitly use `:not(:disabled)` for hover states to prevent unwanted animations from overriding disabled styles like `opacity: 0.6` and `cursor: not-allowed`.
## 2026-10-24 - Skip-to-Content Links
**Learning:** The application lacked skip-to-content links, forcing keyboard users to navigate through all navigation items before reaching the main content. This is a critical accessibility issue.
**Action:** Always include a visually hidden skip-to-content link (`<a href="#main-content" class="skip-link">Skip to main content</a>`) immediately after the `<body>` tag, which becomes visible on `:focus`. Ensure the main content area has the corresponding `id="main-content"`.
## 2026-10-25 - Standard Form Autocomplete Attributes
**Learning:** Standard form fields (like Name and Email) in `contact.html` and `index.html` were missing the `autocomplete` attribute. This is an accessibility and UX issue as it fails to leverage browser autofill capabilities to reduce cognitive load and friction for users (WCAG 1.3.5 Identify Input Purpose).
**Action:** Always include appropriate `autocomplete` attributes (e.g., `autocomplete="name"`, `autocomplete="email"`) on standard form input fields.
