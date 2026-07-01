## 2026-07-01 - Explicit Label Pairings for Contact Form
**Learning:** The contact form elements initially lacked explicit id and for associations, which disrupts screen reader compatibility. This is a common pattern in raw HTML forms without framework wrappers.
**Action:** Always ensure <label> tags have a 'for' attribute matching the 'id' of their associated <input>, <select>, or <textarea> to maintain a11y compliance.
