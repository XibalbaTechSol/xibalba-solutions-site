## 2026-05-16 - [Forms Must Use Explicit Label Pairings]
**Learning:** Found multiple form inputs in `contact.html` that lacked explicit label associations, which degrades the experience for screen reader and keyboard users.
**Action:** When auditing forms, ensure every `<label>` has a `for` attribute that correctly points to the corresponding input's `id`.
