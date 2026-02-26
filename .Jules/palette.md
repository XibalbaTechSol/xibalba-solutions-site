## 2025-05-15 - [Mobile Menu Accessibility Pattern]
**Learning:** The mobile hamburger menu lacked `aria-expanded` state management, confusing screen reader users about the menu's state (open/closed).
**Action:** Implemented `aria-expanded` toggle logic in `js/main.js` and updated all HTML files to include `aria-expanded="false"` by default. Verified with Playwright tests.
