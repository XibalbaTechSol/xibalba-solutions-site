## 2024-05-15 - Hamburger menu missing aria-expanded
**Learning:** The mobile hamburger menu has `aria-label="Toggle Menu"` but is missing the dynamic `aria-expanded` state which is crucial for screen readers to know if the menu is open or closed.
**Action:** Add `aria-expanded="false"` by default in HTML and dynamically toggle it to `true` when the menu is active in `js/main.js`.
