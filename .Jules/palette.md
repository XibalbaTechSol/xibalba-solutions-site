## 2026-06-16 - [Added explicit form label associations]
**Learning:** Form inputs were missing explicit `id` attributes and their corresponding `label`s were missing `for` attributes, which breaks screen reader compatibility. Explicit associations are a crucial accessibility standard.
**Action:** Ensure all form inputs across the application use explicit `<label for='x'>` and `<input id='x'>` pairings.
