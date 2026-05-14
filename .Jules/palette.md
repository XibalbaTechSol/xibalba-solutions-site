## 2026-05-14 - [Explicit Label Pairings]
**Learning:** Found an accessibility issue pattern where `<label>` elements lack a `for` attribute mapping to their corresponding input `id`s, which breaks screen reader focus and selection interactions.
**Action:** Always ensure all form inputs across the application use explicit `<label for="x">` and `<input id="x">` pairings to guarantee screen reader compatibility.
