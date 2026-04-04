## 2024-05-15 - Synchronous ARIA State Updates
**Learning:** When visual states of interactive elements like navigation menus are toggled via JavaScript classes (e.g. `.active`), their associated ARIA attributes (like `aria-expanded`) must be synchronously updated in the same event handler to prevent screen reader context loss.
**Action:** Ensure all future UI toggles that affect visual visibility explicitly manage `aria-expanded`, `aria-hidden`, or related ARIA properties in tandem with CSS class changes.
