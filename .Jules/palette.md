## 2024-05-24 - Accessibility states for mobile menu
**Learning:** Visual state changes on interactive elements (like the `.hamburger` menu toggling an `.active` class) must have synchronously updated ARIA attributes (`aria-expanded`) to ensure screen reader context remains accurate.
**Action:** When adding JS to toggle visual states, always add corresponding logic to update relevant ARIA attributes. Added `aria-expanded` initial state to HTML and dynamic updates to `js/main.js`.
