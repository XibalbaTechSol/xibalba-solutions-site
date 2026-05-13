## 2026-05-13 - [Add aria-expanded to hamburger menu]
**Learning:** Visual toggle states (like .active on the hamburger menu) must be accompanied by synchronous updates to ARIA attributes (e.g., aria-expanded) in the event handler to ensure screen reader users are aware of the changing state.
**Action:** Always pair visual state toggles with corresponding ARIA attribute updates in JavaScript, and set the initial ARIA state in the HTML.
