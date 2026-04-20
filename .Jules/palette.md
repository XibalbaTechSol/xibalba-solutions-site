## 2024-04-20 - Missing aria-expanded on Mobile Nav
**Learning:** The mobile hamburger menu toggles visibility using a CSS class but fails to update the aria-expanded attribute, leaving screen reader users unaware of the menu's state.
**Action:** Update JavaScript to synchronously toggle aria-expanded when the menu opens/closes, and ensure the attribute exists in HTML.
