## 2025-10-24 - Accessibility on forms
**Learning:** Explicit `for` and `id` attributes should always be used to pair form labels with inputs/selects/textareas for proper screen reader accessibility. This application's `contact.html` was missing these pairs.
**Action:** Always ensure any added form field has a matching explicit `<label for="...">`.
