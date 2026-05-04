## 2024-05-04 - Form Input Accessibility
**Learning:** Standalone pages like `contact.html` were missing explicit `id` and `for` associations on form labels, whereas other components had them. This pattern limits screen reader compatibility and reduces the clickable area for form fields.
**Action:** Always ensure explicit `<label for="x">` and `<input id="x">` pairings are used across all forms to improve both accessibility and general UX.
