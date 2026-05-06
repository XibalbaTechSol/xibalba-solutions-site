## 2024-05-06 - [Explicit Form Labels in Contact Form]
**Learning:** Found that the main `contact.html` form lacked explicit `<label for="x">` and `<input id="x">` associations, relying only on visual grouping. This degrades both screen reader accessibility and usability for mouse users who expect to focus inputs by clicking their labels.
**Action:** Always ensure all form inputs across the application use explicit `for` and `id` pairings to ensure full screen reader compatibility and improved click targets.
