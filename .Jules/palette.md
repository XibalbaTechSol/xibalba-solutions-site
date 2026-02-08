## 2025-02-23 - Mobile Navigation Accessibility
**Learning:** Mobile navigation menus implemented with `display: none` by default and toggled via a class (e.g., `.active`) are robust but require explicit `aria-expanded` management in JS for accessibility compliance. The 'hamburger' button needs to be explicitly styled (often using `span` elements) as it is often unstyled by default.
**Action:** When implementing mobile menus, always pair the CSS toggle class with a corresponding `aria-expanded` toggle in the event listener.
