## 2026-06-26 - Form Accessibility Pattern
**Learning:** Found a recurring pattern in the design system where form labels were visually styled but lacked explicit `for` associations with their inputs, making them unclickable and hidden from screen readers.
**Action:** When adding new forms, always pair `<label for="id">` with `<input id="id">` to ensure the entire visual label is interactive and screen-reader accessible.
