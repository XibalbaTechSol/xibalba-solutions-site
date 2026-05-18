## 2024-05-24 - Accessibility insights
**Learning:** Add `aria-expanded` to hamburger menu buttons to improve accessibility for screen readers.
**Action:** When adding `aria-expanded="false"`, make sure it toggles to `aria-expanded="true"` via JavaScript when the menu is opened.
## 2026-05-18 - Added aria-expanded to Hamburger Menu
**Learning:** A visually animated toggle button (hamburger menu) requires an explicit `aria-expanded` attribute that dynamically updates via JavaScript to convey its state to screen readers.
**Action:** Added `aria-expanded="false"` to the initial HTML and added JS logic to toggle it to `true` when the `.active` class is applied.
