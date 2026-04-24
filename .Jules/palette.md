## 2024-04-24 - Hamburger Menu ARIA Synchronization
**Learning:** The mobile navigation menu visual state was managed via JavaScript class toggling (`.active`), but the associated ARIA attribute (`aria-expanded`) on the trigger button was not synchronously updated, leaving screen readers unaware of the expanded state.
**Action:** When visual states of interactive elements are toggled via JavaScript, their associated ARIA attributes (like `aria-expanded`) must be synchronously updated in the same event handler to ensure screen reader context.
