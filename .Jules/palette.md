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
## 2026-10-26 - Keyboard Accessible Mobile Menu Dismissal
**Learning:** The mobile navigation menu lacked support for keyboard dismissal via the Escape key. This forces keyboard and screen reader users to either navigate backwards through all menu items or find the toggle button again to close the menu.
**Action:** Always implement an event listener for the Escape key when building modal or full-screen navigation overlays. When the menu is dismissed via the keyboard, ensure focus is explicitly returned to the trigger button (`hamburger?.focus()`) so users don't lose their place on the page.
## 2026-10-27 - Accessible Scroll Spy Navigation
**Learning:** Using JavaScript to visually toggle an active state on navigation links (e.g., in a scroll spy) without explicitly toggling the `aria-current="true"` attribute leaves screen reader users unaware of the current page section.
**Action:** When implementing visual class changes (like `.active`) for navigation state, always explicitly set or remove the `aria-current="true"` attribute to ensure parity for assistive technologies.
## 2026-10-27 - Aria-Current for Scroll-Spy Navigation
**Learning:** The scroll-spy navigation pattern updated visual link states (`.active`) when sections scrolled into view, but failed to communicate these active state changes to screen reader users because it lacked corresponding ARIA attributes.
**Action:** Always ensure visual state changes for navigation links (e.g., adding `.active` class) are paired with explicitly toggling the `aria-current="true"` attribute to maintain parity for assistive technologies.
## 2026-10-27 - Scroll Spy Navigation Accessibility
**Learning:** The scroll spy functionality visually highlighted active navigation links by toggling the `.active` class, but it failed to programmatically convey this state to screen readers. This resulted in an inaccessible navigation experience for assistive technology users.
**Action:** When using JavaScript to visually toggle an active state on navigation links (e.g., in a scroll spy), always pair the visual class change with explicitly toggling the `aria-current="true"` attribute to ensure parity for screen reader users.
## 2024-10-24 - Accessibility for Scroll Spys
**Learning:** When using JavaScript to visually toggle an active state on navigation links (e.g., in a scroll spy), it's critical to also toggle the `aria-current="true"` attribute to ensure parity for screen reader users.
**Action:** Always pair visual active classes on navigation links with explicitly toggling the `aria-current="true"` attribute.
## 2026-10-27 - Aria-current for visual active states
**Learning:** When using JavaScript to visually toggle an active state on navigation links (e.g., in a scroll spy), always pair the visual class change (e.g., `.active`) with explicitly toggling the `aria-current="true"` attribute to ensure parity for screen reader users.
**Action:** Always toggle the `aria-current="true"` attribute alongside the `.active` class when implementing dynamic active states.
## 2026-10-27 - Dynamic Active Links aria-current Parity
**Learning:** The navigation scroll spy visually updated active links using a `.active` class, but failed to toggle the `aria-current="true"` attribute. This prevents screen reader users from understanding their current position on the page as they navigate.
**Action:** Always pair visual class changes (e.g., `.active`) with explicitly toggling the `aria-current="true"` attribute to ensure parity for screen reader users.
## 2026-10-27 - Async Form Loading State
**Learning:** Submitting forms without a visual loading indicator (e.g. spinner) can cause user uncertainty. Simply changing button text is often not enough visual feedback to indicate an active network request.
**Action:** Always include a visual loading indicator (like a CSS spinner) alongside text changes for async form submissions to improve feedback and reduce user friction.
## 2026-11-08 - Async Form Loading State Spinner
**Learning:** We documented adding a loading spinner, but we didn't document that standard hover effects and animations continue to apply to elements even when they are set to `:disabled` via JavaScript, leading to mixed signals for the user (e.g. they see a spinner, but hovering still highlights the button).
**Action:** When implementing `:disabled` states for interactive elements (like buttons with spinners), explicitly prevent hover states by using `:not(:disabled)` in the CSS selectors for hover effects (e.g., `.btn:not(:disabled):hover`).
