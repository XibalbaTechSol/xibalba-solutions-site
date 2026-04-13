## 2025-04-13 - Form Accessibility: Missing Explicit Labels
**Learning:** Several standard HTML forms in this project's template use visual labels but omit the explicit `for` and `id` attributes, relying implicitly on visual proximity which breaks screen reader context.
**Action:** Always verify that `<label>` elements have a `for` attribute that precisely matches the `id` of the corresponding form input, especially in new form components.
