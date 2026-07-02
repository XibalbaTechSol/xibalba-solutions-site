## 2026-07-02 - Added missing form element associations in contact form
**Learning:** Found an accessibility issue where <label> elements in contact.html lacked for attributes connecting them to the corresponding form inputs, breaking screen reader association and click-to-focus behavior.
**Action:** Add for attributes to labels and corresponding id attributes to inputs, selects, and textareas.
