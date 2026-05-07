## 2024-05-24 - Syncing ARIA with Visual States
**Learning:** When toggling visual classes (like `.active`) via JavaScript to open/close interactive menus, screen reader users miss these updates unless the corresponding ARIA attribute (like `aria-expanded`) is synchronously updated in the same event handler.
**Action:** Always pair `classList.add('active')`/`remove('active')` with `setAttribute('aria-expanded', 'true')`/`'false'` on toggleable elements.
