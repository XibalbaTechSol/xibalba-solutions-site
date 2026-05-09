## 2026-05-09 - Explicit Form Label Association
**Learning:** In this application, forms (like on the contact page) occasionally omit explicit `for` attributes on labels and corresponding `id` attributes on inputs, relying solely on visual proximity. This breaks screen reader compatibility and reduces the clickable target area for users.
**Action:** Always verify that every `<label>` has a `for` attribute and pairs with an `<input id="...">` (or `textarea`/`select`) to guarantee accessibility and better UX.
