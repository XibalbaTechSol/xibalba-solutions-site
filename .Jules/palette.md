## 2026-04-27 - [Toggle aria-expanded for hamburger menu]
**Learning:** Screen readers need synchronous state updates when visual changes happen to interactive elements like a `.hamburger` toggle button to accurately communicate state changes (e.g., expanded/collapsed menu).
**Action:** When visual states of interactive elements are toggled via JavaScript (e.g., toggling an `.active` class), their associated ARIA attributes (like `aria-expanded`) must be synchronously updated in the same event handler.
