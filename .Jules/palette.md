## 2025-05-24 - Missing ARIA State on Interactive Elements
**Learning:** Custom interactive elements (like the hamburger menu) often lack state attributes like `aria-expanded`, making them confusing for screen reader users who don't know if the menu is open or closed.
**Action:** When implementing toggles, always pair visual state changes (like `.active` class) with ARIA state updates (`aria-expanded`, `aria-pressed`) to ensure semantic parity.
