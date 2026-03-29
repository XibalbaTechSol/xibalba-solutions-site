## 2024-03-29 - Synchronous Visual and ARIA State for Mobile Navigation
**Learning:** When visual states of interactive elements are toggled via JavaScript (e.g., toggling an `.active` class for the hamburger menu), their associated ARIA attributes (like `aria-expanded`) must be synchronously updated in the same event handler to ensure screen reader context is maintained.
**Action:** Always verify that interactive custom components (like mobile menus) toggle both visual class names and corresponding ARIA attributes simultaneously.
