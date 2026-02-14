## 2025-02-12 - Missing Labels & Form Usability
**Learning:** Auth forms in `dashboard.html` rely entirely on placeholders and lack `<label>` elements, which is a major accessibility barrier.
**Action:** In future updates, refactor dynamic forms to include explicit `<label>` elements linked to inputs via `for/id`.

## 2025-02-12 - Select Input Usability
**Learning:** Using `style="appearance: none;"` on `<select>` inputs without providing a custom background arrow renders the dropdown indistinguishable from a text input, confusing users.
**Action:** Avoid removing native appearance unless a custom replacement is implemented. For quick fixes, remove the style to restore native usability.
