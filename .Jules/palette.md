## 2024-05-18 - Aria-Expanded on Interactive Elements
**Learning:** Visual state toggles (like `.active` classes on a hamburger menu) do not inherently communicate their state to screen readers.
**Action:** Always pair visual class toggles with corresponding ARIA attribute updates (e.g., `aria-expanded="true/false"`) in the same JavaScript event handlers.
