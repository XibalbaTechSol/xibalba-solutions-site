## 2026-05-20 - [Standalone forms lack label associations]
**Learning:** Found that while the index page contact form had correct `for` and `id` mappings, the standalone `contact.html` form lacked explicit label-to-input pairings.
**Action:** Always verify all forms, not just the primary ones. Ensured explicit `<label for="x">` and `<input id="x">` pairs are used across all form fields.
