## 2026-05-22 - Explicit Form Control Labelling in Contact Form
**Learning:** Found that the primary contact form (`contact.html`) had implicit labels lacking explicit `for` and `id` bindings. This prevents screen readers from correctly associating the label text with the input field, and users cannot click the label text to focus the inputs.
**Action:** Always ensure `<label>` elements have an explicit `for` attribute that correctly pairs with the `id` of their associated input, select, or textarea, rather than relying solely on visual proximity or implicit nesting.
