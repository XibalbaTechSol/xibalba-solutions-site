## 2026-05-10 - Explicit Form Control Pairing Required
**Learning:** Found forms where visual labels were adjacent to inputs but lacked explicit `for` and `id` bindings. This prevents screen readers from announcing the label when the input receives focus, and prevents users from clicking the label to focus the input.
**Action:** Always ensure `<label for="x">` explicitly matches `<input id="x">` across all form elements (inputs, selects, textareas).
