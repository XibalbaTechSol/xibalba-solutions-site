## 2026-06-18 - Explicit Label-Input Pairings
**Learning:** Found that some forms lack explicit `for` and `id` attributes linking labels to inputs, relying only on visual proximity. This breaks accessibility for screen reader users trying to navigate and interact with the form fields accurately.
**Action:** Always ensure all form inputs across the application use explicit `<label for="x">` and `<input id="x">` pairings, or `aria-label` attributes when visual labels are omitted, to guarantee screen reader compatibility.
