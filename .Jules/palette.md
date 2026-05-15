## 2026-05-24 - Mobile Navigation Missing aria-expanded
**Learning:** Visual state changes on interactive elements (like toggling a `.active` class for a hamburger menu) often lack synchronized ARIA attribute updates, leading to screen reader desync.
**Action:** Always ensure that ARIA attributes (like `aria-expanded`) are synchronously updated within the same JavaScript event handlers that toggle visual states.
