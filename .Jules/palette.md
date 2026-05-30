## 2026-05-30 - aria-expanded toggling for mobile menus
**Learning:** The mobile hamburger menu needs an explicit `aria-expanded` attribute that toggles between true and false to ensure screen readers can understand the current state of the navigation menu.
**Action:** Add `hamburger.setAttribute('aria-expanded', 'true'/'false')` inside the existing javascript open/close handlers.
