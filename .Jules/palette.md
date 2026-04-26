## 2024-04-26 - Form Label Associations
**Learning:** Discovered inputs in `contact.html` relying solely on visual proximity to labels without explicit `for`/`id` pairings, which causes screen readers to announce inputs without context.
**Action:** Ensure all forms use explicit `<label for="x">` and `<input id="x">` pairings across the application for screen reader compatibility.
