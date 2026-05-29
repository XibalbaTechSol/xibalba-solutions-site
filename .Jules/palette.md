## 2026-05-29 - [Explicit Label Associations for Screen Readers]
**Learning:** Found forms missing explicit `for` and `id` attributes, specifically the secondary standalone contact page. This degrades screen reader experience as they rely on explicit pairings.
**Action:** Always ensure `<label>` elements are explicitly tied to their input fields using the `for` and `id` attributes, even if they visually appear adjacent.
