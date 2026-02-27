## 2025-02-28 - Dynamic ARIA Attributes for Interactive Elements
**Learning:** Screen readers rely heavily on attributes like `aria-expanded` to communicate the state of collapsible UI components. Static HTML attributes are insufficient for dynamic interactions.
**Action:** Always ensure that JavaScript event listeners for toggleable elements (like menus, accordions, and modals) explicitly update the relevant ARIA attributes to reflect the current state.
