## 2024-04-08 - Accessible Mobile Navigation and Focus States
**Learning:** JavaScript-driven visual toggles (like `.active` classes on menus) must synchronously update `aria-expanded` attributes on controlling buttons to provide context to screen readers. Global `:focus-visible` ensures consistent keyboard navigation visibility without disrupting mouse users.
**Action:** Always pair visual state toggles (`classList.toggle`) with ARIA state updates (`setAttribute`) in the same event handler. Define a global `:focus-visible` outline using the secondary brand color and a 4px offset.
