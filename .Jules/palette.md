## 2024-10-10 - Synchronizing ARIA Attributes with CSS State Toggles
**Learning:** Mobile navigation components in this repository use the `.active` CSS class to control visibility but fail to communicate this state to assistive technologies, revealing a pattern where visual state is decoupled from semantic state.
**Action:** Synchronously toggle `aria-expanded` in the same JS function that modifies the `.active` class for the hamburger menu, and ensure all HTML files define an initial `aria-expanded="false"` state.
