## 2024-05-24 - [Hamburger Menu Accessibility]
**Learning:** Found that the hamburger menu does not update its aria-expanded state when opened/closed. This is a common pattern that makes navigation difficult for screen reader users, as they are not informed of the menu's state.
**Action:** When visual states of interactive elements are toggled via JavaScript (e.g., toggling an .active class), their associated ARIA attributes (like aria-expanded) must be synchronously updated in the same event handler to ensure screen reader context.
