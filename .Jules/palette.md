## 2024-05-24 - Initial Journal
**Learning:** Initialized Palette journal for UX/a11y insights.
**Action:** Ready to log critical learnings.

## 2026-06-02 - Dynamic aria-expanded for Mobile Navigation
**Learning:** Found an accessibility issue pattern specific to this app's components: visual states of interactive elements toggled via JavaScript (like the .hamburger menu's .active class) were not synchronously updating their associated ARIA attributes (aria-expanded).
**Action:** Implemented a standard pattern to update aria-expanded in the same event handlers that toggle visual states to ensure screen reader context.
