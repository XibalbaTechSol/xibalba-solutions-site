## 2025-03-01 - Syncing Visual and ARIA states on custom Navigation components
**Learning:** Custom UI components like the hamburger menu often toggle visual classes (e.g., `.active`) but forget to synchronously update screen reader context. Screen readers rely heavily on attributes like `aria-expanded` to understand state changes for toggle buttons.
**Action:** Always ensure that when visual states are toggled via JavaScript on interactive elements, their associated ARIA attributes (like `aria-expanded` or `aria-pressed`) are updated in the same event handler.
