## 2025-04-02 - Synchronizing ARIA states with visual UI toggles
**Learning:** When visual states of interactive elements (like mobile navigation menus) are toggled via JavaScript, their associated ARIA attributes (like `aria-expanded`) must be synchronously updated in the same event handler to ensure screen reader context.
**Action:** Ensure `aria-expanded` is explicitly updated whenever the `.active` class is toggled on the hamburger button.
